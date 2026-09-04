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
| P4 oracle leakage | True | the hostile product found nothing; no `checks/` in the oracle view |
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

## Held-out oracle

```
expectations (evaluator side, never in any view)
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
| execution boundary | evaluator artifacts from agent-controlled code | let a rewritten check read ground truth or write outside | P1, P2, P5, `BoundaryAdversarialTests` (12 tests) |
| workspace export + hashing | the graded artifact from the thing being graded | let a post-hoc edit change what is graded | `verify-run` mismatch tests, tamper attempt in the red team |
| oracle driver | product correctness measurement | leak expectations, or measure the wrong thing | P4, P5 |
| facts extraction / merge (`b2_grader`) | the mapping from measurement to disposition | produce incoherent facts, or invent a verdict | 15 grader controls, checked by rule and B1 reason |
| pilot readiness gate | the admission decision | let a pilot start on unproven infrastructure | four refusal tests plus the forgery attempt |
| writable adapter mode | the existing read-only path | silently widen 4.2A/4.2B's tool policy | `AdapterCompatibilityTests` |

The check wrapper is deliberately **not** on this list. In the first design draft it was
called a trusted component; it was in fact the bypass, which is why the boundary exists.

## Honest limits

- The boundary is evidence only for what P1-P5 demonstrate, on this host, with this provider.
- `network_disabled: True` is an observation, not a property of the design.
- Surface completeness is a statement about **this small synthetic workspace**, enforced by a
  test that classifies every file in it. It says nothing about real repositories.
- The workspace is writable on purpose. The trust chain around it is an integrity relation.
- No behavioral evidence exists. Readiness is an infrastructure decision.
