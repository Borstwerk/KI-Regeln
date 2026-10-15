"""Preparation controls only: no credential, Claude execution or model request."""
import contextlib
import io
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools import b2_auth_bootstrap as bootstrap


def identity():
    return {"Uid": [1000] * 4, "Gid": [1000] * 4, "Groups": [1000],
            "CapInh": 0, "CapPrm": 0, "CapEff": 0, "CapAmb": 0, "NoNewPrivs": 1}


class IdentityContractTests(unittest.TestCase):
    def test_nonprivileged_identity_does_not_authorise_auth_or_pilot(self):
        observation, blockers = bootstrap.assess_identity(identity())
        self.assertEqual(observation, identity())
        self.assertEqual(blockers, [])

    def test_root_saved_ids_groups_capabilities_and_privilege_gain_are_blocked(self):
        for field in ("Uid", "Gid", "Groups", "CapInh", "CapPrm", "CapEff", "CapAmb", "NoNewPrivs"):
            value = identity()
            value[field] = ([1000, 1000, 0, 1000] if field in ("Uid", "Gid")
                            else [0] if field == "Groups" else 0 if field == "NoNewPrivs" else 1)
            with self.subTest(field=field):
                observation, blockers = bootstrap.assess_identity(value)
                self.assertEqual(observation, value)
                self.assertTrue(blockers)

    def test_missing_extra_and_wrong_type_observations_are_not_persisted(self):
        bad = [None, [], {}, {**identity(), "secret": "synthetic-sensitive"}]
        for key in identity():
            bad.append({name: value for name, value in identity().items() if name != key})
            bad.append({**identity(), key: True})
        bad.extend([{**identity(), "Uid": [True] * 4}, {**identity(), "Gid": [1000]},
                    {**identity(), "Groups": [-1]}, {**identity(), "CapEff": 2**64},
                    {**identity(), "NoNewPrivs": "1"}])
        for value in bad:
            with self.subTest(value=value):
                observation, blockers = bootstrap.assess_identity(value)
                self.assertIsNone(observation)
                self.assertEqual(blockers, ["identity_observation_missing_or_malformed"])


