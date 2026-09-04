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
from pathlib import Path

try:
    from .behavioral_harness_claude import AdapterError, execute_prepared_response
    from .b2_pilot_readiness import evaluate, gate
except ImportError:  # direct script sibling import
    from behavioral_harness_claude import AdapterError, execute_prepared_response
    from b2_pilot_readiness import evaluate, gate


def admit(stored: Path | None = None, fresh_probes: bool = True) -> dict:
    """Evaluate the entry criteria and report the outcome. Not an authorisation token.

    Nothing this returns admits anything. The writable adapter path evaluates the criteria
    again for itself immediately before launching, so a caller cannot skip the gate by
    skipping this function, and cannot pass it by constructing a value.
    """
    report = evaluate(fresh_probes=fresh_probes)
    allowed, reason = gate(stored, fresh_probes=fresh_probes)
    if not allowed:
        raise AdapterError(f"B2 pilot admission refused: {reason}")
    return {"status": report["status"], "reason": reason}


def run(prepared: Path, *, model: str, out_dir: Path, stored_readiness: Path | None = None,
        preflight_only: bool = False, **kwargs):
    """Report the admission, then launch. The launch re-checks it regardless."""
    outcome = admit(stored_readiness)
    if preflight_only:
        return {"admitted": True, "status": outcome["status"], "reason": outcome["reason"],
                "stopped_before": "model process launch", "model_started": False}
    return execute_prepared_response(prepared, model=model, out_dir=out_dir,
                                     writable_workspace=True, **kwargs)


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
