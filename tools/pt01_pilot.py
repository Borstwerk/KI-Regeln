#!/usr/bin/env python3
"""PT-01 offline fixture packer and DEVELOPMENT-LABEL review grader.

Pure stdlib. No model calls, subprocess, external execution or network.
Passing these checks DOES NOT establish an agent/skill quality improvement.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "Evals/Agentenarbeit/Ponytail-Pilot"
CASES = BASE / "runner-input/cases.json"
LABELS = BASE / "judge-only/labels.json"
CHECKPOINT = BASE / "variants/minimal-checkpoint.md"
CATEGORIES = {"bug", "security", "data_loss", "tracked", "no_trigger"}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def safe_rel(value: str) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError(f"unsafe relative filename: {value!r}")
    p = PurePosixPath(value)
    if p.is_absolute() or any(part in ("", ".", "..") for part in p.parts) or p.as_posix() != value:
        raise ValueError(f"unsafe relative filename: {value!r}")
    if p.parts[0] in {"judge-only", "controls"}:
        raise ValueError("reserved filename")
    return p


def validate() -> dict:
    bundle = load_json(CASES)
    labels = load_json(LABELS)
    if bundle.get("schema_version") != 1 or bundle.get("pilot") != "PT-01":
        raise ValueError("runner case schema mismatch")
    if labels.get("schema_version") != 1 or labels.get("pilot") != "PT-01":
        raise ValueError("judge schema mismatch")
    records = bundle.get("cases")
    targets = labels.get("cases")
    if not isinstance(records, list) or len(records) != 8 or not isinstance(targets, list):
        raise ValueError("wrong case/label count")
    identifiers = [r.get("id") for r in records]
    if len(set(identifiers)) != 8 or set(identifiers) != {x.get("id") for x in targets}:
        raise ValueError("case ids missing, duplicated or unpaired")
    if {x.get("track") for x in records} != {"A", "B", "C", "D"}:
        raise ValueError("four required tracks missing")
    for row in records:
        if row.get("kind") not in {"implementation", "review", "audit", "debt"}:
            raise ValueError("invalid kind")
        if row.get("id") != "PT01-" + row["track"] + row["id"][-1]:
            raise ValueError("track/id mismatch")
        if not isinstance(row.get("task"), str) or not row["task"].strip():
            raise ValueError("blank task")
        if not isinstance(row.get("files"), dict) or not row["files"]:
            raise ValueError("missing files")
        for name, body in row["files"].items():
            safe_rel(name)
            if not isinstance(body, str):
                raise ValueError("non-text fixture")
    by_id = {r["id"]: r for r in records}
    for label in targets:
        row = by_id[label["id"]]
        if label.get("kind") != row["kind"]:
            raise ValueError("judge/runner kind mismatch")
        if row["kind"] == "implementation":
            if label.get("findings") is not None:
                raise ValueError("implementation labels are behavioral, not issue anchors")
            continue
        if not isinstance(label.get("findings"), list):
            raise ValueError("missing objective anchors")
        for item in label["findings"]:
            filename = safe_rel(item["path"]).as_posix()
            if filename not in row["files"] or item.get("category") not in CATEGORIES:
                raise ValueError("unresolvable finding label")
            source = row["files"][filename].splitlines()
            needle = item["needle"]
            found = [n for n, line in enumerate(source, 1) if needle in line]
            occurrence = item.get("occurrence", 1)
            if not isinstance(occurrence, int) or occurrence < 1 or len(found) < occurrence:
                raise ValueError("missing judge text anchor")
    return bundle


def get_case(case_id: str) -> dict:
    for row in validate()["cases"]:
        if row["id"] == case_id:
            return row
    raise ValueError(f"unknown case: {case_id}")


def reference(case_id: str) -> set[tuple[str, int, str]]:
    row = get_case(case_id)
    label = next(x for x in load_json(LABELS)["cases"] if x["id"] == case_id)
    found = set()
    for entry in label.get("findings", []):
        lines = row["files"][entry["path"]].splitlines()
        matches = [i for i, line in enumerate(lines, 1) if entry["needle"] in line]
        index = entry.get("occurrence", 1) - 1
        found.add((entry["path"], matches[index], entry["category"]))
    return found


def prepare(case_id: str, arm: str, output: Path) -> dict:
    if arm not in ("A", "B"):
        raise ValueError("Arm C requires a separate external bundle admission; not packable here")
    row = get_case(case_id)
    if output.exists() or output.is_symlink():
        raise ValueError("output must be a new, nonexisting directory")
    output.mkdir(parents=True, exist_ok=False)
    files = {}
    for rel, body in row["files"].items():
        dst = output.joinpath(*safe_rel(rel).parts)
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(body, encoding="utf-8")
        files[rel] = hashlib.sha256(body.encode("utf-8")).hexdigest()
    task = (
        f"# {case_id} – {row['track']} / {row['kind']}\n\n"
        + row["task"] + "\n\n"
        + "## Rahmen\n\n"
        + "\n".join("- " + item for item in row["constraints"])
        + "\n\n## Abgabe\n\n"
        + ("Ändere nur die notwendigen Workspace-Dateien, liefere Diff und frische Checks. "
           if row["kind"] == "implementation" else
           "Keine Codeänderung. Liefere REPORT.json mit case_id und findings als Liste "
           "mit path, line (positive Zahl) und category; bei echten Nullbefunden []. ")
        + "Berichte ausdrücklich NOT RUN, wenn Prüfschritte nicht liefen.\n"
    )
    (output / "TASK.md").write_text(task, encoding="utf-8")
    if arm == "B":
        (output / "OPTIONAL_CHECKPOINT.md").write_text(CHECKPOINT.read_text(encoding="utf-8"), encoding="utf-8")
    manifest = {"pilot": "PT-01", "case_id": case_id, "arm": arm, "files_sha256": files,
                "task_sha256": hashlib.sha256(task.encode("utf-8")).hexdigest(),
                "status": "FIXTURE_PREPARED_NOT_MODEL_RUN"}
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest


def grade_report(case_id: str, submission: dict) -> dict:
    row = get_case(case_id)
    if row["kind"] == "implementation":
        raise ValueError("implementation requires executed independent behavior tests and human scope review")
    if not isinstance(submission, dict) or submission.get("case_id") != case_id:
        raise ValueError("case ID mismatch")
    entries = submission.get("findings")
    if not isinstance(entries, list) or len(entries) > 30:
        raise ValueError("findings must be a list with at most 30 items")
    actual = set()
    for item in entries:
        if not isinstance(item, dict):
            raise ValueError("invalid finding object")
        p = safe_rel(item.get("path"))
        n = item.get("line")
        category = item.get("category")
        if str(p) not in row["files"] or not isinstance(n, int) or isinstance(n, bool) or n < 1:
            raise ValueError("finding references invalid file/line")
        if n > len(row["files"][str(p)].splitlines()) or category not in CATEGORIES:
            raise ValueError("finding invalid line/category")
        key = (str(p), n, category)
        if key in actual:
            raise ValueError("duplicate finding")
        actual.add(key)
    gold = reference(case_id)
    true = actual & gold
    return {"case_id": case_id, "status": "DEVELOPMENT_LABEL_SCORE_ONLY",
            "correct": len(true), "expected": len(gold),
            "unexpected": len(actual - gold), "missing": len(gold - actual),
            "precision": (len(true) / len(actual) if actual else (1.0 if not gold else 0.0)),
            "recall": (len(true) / len(gold) if gold else (1.0 if not actual else 0.0)),
            "limitations": "Anchor/line exact match; valid alternative findings need human review."}


def selftest() -> dict:
    from tempfile import TemporaryDirectory
    data = validate()
    with TemporaryDirectory() as d:
        for row in data["cases"]:
            case = row["id"]
            arm = "A"
            target = Path(d) / case
            manifest = prepare(case, arm, target)
            assert manifest["status"] == "FIXTURE_PREPARED_NOT_MODEL_RUN"
            assert not (target / "judge-only").exists()
            assert not (target / "labels.json").exists()
            assert "OPTIONAL_CHECKPOINT.md" not in [x.name for x in target.iterdir()]
            if row["kind"] != "implementation":
                ref = [{"path": p, "line": line, "category": cat}
                       for p, line, cat in sorted(reference(case))]
                report = grade_report(case, {"case_id": case, "findings": ref})
                assert report["missing"] == 0 and report["unexpected"] == 0
                if ref:
                    negative = grade_report(case, {"case_id": case, "findings": []})
                    assert negative["missing"] > 0
            else:
                try:
                    grade_report(case, {"case_id": case, "findings": []})
                except ValueError:
                    pass
                else:
                    raise AssertionError("implementation must not get fake automatic score")
        bpath = Path(d) / "B-variant"
        prepare("PT01-B1", "B", bpath)
        assert (bpath / "OPTIONAL_CHECKPOINT.md").is_file()
        try:
            prepare("PT01-B1", "C", Path(d) / "blocked")
        except ValueError:
            pass
        else:
            raise AssertionError("unadmitted external arm C was prepared")
        for bad in ("../escape.py", "/root/a", "judge-only/labels.json", "a\\b"):
            try:
                safe_rel(bad)
            except ValueError:
                pass
            else:
                raise AssertionError("unsafe path accepted: " + bad)
    return {"status": "SELFTEST_OK_OFFLINE", "case_count": len(data["cases"]),
            "message": "Only fixture integrity and development grader tested; no agent outcome measured"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    pack = sub.add_parser("prepare")
    pack.add_argument("--case", required=True)
    pack.add_argument("--arm", choices=("A", "B", "C"), required=True)
    pack.add_argument("--out", type=Path, required=True)
    grade = sub.add_parser("grade-report")
    grade.add_argument("--case", required=True)
    grade.add_argument("--submission", type=Path, required=True)
    sub.add_parser("selftest")
    args = parser.parse_args()
    if args.command == "selftest":
        result = selftest()
    elif args.command == "prepare":
        result = prepare(args.case, args.arm, args.out)
    else:
        if args.submission.stat().st_size > 100_000:
            raise ValueError("oversized report")
        result = grade_report(args.case, load_json(args.submission))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
