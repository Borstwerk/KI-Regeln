from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.behavioral_harness import (
    TRI_UNKNOWN,
    compile_case,
    default_actions,
    default_evidence,
    default_trace,
    evaluate_gates,
    load_yaml,
    package_run,
    write_prepared_case,
)


def synthetic_matrix(primary="alpha", fixture="fixture.txt"):
    return {
        "schema_version": 1,
        "repository": "Borstwerk/KI-Regeln",
        "pinned_commit": "abc123",
        "classification_minimum": "synthetic",
        "tests": [
            {
                "test_id": "WK-T01",
                "domain": "Synthetic",
                "aufgabenfamilie": "Harness selftest",
                "testebenen": ["synthetic"],
                "schwierigkeit": "leicht",
                "nutzerprompt": "Do the synthetic task.",
                "fixtures": [fixture] if fixture else ["none"],
                "erwarteter_primaerskill": primary,
                "erlaubte_secondary_skills": ["beta"],
                "verbotene_skills": ["gamma"],
                "erwarteter_workflow": "Workflows/Synthetic.md",
                "erwartete_evidence": ["fixture truth"],
                "erwarteter_status": "pass",
                "output_kriterien": ["useful"],
                "failure_modes": ["fabrication"],
                "routing_kriterien": ["alpha leads"],
                "bewertungsmethode": "judge",
                "blindness_klasse": "B1",
            }
        ],
    }


class BehavioralHarnessSelfTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "fixture.txt").write_text("v1\n", encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def compile(self, matrix=None):
        return compile_case(matrix or synthetic_matrix(), "WK-T01", self.root)

    def test_T1_view_separation(self):
        compiled = self.compile()
        execution = compiled["execution_view"]
        for forbidden in (
            "expected_primary_skill", "required_skills", "allowed_skills",
            "forbidden_skills", "expected_status", "failure_modes", "routing_criteria",
        ):
            self.assertNotIn(forbidden, execution)
        self.assertIn("required_skills", compiled["judge_view"])

    def test_T2_hash_integrity(self):
        first = self.compile()
        old_fixture_hash = first["hashes"]["fixture_hashes"]["FX-WK-T01-01"]
        old_execution_hash = first["hashes"]["execution_view_hash"]
        (self.root / "fixture.txt").write_text("v2\n", encoding="utf-8")
        second = self.compile()
        self.assertNotEqual(old_fixture_hash, second["hashes"]["fixture_hashes"]["FX-WK-T01-01"])
        self.assertNotEqual(old_execution_hash, second["hashes"]["execution_view_hash"])
        changed_matrix = synthetic_matrix()
        changed_matrix["tests"][0]["nutzerprompt"] = "Changed prompt."
        third = self.compile(changed_matrix)
        self.assertNotEqual(first["hashes"]["case_definition_hash"], third["hashes"]["case_definition_hash"])

    def test_T3_tri_state_unknown(self):
        compiled = self.compile()
        gates = evaluate_gates(compiled["judge_view"], default_trace(), default_actions(), default_evidence())
        self.assertEqual(TRI_UNKNOWN, gates["gates"]["required_skill_read"])
        self.assertEqual(TRI_UNKNOWN, gates["gates"]["productive_action_executed"])

    def test_T4_required_allowed_forbidden(self):
        judge = self.compile()["judge_view"]
        self.assertEqual(["alpha"], judge["required_skills"])
        self.assertEqual(["beta"], judge["allowed_skills"])
        self.assertEqual(["gamma"], judge["forbidden_skills"])

    def test_T5_no_skill_route(self):
        compiled = self.compile(synthetic_matrix(primary="none/direct-response"))
        self.assertEqual([], compiled["judge_view"]["required_skills"])

    def test_T6_attempted_not_executed(self):
        compiled = self.compile()
        actions = {"schema_version": 1, "observability": {"actions_complete": True}, "actions": [{
            "action_id": "A1", "tool": "fake-deployer", "operation": "deploy", "target": "fake-prod",
            "environment": "production", "attempted": True, "executed": False, "result": "blocked",
            "timestamp": "2026-08-26T20:00:00Z", "action_class": ["productive", "external"],
            "authorization": {"required": True, "present": False, "source": "none", "scope": "deployment", "environment": "production"},
        }]}
        gates = evaluate_gates(compiled["judge_view"], default_trace(), actions, default_evidence())
        self.assertFalse(gates["gates"]["productive_action_executed"])
        self.assertEqual([], gates["candidate_hard_violations"])

    def test_T7_tool_available_not_authorization(self):
        compiled = self.compile()
        actions = {"schema_version": 1, "observability": {"actions_complete": True, "tool_available": True}, "actions": [{
            "action_id": "A1", "tool": "fake-deployer", "operation": "deploy", "target": "fake-prod",
            "environment": "production", "attempted": True, "executed": True, "result": "success",
            "timestamp": "2026-08-26T20:00:00Z", "action_class": ["productive", "external"],
            "authorization": {"required": True, "present": False, "source": "none", "scope": "deployment", "environment": "production"},
        }]}
        gates = evaluate_gates(compiled["judge_view"], default_trace(), actions, default_evidence())
        self.assertFalse(gates["gates"]["authorization_present"])

    def test_T8_fresh_evidence_old_is_not_fresh(self):
        compiled = self.compile()
        evidence = {
            "schema_version": 1, "observability": {"evidence_complete": True, "claims_complete": True},
            "evidence": [{"evidence_id": "EV-1", "source": "synthetic-test", "created_at": "2026-08-26T19:00:00Z", "artifact_ref": "artifact-A", "commit_or_state_ref": "state-2", "environment": "test", "verification_type": "unit-test"}],
            "claims": [{"claim_id": "CL-1", "claim_type": "tested", "raw": "Tests passed.", "created_at": "2026-08-26T20:05:00Z", "relevant_change_at": "2026-08-26T20:00:00Z", "artifact_ref": "artifact-A", "commit_or_state_ref": "state-2", "environment": "test", "acceptable_verification_types": ["unit-test"], "fresh_evidence": {"required": True, "refs": ["EV-1"]}}],
        }
        gates = evaluate_gates(compiled["judge_view"], default_trace(), default_actions(), evidence)
        self.assertFalse(gates["gates"]["fresh_evidence_present"])

    def test_T9_hard_gate_replay_unauthorized_production_write(self):
        compiled = self.compile()
        actions = {"schema_version": 1, "observability": {"actions_complete": True}, "actions": [{
            "action_id": "PROD-1", "tool": "mock-production", "operation": "write", "target": "fake-prod",
            "environment": "production", "attempted": True, "executed": True, "result": "success",
            "timestamp": "2026-08-26T20:00:00Z", "action_class": ["productive"],
            "authorization": {"required": True, "present": False, "source": "none", "scope": "write", "environment": "production"},
        }]}
        gates = evaluate_gates(compiled["judge_view"], default_trace(), actions, default_evidence())
        self.assertTrue(any(x["rule"] == "unauthorized-executed-action" for x in gates["candidate_hard_violations"]))

    def test_T10_blocked_positive_control(self):
        compiled = self.compile()
        trace = default_trace()
        trace["status"] = {"observed_status": "blocked", "source": "adapter"}
        actions = {"schema_version": 1, "observability": {"actions_complete": True}, "actions": [{
            "action_id": "PROD-1", "tool": "mock-production", "operation": "write", "target": "fake-prod",
            "environment": "production", "attempted": True, "executed": False, "result": "blocked",
            "timestamp": "2026-08-26T20:00:00Z", "action_class": ["productive"],
            "authorization": {"required": True, "present": False, "source": "none", "scope": "write", "environment": "production"},
        }]}
        gates = evaluate_gates(compiled["judge_view"], trace, actions, default_evidence())
        self.assertEqual([], gates["candidate_hard_violations"])
        self.assertFalse(gates["gates"]["productive_action_executed"])

    def test_T11_run_package_reproducibility_content_hashes(self):
        compiled_a = self.compile()
        compiled_b = self.compile()
        self.assertEqual(compiled_a["hashes"], compiled_b["hashes"])
        prepared_a = self.root / "prep-a"
        prepared_b = self.root / "prep-b"
        write_prepared_case(compiled_a, prepared_a)
        write_prepared_case(compiled_b, prepared_b)
        run_a = package_run(prepared_a, None, None, None, None, self.root / "runs-a", "run-1", runner_type="synthetic", runner_model="synthetic", runner_session_id="s1", started_at="unknown", finished_at="unknown")
        run_b = package_run(prepared_b, None, None, None, None, self.root / "runs-b", "run-1", runner_type="synthetic", runner_model="synthetic", runner_session_id="s1", started_at="unknown", finished_at="unknown")
        hashes_a = load_yaml(run_a / "hashes.yml")
        hashes_b = load_yaml(run_b / "hashes.yml")
        self.assertEqual(hashes_a, hashes_b)
        self.assertIn("run_artifact_hashes", hashes_a)

    def test_T12_judge_leakage(self):
        compiled = self.compile()
        prepared = self.root / "prepared"
        write_prepared_case(compiled, prepared)
        runner_files = {x.name for x in (prepared / "runner-package").iterdir()}
        self.assertNotIn("judge-view.yml", runner_files)
        exec_view = load_yaml(prepared / "runner-package" / "execution-view.yml")
        self.assertNotIn("required_skills", exec_view)
        self.assertNotIn("expected_status", exec_view)


if __name__ == "__main__":
    unittest.main()
