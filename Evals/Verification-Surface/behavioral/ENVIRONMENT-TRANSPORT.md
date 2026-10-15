# Credential-free environment transport preparation

Baseline: `15ecfdb0c17d606c268d669d65443fdc90b81f92` (PR #82 merged).
This slice prepares a transport for the explicit separated diagnostic runtime.
It does not admit credentials, authenticate a CLI, start a model or change criterion 22.

## Problem and bounded change

The classic namespace provider embeds its payload environment in the setup shell's argv.
That is unsuitable for future credentials. The separated diagnostic now carries its
dynamic environment in `sealed-memfd-environment/v1`; the classic default and writable
adapter remain unchanged. Known credential/provider variables are still refused in the
actual ambient and supplied environment before tool checks, snapshots or descriptors.

| Stage | Control |
| --- | --- |
| Evaluator | Validate a string-to-string mapping, at most 128 entries and 64 KiB of UTF-8 JSON; no NUL values, only ASCII environment identifiers |
| Transport | Create an anonymous Linux memfd with a fixed non-sensitive name; handle partial writes; seal writes, growth, shrinkage and further seal changes before handoff |
| Descriptor | Duplicate with close-on-exec to a descriptor of at least 10, close the original, and pass only that descriptor explicitly via `pass_fds` |
| Setup and privilege drop | Keep only the fixed `VIEW_ENV` in the setup command; run the fixed isolated system-Python helper after the existing UID/GID/capability/NoNewPrivs controls |
| Receiver | Require a regular, bounded, fully sealed descriptor; bounded `pread`; reject malformed UTF-8, duplicate JSON keys and invalid environment shape |
| Payload exec | Close the descriptor before replacing the helper with the original target and its decoded environment |
| Context exit | Close the evaluator's descriptor on success, failure or interruption |

Descriptor 3 remains reserved for the existing setup marker. The new `ConfinedInvocation`
field defaults to an empty `pass_fds` tuple for classic callers. The separated executor
propagates the descriptor explicitly; omitting it blocks before the target can execute.
No transport file is created in the workspace, scratch or staged runtime. The staged
trusted-runtime allowlist remains exactly its original two modules. The fixed helper
code and descriptor number are public argv; the serialized dynamic environment is not.
Existing constant startup values remain visible. This mechanism does not scrub values
that a caller explicitly puts in the target's own argv, stdin or output.

The preparation report also binds the transport module's digest. It still reports
`PREPARED_ONLY`, authentication/model permissions false and pending auth jobs `NOT RUN`.
Neither this report nor the new contract string is pilot-admission evidence.

## Bounded execution and cancellation

The separated preparation controls use one executor with a new process session. Timeout
or interruption signals only the session group belonging to its successfully created
process, then performs bounded collection/reaping. Errors have fixed diagnostics without
captured stdout/stderr. The descriptor context closes independently on exit.

A real control reaches the non-root payload after environment handoff and verifies that
its transport descriptor is closed. It then deliberately times out. The evaluator checks
that the monitor and namespace init are no longer live and that neither a dead child nor
the evaluator retains the transport descriptor. An adopted zombie is distinguished from
a live process; this is not a promise that the evaluator can reap non-child processes.

This observation covers the fixed preparation/identity/check startup path. It does not
certify cancellation of an arbitrary future model process whose namespace init deliberately
leaves the process group with `setsid`. Such model-runtime lifecycle and cancellation
paths require their own implementation and evidence before live admission. No claim
relies solely on `unshare --kill-child`: a parent-death signal may be cleared by credential
identity changes, so the executor explicitly controls its own process group.

## Verification and negative controls

Portable tests cover input/byte/entry refusal, literal data encoding, unavailable Linux
transport, classic defaults, static bootstrap construction, early start failure and
bounded cleanup on timeout/interruption. The full integration retains every original B2
test and adds these real Linux controls to the existing credential-free child suite:

- Actual seals refuse write, truncate, growth and further seal changes. Parent descriptors
  close on normal and exceptional exits.
- Missing and unsealed descriptors, malformed UTF-8/JSON, duplicate keys, NUL/non-string
  values and oversized input cannot run a target marker. Diagnostics are static.
- A synthetic canary with quotes, shell metacharacters, a newline and Unicode arrives
  literally. It is absent from the setup argv/environment and invocation representation;
  no shell command planted in it executes. The payload has no inherited transport fd.
- A timeout after observed non-root handoff leaves no live monitor/init or open transport
  descriptor in the measured processes.

The preceding identity, nested red/green checks, evaluator-sentinel, writable-location,
inner environment/PID/network isolation and CLI startup controls remain active. The
original real-token test remains present; a missing-token skip still prevents full PASS.
No historical evidence, trust pin or skill maturity is changed. These are development
and regression controls, not held-out skill-effectiveness evidence.

## Remaining boundaries

The memfd has no filesystem directory entry; it is not encrypted storage or a guarantee
against swap, core dumps, root, same-user host inspection or process-memory inspection.
The trusted evaluator retains its own descriptor until its context closes. The child
receives its environment intentionally; this is not Claude Bash credential-scrub evidence
or built-in Read enforcement. On-disk managed policy is still unverified by this path.

Actual secret intake, managed-policy admission, service authentication and invalid-token
rejection, supported request/budget review, authenticated-context binding, general model
cancellation, real tool subprocess/Read controls and workspace export/adoption remain
separate jobs. No real credential or service/model request is used for this slice.

Rollback removes the new separated environment handoff and executor, restores that
diagnostic's preceding construction and removes its added controls. Classic invocation,
writable admission, grading and trust roots do not change.

Implementation references: [memfd and seals](https://man7.org/linux/man-pages/man2/memfd_create.2.html),
[explicit descriptor inheritance](https://docs.python.org/3.12/library/subprocess.html),
[parent-death signal limits](https://man7.org/linux/man-pages/man2/PR_SET_PDEATHSIG.2const.html).
