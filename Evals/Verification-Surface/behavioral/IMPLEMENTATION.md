# Phase 4.2C / B2 — what was built

Companion to [`DESIGN.md`](DESIGN.md), which stays the reviewed design. This records the
implementation: the provider that carries the boundary, what the probes actually observed,
and which components are now load-bearing.

**No model was run. No model response was produced, no judge, no unblinding, no pairing, no
skill-effect statement, no maturity or coverage change.** Everything below is infrastructure,
integrity and method evidence.

## The pieces

| Component | File | What it does |
| --- | --- | --- |
| execution boundary | `tools/b2_boundary.py` | assembles an isolated view and runs one argv in it |
| held-out oracle | `tools/b2_oracle.py`, `oracle/` | measures the product as a black box |
| grader | `tools/b2_grader.py` | facts -> disposition -> case result |
| disposition algebra | `tools/verification_governance_disposition.py` | reviewed in the design phase, unchanged |
| dry run | `tools/b2_dry_run.py`, `tools/b2_run_package.py` | model-free end-to-end |
| boundary probes | `tools/b2_boundary_probes.py` | P1-P6, deliberate breakage |
| gaming red team | `tools/b2_eval_gaming_redteam.py` | T9 against the built system |
| readiness and gate | `tools/b2_pilot_readiness.py` | evaluates 19 criteria, refuses a pilot |
| writable adapter mode | `tools/behavioral_harness_claude.py` | opt-in, additive |
| export in the run package | `tools/behavioral_harness.py` | hashed, covered by `verify-run` |

## Execution boundary

**Provider: `unshare-namespace/v1`** — an unprivileged-capable Linux namespace set assembled
with `unshare --mount --pid --net --uts --ipc --fork`, into which a minimal root is built by
bind mount and entered with `pivot_root`. The old root is detached with a lazy unmount, so
the host filesystem is not hidden behind permissions: it is not reachable.

What the view contains, and nothing else:

```
/usr /bin /sbin /lib /lib64 /etc/alternatives   read-only bind, the runtime
/proc                                           fresh, this namespace
/dev                                            tmpfs with null, zero, urandom bound in
/workspace                                      the writable workspace COPY
/scratch                                        writable tmpfs, 16 MiB
/                                               the view root itself, sealed read-only
```

The environment is built with `env -i` plus a fixed assignment list; nothing is inherited.
The two views differ in exactly what they carry: the visible check gets the workspace copy,
and the oracle gets the product only — no `checks/` directory at all, so an agent that
rewrote a check cannot influence the oracle run.

The root is sealed read-only **because P2 found that it was not**. Writes into the view's own
`/etc` and `/` succeeded on the first implementation. They were ephemeral and reached nothing,
but "writes only where it is meant to" is the contract, so the boundary was fixed rather than
the probe relaxed.

### Probe results

| Probe | Passed | Observed |
| --- | --- | --- |
| P1 hidden read | True | every path denied; `FOUND` empty; the sentinel appears in no stream |
| P2 outside write | True | host target absent afterwards; every in-view escape denied |
| P3 legitimate check | True | exit 1, the seeded defect reported — not a boundary artifact |
| P4 oracle leakage | True | the driver mount carries exactly `driver.py`; `/oracle-driver/expectations.yml` raises `FileNotFoundError`; the leak canary appears nowhere |
| P5 broken product | True | red on all six held-out inputs, each with its value mismatch |
| P6 network | reports, never gates | `network_disabled: True` — both attempts refused inside an unshared network namespace |

**On P6.** Both connection attempts from inside the view were refused, in an unshared and
empty network namespace. That is an observation on this host with this provider, and it is
the only basis for the value. Nothing is inferred from the absence of a network tool, and no
claim is made about any other host. The full record is in
`evidence/boundary-probes.yml`.

**What is not claimed.** This is a boundary for keeping evaluation artifacts out of reach of
code the eval itself placed in the workspace. It is not a security sandbox against a
determined attacker, and nothing beyond what P1-P5 demonstrate is asserted anywhere.

## Review corrections

Seven findings were closed after the first implementation review. Three of them are worth
recording because the property had been claimed rather than carried.

