from __future__ import annotations

import hashlib
import tempfile
import unittest
from pathlib import Path

import yaml

from tools.behavioral_harness import HarnessError, load_yaml, package_run
from tools.behavioral_harness_pair import (
    METHOD_EVIDENCE_CONTRACT,
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
        "recommended_repetitions": 3,
        "evaluation_dimensions": [{"id": "classification", "question": "correct?"}],
        "global_hard_failures": ["fabrication"],
        "cases": [
            {
                "case_id": "CV-T01",
                "user_prompt": "Verify the claim from the supplied sources.",
                "fixtures": [
                    {"path": "source-a.md", "role": "authoritative-source"},
                    {"path": "source-b.md", "role": "supporting-source"},
                ],
                "ground_truth": {
                    "classification": {
                        "preferred": "partial",
                        "accepted_alternatives": {
                            "unsupported": {
                                "conditions": [
                                    "must explicitly distinguish the supported and unsupported parts"
                                ]
                            }
                        },
                        "disallowed": ["supported", "conflicting", "not-verified"],
                    },
                    "relevant_evidence": ["A", "B"],
                    "decisive_reason": "one source supports only part of the claim",
                    "known_traps": ["guessing"],
                    "allowed_uncertainty": [],
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
        (self.root / "skill.md").write_text(
            "# claim-verification\nUse evidence.\n",
            encoding="utf-8",
        )
        self.experiment = synthetic_experiment()

    def tearDown(self):
        self.tmp.cleanup()

    def experiment_file(self, experiment=None):
        path = self.root / "experiment.yml"
        path.write_text(
            yaml.safe_dump(experiment or self.experiment, sort_keys=False),
            encoding="utf-8",
        )
        return path

    def prepare(self, repetition=1, seed="blind-seed"):
        pair = compile_paired_case(
            self.experiment,
            "CV-T01",
            self.root,
            repetition,
            seed,
        )
        out = self.root / f"prepared-{repetition}-{hashlib.sha256(seed.encode()).hexdigest()[:6]}"
        write_paired_case(pair, self.root, out)
        return out

    def package_runs(
        self,
        pair_dir: Path,
        model_a="same-model",
        model_b="same-model",
        runner_a="synthetic",
        runner_b="synthetic",
        session_a="session-1",
        session_b="session-2",
    ):
        control = load_yaml(pair_dir / "control.yml")
        run_dirs = []
        for index, response_id in enumerate(sorted(control["response_assignments"]), start=1):
            run_dir = package_run(
                pair_dir / "responses" / response_id,
                None,
                None,
                None,
                None,
                self.root / f"runs-{pair_dir.name}",
                f"run-{index}",
                runner_type=runner_a if index == 1 else runner_b,
                runner_model=model_a if index == 1 else model_b,
                runner_session_id=session_a if index == 1 else session_b,
                started_at="unknown",
                finished_at="unknown",
            )
            run_dirs.append(run_dir)
        return run_dirs

    def write_method_evidence(
        self,
        pair_dir: Path,
        run_dirs: list[Path],
        complete=True,
        same_config=True,
        same_runtime=True,
    ):
        paths = []
        for index, run_dir in enumerate(run_dirs, start=1):
            manifest = load_yaml(run_dir / "manifest.yml")
            model_fp = (
                "sha256:" + ("1" * 64 if same_config or index == 1 else "2" * 64)
                if complete
                else "unknown"
            )
            runtime_fp = (
                "sha256:" + ("3" * 64 if same_runtime or index == 1 else "4" * 64)
                if complete
                else "unknown"
            )
            data = {
                "schema_version": 1,
                "contract": METHOD_EVIDENCE_CONTRACT,
                "response_id": manifest["test_id"],
                "runner_type": manifest["runner_type"] if complete else "unknown",
                "runner_model": manifest["runner_model"] if complete else "unknown",
                "runner_session_id": manifest["runner_session_id"] if complete else "unknown",
                "model_configuration_fingerprint": model_fp,
                "runtime_configuration_fingerprint": runtime_fp,
                "fresh_context": True if complete else "unknown",
                "network_disabled": True if complete else "unknown",
                "repository_access_disabled": True if complete else "unknown",
                "package_only_access": True if complete else "unknown",
            }
            path = self.root / f"method-{index}-{pair_dir.name}.yml"
            path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
            paths.append(path)
        return paths

    def test_P1_load_contract_roles_and_classification_structure(self):
        loaded = load_paired_experiment(self.experiment_file())
        truth = loaded["cases"][0]["ground_truth"]["classification"]
        self.assertEqual("partial", truth["preferred"])
        self.assertIn("unsupported", truth["accepted_alternatives"])
        self.assertEqual("authoritative-source", loaded["cases"][0]["fixtures"][0]["role"])
        self.assertEqual("supporting-source", loaded["cases"][0]["fixtures"][1]["role"])

    def test_P2_invalid_classification_metadata_is_rejected(self):
        invalid = synthetic_experiment()
        invalid["cases"][0]["ground_truth"]["classification"]["preferred"] = "maybe"
        with self.assertRaises(HarnessError):
            load_paired_experiment(self.experiment_file(invalid))

        invalid = synthetic_experiment()
        del invalid["cases"][0]["ground_truth"]["classification"]["accepted_alternatives"]["unsupported"]["conditions"]
        with self.assertRaises(HarnessError):
            load_paired_experiment(self.experiment_file(invalid))

        invalid = synthetic_experiment()
        invalid["cases"][0]["ground_truth"]["classification"]["disallowed"].append("unsupported")
        with self.assertRaises(HarnessError):
            load_paired_experiment(self.experiment_file(invalid))

    def test_P3_prompt_sources_roles_and_skill_only_delta(self):
        pair_dir = self.prepare()
        status = verify_paired_prepared(pair_dir)
        self.assertTrue(status["prompt_parity"])
        self.assertTrue(status["subject_source_parity"])
        self.assertTrue(status["subject_role_parity"])

        control = load_yaml(pair_dir / "control.yml")
        expected_roles = {
            "source-a.md": "authoritative-source",
            "source-b.md": "supporting-source",
        }
        self.assertEqual(expected_roles, control["shared_subject_source_roles"])

        for response_id, treatment in control["response_assignments"].items():
            response = pair_dir / "responses" / response_id
            judge = load_yaml(response / "judge-view.yml")
            subject_roles = {
                item["path"]: item["role"]
                for item in judge["fixtures"]
                if item["role"] != "skill-instruction"
            }
            self.assertEqual(expected_roles, subject_roles)
            skill_records = [
                item for item in judge["fixtures"]
                if item["role"] == "skill-instruction"
            ]
            if treatment == "baseline":
                self.assertEqual([], skill_records)
            else:
                self.assertEqual(1, len(skill_records))

    def test_P4_ground_truth_and_roles_reach_blind_judge_without_treatment(self):
        pair_dir = self.prepare()
        judge = load_yaml(pair_dir / "judge-contract.yml")
        self.assertEqual(
            "partial",
            judge["ground_truth"]["classification"]["preferred"],
        )
        self.assertIn(
            "unsupported",
            judge["ground_truth"]["classification"]["accepted_alternatives"],
        )
        self.assertEqual("supporting-source", judge["source_roles"][1]["role"])
        text = (pair_dir / "judge-contract.yml").read_text(encoding="utf-8").lower()
        self.assertNotIn("response_assignments", text)
        self.assertNotIn("execution_order", text)
        self.assertNotIn("baseline", text)

    def test_P5_treatment_order_is_reproducible_and_counterbalanced(self):
        first = self.prepare(repetition=1, seed="stable-seed")
        first_control = load_yaml(first / "control.yml")
        repeat_pair = compile_paired_case(
            self.experiment,
            "CV-T01",
            self.root,
            1,
            "stable-seed",
        )
        self.assertEqual(first_control["execution_order"], repeat_pair["control"]["execution_order"])

        second = self.prepare(repetition=2, seed="stable-seed")
        second_control = load_yaml(second / "control.yml")
        first_treatments = [
            first_control["response_assignments"][rid]
            for rid in first_control["execution_order"]
        ]
        second_treatments = [
            second_control["response_assignments"][rid]
            for rid in second_control["execution_order"]
        ]
        self.assertEqual(list(reversed(first_treatments)), second_treatments)
        self.assertEqual({"baseline", "skill"}, set(first_treatments))

    def test_P6_tampered_runner_source_copy_is_rejected(self):
        pair_dir = self.prepare()
        control = load_yaml(pair_dir / "control.yml")
        response_id = next(iter(control["response_assignments"]))
        source = next(
            (pair_dir / "responses" / response_id / "runner-package" / "sources").glob("*")
        )
        source.write_text("tampered\n", encoding="utf-8")
        with self.assertRaises(HarnessError):
            verify_paired_prepared(pair_dir)

    def test_P7_missing_method_evidence_packages_but_is_not_comparison_eligible(self):
        pair_dir = self.prepare()
        run_dirs = self.package_runs(pair_dir)
        blind = package_blind_pair(pair_dir, run_dirs, self.root / "blind-partial")
        parity = load_yaml(blind / "parity.yml")
        self.assertEqual("partial", parity["method_evidence_status"])
        self.assertFalse(parity["comparison_eligible"])
        self.assertEqual("unknown", parity["model_configuration_parity"])

    def test_P8_complete_synthetic_method_evidence_can_validate_pair(self):
        pair_dir = self.prepare()
        run_dirs = self.package_runs(pair_dir)
        evidence = self.write_method_evidence(pair_dir, run_dirs, complete=True)
        blind = package_blind_pair(
            pair_dir,
            run_dirs,
            self.root / "blind-valid",
            evidence,
        )
        parity = load_yaml(blind / "parity.yml")
        self.assertEqual("pass", parity["method_evidence_status"])
        self.assertTrue(parity["comparison_eligible"])
        self.assertTrue(parity["model_configuration_parity"])
        self.assertTrue(parity["runtime_configuration_parity"])
        self.assertTrue(parity["fresh_context_sessions_distinct"])

    def test_P9_known_model_or_session_mismatch_is_stored_as_method_fail(self):
        pair_dir = self.prepare()
        run_dirs = self.package_runs(
            pair_dir,
            model_a="model-a",
            model_b="model-b",
            session_a="same-session",
            session_b="same-session",
        )
        evidence = self.write_method_evidence(pair_dir, run_dirs, complete=True)
        blind = package_blind_pair(
            pair_dir,
            run_dirs,
            self.root / "blind-fail",
            evidence,
        )
        parity = load_yaml(blind / "parity.yml")
        self.assertEqual("fail", parity["method_evidence_status"])
        self.assertFalse(parity["comparison_eligible"])
        self.assertFalse(parity["same_runner_model"])
        self.assertFalse(parity["fresh_context_sessions_distinct"])

    def test_P10_runtime_configuration_mismatch_is_method_fail(self):
        pair_dir = self.prepare()
        run_dirs = self.package_runs(pair_dir)
        evidence = self.write_method_evidence(
            pair_dir,
            run_dirs,
            complete=True,
            same_runtime=False,
        )
        blind = package_blind_pair(
            pair_dir,
            run_dirs,
            self.root / "blind-runtime-fail",
            evidence,
        )
        parity = load_yaml(blind / "parity.yml")
        self.assertFalse(parity["runtime_configuration_parity"])
        self.assertEqual("fail", parity["method_evidence_status"])
        self.assertFalse(parity["comparison_eligible"])

    def test_P11_blind_package_contains_no_order_or_mapping(self):
        pair_dir = self.prepare()
        run_dirs = self.package_runs(pair_dir)
        blind = package_blind_pair(pair_dir, run_dirs, self.root / "blind-clean")
        text = (
            (blind / "judge-contract.yml").read_text(encoding="utf-8")
            + (blind / "blind-judge-input.yml").read_text(encoding="utf-8")
            + (blind / "parity.yml").read_text(encoding="utf-8")
        ).lower()
        self.assertNotIn("response_assignments", text)
        self.assertNotIn("execution_order", text)
        self.assertNotIn("baseline", text)

    def test_P12_treatment_disclosure_rejected(self):
        pair_dir = self.prepare()
        control = load_yaml(pair_dir / "control.yml")
        response_ids = sorted(control["response_assignments"])
        disclosure = self.root / "disclosure.md"
        disclosure.write_text(
            "I used claim-verification for this answer.\n",
            encoding="utf-8",
        )
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
            package_blind_pair(
                pair_dir,
                run_dirs,
                self.root / "blind-disclosure",
            )

    def test_P12a_disclosure_forms_are_rejected(self):
        """Each form must be refused end to end, not just by the predicate."""
        pair_dir = self.prepare()
        response_ids = sorted(load_yaml(pair_dir / "control.yml")["response_assignments"])
        forms = {
            "skill-treatment": "This answer comes from the skill treatment.\n",
            "baseline-treatment": "I am the baseline treatment for this case.\n",
            "skill-instruction": "I followed the skill instruction supplied to me.\n",
            "treatment-instruction": "The treatment instruction told me to cite sources.\n",
            "instruction-path": "I read instructions/SKILL.md before answering.\n",
            "target-skill-id": "I used claim-verification for this answer.\n",
            "skill-variant": "This is the skill variant of the run.\n",
            "baseline-condition": "Answering under the baseline condition.\n",
        }
        for label, body in forms.items():
            with self.subTest(form=label):
                disclosure = self.root / f"disc-{label}.md"
                disclosure.write_text(body, encoding="utf-8")
                run_dirs = [
                    package_run(
                        pair_dir / "responses" / response_id,
                        disclosure if index == 1 else None,
                        None, None, None,
                        self.root / f"runs-{label}",
                        f"run-{label}-{index}",
                        runner_type="synthetic", runner_model="same-model",
                        runner_session_id=f"session-{label}-{index}",
                        started_at="unknown", finished_at="unknown",
                    )
                    for index, response_id in enumerate(response_ids, start=1)
                ]
                with self.assertRaises(HarnessError):
                    package_blind_pair(pair_dir, run_dirs, self.root / f"blind-{label}")

    def test_P12b_ordinary_subject_language_still_packages_blind(self):
        """Negative control: normal wording, including the bare word 'skill', must pass."""
        pair_dir = self.prepare()
        response_ids = sorted(load_yaml(pair_dir / "control.yml")["response_assignments"])
        answer = self.root / "ordinary.md"
        answer.write_text(
            "Verdict: supported.\n\n"
            "The release notes state the value directly, and the admin guide agrees.\n"
            "Assessing this well takes skill and care; the baseline throughput quoted in\n"
            "the report is 30 seconds, and the instruction in the policy document is clear.\n",
            encoding="utf-8",
        )
        run_dirs = [
            package_run(
                pair_dir / "responses" / response_id,
                answer, None, None, None,
                self.root / "runs-ordinary",
                f"run-ordinary-{index}",
                runner_type="synthetic", runner_model="same-model",
                runner_session_id=f"session-ordinary-{index}",
                started_at="unknown", finished_at="unknown",
            )
            for index, response_id in enumerate(response_ids, start=1)
        ]
        blind = package_blind_pair(pair_dir, run_dirs, self.root / "blind-ordinary")
        parity = load_yaml(blind / "parity.yml")
        self.assertFalse(parity["treatment_disclosure_detected"])


class ClaimVerificationExperimentContractTests(unittest.TestCase):
    def test_actual_cv05_source_roles_are_not_flattened(self):
        repo_root = Path(__file__).resolve().parents[1]
        experiment = load_paired_experiment(
            repo_root
            / "Evals/Behavioral-Harness/experiments/claim-verification-v1/experiment.yml"
        )
        case = next(item for item in experiment["cases"] if item["case_id"] == "CV-05-primary-vs-summary")
        roles = {Path(item["path"]).name: item["role"] for item in case["fixtures"]}
        self.assertEqual("authoritative-source", roles["api-v2-reference.md"])
        self.assertEqual("supporting-source", roles["api-search-summary.md"])
        self.assertEqual("supporting-source", roles["community-batch-guide.md"])

    def test_actual_cv02_and_cv06_alternatives_are_structured(self):
        repo_root = Path(__file__).resolve().parents[1]
        experiment = load_paired_experiment(
            repo_root
            / "Evals/Behavioral-Harness/experiments/claim-verification-v1/experiment.yml"
        )
        cases = {item["case_id"]: item for item in experiment["cases"]}
        cv02 = cases["CV-02-population-partial"]["ground_truth"]["classification"]
        cv06 = cases["CV-06-insufficient-evidence"]["ground_truth"]["classification"]
        self.assertEqual("partial", cv02["preferred"])
        self.assertIn("unsupported", cv02["accepted_alternatives"])
        self.assertEqual("not-verified", cv06["preferred"])
        self.assertIn("partial", cv06["accepted_alternatives"])


if __name__ == "__main__":
    unittest.main()
