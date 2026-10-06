#!/usr/bin/env python3
"""Project a Golden Task into a blind execution-only view."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]

# Keep the runner view deliberately smaller than the full task definition.
# title/goal/id are editorial/evaluator metadata and have repeatedly encoded
# the expected route in natural language. sources_of_truth roles can do the same.
EXECUTION_FIELDS = (
    "schema_version",
    "assignment",
    "fixtures",
    "required_capabilities",
)

EVALUATOR_ONLY_FIELDS = (
    "behavioral_routing_mode",
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

ROUTING_HINT_FIELDS = (
    "id",
    "title",
    "goal",
    "sources_of_truth",
)

BLINDNESS_FORBIDDEN_FIELDS = frozenset(EVALUATOR_ONLY_FIELDS + ROUTING_HINT_FIELDS)


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


def assert_blind(view: dict[str, Any]) -> None:
    leaked = sorted(set(view) & BLINDNESS_FORBIDDEN_FIELDS)
    if leaked:
        raise SystemExit(f"blindness-sensitive fields leaked into execution view: {leaked}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("task", help="Repository-relative path to a Golden Task task.yml")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of YAML")
    parser.add_argument(
        "--assert-no-evaluator-fields",
        action="store_true",
        help="Compatibility flag: assert that neither evaluator fields nor routing-hint metadata leaked.",
    )
    parser.add_argument("--assert-blind", action="store_true", help="Assert the blind runner-view contract.")
    args = parser.parse_args()

    rel = Path(args.task)
    if rel.is_absolute() or ".." in rel.parts:
        raise SystemExit("task path must stay repository-relative")
    path = ROOT / rel
    data = load_task(path)
    view = project(data)

    if args.assert_no_evaluator_fields or args.assert_blind:
        assert_blind(view)

    if args.json:
        print(json.dumps(view, ensure_ascii=False, indent=2))
    else:
        print(yaml.safe_dump(view, allow_unicode=True, sort_keys=False), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
