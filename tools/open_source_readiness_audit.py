#!/usr/bin/env python3
"""Read-only open-source readiness audit for KI-Regeln.

The audit deliberately separates deterministic repository facts from review signals.
It never decides copyright or license compatibility from text similarity.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import html
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
from typing import Any
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen

import yaml

ROOT = Path(__file__).resolve().parents[1]

DERIVATION_RE = re.compile(
    r"\b(adapted\s+from|based\s+on|copied\s+from|derived\s+from|"
    r"übernommen\s+aus|adaptiert\s+von|basiert\s+auf|inspiriert\s+von|inspired\s+by)\b",
    re.I,
)
LICENSE_NAME_RE = re.compile(r"^(license|copying|notice)(?:[._-].*)?$", re.I)
TEXT_EXTENSIONS = {
    ".md", ".txt", ".yml", ".yaml", ".json", ".py", ".ps1", ".sh", ".sql",
    ".html", ".css", ".js", ".ts", ".tsx", ".jsx", ".xml", ".xsl", ".xslt",
    ".csv", ".toml", ".ini", ".cfg", ".conf", ".properties", ".patch", ".diff",
}
KNOWN_BINARY_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svgz", ".pdf", ".zip", ".ico",
}
SENSITIVE_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("private-key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("github-pat", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b")),
    ("aws-access-key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("credentialed-url", re.compile(r"\b[a-z][a-z0-9+.-]*://[^\s/:@]+:[^\s/@]+@", re.I)),
    ("connection-string-password", re.compile(r"(?i)\b(?:password|pwd)\s*=\s*[^;\s]{4,}")),
    ("bearer-token-literal", re.compile(r"(?i)\bAuthorization\s*:\s*Bearer\s+[A-Za-z0-9._~+/=-]{16,}")),
]
CONTEXT_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("email-address", re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)),
    ("private-ipv4", re.compile(r"\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b")),
    ("internal-hostname", re.compile(r"\b[a-z0-9][a-z0-9.-]*\.(?:internal|corp|local)\b", re.I)),
    ("confidential-marker", re.compile(r"(?i)\b(confidential|vertraulich|intern(?:al)?[- ]only)\b")),
    ("patient-marker", re.compile(r"(?i)\b(patient(?:en|in|innen)?|patientendaten)\b")),
    ("customer-marker", re.compile(r"(?i)\b(kundendaten|customer data|client data)\b")),
]


def run(*args: str, check: bool = True) -> str:
    proc = subprocess.run(args, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and proc.returncode:
        raise RuntimeError(f"command failed ({proc.returncode}): {' '.join(args)}\n{proc.stderr}")
    return proc.stdout


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def tracked_files() -> list[str]:
    return [line for line in run("git", "ls-files").splitlines() if line]


def is_probably_text(data: bytes, path: str) -> bool:
    if Path(path).suffix.lower() in TEXT_EXTENSIONS:
        return True
    if b"\x00" in data[:8192]:
        return False
    try:
        data[:65536].decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False


def safe_text(path: Path, max_bytes: int = 4_000_000) -> str | None:
    try:
        data = path.read_bytes()
    except OSError:
        return None
    if len(data) > max_bytes or not is_probably_text(data, str(path)):
        return None
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return None


def scan_text(path: str, text: str) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for category, pattern in SENSITIVE_PATTERNS:
            if pattern.search(line):
                findings.append({"path": path, "line": lineno, "class": category, "severity": "potential-secret"})
        for category, pattern in CONTEXT_PATTERNS:
            if pattern.search(line):
                findings.append({"path": path, "line": lineno, "class": category, "severity": "review-context"})
    return findings


def current_tree_scan(files: list[str]) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    binaries: list[dict[str, Any]] = []
    derivations: list[dict[str, Any]] = []
    for rel in files:
        path = ROOT / rel
        try:
            data = path.read_bytes()
        except OSError:
            continue
        if not is_probably_text(data, rel):
            binaries.append({
                "path": rel,
                "size": len(data),
                "extension": Path(rel).suffix.lower(),
                "known_binary_type": Path(rel).suffix.lower() in KNOWN_BINARY_EXTENSIONS,
            })
            continue
        if len(data) > 4_000_000:
            findings.append({"path": rel, "line": None, "class": "large-text-not-scanned", "severity": "review-context"})
            continue
        text = data.decode("utf-8", errors="replace")
        findings.extend(scan_text(rel, text))
        for lineno, line in enumerate(text.splitlines(), 1):
            if DERIVATION_RE.search(line):
                derivations.append({"path": rel, "line": lineno})
    return {"findings": findings, "binaries": binaries, "derivation_markers": derivations}


def scan_blob(sha: str, path_hint: str | None) -> tuple[list[dict[str, Any]], bool, int]:
    data = subprocess.check_output(["git", "cat-file", "blob", sha], cwd=ROOT)
    size = len(data)
    if size > 4_000_000 or not is_probably_text(data, path_hint or ""):
        return [], False, size
    text = data.decode("utf-8", errors="replace")
    results = []
    for finding in scan_text(path_hint or f"blob:{sha[:12]}", text):
        finding["blob"] = sha
        results.append(finding)
    return results, True, size


def history_scan() -> dict[str, Any]:
    # Scope: objects reachable from refs available in the local full-history clone.
    refs = [line for line in run("git", "for-each-ref", "--format=%(refname)").splitlines() if line]
    raw = run("git", "rev-list", "--objects", "--all")
    first_path: dict[str, str | None] = {}
    for line in raw.splitlines():
        if not line:
            continue
        parts = line.split(" ", 1)
        first_path.setdefault(parts[0], parts[1] if len(parts) == 2 else None)
    blob_shas: list[str] = []
    if first_path:
        proc = subprocess.Popen(
            ["git", "cat-file", "--batch-check=%(objectname) %(objecttype)"],
            cwd=ROOT,
            text=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        assert proc.stdin is not None and proc.stdout is not None
        for sha in first_path:
            proc.stdin.write(sha + "\n")
        proc.stdin.close()
        for line in proc.stdout:
            sha, kind = line.strip().split(" ", 1)
            if kind == "blob":
                blob_shas.append(sha)
        proc.wait()
    findings: list[dict[str, Any]] = []
    binary_count = 0
    large_count = 0
    for sha in blob_shas:
        path_hint = first_path.get(sha)
        try:
            results, text_scanned, size = scan_blob(sha, path_hint)
        except subprocess.CalledProcessError:
            continue
        if size > 4_000_000:
            large_count += 1
        elif not text_scanned:
            binary_count += 1
        findings.extend(results)
    return {
        "scope": "all objects reachable from refs present in the full-history checkout",
        "refs": refs,
        "unique_reachable_blobs": len(blob_shas),
        "binary_blobs_not_text_scanned": binary_count,
        "large_blobs_not_text_scanned": large_count,
        "findings": findings,
    }


class HTMLText(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.skip = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript"}:
            self.skip += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self.skip:
            self.skip -= 1

    def handle_data(self, data: str) -> None:
        if not self.skip:
            self.parts.append(data)


def normalize_words(text: str) -> list[str]:
    text = html.unescape(text).lower()
    return re.findall(r"[a-z0-9äöüß][a-z0-9äöüß'_-]*", text, re.I)


def normalized_long_lines(text: str) -> set[str]:
    result: set[str] = set()
    for line in text.splitlines():
        clean = " ".join(normalize_words(line))
        if len(clean) >= 70 and len(clean.split()) >= 10:
            result.add(clean)
    return result


def shingles(words: list[str], n: int = 12) -> set[str]:
    if len(words) < n:
        return set()
    return {" ".join(words[i:i+n]) for i in range(len(words) - n + 1)}


def similarity_metrics(upstream: str, local: str) -> dict[str, Any]:
    ulines = normalized_long_lines(upstream)
    llines = normalized_long_lines(local)
    exact_lines = len(ulines & llines)
    ush = shingles(normalize_words(upstream))
    lsh = shingles(normalize_words(local))
    common_shingles = len(ush & lsh)
    if exact_lines >= 2 or common_shingles >= 8:
        signal = "high"
    elif exact_lines >= 1 or common_shingles >= 3:
        signal = "medium"
    elif common_shingles >= 1:
        signal = "low"
    else:
        signal = "none"
    return {
        "signal": signal,
        "exact_long_line_count": exact_lines,
        "common_12_word_shingle_count": common_shingles,
    }


def github_repo_name(source: dict[str, Any]) -> str | None:
    raw = source.get("repository")
    if isinstance(raw, str) and "/" in raw and not raw.startswith("http"):
        return raw.strip("/")
    url = source.get("source_url") or source.get("snapshot_url") or source.get("url")
    if isinstance(url, str):
        parsed = urlparse(url)
        if parsed.hostname and parsed.hostname.lower() == "github.com":
            parts = [p for p in parsed.path.split("/") if p]
            if len(parts) >= 2:
                return f"{parts[0]}/{parts[1]}".removesuffix(".git")
    return None


class GitHubAPI:
    def __init__(self, token: str | None) -> None:
        self.token = token
        self.cache: dict[str, Any] = {}
        self.calls = 0

    def get(self, path_or_url: str, *, optional: bool = False) -> Any:
        if path_or_url.startswith("http"):
            url = path_or_url
        else:
            url = "https://api.github.com" + path_or_url
        if url in self.cache:
            return self.cache[url]
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "KI-Regeln-readiness-audit"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        req = Request(url, headers=headers)
        try:
            with urlopen(req, timeout=30) as response:
                data = json.loads(response.read().decode("utf-8"))
        except Exception as exc:
            if optional:
                self.cache[url] = None
                return None
            raise RuntimeError(f"GitHub API request failed for {url}: {type(exc).__name__}") from exc
        self.calls += 1
        self.cache[url] = data
        return data


def decode_content(obj: Any) -> str | None:
    if not isinstance(obj, dict):
        return None
    content = obj.get("content")
    if isinstance(content, str) and obj.get("encoding") == "base64":
        try:
            return base64.b64decode(content).decode("utf-8", errors="replace")
        except Exception:
            return None
    return None


def detect_license_text(text: str) -> str:
    low = text.lower()
    if "apache license" in low and "version 2.0" in low:
        return "Apache-2.0"
    if "permission is hereby granted, free of charge" in low and "the software" in low:
        return "MIT"
    if "creative commons attribution 4.0 international" in low or "cc by 4.0" in low:
        return "CC-BY-4.0"
    if "bsd 3-clause" in low or ("redistribution and use in source and binary forms" in low and "neither the name" in low):
        return "BSD-3-Clause"
    if "mozilla public license" in low and "2.0" in low:
        return "MPL-2.0"
    if "gnu general public license" in low and "version 3" in low:
        return "GPL-3.0-only"
    return "UNKNOWN"


def artifact_license_declarations(text: str) -> list[str]:
    hits: list[str] = []
    first = "\n".join(text.splitlines()[:80])
    patterns = [
        r"(?im)^\s*(?:license|license_spdx|spdx-license-identifier)\s*:\s*['\"]?([^'\"\n#]+)",
        r"(?im)SPDX-License-Identifier:\s*([^\s]+)",
        r"(?i)\b(CC-BY-4\.0|Apache-2\.0|MIT License|GPL-3\.0|MPL-2\.0)\b",
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, first):
            value = " ".join(match.group(1).strip().split())
            if value and value not in hits:
                hits.append(value)
    return hits


def directory_license_files(api: GitHubAPI, repo: str, commit: str, source_path: str) -> list[dict[str, Any]]:
    parts = source_path.split("/")[:-1]
    dirs = ["/".join(parts[:i]) for i in range(len(parts), -1, -1)]
    found: list[dict[str, Any]] = []
    seen_paths: set[str] = set()
    for directory in dirs:
        encoded = quote(directory, safe="/")
        endpoint = f"/repos/{repo}/contents/{encoded}?ref={quote(commit)}" if directory else f"/repos/{repo}/contents?ref={quote(commit)}"
        listing = api.get(endpoint, optional=True)
        if not isinstance(listing, list):
            continue
        for item in listing:
            name = item.get("name") if isinstance(item, dict) else None
            path = item.get("path") if isinstance(item, dict) else None
            if not isinstance(name, str) or not isinstance(path, str) or not LICENSE_NAME_RE.match(name):
                continue
            if path in seen_paths:
                continue
            seen_paths.add(path)
            obj = api.get(f"/repos/{repo}/contents/{quote(path, safe='/')}?ref={quote(commit)}", optional=True)
            text = decode_content(obj) or ""
            found.append({
                "path": path,
                "blob_sha": obj.get("sha") if isinstance(obj, dict) else None,
                "detected_spdx": detect_license_text(text),
            })
    return found


def find_observed_commit(api: GitHubAPI, repo: str, path: str, ref: str, observed_blob: str) -> tuple[str | None, dict[str, Any] | None, str]:
    try:
        commit_obj = api.get(f"/repos/{repo}/commits/{quote(ref, safe='')}")
        commit_sha = commit_obj.get("sha") if isinstance(commit_obj, dict) else None
    except Exception:
        commit_sha = None
    if isinstance(commit_sha, str):
        content = api.get(f"/repos/{repo}/contents/{quote(path, safe='/')}?ref={commit_sha}", optional=True)
        if isinstance(content, dict) and content.get("sha") == observed_blob:
            return commit_sha, content, "ref-resolved"
    commits = api.get(f"/repos/{repo}/commits?path={quote(path, safe='')}&per_page=100", optional=True)
    if isinstance(commits, list):
        for item in commits:
            sha = item.get("sha") if isinstance(item, dict) else None
            if not isinstance(sha, str):
                continue
            content = api.get(f"/repos/{repo}/contents/{quote(path, safe='/')}?ref={sha}", optional=True)
            if isinstance(content, dict) and content.get("sha") == observed_blob:
                return sha, content, "path-history-resolved"
    return None, None, "not-resolved"


def audit_github_sources(sources: list[dict[str, Any]], token: str | None) -> dict[str, Any]:
    api = GitHubAPI(token)
    records: list[dict[str, Any]] = []
    for index, source in enumerate(sources, 1):
        sid = str(source.get("id"))
        repo = github_repo_name(source)
        path = source.get("path")
        ref = source.get("ref") or "main"
        observed_blob = source.get("observed_sha")
        record: dict[str, Any] = {
            "source_id": sid,
            "repository": repo,
            "source_path": path,
            "observed_ref": ref,
            "observed_blob_sha": observed_blob,
            "local_impact": source.get("local_impact") or [],
            "repository_commit": None,
            "commit_resolution": "not-attempted",
            "artifact_license_declarations": [],
            "license_files": [],
            "similarity": [],
            "explicit_local_derivation_marker": False,
            "review_signal": "clear-reference-candidate",
            "errors": [],
        }
        if not all(isinstance(value, str) and value for value in (repo, path, ref, observed_blob)):
            record["errors"].append("registry-fields-missing")
            record["review_signal"] = "needs-human/legal-review"
            records.append(record)
            continue
        try:
            commit, content_obj, resolution = find_observed_commit(api, repo, path, ref, observed_blob)
            record["repository_commit"] = commit
            record["commit_resolution"] = resolution
            upstream_text = decode_content(content_obj) or ""
            if commit:
                record["artifact_license_declarations"] = artifact_license_declarations(upstream_text)
                record["license_files"] = directory_license_files(api, repo, commit, path)
            else:
                record["errors"].append("historical-commit-not-resolved")
            strongest = "none"
            rank = {"none": 0, "low": 1, "medium": 2, "high": 3}
            for impact in source.get("local_impact") or []:
                local_path = ROOT / impact
                local_text = safe_text(local_path)
                if local_text is None:
                    record["similarity"].append({"path": impact, "signal": "not-text-or-missing"})
                    continue
                metrics = similarity_metrics(upstream_text, local_text) if upstream_text else {
                    "signal": "not-compared", "exact_long_line_count": 0, "common_12_word_shingle_count": 0
                }
                marker = bool(DERIVATION_RE.search(local_text))
                record["explicit_local_derivation_marker"] = record["explicit_local_derivation_marker"] or marker
                metrics["path"] = impact
                metrics["derivation_marker_present"] = marker
                record["similarity"].append(metrics)
                if metrics.get("signal") in rank and rank[metrics["signal"]] > rank[strongest]:
                    strongest = metrics["signal"]
            if record["explicit_local_derivation_marker"] or strongest == "high":
                record["review_signal"] = "needs-human/legal-review"
            elif strongest == "medium":
                record["review_signal"] = "expression-similarity-review"
            else:
                record["review_signal"] = "clear-reference-candidate"
        except Exception as exc:
            record["errors"].append(type(exc).__name__)
            record["review_signal"] = "needs-human/legal-review"
        records.append(record)
        print(f"github-source {index}/{len(sources)}: {sid} -> {record['review_signal']}", file=sys.stderr)
    return {"api_calls": api.calls, "records": records}


def fetch_web_text(url: str) -> tuple[str | None, str | None]:
    req = Request(url, headers={"User-Agent": "KI-Regeln-readiness-audit/1.0"})
    try:
        with urlopen(req, timeout=25) as response:
            content_type = response.headers.get("Content-Type", "")
            data = response.read(5_000_000)
    except Exception as exc:
        return None, type(exc).__name__
    if "text/html" in content_type:
        parser = HTMLText()
        parser.feed(data.decode("utf-8", errors="replace"))
        return "\n".join(parser.parts), None
    if content_type.startswith("text/") or "json" in content_type or "xml" in content_type:
        return data.decode("utf-8", errors="replace"), None
    return None, f"unsupported-content-type:{content_type.split(';')[0]}"


def audit_non_github_sources(sources: list[dict[str, Any]]) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    for index, source in enumerate(sources, 1):
        sid = str(source.get("id"))
        url = source.get("url")
        record: dict[str, Any] = {
            "source_id": sid,
            "kind": source.get("kind"),
            "url": url,
            "local_impact": source.get("local_impact") or [],
            "fetch_status": "not-attempted",
            "similarity": [],
            "explicit_local_derivation_marker": False,
            "review_signal": "clear-reference-candidate",
        }
        source_text: str | None = None
        if isinstance(url, str) and url.startswith(("http://", "https://")):
            source_text, error = fetch_web_text(url)
            record["fetch_status"] = "fetched" if source_text is not None else error
        else:
            record["fetch_status"] = "no-fetchable-url"
        strongest = "none"
        rank = {"none": 0, "low": 1, "medium": 2, "high": 3}
        for impact in source.get("local_impact") or []:
            local_text = safe_text(ROOT / impact)
            if local_text is None:
                record["similarity"].append({"path": impact, "signal": "not-text-or-missing"})
                continue
            marker = bool(DERIVATION_RE.search(local_text))
            record["explicit_local_derivation_marker"] = record["explicit_local_derivation_marker"] or marker
            metrics = similarity_metrics(source_text, local_text) if source_text else {
                "signal": "not-compared", "exact_long_line_count": 0, "common_12_word_shingle_count": 0
            }
            metrics["path"] = impact
            metrics["derivation_marker_present"] = marker
            record["similarity"].append(metrics)
            if metrics.get("signal") in rank and rank[metrics["signal"]] > rank[strongest]:
                strongest = metrics["signal"]
        if record["explicit_local_derivation_marker"] or strongest == "high":
            record["review_signal"] = "needs-human/legal-review"
        elif strongest == "medium":
            record["review_signal"] = "expression-similarity-review"
        elif source_text is None:
            record["review_signal"] = "reference-only-not-text-compared"
        records.append(record)
        print(f"non-github-source {index}/{len(sources)}: {sid} -> {record['review_signal']}", file=sys.stderr)
    return {"records": records}


def source_inventory(files: list[str]) -> dict[str, Any]:
    registry = load_yaml(ROOT / "Dokumentation/upstream-sources.yml") or {}
    sources = registry.get("sources") or []
    by_kind: dict[str, int] = {}
    for source in sources:
        by_kind[str(source.get("kind"))] = by_kind.get(str(source.get("kind")), 0) + 1
    qi = sorted(path for path in files if path.endswith("Quellen-und-Inspirationen.md"))
    workflows = sorted(path for path in files if path.startswith(".github/workflows/") and path.endswith((".yml", ".yaml")))
    governance_names = [
        "README.md", "CONTRIBUTING.md", "SECURITY.md", "ACKNOWLEDGEMENTS.md", "LICENSE", "LICENSE.md",
        "THIRD-PARTY-NOTICES.md", "CODE_OF_CONDUCT.md", ".github/dependabot.yml",
    ]
    return {
        "tracked_file_count": len(files),
        "sources_total": len(sources),
        "sources_by_kind": dict(sorted(by_kind.items())),
        "github_file_sources": sum(1 for s in sources if s.get("kind") == "github-file"),
        "quellen_und_inspirationen": qi,
        "github_workflows": workflows,
        "governance_files": {name: (ROOT / name).is_file() for name in governance_names},
    }


def scan_quellen_registry(files: list[str], sources: list[dict[str, Any]]) -> dict[str, Any]:
    registry_urls: set[str] = set()
    for source in sources:
        for key in ("url", "source_url", "snapshot_url"):
            value = source.get(key)
            if isinstance(value, str) and value.startswith("http"):
                registry_urls.add(value.rstrip("/"))
    entries: list[dict[str, Any]] = []
    url_re = re.compile(r"https?://[^\s)>\]}]+")
    for path in sorted(p for p in files if p.endswith("Quellen-und-Inspirationen.md")):
        text = safe_text(ROOT / path) or ""
        urls = sorted({m.group(0).rstrip(".,;/") for m in url_re.finditer(text)})
        unregistered = [url for url in urls if url.rstrip("/") not in registry_urls]
        entries.append({"path": path, "url_count": len(urls), "unregistered_urls": unregistered})
    return {"files": entries, "unregistered_url_count": sum(len(x["unregistered_urls"]) for x in entries)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="open-source-readiness-audit.json")
    parser.add_argument("--github", action="store_true", help="Audit concrete GitHub artifacts using GitHub API")
    parser.add_argument("--non-github", action="store_true", help="Fetch and compare non-GitHub sources when possible")
    parser.add_argument("--history", action="store_true", help="Scan reachable Git history; requires full checkout")
    args = parser.parse_args()

    files = tracked_files()
    registry = load_yaml(ROOT / "Dokumentation/upstream-sources.yml") or {}
    sources = registry.get("sources") or []
    github_sources = [s for s in sources if s.get("kind") == "github-file"]
    non_github_sources = [s for s in sources if s.get("kind") != "github-file"]

    result: dict[str, Any] = {
        "schema_version": 1,
        "repository_head": run("git", "rev-parse", "HEAD").strip(),
        "inventory": source_inventory(files),
        "quellen_registry_crosscheck": scan_quellen_registry(files, sources),
        "current_tree": current_tree_scan(files),
        "history": {"status": "not-run"},
        "github_provenance_audit": {"status": "not-run", "records": []},
        "non_github_source_audit": {"status": "not-run", "records": []},
    }
    if args.history:
        result["history"] = history_scan()
    if args.github:
        token = os.environ.get("GITHUB_TOKEN")
        gh = audit_github_sources(github_sources, token)
        gh["status"] = "run"
        result["github_provenance_audit"] = gh
    if args.non_github:
        ng = audit_non_github_sources(non_github_sources)
        ng["status"] = "run"
        result["non_github_source_audit"] = ng

    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    current = result["current_tree"]
    history = result["history"]
    gh_records = result["github_provenance_audit"].get("records", [])
    ng_records = result["non_github_source_audit"].get("records", [])
    print(f"Tracked files: {len(files)}")
    print(f"Sources: {len(sources)} (GitHub files: {len(github_sources)}, non-GitHub: {len(non_github_sources)})")
    print(f"Quellen-und-Inspirationen files: {len(result['inventory']['quellen_und_inspirationen'])}")
    print(f"Current-tree potential-secret findings: {sum(1 for f in current['findings'] if f['severity'] == 'potential-secret')}")
    print(f"Current-tree context-review findings: {sum(1 for f in current['findings'] if f['severity'] == 'review-context')}")
    print(f"Current-tree binary files: {len(current['binaries'])}")
    if args.history:
        print(f"History reachable blobs: {history['unique_reachable_blobs']}")
        print(f"History potential-secret findings: {sum(1 for f in history['findings'] if f['severity'] == 'potential-secret')}")
        print(f"History context-review findings: {sum(1 for f in history['findings'] if f['severity'] == 'review-context')}")
    if args.github:
        counts: dict[str, int] = {}
        for record in gh_records:
            counts[record["review_signal"]] = counts.get(record["review_signal"], 0) + 1
        print("GitHub provenance review signals: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
        print(f"GitHub API calls: {result['github_provenance_audit'].get('api_calls', 0)}")
    if args.non_github:
        counts = {}
        for record in ng_records:
            counts[record["review_signal"]] = counts.get(record["review_signal"], 0) + 1
        print("Non-GitHub review signals: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    print(f"Audit JSON: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
