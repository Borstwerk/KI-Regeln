"""Negative controls for the test runner's success claims; not runtime evidence."""
import contextlib
import io
import json
import unittest
from types import SimpleNamespace
from unittest import mock

from tools import b2_test_runner


class RunnerClaimTests(unittest.TestCase):
    def test_complete_integration_keeps_original_modules_and_adds_bootstrap_controls(self):
        result = SimpleNamespace(testsRun=1, skipped=[], failures=[], errors=[], wasSuccessful=lambda: True)
        with mock.patch.object(b2_test_runner, "integration_prerequisites", return_value=[]), mock.patch.object(
                unittest.defaultTestLoader, "loadTestsFromNames") as loader, mock.patch.object(
                unittest.TextTestRunner, "run", return_value=result), contextlib.redirect_stdout(io.StringIO()):
            b2_test_runner.main(["--integration"])
        self.assertEqual(loader.call_args.args[0], [
            "tests.test_verification_surface", "tests.test_verification_surface_b2_design",
            "tests.test_b2_preflight_controls", "tests.test_b2_test_runner", "tests.test_b2_auth_bootstrap",
            "tests.test_verification_surface_b2_implementation", "tests.test_b2_bootstrap_runtime",
        ])

    def test_missing_integration_prerequisites_stop_before_tests(self):
        output = io.StringIO()
        with mock.patch.object(b2_test_runner, "integration_prerequisites", return_value=["no Linux"]):
            with mock.patch.object(unittest.TextTestRunner, "run", side_effect=AssertionError("must not run")):
                with contextlib.redirect_stdout(output):
                    code = b2_test_runner.main(["--integration"])
        self.assertEqual(code, 2)
        report = json.loads(output.getvalue())
        self.assertEqual(report["status"], "BLOCKED")
        self.assertEqual(report["real_cli_and_boundary_tests"], "NOT RUN")

    def test_skipped_or_empty_integrations_cannot_report_pass(self):
        for count, skipped in ((1, [("test", "unavailable")]), (0, [])):
            result = SimpleNamespace(testsRun=count, skipped=skipped, failures=[], errors=[],
                                     wasSuccessful=lambda: True)
            output = io.StringIO()
            with self.subTest(count=count, skipped=skipped):
                with mock.patch.object(b2_test_runner, "integration_prerequisites", return_value=[]):
                    with mock.patch.object(unittest.TextTestRunner, "run", return_value=result):
                        with contextlib.redirect_stdout(output):
                            code = b2_test_runner.main(["--integration"])
                self.assertEqual(code, 1)
                report = json.loads(output.getvalue())
                self.assertEqual(report["status"], "FAIL")
                self.assertEqual(report["skip_details"],
                                 [{"test": str(test), "reason": reason} for test, reason in skipped])
                self.assertEqual(report["server_authentication"], "NOT RUN")
                self.assertEqual(report["credential_subprocess_and_read_enforcement"], "NOT RUN")
