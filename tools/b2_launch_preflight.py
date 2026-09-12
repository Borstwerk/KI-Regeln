#!/usr/bin/env python3
"""Model-free launch preflight for a Phase 4.2C / B2 writable run.

Three questions, all answerable without a model request, all answered by executing something
rather than by reading source:

1. Does every file path in the model process's own argv exist *inside* the view it will run
   in, and does the argv carry no host path at all? The confinement made this a real
   question: a path that resolves on the host is not a path the confined process can open.
2. Is the Claude Code runtime executable inside exactly that view, and does the installed
   option parser accept exactly the flags a writable run passes?
3. Does the authentication path the pilot is meant to use work inside exactly that view?
   The view carries no host home and a fresh `CLAUDE_CONFIG_DIR`, so this cannot be inferred
   from the fact that the CLI is authenticated on the host.

The third question is allowed to answer "no". A launch context that is not authenticated is
a pilot blocker, not something to repair by mounting the host home back into the view -- that
would re-open the filesystem boundary this phase just closed.
"""
from __future__ import annotations

import argparse
import json
import shlex
import sys
from pathlib import Path
from typing import Any, Mapping

try:
    from .b2_model_confinement import (
        BIN_MOUNT, CONFIG_MOUNT, MODEL_RUNTIME_BINDS, RUNTIME_MOUNT, VIEW_MCP_CONFIG,
        ConfinementError, _node_runtime, model_view, mount_contract, view_environment,
    )
    from .b2_boundary import SCRATCH_MOUNT, WORKSPACE_MOUNT, BoundaryError
    from .behavioral_harness_claude import AdapterError, _argv, probe_claude_code
except ImportError:  # direct script sibling import
    from b2_model_confinement import (
        BIN_MOUNT, CONFIG_MOUNT, MODEL_RUNTIME_BINDS, RUNTIME_MOUNT, VIEW_MCP_CONFIG,
        ConfinementError, _node_runtime, model_view, mount_contract, view_environment,
    )
    from b2_boundary import SCRATCH_MOUNT, WORKSPACE_MOUNT, BoundaryError
    from behavioral_harness_claude import AdapterError, _argv, probe_claude_code

PREFLIGHT_CONTRACT = "verification-governance-b2-launch-preflight/v1"
ROOT = Path(__file__).resolve().parents[1]
# The model id does not influence any of the three questions -- no request is made -- but a
# placeholder is still recorded, so nobody reads the report as covering a particular model.
PLACEHOLDER_MODEL = "placeholder-full-model-id-no-request-is-made"
# Flags whose value Claude Code interprets as a filesystem path.
PATH_VALUE_FLAGS = (
    "--mcp-config", "--settings", "--add-dir", "--plugin-dir", "--agents",
    "--append-system-prompt-file", "--system-prompt-file", "--ide",
)


def _view_prefixes(claude_binary: str = "claude") -> tuple[str, ...]:
    """Absolute path prefixes that exist inside the outer view."""
    prefixes = [WORKSPACE_MOUNT, SCRATCH_MOUNT, RUNTIME_MOUNT, BIN_MOUNT, CONFIG_MOUNT,
                *MODEL_RUNTIME_BINDS]
    node = _node_runtime(claude_binary)
    if node is not None:
        prefixes.append(node[0])
    return tuple(sorted(set(prefixes)))


def _is_path_candidate(index: int, argv: list[str]) -> bool:
    """Does the runtime interpret this argv element as a filesystem path?

    Absolute-looking values are candidates on their own, and so is any value following a flag
    documented to take a path -- otherwise a relative path behind `--settings` would slip
    through a check that only looked for a leading slash.
    """
    value = argv[index]
    if index and argv[index - 1] in PATH_VALUE_FLAGS:
        return not value.startswith("{")
    return value.startswith("/") or value.startswith("./") or value.startswith("../")


