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
import hashlib
import json
import shutil
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Mapping

try:
    from .b2_boundary import (
        PROVIDER, SCRATCH_MOUNT, WORKSPACE_MOUNT, BoundaryError, ViewSpec, confined_invocation,
    )
    from .b2_check_launcher import BIN_DIR, LAUNCHER_NAME, TRUSTED_RUNTIME_FILES, materialize
except ImportError:  # direct script sibling import
    from b2_boundary import (
        PROVIDER, SCRATCH_MOUNT, WORKSPACE_MOUNT, BoundaryError, ViewSpec, confined_invocation,
    )
    from b2_check_launcher import BIN_DIR, LAUNCHER_NAME, TRUSTED_RUNTIME_FILES, materialize

# Where the trusted pieces appear *inside* the view. The launcher embeds these, so nothing
# it contains points at the host: an agent that reads `bin/check` learns `/workspace` and
# `/b2-runtime`, which are the two places it already knows about.
RUNTIME_MOUNT = "/b2-runtime"
BIN_MOUNT = "/b2-bin"
# Every file path in the model process's own argv has to exist *inside* the view. The empty
# MCP configuration used to be written into the adapter's host temporary directory and passed
# by host path -- a path the confined process cannot open, because the view deliberately
# carries no host temp tree. It now has a read-only view of its own.
CONFIG_MOUNT = "/b2-config"
EMPTY_MCP_FILENAME = "empty-mcp.json"
VIEW_MCP_CONFIG = f"{CONFIG_MOUNT}/{EMPTY_MCP_FILENAME}"
EMPTY_MCP_JSON = '{"mcpServers": {}}\n'
CONFIG_DIR = "b2-config"
# Transport variables whose value is a *file* path. Left as host paths they name something the
# confined process cannot open -- the runtime then logs `load failed: No such file or
# directory` and proceeds with a trust store the launch did not intend. A readable host file
# is therefore staged read-only into the configuration view and the variable is rewritten to
# its in-view path; a missing one is dropped rather than passed on inert.
TRANSPORT_FILE_ENV = ("NODE_EXTRA_CA_CERTS", "SSL_CERT_FILE", "REQUESTS_CA_BUNDLE",
                      "AWS_CA_BUNDLE")
# Directory-valued ones. A directory outside the view is not staged: copying a trust-store
# directory silently is a decision about transport trust, not a mechanical fix, so the
# preflight refuses and a human decides.
TRANSPORT_DIR_ENV = ("SSL_CERT_DIR",)
TRANSPORT_STAGE_DIR = "transport"
# Anything already under one of these is reachable in the view as it stands.
VIEW_VISIBLE_PREFIXES = (WORKSPACE_MOUNT, SCRATCH_MOUNT, RUNTIME_MOUNT, BIN_MOUNT, CONFIG_MOUNT)
# Read-only host paths the Claude Code runtime needs beyond the boundary's own defaults.
# `/etc` carries TLS roots and resolver configuration and holds no evaluator material.
MODEL_RUNTIME_BINDS = ("/usr", "/bin", "/sbin", "/lib", "/lib64", "/etc")
BASE_VIEW_PATH = f"{BIN_MOUNT}:/usr/local/bin:/usr/bin:/bin"
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


def view_path(claude_binary: str = "claude") -> str:
    """`PATH` inside the view.

    The Claude Code runtime is mounted at its own host path when it lives outside the default
    binds, and the launch passes `claude` rather than an absolute path -- so the directory the
    binary actually sits in has to be on `PATH` too. Leaving it off made the confined process
    fail to start at all, which the launch preflight found and this fixes.
    """
    node = _node_runtime(claude_binary)
    if node is None:
        return BASE_VIEW_PATH
    resolved = shutil.which(claude_binary)
    directory = str(Path(resolved).resolve().parent) if resolved else node[0]
    return f"{BIN_MOUNT}:{directory}:/usr/local/bin:/usr/bin:/bin"


def _under(value: str, prefixes) -> bool:
    return any(value == p or value.startswith(p.rstrip("/") + "/") for p in prefixes)


