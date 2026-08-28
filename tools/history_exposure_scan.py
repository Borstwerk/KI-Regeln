#!/usr/bin/env python3
"""Sanitized exposure scan across commits reachable from local Git refs.

The tool reports only commit/path/line/category metadata. Matched values are never
printed. It does not claim to cover unreachable/pruned Git objects.
"""
from __future__ import annotations

from collections import defaultdict
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CAT_FILE_TIMEOUT_SECONDS = 120

PATTERNS = {
    "private-key": r"-----BEGIN (RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----",
    "github-token": r"gh[pousr]_[A-Za-z0-9]{20,}",
    "github-pat": r"github_pat_[A-Za-z0-9_]{20,}",
    "aws-access-key": r"(AKIA|ASIA)[A-Z0-9]{16}",
    "credentialed-url": r"[A-Za-z][A-Za-z0-9+.-]*://[^[:space:]/:@]+:[^[:space:]/@]+@",
    "connection-string-password": r"(password|pwd)[[:space:]]*=[[:space:]]*[^;[:space:]]{4,}",
    "bearer-token-literal": r"Authorization[[:space:]]*:[[:space:]]*Bearer[[:space:]]+[A-Za-z0-9._~+/=-]{16,}",
}

CONTEXT_PATTERNS = {
    "email-address": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    "private-ipv4": r"(10(\.[0-9]{1,3}){3}|192\.168(\.[0-9]{1,3}){2}|172\.(1[6-9]|2[0-9]|3[01])(\.[0-9]{1,3}){2})",
    "internal-hostname": r"[A-Za-z0-9][A-Za-z0-9.-]*\.(internal|corp|local)",
}


def run(*args: str) -> str:
    proc = subprocess.run(args, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode:
        raise SystemExit(f"command failed: {' '.join(args)}\n{proc.stderr}")
    return proc.stdout


def commits() -> list[str]:
    return [line for line in run("git", "rev-list", "--all").splitlines() if line]


def refs() -> list[str]:
    return [line for line in run("git", "for-each-ref", "--format=%(refname)").splitlines() if line]


def grep_pattern(revisions: list[str], category: str, pattern: str, severity: str) -> list[dict[str, object]]:
    found: dict[tuple[str, str, int, str], dict[str, object]] = {}
    # Keep argv comfortably below platform limits even for long histories.
    for start in range(0, len(revisions), 150):
        batch = revisions[start:start + 150]
        proc = subprocess.run(
            ["git", "grep", "-I", "-n", "-i", "-E", "-e", pattern, *batch, "--"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if proc.returncode not in (0, 1):
            raise SystemExit(f"git grep failed for {category}: {proc.stderr}")
        for raw in proc.stdout.splitlines():
            # Revision output format: <commit>:<path>:<line>:<matched line>
            parts = raw.split(":", 3)
            if len(parts) < 4:
                continue
            commit, path, line_raw, _value = parts
            try:
                line = int(line_raw)
            except ValueError:
                continue
            key = (commit, path, line, category)
            found[key] = {
                "commit": commit,
                "path": path,
                "line": line,
                "class": category,
                "severity": severity,
            }
    return list(found.values())


def unique_reachable_blob_count() -> int:
    objects = run("git", "rev-list", "--objects", "--all").splitlines()
    if not objects:
        return 0

    object_ids = [line.split(" ", 1)[0] for line in objects if line.strip()]
    payload = "".join(f"{object_id}\n" for object_id in object_ids)
    try:
        proc = subprocess.run(
            ["git", "cat-file", "--batch-check=%(objecttype)"],
            cwd=ROOT,
            text=True,
            input=payload,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=CAT_FILE_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired as exc:
        raise SystemExit(
            f"git cat-file timed out after {CAT_FILE_TIMEOUT_SECONDS}s"
        ) from exc

    if proc.returncode:
        raise SystemExit(f"git cat-file failed: {proc.stderr}")
    return sum(1 for line in proc.stdout.splitlines() if line.strip() == "blob")


def main() -> int:
    revisions = commits()
    findings: list[dict[str, object]] = []
    for category, pattern in PATTERNS.items():
        findings.extend(grep_pattern(revisions, category, pattern, "potential-secret"))
    for category, pattern in CONTEXT_PATTERNS.items():
        findings.extend(grep_pattern(revisions, category, pattern, "review-context"))

    summary = {
        "schema_version": 1,
        "scope": "all commits and blobs reachable from refs present in this full-history checkout; unreachable/pruned objects are outside scope",
        "commit_count": len(revisions),
        "ref_count": len(refs()),
        "unique_reachable_blob_count": unique_reachable_blob_count(),
        "potential_secret_finding_count": sum(1 for f in findings if f["severity"] == "potential-secret"),
        "context_review_finding_count": sum(1 for f in findings if f["severity"] == "review-context"),
        "findings": sorted(findings, key=lambda f: (str(f["class"]), str(f["path"]), str(f["commit"]), int(f["line"]))),
    }

    output = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    rendered = json.dumps(summary, ensure_ascii=False, indent=2) + "\n"
    if output:
        output.write_text(rendered, encoding="utf-8")
    print(f"Reachable commits: {summary['commit_count']}")
    print(f"Reachable unique blobs: {summary['unique_reachable_blob_count']}")
    print(f"Potential-secret findings: {summary['potential_secret_finding_count']}")
    print(f"Context-review findings: {summary['context_review_finding_count']}")
    if output:
        print(f"Report: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
