# B2 authentication bootstrap preparation

Baseline: `1be63377bc14c6aec24157bbc4915a20ea19b193` (PR #76 merged).
Scope: a model-free diagnostic prefix and a reviewed measurement contract. It does not
implement authentication, launch a model, change admission or consume credentials.
The subsequent explicit credential-free runtime option and its measured limits are in
[RUNTIME-SEPARATION.md](RUNTIME-SEPARATION.md); the classic diagnostic below is retained.
Its subsequent credential-free descriptor handoff is described in
[ENVIRONMENT-TRANSPORT.md](ENVIRONMENT-TRANSPORT.md); live authentication remains unadmitted.

## Runtime decision before credentials

Use two distinct roles for the eventual runtime:

| Role | Required rights / observation | Current state |
| --- | --- | --- |
| Trusted evaluator / view setup | Establish the mount/PID view and inspect results outside the evaluated workspace | Current provider requires mount privileges; measured in the dedicated WSL test distro |
| Credential-bearing CLI / its tools | No zero real/effective/saved/filesystem UID or GID, no root supplementary group, zero inheritable/permitted/effective/ambient capabilities, `NoNewPrivs=1` | Current shared view inherits evaluator root; blocked for bootstrap preparation |

The identity conditions are a conservative preparation floor, not a complete sandbox
definition. In particular, a root UID inside a future user namespace would still be refused
by this version; it makes no claim about that namespace's host-level privileges.

The current provider does not separate those roles. Dropping a UID alone would also leave
the nested `check` mount path unresolved. This PR therefore measures and refuses the
current context instead of adding a privileged credential-bearing launch or changing
kernel restrictions, capabilities, sudo policy or the existing boundary. A following
runtime slice must implement and review role separation **and** demonstrate that nested
checks and the CLI's credential-scrub mechanism still work in that context, first with
synthetic controls. No authenticated run is enabled by this preparation.

## What the command actually does

From a Linux checkout with the installed binary available for binding:

```bash
.validation/linux-venv/bin/python tools/b2_auth_bootstrap.py --prepare-only --report .validation/b2-bootstrap-report.json
```

The command:

1. Refuses known credential/provider environment channels in either the actual host
   environment or an explicit API environment. An explicit empty environment cannot hide
   an ambient token. Only known variable names appear in the refusal.
2. Resolves and hashes the CLI file without executing it. No `--help`, `--version`,
   `auth status`, login, arbitrary prompt or model command is run.
3. Uses the adapter's shared environment controls with a fixed minimal process environment.
   No caller proxy, endpoint, CA-file path, arbitrary customization or credential value is
   inherited. Files/configuration visible in the shared runtime binds are **not** audited;
   the fixed Python payload does not read them or execute their providers.
4. Builds the existing `confined_model_invocation` with a fixed trusted Python payload.
   The shared mount/PID contract and payload-start marker are used without fallback.
   The view's network namespace remains shared, as in the model contract; the fixed
   payload performs no network operation. This is not a network-isolation observation.
5. Reads only selected fields from `/proc/self/status`, checks the complete fixed schema,
   and classifies identity/capability observations. Missing fields, booleans in integer
   fields, extra data, failed processes, missing markers and timeouts cannot pass.

The field meanings follow the Linux kernel's [/proc documentation](https://docs.kernel.org/filesystems/proc.html)
and [No New Privileges contract](https://docs.kernel.org/userspace-api/no_new_privs.html).
No raw subprocess stdout/stderr, exception diagnostics, token values, token hashes,
caller environment values or host config paths enter the report.

| Result | Exit | Meaning |
| --- | --- | --- |
| `BLOCKED` | 2 | Preparation could not establish the identity floor or was refused before running |
| `PREPARED_ONLY` | 0 | Identity observation satisfies this floor; every live operation remains unapproved and unmeasured |

Both results carry `may_start_authentication=false`, `may_start_model_pilot=false`,
`report_is_admission=false`. `PREPARED_ONLY` is **not** `READY_FOR_MODEL_PILOT`.
The report is not read by the writable admission path. Code/binary digests describe this
diagnostic snapshot only; they do not attest to an authenticated CLI or a future launch.
Claude execution, authentication and behavioral evals remain `NOT RUN` even in a successful
synthetic preparation test. `requested_tool_policy` describes requested controls, not
observed tool enforcement.

## Subsequent measurement jobs and acceptance

All of these jobs remain `NOT RUN` in this PR. They are separate from the writable pilot.

| Job | Required evidence before completion |
| --- | --- |
| Runtime privilege separation review | Actual evaluator/CLI identities, capabilities, fresh confinement controls and working nested checks; missing rights must block |
| Supported request and budget review | A verified supported operation, selected model if needed, bounded calls/cost, deadlines and a reviewed operator command; no arbitrary shell/prompt API |
| Managed credential path | Actual policy read inside the eventual CLI view establishes the intended provider; ambiguity blocks |
| Server authentication | A real service-authenticated operation through the intended credential path; local `auth status` is insufficient |
| Invalid credential rejection | Rejection attributable to the service rather than local parsing; missing authentication observation cannot certify validity |
| Subprocess credential isolation | Actual tool execution attempts to inspect both its environment and the parent's process environment; observed results evaluated outside model claims |
| Built-in Read enforcement | Actual attempted built-in Read of the process environment and observed denial; an omitted attempt is `NOT RUN` |
| Authenticated context binding | Observations bind the binary, filtered environment, controls and filesystem context of the eventual launch; changes invalidate them, no reusable caller attestation |

The future collector must discard/redact credential-bearing raw results **before**
writing artifacts. A missing attempted action, an invalid control or an unobservable
result stays open. Neither this report nor a caller-supplied boolean may turn criterion
22 green. Login, token supply and any bounded authenticated/model request are later
operator steps after the runtime and measurement implementation are reviewed.

## Tests and rollback

Portable tests use fixed observations and synthetic credential strings; they prove
classification, early refusal and output hygiene, not runtime isolation or skill efficacy.
The complete integration runner additionally executes a real fixed-payload identity test
through the shared namespace boundary. Its original real-token test remains unchanged,
and a skip still prevents PASS. No existing tests, trust pins or historical evidence are
removed or relabelled. Rollback removes this separate preparatory command, tests and runner
registration; the existing admission path remains intact.
