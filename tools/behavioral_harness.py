#!/usr/bin/env python3
"""CLI and immutable packaging for the KI-Regeln behavioral-test harness."""
try:
    from .behavioral_harness_core import *
    from .behavioral_harness_gates import *
except ImportError:  # direct execution: python tools/behavioral_harness.py
    from behavioral_harness_core import *
    from behavioral_harness_gates import *

def copy_or_default(src: Path | None, default: dict[str, Any], dst: Path) -> dict[str, Any]:
    if src is None:
        data = copy.deepcopy(default)
        dump_yaml(data, dst)
        return data
    data = load_yaml(src)
    if not isinstance(data, dict):
        raise HarnessError(f"expected mapping in {src}")
    dump_yaml(data, dst)
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
) -> Path:
    execution = load_yaml(prepared_dir / "execution-view.yml")
    judge = load_yaml(prepared_dir / "judge-view.yml")
    hashes = load_yaml(prepared_dir / "hashes.yml")
    test_id = str(execution["test_id"])

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

    trace = copy_or_default(trace_path, default_trace(), target / "trace.yml")
    actions = copy_or_default(actions_path, default_actions(), target / "actions.yml")
    evidence = copy_or_default(evidence_path, default_evidence(), target / "evidence.yml")
    gates = evaluate_gates(judge, trace, actions, evidence)
    dump_yaml(gates, target / "deterministic-gates.yml")

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
    dump_yaml(manifest, target / "manifest.yml")

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
    dump_yaml(judge_input, target / "judge-input.yml")

    final_hashes = copy.deepcopy(hashes)
    final_hashes["run_artifact_hashes"] = {
        name: hash_file(target / name)
        for name in (
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
    }
    dump_yaml(final_hashes, target / "hashes.yml")
    return target


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
    compiled = compile_case(
        matrix, args.test_id, repo_root, repo_commit=args.repo_commit, role_overrides=overrides
    )
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


def cli_selftest(_: argparse.Namespace) -> int:
    import subprocess

    return subprocess.call(
        [sys.executable, "-m", "unittest", "-v", "tests.test_behavioral_harness"],
        cwd=ROOT,
    )


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
