"""Portable negative controls for B2 admission; no CLI, credentials or model calls.

These scripted process results test the policy reader, not runtime enforcement.
The original real-view and installed-runtime tests remain in the B2 suite.
"""
import json
import unittest
from pathlib import Path

from tools.b2_launch_preflight import (
    MANAGED_SETTINGS_PATHS, MANAGED_VERDICT_CLEAR, MANAGED_VERDICT_UNKNOWN,
    MANAGED_VERDICT_PROVIDER, managed_credential_provider,
)
from tools import behavioral_harness_claude as adapter


class ManagedPolicyReadIntegrityTests(unittest.TestCase):
    def read(self, listing, *, rc=0, started=True, timed_out=False, doctor_rc=0,
             stderr=""):
        def run(argv, view_timeout=None):
            policy = argv[0] == "/bin/sh"
            return {
                "returncode": rc if policy else doctor_rc,
                "stdout": listing if policy else
                    "Managed settings (remote): none configured for this organization\n",
                "stderr": stderr, "payload_started": started, "timed_out": timed_out,
            }
        return managed_credential_provider(run, "unused-scripted-cli")

    @staticmethod
    def complete():
        return "\n".join(f"=== {p}\n@ABSENT" for p in MANAGED_SETTINGS_PATHS) + "\n=== end\n"

    def test_complete_successful_absence_is_accepted(self):
        self.assertEqual(self.read(self.complete())["verdict"], MANAGED_VERDICT_CLEAR)

    def test_incomplete_output_never_proves_absence(self):
        for listing in ("", "=== end\n", f"=== {MANAGED_SETTINGS_PATHS[-1]}\n@ABSENT\n=== end\n",
                        self.complete().removesuffix("=== end\n"), self.complete() + "x" * 2100):
            with self.subTest(listing=listing[:60]):
                self.assertEqual(self.read(listing)["verdict"], MANAGED_VERDICT_UNKNOWN)

    def test_failed_or_incomplete_process_never_proves_absence(self):
        for overrides in ({"rc": 1}, {"started": False}, {"timed_out": True}, {"doctor_rc": 1}):
            with self.subTest(overrides=overrides):
                self.assertEqual(self.read(self.complete(), **overrides)["verdict"],
                                 MANAGED_VERDICT_UNKNOWN)

    def test_empty_file_is_unknown_rather_than_absent(self):
        listing = self.complete().replace("@ABSENT", "", 1)
        self.assertEqual(self.read(listing)["verdict"], MANAGED_VERDICT_UNKNOWN)

    def test_policy_diagnostics_do_not_persist_values(self):
        secret = "B2-SYNTHETIC-HELPER-SECRET"
        report = self.read(self.complete(), stderr=secret)
        self.assertNotIn(secret, json.dumps(report))

    def test_managed_oauth_override_is_not_mistaken_for_the_supplied_token(self):
        for name in (adapter.SUBSCRIPTION_OAUTH_ENV, *adapter.HOST_ONLY_AUTH_ENV):
            with self.subTest(channel=name):
                document = json.dumps({"env": {name: "B2-SYNTHETIC-POLICY-OVERRIDE"}})
                report = self.read(self.complete().replace("@ABSENT", document, 1))
                self.assertEqual(report["verdict"], MANAGED_VERDICT_PROVIDER)
                self.assertIn(f"env.{name}", report["credential_provider_keys"])
                self.assertNotIn("B2-SYNTHETIC-POLICY-OVERRIDE", json.dumps(report))


class AuthEnvironmentScopeTests(unittest.TestCase):
    def test_read_only_does_not_inherit_the_b2_subscription_token(self):
        name = adapter.SUBSCRIPTION_OAUTH_ENV
        env, policy = adapter._child_env({name: "B2-SYNTHETIC-TOKEN"}, Path("unused-config"))
        self.assertNotIn(name, env)
        self.assertIn(name, policy["removed_agent_names"])

    def test_writable_opt_in_inherits_only_the_named_token(self):
        name = adapter.SUBSCRIPTION_OAUTH_ENV
        raw = {name: "B2-SYNTHETIC-TOKEN", "CLAUDE_CODE_OAUTH_TOKEN_FILE": "/host/token"}
        env, policy = adapter._child_env(raw, Path("unused-config"), adapter.B2_CONTROL_ENV,
                                         allow_subscription_oauth=True)
        self.assertEqual(env[name], raw[name])
        self.assertNotIn("CLAUDE_CODE_OAUTH_TOKEN_FILE", env)
        self.assertEqual(env[adapter.SUBPROCESS_SCRUB_ENV], "1")
        self.assertNotIn(raw[name], json.dumps(policy))


class AuthProbeEvidenceTests(unittest.TestCase):
    def test_raw_auth_diagnostics_and_extra_fields_are_not_persisted(self):
        from tools.b2_launch_preflight import _auth_probe
        secret = "B2-SYNTHETIC-AUTH-DIAGNOSTIC"

        def run(argv, view_timeout=None):
            return {"returncode": 0, "stdout": json.dumps({
                "loggedIn": True, "authMethod": "oauth_token", "token": secret,
            }), "stderr": secret, "payload_started": True, "timed_out": False}

        probe = _auth_probe(run, "unused-scripted-cli")
        self.assertTrue(probe["accepted"])
        self.assertNotIn(secret, json.dumps(probe))


if __name__ == "__main__":
    unittest.main()
