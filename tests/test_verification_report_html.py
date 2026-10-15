"""Offline HTML presentation tests; no native runner/model/browser evidence is asserted."""
from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from tools import verification_report_html as report
from tests.test_verification_run_contract import example


def local_case() -> dict:
    return {
        "schema_version": 1,
        "generated_at": "2026-10-15T09:00:00Z",
        "mode": "Full",
        "repository_head": "abc123",
        "overall": "PASS",
        "exit_code": 0,
        "behavioral_validation": "NOT RUN",
        "checks": [
            {"name": "Structural validation", "status": "PASS", "code": "",
             "message": "errors=0 warnings=1", "duration_ms": 3},
            {"name": "Git working tree", "status": "WARN", "code": "WORKTREE_DIRTY",
             "message": "Uncommitted files", "duration_ms": 2},
            {"name": "Current-tree exposure", "status": "SKIP", "code": "",
             "message": "Only in Release", "duration_ms": 0},
        ],
        "findings": [{"severity": "warning", "code": "WORKTREE_DIRTY",
                      "message": "Uncommitted files", "path": "src/app.ps1"}],
    }


class HTMLReportTests(unittest.TestCase):
    def test_portable_has_no_inferred_overall_pass(self):
        result = report.render_report(example())
        self.assertIn("Keine Gesamtfreigabe abgeleitet", result)
        self.assertIn("Pester", result)
        self.assertIn("PASS-Checks", result)
        self.assertNotIn("Strukturprüfung laut Harness: PASS", result)

    def test_local_report_retains_skip_and_separate_behavioral_not_run(self):
        result = report.render_report(local_case())
        self.assertIn("Strukturprüfung laut Harness: PASS", result)
        self.assertIn("Behavioral validation", result)
        self.assertIn("NOT RUN", result)
        self.assertIn("SKIP", result)
        self.assertIn("WORKTREE_DIRTY", result)
        self.assertIn("HEAD abc123; uncommitted state not fingerprinted", result)

    def test_error_local_report_is_not_green(self):
        data = local_case()
        data["overall"], data["exit_code"] = "FAIL", 1
        data["checks"][0]["status"] = "FAIL"
        rendered = report.render_report(data)
        self.assertIn("Strukturprüfung laut Harness: FAIL", rendered)
        self.assertIn("FAIL-Checks", rendered)

    def test_local_false_green_rejected(self):
        data = local_case()
        data["checks"][0]["status"] = "FAIL"
        with self.assertRaises(report.ReportError):
            report.render_report(data)

    def test_local_inconsistent_exit_rejected(self):
        data = local_case()
        data["exit_code"] = 1
        with self.assertRaises(report.ReportError):
            report.render_report(data)

    def test_native_invalid_schema_rejected(self):
        data = example()
        data["checks"][0]["status"] = "PASS"
        data["checks"][0]["exit_code"] = 9
        with self.assertRaises(report.ReportError):
            report.render_report(data)

    def test_missing_required_source_binding_rejected(self):
        data = example()
        data["source_state"] = {"kind": "unavailable", "reason": "no snapshot"}
        with self.assertRaises(report.ReportError):
            report.render_report(data)

    def test_untrusted_content_is_html_escaped(self):
        data = example()
        data["project"]["name"] = "<script>alert(1)</script>"
        data["checks"][0]["reason"] = '<img src=x onerror="alert(2)">'
        output = report.render_report(data, include_messages=True)
        self.assertNotIn("<script>", output)
        self.assertNotIn("<img src=", output)
        self.assertIn("&lt;script&gt;", output)
        self.assertIn("&lt;img src=", output)

    def test_sensitive_details_hidden_by_default(self):
        data = example()
        data["checks"][0]["command_display"] = "SECRET_COMMAND"
        data["checks"][0]["reason"] = "SECRET_REASON"
        data["checks"][0]["evidence_refs"] = ["private/SECRET_FILE"]
        output = report.render_report(data)
        for marker in ("SECRET_COMMAND", "SECRET_REASON", "SECRET_FILE"):
            self.assertNotIn(marker, output)
        self.assertIn("Evidence-Referenzen: 1", output)

    def test_sensitive_details_explicit_opt_in_only(self):
        data = example()
        data["checks"][0]["reason"] = "extra context"
        data["checks"][0]["command_display"] = "dotnet test"
        output = report.render_report(data, include_messages=True)
        self.assertIn("extra context", output)
        self.assertIn("dotnet test", output)
        self.assertIn("vor Weitergabe auf sensible Inhalte prüfen", output)

    def test_offline_static_document_no_scripts_or_links(self):
        output = report.render_report(example())
        self.assertIn("default-src 'none'", output)
        self.assertIn("<style>", output)
        self.assertIn("<details", output)
        self.assertNotIn("<script", output)
        self.assertNotIn('href=', output)
        self.assertNotIn('src=', output)

    def test_synthetic_blocker_kept_visible(self):
        data = example()
        data["checks"].append({
            "id": "db", "type": "integration", "required_for_claim": True,
            "selection": "discovered", "tool": "DB integration",
            "status": "BLOCKED", "exit_code": None, "skipped": 0,
            "evidence_refs": [], "reason": "no sandbox",
        })
        output = report.render_report(data)
        self.assertIn("BLOCKED", output)
        self.assertIn("Keine Gesamtfreigabe", output)
        self.assertIn("Offen / nicht ausgeführt", output)

    def test_cli_writes_standalone_html(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)
            inp, out = path / "result.json", path / "report.html"
            inp.write_text(json.dumps(local_case()), encoding="utf-8")
            self.assertEqual(report.main(["--input", str(inp), "--output", str(out)]), 0)
            self.assertTrue(out.exists())
            self.assertIn("<!doctype html>", out.read_text(encoding="utf-8").lower())

    def test_invalid_input_does_not_replace_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)
            inp, out = path / "result.json", path / "report.html"
            inp.write_text('{"invalid": true}', encoding="utf-8")
            out.write_text("previous trusted report", encoding="utf-8")
            with self.assertRaises(SystemExit) as result:
                report.main(["--input", str(inp), "--output", str(out)])
            self.assertEqual(result.exception.code, 2)
            self.assertEqual(out.read_text(encoding="utf-8"), "previous trusted report")

    def test_unsupported_input_kind_rejected(self):
        with self.assertRaises(report.ReportError):
            report.render_report({"schema_version": 1})

    def test_explicit_wrong_kind_rejected(self):
        with self.assertRaises(report.ReportError):
            report.render_report(local_case(), kind="verification-run")


if __name__ == "__main__":
    unittest.main()
