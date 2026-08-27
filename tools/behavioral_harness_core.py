#!/usr/bin/env python3
"""Technical behavioral-test harness for KI-Regeln.

The harness compiles evaluator-hidden execution views, records only observable
telemetry, evaluates deterministic tri-state gates, validates versioned schema
contracts, and packages immutable judge inputs. It does not run semantic
judging and does not infer private model state.
"""
from __future__ import annotations

import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover - dependency failure is surfaced as HarnessError
    Draft202012Validator = None

ROOT = Path(__file__).resolve().parents[1]
HARNESS_DIR = ROOT / "Evals" / "Behavioral-Harness"
SCHEMA_DIR = HARNESS_DIR / "schemas"
PILOT_SOURCE_LOCK = HARNESS_DIR / "pilot-source-lock.yml"
DEFAULT_FIXTURE_ROLES = HARNESS_DIR / "fixture-role-overrides.yml"
HARNESS_VERSION = "1.1.0"
SCHEMA_VERSION = 1
TRI_UNKNOWN = "unknown"
STATUS_VALUES = {"pass", "partial", "blocked", "fail", "unverifiable"}
RISK_CLASSES = {"productive", "external", "destructive"}
RELIABLE_SKILL_EVENT_SOURCES = {
    "read": {"tool-observation", "replay"},
    "selected": {"orchestrator", "replay"},
    "applied": {"orchestrator", "replay"},
}
SCHEMA_FILES = {
    "trace": "trace.schema.json",
    "actions": "actions.schema.json",
    "evidence": "evidence.schema.json",
    "manifest": "manifest.schema.json",
    "deterministic-gates": "deterministic-gates.schema.json",
    "judge-input": "judge-input.schema.json",
    "runner-adapter": "runner-adapter.schema.json",
}
EVALUATOR_ONLY_EXECUTION_KEYS = {
    "route_kind",
    "expected_primary_skill",
    "required_skills",
    "allowed_skills",
    "forbidden_skills",
    "expected_workflow",
    "expected_status",
    "failure_modes",
    "output_criteria",
    "routing_criteria",
    "authoritative_sources",
    "intentionally_missing_evidence",
    "authorization_expectations",
    "erwarteter_primaerskill",
    "erlaubte_secondary_skills",
    "verbotene_skills",
    "erwarteter_workflow",
    "erwarteter_status",
    "output_kriterien",
    "routing_kriterien",
}


class HarnessError(RuntimeError):
    pass


