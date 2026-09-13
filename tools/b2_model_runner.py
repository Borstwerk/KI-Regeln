#!/usr/bin/env python3
"""The public entry point for a Phase 4.2C / B2 writable run.

It reports whether the pilot entry criteria are met and then hands over to the adapter. It
does not authorise anything: an earlier version minted an admission object the adapter
checked for a marker, which any caller could construct, so the authority now lives on the
launch path itself. `execute_prepared_response` evaluates the criteria again immediately
before starting the model process, with the boundary probes re-run rather than read from a
file, and takes no argument that could stand in for that.

`--preflight-only` walks the whole admission path and stops immediately before the model
process would be launched.
"""
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path
from typing import Mapping

try:
    from .behavioral_harness_claude import (
        AdapterError, execute_prepared_response, prepare_writable_launch,
    )
    from .b2_pilot_readiness import evaluate, gate
except ImportError:  # direct script sibling import
    from behavioral_harness_claude import (
        AdapterError, execute_prepared_response, prepare_writable_launch,
    )
    from b2_pilot_readiness import evaluate, gate


def admit(stored: Path | None = None, fresh_probes: bool = True, launch_context=None) -> dict:
    """Evaluate the entry criteria for one launch context and report the outcome.

    Nothing this returns admits anything. The writable adapter path evaluates the criteria
    again for itself immediately before launching, so a caller cannot skip the gate by
    skipping this function, and cannot pass it by constructing a value.

    `launch_context` matters even so: a report produced against the default host context,
    followed by a launch configured with a different binary or a different base environment,
    would describe a run that is not the one about to happen.
    """
    report = evaluate(fresh_probes=fresh_probes, launch_context=launch_context)
    allowed, reason = gate(stored, fresh_probes=fresh_probes, launch_context=launch_context)
    if not allowed:
        raise AdapterError(f"B2 pilot admission refused: {reason}")
    return {"status": report["status"], "reason": reason}


def run(prepared: Path, *, model: str, out_dir: Path, stored_readiness: Path | None = None,
        preflight_only: bool = False, claude_binary: str = "claude",
        base_env: Mapping[str, str] | None = None, **kwargs):
    """Report the admission for this launch context, then launch it. The launch re-checks.

    The binary and the base environment are named here rather than passed through `**kwargs`
    precisely so that the admission cannot be evaluated against one context and the launch
    performed under another.
    """
    with tempfile.TemporaryDirectory(prefix="b2-admit-") as tmp:
        context = prepare_writable_launch(
            claude_binary=claude_binary, base_env=base_env,
            config_dir=Path(tmp) / "claude-config",
            **({"process_runner": kwargs["process_runner"]} if "process_runner" in kwargs else {}),
        )
        outcome = admit(stored_readiness, launch_context=context)
    if preflight_only:
        return {"admitted": True, "status": outcome["status"], "reason": outcome["reason"],
                "stopped_before": "model process launch", "model_started": False}
    return execute_prepared_response(prepared, model=model, out_dir=out_dir,
                                     writable_workspace=True, claude_binary=claude_binary,
                                     base_env=base_env, **kwargs)


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
