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
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Mapping

try:
    from .b2_model_confinement import (
        BIN_MOUNT, CONFIG_MOUNT, MODEL_RUNTIME_BINDS, RUNTIME_MOUNT, VIEW_MCP_CONFIG,
        ConfinementError, _node_runtime, model_view, mount_contract, transport_path_plan,
        view_environment,
    )
    from .b2_boundary import SCRATCH_MOUNT, WORKSPACE_MOUNT, BoundaryError
    from .behavioral_harness_claude import (
        AUTH_SUBSCRIPTION_OAUTH, SUBPROCESS_SCRUB_ENV, SUBSCRIPTION_OAUTH_ENV, AdapterError,
        WritableLaunchContext, _argv, credential_channels, effective_auth_mode,
        prepare_writable_launch,
    )
except ImportError:  # direct script sibling import
    from b2_model_confinement import (
        BIN_MOUNT, CONFIG_MOUNT, MODEL_RUNTIME_BINDS, RUNTIME_MOUNT, VIEW_MCP_CONFIG,
        ConfinementError, _node_runtime, model_view, mount_contract, transport_path_plan,
        view_environment,
    )
    from b2_boundary import SCRATCH_MOUNT, WORKSPACE_MOUNT, BoundaryError
    from behavioral_harness_claude import (
        AUTH_SUBSCRIPTION_OAUTH, SUBPROCESS_SCRUB_ENV, SUBSCRIPTION_OAUTH_ENV, AdapterError,
        WritableLaunchContext, _argv, credential_channels, effective_auth_mode,
        prepare_writable_launch,
    )

PREFLIGHT_CONTRACT = "verification-governance-b2-launch-preflight/v1"
DENY_PROC_RULE = "Read(//proc/**)"
# Tri-state, matching the harness convention elsewhere: an observation nobody has made is not
# a negative result. It blocks exactly like `false`, and says something different.
UNKNOWN_OBSERVATION = "unknown"
ROOT = Path(__file__).resolve().parents[1]
# The model id does not influence any of the three questions -- no request is made -- but a
# placeholder is still recorded, so nobody reads the report as covering a particular model.
PLACEHOLDER_MODEL = "placeholder-full-model-id-no-request-is-made"
# Flags whose value Claude Code interprets as a filesystem path.
PATH_VALUE_FLAGS = (
    "--mcp-config", "--settings", "--add-dir", "--plugin-dir", "--agents",
    "--append-system-prompt-file", "--system-prompt-file", "--ide",
)


# Literal permission-rule forms the installed runtime carries in its own material. Finding
# them is evidence about the *syntax* -- that `//` addresses the filesystem while a single
# leading slash is workspace-rooted -- and nothing more. Whether a deny rule actually stops a
# Read is a vendor contract: no model-free command on this runtime evaluates permission rules,
# and demonstrating the block needs a running model process, which this phase does not start.
RULE_SYNTAX_LITERALS = ("(//proc/**)", "Edit(//etc/*)", "Read(~/**)")


def rule_syntax_evidence(claude_binary: str = "claude") -> dict[str, Any]:
    """Which absolute-path rule forms appear in the installed runtime. Measured, not recalled."""
    import shutil as _shutil
    import subprocess

    resolved = _shutil.which(claude_binary) or claude_binary
    real = str(Path(resolved).resolve())
    found, error = {}, None
    for literal in RULE_SYNTAX_LITERALS:
        try:
            done = subprocess.run(["grep", "-a", "-m1", "-F", "-q", literal, real],
                                  capture_output=True, timeout=120, check=False)
            found[literal] = done.returncode == 0
        except (OSError, subprocess.SubprocessError) as exc:  # noqa: PERF203
            error = f"{type(exc).__name__}: {exc}"
            found[literal] = None
    return {
        "binary": real,
        "literals_present": found,
        "error": error,
        "supports": ("the `//`-prefixed filesystem-absolute rule form used by "
                     f"{DENY_PROC_RULE!r}"),
        "does_not_support": ("that the rule blocks a Read; that is a vendor contract until a "
                             "model process demonstrates it"),
    }


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


