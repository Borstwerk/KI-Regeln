"""Tests for the paired UI reference pilot; no model or browser is invoked."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.ui_reference_pilot import ARMS, COMMON, REFERENCE, prepare, verify


ROOT = Path(__file__).resolve().parents[1]


class UIReferencePilotTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.out = Path(self.temp.name) / "packages"

    def tearDown(self):
        self.temp.cleanup()

    def test_both_arms_share_exact_common_files(self):
        manifest = prepare(ROOT, self.out)
        self.assertEqual("NOT_RUN", manifest["model_runs"])
        for p in COMMON:
            first = (self.out / ARMS[0] / p).read_bytes()
            second = (self.out / ARMS[1] / p).read_bytes()
            self.assertEqual(first, second, str(p))
        self.assertEqual("PASS", verify(self.out)["contract"])

    def test_external_reference_only_in_augmented_arm(self):
        prepare(ROOT, self.out)
        self.assertFalse((self.out / ARMS[0] / REFERENCE).exists())
        self.assertTrue((self.out / ARMS[1] / REFERENCE).is_file())
        self.assertFalse((self.out / ARMS[0] / "judge").exists())
        self.assertFalse((self.out / ARMS[1] / "judge").exists())

    def test_edit_to_frozen_reference_detected(self):
        prepare(ROOT, self.out)
        target = self.out / ARMS[1] / REFERENCE
        target.write_text(target.read_text(encoding="utf-8") + "\nmodified\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Integrity mismatch"):
            verify(self.out)

    def test_missing_required_file_detected(self):
        prepare(ROOT, self.out)
        (self.out / ARMS[0] / COMMON[0]).unlink()
        with self.assertRaisesRegex(ValueError, "Unexpected or missing files"):
            verify(self.out)

    def test_injected_judge_file_detected(self):
        prepare(ROOT, self.out)
        (self.out / ARMS[1] / "judge-labels.txt").write_text("leak", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Unexpected or missing files"):
            verify(self.out)

    def test_tampering_with_manifest_not_silently_accepted(self):
        prepare(ROOT, self.out)
        p = self.out / "manifest.json"
        data = json.loads(p.read_text(encoding="utf-8"))
        data["files"]["A-baseline"][str(REFERENCE)] = "bogus"
        p.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Unexpected manifest paths"):
            verify(self.out)

    def test_nonempty_output_rejected(self):
        self.out.mkdir()
        (self.out / "unrelated.txt").write_text("preserve", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "new or empty"):
            prepare(ROOT, self.out)
        self.assertEqual("preserve", (self.out / "unrelated.txt").read_text(encoding="utf-8"))

    def test_repo_internal_output_rejected(self):
        with self.assertRaisesRegex(ValueError, "outside"):
            prepare(ROOT, ROOT / "Evals" / "Webentwicklung" / "UI-Reference-Pilot" / "runs")

    def test_source_metadata_and_evidence_absent_from_runner_input(self):
        task = (ROOT / COMMON[0]).read_text(encoding="utf-8")
        self.assertNotIn("UI-UX-Pro-Max-Benchmark-Erfolg", task)
        self.assertNotIn("Punktzahl", task)
        self.assertEqual(5, len(json.loads((ROOT / COMMON[1]).read_text(encoding="utf-8"))["items"]))


if __name__ == "__main__":
    unittest.main()
