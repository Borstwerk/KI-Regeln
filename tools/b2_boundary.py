#!/usr/bin/env python3
"""Execution boundary for agent-controlled code in the Phase 4.2C / B2 eval.

The problem this exists for: B2's verification artifacts are writable by design, and the
check runner among them. An agent can put arbitrary code into a file that is then executed.
A tool policy is not a boundary against that, and neither is a scrubbed environment — it
protects environment variables and nothing about the filesystem. Without a real boundary the
one allowed check invocation is a full bypass: read the repository, read the case matrix,
find the trust root, write outside the workspace.

So agent-controlled code runs inside a view that *does not contain* those things. Not
unreadable, not chmodded: absent.

Provider: an unprivileged-capable Linux namespace built with `unshare`, into which a minimal
root is assembled by bind mount and entered with `pivot_root`. The view carries a read-only
runtime, a fresh `/proc`, and the writable workspace copy. Nothing else exists in it.

This is a boundary for *this* purpose — keeping evaluation artifacts out of reach of code
the eval itself placed there. It is not a security sandbox against a determined attacker,
and no claim beyond what probes P1-P5 demonstrate is made anywhere in B2.

Fails closed. If the provider cannot be established, there is no degraded path: callers get
an error, and pilot readiness stays false.
"""
from __future__ import annotations

import argparse
import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

PROVIDER = "unshare-namespace/v1"
# Read-only host paths the runtime needs. Deliberately a fixed list: /home, /root, /tmp and
# the repository are absent from it, which is the entire point.
RUNTIME_BINDS = ("/usr", "/bin", "/sbin", "/lib", "/lib64", "/etc/alternatives")
WORKSPACE_MOUNT = "/workspace"
SCRATCH_MOUNT = "/scratch"
DEFAULT_TIMEOUT = 60
# Nothing from the caller's environment is inherited. The check gets a bare, fixed set.
VIEW_ENV = {
    "PATH": "/usr/local/bin:/usr/bin:/bin",
    "HOME": SCRATCH_MOUNT,
    "TMPDIR": SCRATCH_MOUNT,
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONHASHSEED": "0",
    "LC_ALL": "C.UTF-8",
    "NO_COLOR": "1",
}


class BoundaryError(RuntimeError):
    """The boundary could not be established, or was asked to do something unsafe."""


@dataclass(frozen=True)
class BoundaryResult:
    returncode: int
    stdout: str
    stderr: str
    provider: str = PROVIDER
    network_namespace_unshared: bool = True


@dataclass(frozen=True)
class ViewSpec:
    """One isolated execution view.

    `workspace` is the only writable path the code can reach, and it is always a copy: the
    graded artifact is never handed to the thing being graded.
    """

    workspace: Path
    argv: tuple[str, ...]
    extra_ro: tuple[tuple[str, Path], ...] = field(default=())
    timeout: int = DEFAULT_TIMEOUT
    stdin_text: str | None = None
    workdir: str = WORKSPACE_MOUNT

    def validate(self) -> None:
        if not self.workspace.is_dir():
            raise BoundaryError(f"view workspace is not a directory: {self.workspace}")
        if not self.argv:
            raise BoundaryError("view requires an argv")
        for mount, source in self.extra_ro:
            if not mount.startswith("/") or ".." in Path(mount).parts:
                raise BoundaryError(f"extra mount point must be a safe absolute path: {mount!r}")
            if mount in {WORKSPACE_MOUNT, SCRATCH_MOUNT} or mount.startswith(tuple(RUNTIME_BINDS)):
                raise BoundaryError(f"extra mount {mount!r} would shadow a reserved path")
            if not Path(source).exists():
                raise BoundaryError(f"extra mount source is missing: {source}")


def _script(spec: ViewSpec) -> str:
    """The shell program that assembles the view and then becomes the payload."""
    lines = [
        "set -eu",
        "mount --make-rprivate /",
        'R="$B2_ROOT"',
        # Every mount point is created before the root is sealed, because a read-only root
        # cannot have directories added to it afterwards.
        'mkdir -p "$R"/proc "$R"/dev "$R"/oldroot',
        f'mkdir -p "$R"{WORKSPACE_MOUNT} "$R"{SCRATCH_MOUNT}',
    ]
    for path in RUNTIME_BINDS:
        lines.append(f'if [ -e {shlex.quote(path)} ]; then mkdir -p "$R"{shlex.quote(path)}; fi')
    for mount, _ in spec.extra_ro:
        lines.append(f'mkdir -p "$R"{shlex.quote(mount)}')
    lines += [
        # Seal the root itself. Without this, agent-controlled code can still write into the
        # view's own filesystem -- /etc and / included. It is ephemeral, so nothing escapes
        # a run, but "writes only where it is meant to" is the contract, so it is enforced
        # rather than argued about. P2 is what caught this.
        'mount --bind "$R" "$R"',
        'mount -o remount,bind,ro "$R"',
    ]
    for path in RUNTIME_BINDS:
        lines += [
            f'if [ -e {shlex.quote(path)} ]; then',
            f'  mount --bind {shlex.quote(path)} "$R"{shlex.quote(path)}',
            f'  mount -o remount,bind,ro "$R"{shlex.quote(path)}',
            "fi",
        ]
    lines += [
        'mount -t proc proc "$R"/proc',
        # A minimal /dev: the three character devices a runtime expects, and nothing else.
        # Bound individually rather than by exposing the host /dev.
        'mount -t tmpfs -o size=1m tmpfs "$R"/dev',
        'for d in null zero urandom; do : > "$R"/dev/$d; mount --bind /dev/$d "$R"/dev/$d; done',
        # Writable, and only these two.
        f'mount --bind "$B2_WORKSPACE" "$R"{WORKSPACE_MOUNT}',
        f'mount -t tmpfs -o size=16m tmpfs "$R"{SCRATCH_MOUNT}',
    ]
    for i, (mount, _) in enumerate(spec.extra_ro):
        lines += [
            f'mount --bind "$B2_RO_{i}" "$R"{shlex.quote(mount)}',
            f'mount -o remount,bind,ro "$R"{shlex.quote(mount)}',
        ]
    lines += [
        'cd "$R"',
        "pivot_root . oldroot",
        # The old root is detached, so the host filesystem is not merely hidden by
        # permissions: after this line it is not reachable from inside the view at all.
        "umount -l /oldroot",
        f"cd {shlex.quote(spec.workdir)}",
        # `env -i` plus an explicit assignment list: the view gets a fixed, minimal
        # environment and inherits nothing from the caller. Without the assignments this
        # ran with an empty environment, which silently turned bytecode caching back on and
        # let the runtime write `__pycache__` into the graded workspace.
        "exec env -i " + " ".join(f"{k}={shlex.quote(v)}" for k, v in sorted(VIEW_ENV.items())) + ' "$@"',
    ]
    return "\n".join(lines)


