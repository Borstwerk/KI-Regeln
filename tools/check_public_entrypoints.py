#!/usr/bin/env python3
"""Check public entrypoint navigation and multilingual structural parity.

Read-only and standard-library-only. This does NOT validate translation meaning,
off-site links, Markdown rendering, agent routing or repository release readiness.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ENTRYPOINTS = ("README.md", "START-HIER.md", "START-HERE.md")
SCANNED = (*ENTRYPOINTS, "AGENTS.md", "Dokumentation/Public-Entrypoints-und-Sprachpflege.md")
REQUIRED_LINKS = {
    "README.md": {
        "START-HIER.md", "START-HERE.md", "AGENTS.md",
        "CONTRIBUTING.md", "ASSET-LICENSES.md",
        "Dokumentation/open-source-readiness.yml",
    },
    "START-HIER.md": {
        "START-HERE.md", "README.md", "PRAXISBEISPIELE.md",
        "Dokumentation/Nutzung-des-Repositories.md",
        "Dokumentation/Skill-Handbuch.md", "Dokumentation/Skill-Katalog.md",
        "AGENTS.md", "CONTRIBUTING.md",
    },
    "START-HERE.md": {
        "START-HIER.md", "README.md", "PRAXISBEISPIELE.md",
        "Dokumentation/Nutzung-des-Repositories.md",
        "Dokumentation/Skill-Handbuch.md", "Dokumentation/Skill-Katalog.md",
        "AGENTS.md", "CONTRIBUTING.md",
    },
}
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")


def local_targets(root: Path, relative: str, content: str) -> tuple[set[str], list[str]]:
    """Return normalized repository-relative targets plus broken/unsafe link errors."""
    root = root.resolve()
    source = (root / relative).resolve()
    found: set[str] = set()
    errors: list[str] = []
    for match in LINK_PATTERN.finditer(content):
        value = match.group(1).strip()
        # Markdown <angle wrapped links> and optional title are not part of the
        # minimal public docs link syntax. Reject instead of silently ignoring.
        if not value or " " in value or value.startswith("<"):
            errors.append(f"{relative}: unsupported link syntax: {value!r}")
            continue
        parsed = urlsplit(value)
        if parsed.scheme in ("https", "http", "mailto"):
            continue
        if parsed.scheme or parsed.netloc or value.startswith("//"):
            errors.append(f"{relative}: unsupported URL scheme: {value!r}")
            continue
        if not parsed.path:
            # Same-page anchors; heading/anchor validation is out of scope.
            continue
        if parsed.path.startswith("/"):
            errors.append(f"{relative}: absolute path not allowed: {value!r}")
            continue
        target = (source.parent / unquote(parsed.path)).resolve()
        try:
            name = target.relative_to(root).as_posix()
        except ValueError:
            errors.append(f"{relative}: link leaves repository: {value!r}")
            continue
        found.add(name)
        if not target.exists():
            errors.append(f"{relative}: missing link target: {name}")
    return found, errors


def validate_entries(root: Path = ROOT) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    for name in SCANNED:
        path = root / name
        if not path.is_file():
            errors.append(f"missing public entrypoint or guide: {name}")
            continue
        content = path.read_text(encoding="utf-8")
        targets, invalid = local_targets(root, name, content)
        errors.extend(invalid)
        if name in ENTRYPOINTS and not content.startswith("# "):
            errors.append(f"{name}: missing H1")
        for required in sorted(REQUIRED_LINKS.get(name, set()) - targets):
            errors.append(f"{name}: required navigation link absent: {required}")
    root_readme = root / "README.md"
    if root_readme.is_file() and root_readme.stat().st_size > 8500:
        errors.append("README.md: public landing page grew above 8500 bytes; move detail into docs")
    return errors


def main() -> int:
    issues = validate_entries()
    for issue in issues:
        print("DOC-ENTRY: " + issue, file=sys.stderr)
    if issues:
        print(f"Public entrypoints: FAIL ({len(issues)} issue(s))", file=sys.stderr)
        return 1
    print("Public entrypoints: PASS (links/navigation/landing-size; NOT translation semantics)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
