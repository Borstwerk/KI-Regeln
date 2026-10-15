# Credential-free runtime separation

Baseline: `dd0a77d22ac5cbdf185f703a0cc83070f88d9174` (PR #80 merged).
The preparation from PR #77 remains valid. This slice adds an explicit opt-in diagnostic
runtime; the existing writable adapter, pilot admission and criterion 22 stay unchanged.

## Runtime contract

`nonroot-unshare-view+userns-check/v1` has two roles:

| Role | Implementation / observed floor |
| --- | --- |
| Trusted evaluator | Establish the outer mount/PID view with the existing provider; create a private workspace snapshot |
| Outer payload | `setpriv` changes all real/effective/saved/filesystem UID/GID values to 1000, clears supplementary groups, drops inheritable/permitted/effective/ambient and bounding capabilities, sets `NoNewPrivs=1` |
| Nested `check` | A fixed bubblewrap invocation creates user/PID/network/UTS/IPC namespaces, drops capabilities and executes only `/workspace/checks/validate.py` with the fixed check environment |

UID/GID 1000 is a fixed policy for this opt-in slice, not a caller-controlled privilege
argument. The outer provider does not create a user namespace; its observed payload IDs
therefore reflect the actual non-root identity rather than mapping host root to another
number. The nested user namespace keeps that nonzero identity. The original evaluator
still needs mount privileges. No user capabilities, sudo rules, setuid helpers or kernel
restrictions are changed. The selected system `setpriv`/`bwrap` files must be root-owned
regular files without group/other write access, setuid/setgid bits or file capabilities.
An unreadable capability state blocks instead of being treated as absent.

The outer root remains read-only. Only its private workspace copy and UID/GID-owned
scratch tmpfs are writable. An **empty read-only `/tmp` directory** is created before
sealing because bubblewrap 0.9 uses it as its construction mountpoint. No host `/tmp` is
mounted. The inner view carries the fixed check-runtime binds, workspace, private proc,
the existing null/zero/urandom devices and scratch. `/etc` contains only the parent needed
for the existing `/etc/alternatives` runtime bind. The inner root is read-only, while its
workspace and scratch remain writable. The outer network remains shared; only the nested
check receives a private network namespace.

The shared model-view factory supplies staging, config mounts and environment handling
to both variants. The separated launcher calls a distinct fixed entry point; a missing
bubblewrap, privilege-drop failure, incomplete identity observation or failed setup never
falls back to the classic provider. The outer setup marker is not an identity assertion:
successful process evidence and the observed identity are also required. The nested
trusted wrapper emits a start marker only after bubblewrap reaches its payload; the
launcher strips that marker and preserves genuine product exit codes, including red.

## Workspace ownership without host mutation

The separated runtime always executes a disposable snapshot and removes it after the
context closes. It does not chown/chmod the caller's original workspace. Every source
directory component is opened through directory descriptors with `O_NOFOLLOW`. Child
inodes are inspected with `O_PATH` before any content I/O; only a verified regular file is
reopened through its stable kernel descriptor. Source symlinks (including ancestors),
multiply linked files, FIFOs/sockets/devices and setuid/setgid bits are refused.

Destination directories/files are exclusively new under an evaluator-owned private temp
parent. Only destination descriptors receive ownership changes. Copying checks inode
identity, size, timestamps, link count and directory membership for observed source
changes. This is a bounded evaluation-workspace snapshot, not an atomic filesystem
snapshot service or an adversarial container certification. Concurrent source changes
must be refused when detected; this does not prove a globally atomic multi-file revision.

No export/adoption of the private post-run workspace into a production model run is
implemented here. That integration needs its own evidence and review.

## Diagnostic command and limits

```bash
.validation/linux-venv/bin/python tools/b2_auth_bootstrap.py --prepare-only --separated-runtime --report .validation/b2-separation-preparation.json
```

On the measured privileged evaluator this produces `PREPARED_ONLY` with the non-root
identity floor. It still sets `may_start_authentication=false`,
`may_start_model_pilot=false`, `report_is_admission=false`; all pending auth jobs remain
`NOT RUN`. Without `--separated-runtime`, the original diagnostic keeps its original
context and remains blocked on this host. Normal-user evaluator setup remains unavailable.

Known credential/provider variables in either the host or supplied environment are
refused before tool checks or view construction. This does not audit credentials in
on-disk managed policy. The classic boundary serializes payload environment values into
the setup command's argv. The separated diagnostic's subsequent credential-free
descriptor preparation is documented in [ENVIRONMENT-TRANSPORT.md](ENVIRONMENT-TRANSPORT.md).
Neither path is admitted for real credentials. Secret intake, managed-policy admission, authenticated
context binding and a bounded supported service request remain separate blockers.

The new command runs only a fixed trusted Python identity probe. Separate tests exercise
credential-free CLI `--version`/`--help` startup with the scrub setting present. They do
not observe a real Claude Bash subprocess or built-in Read enforcement, validate a token,
or start a model. A synthetic provider canary in the manual nested-check test measures
that check provider's environment/PID isolation only.

## Evidence and regression mapping

Portable construction and refusal controls run in both runner modes. The full integration
also runs seven real Linux controls inside a credential-free child process, so an
operator's future A20 token cannot accidentally enter these tests.

| Invariant / earlier probe family | Current observation |
| --- | --- |
| P1 evaluator separation | Actual evaluator-sentinel read attempted and refused in outer view; sentinel path absent in inner view |
| P2 allowed writes | Workspace/scratch writable, root/runtime/config and empty `/tmp` read-only; original source hashes/ownership/modes unchanged |
| P3 genuine defect | Same seeded visible check returns red with the expected failure, then green after the legitimate product fix |
| P4 oracle separation | Inner view excludes evaluator/launcher modules; original oracle P4 remains covered by the full classic suite, not claimed newly certified for a separated model pilot |
| P5 grading integrity | Existing canonical dry-run/oracle/disposition controls remain in the full suite; this slice does not change grading or trust pins |
| P6 network observation | Host loopback listener is reachable in a positive control and unreachable from the inner network namespace; no outer network-isolation claim |
| Privilege floor | Actual outer and inner four-way IDs, capability sets and `NoNewPrivs`; regaining UID 0 refused |
| Snapshot safety | Link/special-file refusal, ancestor-symlink refusal and a deliberate file-replacement race never copy outside sentinel bytes |
| False-green boundary | Missing start marker, unavailable tool, timeout and incomplete/privileged identity block rather than becoming a product PASS |

A real in-memory break control removes `--no-new-privs` and makes the measured identity
test red for that reason. These are development/regression controls, not independent
held-out skill-effectiveness evidence. Separate-agent review uses the same model family.

No committed historical evidence is relabelled. Changed code bindings intentionally
invalidate historical results; current binding tests produce fresh temporary observations.
The original real-token test remains present and any skip still prevents full-suite PASS.

Rollback removes the explicit opt-in command/runtime path and its tests. The classic
model-view default, authentication gate, trust roots and case semantics remain unchanged.

Implementation references: [bubblewrap 0.9 construction](https://github.com/containers/bubblewrap/blob/v0.9.0/bubblewrap.c),
[bubblewrap security model](https://github.com/containers/bubblewrap/blob/main/README.md),
[setpriv](https://man7.org/linux/man-pages/man1/setpriv.1.html),
[No New Privileges](https://docs.kernel.org/userspace-api/no_new_privs.html).
