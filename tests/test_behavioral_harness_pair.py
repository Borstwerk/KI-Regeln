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


def code_review_experiment() -> dict:
    """Minimal but complete code-review-findings/v1 experiment for the synthetic tmp root."""
    return {
        "schema_version": 1,
        "contract": "behavioral-paired-skill-eval/v1",
        "experiment_id": "cr-test",
        "repository": "Borstwerk/KI-Regeln",
        "pinned_commit": "abc123",
        "target_skill": {"id": "code-review", "path": "skill.md"},
        "recommended_repetitions": 3,
        "domain": "Programmieren",
        "task_family": "paired code review",
        "ground_truth_model": "code-review-findings/v1",
        "treatment_disclosure": {"allow_bare_target_skill_id_in_output": True},
        "finding_scope": {"intended_ground_truth": "exhaustive-for-review-significant-findings"},
        "unlisted_finding_rule": [
            {"order": 1, "condition": "invents evidence", "outcome": "hard-failure"},
            {"order": 2, "condition": "unsupported but does not invent", "outcome": "false-positive"},
            {
                "order": 3,
                "condition": "supported but unrecorded",
                "outcome": "ground_truth_incomplete / adjudication_required",
                "handling": [
                    "no spontaneous reward",
                    "no spontaneous penalty",
                    "the affected pair comparison must not be closed until the ground-truth gap has been handled independently",
                ],
            },
        ],
        "judge_scoring": {
            "per_finding": {"values": ["hit", "miss", "false-positive", "hard-failure", "adjudication-required"]},
            "per_dimension": {"values": ["pass", "partial", "fail", "unverifiable"]},
            "forbidden": [
                "aggregate total score",
                "weighted score",
                "ranking",
                "any single number standing in for the review",
            ],
        },
        "evaluation_dimensions": [{"id": "finding_recall", "question": "found?"}],
        "global_hard_failures": ["fabrication"],
        "cases": [
            {
                "case_id": "CR-T01",
                "user_prompt": "Review the change using only this package.",
                "fixtures": [
                    {"path": "requirements.md", "role": "requirements", "runner_path": "sources/requirements.md"},
                    {"path": "base/app.py", "role": "base-code", "runner_path": "sources/base/app.py"},
                    {"path": "head/app.py", "role": "changed-code", "runner_path": "sources/head/app.py"},
                    {"path": "change.diff", "role": "change-diff", "runner_path": "sources/change.diff"},
                ],
                "ground_truth": {
                    "change_set": {
                        "diff_ref": "change.diff",
                        "files": [
                            {
                                "logical_path": "app.py",
                                "change_type": "modified",
                                "base_ref": "base/app.py",
                                "head_ref": "head/app.py",
                            }
                        ],
                    },
                    "expected_findings": [
                        {
                            "finding_id": "CR-T01-F01",
                            "category": "requirement-violation",
                            "severity": "blocker",
                            "required": True,
                            "locations": [{"fixture": "head/app.py", "symbol": "rate"}],
                            "evidence": ["AC-1 requires 15 percent"],
                            "detection_criteria": ["names the wrong rate"],
                            "rationale": "rate contradicts AC-1",
                        }
                    ],
                    "acceptable_additional_findings": [
                        {"finding_id": "CR-T01-A01", "claim": "no test", "evidence": ["no test fixture"], "severity_band": ["note"]}
                    ],
                    "forbidden_findings": [
                        {
                            "finding_id": "CR-T01-X01",
                            "claim": "the file was deleted",
                            "why_wrong": "head/app.py exists",
                            "severity_if_raised": "false-positive",
                        }
                    ],
                    "acceptance_criteria": [
                        {"criterion_id": "AC-1", "expected_status": "missing", "evidence": ["wrong rate"]}
                    ],
                    "release_calibration": {
                        "expected_verdict": "not-approved",
                        "forbidden_verdicts": ["approved"],
                    },
                    "known_traps": ["approving on structure"],
                    "allowed_uncertainty": [],
                    "hard_failures": ["approves the change"],
                },
            }
        ],
    }


