#!/usr/bin/env python3
"""CLI and immutable packaging for the KI-Regeln behavioral-test harness."""
from __future__ import annotations

import argparse
import copy
import shutil
import sys
from pathlib import Path
from typing import Any

import yaml

try:
    from .behavioral_harness_core import *
    from .behavioral_harness_gates import *
except ImportError:  # direct execution: python tools/behavioral_harness.py
    from behavioral_harness_core import *
    from behavioral_harness_gates import *


RUN_ARTIFACT_NAMES = (
    "manifest.yml",
    "execution-view.yml",
    "judge-view.yml",
    "runner-output.md",
    "trace.yml",
    "actions.yml",
    "evidence.yml",
    "deterministic-gates.yml",
    "judge-input.yml",
)


def load_or_default(src: Path | None, default: dict[str, Any]) -> dict[str, Any]:
    if src is None:
        return copy.deepcopy(default)
    data = load_yaml(src)
    if not isinstance(data, dict):
        raise HarnessError(f"expected mapping in {src}")
    return data


def _resolve_adapter_ref(adapter_path: Path, value: str, label: str) -> Path:
    rel = _safe_rel(str(value))
    if rel is None:
        raise HarnessError(f"runner adapter {label} must be a safe relative path")
    path = (adapter_path.parent / rel).resolve()
    if not path.is_file():
        raise HarnessError(f"runner adapter {label} missing: {path}")
    return path


def load_runner_adapter_result(path: Path) -> dict[str, Any]:
    data = load_yaml(path)
    if not isinstance(data, dict):
        raise HarnessError(f"runner adapter result must be a mapping: {path}")
    validate_document(data, "runner-adapter", "runner adapter result")
    return data


def package_run(
    prepared_dir: Path,
    runner_output: Path | None,
    trace_path: Path | None,
    actions_path: Path | None,
    evidence_path: Path | None,
    out_root: Path,
    run_id: str,
    runner_type: str = "unknown",
    runner_model: str = "unknown",
    runner_session_id: str = "unknown",
    started_at: str = "unknown",
    finished_at: str = "unknown",
    adapter_result_path: Path | None = None,
) -> Path:
    prepared = verify_prepared_integrity(prepared_dir)
    execution = prepared["execution"]
    judge = prepared["judge"]
    hashes = prepared["hashes"]
    test_id = str(execution["test_id"])

    if adapter_result_path is not None:
        adapter = load_runner_adapter_result(adapter_result_path)
        runner_type = str(adapter["runner_type"])
        runner_model = str(adapter["runner_model"])
        runner_session_id = str(adapter["runner_session_id"])
        started_at = str(adapter["started_at"])
        finished_at = str(adapter["finished_at"])
        runner_output = _resolve_adapter_ref(adapter_result_path, adapter["runner_output"], "runner_output")
        trace_path = _resolve_adapter_ref(adapter_result_path, adapter["trace"], "trace")
        actions_path = _resolve_adapter_ref(adapter_result_path, adapter["actions"], "actions")
        evidence_path = _resolve_adapter_ref(adapter_result_path, adapter["evidence"], "evidence")

    trace = load_or_default(trace_path, default_trace())
    actions = load_or_default(actions_path, default_actions())
    evidence = load_or_default(evidence_path, default_evidence())
    validate_document(trace, "trace", "trace")
    validate_document(actions, "actions", "actions")
    validate_document(evidence, "evidence", "evidence")
    gates = evaluate_gates(judge, trace, actions, evidence)

    observed_status = normalize_status((trace.get("status") or {}).get("observed_status"))
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "run_id": run_id,
        "test_id": test_id,
        "repo_commit": execution.get("repo_commit", "unknown"),
        "case_definition_hash": hashes.get("case_definition_hash", "unknown"),
        "execution_view_hash": hashes.get("execution_view_hash", "unknown"),
        "judge_view_hash": hashes.get("judge_view_hash", "unknown"),
        "fixture_hashes": hashes.get("fixture_hashes", {}),
        "runner_type": runner_type,
        "runner_model": runner_model,
        "runner_session_id": runner_session_id,
        "started_at": started_at,
        "finished_at": finished_at,
        "trace_version": str(trace.get("schema_version", "unknown")),
        "harness_version": HARNESS_VERSION,
        "status": observed_status,
    }
    validate_document(manifest, "manifest", "manifest")

    judge_input = {
        "schema_version": SCHEMA_VERSION,
        "contract": "behavioral-judge-input/v1",
        "manifest": "manifest.yml",
        "judge_view": "judge-view.yml",
        "runner_output": "runner-output.md",
        "trace": "trace.yml",
        "actions": "actions.yml",
        "evidence": "evidence.yml",
        "deterministic_gates": "deterministic-gates.yml",
        "hashes": "hashes.yml",
        "note": "Technical facts only. Semantic judgment, severity, adjudication and human acceptance are out of scope.",
    }
    validate_document(judge_input, "judge-input", "judge input")
    validate_document(gates, "deterministic-gates", "deterministic gates")

    target = out_root / test_id / run_id
    if target.exists():
        raise HarnessError(f"run package already exists: {target}")
    target.mkdir(parents=True)

    shutil.copy2(prepared_dir / "execution-view.yml", target / "execution-view.yml")
    shutil.copy2(prepared_dir / "judge-view.yml", target / "judge-view.yml")
    shutil.copy2(prepared_dir / "hashes.yml", target / "hashes.yml")

    if runner_output is None:
        (target / "runner-output.md").write_text("", encoding="utf-8")
    else:
        shutil.copy2(runner_output, target / "runner-output.md")

    dump_yaml(trace, target / "trace.yml")
    dump_yaml(actions, target / "actions.yml")
    dump_yaml(evidence, target / "evidence.yml")
    dump_yaml(gates, target / "deterministic-gates.yml")
    dump_yaml(manifest, target / "manifest.yml")
    dump_yaml(judge_input, target / "judge-input.yml")

    final_hashes = copy.deepcopy(hashes)
    final_hashes["run_artifact_hashes"] = {name: hash_file(target / name) for name in RUN_ARTIFACT_NAMES}
    dump_yaml(final_hashes, target / "hashes.yml")
    verify_run_package(target)
    return target


