#!/usr/bin/env python3
"""Deterministic, read-only structural validator for KI-Regeln."""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []


def err(code: str, msg: str) -> None:
    ERRORS.append(f"{code}: {msg}")


def warn(code: str, msg: str) -> None:
    WARNINGS.append(f"{code}: {msg}")


def load_yaml(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as fh:
            return yaml.safe_load(fh)
    except Exception as exc:
        err("YAML", f"{path.relative_to(ROOT)}: {exc}")
        return None


def normalize_schema_value(value: Any) -> Any:
    """Convert YAML-native date values for JSON Schema validation only."""
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: normalize_schema_value(item) for key, item in value.items()}
    if isinstance(value, list):
        return [normalize_schema_value(item) for item in value]
    return value


def validate_schema(data: Any, schema_path: Path, label: str) -> None:
    schema = load_yaml(schema_path)
    if schema is None or data is None:
        return
    normalized = normalize_schema_value(data)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for issue in sorted(validator.iter_errors(normalized), key=lambda e: list(e.absolute_path)):
        loc = ".".join(str(x) for x in issue.absolute_path) or "<root>"
        err("SCHEMA", f"{label} [{loc}]: {issue.message}")


def frontmatter(path: Path) -> tuple[dict[str, Any] | None, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return None, text
    try:
        data = yaml.safe_load("\n".join(lines[1:end])) or {}
    except Exception as exc:
        err("FRONTMATTER", f"{path.relative_to(ROOT)}: invalid YAML: {exc}")
        return None, text
    return data if isinstance(data, dict) else None, text


def trigger_description(desc: str) -> bool:
    return bool(re.search(r"\b(verwend(?:en|e)|nutze|geeignet|wenn|falls|bei\s+(?:einem|einer|neuen|bestehenden|fragen|anfragen)|use\s+when|for\s+(?:requests|tasks|cases))\b", desc, re.I))


def near_miss_signal(text: str) -> bool:
    return bool(re.search(r"\b(nicht\s+(?:verwenden|geeignet|für)|wann\s+nicht|abgrenzung|near[- ]miss|do\s+not\s+use|not\s+for)\b", text, re.I))


def validate_skills(catalog: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], int]:
    items = catalog.get("skills") or []
    by_id: dict[str, dict[str, Any]] = {}
    for item in items:
        sid = item.get("id")
        if sid in by_id:
            err("SKILL_DUPLICATE", f"duplicate catalog id {sid}")
            continue
        by_id[sid] = item

    maturity_levels = set(catalog.get("maturity_levels") or [])
    coverage_levels = set(catalog.get("eval_coverage_levels") or [])
    for sid, item in by_id.items():
        rel = Path(item["path"])
        path = ROOT / rel
        if not path.is_file():
            err("SKILL_PATH", f"{sid}: missing {rel}")
            continue
        if path.name != "SKILL.md":
            err("SKILL_PATH", f"{sid}: catalog path must point to SKILL.md")
        fm, text = frontmatter(path)
        if fm is None:
            err("FRONTMATTER", f"{sid}: missing/invalid frontmatter in {rel}")
            continue
        if fm.get("name") != sid:
            err("SKILL_NAME", f"{sid}: frontmatter name={fm.get('name')!r}")
        desc = fm.get("description")
        if not isinstance(desc, str) or len(desc.strip()) < 40:
            err("SKILL_DESCRIPTION", f"{sid}: description missing or too short")
        elif not trigger_description(desc):
            err("SKILL_TRIGGER", f"{sid}: description does not contain a reproducible trigger signal")
        if not near_miss_signal(desc + "\n" + text):
            warn("SKILL_NEAR_MISS", f"{sid}: no explicit near-miss/negative boundary found")
        if maturity_levels and item.get("maturity") not in maturity_levels:
            err("SKILL_MATURITY", f"{sid}: unknown maturity {item.get('maturity')}")
        if coverage_levels and item.get("eval_coverage") not in coverage_levels:
            err("SKILL_EVAL_COVERAGE", f"{sid}: unknown eval_coverage {item.get('eval_coverage')}")
        for related in item.get("related") or []:
            if related not in by_id:
                err("RELATED", f"{sid}: unknown related skill {related}")
    return by_id, len(items)


