#!/usr/bin/env python3
"""Prepare Golden Tasks for the existing Behavioral Harness without evaluator leakage.

The Golden Task definition stays the Judge View. The runner receives:
- the user assignment;
- neutralized fixture paths;
- a curated runtime repository view with operational routing/skill/workflow files;
- no Evals tree, changelog, tests, harness implementation or Golden-Task metadata.

This module prepares packages only. It does not run a model and does not semantically judge output.
"""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path
from typing import Any

import yaml

try:
    from .behavioral_harness import (
        HarnessError,
        assert_runner_package_clean,
        dump_yaml,
        hash_file,
        hash_object,
        verify_prepared_integrity,
    )
except ImportError:
    from behavioral_harness import (
        HarnessError,
        assert_runner_package_clean,
        dump_yaml,
        hash_file,
        hash_object,
        verify_prepared_integrity,
    )

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = 1

ROOT_RUNTIME_FILES = (
    "AGENTS.md",
    "skill-catalog.yml",
    "routing-overlays.yml",
    "workflow-index.yml",
)

RUNTIME_DIRS = (
    "Agentenarbeit",
    "Arbeitsweisen",
    "Bildarbeit",
    "Data-Engineering",
    "Datenbanken",
    "Dokumentationserstellung",
    "Finanzen",
    "Grundlagen",
    "Infrastruktur-und-DevOps",
    "Programmieren",
    "Recherche",
    "Reverse-Engineering-und-Binaeranalyse",
    "Reliability-und-System-Observability",
    "Requirements-und-Spezifikations-Engineering",
    "Schnittstellen-und-Vertraege",
    "Schreiben",
    "Sicherheit",
    "Skill-Engineering",
    "Social-Media-und-Content-Praesenz",
    "Software-Architecture-und-System-Design",
    "Storyentwicklung-und-Fiktion",
    "Testing-und-QA",
    "Webentwicklung",
    "Wissensmanagement",
    "Workflows",
)

EXTRA_RUNTIME_FILES = (
    "Dokumentation/Skill-Handbuch.md",
)

# These files describe eval architecture/results rather than the operational runtime.
RUNTIME_EXCLUDED_RELATIVE = {
    "Agentenarbeit/Agent-Evals.md",
    "Dokumentationserstellung/Visual-Answer-Explorativer-AB-Test-2026-10-06.md",
    "Skill-Engineering/Cross-Cutting-Skill-Discovery.md",
    "Skill-Engineering/Quellen-und-Inspirationen.md",
    "Skill-Engineering/Skill-Review-und-Evals.md",
}

