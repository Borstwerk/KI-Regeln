from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.behavioral_harness import HarnessError, load_yaml, package_run
from tools.behavioral_harness_pair import (
    compile_paired_case,
    load_paired_experiment,
    package_blind_pair,
    verify_paired_prepared,
    write_paired_case,
)


def synthetic_experiment() -> dict:
    return {
        "schema_version": 1,
        "contract": "behavioral-paired-skill-eval/v1",
        "experiment_id": "pair-test",
        "repository": "Borstwerk/KI-Regeln",
        "pinned_commit": "abc123",
        "target_skill": {"id": "claim-verification", "path": "skill.md"},
        "recommended_repetitions": 2,
        "evaluation_dimensions": [{"id": "classification", "question": "correct?"}],
        "global_hard_failures": ["fabrication"],
        "cases": [
            {
                "case_id": "CV-T01",
                "user_prompt": "Verify the claim from the supplied sources.",
                "fixtures": ["source-a.md", "source-b.md"],
                "ground_truth": {
                    "expected_classification": "supported",
                    "relevant_evidence": ["A", "B"],
                    "decisive_reason": "both sources support it",
                    "known_traps": ["guessing"],
                    "allowed_uncertainty": ["none"],
                    "hard_failures": ["fabrication"],
                },
            }
        ],
    }


class BehavioralHarnessPairTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "source-a.md").write_text("source A\n", encoding="utf-8")
        (self.root / "source-b.md").write_text("source B\n", encoding="utf-8")
        (self.root / "skill.md").write_text("# claim-verification\nUse evidence.\n", encoding="utf-8")
        self.experiment = synthetic_experiment()

    def tearDown(self):
        self.tmp.cleanup()

    def prepare(self, repetition=1, seed="blind-seed"):
        pair = compile_paired_case(self.experiment, "CV-T01", self.root, repetition, seed)
        out = self.root / f"prepared-{repetition}"
        write_paired_case(pair, self.root, out)
        return out

    def package_runs(self, pair_dir: Path, model_a="same-model", model_b="same-model"):
        control = load_yaml(pair_dir / "control.yml")
        run_dirs = []
        for index, response_id in enumerate(sorted(control["response_assignments"]), start=1):
            run_dir = package_run(
                pair_dir / "responses" / response_id,
                None,
                None,
                None,
                None,
                self.root / "runs",
                f"run-{index}",
                runner_type="synthetic",
                runner_model=model_a if index == 1 else model_b,
                runner_session_id=f"session-{index}",
                started_at="unknown",
                finished_at="unknown",
            )
            run_dirs.append(run_dir)
        return run_dirs

    def test_P1_load_contract_and_repeat_requirement(self):
        path = self.root / "experiment.yml"
        import yaml
        path.write_text(yaml.safe_dump(self.experiment, sort_keys=False), encoding="utf-8")
        loaded = load_paired_experiment(path)
        self.assertEqual("pair-test", loaded["experiment_id"])
        self.experiment["recommended_repetitions"] = 1
        path.write_text(yaml.safe_dump(self.experiment, sort_keys=False), encoding="utf-8")
        with self.assertRaises(HarnessError):
            load_paired_experiment(path)

    def test_P2_prompt_and_subject_source_parity_with_skill_only_delta(self):
        pair_dir = self.prepare()
        status = verify_paired_prepared(pair_dir)
        self.assertTrue(status["prompt_parity"])
        self.assertTrue(status["subject_source_parity"])
        control = load_yaml(pair_dir / "control.yml")
        for response_id, treatment in control["response_assignments"].items():
            runner = pair_dir / "responses" / response_id / "runner-package"
            instructions = list((runner / "instructions").glob("*")) if (runner / "instructions").exists() else []
            if treatment == "baseline":
                self.assertEqual([], instructions)
            else:
                self.assertEqual(1, len(instructions))

    def test_P3_treatment_mapping_hidden_from_blind_judge_contract(self):
        first = self.prepare(repetition=1, seed="stable-seed")
        second_pair = compile_paired_case(self.experiment, "CV-T01", self.root, 1, "stable-seed")
        first_control = load_yaml(first / "control.yml")
        self.assertEqual(first_control["response_assignments"], second_pair["control"]["response_assignments"])
        judge = load_yaml(first / "judge-contract.yml")
        self.assertNotIn("response_assignments", judge)
        self.assertNotIn("treatment", judge)

    def test_P4_tampered_runner_source_copy_is_rejected(self):
        pair_dir = self.prepare()
        control = load_yaml(pair_dir / "control.yml")
        response_id = next(iter(control["response_assignments"]))
        source = next((pair_dir / "responses" / response_id / "runner-package" / "sources").glob("*"))
        source.write_text("tampered\n", encoding="utf-8")
        with self.assertRaises(HarnessError):
            verify_paired_prepared(pair_dir)

    def test_P5_blind_package_contains_outputs_but_not_mapping(self):
        pair_dir = self.prepare()
        run_dirs = self.package_runs(pair_dir)
        blind = package_blind_pair(pair_dir, run_dirs, self.root / "blind")
        blind_input = load_yaml(blind / "blind-judge-input.yml")
        parity = load_yaml(blind / "parity.yml")
        text = (blind / "judge-contract.yml").read_text(encoding="utf-8") + (blind / "blind-judge-input.yml").read_text(encoding="utf-8")
        self.assertNotIn("response_assignments", text)
        self.assertNotIn("baseline", text.lower())
        self.assertEqual(2, len(blind_input["responses"]))
        self.assertEqual("unverified", parity["model_configuration_parity"])

    def test_P6_different_runner_models_rejected(self):
        pair_dir = self.prepare()
        run_dirs = self.package_runs(pair_dir, model_a="model-a", model_b="model-b")
        with self.assertRaises(HarnessError):
            package_blind_pair(pair_dir, run_dirs, self.root / "blind-mismatch")

    def test_P7_treatment_disclosure_rejected(self):
        pair_dir = self.prepare()
        control = load_yaml(pair_dir / "control.yml")
        response_ids = sorted(control["response_assignments"])
        disclosure = self.root / "disclosure.md"
        disclosure.write_text("I used claim-verification for this answer.\n", encoding="utf-8")
        run_dirs = []
        for index, response_id in enumerate(response_ids, start=1):
            output = disclosure if index == 1 else None
            run_dirs.append(
                package_run(
                    pair_dir / "responses" / response_id,
                    output,
                    None,
                    None,
                    None,
                    self.root / "disclosure-runs",
                    f"run-{index}",
                    runner_type="synthetic",
                    runner_model="same-model",
                    runner_session_id=f"session-{index}",
                    started_at="unknown",
                    finished_at="unknown",
                )
            )
        with self.assertRaises(HarnessError):
            package_blind_pair(pair_dir, run_dirs, self.root / "blind-disclosure")


if __name__ == "__main__":
    unittest.main()
