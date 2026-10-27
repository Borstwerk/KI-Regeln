"""PT-01 offline fixture and negative controls, not evidence of model skill lift."""
import tempfile
import unittest
from pathlib import Path

from tools import pt01_pilot as pt


class PonytailPilotOfflineTests(unittest.TestCase):
    def test_case_inventory_and_separate_development_labels(self):
        bundle = pt.validate()
        self.assertEqual(bundle["pilot"], "PT-01")
        self.assertEqual(len(bundle["cases"]), 8)
        for track in "ABCD":
            self.assertEqual(sum(x["track"] == track for x in bundle["cases"]), 2)
        self.assertTrue(pt.LABELS.is_file())
        self.assertNotEqual(pt.CASES.parent, pt.LABELS.parent)

    def test_prepare_A_and_B_no_oracles_or_unapproved_external_skill(self):
        with tempfile.TemporaryDirectory() as root:
            a = Path(root) / "arm-a"
            b = Path(root) / "arm-b"
            pt.prepare("PT01-B1", "A", a)
            pt.prepare("PT01-B1", "B", b)
            self.assertEqual((a / "app/receipt.py").read_bytes(), (b / "app/receipt.py").read_bytes())
            self.assertFalse((a / "OPTIONAL_CHECKPOINT.md").exists())
            self.assertTrue((b / "OPTIONAL_CHECKPOINT.md").is_file())
            for location in (a, b):
                self.assertFalse((location / "judge-only").exists())
                self.assertFalse((location / "labels.json").exists())
                self.assertNotIn("removed total_cents", (location / "TASK.md").read_text(encoding="utf-8"))
                self.assertIn("FIXTURE_PREPARED_NOT_MODEL_RUN", (location / "manifest.json").read_text(encoding="utf-8"))
            with self.assertRaises(ValueError):
                pt.prepare("PT01-B1", "A", a)
            with self.assertRaises(ValueError):
                pt.prepare("PT01-B1", "C", Path(root) / "blocked")

    def test_review_development_labels_reference_and_negative(self):
        for case in ("PT01-B1", "PT01-B2", "PT01-C1", "PT01-C2", "PT01-D1"):
            gold = [{"path": p, "line": n, "category": cat} for p, n, cat in sorted(pt.reference(case))]
            success = pt.grade_report(case, {"case_id": case, "findings": gold})
            self.assertEqual(success["recall"], 1)
            self.assertEqual(success["unexpected"], 0)
            blank = pt.grade_report(case, {"case_id": case, "findings": []})
            self.assertGreater(blank["missing"], 0)
            self.assertEqual(blank["status"], "DEVELOPMENT_LABEL_SCORE_ONLY")
        # With no true source marker, the empty report is correct, not a failure.
        empty = pt.grade_report("PT01-D2", {"case_id": "PT01-D2", "findings": []})
        self.assertEqual(empty["missing"], 0)
        self.assertEqual(empty["unexpected"], 0)
        with_false_finding = pt.grade_report("PT01-D2", {"case_id": "PT01-D2", "findings":
                                             [{"path": "src/transport.py", "line": 2, "category": "tracked"}]})
        self.assertEqual(with_false_finding["unexpected"], 1)
        self.assertEqual(with_false_finding["precision"], 0)

    def test_implementation_requires_independent_behavior_checker(self):
        for case in ("PT01-A1", "PT01-A2"):
            with self.assertRaisesRegex(ValueError, "independent behavior"):
                pt.grade_report(case, {"case_id": case, "findings": []})

    def test_bad_inputs_stop_and_do_not_fake_green(self):
        with self.assertRaises(ValueError):
            pt.grade_report("PT01-B1", {"case_id": "PT01-B2", "findings": []})
        with self.assertRaises(ValueError):
            pt.grade_report("PT01-B1", {"case_id": "PT01-B1", "findings":
                                 [{"path": "../judge-only/labels.json", "line": 1, "category": "bug"}]})
        with self.assertRaises(ValueError):
            pt.grade_report("PT01-B1", {"case_id": "PT01-B1", "findings":
                                 [{"path": "app/receipt.py", "line": 1, "category": "invented"}]})
        with self.assertRaises(ValueError):
            pt.grade_report("PT01-B1", {"case_id": "PT01-B1", "findings":
                                 [{"path": "app/receipt.py", "line": 900, "category": "bug"}]})
        b1 = sorted(pt.reference("PT01-B1"))[0]
        duplicate = {"path": b1[0], "line": b1[1], "category": b1[2]}
        with self.assertRaisesRegex(ValueError, "duplicate"):
            pt.grade_report("PT01-B1", {"case_id": "PT01-B1", "findings": [duplicate, duplicate]})

    def test_offline_selftest_and_no_routing_mutation(self):
        self.assertEqual(pt.selftest()["status"], "SELFTEST_OK_OFFLINE")
        catalog = (pt.ROOT / "skill-catalog.yml").read_text(encoding="utf-8")
        self.assertNotIn("id: ponytail,", catalog)
        self.assertNotIn("id: ponytail-review,", catalog)
        self.assertNotIn("id: ponytail-audit,", catalog)
        overlays = (pt.ROOT / "routing-overlays.yml").read_text(encoding="utf-8")
        self.assertNotIn("skill: ponytail", overlays)

    def test_docs_and_readme_links_exist(self):
        for file in (pt.BASE / "README.md",
                     pt.ROOT / "Dokumentation/Reviews/Ponytail-2026-10-27.md"):
            self.assertTrue(file.exists(), str(file))
        self.assertIn("NOT RUN", (pt.BASE / "README.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