def validate_eval_cases(by_id: dict[str, dict[str, Any]]) -> int:
    schema = load_yaml(ROOT / "Evals/eval-case.schema.yml") or {}
    required = set(schema.get("required_fields") or [])
    allowed_classes = set(schema.get("allowed_classes") or [])
    allowed_status = set(schema.get("allowed_status") or [])
    seen_paths: dict[str, Path] = {}
    case_files = sorted(ROOT.glob("Evals/**/cases.yml"))
    for path in case_files:
        data = load_yaml(path)
        rel = path.relative_to(ROOT)
        if not isinstance(data, dict):
            err("EVAL_FORMAT", f"{rel}: expected mapping")
            continue
        skill_id = path.parent.name
        if skill_id not in by_id:
            err("EVAL_SKILL", f"{rel}: directory skill id {skill_id} not in catalog")
            continue
        if skill_id in seen_paths:
            err("EVAL_DUPLICATE", f"{skill_id}: cases.yml exists at {seen_paths[skill_id]} and {rel}")
        seen_paths[skill_id] = rel
        expected_area = by_id[skill_id].get("area")
        actual_area = path.parent.parent.name
        if expected_area != actual_area:
            err("EVAL_AREA", f"{rel}: area {actual_area} != catalog area {expected_area}")
        cases = data.get("cases")
        if not isinstance(cases, list):
            err("EVAL_FORMAT", f"{rel}: top-level 'cases' must be a list")
            continue
        ids: set[str] = set()
        for idx, case in enumerate(cases):
            if not isinstance(case, dict):
                err("EVAL_CASE", f"{rel} case[{idx}] is not a mapping")
                continue
            missing = sorted(required - set(case))
            if missing:
                err("EVAL_CASE", f"{rel} case[{idx}] missing {missing}")
            cid = case.get("id")
            if cid in ids:
                err("EVAL_CASE_ID", f"{rel}: duplicate case id {cid}")
            ids.add(cid)
            if case.get("class") not in allowed_classes:
                err("EVAL_CLASS", f"{rel} {cid}: invalid class {case.get('class')}")
            if case.get("expected_status") not in allowed_status:
                err("EVAL_STATUS", f"{rel} {cid}: invalid expected_status {case.get('expected_status')}")
            if not isinstance(case.get("should_trigger"), bool):
                err("EVAL_TRIGGER", f"{rel} {cid}: should_trigger must be boolean")
            for field in ("expected", "forbidden"):
                if not isinstance(case.get(field), list):
                    err("EVAL_CASE", f"{rel} {cid}: {field} must be a list")
    for sid, item in by_id.items():
        has = sid in seen_paths
        coverage = item.get("eval_coverage")
        if coverage != "none" and not has:
            err("EVAL_PATH", f"{sid}: eval_coverage={coverage} but no cases.yml exists")
        if coverage == "none" and has:
            err("EVAL_COVERAGE", f"{sid}: cases.yml exists but catalog says eval_coverage=none")
    return len(case_files)


def validate_workflows() -> int:
    index_path = ROOT / "workflow-index.yml"
    data = load_yaml(index_path)
    validate_schema(data, ROOT / "Schemas/workflow-index.schema.json", "workflow-index.yml")
    if not isinstance(data, dict):
        return 0
    indexed = set(data.get("workflows") or [])
    real = {str(p.relative_to(ROOT)).replace("\\", "/") for p in (ROOT / "Workflows").glob("*.md") if p.name != "README.md"}
    for path in sorted(indexed - real):
        err("WORKFLOW_INDEX", f"indexed workflow does not exist: {path}")
    for path in sorted(real - indexed):
        err("WORKFLOW_INDEX", f"workflow missing from index: {path}")
    return len(real)


def validate_manifest() -> None:
    path = ROOT / "Vorlagen/ki-regeln.template.yml"
    data = load_yaml(path)
    validate_schema(data, ROOT / "Schemas/ki-regeln.template.schema.json", str(path.relative_to(ROOT)))
    if not isinstance(data, dict):
        return
    for section in ("rules", "skills", "workflows"):
        for value in data.get(section) or []:
            if "<" in value:
                continue
            p = ROOT / value
            if section == "skills" and p.is_dir():
                p = p / "SKILL.md"
            if not p.exists():
                err("MANIFEST_PATH", f"{section}: missing central path {value}")


