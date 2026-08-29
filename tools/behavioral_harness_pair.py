#!/usr/bin/env python3
"""Thin paired-experiment orchestration for the existing KI-Regeln behavioral harness.

This module does not define a second run/telemetry framework. It reuses the
existing behavioral_harness compile, prepared-case, run-package and integrity
contracts and adds only paired preparation plus treatment-blind judge packaging.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import shutil
from pathlib import Path
from typing import Any

try:
    from .behavioral_harness import (
        HarnessError,
        assert_runner_package_clean,
        compile_case,
        dump_yaml,
        hash_file,
        hash_object,
        load_yaml,
        verify_prepared_integrity,
        verify_run_package,
        write_prepared_case,
    )
except ImportError:  # direct execution: python tools/behavioral_harness_pair.py
    from behavioral_harness import (
        HarnessError,
        assert_runner_package_clean,
        compile_case,
        dump_yaml,
        hash_file,
        hash_object,
        load_yaml,
        verify_prepared_integrity,
        verify_run_package,
        write_prepared_case,
    )

PAIR_CONTRACT = "behavioral-paired-skill-eval/v1"
CONTROL_CONTRACT = "behavioral-paired-control/v1"
BLIND_JUDGE_CONTRACT = "behavioral-paired-blind-judge/v1"
BLIND_INPUT_CONTRACT = "behavioral-paired-blind-input/v1"
TREATMENTS = ("baseline", "skill")


def _safe_rel(raw: str, label: str) -> Path:
    path = Path(raw)
    if path.is_absolute() or ".." in path.parts or not raw.strip():
        raise HarnessError(f"{label} must be a safe repository-relative path: {raw!r}")
    return path


def load_paired_experiment(path: Path) -> dict[str, Any]:
    data = load_yaml(path)
    if not isinstance(data, dict):
        raise HarnessError("paired experiment must be a mapping")
    if data.get("contract") != PAIR_CONTRACT:
        raise HarnessError(f"paired experiment contract must be {PAIR_CONTRACT}")
    for key in ("experiment_id", "repository", "pinned_commit", "target_skill", "evaluation_dimensions", "cases"):
        if key not in data:
            raise HarnessError(f"paired experiment missing {key}")
    target = data.get("target_skill")
    if not isinstance(target, dict) or not target.get("id") or not target.get("path"):
        raise HarnessError("target_skill must contain id and path")
    _safe_rel(str(target["path"]), "target_skill.path")
    dimensions = data.get("evaluation_dimensions")
    if not isinstance(dimensions, list) or not dimensions:
        raise HarnessError("evaluation_dimensions must be a non-empty list")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        raise HarnessError("paired experiment cases must be a non-empty list")
    seen: set[str] = set()
    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            raise HarnessError(f"case[{index}] must be a mapping")
        for key in ("case_id", "user_prompt", "fixtures", "ground_truth"):
            if key not in case:
                raise HarnessError(f"case[{index}] missing {key}")
        case_id = str(case["case_id"])
        if case_id in seen:
            raise HarnessError(f"duplicate paired case id {case_id}")
        seen.add(case_id)
        if not str(case["user_prompt"]).strip():
            raise HarnessError(f"{case_id}: user_prompt must not be empty")
        fixtures = case.get("fixtures")
        if not isinstance(fixtures, list) or not fixtures:
            raise HarnessError(f"{case_id}: fixtures must be a non-empty list")
        for raw in fixtures:
            _safe_rel(str(raw), f"{case_id}.fixture")
        truth = case.get("ground_truth")
        if not isinstance(truth, dict):
            raise HarnessError(f"{case_id}: ground_truth must be a mapping")
        for key in (
            "expected_classification",
            "relevant_evidence",
            "decisive_reason",
            "known_traps",
            "allowed_uncertainty",
            "hard_failures",
        ):
            if key not in truth:
                raise HarnessError(f"{case_id}: ground_truth missing {key}")
    repetitions = int(data.get("recommended_repetitions", 1))
    if repetitions < 2:
        raise HarnessError("recommended_repetitions must be at least 2 for a paired stochastic pilot")
    return data


def _get_case(experiment: dict[str, Any], case_id: str) -> dict[str, Any]:
    matches = [case for case in experiment["cases"] if str(case.get("case_id")) == case_id]
    if len(matches) != 1:
        raise HarnessError(f"expected exactly one paired case {case_id}, found {len(matches)}")
    return copy.deepcopy(matches[0])


def _opaque_response_id(experiment_id: str, case_id: str, repetition: int, treatment: str, blind_seed: str) -> str:
    payload = f"{experiment_id}|{case_id}|{repetition}|{treatment}|{blind_seed}".encode("utf-8")
    return "R-" + hashlib.sha256(payload).hexdigest()[:16]


def _synthetic_matrix(
    experiment: dict[str, Any],
    case: dict[str, Any],
    response_id: str,
    treatment: str,
) -> dict[str, Any]:
    target = str(experiment["target_skill"]["id"])
    skill_path = str(experiment["target_skill"]["path"])
    fixtures = [str(x) for x in case["fixtures"]]
    if treatment == "skill":
        fixtures.append(skill_path)
        primary = target
        forbidden: list[str] = []
    else:
        primary = "none/direct-response"
        forbidden = [target]
    truth = case["ground_truth"]
    return {
        "schema_version": 1,
        "repository": str(experiment["repository"]),
        "pinned_commit": str(experiment["pinned_commit"]),
        "tests": [
            {
                "test_id": response_id,
                "domain": "Recherche",
                "aufgabenfamilie": "paired claim verification",
                "testebenen": ["behavior", "outcome"],
                "schwierigkeit": case.get("difficulty", "mittel"),
                "nutzerprompt": case["user_prompt"],
                "fixtures": fixtures,
                "erwarteter_primaerskill": primary,
                "erlaubte_secondary_skills": [],
                "verbotene_skills": forbidden,
                "erwarteter_workflow": "none",
                "erwartete_evidence": ["use only package-local source fixtures"],
                "erwarteter_status": "pass",
                "output_kriterien": [str(item.get("id", item)) if isinstance(item, dict) else str(item) for item in experiment["evaluation_dimensions"]],
                "failure_modes": [str(x) for x in truth.get("hard_failures", [])],
                "routing_kriterien": [
                    "target skill is available only in the skill treatment" if treatment == "skill" else "target skill must remain unavailable in the baseline treatment"
                ],
                "bewertungsmethode": "paired treatment-blind judge against precommitted ground truth",
                "blindness_klasse": "paired-treatment-blind",
            }
        ],
    }


def _role_overrides(response_id: str, case: dict[str, Any], skill_path: str, treatment: str) -> dict[str, Any]:
    case_roles: dict[str, Any] = {
        str(path): {"role": "authoritative-source", "intentionally_missing_evidence": []}
        for path in case["fixtures"]
    }
    if treatment == "skill":
        case_roles[skill_path] = {"role": "skill-instruction", "intentionally_missing_evidence": []}
    return {"cases": {response_id: case_roles}}


def _recompute_hashes(compiled: dict[str, Any]) -> None:
    compiled["hashes"]["execution_view_hash"] = hash_object(compiled["execution_view"])
    compiled["hashes"]["judge_view_hash"] = hash_object(compiled["judge_view"])


def _prepare_compiled_variant(
    experiment: dict[str, Any],
    case: dict[str, Any],
    response_id: str,
    treatment: str,
    repo_root: Path,
) -> dict[str, Any]:
    target = str(experiment["target_skill"]["id"])
    skill_path = str(experiment["target_skill"]["path"])
    matrix = _synthetic_matrix(experiment, case, response_id, treatment)
    compiled = compile_case(
        matrix,
        response_id,
        repo_root,
        repo_commit=str(experiment["pinned_commit"]),
        role_overrides=_role_overrides(response_id, case, skill_path, treatment),
    )

    copy_plan: list[dict[str, str]] = []
    common_index = 0
    for exec_rec, judge_rec in zip(compiled["execution_view"]["fixtures"], compiled["judge_view"]["fixtures"]):
        original = str(judge_rec["path"])
        if original == skill_path:
            runner_rel = f"instructions/{Path(skill_path).name}"
            kind = "skill-instruction"
        else:
            common_index += 1
            runner_rel = f"sources/{common_index:02d}-{Path(original).name}"
            kind = "subject-source"
        exec_rec["path"] = runner_rel
        copy_plan.append({"source": original, "runner_path": runner_rel, "kind": kind, "fixture_id": str(exec_rec["fixture_id"])})

    compiled["execution_view"]["runtime"] = {
        "fresh_runner_context_required": True,
        "allowed_tools": "package-read-only",
        "network_access": False,
        "repository_access": False,
        "source_root": "sources",
        "skill_instruction": f"instructions/{Path(skill_path).name}" if treatment == "skill" else None,
        "runner_adapter_required": True,
    }
    compiled["judge_view"].update(
        {
            "experiment_id": str(experiment["experiment_id"]),
            "paired_case_id": str(case["case_id"]),
            "treatment": treatment,
        }
    )
    compiled["readiness"].update(
        {
            "package_only_sources": True,
            "network_disabled_by_contract": True,
            "repository_access_disabled_by_contract": True,
        }
    )
    compiled["_copy_plan"] = copy_plan
    compiled["_treatment"] = treatment
    compiled["_target_skill"] = target
    _recompute_hashes(compiled)
    return compiled


def compile_paired_case(
    experiment: dict[str, Any],
    case_id: str,
    repo_root: Path,
    repetition: int,
    blind_seed: str,
) -> dict[str, Any]:
    if repetition < 1:
        raise HarnessError("repetition must be >= 1")
    if not blind_seed:
        raise HarnessError("blind_seed must not be empty")
    case = _get_case(experiment, case_id)
    response_ids = {
        treatment: _opaque_response_id(str(experiment["experiment_id"]), case_id, repetition, treatment, blind_seed)
        for treatment in TREATMENTS
    }
    if len(set(response_ids.values())) != 2:
        raise HarnessError("opaque response id collision")

    compiled = {
        treatment: _prepare_compiled_variant(experiment, case, response_ids[treatment], treatment, repo_root)
        for treatment in TREATMENTS
    }

    prompt_hashes = {hash_object(compiled[t]["execution_view"]["user_prompt"]) for t in TREATMENTS}
    if len(prompt_hashes) != 1:
        raise HarnessError("paired variants do not have identical user prompts")

    source_hashes: dict[str, str] | None = None
    for treatment in TREATMENTS:
        current = {
            item["runner_path"]: compiled[treatment]["hashes"]["fixture_hashes"][item["fixture_id"]]
            for item in compiled[treatment]["_copy_plan"]
            if item["kind"] == "subject-source"
        }
        if source_hashes is None:
            source_hashes = current
        elif current != source_hashes:
            raise HarnessError("paired variants do not have identical subject-source hashes")

    target_skill_path = repo_root / _safe_rel(str(experiment["target_skill"]["path"]), "target_skill.path")
    if not target_skill_path.is_file():
        raise HarnessError(f"target skill missing at {target_skill_path}")

    control = {
        "schema_version": 1,
        "contract": CONTROL_CONTRACT,
        "experiment_id": str(experiment["experiment_id"]),
        "case_id": case_id,
        "repetition": repetition,
        "blind_seed": blind_seed,
        "blind_seed_hash": hash_object(blind_seed),
        "target_skill": str(experiment["target_skill"]["id"]),
        "target_skill_path": str(experiment["target_skill"]["path"]),
        "target_skill_hash": hash_file(target_skill_path),
        "response_assignments": {response_ids[t]: t for t in TREATMENTS},
        "shared_user_prompt_hash": next(iter(prompt_hashes)),
        "shared_subject_source_hashes": source_hashes or {},
        "independent_variable": "availability of the target skill instruction only",
    }
    judge_contract = {
        "schema_version": 1,
        "contract": BLIND_JUDGE_CONTRACT,
        "experiment_id": str(experiment["experiment_id"]),
        "case_id": case_id,
        "response_ids": sorted(response_ids.values()),
        "ground_truth": copy.deepcopy(case["ground_truth"]),
        "evaluation_dimensions": copy.deepcopy(experiment["evaluation_dimensions"]),
        "global_hard_failures": copy.deepcopy(experiment.get("global_hard_failures", [])),
        "instructions": [
            "Judge each response independently against the precommitted ground truth before comparing them.",
            "Do not infer treatment from style or verbosity.",
            "Report dimensions separately; do not collapse them into an opaque total score.",
            "Flag any hard failure independently of prose quality.",
        ],
    }
    return {"control": control, "judge_contract": judge_contract, "compiled": compiled}


def write_paired_case(pair: dict[str, Any], repo_root: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=False)
    dump_yaml(pair["control"], out_dir / "control.yml")
    dump_yaml(pair["judge_contract"], out_dir / "judge-contract.yml")

    for treatment in TREATMENTS:
        compiled = pair["compiled"][treatment]
        response_id = str(compiled["execution_view"]["test_id"])
        response_dir = out_dir / "responses" / response_id
        write_prepared_case(compiled, response_dir)
        runner_dir = response_dir / "runner-package"
        for item in compiled["_copy_plan"]:
            src = repo_root / _safe_rel(item["source"], "copy source")
            dst = runner_dir / item["runner_path"]
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

        adapter_path = runner_dir / "adapter-request.yml"
        adapter = load_yaml(adapter_path)
        if not isinstance(adapter, dict):
            raise HarnessError(f"invalid adapter request at {adapter_path}")
        adapter["constraints"] = {
            "network_access": False,
            "repository_access": False,
            "readable_roots": ["sources"] + (["instructions"] if treatment == "skill" else []),
            "same_model_and_configuration_across_pair_required": True,
        }
        adapter.setdefault("rules", []).extend(
            [
                "Use only files inside this runner package; do not access the repository or the web.",
                "Do not mention the experiment treatment, baseline/skill condition, or skill file name in the answer.",
                "Use a fresh isolated runner context for this response.",
            ]
        )
        dump_yaml(adapter, adapter_path)
        assert_runner_package_clean(runner_dir)

    pair_hashes = {
        "hash_algorithm": "sha256/canonical-json-v1",
        "control_hash": hash_object(pair["control"]),
        "judge_contract_hash": hash_object(pair["judge_contract"]),
        "response_prepared_hashes": {
            str(pair["compiled"][t]["execution_view"]["test_id"]): hash_object(pair["compiled"][t]["hashes"])
            for t in TREATMENTS
        },
    }
    dump_yaml(pair_hashes, out_dir / "pair-hashes.yml")
    verify_paired_prepared(out_dir)


def verify_paired_prepared(pair_dir: Path) -> dict[str, Any]:
    control = load_yaml(pair_dir / "control.yml")
    judge_contract = load_yaml(pair_dir / "judge-contract.yml")
    pair_hashes = load_yaml(pair_dir / "pair-hashes.yml")
    if not all(isinstance(x, dict) for x in (control, judge_contract, pair_hashes)):
        raise HarnessError("paired control/judge/hash documents must be mappings")
    if control.get("contract") != CONTROL_CONTRACT or judge_contract.get("contract") != BLIND_JUDGE_CONTRACT:
        raise HarnessError("paired contract mismatch")
    if hash_object(control) != pair_hashes.get("control_hash"):
        raise HarnessError("paired control hash mismatch")
    if hash_object(judge_contract) != pair_hashes.get("judge_contract_hash"):
        raise HarnessError("paired judge contract hash mismatch")

    assignments = control.get("response_assignments")
    if not isinstance(assignments, dict) or set(assignments.values()) != set(TREATMENTS) or len(assignments) != 2:
        raise HarnessError("paired response assignments must contain exactly baseline and skill")
    if set(judge_contract.get("response_ids", [])) != set(assignments):
        raise HarnessError("blind judge response ids do not match control assignments")

    compiled_views: dict[str, dict[str, Any]] = {}
    common_hashes: dict[str, str] | None = None
    for response_id, treatment in assignments.items():
        response_dir = pair_dir / "responses" / response_id
        prepared = verify_prepared_integrity(response_dir)
        compiled_views[treatment] = prepared
        if prepared["execution"].get("user_prompt") is None:
            raise HarnessError(f"{response_id}: missing user prompt")
        runner_dir = response_dir / "runner-package"
        runtime = prepared["execution"].get("runtime") or {}
        if runtime.get("network_access") is not False or runtime.get("repository_access") is not False:
            raise HarnessError(f"{response_id}: package-only runtime constraints missing")
        source_map: dict[str, str] = {}
        for record in prepared["execution"].get("fixtures", []):
            rel = _safe_rel(str(record["path"]), "runner fixture path")
            actual = runner_dir / rel
            if not actual.is_file():
                raise HarnessError(f"{response_id}: runner fixture missing: {rel}")
            if hash_file(actual) != record.get("hash"):
                raise HarnessError(f"{response_id}: runner fixture hash mismatch: {rel}")
            if str(rel).startswith("sources/"):
                source_map[str(rel)] = str(record["hash"])
        if common_hashes is None:
            common_hashes = source_map
        elif source_map != common_hashes:
            raise HarnessError("paired runner packages differ in subject-source content")
        instruction_files = [p for p in (runner_dir / "instructions").glob("*") if p.is_file()] if (runner_dir / "instructions").exists() else []
        if treatment == "baseline" and instruction_files:
            raise HarnessError("baseline runner package unexpectedly contains skill instructions")
        if treatment == "skill" and len(instruction_files) != 1:
            raise HarnessError("skill runner package must contain exactly one skill instruction")

    baseline_exec = copy.deepcopy(compiled_views["baseline"]["execution"])
    skill_exec = copy.deepcopy(compiled_views["skill"]["execution"])
    if baseline_exec.get("user_prompt") != skill_exec.get("user_prompt"):
        raise HarnessError("paired user prompt mismatch")
    if baseline_exec.get("repo_commit") != skill_exec.get("repo_commit"):
        raise HarnessError("paired repo commit mismatch")
    if common_hashes != control.get("shared_subject_source_hashes"):
        raise HarnessError("paired common source hashes do not match control")

    return {
        "verified": True,
        "experiment_id": control.get("experiment_id"),
        "case_id": control.get("case_id"),
        "repetition": control.get("repetition"),
        "response_count": 2,
        "prompt_parity": True,
        "subject_source_parity": True,
        "treatment_mapping_hidden_from_judge_contract": "response_assignments" not in judge_contract,
    }


def package_blind_pair(pair_dir: Path, run_dirs: list[Path], out_dir: Path) -> Path:
    pair_status = verify_paired_prepared(pair_dir)
    control = load_yaml(pair_dir / "control.yml")
    judge_contract = load_yaml(pair_dir / "judge-contract.yml")
    assignments = control["response_assignments"]
    expected_ids = set(assignments)
    if len(run_dirs) != 2:
        raise HarnessError("package-blind-pair requires exactly two run directories")

    runs: dict[str, dict[str, Any]] = {}
    for run_dir in run_dirs:
        verify_run_package(run_dir)
        manifest = load_yaml(run_dir / "manifest.yml")
        if not isinstance(manifest, dict):
            raise HarnessError(f"invalid run manifest: {run_dir}")
        response_id = str(manifest.get("test_id"))
        if response_id not in expected_ids:
            raise HarnessError(f"run {run_dir} has unexpected response id {response_id}")
        if response_id in runs:
            raise HarnessError(f"duplicate run for response id {response_id}")
        runs[response_id] = {"dir": run_dir, "manifest": manifest}
    if set(runs) != expected_ids:
        raise HarnessError("blind pair is missing a response run")

    models = {str(item["manifest"].get("runner_model")) for item in runs.values()}
    repo_commits = {str(item["manifest"].get("repo_commit")) for item in runs.values()}
    runner_types = {str(item["manifest"].get("runner_type")) for item in runs.values()}
    if len(models) != 1:
        raise HarnessError("paired runs used different runner models")
    if len(repo_commits) != 1:
        raise HarnessError("paired runs used different repo commits")
    if len(runner_types) != 1:
        raise HarnessError("paired runs used different runner types")
    known_sessions = [str(item["manifest"].get("runner_session_id")) for item in runs.values() if str(item["manifest"].get("runner_session_id")) != "unknown"]
    if len(known_sessions) == 2 and known_sessions[0] == known_sessions[1]:
        raise HarnessError("paired runs reused the same known runner_session_id; fresh-context isolation is not demonstrated")

    target_skill = str(control.get("target_skill", ""))
    disclosure: dict[str, bool] = {}
    for response_id, item in runs.items():
        text = (item["dir"] / "runner-output.md").read_text(encoding="utf-8")
        lower = text.lower()
        disclosure[response_id] = bool(
            (target_skill and target_skill.lower() in lower)
            or "skill variant" in lower
            or "baseline variant" in lower
            or "baseline condition" in lower
        )
    if any(disclosure.values()):
        raise HarnessError("treatment disclosure detected in runner output; blind judge packaging refused")

    if out_dir.exists():
        raise HarnessError(f"blind judge package already exists: {out_dir}")
    out_dir.mkdir(parents=True)
    dump_yaml(judge_contract, out_dir / "judge-contract.yml")
    responses_dir = out_dir / "responses"
    responses_dir.mkdir()
    response_refs = []
    for response_id in sorted(runs):
        target = responses_dir / f"{response_id}.md"
        shutil.copy2(runs[response_id]["dir"] / "runner-output.md", target)
        response_refs.append({"response_id": response_id, "path": f"responses/{response_id}.md", "hash": hash_file(target)})

    session_ids = [str(item["manifest"].get("runner_session_id")) for item in runs.values()]
    parity = {
        "schema_version": 1,
        "same_user_prompt": pair_status["prompt_parity"],
        "same_subject_sources": pair_status["subject_source_parity"],
        "same_repo_commit": True,
        "same_runner_model": True,
        "same_runner_type": True,
        "fresh_context_sessions_distinct": "unknown" if "unknown" in session_ids else len(set(session_ids)) == 2,
        "model_configuration_parity": "unverified",
        "model_configuration_note": "The current generic runner-adapter contract records model identity but no normalized model-configuration fingerprint.",
        "treatment_disclosure_detected": False,
    }
    dump_yaml(parity, out_dir / "parity.yml")
    blind_input = {
        "schema_version": 1,
        "contract": BLIND_INPUT_CONTRACT,
        "judge_contract": "judge-contract.yml",
        "parity": "parity.yml",
        "responses": response_refs,
        "note": "Treatment mapping is intentionally absent. Unblind only after semantic judging is complete.",
    }
    dump_yaml(blind_input, out_dir / "blind-judge-input.yml")
    hashes = {
        "hash_algorithm": "sha256/file-bytes-v1",
        "judge_contract": hash_file(out_dir / "judge-contract.yml"),
        "parity": hash_file(out_dir / "parity.yml"),
        "blind_judge_input": hash_file(out_dir / "blind-judge-input.yml"),
        "responses": {item["response_id"]: item["hash"] for item in response_refs},
    }
    dump_yaml(hashes, out_dir / "hashes.yml")
    return out_dir


def cli_prepare(args: argparse.Namespace) -> int:
    experiment_path = Path(args.experiment).resolve()
    experiment = load_paired_experiment(experiment_path)
    pair = compile_paired_case(
        experiment,
        args.case_id,
        Path(args.repo_root).resolve(),
        args.repetition,
        args.blind_seed,
    )
    out = Path(args.out).resolve()
    write_paired_case(pair, Path(args.repo_root).resolve(), out)
    print(out)
    return 0


def cli_verify(args: argparse.Namespace) -> int:
    status = verify_paired_prepared(Path(args.paired).resolve())
    import yaml
    print(yaml.safe_dump(status, allow_unicode=True, sort_keys=False), end="")
    return 0


def cli_blind(args: argparse.Namespace) -> int:
    out = package_blind_pair(
        Path(args.paired).resolve(),
        [Path(item).resolve() for item in args.run],
        Path(args.out).resolve(),
    )
    print(out)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    prep = sub.add_parser("prepare-pair", help="Prepare one baseline/skill pair using the existing behavioral harness contracts")
    prep.add_argument("case_id")
    prep.add_argument("--experiment", required=True)
    prep.add_argument("--repo-root", default=str(Path(__file__).resolve().parents[1]))
    prep.add_argument("--repetition", type=int, required=True)
    prep.add_argument("--blind-seed", required=True, help="Coordinator-only seed used to derive opaque response IDs")
    prep.add_argument("--out", required=True)
    prep.set_defaults(func=cli_prepare)

    verify = sub.add_parser("verify-pair", help="Verify pair parity, hashes and treatment isolation before execution")
    verify.add_argument("--paired", required=True)
    verify.set_defaults(func=cli_verify)

    blind = sub.add_parser("package-blind-pair", help="Create a treatment-blind judge package from two ordinary harness run packages")
    blind.add_argument("--paired", required=True)
    blind.add_argument("--run", action="append", required=True, help="Ordinary behavioral-harness run directory; pass exactly twice")
    blind.add_argument("--out", required=True)
    blind.set_defaults(func=cli_blind)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        return int(args.func(args))
    except HarnessError as exc:
        import sys
        print(f"HARNESS_ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
