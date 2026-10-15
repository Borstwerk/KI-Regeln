#!/usr/bin/env python3
"""Run explicitly scoped B1/B2 checks without conflating portable and host evidence.

Neither mode starts a model. Integration requires the real Linux boundary and Claude
runtime, retains the complete original suite, and refuses to pass with skipped tests.
"""
from __future__ import annotations

import argparse
import json
import platform
import shutil
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

B2_TESTS = "tests.test_verification_surface_b2_implementation"
BASE_TESTS = [
    "tests.test_verification_surface",
    "tests.test_verification_surface_b2_design",
    "tests.test_b2_preflight_controls",
    "tests.test_b2_test_runner",
    "tests.test_b2_auth_bootstrap",
    "tests.test_b2_separated_runtime",
    "tests.test_b2_environment_transport",
]
PORTABLE = [
    *BASE_TESTS,
    *[f"{B2_TESTS}.{name}" for name in (
        "SeedIntegrityTests", "SurfaceCompletenessTests", "TrustChainTests",
        "AdapterCompatibilityTests", "PilotGateTests", "NoModelRunTests",
        "B2SystemPromptTests", "WritableMethodEvidenceTests",
    )],
    *[f"{B2_TESTS}.ToolNamesVersusPermissionRulesTests.{name}" for name in (
        "test_T1_the_writable_visible_tools_are_tool_names",
        "test_T2_the_writable_allow_rules_carry_the_narrow_bash_rule",
        "test_T3_the_permission_mode_is_locked_down",
        "test_T4_a_runtime_without_the_mode_fails_closed",
        "test_T5_observed_tool_names_are_compared_against_visible_tools",
        "test_T6_a_permission_rule_is_never_treated_as_an_observed_tool_name",
        "test_T7_the_read_only_argv_is_unchanged",
    )],
    *[f"{B2_TESTS}.ManagedCredentialPolicyTests.{name}" for name in (
        "test_P1_no_managed_policy_and_a_known_absent_remote_source_clears_the_path",
        "test_P2_a_managed_api_key_helper_fails_the_path_closed",
        "test_P3_a_managed_policy_without_a_credential_provider_does_not_block",
        "test_P4_an_unreadable_or_ambiguous_policy_fails_closed",
        "test_P5_an_empty_drop_in_directory_is_not_treated_as_a_policy",
    )],
]


def integration_prerequisites() -> list[str]:
    if platform.system() != "Linux":
        return ["Linux namespace provider required; no emulated or unconfined fallback"]
    from tools.b2_boundary import provider_available
    from tools.behavioral_harness_claude import AdapterError, probe_claude_code, require_capabilities

    failures = []
    available, reason = provider_available()
    if not available:
        failures.append(f"boundary provider unavailable: {reason}")
    if shutil.which("claude") is None:
        failures.append("Claude CLI is not installed/on PATH")
    else:
        try:
            require_capabilities(probe_claude_code("claude"))
        except AdapterError:
            failures.append("installed Claude CLI does not satisfy the adapter contract")
    return failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--portable", action="store_true")
    mode.add_argument("--integration", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args(argv)
    scope = "integration" if args.integration else "portable"
    missing = integration_prerequisites() if args.integration else []
    report = {"scope": scope, "behavioral_evals": "NOT RUN",
              "real_cli_and_boundary_tests": "NOT RUN",
              "server_authentication": "NOT RUN",
              "credential_subprocess_and_read_enforcement": "NOT RUN"}
    if missing:
        report.update(status="BLOCKED", reasons=missing)
        code = 2
    else:
        names = (BASE_TESTS + [B2_TESTS, "tests.test_b2_bootstrap_runtime",
                               "tests.test_b2_separation_runtime"]) if args.integration else PORTABLE
        suite = unittest.defaultTestLoader.loadTestsFromNames(names)
        result = unittest.TextTestRunner(verbosity=1).run(suite)
        success = result.wasSuccessful() and result.testsRun > 0 and not result.skipped
        report.update(status="PASS" if success else "FAIL", tests=result.testsRun,
                      failures=len(result.failures), errors=len(result.errors),
                      skipped=len(result.skipped),
                      skip_details=[{"test": str(test), "reason": reason}
                                    for test, reason in result.skipped])
        if args.integration:
            report["real_cli_and_boundary_tests"] = "PASS" if success else "UNVERIFIED"
        code = 0 if success else 1
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
