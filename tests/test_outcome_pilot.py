from __future__ import annotations

import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path

from tools.outcome_pilot import canonical_hash, score_outcome


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "Evals" / "Outcome-Pilot"


def load(relative: str) -> dict:
    return json.loads((PILOT / relative).read_text(encoding="utf-8"))


class OutcomePilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = load("runner-input/candidates.json")
        cls.labels = load("judge-only/labels.json")
        cls.reference = load("controls/reference.json")

    def test_reference_has_full_outcome_but_no_process_claim(self):
        result = score_outcome(self.case, self.labels, self.reference)
        self.assertEqual(result["outcome_status"], "SCORED")
        self.assertEqual(result["outcome_score"], 100.0)
        self.assertEqual(result["true_positives"], 2)
        self.assertEqual(result["process_verification"], "NOT_RUN")

    def test_empty_baseline_is_zero(self):
        result = score_outcome(self.case, self.labels, load("controls/empty.json"))
        self.assertEqual(result["outcome_status"], "SCORED")
        self.assertEqual(result["outcome_score"], 0.0)
        self.assertEqual(result["false_negatives"], 2)

    def test_irrelevant_but_cited_selection_degrades_outcome(self):
        submission = copy.deepcopy(self.reference)
        submission["selected"].append({
            "id": "viral-ai-wallpaper",
            "evidence_urls": ["https://example.invalid/wallpaper"],
        })
        result = score_outcome(self.case, self.labels, submission)
        self.assertEqual(result["outcome_status"], "SCORED")
        self.assertLess(result["outcome_score"], 100.0)
        self.assertEqual(result["false_positives"], 1)

    def test_historical_alias_is_hard_blocker(self):
        result = score_outcome(
            self.case, self.labels, load("controls/historical-duplicate.json")
        )
        self.assertEqual(result["outcome_status"], "BLOCKED")
        self.assertEqual(result["outcome_score"], 0.0)
        self.assertIn("historical-duplicate:browser-relay-redux", result["blockers"])

    def test_forged_evidence_is_hard_blocker(self):
        submission = copy.deepcopy(self.reference)
        submission["selected"][0]["evidence_urls"] = ["https://attacker.invalid/fake"]
        result = score_outcome(self.case, self.labels, submission)
        self.assertEqual(result["outcome_status"], "BLOCKED")
        self.assertIn("unsupported-evidence:outcome-grader", result["blockers"])

    def test_missing_evidence_is_hard_blocker(self):
        submission = copy.deepcopy(self.reference)
        submission["selected"][0]["evidence_urls"] = []
        result = score_outcome(self.case, self.labels, submission)
        self.assertIn("missing-evidence:outcome-grader", result["blockers"])

    def test_unknown_and_repeated_ids_are_hard_blockers(self):
        submission = copy.deepcopy(self.reference)
        submission["selected"].append({
            "id": "not-in-snapshot", "evidence_urls": ["https://example.invalid/x"]
        })
        result = score_outcome(self.case, self.labels, submission)
        self.assertIn("unknown-id:not-in-snapshot", result["blockers"])
        repeated = copy.deepcopy(self.reference)
        repeated["selected"].append(repeated["selected"][0])
        result = score_outcome(self.case, self.labels, repeated)
        self.assertIn("repeated-selection:outcome-grader", result["blockers"])

    def test_untrusted_self_scoring_is_not_accepted(self):
        submission = {**self.reference, "outcome_score": 100}
        with self.assertRaisesRegex(ValueError, "exactly"):
            score_outcome(self.case, self.labels, submission)

    def test_bad_judge_truth_rejected(self):
        labels = copy.deepcopy(self.labels)
        labels["relevant_ids"].append("browser-relay-redux")
        with self.assertRaisesRegex(ValueError, "historical duplicate"):
            score_outcome(self.case, labels, self.reference)

    def test_input_fingerprint_changes_when_case_changes(self):
        changed = copy.deepcopy(self.case)
        changed["already_delivered"].append("new-history")
        self.assertNotEqual(canonical_hash(self.case), canonical_hash(changed))
        self.assertEqual(canonical_hash(self.case), canonical_hash(copy.deepcopy(self.case)))

    def test_cli_succeeds_and_records_exact_inputs(self):
        command = [
            sys.executable, str(ROOT / "tools" / "outcome_pilot.py"),
            "--case", str(PILOT / "runner-input/candidates.json"),
            "--judge", str(PILOT / "judge-only/labels.json"),
            "--submission", str(PILOT / "controls/reference.json"),
            "--agent", "synthetic-reference",
        ]
        run = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(run.returncode, 0, run.stderr)
        output = json.loads(run.stdout)
        self.assertEqual(output["agent"], "synthetic-reference")
        self.assertEqual(output["sha256"]["judge"], canonical_hash(self.labels))
        self.assertEqual(output["outcome_score"], 100.0)
        command[-1] = "synthetic-block"
        command[command.index("--submission") + 1] = str(
            PILOT / "controls/historical-duplicate.json"
        )
        blocked = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(blocked.returncode, 1, blocked.stderr)
        self.assertEqual(json.loads(blocked.stdout)["outcome_status"], "BLOCKED")

    def test_judge_labels_not_in_runner_directory(self):
        runner = PILOT / "runner-input"
        self.assertFalse((runner / "labels.json").exists())
        self.assertNotIn("relevant_ids", (runner / "TASK.md").read_text(encoding="utf-8"))
        self.assertNotIn("relevant_ids", (runner / "candidates.json").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
