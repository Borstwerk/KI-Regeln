#!/usr/bin/env python3
"""Check public navigation and the bounded, explicit project-search manifest.

Read-only and standard-library-only. This does NOT validate translation meaning,
off-site links, Markdown rendering, embeddings, agent routing or release readiness.
"""
from __future__ import annotations

import fnmatch
import json
import re
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ENTRYPOINTS = ("README.md", "START-HIER.md", "START-HERE.md")
SCANNED = (*ENTRYPOINTS, "AGENTS.md", "Dokumentation/Public-Entrypoints-und-Sprachpflege.md",
           "PROJECT.md", "CONTRIBUTING.md", "Skill-Engineering/README.md",
           "Sicherheit/README.md", "Testing-und-QA/README.md")
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
    "PROJECT.md": {"AGENTS.md", "Dokumentation/Skill-Handbuch.md", "CONTRIBUTING.md",
                   "Skill-Engineering/README.md", "Sicherheit/README.md", "Testing-und-QA/README.md"},
}
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
MAX_PROJECT_DOCS = 200
MAX_PROJECT_FILE_BYTES = 256 * 1024
MAX_PROJECT_BYTES = 1024 * 1024
PROJECT_CORE = {"PROJECT.md", "README.md", "START-HIER.md", "AGENTS.md", "CONTRIBUTING.md",
                "Dokumentation/Skill-Handbuch.md", "Skill-Engineering/README.md",
                "Sicherheit/README.md", "Testing-und-QA/README.md"}


def validate_project_manifest(root: Path = ROOT) -> tuple[list[str], dict[str, int]]:
    """Validate this repo's literal-file pilot; do not implement a search engine."""
    root = root.resolve()
    errors: list[str] = []
    sizes: list[int] = []
    try:
        data = json.loads((root / "mara-project.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as exc:
        return [f"mara-project.json: cannot read manifest ({type(exc).__name__})"], {}
    if not isinstance(data, dict):
        return ["mara-project.json: expected object"], {}
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        errors.append("mara-project.json: expected schema_version 1")
    if data.get("id") != "ki-regeln" or data.get("kind") != "collection":
        errors.append("mara-project.json: expected ki-regeln collection")
    entries, search = data.get("entrypoints"), data.get("search")
    if not isinstance(entries, dict) or set(entries) != {"overview", "contents", "status", "plan"}:
        errors.append("mara-project.json: four project entrypoint roles required")
        entries = {}
    if not isinstance(search, dict) or any(not isinstance(search.get(k), list) for k in ("include", "exclude")):
        return errors + ["mara-project.json: search.include/exclude must be lists"], {}
    included, excluded = search["include"], search["exclude"]
    if any(not isinstance(x, str) or not x or "\\" in x or PurePosixPath(x).is_absolute()
           or ".." in PurePosixPath(x).parts or ":" in x for x in excluded):
        return errors + ["mara-project.json: unsafe exclude pattern"], {}
    seen: set[str] = set()
    forbidden_parts = {"evals", "tests", "raw", "archive", "archiv", "reports", "vendor", "node_modules", "original"}
    for label, values in (("entrypoints", list(entries.values())), ("search.include", included)):
        for value in values:
            if (not isinstance(value, str) or not value or "\\" in value or ":" in value
                    or any(c in value for c in "*?[]#") or value.startswith("/")
                    or any(p in ("", ".", "..") or p.startswith(".") for p in value.split("/"))
                    or PurePosixPath(value).suffix.lower() != ".md"):
                errors.append(f"{label}: expected explicit safe Markdown file: {value!r}")
                continue
            parts = PurePosixPath(value).parts
            target = root.joinpath(*parts)
            if any(root.joinpath(*parts[:i]).is_symlink()
                   or root.joinpath(*parts[:i]).is_junction() for i in range(1, len(parts) + 1)):
                errors.append(f"{label}: symlink/junction not allowed: {value}")
                continue
            if not target.resolve().is_relative_to(root) or not target.is_file():
                errors.append(f"{label}: missing or escaping file: {value}")
                continue
            if label == "search.include":
                if value.casefold() in seen:
                    errors.append(f"search.include: duplicate file: {value}")
                    continue
                seen.add(value.casefold())
                if (any(p.casefold() in forbidden_parts for p in parts)
                        or any(fnmatch.fnmatchcase(value.casefold(), x.casefold()) for x in excluded)):
                    errors.append(f"search.include: excluded source selected: {value}")
                    continue
                try:
                    body = target.read_bytes()
                    body.decode("utf-8")
                except (OSError, UnicodeError):
                    errors.append(f"search.include: unreadable UTF-8: {value}")
                    continue
                sizes.append(len(body))
                if len(body) > MAX_PROJECT_FILE_BYTES:
                    errors.append(f"search.include: file above 256 KiB: {value}")
    for name in sorted(PROJECT_CORE - set(x for x in included if isinstance(x, str))):
        errors.append(f"search.include: required pilot entry absent: {name}")
    if len(included) > MAX_PROJECT_DOCS:
        errors.append("search.include: more than 200 documents")
    if sum(sizes) > MAX_PROJECT_BYTES:
        errors.append("search.include: total above 1 MiB")
    return errors, {"documents": len(sizes), "utf8_bytes": sum(sizes), "max_file_bytes": max(sizes, default=0)}


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
    project_issues, metrics = validate_project_manifest()
    issues.extend(project_issues)
    for issue in issues:
        print("DOC-ENTRY: " + issue, file=sys.stderr)
    if issues:
        print(f"Public entrypoints: FAIL ({len(issues)} issue(s))", file=sys.stderr)
        return 1
    print("Public entrypoints: PASS (links/navigation/landing-size; NOT translation semantics)")
    print("Project search selection: PASS " + json.dumps(metrics, sort_keys=True)
          + " (NOT embeddings, agent answers or a live index)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
