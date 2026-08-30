# Claim Verification Paired Pilot – Method Result

Canonical closing record for the Phase 4.2A method pilot. It states what was executed, what the method evidence supports, and what it explicitly does not.

**Phase 4.2A method pilot completed with partial method evidence.**

## Scope

The pilot asked whether a controlled with-vs-without-skill comparison for `claim-verification` can be *methodologically* established: a paired preparation, an isolated runner per response, canonical run packaging, treatment-blind judge packaging, and evidence for the method facts the paired contract requires.

It did not ask, and does not answer, whether the skill changes behavior.

## Executed evidence

| Component | Status |
| --- | --- |
| Experiment design (six cases, precommitted ground truth, counterbalanced order) | pass |
| Pair harness (`tools/behavioral_harness_pair.py`) | pass |
| Claude Code runner adapter (`tools/behavioral_harness_claude.py`) | pass |
| Subscription/managed auth in the normal host context | pass |
| Fresh context | pass |
| Filesystem/package isolation | pass |
| Real runtime observation | pass |
| Blind packaging | pass |
| Network/egress evidence | **incomplete** |

Runtime: Claude Code `2.1.251`, model `claude-haiku-4-5-20251001`.

The last generally passing runtime state before the paired smoke:

```yaml
fresh_context: true
repository_access_disabled: true
package_only_access: true
network_disabled: unknown
```

## The behavioral smoke that was actually run

```text
Case:        CV-01-supported
Repetition:  1
Responses:   exactly 2   (one baseline, one skill)
```

Opaque response IDs: `R-007a75f9cb800142`, `R-5dfb9b017098a32e`.

The treatment mapping is coordinator-only and is **not** recorded here. Both responses were produced successfully and packaged canonically; both run packages verified.

Planned but **not run**: the remaining 34 responses of the full experiment (six cases × three repetitions × two treatments).

## Method facts

```yaml
technical_run_packages_verified: true

same_user_prompt: true
same_subject_sources: true
same_subject_roles: true
same_prepared_runtime_contract: true
same_repo_commit_and_pinned_version: true
target_skill_version_pinned: true
same_runner_model: true
same_runner_type: true
fresh_context_sessions_distinct: true
method_evidence_matches_run_manifest: true
model_configuration_parity: true
runtime_configuration_parity: true

fresh_context_reported: true
network_disabled_reported: unknown
repository_access_disabled_reported: true
package_only_access_reported: true

treatment_disclosure_detected: false

method_evidence_status: partial
comparison_eligible: false
```

Seventeen of eighteen parity facts are satisfied. The single unproven fact is `network_disabled`.

Blind packaging produced no treatment disclosure, no mapping leak, no `control.yml`, no execution order and no blind seed in the judge package; the precommitted ground truth is present as the contract requires.

## Network/egress infrastructure sequence

Infrastructure evidence, deliberately kept separate from behavioral evidence.

| Step | Verdict | Established |
| --- | --- | --- |
| Feasibility survey | yes, with conditions | root, `CAP_NET_ADMIN`, nftables present; `bwrap`, `firejail`, `ip`, `slirp4netns`, `socat` absent |
| Provider through the host-managed proxy | pass | CONNECT and TLS succeed once the provider's `NO_PROXY` bypass is dropped; one tested non-provider host denied at CONNECT. This licenses only "fixed-destination guard plus enforcement is technically plausible" — never `network_disabled: true` |
| Fixed-destination guard, offline | pass | `tools/runner_egress_guard.py`: loopback-only, ephemeral port, CONNECT only, exact configured provider host and port 443, fail closed, controlled upstream tunnel, no generic forward proxying, no TLS termination, no payload persistence. Offline and regression tests pass |
| Real per-UID nft enforcement | pass | with a temporary UID-scoped policy actually loaded: only the guard socket reachable; direct provider, direct host proxy, DNS path, other loopback and other external TCP blocked; other UIDs unaffected; teardown complete |
| Real Claude child under that boundary | **fail** | process started, `system/init` reached, correct model observed, `tools == ["Read"]`, `mcp_servers == []`, `plugins == []`, then `authentication_failed` |
| cgroup-scoped enforcement | **fail** | hybrid cgroup v1/v2 environment; v2 hierarchy present and a temporary child cgroup creatable, but nftables cannot address it because the v2 hierarchy is not where nftables resolves paths; a workaround would require invasive host changes, which were deliberately not made |

The per-UID result proves the enforcement architecture can confine an unprivileged process to the local guard socket. It does **not** prove that the productive Claude runner can run under that boundary.

On the failed run: in the tested environment the managed-auth path did not succeed under the combination of a privilege drop to a foreign UID and an empty probe `HOME`. The exact causality between credential/`HOME` access and a possibly required additional auth network path was not resolved further. No claim is made that managed auth generally cannot work under a different UID.

No fresh-context or behavioral conclusions are drawn from that failed run.

## Final method verdict

```yaml
network_disabled: unknown
method_evidence_status: partial
comparison_eligible: false
skill_effect: unknown
```

This is a permitted terminal state of the method contract, not a defect in it. The infrastructure does not sufficiently evidence one required method fact, so the contract correctly reports `partial`.

## Why the pilot ends here

The remaining options would each introduce a new infrastructure contract: a dedicated runner credential, additional auth or guard destinations, a host cgroup remount, or new namespace/proxy infrastructure. Any of those stops being a test of the existing method contract and becomes a substantial rebuild of the host and credential architecture. That is not required for a first pilot.

The contract was therefore not adjusted to fit the environment.

## Explicit non-results

- Semantic judging: **not run**
- Unblinding: **not run**
- Behavioral comparison: **not performed**
- Skill effect: **unknown**
- Full planned experiment (36 responses): **not run**
- No maturity promotion, no Eval Coverage promotion, no benchmark claim
- The two stored responses were not compared, ranked or classified, and their treatment assignment is not disclosed

## Interpretation boundary

The pilot neither proved nor disproved the effectiveness of `claim-verification`. What it did establish empirically is a working paired-eval runner, real fresh-context and filesystem/package evidence, working blind packaging, and the limits of defensible network-egress evidence in the available host environment.

`partial` means the pair is technically executed and inspectable but not eligible for a with-vs-without comparison. Any later skill-effect statement requires a pair that reaches `method_evidence_status: pass`, followed by blind semantic judging and only then unblinding.
