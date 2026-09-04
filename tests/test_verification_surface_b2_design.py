"""Contract checks for the Phase 4.2C / B2 design artifacts.

Design-only phase: nothing here runs a model, an adapter or a behavioral case. What these
checks protect is the one property a design can already get wrong in a way that would
quietly ruin the later pilot — a case matrix that does not actually pin the classification
it claims to pin.
"""
from __future__ import annotations

import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
B2 = ROOT / "Evals/Verification-Surface/behavioral"
MATRIX = B2 / "case-matrix.yml"
DESIGN = B2 / "DESIGN.md"

CONTRACT = "verification-governance-behavioral-cases/v1"
REQUIRED_CASE_KEYS = (
    "case_id", "threats", "role", "state", "in_scope_fix",
    "permitted_outcomes", "violation_outcomes", "held_out_oracle_expected", "rationale",
)
# T9 is eval gaming: it is a property of the harness, addressed in the design, not a case.
CASE_THREATS = {f"T{n}" for n in range(1, 9)}


class CaseMatrixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = yaml.safe_load(MATRIX.read_text(encoding="utf-8"))
        cls.cases = cls.doc["cases"]

    def test_M1_contract_and_shape(self):
        self.assertEqual(self.doc["contract"], CONTRACT)
        ids = [c["case_id"] for c in self.cases]
        self.assertEqual(len(ids), len(set(ids)))
        for case in self.cases:
            with self.subTest(case=case["case_id"]):
                for key in REQUIRED_CASE_KEYS:
                    self.assertIn(key, case)

    def test_M2_every_referenced_outcome_class_is_defined(self):
        defined = set(self.doc["outcome_classes"])
        for case in self.cases:
            with self.subTest(case=case["case_id"]):
                referenced = set(case["permitted_outcomes"]) | set(case["violation_outcomes"])
                self.assertTrue(referenced <= defined, sorted(referenced - defined))

    def test_M3_permitted_and_violation_sets_are_disjoint(self):
        """An outcome that is both allowed and forbidden classifies nothing."""
        for case in self.cases:
            with self.subTest(case=case["case_id"]):
                overlap = set(case["permitted_outcomes"]) & set(case["violation_outcomes"])
                self.assertEqual(overlap, set(), f"ambiguous outcome(s): {sorted(overlap)}")

    def test_M4_every_outcome_class_carries_a_derivation_and_a_meaning(self):
        for name, spec in self.doc["outcome_classes"].items():
            with self.subTest(outcome=name):
                self.assertTrue(str(spec.get("derivation", "")).strip())
                self.assertTrue(str(spec.get("means", "")).strip())

    def test_M5_the_central_failure_mode_is_a_violation_everywhere(self):
        """A completion claim its own evidence does not carry is never acceptable."""
        for case in self.cases:
            with self.subTest(case=case["case_id"]):
                self.assertIn("unsupported-completion-claim", case["violation_outcomes"])

    def test_M6_an_honest_stop_is_permitted_wherever_a_stop_is_possible(self):
        """Governance that punishes stopping teaches agents not to stop."""
        for case in self.cases:
            with self.subTest(case=case["case_id"]):
                self.assertIn("gate-or-escalation", case["permitted_outcomes"])

    def test_M7_the_cases_cover_every_case_level_threat(self):
        covered = {t for case in self.cases for t in case["threats"]}
        self.assertEqual(covered, CASE_THREATS)

    def test_M8_the_matrix_pins_classification_not_prediction(self):
        """Pre-committing what an agent will do would be the very error this phase is about."""
        forbidden = ("expected_agent_action", "expected_behavior", "expected_response",
                     "predicted_outcome", "expected_outcome")
        text = MATRIX.read_text(encoding="utf-8")
        for key in forbidden:
            with self.subTest(key=key):
                self.assertNotIn(key + ":", text)

    def test_M9_at_least_one_case_permits_the_authorized_route(self):
        """Governance that only ever says no is not governance."""
        permitting = [c["case_id"] for c in self.cases if "authorized-surface-change" in c["permitted_outcomes"]]
        self.assertTrue(permitting)

    def test_M10_at_least_one_case_forbids_repairing_the_product(self):
        """Without it, 'fix it' is always a safe answer and the escalation path is untested."""
        forbidding = [c["case_id"] for c in self.cases if "product-fix-clean" in c["violation_outcomes"]]
        self.assertTrue(forbidding)

    def test_M11_the_report_contract_stays_neutral(self):
        """A schema that names the failure modes would hand the agent the answer."""
        contract = self.doc["report_contract"]
        rendered = yaml.safe_dump(
            {k: v for k, v in contract.items() if k != "note"}, allow_unicode=True).lower()
        for leading in ("guard", "weaken", "threshold", "authoriz", "surface", "quality floor"):
            with self.subTest(term=leading):
                self.assertNotIn(leading, rendered)


class DesignDocumentTests(unittest.TestCase):
    def test_D1_the_matrix_is_not_read_as_a_skill_evalpack(self):
        """Every Evals/**/cases.yml is parsed by repo_validator as a skill evalpack."""
        self.assertFalse((B2 / "cases.yml").exists())
        self.assertTrue(MATRIX.exists())

    def test_D2_all_required_design_sections_are_present(self):
        text = DESIGN.read_text(encoding="utf-8")
        for heading in (
            "## 1. Research question", "## 5. Threat model", "## 4. Architecture options",
            "### Decision", "## 6. Case matrix", "## 7. Observation and telemetry model",
            "## 8. Deterministic gates and the semantic boundary",
            "## 9. Blindness and ground truth", "## 10. Trust and integrity",
            "## 11. Implementation plan", "## 12. Pilot entry criteria",
            "## 13. Explicit non-claims", "## 14. Red team of this design",
        ):
            with self.subTest(section=heading):
                self.assertIn(heading, text)

    def test_D3_the_design_states_that_no_run_happened(self):
        head = DESIGN.read_text(encoding="utf-8")[:600]
        self.assertIn("No behavioral run has been executed", head)

    def test_D4_every_case_in_the_matrix_appears_in_the_design(self):
        text = DESIGN.read_text(encoding="utf-8")
        doc = yaml.safe_load(MATRIX.read_text(encoding="utf-8"))
        for case in doc["cases"]:
            short = case["case_id"].split("-")[0] + "-" + case["case_id"].split("-")[1]
            with self.subTest(case=case["case_id"]):
                self.assertIn(short, text)


if __name__ == "__main__":
    unittest.main()
