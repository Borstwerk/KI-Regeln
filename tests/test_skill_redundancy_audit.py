import tempfile
import unittest
from pathlib import Path

from tools.skill_redundancy_audit import audit, instruction_blocks


REPEATED = (
    "Prüfe zuerst die tatsächliche Quelle und trenne Beobachtung von Hypothese, "
    "bevor du einen Fix vorschlägst. Behaupte niemals einen ausgeführten Test, "
    "dessen Ergebnis nicht im Run nachgewiesen wurde."
)


class SkillRedundancyAuditTests(unittest.TestCase):
    def test_reports_cross_skill_repeats_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for area in ("alpha", "beta"):
                path = root / area / "Skills" / "example" / "SKILL.md"
                path.parent.mkdir(parents=True)
                path.write_text(
                    "---\nname: example\ndescription: test\n---\n\n"
                    + REPEATED + "\n",
                    encoding="utf-8",
                )
            report = audit(root, minimum_words=18)
            self.assertEqual("CANDIDATES_ONLY", report["status"])
            self.assertEqual(2, report["skill_files"])
            self.assertEqual(1, report["duplicate_groups_found"])
            self.assertEqual(2, len(report["groups"][0]["locations"]))

    def test_does_not_report_single_file_or_short_duplicated_phrase(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            p = root / "a" / "SKILL.md"
            p.parent.mkdir()
            p.write_text("Prüfe den Kontext.\n\nPrüfe den Kontext.\n", encoding="utf-8")
            report = audit(root)
            self.assertEqual(0, report["duplicate_groups_found"])

    def test_fenced_code_and_frontmatter_are_not_instruction_blocks(self):
        text = (
            "---\nname: sample\ndescription: repeated repeated repeated repeated\n---\n"
            "```text\n" + REPEATED + "\n```\n"
        )
        self.assertEqual([], instruction_blocks(text, minimum_words=18))

    def test_not_a_semantic_quality_or_token_savings_claim(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = audit(Path(tmp))
            self.assertEqual(0, report["skill_files"])
            self.assertTrue(any("not paraphrases" in x for x in report["limitations"]))
            self.assertTrue(any("token use" in x for x in report["limitations"]))


if __name__ == "__main__":
    unittest.main()
