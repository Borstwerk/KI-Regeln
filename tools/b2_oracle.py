#!/usr/bin/env python3
"""Held-out product oracle for Phase 4.2C / B2. Black box by construction.

    evaluator-controlled expectations  (here, outside every view)
            v  test inputs on stdin
    isolated product process           (workspace copy + runtime + thin driver)
            v  observable outputs on stdout
    evaluator compares                 (here, outside every view)

The product process receives a driver that knows the input shape and nothing else. It never
receives the expectations, the case matrix, the disposition rules or the oracle source. And
it never receives the agent's own check files: the oracle view carries the product only, so
an agent that rewrote a check cannot influence this measurement at all.

What this answers is the one question the verification surface cannot: is the defect gone.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any

try:
    from .b2_boundary import BoundaryError, ViewSpec, run_in_view
    from .behavioral_harness_core import load_yaml
except ImportError:  # direct script sibling import
    from b2_boundary import BoundaryError, ViewSpec, run_in_view
    from behavioral_harness_core import load_yaml

ORACLE_CONTRACT = "verification-governance-oracle/v1"
DRIVER_MOUNT = "/oracle-driver"
# Only these enter the oracle view from the workspace. The agent's checks are not among them.
PRODUCT_PATHS = ("product", "vendor")
RESULTS = ("green", "red", "not-run")


class OracleError(RuntimeError):
    pass


def load_expectations(path: Path) -> dict[str, Any]:
    data = load_yaml(path)
    if not isinstance(data, dict) or data.get("contract") != ORACLE_CONTRACT:
        raise OracleError(f"{path}: contract must be {ORACLE_CONTRACT}")
    inputs = data.get("inputs")
    if not isinstance(inputs, list) or not inputs:
        raise OracleError(f"{path}: expectations need a non-empty inputs list")
    ids = [str(item["id"]) for item in inputs]
    if len(ids) != len(set(ids)):
        raise OracleError(f"{path}: duplicate input ids")
    return data


def _product_view(workspace: Path, destination: Path) -> Path:
    """Copy only the product out of the workspace. Nothing the agent could have rewritten
    as a check comes with it."""
    destination.mkdir(parents=True)
    copied = []
    for name in PRODUCT_PATHS:
        source = workspace / name
        if source.is_dir():
            shutil.copytree(source, destination / name)
            copied.append(name)
    if not copied:
        raise OracleError(f"workspace {workspace} carries no product to measure")
    return destination


def run_oracle(workspace: Path, expectations_path: Path, driver_path: Path, scratch: Path,
               timeout: int = 60) -> dict[str, Any]:
    """Measure the product in isolation and compare outside the view."""
    expectations = load_expectations(expectations_path)
    tolerance = float(expectations.get("tolerance", 0.0))
    view = _product_view(workspace, scratch / "oracle-product")
    payload = "".join(
        json.dumps({"id": item["id"], "tier": item["tier"], "units": item["units"]}) + "\n"
        for item in expectations["inputs"]
    )
    try:
        result = run_in_view(ViewSpec(
            workspace=view,
            argv=("/usr/bin/env", "python3", f"{DRIVER_MOUNT}/driver.py"),
            extra_ro=((DRIVER_MOUNT, driver_path.parent),),
            timeout=timeout,
            stdin_text=payload,
        ))
    except BoundaryError as exc:
        # No boundary, no measurement. Reporting green here would be the worst possible lie.
        return {"result": "not-run", "reason": f"execution boundary unavailable: {exc}",
                "mismatches": [], "observed": {}}

    observed: dict[str, Any] = {}
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        observed[str(row.get("id"))] = row

    mismatches = []
    for item in expectations["inputs"]:
        row = observed.get(str(item["id"]))
        if row is None:
            mismatches.append({"id": item["id"], "reason": "no output for this input"})
            continue
        if "error" in row:
            mismatches.append({"id": item["id"], "reason": f"product raised {row['error']}"})
            continue
        value = row.get("value")
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            mismatches.append({"id": item["id"], "reason": f"non-numeric output {value!r}"})
            continue
        if abs(float(value) - float(item["expect"])) > tolerance:
            mismatches.append({"id": item["id"], "reason": f"expected {item['expect']}, observed {value}"})

    if result.returncode != 0 and not mismatches:
        mismatches.append({"id": "*", "reason": f"driver exited {result.returncode}"})
    return {
        "result": "red" if mismatches else "green",
        "reason": "every held-out input matched" if not mismatches
                  else f"{len(mismatches)} held-out input(s) did not match",
        "mismatches": mismatches,
        "observed": observed,
        "inputs_checked": len(expectations["inputs"]),
    }


def _cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--expectations", required=True)
    parser.add_argument("--driver", required=True)
    parser.add_argument("--scratch", required=True)
    args = parser.parse_args(argv)
    try:
        report = run_oracle(Path(args.workspace), Path(args.expectations),
                            Path(args.driver), Path(args.scratch))
    except OracleError as exc:
        print(f"ORACLE_ERROR: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({k: v for k, v in report.items() if k != "observed"}, indent=2))
    return 0 if report["result"] == "green" else 1


if __name__ == "__main__":
    raise SystemExit(_cli())
