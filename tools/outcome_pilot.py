#!/usr/bin/env python3
"""Deterministic, offline outcome scorer for a synthetic HypeRadar hand-off.

This does NOT evaluate an agent's process or authorization. Keep judge labels
outside the agent's runtime workspace; the public repository is not secret.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _ids(values: object, name: str) -> list[str]:
    if not isinstance(values, list) or any(not isinstance(v, str) or not v.strip() for v in values):
        raise ValueError(f"{name} must be an array of nonempty strings")
    if len(values) != len(set(values)):
        raise ValueError(f"{name} contains repeated values")
    return values


def score_outcome(case: dict, labels: dict, submission: dict) -> dict:
    """Judge a frozen, synthetic discovery hand-off without external requests."""
    if not all(isinstance(x, dict) for x in (case, labels, submission)):
        raise ValueError("case, labels and submission must be JSON objects")
    case_id = case.get("case_id")
    if not isinstance(case_id, str) or not case_id:
        raise ValueError("missing case_id")
    if labels.get("case_id") != case_id or submission.get("case_id") != case_id:
        raise ValueError("case_id mismatch")
    if set(submission) != {"case_id", "selected"}:
        raise ValueError("submission must contain exactly case_id and selected")
    candidates = case.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        raise ValueError("candidates must be a nonempty array")
    index = {}
    for candidate in candidates:
        if not isinstance(candidate, dict) or not isinstance(candidate.get("id"), str):
            raise ValueError("candidate id missing")
        ident = candidate["id"]
        if not ident or ident in index:
            raise ValueError("duplicate or empty candidate id")
        _ids(candidate.get("aliases", []), "aliases")
        sources = _ids(candidate.get("sources"), "candidate sources")
        if not sources:
            raise ValueError("each candidate needs a source")
        index[ident] = candidate

    history = set(_ids(case.get("already_delivered"), "already_delivered"))
    relevant = set(_ids(labels.get("relevant_ids"), "relevant_ids"))
    if not relevant or not relevant.issubset(index):
        raise ValueError("judge labels must reference nonempty, known candidate ids")
    if any(history.intersection({ident, *index[ident]["aliases"]}) for ident in relevant):
        raise ValueError("judge labels include a historical duplicate")

    selected = submission.get("selected")
    if not isinstance(selected, list):
        raise ValueError("selected must be an array")
    blockers = []
    seen = set()
    chosen = set()
    for item in selected:
        if not isinstance(item, dict) or set(item) != {"id", "evidence_urls"}:
            raise ValueError("each selection needs exactly id and evidence_urls")
        ident = item["id"]
        if not isinstance(ident, str) or not ident:
            raise ValueError("selected id must be a nonempty string")
        if ident in seen:
            blockers.append(f"repeated-selection:{ident}")
        seen.add(ident)
        candidate = index.get(ident)
        if candidate is None:
            blockers.append(f"unknown-id:{ident}")
            continue
        if history.intersection({ident, *candidate["aliases"]}):
            blockers.append(f"historical-duplicate:{ident}")
        evidence = item["evidence_urls"]
        if not isinstance(evidence, list) or not evidence or any(not isinstance(u, str) for u in evidence):
            blockers.append(f"missing-evidence:{ident}")
        elif any(u not in candidate["sources"] for u in evidence):
            blockers.append(f"unsupported-evidence:{ident}")
        chosen.add(ident)

    tp, fp, fn = len(chosen & relevant), len(chosen - relevant), len(relevant - chosen)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "outcome_status": "BLOCKED" if blockers else "SCORED",
        "outcome_score": 0.0 if blockers else round(f1 * 100, 1),
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "true_positives": tp,
        "false_positives": fp,
        "false_negatives": fn,
        "blockers": blockers,
        "process_verification": "NOT_RUN",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", type=Path, required=True)
    parser.add_argument("--judge", type=Path, required=True)
    parser.add_argument("--submission", type=Path, required=True)
    parser.add_argument("--agent", default="unattributed")
    args = parser.parse_args()
    try:
        case = json.loads(args.case.read_text(encoding="utf-8"))
        judge = json.loads(args.judge.read_text(encoding="utf-8"))
        submission = json.loads(args.submission.read_text(encoding="utf-8"))
        result = score_outcome(case, judge, submission)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"outcome_status": "INVALID", "error": str(exc)}, ensure_ascii=False))
        return 2
    result["agent"] = args.agent
    result["case_id"] = case["case_id"]
    result["sha256"] = {
        "case": canonical_hash(case),
        "judge": canonical_hash(judge),
        "submission": canonical_hash(submission),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["outcome_status"] == "SCORED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
