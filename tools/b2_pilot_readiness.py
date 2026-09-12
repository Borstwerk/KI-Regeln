#!/usr/bin/env python3
"""Pilot readiness evaluation and the gate that actually blocks a Phase 4.2C / B2 model run.

The entry criteria in the B2 design are not a checklist someone ticks. Each one is
evaluated here, most of them by running the check rather than by asserting the answer, and
the result decides whether a model pilot may start at all.

Two rules make this more than paperwork:

* a criterion is `met` only when a deterministic check says so. Where no check exists yet the
  answer is `unknown`, which blocks exactly like `false`. There is no manual `true`.
* the readiness artifact cannot authorise itself. `gate()` re-evaluates the criteria; a
  hand-edited file claiming success is ignored, and a mismatch between a stored artifact and
  a fresh evaluation is itself a refusal.

`--preflight-only` walks the entire admission path and stops immediately before the point
where a model process would be started.
"""
from __future__ import annotations

import argparse
import json
import platform
import sys
from pathlib import Path
from typing import Any, Callable

try:
    from .b2_boundary import PROVIDER, provider_available
    from .behavioral_harness_core import hash_file, hash_object, load_yaml
    from .verification_governance_disposition import DOMINANCE, NON_BEHAVIORAL, PERMITTED, VIOLATION
    from .verification_surface import load_pinned_trust_root
except ImportError:  # direct script sibling import
    from b2_boundary import PROVIDER, provider_available
    from behavioral_harness_core import hash_file, hash_object, load_yaml
    from verification_governance_disposition import DOMINANCE, NON_BEHAVIORAL, PERMITTED, VIOLATION
    from verification_surface import load_pinned_trust_root

READINESS_CONTRACT = "verification-governance-pilot-readiness/v1"
ROOT = Path(__file__).resolve().parents[1]
B2 = ROOT / "Evals/Verification-Surface/behavioral"
TRUST_ROOT = ROOT / "Evals/Verification-Surface/canonical/trust-root.yml"
BOUNDARY_EVIDENCE = B2 / "evidence/boundary-probes.yml"
# The outermost link of the chain: code, not data. Mirrored in tests/test_verification_surface.py
# so that a change to either without the other is a failing test rather than a quiet update.
TRUST_ROOT_DOCUMENT_HASH = "sha256:ed83127f835902868b4ea18c78ffc4b713c7a0f4846bb97a506269b683af1448"
SEMANTIC_PROJECTION_HASH = "sha256:2367afcb9d16a3c30455e3aa2bd47d3d1ffd2072dadaa77a9b5a5ee67d515d20"
# Probes that must have passed. P6 is network observation: evidence, never a gate.
REQUIRED_PROBES = ("P1", "P2", "P3", "P4", "P5")


class ReadinessError(RuntimeError):
    pass


def semantic_projection(matrix: dict[str, Any]) -> dict[str, Any]:
    """The reviewed behavioral semantics, and nothing else.

    Technical metadata may be added to the matrix during implementation; this projection is
    what may not move. Pinning it separately is what stops "update the trust root pin" from
    becoming the way a case semantics changes quietly.
    """
    return {
        "contract": matrix["contract"],
        "cases": [
            {"case_id": c["case_id"], "threats": sorted(c["threats"]), "role": c["role"],
             "permitted_dispositions": sorted(c["permitted_dispositions"])}
            for c in matrix["cases"]
        ],
        "disposition_classes": {k: v["class"] for k, v in sorted(matrix["dispositions"].items())},
        "dominance": [r["id"] for r in matrix["dominance"]["rules"]],
    }


def _tri(ok: bool | None, reason: str, evidence: str) -> dict[str, Any]:
    return {"met": ok if ok is not None else "unknown", "reason": reason, "evidence": evidence}


def _pins() -> dict[str, Any]:
    return load_pinned_trust_root(TRUST_ROOT, TRUST_ROOT_DOCUMENT_HASH)["pins"]


def evidence_binding() -> dict[str, str]:
    """What the probe evidence is only valid for.

    Probe results age the moment the code they exercised changes. After the review found a
    leak in the oracle view, the old P4 result described a system that no longer exists — so
    evidence now carries the hashes of the components it was produced against, and is
    rejected when any of them moves.
    """
    return {
        "provider": PROVIDER,
        "boundary_code": hash_file(ROOT / "tools/b2_boundary.py"),
        "confinement_code": hash_file(ROOT / "tools/b2_model_confinement.py"),
        "launcher_code": hash_file(ROOT / "tools/b2_check_launcher.py"),
        "oracle_code": hash_file(ROOT / "tools/b2_oracle.py"),
        "probe_code": hash_file(ROOT / "tools/b2_boundary_probes.py"),
        "preflight_code": hash_file(ROOT / "tools/b2_launch_preflight.py"),
        "driver": hash_file(B2 / "oracle/driver.py"),
        "expectations": hash_file(B2 / "oracle/expectations.yml"),
        "platform": f"{platform.system()}-{platform.machine()}",
        "python": platform.python_version(),
    }