def validate_upstreams() -> tuple[int, int, int]:
    path = ROOT / "Dokumentation/upstream-sources.yml"
    data = load_yaml(path)
    validate_schema(data, ROOT / "Schemas/upstream-sources.schema.json", str(path.relative_to(ROOT)))
    sources = (data or {}).get("sources") if isinstance(data, dict) else []
    sources = sources or []
    ids: set[str] = set()
    github: dict[str, dict[str, Any]] = {}
    for source in sources:
        sid = source.get("id")
        if sid in ids:
            err("UPSTREAM_ID", f"duplicate source id {sid}")
        ids.add(sid)
        for impact in source.get("local_impact") or []:
            if not (ROOT / impact).exists():
                err("UPSTREAM_IMPACT", f"{sid}: missing local_impact path {impact}")
        if source.get("kind") == "github-file":
            github[sid] = source

    ppath = ROOT / "Dokumentation/upstream-provenance.yml"
    pdata = load_yaml(ppath)
    validate_schema(pdata, ROOT / "Schemas/upstream-provenance.schema.json", str(ppath.relative_to(ROOT)))
    entries = (pdata or {}).get("sources") if isinstance(pdata, dict) else []
    entries = entries or []
    pids: set[str] = set()
    for entry in entries:
        sid = entry.get("source_id")
        if sid in pids:
            err("PROVENANCE_ID", f"duplicate provenance source_id {sid}")
        pids.add(sid)
        if sid not in github:
            err("PROVENANCE_ID", f"provenance source_id not a github-file upstream: {sid}")
    for sid in sorted(set(github) - pids):
        err("PROVENANCE_MISSING", f"github-file upstream missing source-specific provenance record: {sid}")
    defaults = (pdata or {}).get("defaults", {}) if isinstance(pdata, dict) else {}
    unresolved = 0
    by_provenance = {entry.get("source_id"): entry for entry in entries}
    for sid in sorted(github):
        entry = by_provenance.get(sid, {})
        effective = dict(defaults)
        effective.update(entry)
        if effective.get("license_spdx") in (None, "UNKNOWN") or effective.get("redistribution_status") == "unresolved":
            unresolved += 1
        if effective.get("license_spdx") in (None, "UNKNOWN") and effective.get("redistribution_status") not in ("unresolved", "not-redistributable"):
            err("PROVENANCE_LICENSE", f"{sid}: unknown license may not be marked redistributable")
        if effective.get("use_class") in ("adapted", "copied/vendored") and effective.get("license_spdx") in (None, "UNKNOWN"):
            err("PROVENANCE_LICENSE", f"{sid}: {effective.get('use_class')} requires resolved license before redistribution")
        if effective.get("use_class") == "reference/inspiration" and effective.get("notice_requirement") not in ("none", "none-for-reference-only", "unknown"):
            warn("PROVENANCE_NOTICE", f"{sid}: reference/inspiration should not be presented as vendored notice material")
        commit = effective.get("repository_commit")
        license_path = effective.get("license_path")
        license_blob = effective.get("license_blob_sha")
        if any(value is not None for value in (commit, license_path, license_blob)) and not all(value is not None for value in (commit, license_path, license_blob)):
            err("PROVENANCE_EVIDENCE", f"{sid}: same-state license evidence requires repository_commit, license_path and license_blob_sha together")
    return len(sources), len(github), unresolved


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--warnings-as-errors", action="store_true")
    args = parser.parse_args()

    catalog_path = ROOT / "skill-catalog.yml"
    catalog = load_yaml(catalog_path)
    validate_schema(catalog, ROOT / "Schemas/skill-catalog.schema.json", "skill-catalog.yml")
    if not isinstance(catalog, dict):
        err("CATALOG", "skill-catalog.yml is not a mapping")
        catalog = {"skills": []}
    by_id, skill_count = validate_skills(catalog)
    eval_files = validate_eval_cases(by_id)
    workflow_count = validate_workflows()
    validate_manifest()
    upstream_count, github_upstreams, unresolved = validate_upstreams()

    print(f"Validated skills: {skill_count}")
    print(f"Validated eval files: {eval_files}")
    print(f"Validated workflows: {workflow_count}")
    print(f"Validated upstream sources: {upstream_count} ({github_upstreams} GitHub files; {unresolved} unresolved license/provenance records)")
    for message in WARNINGS:
        print(f"WARNING {message}")
    for message in ERRORS:
        print(f"ERROR {message}")
    if ERRORS or (args.warnings_as_errors and WARNINGS):
        print(f"RESULT: FAIL ({len(ERRORS)} errors, {len(WARNINGS)} warnings)")
        return 1
    print(f"RESULT: PASS (0 errors, {len(WARNINGS)} warnings)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
