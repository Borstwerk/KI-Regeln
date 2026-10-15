"""Offline tests for the GT-01 blind handoff and the GT-04 fixed pilot."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[1]
GT = ROOT / "Evals/Golden-Tasks"


def imported(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


class BlindTests(unittest.TestCase):
    def setUp(self):
        self.blind = imported(GT / "GT-01/prepare_blind_review.py", "blind_gt01")

    def test_packet_separates_labels_from_reveal_and_rubric_is_frozen(self):
        with tempfile.TemporaryDirectory() as tmp:
            review, secret = Path(tmp) / "review", Path(tmp) / "secret"
            record = self.blind.prepare(ROOT, review, secret, flip=False)
            self.assertEqual(sorted(f.name for f in review.iterdir()),
                             ["A.md", "B.md", "REVIEW-INSTRUCTIONS.md",
                              "scorecard-template.json", "table-schema.sql", "usage.md"])
            self.assertEqual(sorted(f.name for f in secret.iterdir()), ["reveal.json"])
            self.assertEqual(len(self.blind.criteria((review / "REVIEW-INSTRUCTIONS.md").read_text())), 9)
            instructions = (review / "REVIEW-INSTRUCTIONS.md").read_text().lower()
            self.assertNotIn("baseline", instructions)
            self.assertNotIn("skill", instructions)
            self.assertNotIn("fail", (review / "scorecard-template.json").read_text())
            self.assertEqual(record["labels"]["A"]["arm"], "baseline")

    def test_flip_swaps_original_answer_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            review, secret = Path(tmp) / "review", Path(tmp) / "private"
            info = self.blind.prepare(ROOT, review, secret, flip=True)
            self.assertEqual(info["labels"]["A"]["arm"], "skill")
            self.assertEqual(self.blind.sha((review / "A.md").read_bytes()),
                             info["labels"]["A"]["sha256"])

    def test_changed_original_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "source"
            gt = root / self.blind.GT
            gt.mkdir(parents=True)
            for suffix in (".json", ".md", "-baseline.md", "-skill.md"):
                original = self.blind.BASE + suffix
                shutil.copyfile(ROOT / self.blind.GT / original, gt / original)
            for filename in self.blind.SOURCES:
                shutil.copyfile(ROOT / self.blind.GT / filename, gt / filename)
            broken = gt / (self.blind.BASE + "-skill.md")
            broken.write_text(broken.read_text(encoding="utf-8") + "\nchanged", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Changed answer artifact"):
                self.blind.prepare(root, Path(tmp) / "review", Path(tmp) / "secret")

    def test_reviewer_dir_cannot_contain_operator_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            review = Path(tmp) / "review"
            with self.assertRaisesRegex(ValueError, "Separate reviewer"):
                self.blind.prepare(ROOT, review, review / "secret")

    def test_existing_packet_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            review, secret = Path(tmp) / "review", Path(tmp) / "secret"
            review.mkdir()
            with self.assertRaises(FileExistsError):
                self.blind.prepare(ROOT, review, secret)


class GT04Tests(unittest.TestCase):
    def setUp(self):
        self.driver = imported(ROOT / "Evals/Agentenarbeit/verification-loop/codex_instruction_pilot.py",
                               "gt04_pilot")

    def test_pins_match_committed_files_and_rubric_remains_partial_incident(self):
        blobs = self.driver.GT04_BLOBS
        self.assertEqual(len(blobs), 4)
        for name, git_blob in blobs.items():
            content = subprocess.check_output(["git", "cat-file", "blob", git_blob], cwd=ROOT)
            self.assertEqual(content, (ROOT / name).read_bytes(), name)
        task = yaml.safe_load((GT / "GT-04/task.yml").read_text(encoding="utf-8"))
        self.assertEqual(task["id"], "GT-04")
        self.assertEqual(task["expected_status"], "partial")
        self.assertEqual(set(task["required_skills"]), {"incident-response", "diagnose"})

    def test_prepare_only_creates_protocol_and_no_model_call(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(self.driver, "OUT", Path(tmp) / "codex-rule-pilot"), \
                 patch.object(sys, "argv", ["codex_instruction_pilot.py", "--gt04"]):
                self.driver.main()
            out = Path(tmp) / "codex-gt04-pilot-20261015"
            protocol = json.loads((out / "protocol.json").read_text(encoding="utf-8"))
            self.assertEqual(protocol["max_cli_sessions"], 2)
            self.assertFalse(protocol["retry_or_fallback"])
            self.assertEqual(len(protocol["cases"]), 1)
            case = protocol["cases"][0]
            self.assertEqual(case["id"], "GT-04")
            self.assertIn("inventory request timed out after 2000ms", case["input"])
            self.assertNotIn("required_skills", case["input"])
            self.assertNotIn("rubric", case["input"])
            self.assertFalse((out / "started.json").exists())
            self.assertFalse((out / "responses.json").exists())


if __name__ == "__main__":
    unittest.main()