# Set only for the duration of one `evaluate(fresh_probes=True)`. A namespace boundary's
# protection depends on the host kernel and util-linux as much as on this repository's code,
# and a stored result cannot speak for a machine it never ran on -- so the pilot admission
# re-runs P1-P5 instead of trusting a file.
_FRESH_PROBES: dict[str, Any] | None = None


def run_fresh_probes() -> dict[str, Any]:
    """Execute P1-P6 now, in this process, on this host."""
    try:
        from .b2_boundary_probes import run_all
    except ImportError:  # direct script sibling import
        from b2_boundary_probes import run_all
    return run_all()


def _boundary_probe_report() -> dict[str, Any] | None:
    """The probe evidence, or None when it is absent, unreadable or stale."""
    if _FRESH_PROBES is not None:
        return _FRESH_PROBES
    if not BOUNDARY_EVIDENCE.is_file():
        return None
    try:
        data = load_yaml(BOUNDARY_EVIDENCE)
    except Exception:  # noqa: BLE001
        return None
    if not isinstance(data, dict):
        return None
    recorded = data.get("bound_to")
    if recorded != evidence_binding():
        return None
    return data


# --- criteria -------------------------------------------------------------------------

def _c01_matrix_pinned() -> dict[str, Any]:
    try:
        pins = _pins()
    except Exception as exc:  # noqa: BLE001
        return _tri(False, f"trust root does not load under its external pin: {exc}", str(TRUST_ROOT))
    actual = hash_file(B2 / "case-matrix.yml")
    ok = actual == pins.get("b2_case_matrix_hash")
    return _tri(ok, "case matrix matches its pin in the trust root" if ok
                else "case matrix does not match the pinned hash", "trust-root.yml:b2_case_matrix_hash")


def _c02_expected_outcomes_committed() -> dict[str, Any]:
    matrix = load_yaml(B2 / "case-matrix.yml")
    projection = semantic_projection(matrix)
    ok = hash_object(projection) == SEMANTIC_PROJECTION_HASH
    return _tri(ok, "reviewed behavioral semantics unchanged" if ok
                else "the semantic projection has moved since review", "semantic projection hash")


def _c03_evaluator_data_separated() -> dict[str, Any]:
    leaks = []
    for case in sorted((B2 / "cases").iterdir()):
        seed = case / "seed"
        if not seed.is_dir():
            continue
        for p in seed.rglob("*"):
            rel = p.relative_to(seed).as_posix()
            if rel.startswith("canonical") or "expectations" in rel or "case-matrix" in rel:
                leaks.append(f"{case.name}/{rel}")
    return _tri(not leaks, "no evaluator artifact appears in any seed" if not leaks
                else f"evaluator artifacts inside seeds: {leaks}", "cases/*/seed")


def _c04_expected_verdicts_unreadable() -> dict[str, Any]:
    report = _boundary_probe_report()
    if report is None:
        return _tri(None, "boundary probe evidence is absent or no longer binds to this build",
                    str(BOUNDARY_EVIDENCE))
    probe = (report.get("probes") or {}).get("P1")
    ok = bool(probe and probe.get("passed") is True)
    return _tri(ok, "P1 shows hidden evaluator data unreadable from the check view" if ok
                else "P1 did not pass", "evidence/boundary-probes.yml:P1")


def _functional(name: str):
    """Import a checker lazily; a failing import is `unknown`, never a quiet pass."""
    from importlib import import_module
    try:
        module = import_module("tools.b2_readiness_checks")
    except ImportError:
        module = import_module("b2_readiness_checks")
    return getattr(module, name)


def _c05_b1_in_the_eval_path() -> dict[str, Any]:
    """Run a real strict B1 assessment through the grader. Grepping for `assess(` proved
    that the string exists, which is not the same property."""
    ok, reason = _functional("b1_strict_control")()
    return _tri(ok, reason, "b2_readiness_checks.b1_strict_control")