def provider_available() -> tuple[bool, str]:
    """Can this host actually establish the boundary? Answered by doing it, not by guessing."""
    if sys.platform != "linux":
        return False, f"namespace provider needs Linux, host is {sys.platform}"
    if shutil.which("unshare") is None:
        return False, "unshare is not on PATH"
    try:
        with tempfile.TemporaryDirectory(prefix="b2-probe-") as tmp:
            workspace = Path(tmp) / "ws"
            workspace.mkdir()
            (workspace / "ok.txt").write_text("ok\n", encoding="utf-8")
            result = run_in_view(ViewSpec(
                workspace=workspace,
                argv=("/usr/bin/env", "python3", "-c",
                      "import json,os,pathlib;"
                      "print(pathlib.Path('/workspace/ok.txt').read_text().strip());"
                      "print(json.dumps({'root': sorted(os.listdir('/')),"
                      " 'oldroot': sorted(os.listdir('/oldroot')) if os.path.isdir('/oldroot') else []}))"),
                timeout=30,
            ))
    except BoundaryError as exc:
        return False, str(exc)
    if result.returncode != 0 or "ok" not in result.stdout:
        return False, f"probe run failed: rc={result.returncode} stderr={result.stderr[:200]!r}"
    seen = json.loads(result.stdout.strip().splitlines()[-1])
    forbidden = set(seen["root"]) & {"home", "root", "tmp", "opt", "srv", "var"}
    if forbidden:
        return False, f"probe view still exposes host paths: {sorted(forbidden)}"
    # `/oldroot` survives as an empty directory: the root is sealed read-only before
    # `pivot_root`, so it cannot be removed afterwards. What matters is that it is detached,
    # which is what an empty listing shows.
    if seen["oldroot"]:
        return False, f"the old root is still populated: {seen['oldroot'][:5]}"
    return True, "unshare namespace with pivot_root established"


def run_in_view(spec: ViewSpec) -> BoundaryResult:
    """Run one argv inside an isolated view. Never falls back to an unisolated run."""
    spec.validate()
    if shutil.which("unshare") is None:
        raise BoundaryError("no boundary provider: unshare is not available, and there is no fallback")
    with tempfile.TemporaryDirectory(prefix="b2-view-") as tmp:
        root = Path(tmp) / "root"
        root.mkdir()
        env = {
            "B2_ROOT": str(root), "B2_WORKSPACE": str(spec.workspace.resolve()),
            "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
        }
        for i, (_, source) in enumerate(spec.extra_ro):
            env[f"B2_RO_{i}"] = str(Path(source).resolve())
        argv = [
            "unshare", "--mount", "--pid", "--net", "--uts", "--ipc", "--fork",
            "/bin/sh", "-c", _script(spec), "b2-boundary", *spec.argv,
        ]
        try:
            done = subprocess.run(
                argv, input=spec.stdin_text, text=True, capture_output=True,
                timeout=spec.timeout, env=env, cwd="/", check=False,
            )
        except subprocess.TimeoutExpired as exc:
            raise BoundaryError(f"view exceeded its {spec.timeout}s budget") from exc
        except OSError as exc:
            raise BoundaryError(f"cannot start the boundary: {exc}") from exc
    if done.returncode != 0 and "pivot_root" in done.stderr:
        raise BoundaryError(f"boundary could not be established: {done.stderr.strip()[:300]}")
    return BoundaryResult(done.returncode, done.stdout, done.stderr)


def copy_workspace(source: Path, destination: Path) -> Path:
    """Materialise a writable copy. Graded artifacts are never executed in place."""
    if destination.exists():
        raise BoundaryError(f"destination already exists: {destination}")
    shutil.copytree(source, destination)
    return destination


def _cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--probe", action="store_true", help="Report whether the provider works here")
    parser.add_argument("--workspace")
    parser.add_argument("command", nargs="*")
    args = parser.parse_args(argv)
    if args.probe:
        available, reason = provider_available()
        print(json.dumps({"provider": PROVIDER, "available": available, "reason": reason}, indent=2))
        return 0 if available else 1
    if not args.workspace or not args.command:
        parser.error("--workspace and a command are required unless --probe is given")
    try:
        result = run_in_view(ViewSpec(workspace=Path(args.workspace), argv=tuple(args.command)))
    except BoundaryError as exc:
        print(f"BOUNDARY_ERROR: {exc}", file=sys.stderr)
        return 2
    sys.stdout.write(result.stdout)
    sys.stderr.write(result.stderr)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(_cli())
