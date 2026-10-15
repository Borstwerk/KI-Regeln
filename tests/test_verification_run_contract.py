"""Portable verification report contract: schema-positive and adversarial negative controls.

These are synthetic schema checks; no project test, native runner, model or HTML
renderer is executed by this suite.
"""
from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


SCHEMA = json.loads(
    (Path(__file__).resolve().parents[1] / "Schemas/verification-run.schema.json")
    .read_text(encoding="utf-8")
)
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())


def example() -> dict:
    return {
        "schema_version": 1,
        "project": {"name": "Demo"},
        "task": "Verify a change",
        "source_state": {"kind": "git-clean", "revision": "abc123"},
        "environment": {"location": "local", "os": "Windows", "runtime": "PowerShell 7.4"},
        "checks": [{
            "id": "pester", "type": "unit", "required_for_claim": True,
            "selection": "project-prescribed", "tool": "Pester",
            "status": "PASS", "exit_code": 0, "skipped": 0,
            "evidence_refs": ["artifacts/pester.xml"],
            "observed_at": "2026-10-15T09:00:00Z",
        }],
    }


class VerificationRunContractTests(unittest.TestCase):
    def setUp(self):
        self.report = example()

    def assert_invalid(self, report):
        errors = list(VALIDATOR.iter_errors(report))
        self.assertTrue(errors, "invalid evidence must not satisfy the report schema")

    def test_schema_itself_is_valid(self):
        Draft202012Validator.check_schema(SCHEMA)

    def test_native_powershell_report_valid(self):
        VALIDATOR.validate(self.report)

    def test_native_dotnet_ci_report_valid(self):
        report = example()
        report["environment"] = {"location": "ci", "os": "Linux", "runtime": ".NET 8"}
        report["checks"][0].update(tool="dotnet test", type="unit")
        VALIDATOR.validate(report)

    def test_clean_vs_dirty_source_requires_scope_and_digest(self):
        self.report["source_state"] = {"kind": "git-dirty", "revision": "abc123"}
        self.assert_invalid(self.report)
        self.report["source_state"].update(
            content_sha256="a" * 64, digest_scope="tracked+untracked files"
        )
        VALIDATOR.validate(self.report)
        self.report["source_state"]["content_sha256"] = "not-a-hash"
        self.assert_invalid(self.report)

    def test_snapshot_source_requires_digest(self):
        self.report["source_state"] = {"kind": "snapshot", "digest_scope": "workspace"}
        self.assert_invalid(self.report)
        self.report["source_state"]["content_sha256"] = "f" * 64
        VALIDATOR.validate(self.report)

    def test_unanchored_source_cannot_claim_pass(self):
        self.report["source_state"] = {"kind": "unavailable", "reason": "no snapshot"}
        self.assert_invalid(self.report)
        self.report["checks"][0].update(status="UNVERIFIED", reason="source unbound")
        VALIDATOR.validate(self.report)

    def test_false_green_nonzero_exit_is_rejected(self):
        self.report["checks"][0]["exit_code"] = 1
        self.assert_invalid(self.report)

    def test_false_green_without_evidence_is_rejected(self):
        self.report["checks"][0]["evidence_refs"] = []
        self.assert_invalid(self.report)

    def test_false_green_with_skipped_tests_is_rejected(self):
        self.report["checks"][0]["skipped"] = 1
        self.assert_invalid(self.report)

    def test_missing_pass_observation_time_is_rejected(self):
        del self.report["checks"][0]["observed_at"]
        self.assert_invalid(self.report)

    def test_not_run_must_have_no_exit_and_a_reason(self):
        check = self.report["checks"][0]
        check.update(status="NOT_RUN", exit_code=None, evidence_refs=[], reason="no SDK")
        VALIDATOR.validate(self.report)
        check["exit_code"] = 0
        self.assert_invalid(self.report)
        check["exit_code"] = None
        del check["reason"]
        self.assert_invalid(self.report)

    def test_blocked_must_not_reuse_prior_evidence(self):
        check = self.report["checks"][0]
        check.update(status="BLOCKED", exit_code=None, reason="approval missing")
        self.assert_invalid(self.report)
        check["evidence_refs"] = []
        VALIDATOR.validate(self.report)

    def test_unknown_status_and_extra_fields_rejected(self):
        self.report["checks"][0]["status"] = "SUCCESS"
        self.assert_invalid(self.report)
        self.report = example()
        self.report["overall_pass"] = True
        self.assert_invalid(self.report)


if __name__ == "__main__":
    unittest.main()
