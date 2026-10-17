"""Static/schema checks for the experimental prompt-engineering cases.

These checks do NOT prove natural skill activation, prompt quality, or downstream
outcome. Model behavior requires a separate controlled A/B run.
"""
from pathlib import Path
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "Arbeitsweisen/Skills/prompt-engineering"
SKILL = BASE / "SKILL.md"
EVAL = ROOT / "Evals/Arbeitsweisen/prompt-engineering"
CASES = EVAL / "cases.yml"
ADAPTERS = ("agentic-code.md", "chat-research.md", "creative-media.md")
FOCUSES = {"create", "improve", "adapt", "decompile", "split", "review",
           "negative-near-miss", "negative-missing-input"}
STATUSES = {"pass", "partial", "blocked"}


def check_cases(records):
    """Return specific failures for positive controls and deliberate breakage."""
    errors = []
    if len(records) != 6:
        errors.append("case_count")
    ids = [c.get("id") for c in records]
    if len(ids) != len(set(ids)):
        errors.append("duplicate_ids")
    for c in records:
        cid = c.get("id", "<unknown>")
        if c.get("focus") not in FOCUSES:
            errors.append(f"{cid}:focus")
        if c.get("class") not in {"behavior", "trigger", "outcome", "regression"}:
            errors.append(f"{cid}:class")
        if not isinstance(c.get("should_trigger"), bool):
            errors.append(f"{cid}:should_trigger")
        if c.get("expected_status") not in STATUSES:
            errors.append(f"{cid}:expected_status")
        if not isinstance(c.get("input"), str) or not c["input"].strip():
            errors.append(f"{cid}:input")
        for field in ("expected", "forbidden"):
            val = c.get(field)
            if not isinstance(val, list) or not val or not all(isinstance(x, str) and x.strip() for x in val):
                errors.append(f"{cid}:{field}")
    return errors


class PromptEngineeringPilotStaticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.bundle = yaml.safe_load(CASES.read_text(encoding="utf-8"))
        cls.cases = cls.bundle["cases"]

    def test_registered_as_experimental_and_not_global_overlay(self):
        catalog = (ROOT / "skill-catalog.yml").read_text(encoding="utf-8")
        self.assertIn("id: prompt-engineering, area: Arbeitsweisen", catalog)
        self.assertIn("path: Arbeitsweisen/Skills/prompt-engineering/SKILL.md, maturity: experimental", catalog)
        self.assertIn("name: prompt-engineering", self.skill)
        self.assertIn("description:", self.skill)
        overlay = (ROOT / "routing-overlays.yml").read_text(encoding="utf-8")
        self.assertNotIn("skill: prompt-engineering", overlay)

    def test_optional_adapters_and_eval_docs_are_linked(self):
        for name in ADAPTERS:
            self.assertTrue((BASE / "references" / name).is_file(), name)
            self.assertIn("references/" + name, self.skill)
        self.assertIn("prompt-engineering", (EVAL / "README.md").read_text(encoding="utf-8").lower())
        self.assertIn("Evals/Arbeitsweisen/prompt-engineering/README.md", self.skill)

    def test_skill_has_explicit_trigger_and_near_misses(self):
        self.assertIn("Near-Misses", self.skill)
        for marker in ("delegation-contract", "context-engineering", "skill-authoring",
                       "UNVERIFIED", "nicht"):
            self.assertIn(marker, self.skill)
        for operation in ("create", "improve", "adapt", "decompile", "split", "review"):
            self.assertIn("`" + operation + "`", self.skill)

    def test_six_native_yaml_cases_are_well_formed(self):
        self.assertEqual(self.bundle["schema_version"], 1)
        self.assertEqual(self.bundle["skill"], "prompt-engineering")
        self.assertEqual(check_cases(self.cases), [])
        self.assertEqual(sum(c["should_trigger"] for c in self.cases), 5)
        self.assertEqual(sum(not c["should_trigger"] for c in self.cases), 1)

    def test_security_and_adapter_cases_present(self):
        joined = " ".join(str(x) for x in self.cases).lower()
        for term in ("codex", "claude code", "read-only", "freigabe", ".env", "referenzbild", "sql"):
            self.assertIn(term, joined)
        near_miss = next(c for c in self.cases if not c["should_trigger"])
        self.assertEqual(near_miss["id"], "PM-05")
        self.assertEqual(near_miss["class"], "trigger")
        self.assertEqual(next(c for c in self.cases if c["id"] == "PM-06")["expected_status"], "partial")

    def test_deliberate_breakage_triggers_expected_guard(self):
        self.assertIn("case_count", check_cases(self.cases[:5]))
        self.assertIn("duplicate_ids", check_cases(self.cases[:5] + [self.cases[0]]))
        damaged = [dict(c) for c in self.cases]
        damaged[0]["expected"] = []
        self.assertIn("PM-01:expected", check_cases(damaged))

    def test_pilot_reports_unverified_model_outcomes(self):
        report = (EVAL / "README.md").read_text(encoding="utf-8")
        self.assertIn("NOT RUN", report)
        self.assertIn("UNVERIFIED", report)
        self.assertIn("Kontrollvergleich", report)
        self.assertIn("evaluator-only", report)


if __name__ == "__main__":
    unittest.main()
