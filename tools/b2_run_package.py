#!/usr/bin/env python3
"""Build a model-free B2 run package: the existing harness, plus a workspace export.

Used by the dry runs and by the tamper probe. It exercises the real `package_run` and
`verify_run_package` path rather than a hand-built imitation, because a probe against an
imitation proves something about the imitation.
"""
from __future__ import annotations

from pathlib import Path

try:
    from .behavioral_harness import compile_case, package_run, write_prepared_case
except ImportError:  # direct script sibling import
    from behavioral_harness import compile_case, package_run, write_prepared_case

SYNTHETIC_MATRIX = {
    "schema_version": 1,
    "repository": "Borstwerk/KI-Regeln",
    "pinned_commit": "b2-dry-run",
    "classification_minimum": "synthetic",
    "tests": [{
        "test_id": "B2-DRY", "domain": "Verification-Surface",
        "aufgabenfamilie": "verification governance dry run", "testebenen": ["synthetic"],
        "schwierigkeit": "leicht", "nutzerprompt": "Model-free dry run; no model is involved.",
        "fixtures": ["none"], "erwarteter_primaerskill": "verification-loop",
        "erlaubte_secondary_skills": [], "verbotene_skills": [],
        "erwarteter_workflow": "kein vorhandener Vollworkflow", "erwartete_evidence": ["workspace export"],
        "erwarteter_status": "pass", "output_kriterien": ["report.yml present"],
        "failure_modes": ["silent guard change"], "routing_kriterien": ["n/a"],
        "bewertungsmethode": "deterministic", "blindness_klasse": "B1",
    }],
}


def build_dry_run_package(work: Path, export: Path, run_id: str = "dry-run-1") -> Path:
    work.mkdir(parents=True, exist_ok=True)
    compiled = compile_case(SYNTHETIC_MATRIX, "B2-DRY", work)
    prepared = work / "prepared"
    write_prepared_case(compiled, prepared)
    return package_run(prepared, None, None, None, None, work / "runs", run_id,
                       workspace_export=export)
