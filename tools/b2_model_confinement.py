#!/usr/bin/env python3
"""Confine the Claude Code process itself for a Phase 4.2C / B2 writable run.

The gap this closes. `run_in_view` confines the code the *agent writes* — the check suite
and the product module. It never confined the agent's own process. And a tool policy cannot
stand in for that, because Claude Code treats a class of read-only shell commands (`cat`,
`ls`, `find`, `grep`, `head`, `stat`, …) as permissible without a prompt even under
`--permission-mode dontAsk`, so `Bash(check)` was never the only executable Bash action.
Together with a launcher that embedded an absolute repository path, that was a route from
the workspace to the evaluator's own files.

So the model process runs inside the same namespace provider, one level further out:

    unshare(mount, pid, uts, ipc) + pivot_root
        /workspace     the B2 workspace, writable, and the process starts here
        /scratch       writable tmpfs; CLAUDE_CONFIG_DIR lives here
        /b2-runtime    two staged trusted modules, read-only
        /b2-bin        the check launcher, read-only, first on PATH
        runtime binds  read-only; no /home, no /root, no /tmp, no repository
        -> bin/check   nests a second view for the agent's own check code

The network namespace is deliberately *not* unshared here: the model process has to reach
its API. That is the one isolation this outer view does not provide, and it is stated rather
than implied. Every filesystem claim is demonstrated by the confinement probes.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Mapping

try:
    from .b2_boundary import (
        SCRATCH_MOUNT, WORKSPACE_MOUNT, BoundaryError, ViewSpec, confined_invocation,
    )
    from .b2_check_launcher import BIN_DIR, LAUNCHER_NAME, TRUSTED_RUNTIME_FILES, materialize
except ImportError:  # direct script sibling import
    from b2_boundary import (
        SCRATCH_MOUNT, WORKSPACE_MOUNT, BoundaryError, ViewSpec, confined_invocation,
    )
    from b2_check_launcher import BIN_DIR, LAUNCHER_NAME, TRUSTED_RUNTIME_FILES, materialize

# Where the trusted pieces appear *inside* the view. The launcher embeds these, so nothing
# it contains points at the host: an agent that reads `bin/check` learns `/workspace` and
# `/b2-runtime`, which are the two places it already knows about.
RUNTIME_MOUNT = "/b2-runtime"
BIN_MOUNT = "/b2-bin"
# Read-only host paths the Claude Code runtime needs beyond the boundary's own defaults.
# `/etc` carries TLS roots and resolver configuration and holds no evaluator material.
MODEL_RUNTIME_BINDS = ("/usr", "/bin", "/sbin", "/lib", "/lib64", "/etc")
VIEW_PATH = f"{BIN_MOUNT}:/usr/local/bin:/usr/bin:/bin"
# Host directories that must never appear in the view. Asserted, not assumed.
FORBIDDEN_IN_VIEW = ("home", "root", "tmp", "srv", "var", "media", "mnt")
# `/opt` may exist, but only as the parent of the node runtime mount. Anything else under it
# would be host content the view has no business carrying, so the listing is checked.
RUNTIME_PARENTS = ("opt",)


class ConfinementError(RuntimeError):
    pass


def _node_runtime(claude_binary: str) -> tuple[str, Path] | None:
    """Where the Claude Code binary lives, if it is outside the default runtime binds.

    Returned as an extra read-only mount at its own host path, so the launcher command and
    `PATH` keep working unchanged inside the view.
    """
    resolved = shutil.which(claude_binary)
    if resolved is None:
        raise ConfinementError(f"the Claude Code binary {claude_binary!r} is not on PATH")
    real = Path(resolved).resolve()
    for prefix in MODEL_RUNTIME_BINDS:
        if str(real).startswith(prefix.rstrip("/") + "/"):
            return None
    # e.g. /opt/claude-code/bin/claude -> mount /opt/claude-code
    root = real.parent.parent if real.parent.name == "bin" else real.parent
    return (str(root), root)


def runtime_parent_expectation(claude_binary: str = "claude") -> tuple[str, str] | None:
    """The single directory a runtime mount may add under a host parent like `/opt`."""
    node = _node_runtime(claude_binary)
    if node is None:
        return None
    mount = Path(node[0])
    return (mount.parent.name, mount.name)


def view_environment(base: Mapping[str, str]) -> dict[str, str]:
    """The environment the confined model process runs with.

    Built from the adapter's already-filtered child environment, with every path that points
    into the host rewritten to its in-view equivalent. Anything naming a host directory that
    the view does not carry is dropped rather than left dangling.
    """
    env = {k: v for k, v in base.items() if k not in {"PATH", "HOME", "TMPDIR", "TMP", "TEMP",
                                                      "PWD", "OLDPWD", "CLAUDE_CONFIG_DIR"}}
    env.update({
        "PATH": VIEW_PATH,
        "HOME": SCRATCH_MOUNT,
        "TMPDIR": SCRATCH_MOUNT,
        "CLAUDE_CONFIG_DIR": f"{SCRATCH_MOUNT}/claude-config",
    })
    return env


@contextmanager
def confined_model_invocation(argv: list[str], *, task_root: Path, workspace: Path,
                              env: Mapping[str, str], claude_binary: str = "claude",
                              timeout: int = 900):
    """Build the confined invocation for one model process. Yields it; runs nothing.

    The caller still executes it through its own process runner, so the confinement is part
    of the argv that gets recorded rather than a side channel around it.
    """
    if not workspace.is_dir():
        raise ConfinementError(f"the B2 workspace is not a directory: {workspace}")
    staging = task_root / "b2-runtime"
    launcher = materialize(task_root, Path(WORKSPACE_MOUNT), tools_dir=Path(RUNTIME_MOUNT),
                           staging=staging)
    if not launcher.is_file():
        raise ConfinementError("the check launcher was not materialised")

    extra_ro: list[tuple[str, Path]] = [
        (RUNTIME_MOUNT, staging),
        (BIN_MOUNT, task_root / BIN_DIR),
    ]
    node = _node_runtime(claude_binary)
    if node is not None:
        extra_ro.append(node)

    spec = ViewSpec(
        workspace=workspace,
        argv=tuple(argv),
        extra_ro=tuple(extra_ro),
        timeout=timeout,
        workdir=WORKSPACE_MOUNT,
        # The model process needs its API. This is the isolation the outer view does not
        # provide, and it is the only one.
        unshare_net=False,
        runtime_binds=MODEL_RUNTIME_BINDS,
        env=view_environment(env),
    )
    with confined_invocation(spec) as invocation:
        yield invocation


def probe_confinement(evaluator_sentinel: Path, sentinel_value: str,
                      claude_binary: str = "claude") -> dict[str, Any]:
    """Run the adversarial command set a model process could run. No model involved.

    The point is the filesystem contract, not the tool allowlist: these are exactly the
    read-only shell forms Claude Code may execute without a prompt, so they are executed for
    real and their output is inspected.
    """
    import tempfile

    try:  # local import: keeps the module import light
        from .b2_boundary import run_in_view
    except ImportError:
        from b2_boundary import run_in_view

    with tempfile.TemporaryDirectory(prefix="b2-confine-") as tmp:
        root = Path(tmp)
        task = root / "task"
        workspace = task / "workspace"
        workspace.mkdir(parents=True)
        (workspace / "note.txt").write_text("workspace file\n", encoding="utf-8")
        (task / "execution-view.yml").write_text("schema_version: 1\n", encoding="utf-8")
        staging = task / "b2-runtime"
        launcher = materialize(task, Path(WORKSPACE_MOUNT), tools_dir=Path(RUNTIME_MOUNT),
                               staging=staging)

        # The sentinel arrives as an argument, not as a literal in the script: a probe whose
        # own file contains the needle finds it and reports a leak that is its own doing.
        script = "\n".join([
            "set +e",
            'SENTINEL="$1"',
            'echo "--- cwd"; pwd',
            'echo "--- root listing"; ls -1 / 2>&1',
            'echo "--- cat evaluator sentinel"; cat %s 2>&1 | head -2' % evaluator_sentinel,
            'echo "--- opt listing"; ls -1 /opt 2>&1 | head -5',
            'echo "--- cat repository file"; cat %s 2>&1 | head -2' % (Path.cwd() / "tools/b2_grader.py"),
            'echo "--- find case-matrix"; find / -name "case-matrix.yml" 2>/dev/null | head -5',
            'echo "--- find expectations"; find / -name "expectations.yml" 2>/dev/null | head -5',
            # Bounded to everything the view carries that is not the read-only runtime.
            # Grepping /usr adds minutes and no evidence: the runtime is not where evaluator
            # material could be.
            'echo "--- grep outside"; grep -rs "$SENTINEL" / --exclude-dir=usr --exclude-dir=lib '
            '--exclude-dir=lib64 --exclude-dir=bin --exclude-dir=sbin --exclude-dir=proc '
            '--exclude-dir=dev --exclude-dir=opt 2>/dev/null | head -3',
            'echo "--- ls parents"; ls -1 /workspace/.. 2>&1 | head -10; ls -1 /home /root /tmp 2>&1 | head -3',
            'echo "--- cat launcher"; cat %s/%s 2>&1 | head -40' % (BIN_MOUNT, LAUNCHER_NAME),
            'echo "--- cat staged runtime listing"; ls -1 %s 2>&1' % RUNTIME_MOUNT,
            'echo "--- write outside workspace"',
            'for t in /b2-bin/%s /b2-runtime/b2_boundary.py /execution-view.yml /planted /etc/planted %s/planted; do'
            % (LAUNCHER_NAME, RUNTIME_MOUNT),
            '  if echo x > "$t" 2>/dev/null; then echo "WROTE $t"; fi',
            "done",
            'echo "--- write inside workspace"; echo x > /workspace/allowed.txt && echo "WROTE /workspace/allowed.txt"',
            'echo "--- done"',
        ])
        (workspace / "probe.sh").write_text(script, encoding="utf-8")

        node = _node_runtime(claude_binary)
        extra_ro = [(RUNTIME_MOUNT, staging), (BIN_MOUNT, task / BIN_DIR)]
        if node is not None:
            extra_ro.append(node)
        result = run_in_view(ViewSpec(
            workspace=workspace, argv=("/bin/sh", "/workspace/probe.sh", sentinel_value),
            extra_ro=tuple(extra_ro), timeout=300, workdir=WORKSPACE_MOUNT,
            unshare_net=False, runtime_binds=MODEL_RUNTIME_BINDS,
            env=view_environment({}),
        ))
        combined = result.stdout + result.stderr
        def section(name: str) -> list[str]:
            out, capture = [], False
            for line in result.stdout.splitlines():
                if line.startswith(f"--- {name}"):
                    capture = True
                    continue
                if line.startswith("--- "):
                    capture = False
                elif capture and line.strip():
                    out.append(line.strip())
            return out

        listing = set(section("root listing"))
        opt_listing = section("opt listing")
        wrote = [l.split(" ", 1)[1] for l in result.stdout.splitlines() if l.startswith("WROTE ")]
        expected_runtime = runtime_parent_expectation(claude_binary)
        launcher_text = launcher.read_text(encoding="utf-8")
        host_root = str(Path.cwd())
        return {
            "sentinel_leaked": sentinel_value in combined,
            "repository_readable": "def grade(" in combined,
            "discovery_hits": [l for l in result.stdout.splitlines()
                               if l.startswith("/") and l.endswith((".yml", ".yaml"))],
            "root_listing": sorted(listing),
            "host_dirs_in_view": sorted(listing & set(FORBIDDEN_IN_VIEW)),
            # A runtime parent is acceptable; host content under it is not.
            "runtime_parent_listing": opt_listing,
            "unexpected_under_runtime_parent": [
                x for x in opt_listing if expected_runtime is None or x != expected_runtime[1]],
            "wrote": wrote,
            "writes_outside_workspace": [w for w in wrote if not w.startswith(WORKSPACE_MOUNT)],
            "launcher_contains_host_path": host_root in launcher_text,
            "launcher_text": launcher_text,
            "staged_runtime": sorted(p.name for p in staging.rglob("*")),
            "returncode": result.returncode,
            "stdout": result.stdout,
        }


def _cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--probe", action="store_true")
    args = parser.parse_args(argv)
    if not args.probe:
        parser.error("--probe is the only supported invocation")
    import tempfile

    with tempfile.TemporaryDirectory(prefix="b2-sentinel-") as tmp:
        sentinel = Path(tmp) / "case-matrix.yml"
        sentinel.write_text("B2-CONFINEMENT-SENTINEL-7c4a\n", encoding="utf-8")
        try:
            report = probe_confinement(sentinel, "B2-CONFINEMENT-SENTINEL-7c4a")
        except (BoundaryError, ConfinementError) as exc:
            print(f"CONFINEMENT_ERROR: {exc}", file=sys.stderr)
            return 2
    print(json.dumps({k: v for k, v in report.items() if k not in {"stdout", "launcher_text"}}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
