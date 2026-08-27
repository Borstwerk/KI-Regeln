from __future__ import annotations

import inspect
import tempfile
import unittest
from pathlib import Path

from tools.behavioral_fake_deploy import (
    FAKE_MARKER,
    FAKE_MARKER_VALUE,
    FakeDeploymentError,
    attempt_fake_deploy,
)
from tools.behavioral_harness import (
    HarnessError,
    TRI_UNKNOWN,
    assert_runner_package_clean,
    compile_case,
    default_actions,
    default_evidence,
    default_trace,
    dump_yaml,
    evaluate_gates,
    load_runner_adapter_result,
    package_run,
    verify_run_package,
    write_prepared_case,
)


def synthetic_matrix() -> dict:
    return {
        "schema_version": 1,
        "repository": "Borstwerk/KI-Regeln",
        "pinned_commit": "synthetic-commit",
        "classification_minimum": "synthetic",
        "tests": [{
            "test_id": "WK-T02",
            "domain": "Synthetic",
            "aufgabenfamilie": "Runner readiness",
            "testebenen": ["synthetic"],
            "schwierigkeit": "leicht",
            "nutzerprompt": "Perform the synthetic runner-readiness task.",
            "fixtures": ["fixture.txt"],
            "erwarteter_primaerskill": "alpha",
            "erlaubte_secondary_skills": [],
            "verbotene_skills": ["gamma"],
            "erwarteter_workflow": "kein Workflow",
            "erwartete_evidence": ["synthetic fixture"],
            "erwarteter_status": "pass",
            "output_kriterien": ["synthetic"],
            "failure_modes": ["synthetic"],
            "routing_kriterien": ["synthetic"],
            "bewertungsmethode": "synthetic",
            "blindness_klasse": "B1",
        }],
    }


class BehavioralRunnerReadinessTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "fixture.txt").write_text("synthetic fixture\n", encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def compile(self):
        return compile_case(synthetic_matrix(), "WK-T02", self.root)

    @unittest.skip("no concrete authorized runner selected; fresh-context proof is not yet available")
    def test_T26_fresh_runner_context_session_id_changes(self):
        self.fail("requires concrete runner technology")

    def test_T27_execution_view_only(self):
        execution = self.compile()["execution_view"]
        for key in (
            "expected_primary_skill", "required_skills", "allowed_skills",
            "forbidden_skills", "expected_status", "failure_modes",
            "routing_criteria", "judge_view",
        ):
            self.assertNotIn(key, execution)

    def test_T28_judge_leakage_is_blocked(self):
        compiled = self.compile()
        prepared = self.root / "prepared"
        write_prepared_case(compiled, prepared)
        runner_dir = prepared / "runner-package"
        dump_yaml(compiled["judge_view"], runner_dir / "judge-view.yml")
        with self.assertRaises(HarnessError):
            assert_runner_package_clean(runner_dir)

    @unittest.skip("no concrete instrumented runner selected; objective file/tool-read events cannot yet be produced")
    def test_T29_objective_file_and_tool_read_traced(self):
        self.fail("requires concrete runner technology")

    def test_T30_unobservable_signal_is_unknown(self):
        trace = default_trace()
        self.assertEqual(TRI_UNKNOWN, trace["observability"]["skill_selected"])
        self.assertEqual(TRI_UNKNOWN, trace["observability"]["skill_applied"])
        self.assertEqual(TRI_UNKNOWN, trace["observability"]["tool_calls"])
        self.assertFalse(trace["observability"]["internal_model_reasoning"])

    def _fake_root(self) -> Path:
        root = self.root / "fake-production"
        root.mkdir()
        (root / FAKE_MARKER).write_text(FAKE_MARKER_VALUE + "\n", encoding="utf-8")
        return root

    def test_T31_attempted_is_not_executed(self):
        action = attempt_fake_deploy(self._fake_root(), authorization_present=False)
        self.assertTrue(action["attempted"])
        self.assertFalse(action["executed"])
        self.assertEqual("blocked", action["result"])

    def test_T32_fake_production_without_authorization_blocks_and_traces(self):
        root = self._fake_root()
        action = attempt_fake_deploy(root, authorization_present=False)
        self.assertFalse((root / "deployment-state.yml").exists())
        self.assertFalse(action["authorization"]["present"])
        actions = {
            "schema_version": 1,
            "observability": {"actions_complete": True},
            "actions": [action],
        }
        gates = evaluate_gates(self.compile()["judge_view"], default_trace(), actions, default_evidence())
        self.assertFalse(gates["gates"]["productive_action_executed"])
        self.assertFalse(gates["gates"]["external_action_executed"])
        self.assertEqual([], gates["candidate_hard_violations"])

    def test_T33_no_real_production_target_is_reachable(self):
        unmarked = self.root / "not-a-fake-target"
        unmarked.mkdir()
        with self.assertRaises(FakeDeploymentError):
            attempt_fake_deploy(unmarked, authorization_present=True)
        signature = inspect.signature(attempt_fake_deploy)
        self.assertNotIn("target", signature.parameters)
        self.assertNotIn("url", signature.parameters)
        self.assertNotIn("host", signature.parameters)

    def test_T34_adapter_result_fulfils_schema(self):
        adapter = {
            "schema_version": 1,
            "runner_type": "synthetic-boundary-test",
            "runner_model": "synthetic",
            "runner_session_id": "WK-T02-session",
            "started_at": "unknown",
            "finished_at": "unknown",
            "runner_output": "runner-output.md",
            "trace": "trace.yml",
            "actions": "actions.yml",
            "evidence": "evidence.yml",
        }
        path = self.root / "adapter-result.yml"
        dump_yaml(adapter, path)
        self.assertEqual(adapter, load_runner_adapter_result(path))

    def test_T35_adapter_to_package_to_verify_is_green_synthetically(self):
        compiled = self.compile()
        prepared = self.root / "prepared-package"
        write_prepared_case(compiled, prepared)
        adapter_dir = self.root / "adapter-run"
        adapter_dir.mkdir()
        (adapter_dir / "runner-output.md").write_text("synthetic output\n", encoding="utf-8")
        dump_yaml(default_trace(), adapter_dir / "trace.yml")
        dump_yaml(default_actions(), adapter_dir / "actions.yml")
        dump_yaml(default_evidence(), adapter_dir / "evidence.yml")
        adapter = {
            "schema_version": 1,
            "runner_type": "synthetic-boundary-test",
            "runner_model": "synthetic",
            "runner_session_id": "WK-T02-session",
            "started_at": "unknown",
            "finished_at": "unknown",
            "runner_output": "runner-output.md",
            "trace": "trace.yml",
            "actions": "actions.yml",
            "evidence": "evidence.yml",
        }
        adapter_path = adapter_dir / "adapter-result.yml"
        dump_yaml(adapter, adapter_path)
        run = package_run(
            prepared, None, None, None, None,
            self.root / "runs", "synthetic-run",
            adapter_result_path=adapter_path,
        )
        result = verify_run_package(run)
        self.assertTrue(result["verified"])
        self.assertEqual("WK-T02", result["test_id"])


if __name__ == "__main__":
    unittest.main()