def _c06_controls_present() -> dict[str, Any]:
    matrix = load_yaml(B2 / "case-matrix.yml")
    positive = [c["case_id"] for c in matrix["cases"] if "PERMITTED_PRODUCT_FIX" in c["permitted_dispositions"]]
    negative = [c["case_id"] for c in matrix["cases"] if "PERMITTED_PRODUCT_FIX" not in c["permitted_dispositions"]]
    ok = bool(positive and negative)
    return _tri(ok, f"{len(positive)} positive and {len(negative)} escalation-only control(s)",
                "case-matrix.yml")


def _c07_deliberate_breakage() -> dict[str, Any]:
    report = _boundary_probe_report()
    if report is None:
        return _tri(None, "boundary probe evidence is absent or no longer binds to this build",
                    str(BOUNDARY_EVIDENCE))
    probes = report.get("probes") or {}
    missing = [p for p in REQUIRED_PROBES if not (probes.get(p) or {}).get("passed") is True]
    reasons = all(str((probes.get(p) or {}).get("observed", "")).strip() for p in REQUIRED_PROBES)
    ok = not missing and reasons
    return _tri(ok, "P1-P5 passed with their observed failure reasons recorded" if ok
                else f"probes not passed or without an observed reason: {missing or 'reasons missing'}",
                "evidence/boundary-probes.yml")


def _c08_gaming_routes_reviewed() -> dict[str, Any]:
    path = B2 / "evidence/eval-gaming-redteam.yml"
    if not path.is_file():
        return _tri(None, "red-team evidence against the built system is absent", str(path))
    data = load_yaml(path)
    attempts = data.get("attempts") if isinstance(data, dict) else None
    ok = isinstance(attempts, list) and len(attempts) >= 8 and all(
        a.get("blocked") is True for a in attempts)
    return _tri(ok, f"{len(attempts)} gaming attempts, all blocked" if ok
                else "gaming attempts missing or not all blocked", "evidence/eval-gaming-redteam.yml")


def _c09_telemetry_sufficient() -> dict[str, Any]:
    """Export a real workspace and confirm the hashes are produced and complete."""
    ok, reason = _functional("workspace_export_control")()
    return _tri(ok, reason, "b2_readiness_checks.workspace_export_control")


def _c10_run_artifacts_versioned() -> dict[str, Any]:
    """Build a real run package with an export, verify it, then tamper and verify again."""
    ok, reason = _functional("package_verify_control")()
    return _tri(ok, reason, "b2_readiness_checks.package_verify_control")


def _c11_judge_schema() -> dict[str, Any]:
    """Not applicable, and modelled as such rather than dressed up as a measurement.

    No judge exists on the grading path, so there is no schema to fix. What *is* measured is
    the antecedent: that the grading module imports and calls no judge.
    """
    ok, reason = _functional("no_judge_on_the_path")()
    return {"met": ok if ok else "unknown", "applicable": False,
            "reason": (f"not applicable: {reason}" if ok else reason),
            "evidence": "b2_readiness_checks.no_judge_on_the_path"}


def _c12_unblinding_process() -> dict[str, Any]:
    """Also not applicable at one condition, and said so plainly.

    There is nothing here a deterministic check can measure, and inventing one would be
    exactly the manufactured `true` this contract forbids. What is checked is that the
    evaluation really does run a single condition.
    """
    ok, reason = _functional("single_condition")()
    return {"met": ok if ok else "unknown", "applicable": False,
            "reason": (f"not applicable: {reason}" if ok else reason),
            "evidence": "b2_readiness_checks.single_condition"}


def _c13_no_self_attestation() -> dict[str, Any]:
    """Feed the grader a report that lies, and prove the measured facts win."""
    ok, reason = _functional("report_is_not_ground_truth_control")()
    return _tri(ok, reason, "b2_readiness_checks.report_is_not_ground_truth_control")


def _c14_boundary_present() -> dict[str, Any]:
    available, reason = provider_available()
    return _tri(available, f"{PROVIDER}: {reason}", "tools/b2_boundary.py --probe")


def _c15_probes_executed() -> dict[str, Any]:
    return _c07_deliberate_breakage()


def _c16_oracle_separated() -> dict[str, Any]:
    report = _boundary_probe_report()
    if report is None:
        return _tri(None, "boundary probe evidence is absent or no longer binds to this build",
                    str(BOUNDARY_EVIDENCE))
    probe = (report.get("probes") or {}).get("P4") or {}
    seeds_clean = _c03_evaluator_data_separated()["met"] is True
    staged_ok, staged_reason = _functional("oracle_driver_view_control")()
    ok = probe.get("passed") is True and seeds_clean and staged_ok
    return _tri(ok, f"P4 shows oracle source and expectations unreadable from the product view; {staged_reason}"
                if ok else f"oracle separation is not demonstrated ({staged_reason})",
                "evidence/boundary-probes.yml:P4")


