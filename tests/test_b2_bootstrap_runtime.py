"""Real Linux namespace observation. Selected only by the full integration runner."""
import os
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools import b2_auth_bootstrap as bootstrap


class RuntimePreparationTests(unittest.TestCase):
    def test_identity_is_measured_in_the_shared_view_without_a_claude_command(self):
        actual_run = subprocess.run
        calls = []

        def observe(argv, **kwargs):
            calls.append(argv)
            self.assertEqual(argv[0], "unshare")
            self.assertIn(bootstrap.IDENTITY_PROBE, argv)
            self.assertNotIn("--help", argv)
            self.assertNotIn("--version", argv)
            return actual_run(argv, **kwargs)

        # This test measures the fixed credential-free payload independently of whether
        # the operator supplied a credential for A20 elsewhere in the complete suite.
        # The parent environment is never patched or inherited by the payload.
        with tempfile.TemporaryDirectory() as tmp:
            env, _ = bootstrap._child_env(bootstrap.MINIMAL_ENV, Path(tmp) / "config", bootstrap.B2_CONTROL_ENV)
            with mock.patch.object(bootstrap.subprocess, "run", side_effect=observe):
                observed = bootstrap._measure_identity(str(Path(shutil.which("claude")).resolve()), env)
        self.assertEqual(len(calls), 1)
        observation, blockers = bootstrap.assess_identity(observed)
        self.assertIsNotNone(observation, blockers)
        self.assertEqual(observed["Uid"][:3], list(os.getresuid()))
        self.assertEqual(observed["Gid"][:3], list(os.getresgid()))
        self.assertEqual(sorted(observed["Groups"]), sorted(os.getgroups()))
        if os.geteuid() == 0:
            self.assertIn("payload_has_root_identity_or_group", blockers)

    def test_preparation_cli_runs_in_a_credential_free_child_not_the_operator_environment(self):
        with tempfile.TemporaryDirectory() as tmp:
            done = subprocess.run([
                sys.executable, str(bootstrap.ROOT / "tools/b2_auth_bootstrap.py"), "--prepare-only",
                "--claude-binary", str(Path(shutil.which("claude")).resolve()),
            ], env={**bootstrap.MINIMAL_ENV, "HOME": tmp}, cwd=tmp, text=True,
                capture_output=True, timeout=45, check=False)
        self.assertIn(done.returncode, (0, 2))
        report = json.loads(done.stdout)
        self.assertIsNotNone(report["identity_observation"], report["blockers"])
        if os.geteuid() == 0:
            self.assertEqual(done.returncode, 2)
            self.assertIn("payload_has_root_identity_or_group", report["blockers"])
        self.assertFalse(report["may_start_authentication"])
        self.assertFalse(report["may_start_model_pilot"])
        self.assertEqual(report["cli_execution"], "NOT RUN")
