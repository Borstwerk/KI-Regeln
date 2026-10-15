#!/usr/bin/env python3
"""Prepare a GT-01 arm-blinded reviewer packet without running a model."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import secrets

ROOT = Path(__file__).resolve().parents[3]
GT = Path("Evals/Golden-Tasks/GT-01")
BASE = "Codex-Product-Pilot-2026-10-15"
SOURCES = ("table-schema.sql", "usage.md")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def criteria(report):
    rows = [line for line in report.splitlines() if re.match(r"^\| C[1-9] \| ", line)]
    ids = [re.match(r"^\| (C[1-9]) \|", line).group(1) for line in rows]
    if ids != [f"C{n}" for n in range(1, 10)]:
        raise ValueError("Frozen C1-C9 rubric is missing or changed")
    return rows


def prepare(root, reviewer_dir, operator_dir, flip=False):
    root = Path(root).resolve()
    reviewer_dir = Path(reviewer_dir).resolve()
    operator_dir = Path(operator_dir).resolve()
    if reviewer_dir == operator_dir or reviewer_dir in operator_dir.parents or operator_dir in reviewer_dir.parents:
        raise ValueError("Separate reviewer and operator directories are mandatory")
    if reviewer_dir.exists() or operator_dir.exists():
        raise FileExistsError("Existing output must not be overwritten")
    folder = root / GT
    evidence = json.loads((folder / f"{BASE}.json").read_text(encoding="utf-8"))
    for name in SOURCES:
        path = GT / name
        if sha((root / path).read_bytes()) != evidence["protocol"]["source_sha256"][path.as_posix()]:
            raise ValueError("Changed source: " + name)
    rows = evidence["responses"]
    if len(rows) != 2 or {r["arm"] for r in rows} != {"baseline", "skill"}:
        raise ValueError("Expected one recorded response per arm")
    bodies = {}
    for arm in ("baseline", "skill"):
        body = (folder / f"{BASE}-{arm}.md").read_bytes()
        expected = next(row["artifact_sha256"] for row in rows if row["arm"] == arm)
        if sha(body) != expected:
            raise ValueError("Changed answer artifact: " + arm)
        bodies[arm] = body
    rubric = criteria((folder / f"{BASE}.md").read_text(encoding="utf-8"))
    reviewer_dir.mkdir(parents=True)
    operator_dir.mkdir(parents=True)
    order = ("skill", "baseline") if flip else ("baseline", "skill")
    labels = {}
    for label, arm in zip(("A", "B"), order):
        (reviewer_dir / f"{label}.md").write_bytes(bodies[arm])
        labels[label] = {"arm": arm, "sha256": sha(bodies[arm])}
    for name in SOURCES:
        (reviewer_dir / name).write_bytes((folder / name).read_bytes())
    rubric_doc = [
        "# GT-01: arm-blinded reviewer packet", "",
        "Evaluate A.md and B.md separately using ONLY these files.",
        "Do not browse GitHub, original PRs, past results or the operator directory.",
        "The two local fixtures are the full sources of truth. No database is available.",
        "Task: Document the existing customer_note table without schema redesign.", "",
        "## Frozen C1-C9 criteria", "",
        "| ID | Required output |", "| --- | --- |", *rubric, "",
        "For each criterion provide pass/partial/fail/unverified with a supporting quote.",
        "pass = complete; partial = missing but not contradicted; fail = false or forbidden claim;",
        "unverified = no usable response. Any fail => overall fail; otherwise partial if any",
        "criterion is partial; all nine pass => overall pass. Explain any ambiguities.",
        "Do not infer tool use, file reads, SQL execution or natural skill discovery.",
        "Do not guess the arm mapping. This package does not itself prove independent review.", "",
    ]
    (reviewer_dir / "REVIEW-INSTRUCTIONS.md").write_text("\n".join(rubric_doc), encoding="utf-8")
    scorecard = {"A": {f"C{i}": None for i in range(1, 10)},
                 "B": {f"C{i}": None for i in range(1, 10)},
                 "findings_A": [], "findings_B": [],
                 "reviewer_and_context": None, "reviewed_at": None}
    (reviewer_dir / "scorecard-template.json").write_text(json.dumps(scorecard, indent=2) + "\n", encoding="utf-8")
    record = {"labels": labels, "packet_sha256": {p.name: sha(p.read_bytes()) for p in sorted(reviewer_dir.iterdir())},
              "warning": "PRIVATE OPERATOR MAPPING – NEVER SHARE WITH BLIND REVIEWER"}
    (operator_dir / "reveal.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reviewer-out", type=Path, default=ROOT / ".validation/gt01-blind-reviewer")
    parser.add_argument("--operator-out", type=Path, default=ROOT / ".validation/gt01-blind-operator")
    args = parser.parse_args()
    safe_root = (ROOT / ".validation").resolve()
    if any(not path.resolve().is_relative_to(safe_root) for path in (args.reviewer_out, args.operator_out)):
        parser.error("Output folders must be inside gitignored .validation")
    try:
        prepare(ROOT, args.reviewer_out, args.operator_out, flip=bool(secrets.randbits(1)))
    except (ValueError, FileExistsError) as exc:
        parser.error(str(exc))
    print("Reviewer-only packet: " + str(args.reviewer_out))
    print("Private mapping (DO NOT SHARE): " + str(args.operator_out))
    print("Independent reviewer: NOT RUN")


if __name__ == "__main__":
    main()