def transport_path_plan(env: Mapping[str, str]) -> dict[str, dict[str, Any]]:
    """What becomes of each path-valued transport variable inside the view.

    Four outcomes, each with a reason: `keep` when the path is already reachable, `stage` when
    a readable host file can be mounted read-only and the variable rewritten, `drop` when the
    path does not exist on the host and was already inert, and `reject` when the value is a
    directory outside the view, which is a trust decision rather than a mechanical fix.

    No host path is returned. Callers that need one take it from `env` themselves.
    """
    plan: dict[str, dict[str, Any]] = {}
    reachable = (*VIEW_VISIBLE_PREFIXES, *MODEL_RUNTIME_BINDS)
    for name in (*TRANSPORT_FILE_ENV, *TRANSPORT_DIR_ENV):
        value = (env.get(name) or "").strip()
        if not value:
            continue
        directory_valued = name in TRANSPORT_DIR_ENV
        if _under(value, reachable):
            action, reason = "keep", "already reachable inside the view"
        elif directory_valued:
            action, reason = "reject", ("a trust-store directory outside the view is not "
                                        "staged automatically; it needs a decision")
        elif Path(value).is_file():
            action, reason = "stage", "readable host file, mounted read-only into the config view"
        else:
            action, reason = "drop", ("names nothing on the host, so it was already inert and "
                                      "is removed rather than passed on")
        entry: dict[str, Any] = {
            "configured": True,
            "kind": "directory" if directory_valued else "file",
            "accessible_in_view": action == "keep",
            "action": action,
            "reason": reason,
        }
        if action == "stage":
            entry["view_path"] = f"{CONFIG_MOUNT}/{TRANSPORT_STAGE_DIR}/{name}"
        plan[name] = entry
    return plan


def stage_config(task_root: Path, env: Mapping[str, str] | None = None) -> Path:
    """Materialise the read-only configuration view: the empty MCP file, plus staged CA files.

    Nothing else may land here. The allowlist is checked after writing rather than assumed,
    so a future caller that copies something extra fails instead of widening the view.
    """
    directory = task_root / CONFIG_DIR
    directory.mkdir(parents=True, exist_ok=True)
    (directory / EMPTY_MCP_FILENAME).write_text(EMPTY_MCP_JSON, encoding="utf-8")
    expected = {EMPTY_MCP_FILENAME}
    plan = transport_path_plan(env or {})
    staged = {name: entry for name, entry in plan.items() if entry["action"] == "stage"}
    if staged:
        stage = directory / TRANSPORT_STAGE_DIR
        stage.mkdir(exist_ok=True)
        expected.add(TRANSPORT_STAGE_DIR)
        for name in staged:
            shutil.copyfile((env or {})[name].strip(), stage / name)
        extra = sorted(p.name for p in stage.iterdir() if p.name not in staged)
        if extra:
            raise ConfinementError(f"the staged transport directory carries {extra}")
    stray = sorted(p.name for p in directory.iterdir() if p.name not in expected)
    if stray:
        raise ConfinementError(f"the configuration view carries unexpected files: {stray}")
    return directory


def runtime_parent_expectation(claude_binary: str = "claude") -> tuple[str, str] | None:
    """The single directory a runtime mount may add under a host parent like `/opt`."""
    node = _node_runtime(claude_binary)
    if node is None:
        return None
    mount = Path(node[0])
    return (mount.parent.name, mount.name)


def view_environment(base: Mapping[str, str], claude_binary: str = "claude") -> dict[str, str]:
    """The environment the confined model process runs with.

    Built from the adapter's already-filtered child environment, with every path that points
    into the host rewritten to its in-view equivalent. Anything naming a host directory that
    the view does not carry is dropped rather than left dangling.
    """
    env = {k: v for k, v in base.items() if k not in {"PATH", "HOME", "TMPDIR", "TMP", "TEMP",
                                                      "PWD", "OLDPWD", "CLAUDE_CONFIG_DIR"}}
    env.update({
        "PATH": view_path(claude_binary),
        "HOME": SCRATCH_MOUNT,
        "TMPDIR": SCRATCH_MOUNT,
        "CLAUDE_CONFIG_DIR": f"{SCRATCH_MOUNT}/claude-config",
    })
    # Path-valued transport variables follow their plan. A host path that survives here names
    # a file the confined process cannot open, which is how a CA bundle came to be passed on
    # as `/root/.ccr/ca-bundle.crt` into a view with no `/root`.
    for name, entry in transport_path_plan(base).items():
        if entry["action"] == "stage":
            env[name] = entry["view_path"]
        elif entry["action"] in ("drop", "reject"):
            env.pop(name, None)
    return env


