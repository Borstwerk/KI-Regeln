# Method result — `code-review-v1`, Phase 4.2B cross-domain runner smoke

**Phase 4.2B cross-domain runner smoke completed with partial method evidence.**

This document records what the paired-eval machinery did in a second domain. It says
nothing about the quality of either response, nothing about which findings were or were
not reported, and nothing about the effect of the `code-review` skill. No such statement
is possible before a semantic judge and an unblinding, neither of which was run.

## Scope of this run

| | |
| --- | --- |
| Experiment | `code-review-v1` |
| Case | `CR-01-requirement-violation` |
| Repetition | 1 |
| Behavioral responses | exactly 2 |
| Model attempts | exactly 2, no retries |
| Opaque response IDs | `R-0193e38198d6b615`, `R-74ed80997d542d6a` |
| Treatment mapping | coordinator-only, **not recorded here** |
| Execution order | coordinator-defined, **not recorded here** |
| Remaining planned responses | 34, **not run** |

The blind seed, the treatment assignment and the execution order stay with the
coordinator. They are deliberately absent from this file, from the blind judge package
and from the round's report.

## Runtime

Phase 4.2B used Claude Code `2.1.258` with `tools/behavioral_harness_claude.py` adapter
version `0.2.1` and model `claude-haiku-4-5-20251001`.

The earlier Phase-4.2A claim-verification smoke used Claude Code `2.1.251`. **Therefore
this is not an exact runtime replication across domains.** No cross-phase
runtime-fingerprint equality is claimed, and no judgement is offered on whether `2.1.258`
behaves better, worse or identically to `2.1.251`.

The relevant B2 question is whether the unchanged paired-eval machinery operates
successfully in the second domain and reaches the same defensible method-evidence state.
"Same method-evidence state" means exactly the tri-state facts below — not identical
fingerprints across phases.

Within the pair, runtime parity is strict and was met: both responses ran under the same
Claude Code version, the same adapter version and code hash, the same model, the same
model-configuration fingerprint and the same runtime-configuration fingerprint, in two
distinct fresh sessions.

## Pinned inputs

| | |
| --- | --- |
| `experiment.yml` contract | `behavioral-paired-skill-eval/v1` |
| `ground_truth_model` | `code-review-findings/v1` |
| `pinned_commit` | `1483c0c4afdc46a25ffdc8ab92d8bd221e2e3a51` |
| Target skill | `Programmieren/Skills/code-review/SKILL.md`, blob `c375d97da41023d48d6172c82acc3ae94f5dedea` |
| Branch head at execution | `34d0608a27ad8c7bb4edf4ae3bfa35f3ceeaef0b` |

The experiment pin names the frozen evaluated package state, not the branch head. It was
not moved for this run.

## What was executed and verified

- pair prepared and `verify_paired_prepared` PASS before any model call: 2 responses,
  prompt parity, subject-source parity, subject-role parity, prepared-runtime parity,
  treatment mapping and execution order absent from the judge contract;
- 2 adapter runs, one attempt each, both successful;
- **2 / 2 canonical run packages verified** via the ordinary `package-run` / run
  verification path — the pair harness introduces no second run contract;
- fresh-context assessment: 25 of 25 checks satisfied on both responses, with an empty
  `violated` list and an empty `unproven` list;
- automatic treatment-disclosure check on both runner outputs: no disclosure;
- blind pair packaging successful, with both `method-evidence.yml` supplied.

The runner packages materialised the new `runner_path` structure — `sources/requirements.md`,
`sources/base/…`, `sources/head/…`, `sources/change.diff` — identically in both arms, with
the pinned skill present as `instructions/SKILL.md` in exactly one arm. This is the
concrete cross-domain result: the generalised materialisation works against a real runner.

## Method facts

```yaml
runner_type: claude-code
runner_model: claude-haiku-4-5-20251001

fresh_context: true
repository_access_disabled: true
package_only_access: true
network_disabled: unknown
```

Pair parity as recorded in the blind package:

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
```

## Closing state

```yaml
method_evidence_status: partial
comparison_eligible: false

semantic_judge: not_run
unblinding: not_run
behavioral_comparison: not_performed
skill_effect: unknown

full_planned_experiment: not_run
```

Seventeen of eighteen parity facts are satisfied. The single unproven fact is
`network_disabled`. The reason is the infrastructure limit already established and closed
in Phase 4.2A — egress enforcement and working managed authentication could not be
achieved together in this host without invasive changes — recorded in
`Evals/Behavioral-Harness/experiments/claim-verification-v1/METHOD-RESULT.md`. Phase 4.2B
inherits that limit unchanged and deliberately reopened no network-isolation
investigation.

`partial` is therefore a permitted terminal state of the method contract, not a defect in
it, and not a statement about either response. `comparison_eligible: false` means the pair
is technically executed and inspectable but **not** eligible for a with-vs-without
comparison. Any later skill-effect statement requires a pair that reaches
`method_evidence_status: pass`, followed by blind semantic judging and only then
unblinding.

## Not done

No semantic judge, no unblinding, no behavioral comparison, no skill-effect statement.
Neither runner output was read or compared. No finding, no quality difference and no
treatment attribution was derived from the responses. `code-review/SKILL.md` is unchanged,
the existing `Evals/Programmieren/code-review/cases.yml` evalpack is unchanged, and no
maturity or eval-coverage value was moved. No raw run artifact — prepared pair, runner
packages, adapter output, run packages, blind judge package or response text — is
committed; only this methodological summary is persisted.
