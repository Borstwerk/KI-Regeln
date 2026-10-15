# B2 Linux integration repair — 2026-10-15

Baseline: `56310a3` (PR #75 merged). The user approved the bounded Linux repair plan;
a separate agent reviewed that plan before edits and reviews the final diff. Scope is
test setup, actual runtime-parent observations, current probe evidence and diagnostics.
The execution-mode guard, admission rules, auth criterion, trust pins and case semantics
remain unchanged. Rollback is a revert of this repair; historical evidence is retained.

## Reproduced failures and repair

The first full Linux run executed 278 tests with 7 failures, 7 errors and 2 skips.

| Cause | Repair and controls |
| --- | --- |
| Three hand-built writable packages omit `runtime.execution_mode`; the adapter correctly refuses escalation before the intended assertions | Declare writable in those fixtures. A real package with missing/read-only mode must still stop before any runner call; bypassing the guard makes that control fail. |
| The confinement probe assumes `/opt` exists and treats its absence under an apt `/usr` install as leaked content | Observe existence, errors and the complete directory listing inside the real view. Inspect `/opt` and the actual additional runtime parent. Require absence or exactly the expected runtime directory. Real namespace tests cover `/usr`, `/opt`, six planted siblings and missing/malformed observations. Restoring the old probe makes the regression fail. |
| O3/G1 compare historical code/Python bindings with today's code and Python 3.12 | Execute boundary probes and preflight afresh, serialize to temporary files and verify the resulting bindings. O3 additionally passes the real loader with current evidence and rejects a deliberately changed binding. Committed historical YAML is unchanged. |
| The CA-path test only runs if the operator happens to configure a CA file | Use an actual temporary readable file through the same environment/path logic. This tests path staging, not TLS certificate validity. The separate copy/content controls remain. |
| A skip count hides which observation is absent | Add test IDs and reasons to reports; any skip still prevents PASS. The real-token test is unchanged. |

These are development and regression observations, not held-out evidence of skill efficacy.
Historical shape/content checks remain historical; they do not certify the current host.

## Runtime and privileges

The dedicated WSL2 distro `KI-Regeln-Ubuntu` runs Ubuntu 24.04, Python 3.12.3 and Claude
Code 2.1.292 installed under `/usr`. The Linux checkout is separate from the Windows
working tree, at `/home/raine/src/KI-Regeln`; its venv uses the repository's requirements lock.

The **current** namespace provider needs mount privileges in the caller's namespace.
It does not create a user namespace. On this WSL host the normal `raine` user cannot run
that provider, even though a simple user-namespace probe succeeds. An outer user namespace
also failed at the read-only remount. No kernel restriction was disabled and no extra
capability was granted to that user.

Full namespace tests were therefore run as evaluator-only root in this dedicated test
distro, without real credentials or model requests. This establishes observations for
that privileged test context. It does not certify unprivileged execution, containment
against a determined attacker, or an authenticated model process. A future operator must
choose and review a suitable runtime context before any credential-bearing pilot.

## Reproduce and interpret

From the Linux checkout, with the locked venv and supported CLI available:

```bash
.validation/linux-venv/bin/python tools/b2_test_runner.py --portable --report .validation/wsl-linux-portable-report.json
# In the explicitly chosen evaluator context with mount privileges:
.validation/linux-venv/bin/python tools/b2_test_runner.py --integration --report .validation/wsl-linux-integration-report.json
```

The complete integration suite still includes the operator-token observation A20.
Without `CLAUDE_CODE_OAUTH_TOKEN`, it records that test as skipped and returns exit 1,
even when every executed assertion passes. Do not supply a synthetic token to turn this
real-token observation green. Supplying a real token still would not prove server
authentication or model-tool credential isolation; those require the separate bounded
bootstrap described in [INTEGRATION.md](INTEGRATION.md).

Current validation results are recorded in the repair PR and local ignored reports.
Full integration is not called PASS while A20 is absent. Server authentication,
credential subprocess isolation, built-in Read enforcement and behavioral evals remain
`NOT RUN`; criterion 22 and `NOT_READY_FOR_MODEL_PILOT` remain in force.
