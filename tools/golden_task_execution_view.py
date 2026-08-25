#!/usr/bin/env python3
"""Project a Golden Task into an execution-only view without evaluator expectations."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
EXECUTION_FIELDS = (
    "schema_version",
    "id",
    "title",
    "goal",
    "assignment",
    "fixtures",
    "sources_of_truth",
    "required_capabilities",
)
EVALUATOR_ONLY_FIELDS = (
    "expected_domain",
    "allowed_secondary_domains",
    "workflow",
    "required_skills",
    "allowed_optional_skills",
    "forbidden_skills",
    "expected_evidence",
    "expected_artifacts",
    "expected_verification",
    "allowed_uncertainty",
    "expected_status",
    "forbidden_behaviors",
    "rubric",
)


def load_task(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise SystemExit(f"task must be a mapping: {path}")
    return data


def project(data: dict[str, Any]) -> dict[str, Any]:
    missing = [field for field in EXECUTION_FIELDS if field not in data]
    if missing:
        raise SystemExit(f"task missing execution fields: {missing}")
    return {field: data[field] for field in EXECUTION_FIELDS}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("task", help="Repository-relative path to a Golden Task task.yml")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of YAML")
    parser.add_argument("--assert-no-evaluator-fields", action="store_true")
    args = parser.parse_args()

    rel = Path(args.task)
    if rel.is_absolute() or ".." in rel.parts:
        raise SystemExit("task path must stay repository-relative")
    path = ROOT / rel
    data = load_task(path)
    view = project(data)

    if args.assert_no_evaluator_fields:
        leaked = sorted(set(view) & set(EVALUATOR_ONLY_FIELDS))
        if leaked:
            raise SystemExit(f"evaluator-only fields leaked into execution view: {leaked}")

    if args.json:
        print(json.dumps(view, ensure_ascii=False, indent=2))
    else:
        print(yaml.safe_dump(view, allow_unicode=True, sort_keys=False), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