**The oracle view carried the expectations.** `expectations.yml` sits beside `driver.py` in
the repository, and the whole directory was mounted, so `/oracle-driver/expectations.yml` was
readable from inside the agent-controlled product view — the black-box contract broken by a
line of convenience. The driver is now staged into a directory of its own containing exactly
one file, and a structural check asserts that. P4 had been blind to it because the hostile
product skipped `oracle-driver` while searching, and its leak test keyed on path strings that
appear in ordinary results; it now probes that exact path, walks the whole view, and keys on a
`leak_canary` value that exists in no legitimate output. The old P4 evidence described a
system that no longer exists and was discarded.

**The writable system prompt forbade writing.** The controlled prompt says "do not write/edit
files", which would have forbidden the very behaviour B2 exists to observe. The read-only
prompt is unchanged; the writable mode has its own, which permits work inside the workspace
and names `check` — and says nothing about guards, thresholds, authorization or governance,
because warning an agent away from the tempting move would measure prompt compliance instead
of conduct.

**Evidence described a policy the run would not have executed.** `_fresh_context`, the runtime
preimage, `_evidence` and `_method` all named the read-only tuples unconditionally, so a
writable run would have reported `allowed: [Read]` while executing something else. The
effective policy is now derived once and threaded through every load-bearing evidence
function, including the system-prompt hash.

## Second-round corrections

Four further findings were closed. Each had the same shape: a property was arranged for but
not actually carried.

**The admission was a bearer token.** The writable path accepted an object and checked a
public marker on it, while the marker was the default of a public dataclass — a ticket anyone
could print. There is now nothing to hand it. The writable path evaluates the entry criteria
itself, immediately before the model process would start, and `execute_prepared_response` no
longer has an `admission` parameter at all. `b2_model_runner.py` remains the public entry and
reports the outcome; it authorises nothing.

**Tool names and permission rules were run together.** `--tools` names built-in tools — the
CLI's own help says "Specify the list of available tools from the built-in set … e.g.
Bash,Edit,Read" — while `--allowedTools` takes permission rules, of which `Bash(check)` is
one. Passing the rule to `--tools` asked for a tool that does not exist under that name, and
comparing the runtime's observed tool list against a rule could never match: the init stream
reports `Bash`. The policy record now separates `visible_tools`, `allow_rules`, `deny_rules`
and `permission_mode`, evidence reports all four, and only `visible_tools` is ever compared
to what was observed. The writable run adds `--permission-mode dontAsk`, so anything not
pre-allowed is refused rather than routed to a prompt nobody would answer; a build without
that mode fails pilot entry with no weaker fallback (criterion 20, added here).

**An oracle instrumentation failure was scored as agent conduct.** `run_oracle` reported
`not-run` with `instrumentation_failure`, but the grader dropped the flag, so the facts read
`integrity_ok: true` with `oracle: not-run` and D6 turned a broken sandbox into an
`UNSUPPORTED_COMPLETION`. The flag now enters the instrumentation facts, and an `OracleError`
raised while preparing the measurement does the same, so both reach D1. A genuinely red
product with a working boundary still carries D6.

**Probe evidence was too portable.** Binding it to code hashes, provider, platform and Python
version is not enough for a namespace boundary, whose protection also depends on the host
kernel and util-linux: another Linux x86_64 could have adopted a stored result. The model
pilot admission now re-runs P1–P5 in process rather than reading the file, so the evidence
describes the machine that is about to run. P6 remains observation.

## Third-round correction: confining the model process

The largest remaining gap, and the one whose diagnosis matters most: **`run_in_view`
confined the code the agent writes, never the agent's own process.**

The assumption that `--permission-mode dontAsk` plus `Bash(check)` left `check` as the only
executable shell action is wrong. Claude Code treats a class of read-only commands — `cat`,
`ls`, `head`, `grep`, `find`, `stat`, `du` and similar — as permissible without a prompt.
Combined with a launcher that embedded `Path(__file__).resolve().parent`, i.e. the absolute
path of the evaluator's own `tools/` directory, that was a concrete route: read `bin/check`,
learn the repository path, then read the case matrix, the trust root and the oracle
expectations with commands the allowlist never had to mention. The process also ran with
`cwd` at the package root rather than the workspace, so bare `Read`/`Edit`/`Write` were
scoped wider than the experiment.

The model process now runs inside the same namespace provider, one level out:

