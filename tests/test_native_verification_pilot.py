"""Independent pilot report assertions; native processes are executed by the CI job."""
from __future__ import annotations

import hashlib
import json
import os
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
REPORTS = Path(os.environ.get("KI_REGELN_PILOT_REPORT_DIR", ROOT / ".validation/pilot"))
SCHEMA = json.loads((ROOT / "Schemas/verification-run.schema.json").read_text(encoding="utf-8"))
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())

SOURCES = {
    "powershell": [
        "Evals/Verification-Portable/Run-Pilot.ps1",
        "Evals/Verification-Portable/fixtures/powershell/Discount.ps1",
        "Evals/Verification-Portable/fixtures/powershell/Test-Discount.ps1",
    ],
    "dotnet": [
        "Evals/Verification-Portable/Run-Pilot.ps1",
        "Evals/Verification-Portable/fixtures/dotnet/Discount.csproj",
        "Evals/Verification-Portable/fixtures/dotnet/Program.cs",
    ],
    "missing-runtime": ["Evals/Verification-Portable/Run-Pilot.ps1"],
}
MARKERS = {"powershell": "NATIVE_POWERSHELL_ASSERTIONS_PASS",
           "dotnet": "NATIVE_DOTNET_ASSERTIONS_PASS"}


def bound_sha256(scenario: str) -> str:
    lines = [f"{p}:{hashlib.sha256((ROOT / p).read_bytes()).hexdigest()}"
             for p in sorted(SOURCES[scenario])]
    return hashlib.sha256(("\n".join(lines) + "\n").encode("utf-8")).hexdigest()


def read_report(scenario: str) -> dict:
    raw = json.loads((REPORTS / (scenario + ".json")).read_text(encoding="utf-8"))
    VALIDATOR.validate(raw)
    if raw["source_state"]["kind"] != "snapshot":
        raise AssertionError("Expected bounded source snapshot")
    if raw["source_state"]["content_sha256"] != bound_sha256(scenario):
        raise AssertionError("Native source digest mismatch")
    return raw


class NativeVerificationPilotTests(unittest.TestCase):
    def test_powershell_native_check(self):
        doc = read_report("powershell")
        check = doc["checks"][0]
        self.assertEqual(check["status"], "PASS")
        self.assertEqual(check["tool"], "pwsh")
        self.assertEqual(check["exit_code"], 0)
        self.assertEqual(check["skipped"], 0)
        self.assertEqual(len(check["evidence_refs"]), 1)
        self.assertIn(MARKERS["powershell"],
                      (REPORTS / check["evidence_refs"][0]).read_text(encoding="utf-8"))

    def test_dotnet_native_check(self):
        doc = read_report("dotnet")
        check = doc["checks"][0]
        self.assertEqual(check["status"], "PASS")
        self.assertEqual(check["tool"], "dotnet")
        self.assertEqual(check["exit_code"], 0)
        self.assertEqual(check["skipped"], 0)
        self.assertEqual(len(check["evidence_refs"]), 1)
        self.assertIn(MARKERS["dotnet"],
                      (REPORTS / check["evidence_refs"][0]).read_text(encoding="utf-8"))

    def test_missing_runtime_is_not_run(self):
        doc = read_report("missing-runtime")
        check = doc["checks"][0]
        self.assertEqual(check["status"], "NOT_RUN")
        self.assertIsNone(check["exit_code"])
        self.assertEqual(check["evidence_refs"], [])
        self.assertIn("not found", check["reason"].lower())
        self.assertTrue(check["required_for_claim"])

    def test_native_environment_not_fabricated(self):
        for scenario in SOURCES:
            env = read_report(scenario)["environment"]
            self.assertEqual(env["location"],
                             "ci" if os.environ.get("GITHUB_ACTIONS") == "true" else "local")
            self.assertIn("PowerShell", env["runtime"])
            self.assertTrue(env["os"].strip())

    def test_no_pilot_report_claims_overall_green(self):
        for scenario in SOURCES:
            doc = read_report(scenario)
            self.assertNotIn("overall_pass", doc)
            self.assertNotIn("overall", doc)

    def test_schema_rejects_fake_pass_on_missing_runtime(self):
        doc = read_report("missing-runtime")
        doc["checks"][0]["status"] = "PASS"
        self.assertTrue(list(VALIDATOR.iter_errors(doc)))

    def test_source_binding_detects_tamper(self):
        doc = read_report("powershell")
        doc["source_state"]["content_sha256"] = "0" * 64
        self.assertNotEqual(doc["source_state"]["content_sha256"], bound_sha256("powershell"))


if __name__ == "__main__":
    unittest.main()
