#!/usr/bin/env python3
"""Prepare B2 authentication measurements without running Claude or accepting credentials.

This is a diagnostic prefix, never an admission path. No report authorises an auth request,
model call or pilot. The existing criterion 22 and writable admission remain authoritative.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Mapping

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.behavioral_harness_claude import (
    B2_CONTROL_ENV, CREDENTIAL_CHANNEL_NAMES, HOST_ONLY_AUTH_ENV, SECRET_ENV, _child_env,
    effective_tool_policy,
)
from tools.behavioral_harness_core import hash_file
from tools.b2_boundary import BoundaryError
from tools.b2_model_confinement import ConfinementError, confined_model_invocation
from tools.b2_pilot_readiness import evidence_binding

IDENTITY_KEYS = {"Uid", "Gid", "Groups", "CapInh", "CapPrm", "CapEff", "CapAmb", "NoNewPrivs"}
CAPABILITIES = ("CapInh", "CapPrm", "CapEff", "CapAmb")
CONTRACT = "verification-governance-auth-bootstrap-preparation/v1"
CREDENTIAL_NAMES = frozenset(SECRET_ENV) | set(HOST_ONLY_AUTH_ENV) | set(CREDENTIAL_CHANNEL_NAMES)
MINIMAL_ENV = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "TERM": "dumb"}
# Fixed trusted payload. It never reads environ, credentials, CLI configuration or network.
# Uid/Gid include real, effective, saved and filesystem IDs, not just the effective identity.
IDENTITY_PROBE = """import json
from pathlib import Path
fields = {}
for line in Path('/proc/self/status').read_text().splitlines():
    key, _, value = line.partition(':')
    if key in ('Uid', 'Gid', 'Groups'):
        fields[key] = [int(x) for x in value.split()]
    elif key in ('CapInh', 'CapPrm', 'CapEff', 'CapAmb'):
        fields[key] = int(value.strip(), 16)
    elif key == 'NoNewPrivs':
        fields[key] = int(value.strip())