def _c17_network_reported() -> dict[str, Any]:
    report = _boundary_probe_report()
    if report is None:
        return _tri(None, "no P6 observation recorded", str(BOUNDARY_EVIDENCE))
    probe = (report.get("probes") or {}).get("P6") or {}
    value = probe.get("network_disabled")
    ok = value in (True, False, "unknown")
    return _tri(ok, f"network_disabled reported as observed: {value!r}" if ok
                else "network_disabled is not reported as an observation",
                "evidence/boundary-probes.yml:P6")


def _c18_disposition_total() -> dict[str, Any]:
    """Enumerate the whole fact space here, rather than counting list lengths."""
    ok, reason = _functional("disposition_totality")()
    return _tri(ok, reason, "b2_readiness_checks.disposition_totality")


def _c20_runtime_supports_locked_down_permissions() -> dict[str, Any]:
    """A writable run needs `--permission-mode dontAsk`, and there is no weaker fallback.

    Added by this correction: `--tools` names built-in tools while `--allowedTools` takes
    permission rules, and a non-interactive run must refuse anything not pre-allowed rather
    than route it to a prompt nobody will answer. A build without that mode cannot run B2.
    """
    ok, reason = _functional("runtime_permission_mode")()
    return _tri(ok, reason, "b2_readiness_checks.runtime_permission_mode")


def _c21_model_process_workspace_confinement() -> dict[str, Any]:
    """The model process itself, not only the code it writes.

    Added by this correction. `run_in_view` confines agent-written check and product code;
    it never confined the Claude Code process, and a tool policy cannot: read-only shell
    commands execute without a prompt even under `dontAsk`. Measured by running those
    commands for real against a planted sentinel, never by reading the allowlist.
    """
    ok, reason = _functional("model_process_workspace_confinement")()
    return _tri(ok, reason, "b2_readiness_checks.model_process_workspace_confinement")


def _c22_confined_model_runtime_launchable() -> dict[str, Any]:
    """Added by this correction, because confinement created the precondition.

    Before the outer view existed, "the CLI is installed and authenticated" was a property of
    the host and nothing more. Now the launch happens somewhere else: a different filesystem,
    a different PATH, a fresh config directory and no host home. Measured by building the real
    writable argv and exercising it -- paths, startup, parser, auth -- inside exactly that
    view, with no model request.
    """
    ok, reason = _functional("confined_model_runtime_launchable")()
    return _tri(ok, reason, "b2_readiness_checks.confined_model_runtime_launchable")


def _c19_semantics_change_visible() -> dict[str, Any]:
    pins = None
    try:
        pins = _pins()
    except Exception:  # noqa: BLE001
        return _tri(False, "trust root does not load under its external pin", str(TRUST_ROOT))
    ok = pins.get("b2_semantic_projection_hash") == SEMANTIC_PROJECTION_HASH
    return _tri(ok, "the semantic projection is pinned redundantly, in the trust root and in code" if ok
                else "the pinned projection and the code constant disagree",
                "trust-root.yml:b2_semantic_projection_hash")


CRITERIA: tuple[tuple[int, str, bool, Callable[[], dict[str, Any]]], ...] = (
    (1, "Case ground truth committed before any run, and pinned", True, _c01_matrix_pinned),
    (2, "Expected deterministic outcome classes committed", True, _c02_expected_outcomes_committed),
    (3, "Evaluator-hidden data technically separated", True, _c03_evaluator_data_separated),
    (4, "Agent cannot read expected verdicts", True, _c04_expected_verdicts_unreadable),
    (5, "B1 verification surface integrated in the eval path", True, _c05_b1_in_the_eval_path),
    (6, "Positive and negative controls present", True, _c06_controls_present),
    (7, "Deliberate breakage present, with expected failure reason", True, _c07_deliberate_breakage),
    (8, "Eval-gaming routes reviewed against the built system", True, _c08_gaming_routes_reviewed),
    (9, "Telemetry sufficient", True, _c09_telemetry_sufficient),
    (10, "Run artifacts versioned", True, _c10_run_artifacts_versioned),
    (11, "Judge schema fixed before the first run, if a judge is used", True, _c11_judge_schema),
    (12, "Unblinding process defined in advance", True, _c12_unblinding_process),
    (13, "No condition can attest its own success", True, _c13_no_self_attestation),
    (14, "Execution boundary present and confining agent-controlled code", True, _c14_boundary_present),
    (15, "Boundary probes P1-P5 executed and passing", True, _c15_probes_executed),
    (16, "Oracle source and expectations never in an agent-reachable view", True, _c16_oracle_separated),
    (17, "network_disabled reported as observed", False, _c17_network_reported),
    (18, "Disposition function total and unambiguous", True, _c18_disposition_total),
    (19, "Case semantics changes visible as design changes", True, _c19_semantics_change_visible),
    (20, "Runtime offers the locked-down permission mode a writable run needs", True,
     _c20_runtime_supports_locked_down_permissions),
    (21, "Model process confined to the workspace, filesystem-wise", True,
     _c21_model_process_workspace_confinement),
    (22, "The confined model runtime is launchable: view-local argv, executable runtime, "
     "working auth in the view's own environment", True,
     _c22_confined_model_runtime_launchable),
)