class PreparationTests(unittest.TestCase):
    def prepare(self, observation=None):
        with tempfile.TemporaryDirectory() as tmp:
            binary = Path(tmp) / "claude"
            # It is hashed, never executed. A CLI execution would fail this test's intent.
            binary.write_text("this file must never be executed", encoding="utf-8")
            binary.chmod(0o755)
            with mock.patch.dict(os.environ, {}, clear=True), mock.patch.object(
                    bootstrap, "_measure_identity", return_value=identity() if observation is None else observation) as measure:
                report = bootstrap.prepare(claude_binary=str(binary), base_env={"HTTPS_PROXY": "secret-proxy"})
            self.assertEqual(measure.call_count, 1)
            env = measure.call_args.args[1]
            self.assertNotIn("HTTPS_PROXY", env)
            self.assertEqual(env["CLAUDE_CODE_SUBPROCESS_ENV_SCRUB"], "1")
            return report

    def test_prepared_report_roundtrip_cannot_admit_any_live_operation(self):
        report = json.loads(json.dumps(self.prepare()))
        self.assertEqual(report["status"], "PREPARED_ONLY")
        self.assertFalse(report["may_start_authentication"])
        self.assertFalse(report["may_start_model_pilot"])
        self.assertEqual(report["cli_execution"], "NOT RUN")
        self.assertTrue(all(job["status"] == "NOT RUN" for job in report["pending_jobs"]))
        self.assertNotIn("secret-proxy", json.dumps(report))

    def test_explicit_empty_env_does_not_hide_ambient_credentials(self):
        for ambient, supplied in (({"CLAUDE_CODE_OAUTH_TOKEN": "synthetic-sensitive"}, {}),
                                  ({}, {"ANTHROPIC_API_KEY": "synthetic-sensitive"}),
                                  ({}, {"CLAUDE_CODE_OAUTH_TOKEN_FILE": "/private/token"})):
            with self.subTest(ambient=list(ambient), supplied=list(supplied)):
                with mock.patch.dict(os.environ, ambient, clear=True), mock.patch.object(
                        bootstrap, "_measure_identity", side_effect=AssertionError("must stop first")):
                    report = bootstrap.prepare(base_env=supplied)
                self.assertEqual(report["status"], "BLOCKED")
                self.assertIn("credentials_present_preparation_refused", report["blockers"])
                self.assertNotIn("synthetic-sensitive", json.dumps(report))
                self.assertNotIn("/private/token", json.dumps(report))

    def test_root_payload_is_reported_and_blocked(self):
        root = identity()
        root["Uid"] = [0] * 4
        report = self.prepare(root)
        self.assertEqual(report["status"], "BLOCKED")
        self.assertEqual(report["identity_observation"]["Uid"], [0] * 4)

    def test_failed_probe_drops_arbitrary_diagnostic_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            binary = Path(tmp) / "claude"
            binary.write_text("no execution", encoding="utf-8")
            binary.chmod(0o755)
            with mock.patch.dict(os.environ, {}, clear=True), mock.patch.object(
                    bootstrap, "_measure_identity", side_effect=OSError("synthetic-sensitive")):
                report = bootstrap.prepare(claude_binary=str(binary))
        self.assertEqual(report["status"], "BLOCKED")
        self.assertNotIn("synthetic-sensitive", json.dumps(report))

    def test_unknown_execution_or_token_arguments_are_rejected_without_echo(self):
        output = io.StringIO()
        with contextlib.redirect_stderr(output), self.assertRaises(SystemExit):
            bootstrap.main(["--prepare-only", "--token", "synthetic-sensitive", "--execute"])
        self.assertNotIn("synthetic-sensitive", output.getvalue())

    def test_cli_persists_only_the_preparation_report_and_returns_blocked(self):
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / "report.json"
            with mock.patch.dict(os.environ, {"ANTHROPIC_API_KEY": "synthetic-sensitive"}, clear=True):
                with contextlib.redirect_stdout(io.StringIO()) as console:
                    code = bootstrap.main(["--prepare-only", "--report", str(destination)])
            self.assertEqual(code, 2)
            self.assertEqual(json.loads(console.getvalue()), json.loads(destination.read_text()))
            self.assertNotIn("synthetic-sensitive", destination.read_text())


class MeasurementControlsTests(unittest.TestCase):
    def test_timeout_cannot_become_a_successful_observation(self):
        import subprocess
        from types import SimpleNamespace

        @contextlib.contextmanager
        def confined(*args, **kwargs):
            yield SimpleNamespace(argv=["fixed-boundary"], env={})
        timeout = subprocess.TimeoutExpired(["fixed-boundary"], 30,
                                            output="synthetic-sensitive", stderr="synthetic-sensitive")
        with mock.patch.object(bootstrap.sys, "platform", "linux"), mock.patch.object(
                bootstrap, "confined_model_invocation", side_effect=confined), mock.patch.object(
                bootstrap.subprocess, "run", side_effect=timeout):
            with self.assertRaisesRegex(bootstrap.PreparationError, "^identity_probe_timed_out$"):
                bootstrap._measure_identity("unused", {})

    def test_boundary_marker_and_successful_complete_payload_are_required(self):
        from types import SimpleNamespace
        from tools.b2_auth_bootstrap import PreparationError

        for started, rc, stdout in ((False, 0, json.dumps(identity())),
                                    (True, 1, json.dumps(identity())), (True, 0, "synthetic-sensitive")):
            invocation = SimpleNamespace(argv=["fixed-boundary"], env={}, payload_started=lambda: started)
            @contextlib.contextmanager
            def confined(*args, **kwargs):
                yield invocation
            result = SimpleNamespace(returncode=rc, stdout=stdout, stderr="synthetic-sensitive")
            with self.subTest(started=started, rc=rc, stdout=stdout):
                with mock.patch.object(bootstrap.sys, "platform", "linux"), mock.patch.object(
                        bootstrap, "confined_model_invocation", side_effect=confined), mock.patch.object(
                        bootstrap.subprocess, "run", return_value=result):
                    with self.assertRaises(PreparationError) as caught:
                        bootstrap._measure_identity("unused", {})
                self.assertNotIn("synthetic-sensitive", str(caught.exception))
