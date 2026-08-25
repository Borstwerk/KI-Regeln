#!/usr/bin/env python3
from pathlib import Path

TARGETS = {
    "task-graph",
    "verification-loop",
    "delegation-contract",
    "agent-eval",
    "docs-plan",
    "technical-writing",
    "reference-docs",
    "web-search",
    "research-plan",
    "claim-verification",
    "skill-review",
}

path = Path("skill-catalog.yml")
lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
changed = []
out = []
for line in lines:
    matches = [sid for sid in TARGETS if f"id: {sid}," in line]
    if matches:
        sid = matches[0]
        if "eval_coverage: partial" in line:
            out.append(line)
            continue
        if "eval_coverage: none" not in line:
            raise SystemExit(f"unexpected coverage state for {sid}")
        line = line.replace("eval_coverage: none", "eval_coverage: partial", 1)
        changed.append(sid)
    out.append(line)

if changed and set(changed) != TARGETS:
    raise SystemExit(f"expected all 11 targets, changed={sorted(changed)}")
if not changed:
    print("coverage already normalized")
else:
    path.write_text("".join(out), encoding="utf-8")
    print("changed: " + ", ".join(sorted(changed)))