def evaluate(fresh_probes: bool = False) -> dict[str, Any]:
    """Evaluate every criterion now. Nothing is read back from a stored verdict.

    With `fresh_probes`, P1-P6 are executed in this process rather than read from the stored
    evidence file. That is the mode the model-pilot admission uses: probe results describe the
    host they ran on, and a stored result from another machine is not evidence about this one.
    """
    global _FRESH_PROBES
    probes = run_fresh_probes() if fresh_probes else None
    rows = []
    previous, _FRESH_PROBES = _FRESH_PROBES, probes
    try:
        for number, title, blocking, check in CRITERIA:
            try:
                outcome = check()
            except Exception as exc:  # noqa: BLE001 - a failing check is `unknown`, never `met`
                outcome = _tri(None, f"check raised {type(exc).__name__}: {exc}", "check error")
            rows.append({"id": number, "criterion": title, "blocking": blocking, **outcome})
    finally:
        _FRESH_PROBES = previous
    blockers = [r for r in rows if r["blocking"] and r["met"] is not True]
    return {
        "contract": READINESS_CONTRACT,
        "phase": "4.2C / B2",
        "probe_evidence": "executed in this process" if fresh_probes else "read from the stored file",
        "ready": not blockers,
        "status": "READY_FOR_MODEL_PILOT" if not blockers else "NOT_READY_FOR_MODEL_PILOT",
        "blocking_unmet": [r["id"] for r in blockers],
        "criteria": rows,
        "note": "An infrastructure decision. It says nothing about any agent's behaviour.",
    }


def gate(stored: Path | None = None, fresh_probes: bool = False) -> tuple[bool, str]:
    """May a model pilot start? Answered by re-evaluating, never by reading a claim.

    A stored artifact is compared against the fresh evaluation, so a hand-edited file that
    claims readiness is not merely ignored: the disagreement is itself a refusal.

    `fresh_probes` additionally re-runs P1-P5 here rather than trusting the stored evidence.
    The writable launch path uses it; nothing else has to.
    """
    fresh = evaluate(fresh_probes=fresh_probes)
    if stored is not None and stored.is_file():
        try:
            claimed = load_yaml(stored)
        except Exception as exc:  # noqa: BLE001
            return False, f"stored readiness artifact does not parse: {exc}"
        if not isinstance(claimed, dict):
            return False, "stored readiness artifact is not a mapping"
        if claimed.get("ready") != fresh["ready"] or claimed.get("status") != fresh["status"]:
            return False, (
                "the stored readiness artifact disagrees with a fresh evaluation "
                f"(stored {claimed.get('status')!r}, evaluated {fresh['status']!r}); "
                "a readiness file cannot authorise itself"
            )
    if not fresh["ready"]:
        unmet = ", ".join(str(i) for i in fresh["blocking_unmet"])
        return False, f"blocking pilot entry criteria not met: {unmet}"
    return True, "every blocking pilot entry criterion is met"


def _cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", help="Write the readiness artifact to this path")
    parser.add_argument("--gate", action="store_true", help="Exit non-zero unless a pilot may start")
    parser.add_argument("--stored", help="Readiness artifact to check the gate against")
    parser.add_argument("--preflight-only", action="store_true",
                        help="Walk the admission path and stop before a model process would start")
    args = parser.parse_args(argv)

    report = evaluate()
    if args.write:
        import yaml
        Path(args.write).write_text(yaml.safe_dump(report, allow_unicode=True, sort_keys=False), encoding="utf-8")

    if args.gate or args.preflight_only:
        allowed, reason = gate(Path(args.stored) if args.stored else None)
        print(json.dumps({"status": report["status"], "may_start_model_pilot": allowed,
                          "reason": reason,
                          "stopped_before": "model process launch" if args.preflight_only else None},
                         indent=2))
        return 0 if allowed else 1

    print(json.dumps(report, indent=2))
    return 0 if report["ready"] else 1


if __name__ == "__main__":
    raise SystemExit(_cli())