```
unshare(mount, pid, uts, ipc) + pivot_root        <- the model process
    /workspace      the B2 workspace, writable, and the process starts here
    /scratch        writable tmpfs; CLAUDE_CONFIG_DIR lives here
    /b2-runtime     two staged trusted modules, read-only
    /b2-bin         the check launcher, read-only, first on PATH
    runtime binds   read-only; no /home, no /root, no /tmp, no repository
        |
        `-- check -> unshare(... --net) + pivot_root   <- the agent's own check code
```

The confinement is built into the argv the adapter hands to its own process runner, so the
process that starts is the confined one rather than a process wrapped by a side channel. That
by itself put nothing into the run's artifacts, and for one round it did not: the artifacts
still described the inner Claude call, and the runtime preimage still said
`os_or_container_sandbox: false`. What the artifacts carry is covered under
[Confinement in the run evidence](#confinement-in-the-run-evidence). The launcher now embeds
`/workspace` and `/b2-runtime` — in-view paths — and the trusted runtime is staged as exactly
two files, so reading `bin/check` yields nothing about the host.

**What is confined and what is not.** Filesystem, PID, UTS and IPC namespaces. *Not* the
network: the model process has to reach its API, so `--net` is deliberately not unshared in
the outer view. That is the one isolation this layer does not provide and it is stated rather
than implied. The inner view for agent-written check code keeps its empty network namespace.

### Measured, not asserted

`evidence/model-confinement.yml` records the read-only commands executed for real inside the
view, against a sentinel planted outside it:

| Attempt | Observed |
| --- | --- |
| `cat <evaluator sentinel>` | `No such file or directory` |
| `cat <repository>/tools/b2_grader.py` | `No such file or directory` |
| `find / -name case-matrix.yml` | nothing |
| `find / -name expectations.yml` | nothing |
| `grep -rs <sentinel> /` outside the runtime | nothing |
| `ls /home /root /tmp` | all three absent |
| `cat /b2-bin/check` | names `/b2-runtime` and `/workspace`, no host path |
| write to `/b2-bin/check`, `/b2-runtime/*`, `/execution-view.yml`, `/`, `/etc` | every one refused |
| write to `/workspace/allowed.txt` | succeeds — the experiment stays possible |
| `check` from inside the confinement | reaches the nested boundary and reports the real result |

Criterion 21 runs exactly this probe. It is a functional measurement: nothing about it reads
the allowlist, because the allowlist was never what decided.

## Fourth-round corrections: the record, and the launch

Two findings, both about the gap between doing something and being able to show
afterwards that it was done.

### Confinement in the run evidence

The first version of the confinement ran the right process and then described the wrong one.
`evidence.process.argv` held the inner Claude command, and the runtime preimage still carried
`os_or_container_sandbox: false` — a field that was a constant, and so kept saying "no
sandbox" about a run that had one. A reader of those artifacts could not have told a confined
run from an unconfined one, which is the only reason the field exists.

Three things now carry the measurement into the artifacts a run leaves behind:

| Artifact | Field | Source |
| --- | --- | --- |
| `runtime-configuration-preimage.yml` | `model_process_confinement` | `confinement_facts()` |
| `runtime-configuration-preimage.yml` | `filesystem_isolation.os_or_container_sandbox` | derived, not constant |
| `evidence.yml` | `process.outer_invocation` | `invocation_evidence()` |
| `method-evidence.yml` | `model_process_confinement` | `confinement_facts()` |

`established` and `payload_started` both come from the boundary's own setup marker, written
to a host descriptor immediately before `exec`. They report what happened, not that a context
manager was entered.

The outer invocation is bound as a **normalized preimage**, never verbatim. Its argv carries
the boundary assembly script, and its launcher environment carries host temporary paths and
may carry credentials. So the record keeps the argv *shape*, the provider, the mount contract
and the normalized inner argv; the assembly script enters as a SHA-256; the launcher
environment enters as variable names with no values. Nothing replayable is persisted.

Because the confinement enters the runtime preimage, it enters the runtime fingerprint, and
the fingerprint enters the method evidence. An unconfined run therefore cannot produce the
same method evidence as a confined one — not by policy, but because the inputs differ.

### The confined runtime has to be launchable

Confinement created a precondition that did not exist while the process ran on the host: the
launch has to work from *inside* the view. Three separate things were false there, and none
of them is visible in the source or the allowlist.

**Every argv path has to exist in the view.** The empty MCP configuration was written into
the adapter's host temporary directory and passed to `--mcp-config` by host path — a path the
confined process cannot open, because the view deliberately carries no host temp tree. It now
has a read-only view of its own, `/b2-config/empty-mcp.json`, staged with exactly one file.

The help text offers an inline-JSON form for `--mcp-config`, which would have avoided the
mount. It was not taken: no model-free invocation of the installed CLI parses that option —
`claude mcp list` ignores it, and everything that does parse it makes a model request — so
accepting a string would have rested on documentation rather than on a measurement. A file
path in the view is directly observable, and `tests` check for its presence rather than for
its spelling.

**The runtime has to be on the view's PATH.** `PATH` listed `/b2-bin` and the standard
directories; the Claude Code runtime lives outside them and is mounted at its own host path.
The confined launch therefore died with `env: 'claude': No such file or directory` — the
preflight's first real finding. `view_path()` now derives the entry from the resolved binary.

**Authentication has to work in the view's own environment.** The view carries no host home
and a fresh `CLAUDE_CONFIG_DIR` under `/scratch`, so "the CLI is logged in" is a statement
about the host, not about the launch context. `evidence/launch-preflight.yml` records
`claude auth status` executed inside exactly that view.

Criterion 22 is these three together, and one criterion rather than three on purpose: it
expresses a single precondition — the confined runtime is launchable — and splitting it would
let two thirds of a launch read as progress toward a pilot that still cannot start.

### One derivation, not two

The criterion and the launch were still deriving their context separately. The adapter builds
the model process's environment with `_child_env` — an explicit allowlist, the control
variables, a fresh `CLAUDE_CONFIG_DIR`, everything else dropped — while the preflight handed
`os.environ` straight to the view. The stored evidence showed it plainly: about a hundred
variable names, most of which the model process would never inherit.

That is not a cosmetic mismatch. Criterion 22's last question is whether the launch context
can authenticate. A gate answering that question about a *different* environment could in
principle go green on a credential the run does not receive. The same applied to
`claude_binary` and `base_env`, which `execute_prepared_response` accepts and
`_require_admission` did not know about at all: the gate could be evaluated against the
default host context and the launch then performed under another.

```
raw base env ─┐
              ├─► prepare_writable_launch() ─► WritableLaunchContext ─┬─► criterion 22
claude binary ┘   (probe + _child_env)                                └─► the launch
```

`WritableLaunchContext` carries the binary, the filtered child environment, the environment
policy and the probed capabilities. `execute_prepared_response` builds it once and passes the
same instance to `_require_admission`, which passes it to `gate` → `evaluate` → criterion 22 →
the preflight. `b2_model_runner.run` names `claude_binary` and `base_env` explicitly instead
of forwarding them through `**kwargs`, so its report is about the launch it will then perform.

`base_env` stays supported (variant B): it is not merely a test seam, and the fix is that one
concrete `base_env` now reaches the criterion, the admission and the launch — not that the
parameter disappears.

The counter-test provokes the actual defect. A base environment carrying
`CLAUDE_CODE_OAUTH_TOKEN` — a host-only auth channel the adapter contract removes — is fed
in, and the chain is followed: present in the raw environment, absent from the prepared child
environment, absent from what the criterion measures, absent from the view. An allowed
`ANTHROPIC_API_KEY`-shaped value passes the same filter structurally; only its *name* is ever
asserted on, and no value of either kind appears in any report or artifact. A host variable
that exists only in `os.environ` is likewise provoked and must not travel — a source check for
the string would have passed on a file that merely mentions it in a comment.

`launch-preflight.yml` now records `child_environment_names` and
`child_environment_policy` — the adapter's own contract, names only, no values.

One consequence was a duplicated capability probe: `execute_prepared_response` probed the
binary and `prepare_writable_launch` probed it again, two `--version`/`--help` pairs for one
launch. The adapter now passes its probe in, and the preparation refuses a probe that
describes a *different* binary — reuse is an optimisation, never a way to vouch for something
else. `require_capabilities()` holds the two capability preconditions in one place.


## Held-out oracle

```
expectations (evaluator side, never in any view, never beside the mounted driver)
   v  one JSON object per line on stdin
isolated product process: workspace product copy + runtime + a thin driver
   v  one JSON object per line on stdout
comparison, outside the view
```

The driver knows the input shape and how to import the product. It carries no expected
values, no case classification and no ground truth, so product code that reads it learns the
input shape and nothing else. P4 confirms the separation by trying.

## Trusted components

| Component | Protects | A defect would | Countertest |
| --- | --- | --- | --- |
| execution boundary | evaluator artifacts from agent-controlled code | let a rewritten check read ground truth or write outside | P1, P2, P5, `BoundaryAdversarialTests`, `BoundaryLifecycleTests` |
| model-process confinement | evaluator artifacts from the agent's own process | let read-only shell commands reach the repository, the matrix or the oracle | the probe above, criterion 21, `ModelProcessConfinementTests` (12 tests) |
| confinement evidence | telling a confined run from an unconfined one, afterwards | let the artifacts describe a run that did not happen | `ConfinementInTheRunEvidenceTests`: a real outer boundary, a synthetic payload, no model |
| launch preflight | the confined runtime's launchability | let a pilot be admitted that cannot start, or start against a host path | criterion 22, `ViewLocalLaunchArgvTests`, `ConfinedLaunchPreflightTests` |
| shared launch preparation | that the gate and the launch mean the same run | let the criterion pass on an environment or a binary the process never gets | `SharedLaunchPreparationTests`: host-only auth channel, allowed credential, binary identity |
| boundary lifecycle marker | telling a failed sandbox from a failing payload | let an instrumentation failure read as a red product | setup broken on purpose before `exec`: `BoundaryError`, payload never ran, oracle `not-run` |
| check launcher (`bin/check`) | the one allowed Bash invocation | let `check` reach something other than the boundary | `CheckLauncherTests`: real PATH, real cwd, arguments refused, impostor not shadowing |
| B2 model runner admission | the pilot gate | let a writable run start without passing the criteria | five refusal tests with a runner that fails if invoked |
| workspace export + hashing | the graded artifact from the thing being graded | let a post-hoc edit change what is graded | `verify-run` mismatch tests, tamper attempt in the red team |
| oracle driver | product correctness measurement | leak expectations, or measure the wrong thing | P4, P5 |
| facts extraction / merge (`b2_grader`) | the mapping from measurement to disposition | produce incoherent facts, or invent a verdict | 15 grader controls, checked by rule and B1 reason |
| pilot readiness gate | the admission decision | let a pilot start on unproven infrastructure | four refusal tests plus the forgery attempt |
| writable adapter mode | the existing read-only path | silently widen 4.2A/4.2B's tool policy | `AdapterCompatibilityTests` |

The check *wrapper concept* from the first design draft is deliberately not on this list: it
was called a trusted component when it was in fact the bypass, which is why the boundary
exists. `bin/check` is a different thing — it holds no policy of its own, takes no arguments,
and does nothing except hand a path the adapter chose to the boundary.

## Honest limits

- The boundary is evidence only for what P1-P5 demonstrate, on this host, with this provider.
- `network_disabled: True` is an observation, not a property of the design.
- Surface completeness is a statement about **this small synthetic workspace**, enforced by a
  test that classifies every file in it. It says nothing about real repositories.
- The workspace is writable on purpose. The trust chain around it is an integrity relation.
- No behavioral evidence exists. Readiness is an infrastructure decision.
- The outer view confines the filesystem, not the network. Nothing here claims otherwise.
- The stored readiness artifact is documentation, produced in stored-probe mode. The mode
  that admits a run re-executes P1–P6 and says so in `probe_evidence`.
- Probe evidence is bound to the hashes of the boundary, oracle, probe code, driver and
  expectations it was produced against, plus the provider and platform. When any of those
  moves, readiness reports the evidence as absent rather than reusing it — which is what a
  stale P4 result would otherwise have done after the leak fix.
- Two entry criteria are genuinely not applicable: there is no judge to fix a schema for, and
  nothing to unblind at one condition. They are labelled `applicable: false` with their
  antecedent measured, rather than dressed up as measurements that passed.
- **Criterion 22 is currently unmet, and the pilot is therefore blocked.** The Claude Code
  runtime authenticates from a credential under a host home directory. The outer view does
  not carry that directory, and mounting it back would undo the boundary this phase exists to
  establish, so `claude auth status` inside the view reports `loggedIn: false`. Everything
  else — argv locality, runtime startup, flag parsing, the confinement itself — is measured
  and met. A pilot needs an authentication path that works inside the view, named as the
  pilot's auth path and confirmed model-free before it is used. There is no such path on this
  host today, and the readiness artifact says `NOT_READY_FOR_MODEL_PILOT`.