FORBIDDEN_RUNNER_PATH_PARTS = {".git", ".github", "Evals", "tests", "tools"}
FORBIDDEN_RUNNER_ROOT_FILES = {
    "CHANGELOG.md",
    "README.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "START-HIER.md",
}
CONTAMINATION_PATTERN = re.compile(r"\bGT-(?:0[1-9]|1[0-8])\b|Evals/Golden-Tasks|Golden Tasks", re.IGNORECASE)


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise HarnessError(f"cannot load Golden Task {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise HarnessError(f"Golden Task must be a mapping: {path}")
    return data


def _safe_repo_path(raw: str) -> Path:
    path = Path(str(raw))
    if path.is_absolute() or ".." in path.parts:
        raise HarnessError(f"unsafe repository-relative path: {raw}")
    return path


def _fixture_role_map(task: dict[str, Any]) -> dict[str, str]:
    result: dict[str, str] = {}
    for source in task.get("sources_of_truth") or []:
        if isinstance(source, dict) and isinstance(source.get("path"), str):
            result[source["path"]] = str(source.get("role") or "source-of-truth")
    return result


def _neutral_fixture_path(index: int, original: Path) -> str:
    suffix = original.name or f"fixture-{index:02d}"
    return f"workspace/task/fixture-{index:02d}-{suffix}"


def build_fixture_records(task: dict[str, Any], repo_root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    roles = _fixture_role_map(task)
    execution: list[dict[str, Any]] = []
    judge: list[dict[str, Any]] = []
    for index, raw in enumerate(task.get("fixtures") or [], 1):
        original = _safe_repo_path(str(raw))
        source = repo_root / original
        if not source.is_file():
            raise HarnessError(f"Golden Task fixture missing: {original.as_posix()}")
        fixture_id = f"FX-{task['id']}-{index:02d}"
        digest = hash_file(source)
        neutral = _neutral_fixture_path(index, original)
        execution.append({
            "fixture_id": fixture_id,
            "path": neutral,
            "hash": digest,
            "hash_kind": "content",
            "materialization": "available",
        })
        judge.append({
            "fixture_id": fixture_id,
            "path": neutral,
            "original_path": original.as_posix(),
            "hash": digest,
            "hash_kind": "content",
            "materialization": "available",
            "role": roles.get(original.as_posix(), "task-fixture"),
            "intentionally_missing_evidence": [],
        })
    return execution, judge


def normalize_workflow(task: dict[str, Any]) -> dict[str, Any]:
    raw = task.get("workflow") or {}
    if not isinstance(raw, dict):
        return {"mode": "none", "allowed": []}
    allowed = [str(x) for x in raw.get("allowed") or []]
    if raw.get("required") is True:
        return {"mode": "required", "allowed": allowed}
    return {"mode": "optional" if allowed else "none", "allowed": allowed}


def compile_task(task_path: Path, repo_root: Path, repo_commit: str) -> dict[str, Any]:
    task = load_yaml(task_path)
    task_id = str(task.get("id") or "").strip()
    assignment = str(task.get("assignment") or "").strip()
    if not task_id or not assignment:
        raise HarnessError("Golden Task requires id and assignment")

    exec_fixtures, judge_fixtures = build_fixture_records(task, repo_root)
    required = [str(x) for x in task.get("required_skills") or []]
    optional = [str(x) for x in task.get("allowed_optional_skills") or []]
    forbidden = [str(x) for x in task.get("forbidden_skills") or []]
    routing_mode = str(task.get("behavioral_routing_mode") or "discovery-required")
    if routing_mode not in {"discovery-required", "outcome-primary"}:
        raise HarnessError(f"unsupported behavioral_routing_mode: {routing_mode!r}")
    execution_mode = str(task.get("behavioral_execution_mode") or "read-only")
    if execution_mode not in {"read-only", "writable"}:
        raise HarnessError(f"unsupported behavioral_execution_mode: {execution_mode!r}")

    execution = {
        "schema_version": SCHEMA_VERSION,
        "test_id": task_id,
        "repository": "Borstwerk/KI-Regeln",
        "repo_commit": repo_commit,
        "user_prompt": assignment,
        "fixtures": exec_fixtures,
        "sources": [],
        "runtime": {
            "fresh_runner_context_required": True,
            "execution_mode": execution_mode,
            "allowed_tools": (
                "read-only-discovery"
                if execution_mode == "read-only"
                else "writable-isolated-runner-required"
            ),
            "runner_adapter_required": True,
            "bootstrap_files": ["workspace/repository/AGENTS.md"],
            "repository_view": "workspace/repository",
            "subject_sources": [item["path"] for item in exec_fixtures],
            "task_workspace": "workspace/task",
            "workspace_is_curated": True,
        },
    }

    judge = {
        "schema_version": SCHEMA_VERSION,
        "test_id": task_id,
        "domain": task.get("expected_domain"),
        "task_family": "Golden Task",
        "difficulty": "unknown",
        "test_levels": ["golden-task", "behavioral"],
        "route_kind": "no-skill" if not required else "skill",
        "expected_primary_skill": required[0] if required else "none/direct-response",
        "required_skills": required,
        "allowed_skills": optional,
        "routing_evaluation": {
            "mode": routing_mode,
            "required_skill_read_enforced": routing_mode == "discovery-required",
            "note": (
                "Skill discovery is part of the behavioral contract."
                if routing_mode == "discovery-required"
                else "Judge outcome and boundaries first; a missing skill-file read alone is not a routing failure."
            ),
        },
        "execution_requirements": {
            "mode": execution_mode,
            "default_read_only_adapter_compatible": execution_mode == "read-only",
        },
        "forbidden_skills": forbidden,
        "expected_workflow": normalize_workflow(task),
        "expected_status": task.get("expected_status"),
        "expected_evidence": task.get("expected_evidence") or [],
        "failure_modes": task.get("forbidden_behaviors") or [],
        "output_criteria": task.get("expected_artifacts") or [],
        "routing_criteria": ((task.get("rubric") or {}).get("routing") or []),
        "evaluation_method": "Golden Task Judge View",
        "blindness_class": "B1-curated-runtime-view",
        "fixtures": judge_fixtures,
        "authoritative_sources": [
            item["fixture_id"] for item in judge_fixtures
            if item.get("role") not in {"task-fixture", "unknown"}
        ],
        "intentionally_missing_evidence": [],
        "authorization_expectations": "unknown",
        "golden_task_expectations": {
            "allowed_secondary_domains": task.get("allowed_secondary_domains") or [],
            "expected_verification": task.get("expected_verification") or [],
            "allowed_uncertainty": task.get("allowed_uncertainty") or [],
            "rubric": task.get("rubric") or {},
        },
    }

    hashes = {
        "hash_algorithm": "sha256/canonical-json-v1",
        "case_definition_hash": hash_object(task),
        "execution_view_hash": hash_object(execution),
        "judge_view_hash": hash_object(judge),
        "fixture_hashes": {item["fixture_id"]: item["hash"] for item in exec_fixtures},
    }
    return {"task": task, "execution_view": execution, "judge_view": judge, "hashes": hashes}


def _copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def _copy_runtime_repository(repo_root: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=False)

    for raw in ROOT_RUNTIME_FILES:
        source = repo_root / raw
        if not source.is_file():
            raise HarnessError(f"runtime bootstrap file missing: {raw}")
        _copy_file(source, destination / raw)

    for raw in EXTRA_RUNTIME_FILES:
        source = repo_root / raw
        if not source.is_file():
            raise HarnessError(f"runtime router file missing: {raw}")
        _copy_file(source, destination / raw)

    for dirname in RUNTIME_DIRS:
        source_root = repo_root / dirname
        if not source_root.is_dir():
            continue
        for source in sorted(source_root.rglob("*")):
            if not source.is_file():
                continue
            rel = source.relative_to(repo_root)
            rel_text = rel.as_posix()
            if rel_text in RUNTIME_EXCLUDED_RELATIVE:
                continue
            if source.name == "README.md":
                continue
            _copy_file(source, destination / rel)


def _workspace_hashes(workspace: Path) -> dict[str, str]:
    return {
        path.relative_to(workspace).as_posix(): hash_file(path)
        for path in sorted(workspace.rglob("*"))
        if path.is_file()
    }


def assert_curated_workspace_clean(repository_view: Path) -> None:
    if not repository_view.is_dir():
        raise HarnessError("curated repository view is missing")

    violations: list[str] = []
    for path in repository_view.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(repository_view)
        rel_text = rel.as_posix()
        if set(rel.parts) & FORBIDDEN_RUNNER_PATH_PARTS:
            violations.append(f"forbidden evaluator/runtime path: {rel_text}")
            continue
        if len(rel.parts) == 1 and rel.name in FORBIDDEN_RUNNER_ROOT_FILES:
            violations.append(f"forbidden root metadata: {rel_text}")
            continue
        if rel_text in RUNTIME_EXCLUDED_RELATIVE:
            violations.append(f"eval-describing operational doc: {rel_text}")
            continue
        if path.suffix.lower() in {".md", ".yml", ".yaml", ".json", ".txt"}:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if CONTAMINATION_PATTERN.search(text):
                violations.append(f"Golden-Task routing hint: {rel_text}")

    if violations:
        raise HarnessError(
            "runner repository contamination detected:\n- " + "\n- ".join(sorted(violations))
        )


def write_prepared_case(compiled: dict[str, Any], task_path: Path, repo_root: Path, out_dir: Path) -> None:
    if out_dir.exists():
        raise HarnessError(f"output directory already exists: {out_dir}")
    out_dir.mkdir(parents=True)

    execution = compiled["execution_view"]
    judge = compiled["judge_view"]
    hashes = dict(compiled["hashes"])

    dump_yaml(execution, out_dir / "execution-view.yml")
    dump_yaml(judge, out_dir / "judge-view.yml")

    runner = out_dir / "runner-package"
    runner.mkdir()
    dump_yaml(execution, runner / "execution-view.yml")

    adapter_request = {
        "schema_version": 1,
        "contract": "behavioral-runner-adapter/v1",
        "fresh_context_required": True,
        "input": "execution-view.yml",
        "outputs": {
            "runner_output": "runner-output.md",
            "trace": "trace.yml",
            "actions": "actions.yml",
            "evidence": "evidence.yml",
        },
        "rules": [
            "Do not expose judge-view.yml or evaluator-only expectations to the runner.",
            "Use only the supplied curated repository view and task fixtures.",
            "Do not infer selected/applied skills from runner self-report.",
            "Use unknown when telemetry is unavailable.",
        ],
    }
    dump_yaml(adapter_request, runner / "adapter-request.yml")

    workspace = runner / "workspace"
    repository_view = workspace / "repository"
    task_view = workspace / "task"
    _copy_runtime_repository(repo_root, repository_view)
    task_view.mkdir(parents=True, exist_ok=True)

    original_fixtures = compiled["task"].get("fixtures") or []
    for index, raw in enumerate(original_fixtures, 1):
        original = _safe_repo_path(str(raw))
        neutral = Path(_neutral_fixture_path(index, original))
        _copy_file(repo_root / original, runner / neutral)

    assert_curated_workspace_clean(repository_view)
    assert_runner_package_clean(runner)

    workspace_files = _workspace_hashes(workspace)
    hashes["runner_workspace"] = {
        "contract": "golden-task-curated-workspace/v1",
        "dir": "workspace",
        "file_count": len(workspace_files),
        "files": workspace_files,
        "tree_hash": hash_object(workspace_files),
        "excluded_surfaces": [
            "Evals/**",
            ".git/**",
            ".github/**",
            "tests/**",
            "tools/**",
            "CHANGELOG.md",
            "README.md",
            "Dokumentation/Skill-Katalog.md",
            "Agentenarbeit/Agent-Evals.md",
            "Dokumentationserstellung/Visual-Answer-Explorativer-AB-Test-2026-10-06.md",
            "Skill-Engineering/Cross-Cutting-Skill-Discovery.md",
            "Skill-Engineering/Quellen-und-Inspirationen.md",
            "Skill-Engineering/Skill-Review-und-Evals.md",
        ],
    }

    execution_mode = str((execution.get("runtime") or {}).get("execution_mode") or "read-only")
    default_compatible = execution_mode == "read-only"
    readiness = {
        "schema_version": 1,
        "task_id": execution["test_id"],
        "fixtures_materialized": True,
        "blind_execution_view": True,
        "curated_repository_view": True,
        "evaluator_tree_excluded": True,
        "required_execution_mode": execution_mode,
        "default_read_only_runner_compatible": default_compatible,
        "ready_for_behavioral_execution": default_compatible,
        "blocker": (
            None
            if default_compatible
            else "writable task requires an admitted isolated writable runner; the default Claude adapter is read-only"
        ),
    }
    dump_yaml(hashes, out_dir / "hashes.yml")
    dump_yaml(readiness, out_dir / "readiness.yml")
    verify_prepared_integrity(out_dir)


def prepare(task: Path, repo_root: Path, repo_commit: str, out: Path) -> Path:
    task = task.resolve()
    repo_root = repo_root.resolve()
    compiled = compile_task(task, repo_root, repo_commit)
    write_prepared_case(compiled, task, repo_root, out.resolve())
    return out.resolve()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    prep = sub.add_parser("prepare-case", help="Build a blind Golden-Task runner/judge package.")
    prep.add_argument("task", help="Path to GT-XX/task.yml")
    prep.add_argument("--repo-root", default=str(ROOT))
    prep.add_argument("--repo-commit", required=True)
    prep.add_argument("--out", required=True)

    args = parser.parse_args()
    try:
        if args.command == "prepare-case":
            result = prepare(Path(args.task), Path(args.repo_root), args.repo_commit, Path(args.out))
            print(result)
            return 0
    except HarnessError as exc:
        print(f"GOLDEN_HARNESS_ERROR: {exc}")
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
