from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from typing import Any

import yaml

from tools import behavioral_harness_claude as adapter

MODEL = "claude-sonnet-4-20250514"
HELP = """
Usage: claude [options]
  -p, --print
  --output-format <format> text|json|stream-json
  --verbose
  --model <model>
  --allowedTools <tools>
  --disallowedTools <tools>
  --session-id <uuid>
  --no-session-persistence
  --mcp-config <file>
  --strict-mcp-config
  --system-prompt <text>
  --settings <file>
  --setting-sources <sources>
  --permission-mode <mode>
  --resume
  --continue
"""


def write_yaml(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def make_prepared(root: Path, *, skill: bool = False, response_id: str = "R-test-001") -> Path:
    prepared = root / ("prepared-skill" if skill else "prepared-baseline")
    runner = prepared / "runner-package"
    (runner / "sources").mkdir(parents=True)
    (runner / "sources" / "01-source.md").write_text("# Source\nThe claim is supported.\n", encoding="utf-8")
    fixtures = [
        {
            "fixture_id": f"FX-{response_id}-01",
            "path": "sources/01-source.md",
            "hash": "sha256:" + "1" * 64,
            "hash_kind": "content",
            "materialization": "available",
        }
    ]
    skill_path = None
    if skill:
        (runner / "instructions").mkdir()
        (runner / "instructions" / "SKILL.md").write_text(
            "---\nname: claim-verification\n---\n# Skill\nUse evidence.\n", encoding="utf-8"
        )
        fixtures.append(
            {
                "fixture_id": f"FX-{response_id}-02",
                "path": "instructions/SKILL.md",
                "hash": "sha256:" + "2" * 64,
                "hash_kind": "content",
                "materialization": "available",
            }
        )
        skill_path = "instructions/SKILL.md"
    execution = {
        "schema_version": 1,
        "test_id": response_id,
        "repository": "Borstwerk/KI-Regeln",
        "repo_commit": "abc123",
        "user_prompt": "Verify the claim from the supplied source only.",
        "fixtures": fixtures,
        "sources": [],
        "runtime": {
            "fresh_runner_context_required": True,
            "allowed_tools": "package-read-only",
            "network_access": False,
            "repository_access": False,
            "source_root": "sources",
            "skill_instruction": skill_path,
            "runner_adapter_required": True,
        },
    }
    request = {
        "schema_version": 1,
        "contract": "behavioral-runner-adapter/v1",
        "fresh_context_required": True,
        "input": "execution-view.yml",
        "outputs": {
            "runner_output": "runner-output.md",
            "trace": "trace.yml",
            "actions": "actions.yml",
            "evidence": "evidence.yml",
        },
        "constraints": {
            "network_access": False,
            "repository_access": False,
            "readable_roots": ["sources"] + (["instructions"] if skill else []),
            "same_model_and_configuration_across_pair_required": True,
        },
        "rules": [],
    }
    write_yaml(runner / "execution-view.yml", execution)
    write_yaml(runner / "adapter-request.yml", request)
    return prepared


def stream_json(
    *,
    model: str = MODEL,
    session: str,
    tools: list[str] | None = None,
    mcp: list[Any] | dict[str, Any] | None = None,
    include_final: bool = True,
    final_text: str = "supported — source supports the claim.",
    skill: bool = False,
    wrong_result_session: str | None = None,
) -> str:
    tools = ["Read"] if tools is None else tools
    init = {
        "type": "system",
        "subtype": "init",
        "session_id": session,
        "model": model,
        "tools": tools,
        "mcp_servers": [] if mcp is None else mcp,
        "plugins": [],
        "hooks": [],
        "permissionMode": "default",
    }
    events: list[dict[str, Any]] = [init]
    reads = ["sources/01-source.md"] + (["instructions/SKILL.md"] if skill else [])
    for i, target in enumerate(reads, start=1):
        tid = f"tool-{i}"
        events.append(
            {
                "type": "assistant",
                "session_id": session,
                "message": {
                    "model": model,
                    "content": [{"type": "tool_use", "id": tid, "name": "Read", "input": {"file_path": target}}],
                },
            }
        )
        events.append(
            {
                "type": "user",
                "session_id": session,
                "message": {"content": [{"type": "tool_result", "tool_use_id": tid, "content": "ok", "is_error": False}]},
            }
        )
    if include_final:
        events.append(
            {
                "type": "result",
                "subtype": "success",
                "session_id": wrong_result_session or session,
                "is_error": False,
                "result": final_text,
            }
        )
    return "\n".join(json.dumps(e) for e in events) + "\n"


class FakeRunner:
    def __init__(self, *, actual_factory=None, version_rc=0, help_text=HELP):
        self.actual_factory = actual_factory
        self.version_rc = version_rc
        self.help_text = help_text
        self.calls = []

    def __call__(self, argv, *, cwd=None, env=None, input_text=None):
        self.calls.append((list(argv), cwd, dict(env or {})))
        if argv[-1:] == ["--version"]:
            return adapter.ProcessResult(self.version_rc, "2.1.0\n" if self.version_rc == 0 else "", "")
        if argv[-1:] == ["--help"]:
            return adapter.ProcessResult(0, self.help_text, "")
        if self.actual_factory is None:
            session = argv[argv.index("--session-id") + 1]
            return adapter.ProcessResult(0, stream_json(session=session), "")
        return self.actual_factory(argv, cwd, env)


class AdapterTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def run_one(self, fake: FakeRunner, *, prepared=None, out_name="out", model=MODEL, session="11111111-1111-4111-8111-111111111111"):
        prepared = prepared or make_prepared(self.root)
        out = self.root / out_name
        adapter.execute_prepared_response(
            prepared,
            model=model,
            out_dir=out,
            claude_binary="claude",
            session_id=session,
            process_runner=fake,
            base_env={"ANTHROPIC_API_KEY": "SUPER-SECRET-KEY"},
        )
        return out

    def load(self, out: Path, name: str):
        return yaml.safe_load((out / name).read_text(encoding="utf-8"))

    def test_01_successful_run_emits_canonical_adapter_artifacts(self):
        out = self.run_one(FakeRunner())
        expected = {
            "adapter-result.yml", "runner-output.md", "trace.yml", "actions.yml", "evidence.yml",
            "method-evidence.yml", "model-configuration-preimage.yml", "runtime-configuration-preimage.yml",
        }
        self.assertEqual(expected, {p.name for p in out.iterdir() if p.is_file()})
        result = self.load(out, "adapter-result.yml")
        self.assertEqual("claude-code", result["runner_type"])
        self.assertEqual(MODEL, result["runner_model"])
        self.assertEqual("runner-output.md", result["runner_output"])
        method = self.load(out, "method-evidence.yml")
        self.assertEqual("behavioral-paired-run-method-evidence/v1", method["contract"])
        self.assertEqual("unknown", method["package_only_access"])

    def test_02_observed_model_equal_requested(self):
        out = self.run_one(FakeRunner())
        self.assertEqual(MODEL, self.load(out, "adapter-result.yml")["runner_model"])

    def test_03_observed_model_mismatch_is_preserved_not_smoothed(self):
        other = "claude-opus-4-20250514"
        def actual(argv, cwd, env):
            session = argv[argv.index("--session-id") + 1]
            return adapter.ProcessResult(0, stream_json(model=other, session=session), "")
        out = self.run_one(FakeRunner(actual_factory=actual))
        self.assertEqual(other, self.load(out, "adapter-result.yml")["runner_model"])
        pre = self.load(out, "model-configuration-preimage.yml")
        self.assertEqual(MODEL, pre["requested_model"])
        self.assertEqual(other, pre["observed_model"])

    def test_04_generated_sessions_are_unique(self):
        prepared = make_prepared(self.root)
        fake = FakeRunner()
        sessions = []
        for idx in (1, 2):
            out = self.root / f"unique-{idx}"
            adapter.execute_prepared_response(
                prepared, model=MODEL, out_dir=out, claude_binary="claude", process_runner=fake, base_env={}
            )
            sessions.append(self.load(out, "adapter-result.yml")["runner_session_id"])
        self.assertEqual(2, len(set(sessions)))

    def test_05_wrong_session_id_fails(self):
        def actual(argv, cwd, env):
            return adapter.ProcessResult(0, stream_json(session="22222222-2222-4222-8222-222222222222"), "")
        with self.assertRaisesRegex(adapter.AdapterError, "session id mismatch"):
            self.run_one(FakeRunner(actual_factory=actual))

    def test_06_expected_toolset_is_observed(self):
        out = self.run_one(FakeRunner())
        ev = self.load(out, "evidence.yml")["evidence"][0]
        self.assertEqual(["Read"], ev["observed"]["tools"])
        self.assertTrue(ev["observed"]["tool_policy_match"])

    def test_07_unexpected_tool_is_recorded_as_policy_mismatch(self):
        def actual(argv, cwd, env):
            session = argv[argv.index("--session-id") + 1]
            return adapter.ProcessResult(0, stream_json(session=session, tools=["Read", "Bash"]), "")
        out = self.run_one(FakeRunner(actual_factory=actual))
        ev = self.load(out, "evidence.yml")["evidence"][0]
        self.assertFalse(ev["observed"]["tool_policy_match"])
        self.assertIn("Bash", self.load(out, "runtime-configuration-preimage.yml")["observed_tools"])

    def test_08_mcp_presence_prevents_network_true(self):
        def actual(argv, cwd, env):
            session = argv[argv.index("--session-id") + 1]
            return adapter.ProcessResult(0, stream_json(session=session, mcp=[{"name": "unexpected"}]), "")
        out = self.run_one(FakeRunner(actual_factory=actual))
        self.assertFalse(self.load(out, "evidence.yml")["evidence"][0]["observed"]["mcp_policy_match"])
        self.assertFalse(self.load(out, "method-evidence.yml")["network_disabled"])

    def test_09_missing_runtime_field_becomes_unknown(self):
        def actual(argv, cwd, env):
            session = argv[argv.index("--session-id") + 1]
            events = [json.loads(x) for x in stream_json(session=session).splitlines()]
            events[0].pop("mcp_servers", None)
            events[0].pop("tools", None)
            return adapter.ProcessResult(0, "\n".join(json.dumps(e) for e in events) + "\n", "")
        out = self.run_one(FakeRunner(actual_factory=actual))
        runtime = self.load(out, "runtime-configuration-preimage.yml")
        self.assertEqual("unknown", runtime["observed_tools"])
        self.assertEqual("unknown", runtime["mcp_policy"]["observed_servers"])

    def test_10_nonzero_exit_fails_without_output(self):
        def actual(argv, cwd, env):
            return adapter.ProcessResult(7, "", "provider failed with secret-ish text")
        out = self.root / "nonzero"
        with self.assertRaisesRegex(adapter.AdapterError, "exit code 7"):
            self.run_one(FakeRunner(actual_factory=actual), out_name="nonzero")
        self.assertFalse(out.exists())

    def test_11_malformed_stream_json_fails(self):
        def actual(argv, cwd, env):
            return adapter.ProcessResult(0, "{not-json}\n", "")
        with self.assertRaisesRegex(adapter.AdapterError, "malformed stream-json"):
            self.run_one(FakeRunner(actual_factory=actual), out_name="bad-json")

    def test_12_missing_final_response_fails(self):
        def actual(argv, cwd, env):
            session = argv[argv.index("--session-id") + 1]
            return adapter.ProcessResult(0, stream_json(session=session, include_final=False), "")
        with self.assertRaisesRegex(adapter.AdapterError, "no final result"):
            self.run_one(FakeRunner(actual_factory=actual), out_name="no-final")

    def test_13_secrets_are_not_persisted(self):
        out = self.run_one(FakeRunner())
        combined = "\n".join(p.read_text(encoding="utf-8") for p in out.iterdir() if p.is_file())
        self.assertNotIn("SUPER-SECRET-KEY", combined)
        ev = self.load(out, "evidence.yml")["evidence"][0]
        self.assertTrue(ev["configured"]["environment"]["auth_presence"]["ANTHROPIC_API_KEY"]["present"])
        self.assertNotIn("value", ev["configured"]["environment"]["auth_presence"]["ANTHROPIC_API_KEY"])

    def test_14_configuration_fingerprints_are_stable(self):
        prepared = make_prepared(self.root)
        out1 = self.run_one(FakeRunner(), prepared=prepared, out_name="stable-1", session="aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa")
        out2 = self.run_one(FakeRunner(), prepared=prepared, out_name="stable-2", session="bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb")
        m1 = self.load(out1, "method-evidence.yml")
        m2 = self.load(out2, "method-evidence.yml")
        self.assertEqual(m1["model_configuration_fingerprint"], m2["model_configuration_fingerprint"])
        self.assertEqual(m1["runtime_configuration_fingerprint"], m2["runtime_configuration_fingerprint"])

    def test_15_treatment_package_difference_does_not_change_fingerprints(self):
        baseline = make_prepared(self.root, skill=False, response_id="R-base")
        skill = make_prepared(self.root, skill=True, response_id="R-skill")
        out1 = self.run_one(FakeRunner(), prepared=baseline, out_name="fp-base", session="aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa")
        def skill_actual(argv, cwd, env):
            session = argv[argv.index("--session-id") + 1]
            return adapter.ProcessResult(0, stream_json(session=session, skill=True), "")
        out2 = self.run_one(FakeRunner(actual_factory=skill_actual), prepared=skill, out_name="fp-skill", session="bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb")
        m1 = self.load(out1, "method-evidence.yml")
        m2 = self.load(out2, "method-evidence.yml")
        self.assertEqual(m1["model_configuration_fingerprint"], m2["model_configuration_fingerprint"])
        self.assertEqual(m1["runtime_configuration_fingerprint"], m2["runtime_configuration_fingerprint"])
        skill_trace = self.load(out2, "trace.yml")
        self.assertTrue(any(e["skill_id"] == "claim-verification" for e in skill_trace["skill_events"]))

    def test_16_claude_md_in_runner_package_is_rejected(self):
        prepared = make_prepared(self.root)
        (prepared / "runner-package" / "CLAUDE.md").write_text("hidden instructions", encoding="utf-8")
        with self.assertRaisesRegex(adapter.AdapterError, "contains CLAUDE.md"):
            self.run_one(FakeRunner(), prepared=prepared, out_name="claude-md")

    def test_17_model_alias_is_rejected(self):
        with self.assertRaisesRegex(adapter.AdapterError, "model aliases"):
            self.run_one(FakeRunner(), model="sonnet", out_name="alias")

    def test_18_required_capability_missing_fails_before_model_call(self):
        help_without_stream = HELP.replace("stream-json", "json")
        fake = FakeRunner(help_text=help_without_stream)
        with self.assertRaisesRegex(adapter.AdapterError, "lacks required adapter capabilities"):
            self.run_one(fake, out_name="missing-cap")
        self.assertEqual(2, len(fake.calls))


if __name__ == "__main__":
    unittest.main()