def load_yaml(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as fh:
            return yaml.safe_load(fh)
    except OSError as exc:
        raise HarnessError(f"cannot read {path}: {exc}") from exc
    except yaml.YAMLError as exc:
        raise HarnessError(f"invalid YAML in {path}: {exc}") from exc


def dump_yaml(data: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        yaml.safe_dump(data, fh, allow_unicode=True, sort_keys=False)


def canonical_bytes(data: Any) -> bytes:
    return json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    ).encode("utf-8")


def hash_object(data: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_bytes(data)).hexdigest()


def hash_bytes(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def hash_file(path: Path) -> str:
    return hash_bytes(path.read_bytes())


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def tri(value: Any) -> bool | str:
    if value is True or value is False or value == TRI_UNKNOWN:
        return value
    if value is None:
        return TRI_UNKNOWN
    raise HarnessError(f"invalid tri-state value: {value!r}")


def tri_all(values: Iterable[bool | str]) -> bool | str:
    vals = list(values)
    if not vals:
        return True
    if False in vals:
        return False
    if TRI_UNKNOWN in vals:
        return TRI_UNKNOWN
    return True


def tri_any(values: Iterable[bool | str]) -> bool | str:
    vals = list(values)
    if True in vals:
        return True
    if TRI_UNKNOWN in vals:
        return TRI_UNKNOWN
    return False


def load_schema(schema_name: str) -> dict[str, Any]:
    if schema_name not in SCHEMA_FILES:
        raise HarnessError(f"unknown schema contract: {schema_name}")
    path = SCHEMA_DIR / SCHEMA_FILES[schema_name]
    if not path.is_file():
        raise HarnessError(f"schema contract missing: {path}")
    try:
        schema = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise HarnessError(f"cannot load schema {path}: {exc}") from exc
    if Draft202012Validator is None:
        raise HarnessError("jsonschema dependency is required for behavioral harness schema enforcement")
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        raise HarnessError(f"invalid harness schema {schema_name}: {exc}") from exc
    return schema


def validate_document(document: Any, schema_name: str, label: str | None = None) -> None:
    schema = load_schema(schema_name)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(document), key=lambda e: list(e.absolute_path))
    if not errors:
        return
    error = errors[0]
    location = "$"
    if error.absolute_path:
        location += "".join(
            f"[{part}]" if isinstance(part, int) else f".{part}"
            for part in error.absolute_path
        )
    raise HarnessError(
        f"{label or schema_name} violates {schema_name} schema at {location}: {error.message}"
    )


def normalize_status(value: Any) -> str:
    if value is None:
        return "unverifiable"
    text = str(value).strip().lower()
    aliases = {
        "success": "pass",
        "passed": "pass",
        "ok": "pass",
        "complete": "pass",
        "completed": "pass",
        "incomplete": "partial",
        "stop": "blocked",
        "stopped": "blocked",
        "unknown": "unverifiable",
    }
    text = aliases.get(text, text)
    return text if text in STATUS_VALUES else "unverifiable"


def is_no_skill(primary: Any) -> bool:
    if primary is None:
        return True
    text = str(primary).strip().lower()
    return text in {"", "none", "none/direct-response", "direct-response", "no-skill"}


def normalize_route(case: dict[str, Any]) -> tuple[str, list[str], list[str], list[str]]:
    primary = case.get("erwarteter_primaerskill")
    primary_text = "" if primary is None else str(primary).strip()
    primary_lower = primary_text.lower()

    if primary_lower == "capability-gap":
        route_kind = "capability-gap"
        required: list[str] = []
    elif is_no_skill(primary):
        route_kind = "no-skill"
        required = []
    else:
        route_kind = "skill"
        required = [primary_text]

    raw_allowed = case.get("erlaubte_secondary_skills", []) or []
    raw_forbidden = case.get("verbotene_skills", []) or []
    if not isinstance(raw_allowed, list) or not isinstance(raw_forbidden, list):
        raise HarnessError("secondary/forbidden skill declarations must be lists")
    allowed = [str(x) for x in raw_allowed]
    forbidden = [str(x) for x in raw_forbidden]
    return route_kind, required, allowed, forbidden


def _none_workflow_text(text: str) -> bool:
    lower = text.strip().lower()
    if lower in {"", "none", "kein workflow", "no workflow"}:
        return True
    if lower.startswith(("kein ", "keine ", "keinen ", "no ")) and "workflow" in lower:
        return True
    return False


def normalize_workflow(value: Any) -> dict[str, Any]:
    """Normalize matrix workflow semantics without modifying the source matrix."""
    if value is None:
        return {"mode": "none", "allowed": []}

    if isinstance(value, dict):
        mode = str(value.get("mode", "")).strip().lower()
        allowed = value.get("allowed", []) or []
        if mode not in {"required", "optional", "none"}:
            raise HarnessError(f"invalid workflow mode: {mode!r}")
        if not isinstance(allowed, list):
            raise HarnessError("workflow allowed must be a list")
        normalized = [str(x).strip() for x in allowed if str(x).strip()]
        if mode == "none":
            return {"mode": "none", "allowed": []}
        if any(_none_workflow_text(x) for x in normalized):
            raise HarnessError("negative workflow declaration cannot be used as an allowed workflow")
        return {"mode": mode, "allowed": normalized}

    text = str(value).strip()
    if _none_workflow_text(text):
        return {"mode": "none", "allowed": []}

    lower = text.lower()
    mode = "required"
    candidate = text
    optional_suffixes = (" (optional)", " [optional]", " optional")
    for suffix in optional_suffixes:
        if lower.endswith(suffix):
            candidate = text[: -len(suffix)].strip()
            mode = "optional"
            break
    if lower.startswith("optional:"):
        candidate = text.split(":", 1)[1].strip()
        mode = "optional"

    if _none_workflow_text(candidate):
        return {"mode": "none", "allowed": []}
    if not candidate:
        return {"mode": "none", "allowed": []}
    return {"mode": mode, "allowed": [candidate]}


def load_matrix(path: Path) -> dict[str, Any]:
    data = load_yaml(path)
    if not isinstance(data, dict) or not isinstance(data.get("tests"), list):
        raise HarnessError("pilot matrix must be a mapping with tests[]")
    return data


def verify_locked_matrix(path: Path, matrix: dict[str, Any], lock_path: Path = PILOT_SOURCE_LOCK) -> None:
    if not lock_path.is_file():
        raise HarnessError(f"pilot source lock missing: {lock_path}")
    lock = load_yaml(lock_path)
    expected = str((lock.get("artifacts") or {}).get("KI-Regeln-Pilot-Testmatrix.yml", {}).get("sha256", ""))
    actual = hash_file(path)
    if not expected:
        raise HarnessError("pilot source lock has no matrix sha256")
    if actual != expected:
        raise HarnessError(f"pilot matrix hash mismatch: expected {expected}, got {actual}")
    expected_count = int(lock.get("expected_test_count", 50))
    actual_count = len(matrix.get("tests", []))
    if actual_count != expected_count:
        raise HarnessError(f"pilot matrix test count mismatch: expected {expected_count}, got {actual_count}")


def get_case(matrix: dict[str, Any], test_id: str) -> dict[str, Any]:
    matches = [c for c in matrix["tests"] if c.get("test_id") == test_id]
    if len(matches) != 1:
        raise HarnessError(f"expected exactly one case {test_id}, found {len(matches)}")
    return copy.deepcopy(matches[0])


def _safe_rel(path_text: str) -> Path | None:
    p = Path(path_text)
    if p.is_absolute() or ".." in p.parts:
        return None
    return p


def _fixture_role(overrides: dict[str, Any], test_id: str, declared: str, index: int) -> tuple[str, list[str]]:
    if isinstance(overrides, dict) and isinstance(overrides.get("cases"), dict):
        overrides = overrides["cases"]
    case_overrides = overrides.get(test_id, {}) if isinstance(overrides, dict) else {}
    item = None
    if isinstance(case_overrides, dict):
        item = case_overrides.get(declared) or case_overrides.get(str(index))
    if not isinstance(item, dict):
        return "unknown", []
    role = str(item.get("role", "unknown"))
    missing = item.get("intentionally_missing_evidence", [])
    return role, [str(x) for x in missing] if isinstance(missing, list) else []


def build_fixture_records(case: dict[str, Any], repo_root: Path, role_overrides: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    role_overrides = role_overrides or {}
    records: list[dict[str, Any]] = []
    declared_fixtures = case.get("fixtures", [])
    if not isinstance(declared_fixtures, list):
        raise HarnessError("case fixtures must be a list")
    for index, raw in enumerate(declared_fixtures, start=1):
        declared = str(raw)
        if declared.strip().lower() in {"none", ""}:
            continue
        rel = _safe_rel(declared)
        abs_path = repo_root / rel if rel else None
        available = bool(abs_path and abs_path.is_file())
        if available:
            fixture_hash = hash_file(abs_path)
            integrity_kind = "content"
            materialization = "available"
            path_value: str | None = rel.as_posix()
        else:
            fixture_hash = hash_object({"declared_fixture": declared})
            integrity_kind = "declaration"
            materialization = "declared-only"
            path_value = declared
        role, intentionally_missing = _fixture_role(role_overrides, str(case["test_id"]), declared, index)
        records.append({
            "fixture_id": f"FX-{case['test_id']}-{index:02d}",
            "path": path_value,
            "hash": fixture_hash,
            "hash_kind": integrity_kind,
            "materialization": materialization,
            "role": role,
            "intentionally_missing_evidence": intentionally_missing,
        })
    return records


def execution_fixture_view(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    allowed = ("fixture_id", "path", "hash", "hash_kind", "materialization")
    return [{k: rec[k] for k in allowed} for rec in records]


def compile_case(matrix: dict[str, Any], test_id: str, repo_root: Path, repo_commit: str | None = None, role_overrides: dict[str, Any] | None = None) -> dict[str, Any]:
    case = get_case(matrix, test_id)
    pinned = str(matrix.get("pinned_commit", "unknown"))
    repo_commit = repo_commit or pinned
    fixtures = build_fixture_records(case, repo_root, role_overrides)
    route_kind, required, allowed, forbidden = normalize_route(case)
    workflow = normalize_workflow(case.get("erwarteter_workflow"))

    execution = {
        "schema_version": SCHEMA_VERSION,
        "test_id": test_id,
        "repository": str(matrix.get("repository", "Borstwerk/KI-Regeln")),
        "repo_commit": repo_commit,
        "user_prompt": case.get("nutzerprompt"),
        "fixtures": execution_fixture_view(fixtures),
        "sources": [],
        "runtime": {
            "fresh_runner_context_required": True,
            "allowed_tools": "normal-runner-tools",
            "runner_adapter_required": True,
        },
    }
    leaked = set(execution) & EVALUATOR_ONLY_EXECUTION_KEYS
    if leaked:
        raise HarnessError(f"evaluator-only keys leaked into execution view: {sorted(leaked)}")

    intentionally_missing: list[str] = []
    for rec in fixtures:
        intentionally_missing.extend(rec["intentionally_missing_evidence"])

    judge = {
        "schema_version": SCHEMA_VERSION,
        "test_id": test_id,
        "domain": case.get("domain"),
        "task_family": case.get("aufgabenfamilie"),
        "difficulty": case.get("schwierigkeit"),
        "test_levels": case.get("testebenen", []),
        "route_kind": route_kind,
        "expected_primary_skill": case.get("erwarteter_primaerskill"),
        "required_skills": required,
        "allowed_skills": allowed,
        "forbidden_skills": forbidden,
        "expected_workflow": workflow,
        "expected_status": normalize_status(case.get("erwarteter_status")),
        "expected_evidence": case.get("erwartete_evidence", []),
        "failure_modes": case.get("failure_modes", []),
        "output_criteria": case.get("output_kriterien", []),
        "routing_criteria": case.get("routing_kriterien", []),
        "evaluation_method": case.get("bewertungsmethode"),
        "blindness_class": case.get("blindness_klasse"),
        "fixtures": fixtures,
        "authoritative_sources": [rec["fixture_id"] for rec in fixtures if rec["role"] == "authoritative-source"],
        "intentionally_missing_evidence": intentionally_missing,
        "authorization_expectations": "unknown",
    }
    hashes = {
        "hash_algorithm": "sha256/canonical-json-v1",
        "case_definition_hash": hash_object(case),
        "execution_view_hash": hash_object(execution),
        "judge_view_hash": hash_object(judge),
        "fixture_hashes": {rec["fixture_id"]: rec["hash"] for rec in fixtures},
    }
    readiness = {
        "all_fixture_content_materialized": all(rec["materialization"] == "available" for rec in fixtures),
        "all_fixture_roles_curated": all(rec["role"] != "unknown" for rec in fixtures),
        "ready_for_behavioral_execution": all(rec["materialization"] == "available" and rec["role"] != "unknown" for rec in fixtures),
    }
    return {"case": case, "execution_view": execution, "judge_view": judge, "hashes": hashes, "readiness": readiness}


def write_prepared_case(compiled: dict[str, Any], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=False)
    dump_yaml(compiled["execution_view"], out_dir / "execution-view.yml")
    dump_yaml(compiled["judge_view"], out_dir / "judge-view.yml")
    dump_yaml(compiled["hashes"], out_dir / "hashes.yml")
    dump_yaml(compiled["readiness"], out_dir / "readiness.yml")

    runner_dir = out_dir / "runner-package"
    runner_dir.mkdir()
    dump_yaml(compiled["execution_view"], runner_dir / "execution-view.yml")
    adapter_request = {
        "schema_version": SCHEMA_VERSION,
        "contract": "behavioral-runner-adapter/v1",
        "fresh_context_required": True,
        "input": "execution-view.yml",
        "outputs": {"runner_output": "runner-output.md", "trace": "trace.yml", "actions": "actions.yml", "evidence": "evidence.yml"},
        "rules": [
            "Do not expose judge-view.yml or evaluator-only expectations to the runner.",
            "Do not infer selected/applied skills from runner self-report.",
            "Use unknown when telemetry is unavailable.",
        ],
    }
    dump_yaml(adapter_request, runner_dir / "adapter-request.yml")
    assert_runner_package_clean(runner_dir)


def assert_runner_package_clean(runner_dir: Path) -> None:
    forbidden_names = {"judge-view.yml", "judge-input.yml"}
    names = {p.name for p in runner_dir.rglob("*") if p.is_file()}
    if names & forbidden_names:
        raise HarnessError(f"judge artifact leaked into runner package: {sorted(names & forbidden_names)}")
    for path in runner_dir.rglob("*.yml"):
        data = load_yaml(path)
        if isinstance(data, dict):
            leaked = set(data) & EVALUATOR_ONLY_EXECUTION_KEYS
            if leaked:
                raise HarnessError(f"evaluator-only fields leaked into runner package {path}: {sorted(leaked)}")


def _fixture_hash_map(records: Any) -> dict[str, str]:
    if not isinstance(records, list):
        raise HarnessError("fixture records must be a list")
    out: dict[str, str] = {}
    for rec in records:
        if not isinstance(rec, dict) or not rec.get("fixture_id") or not rec.get("hash"):
            raise HarnessError("fixture record missing fixture_id/hash")
        out[str(rec["fixture_id"])] = str(rec["hash"])
    return out


def verify_prepared_integrity(prepared_dir: Path) -> dict[str, Any]:
    execution_path = prepared_dir / "execution-view.yml"
    judge_path = prepared_dir / "judge-view.yml"
    hashes_path = prepared_dir / "hashes.yml"
    for path in (execution_path, judge_path, hashes_path):
        if not path.is_file():
            raise HarnessError(f"prepared artifact missing: {path}")

    execution = load_yaml(execution_path)
    judge = load_yaml(judge_path)
    hashes = load_yaml(hashes_path)
    if not all(isinstance(x, dict) for x in (execution, judge, hashes)):
        raise HarnessError("prepared execution/judge/hashes documents must be mappings")

    for label, document, key in (("execution-view", execution, "execution_view_hash"), ("judge-view", judge, "judge_view_hash")):
        expected = hashes.get(key)
        actual = hash_object(document)
        if not expected or actual != expected:
            raise HarnessError(f"prepared {label} hash mismatch: expected {expected!r}, got {actual}")

    if execution.get("test_id") != judge.get("test_id"):
        raise HarnessError("prepared execution/judge test_id mismatch")

    expected_fixtures = hashes.get("fixture_hashes", {})
    if not isinstance(expected_fixtures, dict):
        raise HarnessError("prepared fixture_hashes must be a mapping")
    exec_fixtures = _fixture_hash_map(execution.get("fixtures", []))
    judge_fixtures = _fixture_hash_map(judge.get("fixtures", []))
    if exec_fixtures != expected_fixtures or judge_fixtures != expected_fixtures:
        raise HarnessError("prepared fixture hash relationship mismatch")

    runner_exec_path = prepared_dir / "runner-package" / "execution-view.yml"
    if runner_exec_path.is_file():
        runner_execution = load_yaml(runner_exec_path)
        if hash_object(runner_execution) != hashes["execution_view_hash"]:
            raise HarnessError("runner-package execution-view hash mismatch")
        assert_runner_package_clean(prepared_dir / "runner-package")

    return {"execution": execution, "judge": judge, "hashes": hashes}
