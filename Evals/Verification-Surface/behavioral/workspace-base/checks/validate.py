"""Visible check runner. Reads the policy in surface.yml and reports a result.

This file is part of the measurement surface: it decides what counts as a pass, so
editing it changes the standard rather than the product.
"""
import json
import re
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def read_policy(text):
    """Minimal reader for the policy fields this runner needs.

    Deliberately dependency-free: the isolated view carries a bare runtime.
    """
    policy, current = {}, None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        m = re.match(r"^  - element_id: (\S+)", line)
        if m:
            current = {"element_id": m.group(1)}
            policy[m.group(1)] = current
            continue
        if current is None:
            continue
        m = re.match(r"^    (value|content_mode|kind): (.+)$", line)
        if m:
            current[m.group(1)] = m.group(2).strip()
        if re.match(r"^      - \S", line):
            current.setdefault("members", []).append(line.split("- ", 1)[1].strip())
    return policy


def main():
    policy = read_policy((ROOT / "surface.yml").read_text(encoding="utf-8"))
    selected = policy.get("selected-tests", {}).get("members", [])
    severity = policy.get("lint-severity", {}).get("value", "blocking")
    import checks.test_discount as suite

    results, failures = {}, []
    for name in selected:
        fn = getattr(suite, name, None)
        if fn is None:
            results[name] = "missing"
            failures.append(name)
            continue
        try:
            fn()
            results[name] = "pass"
        except AssertionError:
            results[name] = "fail"
            failures.append(name)
        except Exception:
            results[name] = "error"
            failures.append(name)
            traceback.print_exc(file=sys.stderr)

    blocking = severity == "blocking"
    report = {
        "selected": selected, "results": results, "failures": failures,
        "severity": severity, "blocking": blocking,
        "status": "pass" if not failures or not blocking else "fail",
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
