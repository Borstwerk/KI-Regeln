"""Deterministic structural checks for a candidate prompt-artifact skill.

These checks validate files, contracts and synthetic fixtures. They do NOT
measure the model's prompt quality, natural triggering or downstream outcomes.
"""
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "Arbeitsweisen/Skills/prompt-engineering"
SKILL = BASE / "SKILL.md"
EVAL = ROOT / "Evals/Arbeitsweisen/Prompt-Engineering-Pilot"
CASES = EVAL / "cases.json"
ADAPTERS = ("agentic-code.md", "chat-research.md", "creative-media.md")
OPERATIONS = {"create", "improve", "adapt", "decompile", "split", "review"}


def check_cases(records):
    """Return violations, not a meaningless pass count."""
    errors = []
    if len(records) != 6:
        errors.append("case_count")
    ids = [c.get("case_id") for c in records]
    if len(ids) != len(set(ids)):
        errors.append("duplicate_ids")
    for case in records:
        cid = case.get("case_id", "<unknown>")
        if case.get("mode") not in OPERATIONS | {"none"}:
            errors.append(f"{cid}:mode")
        if case.get("kind") not in {"positive", "negative-near-miss", "negative-missing-input"}:
            errors.append(f"{cid}:kind")
        for field in ("user_request", "route", "target"):
            if not isinstance(case.get(field), str) or not case[field].strip():
                errors.append(f"{cid}:{field}")
        for field in ("expected", "forbidden"):
            entries = case.get(field)
            if not isinstance(entries, list) or not entries or not all(isinstance(x, str) and x.strip() for x in entries):
                errors.append(f"{cid}:{field}")
    return errors


class PromptEngineeringPilotStaticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.bundle = json.loads(CASES.read_text(encoding="utf-8"))
        cls.cases = cls.bundle["cases"]

    def test_skill_is_registered_at_experimental_maturity(self):
        registry = (ROOT / "skill-catalog.yml").read_text(encoding="utf-8")
        self.assertIn("id: prompt-engineering, area: Arbeitsweisen", registry)
        self.assertIn("path: Arbeitsweisen/Skills/prompt-engineering/SKILL.md, maturity: experimental", registry)
        self.assertIn("name: prompt-engineering", self.skill)
        self.assertIn("description:", self.skill)
        self.assertNotIn("prompt-engineering\n", (ROOT / "routing-overlays.yml").read_text(encoding="utf-8"))

    def test_all_optional_adapters_are_reachable(self):
        for name in ADAPTERS:
            self.assertTrue((BASE / "references" / name).is_file(), name)
            self.assertIn(f"references/{name}", self.skill)
        self.assertIn("prompt-engineering", (EVAL / "README.md").read_text(encoding="utf-8").lower())

    def test_skill_has_a_separate_purpose_and_near_misses(self):
        self.assertIn("Near-Misses", self.skill)
        for marker in ("direkt", "skill-authoring", "delegation-contract",
                       "context-engineering", "nicht", "UNVERIFIED"):
            self.assertIn(marker, self.skill)
        for operation in OPERATIONS:
            self.assertIn("`" + operation + "`", self.skill)

    def test_six_synthetic_cases_complete(self):
        self.assertEqual(self.bundle["schema_version"], 1)
        self.assertEqual(check_cases(self.cases), [])
        self.assertEqual(len([c for c in self.cases if c["kind"] == "positive"]), 4)
        self.assertEqual(len([c for c in self.cases if c["kind"].startswith("negative")]), 2)

    def test_expected_safety_and_tool_adaptation_coverage(self):
        joined = " ".join(str(x) for x in self.cases).lower()
        for term in ("codex", "claude code", "read-only", "freigabe", ".env", "referenzbild", "sql"):
            self.assertIn(term, joined)
        for case in self.cases:
            if case["kind"] == "positive":
                self.assertEqual(case["route"], "prompt-engineering")
        near_miss = next(c for c in self.cases if c["kind"] == "negative-near-miss")
        self.assertEqual(near_miss["route"], "domain-task")

    def test_negative_control_proves_case_validator_can_fail(self):
        self.assertIn("case_count", check_cases(self.cases[:5]))
        self.assertIn("duplicate_ids", check_cases(self.cases[:5] + [self.cases[0]]))
        damaged = [dict(c) for c in self.cases]
        damaged[0]["expected"] = []
        self.assertIn("PM-01:expected", check_cases(damaged))

    def test_no_model_outcome_claim_is_hidden_in_evals(self):
        report = (EVAL / "README.md").read_text(encoding="utf-8")
        self.assertIn("NOT RUN", report)
        self.assertIn("UNVERIFIED", report)
        self.assertIn("Kontrollvergleich", report)
        self.assertIn("evaluator-only", report)


if __name__ == "__main__":
    unittest.main()