print(json.dumps(fields))
"""
PENDING_JOBS = (
    "runtime_privilege_separation_review", "supported_request_and_budget_review",
    "managed_credential_path", "server_authentication", "invalid_credential_rejection",
    "subprocess_credential_isolation", "builtin_read_enforcement", "authenticated_context_binding",
)


class PreparationError(RuntimeError):
    """A fixed diagnostic code, never raw process output."""


def assess_identity(value: Any) -> tuple[dict[str, Any] | None, list[str]]:
    """Validate a complete fixed-shape observation; diagnostics never carry raw input."""
    malformed = ["identity_observation_missing_or_malformed"]
    if not isinstance(value, dict) or set(value) != IDENTITY_KEYS:
        return None, malformed
    for key in ("Uid", "Gid", "Groups"):
        row = value[key]
        if (not isinstance(row, list) or (key != "Groups" and len(row) != 4)
                or any(type(x) is not int or not 0 <= x < 2**32 for x in row)):
            return None, malformed
    for key in CAPABILITIES:
        if type(value[key]) is not int or not 0 <= value[key] < 2**64:
            return None, malformed
    if type(value["NoNewPrivs"]) is not int or value["NoNewPrivs"] not in (0, 1):
        return None, malformed
    blockers = []
    if any(0 in value[key] for key in ("Uid", "Gid", "Groups")):
        blockers.append("payload_has_root_identity_or_group")
    if any(value[key] != 0 for key in CAPABILITIES):
        blockers.append("payload_has_capabilities")
    if value["NoNewPrivs"] != 1:
        blockers.append("payload_allows_new_privileges")
    return {key: list(row) if isinstance(row, list) else row for key, row in value.items()}, blockers


def _measure_identity(binary: str, env: Mapping[str, str]) -> Any:
    if sys.platform != "linux":
        raise PreparationError("linux_runtime_required")
    with tempfile.TemporaryDirectory(prefix="b2-bootstrap-view-") as tmp:
        task = Path(tmp)
        workspace = task / "workspace"
        workspace.mkdir()
        with confined_model_invocation(
            ["/usr/bin/python3", "-I", "-c", IDENTITY_PROBE], task_root=task,
            workspace=workspace, env=env, claude_binary=binary, timeout=30,
        ) as invocation:
            try:
                result = subprocess.run(invocation.argv, env=invocation.env, cwd="/",
                                        capture_output=True, text=True, timeout=30, check=False)
            except subprocess.TimeoutExpired:
                raise PreparationError("identity_probe_timed_out") from None
            if not invocation.payload_started():
                raise PreparationError("boundary_payload_not_started")
            if result.returncode != 0:
                raise PreparationError("identity_probe_failed")
            # Raw stdout/stderr and exception messages are never part of the public report.
            try:
                return json.loads(result.stdout)
            except (ValueError, TypeError):
                raise PreparationError("identity_probe_invalid_json") from None


def prepare(*, claude_binary: str = "claude", base_env: Mapping[str, str] | None = None) -> dict[str, Any]:
    report: dict[str, Any] = {
        "contract": CONTRACT, "status": "BLOCKED", "blockers": [],
        "may_start_authentication": False, "may_start_model_pilot": False,
        "cli_execution": "NOT RUN", "behavioral_evals": "NOT RUN",
        "identity_observation": None, "binding": None,
        "pending_jobs": [{"job": job, "status": "NOT RUN"} for job in PENDING_JOBS],
        "scope": "trusted identity probe in the shared model view; no Claude execution",
        "network_namespace_unshared": False,
        "requested_tool_policy": effective_tool_policy(True),
        "report_is_admission": False,
    }
    supplied = base_env if base_env is not None else {}
    present = sorted(name for name in CREDENTIAL_NAMES if os.environ.get(name) or supplied.get(name))
    if present:
        report["blockers"] = ["credentials_present_preparation_refused"]
        report["credential_names_present"] = present
        return report
    try:
        named = Path(claude_binary)
        resolved = str(named) if named.is_absolute() and named.is_file() else shutil.which(claude_binary)
        if not resolved:
            raise PreparationError("cli_binary_not_found_for_binding")
        binary = str(Path(resolved).resolve())
        report["binding"] = {
            **evidence_binding(), "bootstrap_code": hash_file(Path(__file__)),
            "adapter_code": hash_file(ROOT / "tools/behavioral_harness_claude.py"),
            "cli_binary": hash_file(Path(binary)),
            "note": "diagnostic source/binary binding only; not an authenticated launch context",
        }
        with tempfile.TemporaryDirectory(prefix="b2-bootstrap-env-") as tmp:
            # No ambient proxy, provider, endpoint, transport file or arbitrary user control
            # reaches the child. Use the adapter's central controls without a second policy.
            env, _ = _child_env(MINIMAL_ENV, Path(tmp) / "config", B2_CONTROL_ENV)
            report["child_environment_names"] = sorted(env)
            observation, blockers = assess_identity(_measure_identity(binary, env))
        report["identity_observation"] = observation
        report["blockers"] = blockers
        report["status"] = "BLOCKED" if blockers else "PREPARED_ONLY"
    except PreparationError as exc:
        report["blockers"] = [str(exc)]
    except (BoundaryError, ConfinementError, OSError):
        report["blockers"] = ["runtime_measurement_unavailable"]
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--prepare-only", action="store_true", required=True)
    parser.add_argument("--claude-binary", default="claude")
    parser.add_argument("--report", type=Path)
    args, unsupported = parser.parse_known_args(argv)
    if unsupported:
        parser.error("unsupported arguments; credential and execution arguments are not accepted")
    report = prepare(claude_binary=args.claude_binary)
    encoded = json.dumps(report, indent=2) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    return 0 if report["status"] == "PREPARED_ONLY" else 2


if __name__ == "__main__":
    raise SystemExit(main())
