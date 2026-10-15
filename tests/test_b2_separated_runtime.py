"""Portable construction controls; real separation evidence lives in Linux tests."""
import tempfile
import unittest
import os
import errno
import stat
import subprocess
from types import SimpleNamespace
from unittest import mock
from pathlib import Path

from tools.b2_boundary import BoundaryError, ViewSpec, _script
from tools import b2_boundary as boundary
from tools import b2_separated_runtime as separated


class SeparatedViewContractTests(unittest.TestCase):
    def test_invalid_or_root_payload_identity_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            for identity in ((0, 1000), (1000, 0), (True, 1000), (1000,), (1000, -1)):
                with self.subTest(identity=identity), self.assertRaises(BoundaryError):
                    ViewSpec(workspace=Path(tmp), argv=("true",), payload_identity=identity).validate()

    def test_separated_script_drops_groups_caps_and_privilege_gain_before_exec(self):
        with tempfile.TemporaryDirectory() as tmp:
            script = _script(ViewSpec(workspace=Path(tmp), argv=("true",),
                                     payload_identity=(1000, 1000), private_tmp_mountpoint=True))
        for flag in ("--reuid=1000", "--regid=1000", "--clear-groups", "--bounding-set=-all",
                     "--inh-caps=-all", "--ambient-caps=-all", "--no-new-privs"):
            self.assertIn(flag, script)
        self.assertIn('"$R"/tmp', script)
        self.assertNotIn('mount --bind /tmp', script)
        self.assertIn("uid=1000,gid=1000,mode=0700", script)

    def test_classic_script_does_not_acquire_an_implicit_identity_policy(self):
        with tempfile.TemporaryDirectory() as tmp:
            script = _script(ViewSpec(workspace=Path(tmp), argv=("true",)))
        self.assertNotIn("setpriv", script)
        self.assertNotIn('"$R"/tmp', script)


class SeparatedCredentialGateTests(unittest.TestCase):
    def test_no_credential_bearing_separated_builder_is_enabled(self):
        from tools import b2_separated_runtime as separated
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.dict(os.environ, {"CLAUDE_CODE_OAUTH_TOKEN": "synthetic-sensitive"}, clear=True):
                with mock.patch.object(separated, "require_tools", side_effect=AssertionError("must stop first")):
                    with self.assertRaisesRegex(separated.SeparationError, "credential_free_runtime_required"):
                        with separated.separated_model_invocation(["unused"], task_root=Path(tmp),
                                                                 workspace=Path(tmp), env={}):
                            self.fail("credential-bearing view was admitted")

    def test_supplied_credentials_cannot_enter_an_otherwise_clean_runtime(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.dict(os.environ, {}, clear=True):
            with mock.patch.object(separated, "require_tools", side_effect=AssertionError("must stop first")):
                with self.assertRaisesRegex(separated.SeparationError, "credential_free_runtime_required"):
                    with separated.separated_model_invocation(["unused"], task_root=Path(tmp), workspace=Path(tmp),
                                                             env={"ANTHROPIC_API_KEY": "synthetic-sensitive"}):
                        self.fail("explicit credential was admitted")


class RuntimeToolControlsTests(unittest.TestCase):
    def check_tool(self, mode, *, owner=0, capability=None):
        info = SimpleNamespace(st_mode=mode, st_uid=owner)
        absent = OSError(errno.ENODATA, "no capability")
        with mock.patch.object(separated.sys, "platform", "linux"), mock.patch.object(
                separated.os, "geteuid", return_value=0, create=True), mock.patch.object(
                Path, "stat", return_value=info), mock.patch.object(
                separated.os, "getxattr", side_effect=capability if isinstance(capability, Exception) else
                absent if capability is None else None, return_value=capability, create=True):
            separated.require_tools()

    def test_only_root_owned_regular_nonprivileged_tools_are_accepted(self):
        self.check_tool(stat.S_IFREG | 0o755)
        for mode, owner, capability in ((stat.S_IFREG | 0o4755, 0, None),
                                       (stat.S_IFREG | 0o775, 0, None),
                                       (stat.S_IFREG | 0o755, 1000, None),
                                       (stat.S_IFREG | 0o755, 0, b"capability"),
                                       (stat.S_IFREG | 0o755, 0, OSError(errno.EACCES, "unknown"))):
            with self.subTest(mode=mode, owner=owner, capability=capability):
                with self.assertRaises(separated.SeparationError):
                    self.check_tool(mode, owner=owner, capability=capability)


class NestedBoundaryControlsTests(unittest.TestCase):
    def status(self):
        return {"Uid": "1000 1000 1000 1000", "Gid": "1000 1000 1000 1000",
                "CapInh": "0", "CapPrm": "0", "CapEff": "0", "CapAmb": "0", "NoNewPrivs": "1"}

    def argv_for(self, fields):
        with mock.patch.object(boundary.os, "getuid", return_value=1000, create=True), mock.patch.object(
                boundary.os, "getgid", return_value=1000, create=True), mock.patch.object(
                boundary.os, "getgroups", return_value=[], create=True), mock.patch.object(
                Path, "read_text", return_value="\n".join(f"{key}: {value}" for key, value in fields.items())):
            return boundary.unprivileged_check_argv()

    def test_nested_boundary_requires_all_identity_and_capability_fields(self):
        argv = self.argv_for(self.status())
        self.assertIn("--unshare-user", argv)
        self.assertIn("--unshare-net", argv)
        self.assertNotIn("--unshare-user-try", argv)
        for key in self.status():
            for value in (None, "0 1000 1000 1000" if key in ("Uid", "Gid") else
                          "0" if key == "NoNewPrivs" else "1"):
                fields = self.status()
                if value is None: del fields[key]
                else: fields[key] = value
                with self.subTest(key=key, value=value), self.assertRaises(BoundaryError):
                    self.argv_for(fields)

    def test_zero_exit_without_payload_marker_never_counts_as_a_check(self):
        with mock.patch.object(boundary, "unprivileged_check_argv", return_value=["fixed-boundary"]), mock.patch.object(
                boundary.subprocess, "run", return_value=SimpleNamespace(returncode=0, stdout="", stderr="")):
            with self.assertRaisesRegex(BoundaryError, "payload never started"):
                boundary.run_unprivileged_check()

    def test_real_red_payload_is_distinct_from_unavailable_boundary(self):
        with mock.patch.object(boundary, "unprivileged_check_argv", return_value=["fixed-boundary"]), mock.patch.object(
                boundary.subprocess, "run", return_value=SimpleNamespace(
                    returncode=1, stdout="B2-UNPRIVILEGED-CHECK-STARTED\nred product\n", stderr="")):
            result = boundary.run_unprivileged_check()
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "red product\n")
        for error in (FileNotFoundError("no bwrap"), subprocess.TimeoutExpired(["fixed-boundary"], 60)):
            with mock.patch.object(boundary, "unprivileged_check_argv", return_value=["fixed-boundary"]), mock.patch.object(
                    boundary.subprocess, "run", side_effect=error), self.assertRaises(BoundaryError):
                boundary.run_unprivileged_check()
