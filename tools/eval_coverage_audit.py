#!/usr/bin/env python3
"""Read-only coverage audit for KI-Regeln skill eval packs."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def build_audit() -> dict[str, Any]:
    catalog = load_yaml(ROOT / "skill-catalog.yml") or {}
    skills = catalog.get("skills") or []
    records: list[dict[str, Any]] = []

    coverage_counts: Counter[str] = Counter()
    total_cases = 0
    eval_files = 0

    for skill in skills:
        sid = skill["id"]
        area = skill["area"]
        coverage = skill.get("eval_coverage", "none")
        coverage_counts[coverage] += 1
        cases_path = ROOT / "Evals" / area / sid / "cases.yml"
        cases: list[dict[str, Any]] = []
        if cases_path.is_file():
            data = load_yaml(cases_path) or {}
            raw_cases = data.get("cases") or []
            if isinstance(raw_cases, list):
                cases = [case for case in raw_cases if isinstance(case, dict)]
            eval_files += 1

        class_counts = Counter(str(case.get("class")) for case in cases)
        status_counts = Counter(str(case.get("expected_status")) for case in cases)
        trigger_true = sum(case.get("should_trigger") is True for case in cases)
        trigger_false = sum(case.get("should_trigger") is False for case in cases)
        total_cases += len(cases)

        signals: list[str] = []
        if not cases:
            signals.append("no-evals")
        else:
            if trigger_false == 0:
                signals.append("no-near-miss-signal")
            if status_counts.get("partial", 0) == 0:
                signals.append("no-evidence-gap-signal")
            if status_counts.get("blocked", 0) == 0:
                signals.append("no-authorization-gate-signal")
            if len(class_counts) <= 1:
                signals.append("single-eval-class")

        records.append(
            {
                "id": sid,
                "area": area,
                "eval_coverage": coverage,
                "has_cases": bool(cases),
                "case_count": len(cases),
                "trigger_true": trigger_true,
                "near_miss_or_nontrigger": trigger_false,
                "class_counts": dict(sorted(class_counts.items())),
                "status_counts": dict(sorted(status_counts.items())),
                "audit_signals": signals,
            }
        )

    return {
        "schema_version": 1,
        "skill_count": len(skills),
        "eval_file_count": eval_files,
        "case_count": total_cases,
        "coverage_counts": dict(sorted(coverage_counts.items())),
        "skills_without_evals": [r["id"] for r in records if not r["has_cases"]],
        "one_sided_signal_count": sum(bool(r["audit_signals"]) and r["has_cases"] for r in records),
        "skills": records,
        "notes": [
            "Audit signals are heuristics, not pass/fail rules.",
            "A missing blocked case is not automatically a defect when the skill has no meaningful external-action gate.",
            "Defined cases are not evidence that behavioral evals were executed or passed.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", action="store_true", help="Print compact human-readable counts.")
    args = parser.parse_args()
    audit = build_audit()
    if args.summary:
        print(f"Skills: {audit['skill_count']}")
        print(f"Eval files: {audit['eval_file_count']}")
        print(f"Cases: {audit['case_count']}")
        print("Coverage: " + ", ".join(f"{k}={v}" for k, v in audit["coverage_counts"].items()))
        print(f"Skills without evals: {len(audit['skills_without_evals'])}")
        print(f"Packs with one-sided audit signals: {audit['one_sided_signal_count']}")
    else:
        print(json.dumps(audit, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
