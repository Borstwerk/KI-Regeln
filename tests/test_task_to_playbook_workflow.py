"""Offline structural contracts for the task-to-playbook WORKFLOW.

Not a model evaluation or a proof of operational correctness.
"""
import json
import re
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "Workflows/Wiederkehrende-Aufgabe-zum-Playbook.md"
TEMPLATE = ROOT / "Workflows/Vorlagen/PLAYBOOK.template.md"
EXAMPLE = ROOT / "Dokumentation/Praxisbeispiele/Task-to-Playbook-Synthetisch.md"
PILOT = ROOT / "Evals/Agentenarbeit/Task-to-Playbook-Pilot"
CASES = PILOT / "cases.json"


def case_errors(cases):
    errors = []
    if len(cases) != 6:
        errors.append("wrong_count")
    ids = [x.get("id") for x in cases]
    if len(set(ids)) != len(ids):
        errors.append("duplicate_id")
    for c in cases:
        id_ = c.get("id", "?")
        if c.get("kind") not in ("positive", "near-miss", "gate", "negative-evidence"):
            errors.append(id_ + ":kind")
        if not isinstance(c.get("task"), str) or not c["task"].strip():
            errors.append(id_ + ":task")
        for field in ("expected", "forbidden"):
            v = c.get(field)
            if not isinstance(v, list) or not v or not all(isinstance(x, str) and x.strip() for x in v):
                errors.append(id_ + ":" + field)
    return errors


class TaskToPlaybookContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = WORKFLOW.read_text(encoding="utf-8")
        cls.template = TEMPLATE.read_text(encoding="utf-8")
        cls.example = EXAMPLE.read_text(encoding="utf-8")
        cls.pilot = (PILOT / "README.md").read_text(encoding="utf-8")
        cls.meta = json.loads(CASES.read_text(encoding="utf-8"))

    def test_workflow_discoverable_but_not_new_skill(self):
        registry = yaml.safe_load((ROOT / "workflow-index.yml").read_text(encoding="utf-8"))
        self.assertEqual(registry["workflows"].count("Workflows/Wiederkehrende-Aufgabe-zum-Playbook.md"), 1)
        catalog = (ROOT / "skill-catalog.yml").read_text(encoding="utf-8")
        self.assertNotIn("id: task-to-playbook,", catalog)
        self.assertNotIn("id: delegations-loop,", catalog)
        overlay = (ROOT / "routing-overlays.yml").read_text(encoding="utf-8")
        self.assertNotIn("task-to-playbook", overlay)

    def test_workflow_preserves_existing_skill_owners_and_gates(self):
        for name in ("requirements-elicitation", "delegation-contract",
                     "verification-loop", "skill-authoring",
                     "search before create", "NOT RUN",
                     "Human Gate", "STOP", "keine Mindestzahl"):
            self.assertIn(name.lower(), self.text.lower())
        self.assertIn("keine Execute-/Netz-/Produktivrechte", self.text)
        self.assertIn("unkontrolliert in jede Session", self.text)
        self.assertIn("keine", self.text.lower())

    def test_template_has_explicit_contract_and_no_fake_pass(self):
        for section in ("Wann nutzen", "Nicht nutzen", "Eingaben", "Rechte",
                        "Entscheidungen", "Toolbox", "Fertig heißt",
                        "Sonderfälle", "Pflege und Herkunft"):
            # 'Inputs' appears as a column, not a header.
            self.assertIn(section, self.template)
        self.assertGreaterEqual(self.template.count("NOT RUN"), 3)
        self.assertIn("Human Gate", self.template)

    def test_synthetic_example_does_not_claim_real_execution(self):
        self.assertIn("synthetisch", self.example.lower())
        self.assertIn("NOT RUN", self.example)
        self.assertIn("Near-Miss", self.example)
        self.assertIn("STOP", self.example)
        self.assertIn("Keine Nachricht verschickt", self.example)

    def test_relative_workflow_markdown_links_resolve(self):
        for link in re.findall(r"\]\(([^)]+\.md)\)", self.text):
            self.assertTrue((WORKFLOW.parent / link).resolve().is_file(), link)
        for link in re.findall(r"\]\(([^)]+\.md)\)", self.pilot):
            self.assertTrue(((PILOT / "README.md").parent / link).resolve().is_file(), link)

    def test_six_positive_negative_fixtures_and_report_status(self):
        self.assertEqual(self.meta["schema_version"], 1)
        self.assertEqual(self.meta["pilot"], "PB-01")
        self.assertEqual(self.meta["status"], "PLANNED_NOT_RUN")
        self.assertEqual(case_errors(self.meta["cases"]), [])
        self.assertEqual(sum(c["kind"] == "positive" for c in self.meta["cases"]), 3)
        self.assertEqual(sum(c["kind"] != "positive" for c in self.meta["cases"]), 3)
        self.assertIn("NOT RUN", self.pilot)
        self.assertIn("Judge-only", self.pilot)

    def test_validator_negative_controls_work(self):
        cases = self.meta["cases"]
        self.assertIn("wrong_count", case_errors(cases[:5]))
        self.assertIn("duplicate_id", case_errors(cases[:5] + [cases[0]]))
        broken = [dict(x) for x in cases]
        broken[0]["expected"] = []
        self.assertIn("PB-01:expected", case_errors(broken))


if __name__ == "__main__":
    unittest.main()