def argv_audit(argv: list[str], *, claude_binary: str = "claude") -> dict[str, Any]:
    """Classify the argv. Nothing is executed here; the view check follows separately."""
    prefixes = _view_prefixes(claude_binary)
    candidates, outside = [], []
    for i, value in enumerate(argv):
        if not _is_path_candidate(i, argv):
            continue
        candidates.append(value)
        if not any(value == p or value.startswith(p.rstrip("/") + "/") for p in prefixes):
            outside.append(value)
    # Separately from the path classification: no element may *contain* a host location,
    # however it is meant to be interpreted. A prompt that quoted the repository path would
    # leak it just as effectively as an argument that named it.
    markers = (str(ROOT), "/tmp/ki-regeln-", "/home/", "/root/", "/oldroot")
    embedded = sorted({m for value in argv for m in markers if m in value})
    return {
        "view_prefixes": list(prefixes),
        "path_candidates": candidates,
        "candidates_outside_the_view": outside,
        "embedded_host_markers": embedded,
        "strict_mcp_config_present": "--strict-mcp-config" in argv,
        "mcp_config_value": (argv[argv.index("--mcp-config") + 1]
                             if "--mcp-config" in argv else None),
        "ok": not outside and not embedded and "--strict-mcp-config" in argv,
    }


def writable_launch_argv(claude_binary: str = "claude", model: str = PLACEHOLDER_MODEL,
                         process_runner=None) -> tuple[list[str], dict[str, Any]]:
    """The real writable inner argv, built by the adapter's own code path.

    Not a reconstruction: `_argv` is the function the launch path calls, so an argv change
    that reintroduced a host path would break this check rather than pass beside it.
    """
    probe = probe_claude_code(claude_binary, *( (process_runner,) if process_runner else () ))
    argv, controls = _argv(claude_binary, model, "<preflight task prompt>", "preflight-session",
                           probe["capabilities"], Path("/unused-host-path-must-not-appear"),
                           writable=True)
    return argv, controls


def _run_in_view(run, argv: list[str], *, timeout: int | None = None) -> dict[str, Any]:
    out = run(argv, view_timeout=timeout)
    return {"argv": argv, "returncode": out["returncode"], "payload_started": out["payload_started"],
            "timed_out": out["timed_out"],
            "stdout_tail": (out["stdout"] or "")[-2000:], "stderr_tail": (out["stderr"] or "")[-2000:]}


def preflight(claude_binary: str = "claude", base_env: Mapping[str, str] | None = None,
              model: str = PLACEHOLDER_MODEL) -> dict[str, Any]:
    """Answer all three questions. No model request is made at any point."""
    import os

    env = dict(base_env if base_env is not None else os.environ)
    argv, controls = writable_launch_argv(claude_binary, model)
    audit = argv_audit(argv, claude_binary=claude_binary)

    checks: dict[str, Any] = {}
    with model_view(claude_binary=claude_binary, env=env) as run:
        # 1. Every path candidate, tested for real inside the view.
        script = "\n".join([
            "set +e", "rc=0",
            *[f'if [ -e {shlex.quote(c)} ]; then echo "PRESENT {c}"; '
              f'else echo "MISSING {c}"; rc=1; fi' for c in audit["path_candidates"]],
            'exit "$rc"',
        ])
        present = _run_in_view(run, ["/bin/sh", "-c", script], timeout=120)
        missing = [l.split(" ", 1)[1] for l in present["stdout_tail"].splitlines()
                   if l.startswith("MISSING ")]
        checks["argv_paths_exist_in_view"] = {
            "ok": present["returncode"] == 0 and not missing,
            "missing": missing, "detail": present,
        }

        # 2a. The runtime is executable in the view at all.
        version = _run_in_view(run, [claude_binary, "--version"], timeout=180)
        checks["runtime_executable_in_view"] = {
            "ok": version["returncode"] == 0,
            "version": (version["stdout_tail"] or "").strip().splitlines()[:1],
            "detail": version,
        }

        # 2b. The installed parser accepts exactly the writable flag set. `--help` short-
        # circuits before any request, so this is a parser observation and nothing more.
        accepted = _run_in_view(run, argv[:-1] + ["--help"], timeout=180)
        # A parser that accepted everything would make the positive result meaningless, so a
        # value the parser must reject is offered too.
        rejected = _run_in_view(run, [claude_binary, "--permission-mode", "notAMode", "--help"],
                                timeout=180)
        checks["writable_flags_parse_in_view"] = {
            "ok": accepted["returncode"] == 0 and rejected["returncode"] not in (0, None),
            "accepted_returncode": accepted["returncode"],
            "rejected_returncode": rejected["returncode"],
            "detail": {"accepted": accepted, "rejected": rejected},
        }

        # 3. The authentication path, in exactly this view and this environment.
        auth = _run_in_view(run, [claude_binary, "auth", "status"], timeout=180)
        parsed: Any = None
        try:
            parsed = json.loads(auth["stdout_tail"])
        except (ValueError, TypeError):
            parsed = None
        logged_in = bool(isinstance(parsed, dict) and parsed.get("loggedIn") is True)
        checks["authenticated_in_view"] = {
            "ok": auth["returncode"] == 0 and logged_in,
            "logged_in": logged_in,
            # Method and provider only. No token, no value, nothing that could be replayed.
            "auth_method": (parsed or {}).get("authMethod") if isinstance(parsed, dict) else None,
            "api_provider": (parsed or {}).get("apiProvider") if isinstance(parsed, dict) else None,
            "config_directory": (parsed or {}).get("configDirectory") if isinstance(parsed, dict) else None,
            "detail": auth,
        }

    ok = audit["ok"] and all(c["ok"] for c in checks.values())
    return {
        "contract": PREFLIGHT_CONTRACT,
        "phase": "4.2C / B2",
        "model_placeholder": model,
        "mount_contract": mount_contract(claude_binary),
        "view_environment_names": sorted(view_environment(env, claude_binary)),
        "normalized_inner_argv": list(controls["normalized_argv"]),
        "argv_audit": audit,
        "checks": checks,
        "ok": ok,
        "note": ("Model-free. No request was made; `--help` and `auth status` never reach a "
                 "model. A false `authenticated_in_view` is a pilot blocker, not a reason to "
                 "widen the view."),
    }


