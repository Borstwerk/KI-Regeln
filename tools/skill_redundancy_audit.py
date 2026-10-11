#!/usr/bin/env python3
"""Read-only, report-only lexical redundancy audit for SKILL.md instruction files.

No external packages, no model calls, no writes to the scanned repository.
Exact normalized multiword paragraph matches are candidate findings, not automatic
permission to delete or merge rules.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any


WORD_RE = re.compile(r"\b[\w-]+\b", re.UNICODE)
SPACE_RE = re.compile(r"\s+")


def normalized(text: str) -> str:
    return SPACE_RE.sub(" ", text).casefold().strip()


def instruction_blocks(text: str, minimum_words: int) -> list[dict[str, Any]]:
    lines = text.splitlines()
    # Frontmatter is discovery metadata, not an instruction block.
    if lines and lines[0].strip() == "---":
        try:
            end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
            lines = [""] * (end + 1) + lines[end + 1:]
        except StopIteration:
            pass

    blocks: list[dict[str, Any]] = []
    current: list[str] = []
    first_line = 0
    code_fence = False

    def finish() -> None:
        nonlocal current, first_line
        if current:
            body = " ".join(current)
            words = len(WORD_RE.findall(body))
            if words >= minimum_words:
                blocks.append({
                    "line": first_line,
                    "words": words,
                    "normalized": normalized(body),
                })
            current = []
            first_line = 0

    for index, line in enumerate(lines, start=1):
        strip = line.strip()
        if strip.startswith("```") or strip.startswith("~~~"):
            finish()
            code_fence = not code_fence
            continue
        if code_fence or not strip or strip.startswith(("#", "|")):
            finish()
            continue
        if not current:
            first_line = index
        current.append(strip)
    finish()
    return blocks


def audit(root: Path, minimum_words: int = 18, limit: int = 30) -> dict[str, Any]:
    if minimum_words < 1 or limit < 1:
        raise ValueError("minimum_words and limit must be positive")
    if not root.is_dir():
        raise ValueError("repository root is not a directory")

    files = sorted(
        path for path in root.rglob("SKILL.md")
        if path.is_file()
        and not any(part in {".git", ".github", "Evals", "tests", "tools", ".venv"}
                    for part in path.relative_to(root).parts)
    )
    owners: dict[str, list[dict[str, Any]]] = defaultdict(list)
    word_counts: dict[str, int] = {}

    for path in files:
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        word_counts[rel] = len(WORD_RE.findall(text))
        seen: set[str] = set()
        for block in instruction_blocks(text, minimum_words):
            key = block["normalized"]
            if key in seen:
                continue  # within-file repetition does not become a cross-skill finding
            seen.add(key)
            owners[key].append({"path": rel, "line": block["line"], "words": block["words"]})

    repeated = [
        {"text_sha256": hashlib.sha256(key.encode("utf-8")).hexdigest(),
         "word_count": len(WORD_RE.findall(key)),
         "locations": locations}
        for key, locations in owners.items()
        if len({x["path"] for x in locations}) > 1
    ]
    repeated.sort(key=lambda e: (-len(e["locations"]), -e["word_count"], e["text_sha256"]))
    count = len(repeated)
    return {
        "schema_version": 1,
        "status": "CANDIDATES_ONLY",
        "method": "identical normalized paragraphs across distinct SKILL.md files; no semantic inference",
        "skill_files": len(files),
        "total_skill_words_approx": sum(word_counts.values()),
        "minimum_block_words": minimum_words,
        "duplicate_groups_found": count,
        "duplicate_groups_returned": min(limit, count),
        "groups": repeated[:limit],
        "limitations": [
            "Matching detects only lexically identical paragraph blocks, not paraphrases or contradictions.",
            "Common safety gates may be deliberately repeated; a match does not authorize deletion.",
            "No actual token use, runtime cost, or behavioral improvement was measured.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--min-words", type=int, default=18)
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--json", action="store_true", help="Print complete JSON report")
    args = parser.parse_args()
    try:
        report = audit(args.repo.resolve(), args.min_words, args.limit)
    except (ValueError, OSError, UnicodeError) as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Skill redundancy candidates: {report['duplicate_groups_found']} groups "
              f"across {report['skill_files']} SKILL.md files")
        for item in report["groups"]:
            refs = ", ".join(f"{x['path']}:{x['line']}" for x in item["locations"])
            print(f"  {item['word_count']} words / {item['text_sha256'][:12]}: {refs}")
        print("Report only; review context and semantics before making changes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
