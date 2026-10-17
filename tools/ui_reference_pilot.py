#!/usr/bin/env python3
"""Prepare and verify an isolated, model-free two-arm UI reference pilot.

No agents, renderers, network calls, installations, or judges are run here.
Both arms receive byte-identical task, facts and KI-Regeln skill files.
Only arm B receives the pinned, curated third-party design reference.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

PILOT = Path("Evals/Webentwicklung/UI-Reference-Pilot")
COMMON = (
    PILOT / "runner-input/TASK.md",
    PILOT / "runner-input/facts.json",
    Path("Webentwicklung/Skills/frontend-design/SKILL.md"),
    Path("Webentwicklung/Skills/design-system/SKILL.md"),
    Path("Webentwicklung/Skills/greybox/SKILL.md"),
    Path("Webentwicklung/Skills/visual-verification/SKILL.md"),
)
REFERENCE = PILOT / "reference/ui-pro-max-curated.md"
ARMS = ("A-baseline", "B-reference")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def key(path: Path) -> str:
    """Platform-independent manifest key (always forward slashes)."""
    return path.as_posix()


def within(path: Path, root: Path) -> bool:
    return path == root or path.is_relative_to(root)


def _copy_file(repo: Path, target: Path, relative: Path) -> str:
    source = repo / relative
    if not source.is_file() or source.is_symlink():
        raise ValueError(f"Missing or symlinked fixture: {relative}")
    destination = target / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination, follow_symlinks=False)
    return digest(destination)


def prepare(repo_root: Path, out: Path) -> dict:
    repo = repo_root.resolve()
    output = out.resolve()
    if within(output, repo):
        raise ValueError("Output must be outside the repository")
    if output.exists() and any(output.iterdir()):
        raise ValueError("Output must be a new or empty directory")
    for relative in (*COMMON, REFERENCE):
        source = repo / relative
        if not source.is_file() or source.is_symlink():
            raise ValueError(f"Missing or symlinked fixture: {relative}")
    output.mkdir(parents=True, exist_ok=True)
    files = {}
    for arm in ARMS:
        target = output / arm
        files[arm] = {key(p): _copy_file(repo, target, p) for p in COMMON}
        if arm == "B-reference":
            files[arm][key(REFERENCE)] = _copy_file(repo, target, REFERENCE)
    manifest = {
        "schema_version": 1,
        "case": "UI-REFERENCE-SYNTH-01",
        "type": "prepared-fixtures-only",
        "model_runs": "NOT_RUN",
        "render_check": "NOT_RUN",
        "files": files,
    }
    (output / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    verify(output)
    return manifest


def verify(out: Path) -> dict:
    output = out.resolve()
    manifest_path = output / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != 1 or manifest.get("case") != "UI-REFERENCE-SYNTH-01":
        raise ValueError("Manifest contract mismatch")
    if set(manifest.get("files", {})) != set(ARMS):
        raise ValueError("Manifest arms mismatch")
    for arm in ARMS:
        current = manifest["files"][arm]
        if not isinstance(current, dict):
            raise ValueError(f"Invalid manifest entries for {arm}")
        expected = {key(p) for p in COMMON}
        if arm == "B-reference":
            expected.add(key(REFERENCE))
        if set(current) != expected:
            raise ValueError(f"Unexpected manifest paths in {arm}")
        root = output / arm
        observed = {key(p.relative_to(root)) for p in root.rglob("*") if p.is_file()}
        if observed != expected:
            raise ValueError(f"Unexpected or missing files in {arm}: {sorted(observed ^ expected)}")
        for p, recorded_hash in current.items():
            item = root / p
            if item.is_symlink() or not item.is_file() or digest(item) != recorded_hash:
                raise ValueError(f"Integrity mismatch: {arm}/{p}")
    for p in COMMON:
        if manifest["files"][ARMS[0]][key(p)] != manifest["files"][ARMS[1]][key(p)]:
            raise ValueError(f"Common input differs across arms: {p}")
    if key(REFERENCE) in manifest["files"]["A-baseline"]:
        raise ValueError("Baseline arm leaked the external reference")
    return {
        "contract": "PASS",
        "model_runs": "NOT_RUN",
        "render_check": "NOT_RUN",
        "case": manifest["case"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    p = sub.add_parser("prepare")
    p.add_argument("--repo", required=True, type=Path)
    p.add_argument("--out", required=True, type=Path)
    v = sub.add_parser("verify")
    v.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    try:
        result = prepare(args.repo, args.out) if args.action == "prepare" else verify(args.out)
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(json.dumps({"contract": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