def writable_launch_argv(context: Any, model: str = PLACEHOLDER_MODEL,
                         ) -> tuple[list[str], dict[str, Any]]:
    """The real writable inner argv, built by the adapter's own code path.

    Not a reconstruction: `_argv` is the function the launch path calls, and the capabilities
    come from the context the launch was prepared with, so an argv change that reintroduced a
    host path would break this check rather than pass beside it.
    """
    argv, controls = _argv(context.claude_binary, model, "<preflight task prompt>",
                           "preflight-session", context.capabilities,
                           Path("/unused-host-path-must-not-appear"), writable=True)
    return argv, controls


@contextmanager
def _context_for(context: Any, claude_binary: str, base_env: Mapping[str, str] | None):
    """Yield the launch context to measure: the caller's, or one derived the same way.

    A context that arrives from the adapter is used as it is. Otherwise one is built by
    `prepare_writable_launch` -- the adapter's own function -- so there is never a second
    implementation of the environment contract for the criterion to measure against.
    """
    if context is not None:
        if not isinstance(context, WritableLaunchContext):
            raise AdapterError("the launch preflight requires a prepared launch context")
        yield context
        return
    with tempfile.TemporaryDirectory(prefix="b2-preflight-") as tmp:
        yield prepare_writable_launch(claude_binary=claude_binary, base_env=base_env,
                                      config_dir=Path(tmp) / "claude-config")


def invalid_credential_canary() -> str:
    """A synthetic value for the negative control. Built fresh, never stored anywhere.

    Deliberately shaped like a subscription OAuth token. The installed runtime turns out not
    to care -- measured, any non-blank value is accepted and only whitespace is not -- but a
    later runtime that did validate could reject a malformed value on *shape*, and a control
    rejected for the wrong reason would read as "this runtime validates" and let mere presence
    turn the criterion green. A shape-plausible canary can only be rejected for its value.
    """
    import uuid
    return f"sk-ant-oat01-B2-INVALID-CREDENTIAL-CONTROL-{uuid.uuid4().hex}{uuid.uuid4().hex}"


def _auth_probe(run, claude_binary: str, *, timeout: int = 180) -> dict[str, Any]:
    """`claude auth status` inside a view. No prompt, no -p, no request of any kind."""
    result = _run_in_view(run, [claude_binary, "auth", "status"], timeout=timeout)
    try:
        parsed = json.loads(result["stdout_tail"])
    except (ValueError, TypeError):
        parsed = None
    if not isinstance(parsed, dict):
        parsed = {}
    return {
        "result": result,
        "parsed": parsed,
        "logged_in": parsed.get("loggedIn") is True,
        "accepted": result["returncode"] == 0 and parsed.get("loggedIn") is True,
    }


def _run_in_view(run, argv: list[str], *, timeout: int | None = None) -> dict[str, Any]:
    out = run(argv, view_timeout=timeout)
    return {"argv": argv, "returncode": out["returncode"], "payload_started": out["payload_started"],
            "timed_out": out["timed_out"],
            "stdout_tail": (out["stdout"] or "")[-2000:], "stderr_tail": (out["stderr"] or "")[-2000:]}


def preflight(context: Any = None, *, claude_binary: str = "claude",
              base_env: Mapping[str, str] | None = None,
              model: str = PLACEHOLDER_MODEL) -> dict[str, Any]:
    """Answer all three questions, for one launch context. No model request is made.

    The environment handed to the view is the adapter's **filtered child environment**, not
    the raw host environment. That distinction is the whole point of the parameter: measuring
    a view built from `os.environ` would have answered a question about variables the model
    process never inherits -- including, in principle, a credential it never receives.
    """
    with _context_for(context, claude_binary, base_env) as prepared:
        return _preflight(prepared, model)