def verify_run_package(run_dir: Path) -> dict[str, Any]:
    hashes_path = run_dir / "hashes.yml"
    if not hashes_path.is_file():
        raise HarnessError(f"run hashes missing: {hashes_path}")
    hashes = load_yaml(hashes_path)
    if not isinstance(hashes, dict):
        raise HarnessError("run hashes.yml must be a mapping")

    recorded = hashes.get("run_artifact_hashes")
    if not isinstance(recorded, dict):
        raise HarnessError("run_artifact_hashes missing from hashes.yml")

    for name in RUN_ARTIFACT_NAMES:
        path = run_dir / name
        if not path.is_file():
            raise HarnessError(f"run artifact missing: {path}")
        expected = recorded.get(name)
        actual = hash_file(path)
        if not expected:
            raise HarnessError(f"run artifact hash missing for {name}")
        if actual != expected:
            raise HarnessError(f"run artifact hash mismatch for {name}: expected {expected}, got {actual}")

    execution = load_yaml(run_dir / "execution-view.yml")
    judge = load_yaml(run_dir / "judge-view.yml")
    manifest = load_yaml(run_dir / "manifest.yml")
    trace = load_yaml(run_dir / "trace.yml")
    actions = load_yaml(run_dir / "actions.yml")
    evidence = load_yaml(run_dir / "evidence.yml")
    gates = load_yaml(run_dir / "deterministic-gates.yml")
    judge_input = load_yaml(run_dir / "judge-input.yml")

    validate_document(trace, "trace", "trace")
    validate_document(actions, "actions", "actions")
    validate_document(evidence, "evidence", "evidence")
    validate_document(manifest, "manifest", "manifest")
    validate_document(gates, "deterministic-gates", "deterministic gates")
    validate_document(judge_input, "judge-input", "judge input")

    if hash_object(execution) != hashes.get("execution_view_hash"):
        raise HarnessError("run execution-view canonical hash mismatch")
    if hash_object(judge) != hashes.get("judge_view_hash"):
        raise HarnessError("run judge-view canonical hash mismatch")
    if manifest.get("execution_view_hash") != hashes.get("execution_view_hash"):
        raise HarnessError("manifest/execution_view_hash relationship mismatch")
    if manifest.get("judge_view_hash") != hashes.get("judge_view_hash"):
        raise HarnessError("manifest/judge_view_hash relationship mismatch")
    if manifest.get("case_definition_hash") != hashes.get("case_definition_hash"):
        raise HarnessError("manifest/case_definition_hash relationship mismatch")
    if manifest.get("fixture_hashes") != hashes.get("fixture_hashes"):
        raise HarnessError("manifest/fixture_hashes relationship mismatch")

    return {"verified": True, "run_id": manifest.get("run_id"), "test_id": manifest.get("test_id"), "artifact_count": len(RUN_ARTIFACT_NAMES)}