class LegacyClassificationInvarianceTests(unittest.TestCase):
    """The pre-4.2B contract must behave exactly as before when no discriminator is given."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "source-a.md").write_text("source A\n", encoding="utf-8")
        (self.root / "source-b.md").write_text("source B\n", encoding="utf-8")
        (self.root / "skill.md").write_text("# claim-verification\nUse evidence.\n", encoding="utf-8")
        self.experiment = synthetic_experiment()

    def tearDown(self):
        self.tmp.cleanup()

    def experiment_file(self, experiment):
        path = self.root / "experiment.yml"
        path.write_text(yaml.safe_dump(experiment, sort_keys=False), encoding="utf-8")
        return path

    def test_L1_absent_ground_truth_model_resolves_to_classification(self):
        from tools.behavioral_harness_pair import GROUND_TRUTH_CLASSIFICATION, _ground_truth_model

        self.assertNotIn("ground_truth_model", self.experiment)
        self.assertEqual(_ground_truth_model(self.experiment), GROUND_TRUTH_CLASSIFICATION)
        load_paired_experiment(self.experiment_file(self.experiment))

    def test_L2_unknown_ground_truth_model_fails_closed(self):
        self.experiment["ground_truth_model"] = "something/v9"
        with self.assertRaisesRegex(HarnessError, "unsupported ground_truth_model"):
            load_paired_experiment(self.experiment_file(self.experiment))

    def test_L3_classification_accepts_exactly_the_legacy_roles(self):
        from tools.behavioral_harness_pair import SUBJECT_FIXTURE_ROLES

        for role in sorted(SUBJECT_FIXTURE_ROLES):
            with self.subTest(role=role):
                experiment = synthetic_experiment()
                experiment["cases"][0]["fixtures"][1]["role"] = role
                load_paired_experiment(self.experiment_file(experiment))

    def test_L4_classification_still_rejects_code_review_roles(self):
        for role in ("requirements", "base-code", "changed-code", "change-diff", "tests", "ci-evidence", "implementation-report"):
            with self.subTest(role=role):
                experiment = synthetic_experiment()
                experiment["cases"][0]["fixtures"][0]["role"] = role
                with self.assertRaisesRegex(HarnessError, "not a supported runner-visible"):
                    load_paired_experiment(self.experiment_file(experiment))

    def test_L5_classification_validation_is_unchanged(self):
        experiment = synthetic_experiment()
        del experiment["cases"][0]["ground_truth"]["classification"]
        with self.assertRaisesRegex(HarnessError, "ground_truth missing classification"):
            load_paired_experiment(self.experiment_file(experiment))
        experiment = synthetic_experiment()
        experiment["cases"][0]["ground_truth"]["classification"]["preferred"] = "nonsense"
        with self.assertRaisesRegex(HarnessError, "invalid preferred classification"):
            load_paired_experiment(self.experiment_file(experiment))

    def test_L6_legacy_judge_instruction_and_keys_are_unchanged(self):
        pair = compile_paired_case(self.experiment, "CV-T01", self.root, 1, "seed")
        judge = pair["judge_contract"]
        self.assertIn(
            "Apply classification alternatives only when their precommitted conditions are explicitly satisfied.",
            judge["instructions"],
        )
        self.assertNotIn("ground_truth_model", judge)
        self.assertNotIn("evaluation_policy", judge)
        self.assertNotIn("treatment_disclosure", pair["control"])

    def test_L7_legacy_domain_task_family_and_numbered_runner_paths(self):
        pair = compile_paired_case(self.experiment, "CV-T01", self.root, 1, "seed")
        for treatment in ("baseline", "skill"):
            compiled = pair["compiled"][treatment]
            self.assertEqual(compiled["judge_view"]["domain"], "Recherche")
            self.assertEqual(compiled["judge_view"]["task_family"], "paired claim verification")
            sources = [i["runner_path"] for i in compiled["_copy_plan"] if i["kind"] == "subject-source"]
            self.assertEqual(sources, ["sources/01-source-a.md", "sources/02-source-b.md"])

    def test_L8_legacy_disclosure_detection_is_unchanged(self):
        from tools.behavioral_harness_pair import _treatment_disclosed

        self.assertTrue(_treatment_disclosed("I used claim-verification for this answer.", "claim-verification"))
        self.assertTrue(_treatment_disclosed("see instructions/SKILL.md", "claim-verification"))
        self.assertFalse(_treatment_disclosed("The sources disagree about the retry delay.", "claim-verification"))


class CodeReviewGroundTruthModelTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "skill.md").write_text("# code-review\nRead the diff.\n", encoding="utf-8")
        (self.root / "requirements.md").write_text("AC-1: rate is 15 percent.\n", encoding="utf-8")
        (self.root / "base").mkdir()
        (self.root / "head").mkdir()
        (self.root / "base/app.py").write_text("def rate():\n    return 0.15\n", encoding="utf-8")
        (self.root / "head/app.py").write_text("def rate():\n    return 0.10\n", encoding="utf-8")
        self.experiment = code_review_experiment()
        self.write_diff()

    def tearDown(self):
        self.tmp.cleanup()

    def write_diff(self, experiment=None, target="change.diff"):
        from tools.behavioral_harness_pair import reconstruct_change_diff

        experiment = experiment or self.experiment
        case = experiment["cases"][0]
        (self.root / target).write_text(
            reconstruct_change_diff(case, case["ground_truth"], self.root), encoding="utf-8"
        )

    def experiment_file(self, experiment=None):
        path = self.root / "experiment.yml"
        path.write_text(yaml.safe_dump(experiment or self.experiment, sort_keys=False), encoding="utf-8")
        return path

    def load(self, experiment=None):
        return load_paired_experiment(self.experiment_file(experiment))

    def test_C1_code_review_experiment_loads_and_prepares(self):
        loaded = self.load()
        self.assertEqual(loaded["ground_truth_model"], "code-review-findings/v1")
        pair = compile_paired_case(loaded, "CR-T01", self.root, 1, "seed")
        out = self.root / "prepared"
        write_paired_case(pair, self.root, out)
        status = verify_paired_prepared(out)
        self.assertTrue(status["verified"])
        self.assertTrue(status["subject_source_parity"])

    def test_C2_new_roles_accepted_and_unknown_role_rejected(self):
        for role in ("tests", "ci-evidence", "implementation-report", "policy", "intentionally-incomplete"):
            with self.subTest(role=role):
                experiment = code_review_experiment()
                experiment["cases"][0]["fixtures"][0]["role"] = role
                # requirements fixture is not referenced by change_set, so the role may vary
                self.load(experiment)
        experiment = code_review_experiment()
        experiment["cases"][0]["fixtures"][0]["role"] = "authoritative-source"
        with self.assertRaisesRegex(HarnessError, "not a supported runner-visible"):
            self.load(experiment)

    def test_C3_runner_path_validation(self):
        bad = {
            "/abs/sources/x.md": "safe repository-relative",
            "sources/../x.md": "safe repository-relative",
            "elsewhere/x.md": "must live under sources/",
            "sources": "must live under sources/",
            "instructions/x.md": "must live under sources/",
            "sources/policy/x.md": "must not encode a judge role",
            "sources/baseline/x.md": "must not encode a judge role",
        }
        for value, message in bad.items():
            with self.subTest(runner_path=value):
                experiment = code_review_experiment()
                experiment["cases"][0]["fixtures"][0]["runner_path"] = value
                with self.assertRaisesRegex(HarnessError, message):
                    self.load(experiment)

    def test_C3b_duplicate_runner_path_rejected(self):
        experiment = code_review_experiment()
        experiment["cases"][0]["fixtures"][1]["runner_path"] = "sources/requirements.md"
        with self.assertRaisesRegex(HarnessError, "duplicate runner_path"):
            self.load(experiment)

    def test_C3c_declared_runner_paths_are_materialised_identically_in_both_arms(self):
        pair = compile_paired_case(self.load(), "CR-T01", self.root, 1, "seed")
        out = self.root / "prepared"
        write_paired_case(pair, self.root, out)
        arms = {}
        for response_dir in sorted((out / "responses").iterdir()):
            runner = response_dir / "runner-package"
            arms[response_dir.name] = sorted(
                str(p.relative_to(runner)) for p in runner.rglob("*") if p.is_file()
            )
        (first, second) = arms.values()
        subject_first = [p for p in first if p.startswith("sources/")]
        self.assertEqual(subject_first, [p for p in second if p.startswith("sources/")])
        self.assertEqual(
            subject_first,
            ["sources/base/app.py", "sources/change.diff", "sources/head/app.py", "sources/requirements.md"],
        )
        instructions = [p for arm in (first, second) for p in arm if p.startswith("instructions/")]
        self.assertEqual(instructions, ["instructions/skill.md"])

    def test_C4_change_set_added_and_deleted_are_valid(self):
        experiment = code_review_experiment()
        case = experiment["cases"][0]
        case["fixtures"].append({"path": "head/new.py", "role": "tests", "runner_path": "sources/head/new.py"})
        (self.root / "head/new.py").write_text("def t():\n    pass\n", encoding="utf-8")
        case["ground_truth"]["change_set"]["files"].append(
            {"logical_path": "new.py", "change_type": "added", "base_ref": None, "head_ref": "head/new.py"}
        )
        self.write_diff(experiment)
        loaded = self.load(experiment)
        compile_paired_case(loaded, "CR-T01", self.root, 1, "seed")
        self.assertIn("--- /dev/null", (self.root / "change.diff").read_text())

        experiment = code_review_experiment()
        case = experiment["cases"][0]
        case["fixtures"][2]["role"] = "base-code"
        case["fixtures"][2]["path"] = "base/gone.py"
        case["fixtures"][2]["runner_path"] = "sources/base/gone.py"
        (self.root / "base/gone.py").write_text("x = 1\n", encoding="utf-8")
        case["ground_truth"]["change_set"]["files"] = [
            {"logical_path": "gone.py", "change_type": "deleted", "base_ref": "base/gone.py", "head_ref": None}
        ]
        case["ground_truth"]["expected_findings"][0]["locations"][0]["fixture"] = "base/gone.py"
        self.write_diff(experiment)
        loaded = self.load(experiment)
        compile_paired_case(loaded, "CR-T01", self.root, 1, "seed")
        self.assertIn("+++ /dev/null", (self.root / "change.diff").read_text())

    def test_C5_change_set_nullability_and_role_errors(self):
        cases = {
            "must not carry base_ref": lambda c: c["ground_truth"]["change_set"]["files"][0].update(
                {"change_type": "added"}
            ),
            "must not carry head_ref": lambda c: c["ground_truth"]["change_set"]["files"][0].update(
                {"change_type": "deleted"}
            ),
        }
        for message, mutate in cases.items():
            with self.subTest(message=message):
                experiment = code_review_experiment()
                mutate(experiment["cases"][0])
                with self.assertRaisesRegex(HarnessError, message):
                    self.load(experiment)

        experiment = code_review_experiment()
        experiment["cases"][0]["ground_truth"]["change_set"]["files"][0]["base_ref"] = None
        with self.assertRaisesRegex(HarnessError, "base_ref must be a non-empty string"):
            self.load(experiment)

        experiment = code_review_experiment()
        experiment["cases"][0]["fixtures"][1]["role"] = "requirements"
        with self.assertRaisesRegex(HarnessError, "expected one of"):
            self.load(experiment)

        experiment = code_review_experiment()
        experiment["cases"][0]["ground_truth"]["change_set"]["files"][0]["head_ref"] = "requirements.md"
        with self.assertRaisesRegex(HarnessError, "expected one of"):
            self.load(experiment)

        experiment = code_review_experiment()
        experiment["cases"][0]["ground_truth"]["change_set"]["files"][0]["head_ref"] = "not-a-fixture.py"
        with self.assertRaisesRegex(HarnessError, "is not a fixture of this case"):
            self.load(experiment)

    def test_C6_stale_diff_is_rejected_at_prepare_time(self):
        loaded = self.load()
        (self.root / "change.diff").write_text("--- base/app.py\n+++ head/app.py\n@@ -1 +1 @@\n-x\n+y\n", encoding="utf-8")
        with self.assertRaisesRegex(HarnessError, "does not match the declared change set"):
            compile_paired_case(loaded, "CR-T01", self.root, 1, "seed")

    def test_C6b_extra_or_missing_diff_file_is_rejected(self):
        # a change-set entry whose file is absent from the committed diff
        experiment = code_review_experiment()
        case = experiment["cases"][0]
        (self.root / "head/extra.py").write_text("y = 2\n", encoding="utf-8")
        case["fixtures"].append({"path": "head/extra.py", "role": "changed-code", "runner_path": "sources/head/extra.py"})
        self.write_diff(experiment)  # diff written WITHOUT the extra file
        case["ground_truth"]["change_set"]["files"].append(
            {"logical_path": "extra.py", "change_type": "added", "base_ref": None, "head_ref": "head/extra.py"}
        )
        loaded = self.load(experiment)
        with self.assertRaisesRegex(HarnessError, "does not match the declared change set"):
            compile_paired_case(loaded, "CR-T01", self.root, 1, "seed")

    def test_C7_ground_truth_structural_errors(self):
        checks = [
            ("duplicate finding id", lambda c: c["ground_truth"]["forbidden_findings"][0].update({"finding_id": "CR-T01-F01"})),
            ("severity 'critical' must be one of", lambda c: c["ground_truth"]["expected_findings"][0].update({"severity": "critical"})),
            ("detection_criteria must be a non-empty list", lambda c: c["ground_truth"]["expected_findings"][0].update({"detection_criteria": []})),
            ("evidence must be a non-empty list", lambda c: c["ground_truth"]["expected_findings"][0].update({"evidence": []})),
            ("is not a fixture of this case", lambda c: c["ground_truth"]["expected_findings"][0]["locations"][0].update({"fixture": "nope.py"})),
            ("expected_status 'done' must be one of", lambda c: c["ground_truth"]["acceptance_criteria"][0].update({"expected_status": "done"})),
            ("expected_verdict 'shipped' must be one of", lambda c: c["ground_truth"]["release_calibration"].update({"expected_verdict": "shipped"})),
            ("must not also be forbidden", lambda c: c["ground_truth"]["release_calibration"].update({"forbidden_verdicts": ["not-approved"]})),
            ("severity_if_raised must be one of", lambda c: c["ground_truth"]["forbidden_findings"][0].update({"severity_if_raised": "bad"})),
            ("classification is not part of", lambda c: c["ground_truth"].update({"classification": {}})),
        ]
        for message, mutate in checks:
            with self.subTest(message=message):
                experiment = code_review_experiment()
                mutate(experiment["cases"][0])
                with self.assertRaisesRegex(HarnessError, message):
                    self.load(experiment)

    def test_C8_judge_contract_carries_policy_without_leaks(self):
        pair = compile_paired_case(self.load(), "CR-T01", self.root, 1, "seed")
        judge = pair["judge_contract"]
        self.assertEqual(judge["ground_truth_model"], "code-review-findings/v1")
        policy = judge["evaluation_policy"]
        self.assertEqual(
            [(r["order"], r["outcome"]) for r in policy["unlisted_finding_rule"]],
            [(1, "hard-failure"), (2, "false-positive"), (3, "ground_truth_incomplete / adjudication_required")],
        )
        self.assertIn("adjudication-required", policy["judge_scoring"]["per_finding"]["values"])
        self.assertEqual(policy["finding_scope"]["intended_ground_truth"], "exhaustive-for-review-significant-findings")
        instructions = " ".join(judge["instructions"])
        self.assertNotIn("classification alternatives", instructions)
        self.assertIn("detection criteria", instructions)
        self.assertNotIn("response_assignments", judge)
        self.assertNotIn("execution_order", judge)
        self.assertNotIn("treatment_disclosure", judge)
        # the coordinator keeps the disclosure configuration
        self.assertEqual(
            pair["control"]["treatment_disclosure"], {"allow_bare_target_skill_id_in_output": True}
        )

    def test_C9_domain_and_task_family_come_from_the_experiment(self):
        pair = compile_paired_case(self.load(), "CR-T01", self.root, 1, "seed")
        for treatment in ("baseline", "skill"):
            view = pair["compiled"][treatment]["judge_view"]
            self.assertEqual(view["domain"], "Programmieren")
            self.assertEqual(view["task_family"], "paired code review")


class DisclosureOptInTests(unittest.TestCase):
    """The bare target-skill id may be allowed; experimental context never is."""

    SKILL = "code-review"

    def test_D1_bare_domain_term_allowed_only_with_opt_in(self):
        from tools.behavioral_harness_pair import _treatment_disclosed

        text = "Blocker: die Berechtigungspruefung fehlt. Dieses Code-Review ist nicht freigegeben."
        self.assertTrue(_treatment_disclosed(text, self.SKILL))
        self.assertFalse(_treatment_disclosed(text, self.SKILL, allow_bare_target_skill_id=True))

    def test_D2_experimental_context_still_blocked_under_opt_in(self):
        from tools.behavioral_harness_pair import _treatment_disclosed

        blocked = [
            "Ich habe den code-review Skill verwendet.",
            "Ich habe code-review als Skill angewendet.",
            "Mir wurde code-review als Instruction gegeben.",
            "Ich habe die code-review Instruction gelesen.",
            "This is the code-review treatment.",
            "This is the code-review variant.",
            "This is the code-review condition.",
            "This is the code-review arm.",
            "This is the code-review group.",
            "See instructions/SKILL.md for details.",
            "See instructions/anything.md for details.",
            "Programmieren/Skills/code-review/SKILL.md was provided.",
            "I read SKILL.md before answering.",
            "I was given the skill.",
            "This is a with-vs-without comparison.",
        ]
        for text in blocked:
            with self.subTest(text=text):
                self.assertTrue(
                    _treatment_disclosed(text, self.SKILL, allow_bare_target_skill_id=True),
                    f"should still be a disclosure: {text}",
                )

    def test_D3_ordinary_review_prose_passes_under_opt_in(self):
        from tools.behavioral_harness_pair import _treatment_disclosed

        allowed = [
            "Der Test unterscheidet last_seen nicht von created_at.",
            "Compared to the base version, the head skips validation.",
            "Dieses Code-Review kann nicht freigegeben werden.",
            "The code review found two blockers.",
        ]
        for text in allowed:
            with self.subTest(text=text):
                self.assertFalse(_treatment_disclosed(text, self.SKILL, allow_bare_target_skill_id=True))


class CodeReviewExperimentContractTests(unittest.TestCase):
    """The real, committed code-review-v1 manifest must load and prepare."""

    ROOT = Path(__file__).resolve().parents[1]
    EXPERIMENT = ROOT / "Evals/Behavioral-Harness/experiments/code-review-v1/experiment.yml"

    def test_E1_real_experiment_loads_with_six_cases(self):
        experiment = load_paired_experiment(self.EXPERIMENT)
        self.assertEqual(experiment["experiment_id"], "code-review-v1")
        self.assertEqual(experiment["ground_truth_model"], "code-review-findings/v1")
        self.assertEqual(len(experiment["cases"]), 6)
        self.assertNotIn("shared_user_prompt", experiment)
        prompts = {str(case["user_prompt"]).strip() for case in experiment["cases"]}
        self.assertEqual(len(prompts), 1, "all cases share the one neutralised prompt")

    def test_E2_every_real_case_prepares_and_verifies(self):
        experiment = load_paired_experiment(self.EXPERIMENT)
        with tempfile.TemporaryDirectory() as tmp:
            for case in experiment["cases"]:
                case_id = str(case["case_id"])
                with self.subTest(case=case_id):
                    pair = compile_paired_case(experiment, case_id, self.ROOT, 1, "b1-contract-seed")
                    out = Path(tmp) / case_id
                    write_paired_case(pair, self.ROOT, out)
                    status = verify_paired_prepared(out)
                    self.assertTrue(status["verified"])
                    self.assertEqual(status["response_count"], 2)
                    self.assertTrue(status["subject_source_parity"])
                    self.assertTrue(status["treatment_mapping_hidden_from_judge_contract"])


class CodeReviewEvaluationPolicyTests(unittest.TestCase):
    """The precommitted judge policy must be frozen before execution, not defaulted."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "skill.md").write_text("# code-review\n", encoding="utf-8")
        (self.root / "requirements.md").write_text("AC-1: rate is 15 percent.\n", encoding="utf-8")
        (self.root / "base").mkdir()
        (self.root / "head").mkdir()
        (self.root / "base/app.py").write_text("def rate():\n    return 0.15\n", encoding="utf-8")
        (self.root / "head/app.py").write_text("def rate():\n    return 0.10\n", encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def load(self, experiment):
        from tools.behavioral_harness_pair import reconstruct_change_diff

        case = experiment["cases"][0]
        (self.root / "change.diff").write_text(
            reconstruct_change_diff(case, case["ground_truth"], self.root), encoding="utf-8"
        )
        path = self.root / "experiment.yml"
        path.write_text(yaml.safe_dump(experiment, sort_keys=False), encoding="utf-8")
        return load_paired_experiment(path)

    def test_A1_missing_policy_blocks_are_rejected(self):
        for key in ("finding_scope", "unlisted_finding_rule", "judge_scoring"):
            with self.subTest(missing=key):
                experiment = code_review_experiment()
                del experiment[key]
                with self.assertRaises(HarnessError):
                    self.load(experiment)

    def test_A2_finding_scope_value_is_frozen(self):
        experiment = code_review_experiment()
        experiment["finding_scope"]["intended_ground_truth"] = "some-subset"
        with self.assertRaisesRegex(HarnessError, "intended_ground_truth must be"):
            self.load(experiment)

    def test_A3_unlisted_rule_precedence_is_frozen(self):
        checks = [
            ("must have outcome 'hard-failure'", lambda r: r[0].update({"outcome": "false-positive"})),
            ("must have outcome 'false-positive'", lambda r: r[1].update({"outcome": "hard-failure"})),
            ("exactly 3 rules", lambda r: r.pop()),
            ("must have outcome", lambda r: (r[0].update({"order": 2}), r[1].update({"order": 1}))),
        ]
        for message, mutate in checks:
            with self.subTest(message=message):
                experiment = code_review_experiment()
                mutate(experiment["unlisted_finding_rule"])
                with self.assertRaisesRegex(HarnessError, message):
                    self.load(experiment)

    def test_A3b_swapped_orders_are_rejected_even_when_outcomes_move_with_them(self):
        experiment = code_review_experiment()
        rules = experiment["unlisted_finding_rule"]
        rules[0]["order"], rules[1]["order"] = 2, 1
        with self.assertRaisesRegex(HarnessError, "must have outcome"):
            self.load(experiment)

    def test_A4_adjudication_handling_is_required(self):
        experiment = code_review_experiment()
        del experiment["unlisted_finding_rule"][2]["handling"]
        with self.assertRaisesRegex(HarnessError, "must carry handling"):
            self.load(experiment)
        for dropped in ("reward", "penalty", "closed"):
            with self.subTest(dropped=dropped):
                experiment = code_review_experiment()
                rule = experiment["unlisted_finding_rule"][2]
                rule["handling"] = [h for h in rule["handling"] if dropped not in h]
                with self.assertRaisesRegex(HarnessError, "must be exactly the frozen statements"):
                    self.load(experiment)

    def test_A5_scoring_vocabularies_are_frozen(self):
        experiment = code_review_experiment()
        experiment["judge_scoring"]["per_finding"]["values"] = ["hit", "miss", "false-positive", "hard-failure"]
        with self.assertRaisesRegex(HarnessError, "per_finding.values must be exactly"):
            self.load(experiment)

        experiment = code_review_experiment()
        experiment["judge_scoring"]["per_dimension"]["values"] = ["pass", "fail"]
        with self.assertRaisesRegex(HarnessError, "per_dimension.values must be exactly"):
            self.load(experiment)

    def test_A6_forbidden_scoring_concepts_are_required(self):
        for dropped in ("aggregate", "weighted", "ranking", "single number"):
            with self.subTest(dropped=dropped):
                experiment = code_review_experiment()
                experiment["judge_scoring"]["forbidden"] = [
                    f for f in experiment["judge_scoring"]["forbidden"] if dropped not in f
                ]
                with self.assertRaisesRegex(HarnessError, "must be exactly the frozen statements"):
                    self.load(experiment)

    def test_A7_judge_contract_never_falls_back_to_empty_policy(self):
        from tools.behavioral_harness_pair import _validate_code_review_evaluation_policy

        experiment = code_review_experiment()
        loaded = self.load(experiment)
        del loaded["judge_scoring"]
        with self.assertRaises(HarnessError):
            _validate_code_review_evaluation_policy(loaded)
        with self.assertRaises(HarnessError):
            compile_paired_case(loaded, "CR-T01", self.root, 1, "seed")

    def test_A8_positive_control_real_experiment_still_loads(self):
        root = Path(__file__).resolve().parents[1]
        experiment = load_paired_experiment(root / "Evals/Behavioral-Harness/experiments/code-review-v1/experiment.yml")
        self.assertEqual(experiment["finding_scope"]["intended_ground_truth"], "exhaustive-for-review-significant-findings")
        self.assertEqual(len(experiment["unlisted_finding_rule"]), 3)

    def test_A9_legacy_experiment_needs_no_policy(self):
        # classification/v1 must not acquire the new requirement
        experiment = synthetic_experiment()
        self.assertNotIn("finding_scope", experiment)
        path = self.root / "legacy.yml"
        path.write_text(yaml.safe_dump(experiment, sort_keys=False), encoding="utf-8")
        (self.root / "source-a.md").write_text("A\n", encoding="utf-8")
        (self.root / "source-b.md").write_text("B\n", encoding="utf-8")
        load_paired_experiment(path)


class DisclosureOptInBooleanTests(unittest.TestCase):
    """Truthiness must not be able to enable a blindness relaxation by typo."""

    def test_B1_real_booleans_are_accepted(self):
        from tools.behavioral_harness_pair import _disclosure_opt_in

        for value in (True, False):
            with self.subTest(value=value):
                self.assertEqual(
                    _disclosure_opt_in({"treatment_disclosure": {"allow_bare_target_skill_id_in_output": value}}),
                    {"allow_bare_target_skill_id_in_output": value},
                )

    def test_B2_absent_block_stays_absent(self):
        from tools.behavioral_harness_pair import _disclosure_opt_in

        self.assertIsNone(_disclosure_opt_in({}))

    def test_B3_present_block_without_the_flag_defaults_to_false(self):
        from tools.behavioral_harness_pair import _disclosure_opt_in

        self.assertEqual(
            _disclosure_opt_in({"treatment_disclosure": {"note": "x"}}),
            {"allow_bare_target_skill_id_in_output": False},
        )

    def test_B4_non_boolean_values_are_rejected(self):
        from tools.behavioral_harness_pair import _disclosure_opt_in

        for value in ("false", "true", 0, 1, None, [], {}):
            with self.subTest(value=value):
                with self.assertRaisesRegex(HarnessError, "must be a boolean"):
                    _disclosure_opt_in({"treatment_disclosure": {"allow_bare_target_skill_id_in_output": value}})

    def test_B5_string_false_is_rejected_at_experiment_load(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "source-a.md").write_text("A\n", encoding="utf-8")
            (root / "source-b.md").write_text("B\n", encoding="utf-8")
            experiment = synthetic_experiment()
            experiment["treatment_disclosure"] = {"allow_bare_target_skill_id_in_output": "false"}
            path = root / "experiment.yml"
            path.write_text(yaml.safe_dump(experiment, sort_keys=False), encoding="utf-8")
            with self.assertRaisesRegex(HarnessError, "must be a boolean"):
                load_paired_experiment(path)


class DisclosurePhrasingTests(unittest.TestCase):
    """Hyphenated and reversed skill-instruction context must stay blocked."""

    SKILL = "code-review"

    BLOCKED = [
        "Ich habe den Code-Review-Skill verwendet.",
        "Ich habe die Code-Review-Instruction gelesen.",
        "This was the code-review-treatment.",
        "This was the code-review-variant.",
        "This was the code-review-condition.",
        "The skill code-review was provided to me.",
        "The instruction code-review was provided.",
    ]
    ALLOWED = [
        "Dieses Code-Review ist nicht freigegeben.",
        "The code review found two blockers.",
        "Beim Code-Review fehlt eine Autorisierungspruefung.",
    ]

    def test_F1_hyphenated_and_reversed_forms_are_predicate_blocked(self):
        from tools.behavioral_harness_pair import _treatment_disclosed

        for text in self.BLOCKED:
            with self.subTest(text=text):
                self.assertTrue(_treatment_disclosed(text, self.SKILL, allow_bare_target_skill_id=True))

    def test_F2_ordinary_review_prose_is_not_blocked(self):
        from tools.behavioral_harness_pair import _treatment_disclosed

        for text in self.ALLOWED:
            with self.subTest(text=text):
                self.assertFalse(_treatment_disclosed(text, self.SKILL, allow_bare_target_skill_id=True))

    def test_F3_end_to_end_blind_packaging(self):
        """Blocked forms are refused end to end; ordinary review prose really packages."""
        experiment = code_review_experiment()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "skill.md").write_text("# code-review\n", encoding="utf-8")
            (root / "requirements.md").write_text("AC-1: rate is 15 percent.\n", encoding="utf-8")
            (root / "base").mkdir()
            (root / "head").mkdir()
            (root / "base/app.py").write_text("def rate():\n    return 0.15\n", encoding="utf-8")
            (root / "head/app.py").write_text("def rate():\n    return 0.10\n", encoding="utf-8")
            from tools.behavioral_harness_pair import reconstruct_change_diff

            case = experiment["cases"][0]
            (root / "change.diff").write_text(
                reconstruct_change_diff(case, case["ground_truth"], root), encoding="utf-8"
            )
            path = root / "experiment.yml"
            path.write_text(yaml.safe_dump(experiment, sort_keys=False), encoding="utf-8")
            loaded = load_paired_experiment(path)

            pair = compile_paired_case(loaded, "CR-T01", root, 1, "seed")
            prepared = root / "prepared"
            write_paired_case(pair, root, prepared)
            response_ids = sorted(load_yaml(prepared / "control.yml")["response_assignments"])

            for index, text in enumerate(self.BLOCKED + self.ALLOWED):
                with self.subTest(text=text):
                    output = root / f"out-{index}.md"
                    output.write_text(text + "\n", encoding="utf-8")
                    run_dirs = [
                        package_run(
                            prepared / "responses" / response_id,
                            output if order == 1 else None,
                            None, None, None,
                            root / f"runs-{index}", f"run-{index}-{order}",
                            runner_type="synthetic", runner_model="m",
                            runner_session_id=f"s-{index}-{order}",
                            started_at="unknown", finished_at="unknown",
                        )
                        for order, response_id in enumerate(response_ids, start=1)
                    ]
                    out = root / f"blind-{index}"
                    if text in self.BLOCKED:
                        with self.assertRaises(HarnessError):
                            package_blind_pair(prepared, run_dirs, out)
                    else:
                        package_blind_pair(prepared, run_dirs, out)
                        self.assertTrue((out / "blind-judge-input.yml").is_file())


