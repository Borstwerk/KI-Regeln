#!/usr/bin/env python3
"""The only entry point for a Phase 4.2C / B2 writable run, and the place the gate sits.

A readiness file that nobody consults is documentation. So the admission is minted here, from
a *fresh* evaluation of the entry criteria, and the writable adapter path refuses to start a
model process without one. There is no second public way in: `execute_prepared_response`
raises on `writable_workspace=True` without an admission object carrying the marker, and that
object cannot be built from a stored artifact.

`--preflight-only` walks the whole admission path and stops immediately before the model
process would be launched.
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    from .behavioral_harness_claude import B2_ADMISSION_MARKER, AdapterError, execute_prepared_response
    from .b2_pilot_readiness import evaluate, gate
except ImportError:  # direct script sibling import
    from behavioral_harness_claude import B2_ADMISSION_MARKER, AdapterError, execute_prepared_response
    from b2_pilot_readiness import evaluate, gate


@dataclass(frozen=True)
class Admission:
    """Proof that a fresh evaluation of the entry criteria allowed this run.

    Frozen and marker-carrying on purpose: it is minted by `admit()` and by nothing else.
    """

    granted: bool
    reason: str
    status: str
    marker: str = B2_ADMISSION_MARKER


def admit(stored: Path | None = None) -> Admission:
    """Evaluate the entry criteria now and mint an admission only if they pass."""
    report = evaluate()
    allowed, reason = gate(stored)
    if not allowed:
        raise AdapterError(f"B2 pilot admission refused: {reason}")
    return Admission(granted=True, reason=reason, status=report["status"])


def run(prepared: Path, *, model: str, out_dir: Path, stored_readiness: Path | None = None,
        preflight_only: bool = False, **kwargs):
    """Admit first, then launch. In that order, with nothing between them."""
    admission = admit(stored_readiness)
    if preflight_only:
        return {"admitted": True, "status": admission.status, "reason": admission.reason,
                "stopped_before": "model process launch", "model_started": False}
    return execute_prepared_response(prepared, model=model, out_dir=out_dir,
                                     writable_workspace=True, admission=admission, **kwargs)


def _cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prepared", required=True)
    parser.add_argument("--model")
    parser.add_argument("--out")
    parser.add_argument("--stored-readiness")
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args(argv)
    if not args.preflight_only and not (args.model and args.out):
        parser.error("--model and --out are required unless --preflight-only is given")
    try:
        result = run(Path(args.prepared), model=args.model or "", out_dir=Path(args.out or "."),
                     stored_readiness=Path(args.stored_readiness) if args.stored_readiness else None,
                     preflight_only=args.preflight_only)
    except AdapterError as exc:
        print(f"B2_ADMISSION_ERROR: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result if isinstance(result, dict) else {"out_dir": str(result)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