def _preflight(context: Any, model: str) -> dict[str, Any]:
    claude_binary = context.claude_binary
    env = dict(context.child_env)
    argv, controls = writable_launch_argv(context, model)
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

        # 2a. The runtime is executable in the view at all -- with the credential-scrub
        # control in force, which is not free: this build refuses to start with the control
        # set unless bubblewrap is available to it, so this is also where a missing bwrap in
        # the view surfaces, as a startup failure rather than as a silent downgrade.
        version = _run_in_view(run, [claude_binary, "--version"], timeout=180)
        stderr = (version["stderr_tail"] or "")
        checks["runtime_executable_in_view"] = {
            "ok": version["returncode"] == 0,
            "version": (version["stdout_tail"] or "").strip().splitlines()[:1],
            "subprocess_credential_scrub_requested": env.get(SUBPROCESS_SCRUB_ENV) == "1",
            "bubblewrap_missing": "bubblewrap is required" in stderr,
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

        # 2c. Path-valued transport variables. A value that names nothing inside the view is
        # not a boundary leak, but it is a real transport mismatch: the runtime logs a load
        # failure and carries on with a trust store the launch did not intend. Each one is
        # planned, then the plan's result is tested for real inside the view.
        view_env = view_environment(env, claude_binary)
        transport = transport_path_plan(env)
        expected = {}
        for name, entry in transport.items():
            if entry["action"] == "keep":
                expected[name] = env[name].strip()
            elif entry["action"] == "stage":
                expected[name] = entry["view_path"]
        script = "\n".join([
            "set +e", "rc=0",
            *[f'if [ -e {shlex.quote(path)} ]; then echo "PRESENT {name}"; '
              f'else echo "MISSING {name}"; rc=1; fi' for name, path in expected.items()],
            'exit "$rc"',
        ])
        present_transport = _run_in_view(run, ["/bin/sh", "-c", script], timeout=120)
        unreachable = [l.split(" ", 1)[1] for l in present_transport["stdout_tail"].splitlines()
                       if l.startswith("MISSING ")]
        rejected = sorted(n for n, e in transport.items() if e["action"] == "reject")
        # A dropped or rejected variable must be gone from the view environment, not merely
        # planned away.
        still_present = sorted(n for n, e in transport.items()
                               if e["action"] in ("drop", "reject") and n in view_env)
        checks["transport_paths_resolve_in_view"] = {
            "ok": not unreachable and not rejected and not still_present,
            "unreachable_in_view": unreachable,
            "rejected": rejected,
            "removed_but_still_in_view_environment": still_present,
            "detail": present_transport,
        }

        # 3. The authentication path, in exactly this view and this environment.
        actual = _auth_probe(run, claude_binary)

    # 4. The negative control, in a second view built from the same contract: same binary,
    # same provider, same mounts, same filtered environment and the same controls, with only
    # the credential replaced by a synthetic invalid one. Whether `auth status` reports
    # anything about *validity* is a property of the runtime, so it is measured on the runtime
    # rather than assumed -- and re-measured on every evaluation, so a build that starts
    # validating is recognised instead of being locked out by a constant.
    control_env = dict(env)
    control_env[SUBSCRIPTION_OAUTH_ENV] = invalid_credential_canary()
    # The control has to be answered by the canary and by nothing else. If the environment
    # offers another credential channel, an acceptance could be that channel's doing, and the
    # control would silently measure the wrong thing.
    control_mode = effective_auth_mode(control_env)
    control_answerable = control_mode == AUTH_SUBSCRIPTION_OAUTH
    with model_view(claude_binary=claude_binary, env=control_env) as control_run:
        control = _auth_probe(control_run, claude_binary)
    # What the control actually answers: does `auth status` on this runtime tell the supplied
    # credential apart from a synthetic invalid one? That is discrimination, and it is a
    # property of the local CLI -- a refusal could come from syntax, length, character set,
    # internal token structure, a checksum or any other local parser rule, and nothing proves
    # the canary is parser-equivalent to a real `claude setup-token` credential.
    discriminates = (control_answerable and actual["accepted"] and not control["accepted"])
    # What the control does NOT answer: whether the real credential is valid at the service.
    # Only an operation that actually authenticates server-side can show that, and this phase
    # performs none. Never derived from `auth status`, in either direction.
    server_validity: Any = UNKNOWN_OBSERVATION
    if not actual["accepted"]:
        state = "no-credential-accepted"
    elif control["accepted"]:
        state = "credential-accepted-but-runtime-accepts-an-invalid-one"
    else:
        state = "credential-accepted-and-invalid-control-refused"
    parsed = actual["parsed"]
    checks["authenticated_in_view"] = {
        # Green needs both: the intended credential path recognised locally, and a server-side
        # authenticated operation that used it. The second is out of scope for this phase, so
        # this sub-check is red by construction here -- and for a reason that names the gap
        # rather than the host's missing token.
        "ok": actual["accepted"] and server_validity is True,
        "state": state,
        "credential_accepted_by_cli": actual["accepted"],
        "logged_in": actual["logged_in"],
        "invalid_control_accepted_by_cli": control["accepted"],
        "auth_status_discriminates_invalid_control": discriminates,
        "server_credential_validity_observed": server_validity,
        "discrimination_rule": ("auth_status_discriminates_invalid_control = "
                                "credential_accepted_by_cli AND NOT "
                                "invalid_control_accepted_by_cli"),
        "server_validity_rule": ("server_credential_validity_observed is set only by an "
                                 "operation that authenticates against the service. It is "
                                 "never derived from `auth status`: a local acceptance or "
                                 "refusal can rest on syntax, length, character set, token "
                                 "structure or a checksum, and the canary is not demonstrably "
                                 "parser-equivalent to a real setup-token credential."),
        # Names and classifications only. No token, no canary, no value, no hash of a value.
        "auth_method": parsed.get("authMethod"),
        "api_provider": parsed.get("apiProvider"),
        "config_directory": parsed.get("configDirectory"),
        "subscription_token_supplied": SUBSCRIPTION_OAUTH_ENV in env,
        "effective_auth_mode": effective_auth_mode(env),
        "credential_channels_active": sorted(n for n, on in credential_channels(env).items() if on),
        "detail": actual["result"],
    }
    invalid_credential_control = {
        "executed": True,
        "model_involved": False,
        "credential_accepted_by_cli": control["accepted"],
        "logged_in": control["logged_in"],
        "returncode": control["result"]["returncode"],
        "answerable_by_the_canary_alone": control_answerable,
        "control_effective_auth_mode": control_mode,
        "auth_method": control["parsed"].get("authMethod"),
        "variable": SUBSCRIPTION_OAUTH_ENV,
        "canary_persisted": False,
        "what_it_decides": ("whether `auth status` on this runtime discriminates the supplied "
                            "credential from a synthetic invalid one at all"),
        "what_it_does_not_decide": ("whether a real credential is valid at the service: a "
                                    "local refusal could be about syntax or structure, so "
                                    "server validity needs its own observation"),
        "same_as_the_measured_launch": ["claude_binary", "confinement provider", "mount contract",
                                        "filtered child environment", "controls including "
                                        + SUBPROCESS_SCRUB_ENV],
        "detail": {k: v for k, v in control["result"].items() if k != "stdout_tail"},
    }

    ok = audit["ok"] and all(c["ok"] for c in checks.values())
    return {
        "contract": PREFLIGHT_CONTRACT,
        "phase": "4.2C / B2",
        "model_placeholder": model,
        "claude_binary": claude_binary,
        "mount_contract": mount_contract(claude_binary),
        # Names only, and only the names the adapter's own environment contract admits.
        "child_environment_names": sorted(env),
        "child_environment_policy": {
            "policy": context.env_policy.get("policy"),
            "inherited_names": list(context.env_policy.get("inherited_names", [])),
            "controls_applied": list(context.env_policy.get("controls_applied", [])),
            "removed_agent_names": list(context.env_policy.get("removed_agent_names", [])),
            "removed_generation_names": list(context.env_policy.get("removed_generation_names", [])),
            "removed_other_count": context.env_policy.get("removed_other_count"),
        },
        "view_environment_names": sorted(view_environment(env, claude_binary)),
        "transport_path_environment": transport,
        "invalid_credential_control": invalid_credential_control,
        "permission_rule_syntax": rule_syntax_evidence(claude_binary),
        "process_environment_read_rule": {
            "rule": DENY_PROC_RULE,
            "in_requested_deny_rules": DENY_PROC_RULE in list(controls["requested_deny_rules"]),
            "why": ("the credential-scrub control protects Bash subprocesses, hooks and stdio "
                    "MCP processes; the built-in Read tool is none of those and runs inside "
                    "the parent, which is the process holding the token"),
            "pseudo_filesystems_in_the_view": ["/proc", "/dev"],
            "not_restricted": {"/dev": "carries no process environments; no threat path, so no rule"},
            "measured_here": "that the rule is in the deny list the launch requests",
            "not_measured_here": ("that the runtime refuses the Read; demonstrating that needs "
                                  "a model process"),
        },
        "normalized_inner_argv": list(controls["normalized_argv"]),
        "argv_audit": audit,
        "checks": checks,
        "ok": ok,
        "note": ("Model-free. No request was made; `--version`, `--help` and `auth status` "
                 "never reach a model. A false `authenticated_in_view` is a pilot blocker, not "
                 "a reason to widen the view."),
        "subprocess_credential_scrub": {
            "variable": SUBPROCESS_SCRUB_ENV,
            "requested": env.get(SUBPROCESS_SCRUB_ENV) == "1",
            "vendor_contract": ("the Claude Code parent keeps its provider credentials while "
                                "Bash tool subprocesses, hooks and stdio MCP processes do not "
                                "inherit them; on Linux those subprocesses additionally run in "
                                "their own PID namespace and cannot read the parent's "
                                "environment through /proc"),
            "measured_here": ("that the control is in the child environment, and that the "
                              "runtime starts inside the view with it in force"),
            "not_measured_here": ("that a subprocess actually fails to see the credential; "
                                  "that requires a running model process and is out of scope"),
        },
    }


def launchable(context: Any = None) -> tuple[bool, str]:
    """The readiness criterion: one answer, with the failing part named."""
    try:
        report = preflight(context)
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
            if name == "authenticated_in_view":
                # The server-validity gap is what stands even on a host that supplies a
                # perfectly good token, so it is named first and the local state follows it.
                if check["server_credential_validity_observed"] is not True:
                    failures.append(
                        "authenticated_in_view: server credential validity not yet observed "
                        f"(local state: {check['state']}; auth_status_discriminates_invalid_"
                        f"control={check['auth_status_discriminates_invalid_control']})")
                else:
                    failures.append(f"authenticated_in_view: {check['state']}")
            elif name == "transport_paths_resolve_in_view":
                failures.append(
                    "transport_paths_resolve_in_view: "
                    + "; ".join(filter(None, [
                        f"unreachable in the view: {check['unreachable_in_view']}"
                        if check["unreachable_in_view"] else "",
                        f"needs a decision: {check['rejected']}" if check["rejected"] else "",
                        f"removed but still passed on: "
                        f"{check['removed_but_still_in_view_environment']}"
                        if check["removed_but_still_in_view_environment"] else ""])))
            elif name == "runtime_executable_in_view" and check.get("bubblewrap_missing"):
                failures.append("runtime_executable_in_view: the runtime refuses to start with "
                                "the mandatory credential scrub because bubblewrap is not in "
                                "the view")
            else:
                failures.append(f"{name} failed")
    if failures:
        return False, "; ".join(failures)
    return True, ("the writable argv is view-local, the runtime starts and parses the writable "
                  "flags inside the view, the intended credential path is the one this launch "
                  "would select, and the credential was used in a server-side authenticated "
                  "operation rather than merely recognised locally")


EVIDENCE_CONTRACT = "verification-governance-b2-launch-preflight-evidence/v1"


def evidence_document(claude_binary: str = "claude") -> dict[str, Any]:
    """The preflight result shaped as the committed evidence artifact."""
    try:
        from .b2_pilot_readiness import evidence_binding
    except ImportError:  # direct script sibling import
        from b2_pilot_readiness import evidence_binding
    report = preflight(claude_binary=claude_binary)
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