class PolicySemanticFreezeTests(unittest.TestCase):
    """Token presence does not prove the committed semantics; the statements are frozen."""

    CANONICAL_HANDLING = [
        "no spontaneous reward",
        "no spontaneous penalty",
        "the affected pair comparison must not be closed until the ground-truth gap has been handled independently",
    ]
    CANONICAL_FORBIDDEN = [
        "aggregate total score",
        "weighted score",
        "ranking",
        "any single number standing in for the review",
    ]

    def policy(self, experiment):
        from tools.behavioral_harness_pair import _validate_code_review_evaluation_policy

        _validate_code_review_evaluation_policy(experiment)

    def test_S1_canonical_policy_is_accepted(self):
        experiment = code_review_experiment()
        experiment["unlisted_finding_rule"][2]["handling"] = list(self.CANONICAL_HANDLING)
        experiment["judge_scoring"]["forbidden"] = list(self.CANONICAL_FORBIDDEN)
        self.policy(experiment)

    def test_S2_inverted_handling_statements_are_rejected(self):
        inversions = [
            "spontaneous reward is allowed",
            "spontaneous penalty is encouraged",
            "the affected pair comparison must not be closed until lunch",
        ]
        for index, inverted in enumerate(inversions):
            with self.subTest(inverted=inverted):
                experiment = code_review_experiment()
                handling = list(self.CANONICAL_HANDLING)
                handling[index] = inverted
                experiment["unlisted_finding_rule"][2]["handling"] = handling
                with self.assertRaisesRegex(HarnessError, "must be exactly the frozen statements"):
                    self.policy(experiment)

    def test_S3_bare_tokens_do_not_satisfy_the_handling_freeze(self):
        experiment = code_review_experiment()
        experiment["unlisted_finding_rule"][2]["handling"] = ["reward", "penalty", "must not be closed"]
        with self.assertRaisesRegex(HarnessError, "must be exactly the frozen statements"):
            self.policy(experiment)

    def test_S4_handling_normalisation_is_tolerated(self):
        experiment = code_review_experiment()
        experiment["unlisted_finding_rule"][2]["handling"] = [
            "  No   Spontaneous Reward ",
            "NO SPONTANEOUS PENALTY",
            "The Affected  Pair Comparison Must Not Be Closed Until The Ground-Truth Gap Has Been Handled Independently",
        ]
        self.policy(experiment)

    def test_S5_extra_or_missing_handling_statement_is_rejected(self):
        experiment = code_review_experiment()
        experiment["unlisted_finding_rule"][2]["handling"] = self.CANONICAL_HANDLING + ["and anything else goes"]
        with self.assertRaisesRegex(HarnessError, "unexpected="):
            self.policy(experiment)

        experiment = code_review_experiment()
        experiment["unlisted_finding_rule"][2]["handling"] = self.CANONICAL_HANDLING[:2]
        with self.assertRaisesRegex(HarnessError, "missing="):
            self.policy(experiment)

    def test_S6_inverted_forbidden_scoring_is_rejected(self):
        inversions = [
            "aggregate scores are encouraged",
            "weighted scores are preferred",
            "ranking is required",
            "a single number should represent the review",
        ]
        for index, inverted in enumerate(inversions):
            with self.subTest(inverted=inverted):
                experiment = code_review_experiment()
                forbidden = list(self.CANONICAL_FORBIDDEN)
                forbidden[index] = inverted
                experiment["judge_scoring"]["forbidden"] = forbidden
                with self.assertRaisesRegex(HarnessError, "must be exactly the frozen statements"):
                    self.policy(experiment)

    def test_S7_all_four_inversions_at_once_are_rejected(self):
        experiment = code_review_experiment()
        experiment["judge_scoring"]["forbidden"] = [
            "aggregate scores are encouraged",
            "weighted scores are preferred",
            "ranking is required",
            "a single number should represent the review",
        ]
        with self.assertRaisesRegex(HarnessError, "must be exactly the frozen statements"):
            self.policy(experiment)

    def test_S8_forbidden_normalisation_is_tolerated(self):
        experiment = code_review_experiment()
        experiment["judge_scoring"]["forbidden"] = [
            "Aggregate  Total Score",
            "WEIGHTED SCORE",
            " ranking ",
            "Any Single Number Standing In For The Review",
        ]
        self.policy(experiment)

    def test_S9_rule_order_must_be_a_plain_integer(self):
        for value in (True, False, "1", 1.0):
            with self.subTest(order=value):
                experiment = code_review_experiment()
                experiment["unlisted_finding_rule"][0]["order"] = value
                with self.assertRaisesRegex(HarnessError, "must be a plain integer"):
                    self.policy(experiment)

    def test_S10_integer_orders_remain_valid(self):
        experiment = code_review_experiment()
        self.assertEqual([r["order"] for r in experiment["unlisted_finding_rule"]], [1, 2, 3])
        self.policy(experiment)

    def test_S11_real_experiment_carries_the_frozen_statements(self):
        from tools.behavioral_harness_pair import FORBIDDEN_SCORING, UNLISTED_RULE_3_HANDLING, _normalized_statements

        root = Path(__file__).resolve().parents[1]
        experiment = load_paired_experiment(root / "Evals/Behavioral-Harness/experiments/code-review-v1/experiment.yml")
        rule3 = next(r for r in experiment["unlisted_finding_rule"] if r["order"] == 3)
        self.assertEqual(_normalized_statements(rule3["handling"]), set(UNLISTED_RULE_3_HANDLING))
        self.assertEqual(_normalized_statements(experiment["judge_scoring"]["forbidden"]), set(FORBIDDEN_SCORING))


if __name__ == "__main__":
    unittest.main()