@contextmanager
def confined_model_invocation(argv: list[str], *, task_root: Path, workspace: Path,
                              env: Mapping[str, str], claude_binary: str = "claude",
                              timeout: int = 900):
    """Build the confined invocation for one model process. Yields it; runs nothing.

    The caller still executes it through its own process runner: the confinement is in the
    argv that is actually launched, not a side channel around it. That alone does not put it
    into the run's artifacts -- `confinement_facts` and `invocation_evidence` do, and until
    the adapter writes both the artifacts described the inner Claude call only.
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
        (CONFIG_MOUNT, stage_config(task_root, env)),
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
        env=view_environment(env, claude_binary),
    )
    with confined_invocation(spec) as invocation:
        yield invocation


def mount_contract(claude_binary: str = "claude") -> dict[str, Any]:
    """What the outer view promises, as data rather than as prose.

    Written into the run evidence so that a later reader can tell which view a run happened
    in, and so that a run without the view cannot produce the same fingerprint.
    """
    return {
        "workspace_mount": WORKSPACE_MOUNT,
        "scratch_mount": SCRATCH_MOUNT,
        "launcher_mount": BIN_MOUNT,
        "trusted_runtime_mount": RUNTIME_MOUNT,
        "config_mount": CONFIG_MOUNT,
        "runtime_binds": list(MODEL_RUNTIME_BINDS),
        "workdir": WORKSPACE_MOUNT,
        "network_namespace_unshared": False,
        "view_path": view_path(claude_binary),
    }


def confinement_facts(invocation: Any, *, payload_started: bool) -> dict[str, Any]:
    """The measured confinement, in the shape the run evidence carries.

    `payload_started` is read from the boundary's own setup marker, so `established` means
    the view was assembled and `exec` was reached -- not that a function was called.
    """
    contract = mount_contract()
    return {
        "established": bool(payload_started),
        "provider": getattr(invocation, "provider", PROVIDER),
        "payload_started": bool(payload_started),
        "workspace_mount": contract["workspace_mount"],
        "launcher_mount": contract["launcher_mount"],
        "trusted_runtime_mount": contract["trusted_runtime_mount"],
        "config_mount": contract["config_mount"],
        "network_namespace_unshared": contract["network_namespace_unshared"],
        "note": ("filesystem confinement only; the model process keeps network access "
                 "because it must reach its API"),
    }


def invocation_evidence(invocation: Any, inner_argv_normalized: list[str]) -> dict[str, Any]:
    """A normalized preimage of the *outer* invocation that persists no credentials.

    The outer argv carries the boundary assembly script, and its launcher environment carries
    host temporary paths. Neither belongs in a run artifact verbatim, and neither may simply
    be dropped either -- then the artifact would describe the inner Claude call alone, which
    is the defect this closes. So the structure, the provider, the mount contract and the
    inner argv are bound, the script by hash, and the environment by variable name only.
    """
    argv = list(getattr(invocation, "argv", []) or [])
    # ["unshare", flags..., "/bin/sh", "-c", <script>, "b2-boundary", <inner argv...>]
    script, shape = "", []
    for i, item in enumerate(argv):
        if i and argv[i - 1] == "-c" and argv[i - 2 : i - 1] == ["/bin/sh"]:
            script = item
            shape.append("<boundary-assembly-script>")
        elif item == "b2-boundary":
            shape.append("b2-boundary")
            shape.append("<inner-claude-argv>")
            break
        else:
            shape.append(item)
    preimage = {
        "layer": "confined-outer-process",
        "provider": getattr(invocation, "provider", PROVIDER),
        "outer_argv_shape": shape,
        "boundary_assembly_script_sha256": hashlib.sha256(script.encode("utf-8")).hexdigest(),
        "mount_contract": mount_contract(),
        # Names only. Values would carry host temporary paths, and the child environment can
        # carry credentials; neither is persisted.
        "launcher_environment_names": sorted(getattr(invocation, "env", {}) or {}),
        "inner_argv_normalized": list(inner_argv_normalized),
    }
    digest = hashlib.sha256(
        json.dumps(preimage, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
    return {**preimage, "preimage_sha256": f"sha256:{digest}"}


@contextmanager
def model_view(claude_binary: str = "claude", env: Mapping[str, str] | None = None,
               timeout: int = 300):
    """A throwaway task root shaped exactly like a writable B2 run, for model-free checks.

    Yields a callable that runs one argv inside the real outer view: the same mount contract,
    the same `view_environment` logic, the same launcher. Nothing about the view is rebuilt
    here, so a preflight cannot pass against a view the pilot would not use.
    """
    import subprocess
    import tempfile

    with tempfile.TemporaryDirectory(prefix="b2-model-view-") as tmp:
        task = Path(tmp) / "task"
        workspace = task / "workspace"
        workspace.mkdir(parents=True)

        def run(argv: list[str], *, view_timeout: int | None = None) -> dict[str, Any]:
            with confined_model_invocation(argv, task_root=task, workspace=workspace,
                                           env=env or {}, claude_binary=claude_binary,
                                           timeout=view_timeout or timeout) as confined:
                try:
                    done = subprocess.run(
                        confined.argv, env=confined.env, cwd="/", text=True,
                        capture_output=True, timeout=view_timeout or timeout, check=False,
                    )
                except subprocess.TimeoutExpired:
                    return {"returncode": None, "stdout": "", "stderr": "timeout",
                            "payload_started": confined.payload_started(), "timed_out": True}
                return {"returncode": done.returncode, "stdout": done.stdout,
                        "stderr": done.stderr, "payload_started": confined.payload_started(),
                        "timed_out": False}

        yield run


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
            'echo "--- config view listing"; ls -1 %s 2>&1' % CONFIG_MOUNT,
            'echo "--- write outside workspace"',
            'for t in /b2-bin/%s /b2-runtime/b2_boundary.py %s /b2-config/planted '
            '/execution-view.yml /planted /etc/planted %s/planted; do'
            % (LAUNCHER_NAME, VIEW_MCP_CONFIG, RUNTIME_MOUNT),
            '  if echo x > "$t" 2>/dev/null; then echo "WROTE $t"; fi',
            "done",
            'echo "--- write inside workspace"; echo x > /workspace/allowed.txt && echo "WROTE /workspace/allowed.txt"',
            'echo "--- done"',
        ])
        (workspace / "probe.sh").write_text(script, encoding="utf-8")

        node = _node_runtime(claude_binary)
        extra_ro = [(RUNTIME_MOUNT, staging), (BIN_MOUNT, task / BIN_DIR),
                    (CONFIG_MOUNT, stage_config(task))]
        if node is not None:
            extra_ro.append(node)
        result = run_in_view(ViewSpec(
            workspace=workspace, argv=("/bin/sh", "/workspace/probe.sh", sentinel_value),
            extra_ro=tuple(extra_ro), timeout=300, workdir=WORKSPACE_MOUNT,
            unshare_net=False, runtime_binds=MODEL_RUNTIME_BINDS,
            env=view_environment({}, claude_binary),
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
            "config_view_listing": section("config view listing"),
            "returncode": result.returncode,
            "stdout": result.stdout,
        }


EVIDENCE_CONTRACT = "verification-governance-model-confinement/v1"
SENTINEL_VALUE = "B2-CONFINEMENT-SENTINEL-7c4a"


def evidence_document(claude_binary: str = "claude") -> dict[str, Any]:
    """Run the probe and shape its result as the committed evidence artifact.

    Written by code rather than by hand, so the file in `evidence/` can be regenerated and
    compared instead of being trusted because it is checked in.
    """
    import tempfile

    try:
        from .b2_pilot_readiness import evidence_binding
    except ImportError:  # direct script sibling import
        from b2_pilot_readiness import evidence_binding

    with tempfile.TemporaryDirectory(prefix="b2-sentinel-") as tmp:
        sentinel = Path(tmp) / "case-matrix.yml"
        sentinel.write_text(SENTINEL_VALUE + "\n", encoding="utf-8")
        report = probe_confinement(sentinel, SENTINEL_VALUE, claude_binary)
    observations = {k: v for k, v in report.items()
                    if k not in {"stdout", "launcher_text", "returncode"}}
    return {
        "contract": EVIDENCE_CONTRACT,
        "model_involved": False,
        "bound_to": evidence_binding(),
        "note": ("The read-only shell commands Claude Code may run without a permission "
                 "prompt, executed for real inside the confinement view against a planted "
                 "sentinel. The question is the filesystem the process can see, not what the "
                 "allowlist says."),
        "observations": observations,
        "launcher_as_the_agent_would_read_it": report["launcher_text"],
        "transcript": report["stdout"],
    }


def _cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--probe", action="store_true")
    parser.add_argument("--write", help="Write the confinement evidence to this path")
    parser.add_argument("--claude-binary", default="claude")
    args = parser.parse_args(argv)
    if not args.probe:
        parser.error("--probe is the only supported invocation")
    try:
        document = evidence_document(args.claude_binary)
    except (BoundaryError, ConfinementError) as exc:
        print(f"CONFINEMENT_ERROR: {exc}", file=sys.stderr)
        return 2
    if args.write:
        import yaml
        path = Path(args.write)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(document, allow_unicode=True, sort_keys=False),
                        encoding="utf-8")
    print(json.dumps(document["observations"], indent=2))
    observations = document["observations"]
    clean = (not observations["sentinel_leaked"] and not observations["repository_readable"]
             and not observations["host_dirs_in_view"]
             and not observations["writes_outside_workspace"])
    return 0 if clean else 1


if __name__ == "__main__":
    raise SystemExit(_cli())
