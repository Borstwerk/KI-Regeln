# B2 auth integration and verification boundary — 2026-10-15

This records the PR #75 baseline. For the subsequent runnable WSL host, Linux repairs,
fresh measurements and remaining OAuth skip, see [LINUX-INTEGRATION.md](LINUX-INTEGRATION.md).
The next model-free preparation and unresolved runtime/auth jobs are specified in
[AUTH-BOOTSTRAP.md](AUTH-BOOTSTRAP.md).

## Baseline and scope

The implementation branch was already merged through PR #43. This integration combines
`main` at `6ade166909c0162091cf778db0c9426c259914f4` with the four auth-path commits ending
at `0094a8b996cda42cc2e5cbb14d873d4df1b3c908`. It does not change `verification-loop`,
case semantics, verdicts, trust-root pins, maturity, or the pilot's authorization.

The governing design remains [DESIGN.md](DESIGN.md); the earlier implementation and auth
work is recorded in [IMPLEMENTATION.md](IMPLEMENTATION.md). Existing committed probe files
are **historical evidence** bound to their original code/runtime. They have not been
relabelled with current hashes to simulate a new run. A changed binding must fail closed.

## Reproduced defects and corrections

| Failure | Evidence / cause | Correction |
| --- | --- | --- |
| Intact fixtures fail byte pins on Windows | `core.autocrlf=true`; the case-matrix Git blob and LF-normalized worktree match the committed pin, while the CRLF worktree does not | LF checkout contract for the verification-surface tree and pinned B2 Python components; no pin refresh |
| B2 read-only assertions contradict today's adapter | Tests expect `Read`; current main deliberately exposes `Read,Glob,Grep` for discovery | Independent literal expectations updated; a partial `Read`-only observation must still fail the policy-match check |
| Incomplete managed-policy output can report no provider | Missing sections, truncated output, empty files and failed process results reproduced a false clear verdict | Require every section, final marker and successful process evidence; missingness remains unknown and blocks |
| Managed policy can replace the token without being classified as a provider | A managed `env` block supplies an OAuth token or a host-file/descriptor channel | Classify those keys as credential-provider overrides; persist names only and block the claimed OAuth path |
| Policy/auth diagnostics can persist arbitrary values | Synthetic secret in stderr / an extra auth JSON field survives into the report | Retain process metadata and selected status fields, discard raw auth/policy diagnostic streams |
| The B2 token also reaches read-only launches | Adding it to the global secret allowlist changes the old environment contract | Explicit writable-only opt-in at shared environment preparation; the read-only path still drops it |

The new negative controls failed before their fixes. Known-good policy absence and the
explicit writable-token path continue to pass. These are development/regression controls,
not independent held-out evidence. Review in this session is a same-agent review, not an
independent security approval.

## Reproducible checks

Use the repository's portable Python after the normal local-validation bootstrap:

```powershell
.\Validate-KI-Regeln.ps1 -Full -NoBootstrap
& .\.validation\runtime\venv\Scripts\python.exe tools/b2_test_runner.py --portable --report .validation/b2-portable-report.json
& .\.validation\runtime\venv\Scripts\python.exe -m unittest tests.test_behavioral_harness tests.test_golden_task_behavioral_harness tests.test_behavioral_harness_claude -q
```

`--portable` explicitly selects deterministic B1/design and portable B2 logic controls.
It does **not** certify filesystem confinement, CLI semantics, credential validity or
model-tool enforcement. CI adds this check; it does not replace a full B2 integration run.
No original integration test or ground-truth check was removed, and no new skip was added
to the original suite.

On a suitable Linux host with an installed supported Claude CLI:

```bash
python tools/b2_test_runner.py --integration --report .validation/b2-integration-report.json
```

This mode requires the real namespace provider and CLI before running the **complete**
original B1/B2 suite plus the new controls. Missing prerequisites exit `2` (`BLOCKED`).
Test errors, failures, an empty suite or any skips exit `1`; they cannot produce a pass.
Both modes keep behavioral runs, server authentication and model-level credential
enforcement explicitly `NOT RUN` even when their selected tests pass.

The Windows host used for this integration has no runnable Claude CLI. Its Ubuntu WSL
installation cannot start because virtualization is disabled
(`HCS_E_HYPERV_NOT_INSTALLED`). No OS settings were changed to work around that limit.

Fresh local results on 2026-10-15 for the integrated candidate:

| Check | Result |
| --- | --- |
| Local validation `-Full -NoBootstrap` | PASS, 0 errors, 92 existing warnings; behavioral validation NOT RUN |
| B2 portable runner | PASS, 136 tests, no errors/failures/skips |
| Behavioral/Golden-Task/Claude-adapter regression modules | PASS, 117 tests |
| B2 integration runner | BLOCKED, exit 2 before tests: real Linux provider unavailable |
| Server auth, subprocess scrub and built-in Read enforcement | NOT RUN |

Local logs/reports are in the ignored `.validation/` directory. The full original B2 suite
is not claimed green on this Windows host. Its earlier diagnostic run contained missing-CLI
errors and unavailable Linux tests; portable results do not erase those missing observations.

## Remaining auth / protection work: bounded bootstrap before a writable pilot

Criterion 22 remains unmet. Supplying a token alone cannot fix it: local `auth status`
acceptance is not a service-authentication observation. The code deliberately still has
no path that turns server validity green from a local status or a caller-supplied boolean.

The next runtime stage must be separate from the writable experiment. Its entry conditions
are a live Linux boundary, current real-CLI checks, an explicitly supplied OAuth credential,
and a managed-policy result that establishes the intended credential path. No real token
belongs in arguments, Git, logs or persistent hashes. Do not reopen host-home mounts.

| Required observation | Acceptance evidence | Insufficient evidence |
| --- | --- | --- |
| Server credential validity | A supported operation actually authenticates at the intended service through the confined launch context; compare a real authentication rejection with the synthetic invalid-credential control | `loggedIn`, local canary discrimination, a parser failure, an existing readiness file |
| Subprocess credential isolation | Actual runtime tool-subprocess execution cannot read the provider credential or the parent's process environment; observe the attempted access and result | The scrub variable being set, bubblewrap being installed, a model's statement that it respected the rule |
| Built-in Read protection | The runtime actually receives and denies the attempted process-environment Read under the requested rule | Finding the rule's syntax in the binary or showing the requested deny list |
| Same-context binding | Measurements refer to the binary, filtered environment, controls and filesystem view the eventual launch uses; changed relevant state invalidates them | An attestation or reusable success object supplied by the agent being evaluated |

A missing attempted tool action is `NOT RUN`, not a successful block. The probe must inspect
results outside the model's claims. If a protection fails, discard/redact raw credential-bearing
output in memory before persisting any evidence; record only the observation and failure class.
An authenticated request may be needed to exercise model tools; its concrete supported command
and bounded request cost must be established on that runtime rather than guessed here.

No credential or such runtime is available in this session. These observations have **not**
been performed. Until they are implemented, measured and reviewed, retain
`NOT_READY_FOR_MODEL_PILOT`; a passing portable suite is not admission and carries no
effectiveness claim for the skill.