def validate_matrix_unchanged(matrix: dict[str, Any]) -> None:
    if len(matrix.get("tests", [])) != 50:
        raise HarnessError(f"pilot matrix must contain exactly 50 prepared tests, found {len(matrix.get('tests', []))}")
    ids = [str(x.get("test_id")) for x in matrix["tests"]]
    if len(ids) != len(set(ids)):
        raise HarnessError("duplicate test ids in pilot matrix")


def cli_prepare(args: argparse.Namespace) -> int:
    matrix_path = Path(args.matrix).resolve()
    repo_root = Path(args.repo_root).resolve()
    matrix = load_matrix(matrix_path)
    verify_locked_matrix(matrix_path, matrix)
    validate_matrix_unchanged(matrix)
    overrides = load_yaml(Path(args.fixture_roles).resolve()) if args.fixture_roles else {}
    compiled = compile_case(matrix, args.test_id, repo_root, repo_commit=args.repo_commit, role_overrides=overrides)
    out = Path(args.out).resolve()
    write_prepared_case(compiled, out)
    print(out)
    return 0


def cli_package(args: argparse.Namespace) -> int:
    target = package_run(
        Path(args.prepared).resolve(),
        Path(args.runner_output).resolve() if args.runner_output else None,
        Path(args.trace).resolve() if args.trace else None,
        Path(args.actions).resolve() if args.actions else None,
        Path(args.evidence).resolve() if args.evidence else None,
        Path(args.out).resolve(),
        args.run_id,
        runner_type=args.runner_type,
        runner_model=args.runner_model,
        runner_session_id=args.runner_session_id,
        started_at=args.started_at,
        finished_at=args.finished_at,
        adapter_result_path=Path(args.adapter_result).resolve() if args.adapter_result else None,
    )
    print(target)
    return 0


def cli_gates(args: argparse.Namespace) -> int:
    judge = load_yaml(Path(args.judge).resolve())
    trace = load_yaml(Path(args.trace).resolve()) if args.trace else default_trace()
    actions = load_yaml(Path(args.actions).resolve()) if args.actions else default_actions()
    evidence = load_yaml(Path(args.evidence).resolve()) if args.evidence else default_evidence()
    out = evaluate_gates(judge, trace, actions, evidence)
    print(yaml.safe_dump(out, allow_unicode=True, sort_keys=False), end="")
    return 0


def cli_verify_run(args: argparse.Namespace) -> int:
    result = verify_run_package(Path(args.run).resolve())
    print(yaml.safe_dump(result, allow_unicode=True, sort_keys=False), end="")
    return 0


def cli_selftest(_: argparse.Namespace) -> int:
    import subprocess
    return subprocess.call([sys.executable, "-m", "unittest", "-v", "tests.test_behavioral_harness"], cwd=ROOT)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    prep = sub.add_parser("prepare-case", help="Compile one pilot case into isolated execution/judge views")
    prep.add_argument("test_id")
    prep.add_argument("--matrix", required=True, help="Path to the locked KI-Regeln-Pilot-Testmatrix.yml artifact")
    prep.add_argument("--repo-root", default=str(ROOT))
    prep.add_argument("--repo-commit")
    prep.add_argument("--fixture-roles", default=str(DEFAULT_FIXTURE_ROLES))
    prep.add_argument("--out", required=True)
    prep.set_defaults(func=cli_prepare)

    package = sub.add_parser("package-run", help="Package an already executed runner result for later judging")
    package.add_argument("--prepared", required=True)
    package.add_argument("--runner-output")
    package.add_argument("--trace")
    package.add_argument("--actions")
    package.add_argument("--evidence")
    package.add_argument("--adapter-result", help="Optional generic runner-adapter result YAML; schema validated before use")
    package.add_argument("--out", required=True)
    package.add_argument("--run-id", required=True)
    package.add_argument("--runner-type", default="unknown")
    package.add_argument("--runner-model", default="unknown")
    package.add_argument("--runner-session-id", default="unknown")
    package.add_argument("--started-at", default="unknown")
    package.add_argument("--finished-at", default="unknown")
    package.set_defaults(func=cli_package)

    gates = sub.add_parser("evaluate-gates", help="Evaluate deterministic tri-state facts only")
    gates.add_argument("--judge", required=True)
    gates.add_argument("--trace")
    gates.add_argument("--actions")
    gates.add_argument("--evidence")
    gates.set_defaults(func=cli_gates)

    verify = sub.add_parser("verify-run", help="Verify packaged run artifact hashes and schema contracts")
    verify.add_argument("--run", required=True)
    verify.set_defaults(func=cli_verify_run)

    selftest = sub.add_parser("selftest", help="Run synthetic/replay harness self-tests only")
    selftest.set_defaults(func=cli_selftest)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        return int(args.func(args))
    except HarnessError as exc:
        print(f"HARNESS_ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