def launchable() -> tuple[bool, str]:
    """The readiness criterion: one answer, with the failing part named."""
    try:
        report = preflight()
    except (AdapterError, BoundaryError, ConfinementError, OSError) as exc:
        return False, f"the launch preflight could not run: {type(exc).__name__}: {exc}"
    failures = []
    audit = report["argv_audit"]
    if audit["candidates_outside_the_view"]:
        failures.append(f"argv paths outside the view: {audit['candidates_outside_the_view']}")
    if audit["embedded_host_markers"]:
        failures.append(f"host locations embedded in argv: {audit['embedded_host_markers']}")
    if not audit["strict_mcp_config_present"]:
        failures.append("--strict-mcp-config is not requested")
    for name, check in report["checks"].items():
        if not check["ok"]:
            failures.append(f"{name} failed")
    if failures:
        return False, "; ".join(failures)
    return True, ("the writable argv is view-local, the runtime starts and parses the writable "
                  "flags inside the view, and the view's auth path reports logged in")


EVIDENCE_CONTRACT = "verification-governance-b2-launch-preflight-evidence/v1"


def evidence_document(claude_binary: str = "claude") -> dict[str, Any]:
    """The preflight result shaped as the committed evidence artifact."""
    try:
        from .b2_pilot_readiness import evidence_binding
    except ImportError:  # direct script sibling import
        from b2_pilot_readiness import evidence_binding
    report = preflight(claude_binary)
    return {
        "contract": EVIDENCE_CONTRACT,
        "model_involved": False,
        "bound_to": evidence_binding(),
        "note": ("Executed inside the real outer view, with the real writable argv built by "
                 "the adapter's own `_argv`. `--version`, `--help` and `auth status` make no "
                 "model request."),
        **{k: v for k, v in report.items() if k != "contract"},
    }


def _cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--claude-binary", default="claude")
    parser.add_argument("--write", help="Write the preflight evidence to this path")
    args = parser.parse_args(argv)
    try:
        document = evidence_document(args.claude_binary)
    except (AdapterError, BoundaryError, ConfinementError) as exc:
        print(f"PREFLIGHT_ERROR: {exc}", file=sys.stderr)
        return 2
    if args.write:
        import yaml
        path = Path(args.write)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(document, allow_unicode=True, sort_keys=False),
                        encoding="utf-8")
    print(json.dumps(document, indent=2, default=str))
    return 0 if document["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(_cli())
