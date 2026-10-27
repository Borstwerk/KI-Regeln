#!/usr/bin/env python3
"""Independent PT-01A behavioral oracle.

Run ONLY inside an isolated disposable sandbox against a reviewed agent-generated
workspace. This imports and EXECUTES that workspace's code. Never run it against
untrusted downloaded code on a production machine or in repository CI.
Judge-only development oracle, not a hidden benchmark.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def check(case_id: str, workspace: Path) -> dict:
    root = workspace.resolve(strict=True)
    if not root.is_dir():
        raise ValueError("workspace must be a directory")
    # The harness must not be copied into a worker's input bundle.
    sys.path.insert(0, str(root))
    if case_id == "PT01-A1":
        from app.search import find_titles
        checks = [
            ("ignore case/whitespace", lambda: [x["title"] for x in find_titles("  RIVER  ")] == ["River House"]),
            ("already matching term", lambda: [x["title"] for x in find_titles("Bridge")] == ["Stone Bridge"]),
            ("unknown title", lambda: find_titles("unrelated") == []),
            ("return dictionaries", lambda: all(isinstance(x, dict) for x in find_titles("house"))),
        ]
    elif case_id == "PT01-A2":
        from app.quote import quote_total_cents
        checks = [
            ("small fee", lambda: quote_total_cents("1.00", "0.01") == 101),
            ("default fee", lambda: quote_total_cents("1.25") == 125),
            ("negative fee", lambda: quote_total_cents("2.00", "-0.15") == 185),
            ("cent accuracy", lambda: quote_total_cents("0.10", "0.20") == 30),
        ]
    else:
        raise ValueError("only PT01-A1 and PT01-A2 have execution oracles")
    results = []
    for name, run in checks:
        try:
            passed = bool(run())
            results.append({"check": name, "passed": passed})
        except Exception as exc:
            results.append({"check": name, "passed": False, "error_type": type(exc).__name__})
    return {"case_id": case_id,
            "status": "DEVELOPMENT_BEHAVIOR_CHECK_ONLY",
            "checks": results,
            "passed": sum(x["passed"] for x in results),
            "total": len(results),
            "scope": "Does not grade code minimalism, security, tests, scope or real agent process."}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", choices=("PT01-A1", "PT01-A2"), required=True)
    parser.add_argument("--workspace", type=Path, required=True)
    args = parser.parse_args()
    result = check(args.case, args.workspace)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["passed"] != result["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
