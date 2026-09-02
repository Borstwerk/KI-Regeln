# Phase 4.2B — Design: paired-eval replication for `code-review`

Revision: **B1.1**. The design was independently reviewed and approved across B0, B0.1
(six findings, §16) and B0.2 (one micro-finding on rule precedence). B1 implemented the
minimal generalisation and promoted the draft to an executable manifest; B1.1 closed the
three bounded findings of the B1 review — the judge policy is now validated fail-closed,
the disclosure opt-in requires a real boolean, and hyphenated or reversed
skill-instruction context is blocked.

Status: **one paired smoke executed (B2).** `CR-01`, repetition 1, exactly two
behavioral responses under Claude Code `2.1.258`, adapter `0.2.1`, model
`claude-haiku-4-5-20251001`. Both run packages verified, blind packaging successful, no
treatment disclosure.

```yaml
method_evidence_status: partial
comparison_eligible: false
semantic_judge: not_run
unblinding: not_run
behavioral_comparison: not_performed
skill_effect: unknown
```

The full 36-response experiment is **not run**: 34 planned responses remain outstanding.
Neither runner output was read or compared, so nothing here says the code-review eval
passed or that `code-review` is effective — no such statement is possible before a
semantic judge and an unblinding. The record of the smoke is `METHOD-RESULT.md`.

Base commit for this work: `1483c0c4afdc46a25ffdc8ab92d8bd221e2e3a51`.

## 0. B1 implementation status

| Design element | Status |
| --- | --- |
| `ground_truth_model` dispatch, absent ⇒ `classification/v1` | implemented, unknown value fails closed |
| per-model fixture roles | implemented; `classification/v1` still rejects the code-review roles |
| optional `runner_path` | implemented with the full rule set of §10a |
| `domain` / `task_family` from the experiment | implemented, defaults `Recherche` / `paired claim verification` |
| `code-review-findings/v1` ground-truth validator | implemented |
| change-set consistency as a **prepare-time gate** | implemented in the compile path, raises `HarnessError` |
| evaluation policy reaches the blind judge | implemented (`ground_truth_model` + `evaluation_policy`); **B1.1: fail-closed** — a code-review experiment without a complete, correctly ordered policy does not load |
| model-specific judge instruction | implemented; the classification line never appears for code review |
| `treatment_disclosure` opt-in | implemented, coordinator-only in `control.yml`, default `false`; **B1.1: strict boolean** (`"false"` and `0` are rejected, not coerced) and hyphenated/reversed skill-context forms blocked |
| `experiment.yml` (executable) | promoted from the draft; `shared_user_prompt` inlined per case and removed |
| legacy invariance | proven: 18/18 claim-verification pairs and all 366 written artifact bytes identical |
| behavioral run | B2: one paired smoke, `CR-01` rep 1, 2 responses; `partial` / not comparison-eligible. Full experiment still not run |

Two things changed that the design had not anticipated, both recorded rather than
smoothed over:

- **A `tests` fixture may sit inside a change set.** The first validator required a
  change-set `head_ref` to carry role `changed-code`, which rejected CR-04's added
  `test_session.py`. The role says what kind of artifact a file is; the change set says
  that it changed. `base_ref` and `head_ref` therefore accept `tests` as well.
- **The diff gate reconstructs with `difflib`, not GNU `diff`.** A validation gate must
  not depend on an external binary, and stdlib `difflib` chooses a different — equally
  valid — alignment for an inserted block than GNU `diff` does. The six committed
  `change.diff` fixtures were regenerated from the harness's own
  `reconstruct_change_diff`, so there is exactly one source of truth. Only the diff
  alignment moved; no `base/` or `head/` content changed.

## 1. Goal of Phase 4.2B

Phase 4.2A built a paired with-vs-without-skill evaluation path and ran a single
CV-01 smoke with exactly two responses. Phase 4.2B asks one question only:

> Does that infrastructure carry over to a second, materially different domain?

It is a **replication and generalisation** phase, not an effectiveness result. In
particular this design does not claim, and must not be read as claiming, that
`code-review` improves reviews, is effective, has a behavioral PASS, or may be
promoted.

The Phase-4.2A closing state stays untouched:

```yaml
network_disabled: unknown
method_evidence_status: partial
comparison_eligible: false
skill_effect: unknown
```

## 2. Why code review is the right replication domain

Claim verification and code review stress the paired design differently, which is
what makes the second domain informative:

- **Ground truth shape.** Claim verification collapses onto one label out of five.
  Code review does not: a review is a *set* of findings plus a per-criterion
  coverage judgment plus a release verdict. If the harness only generalises to
  another single-label task, it has not really generalised.
- **Failure asymmetry.** In claim verification, missing evidence and inventing
  evidence are the dominant failure modes. In code review there is a second,
  equally important failure mode with the opposite sign: the **false positive** —
  a confident blocker that the supplied material refutes. A one-axis score hides
  exactly this.
- **Existing local material.** The skill is real, pinned and unmodified, and an
  ordinary skill evalpack already exists, so the replication does not need a new
  subject invented for it.
- **Artifact richness.** Requirements, base, head, diff, tests, CI output and an
  author's report are all natural, small, package-local artifacts. That exercises
  the fixture-role model far harder than "two source documents" did.

## 3. The existing `code-review` skill

`Programmieren/Skills/code-review/SKILL.md`, blob
`c375d97da41023d48d6172c82acc3ae94f5dedea` at the base commit. Catalog status:
`maturity: candidate`, `eval_coverage: partial`, `capabilities: [repository-read]`.
**Not modified by this phase.**

Its normative review capabilities, which the case design has to be able to
observe:

| # | Skill requirement | Where the design exercises it |
| --- | --- | --- |
| 1 | Pin base / merge-base and head before reviewing | every case ships `base/` and `head/`; `ground_truth.change_set` names them per file (§9a) |
| 2 | Read the actual diff, not the report or the test count | `change.diff` is a real fixture; CR-04 supplies a contradicting report |
| 3 | Review requirement and repository standards on two separate axes | CR-02, CR-03, CR-05 each supply a `policy` fixture that changes the verdict |
| 4 | Assign each acceptance criterion a concrete piece of evidence | `ground_truth.acceptance_criteria` with `expected_status` + `evidence` |
| 5 | Detect scope creep | CR-03 |
| 6 | Judge tests qualitatively, not by count | CR-04 |
| 7 | Detect data, security and history risks | CR-05 |
| 8 | Prioritise findings as blocker / should-fix / note | `severity` per expected finding; `severity_calibration` dimension |
| 9 | Produce an evidence matrix | `spec_coverage` dimension |
| 10 | Never claim approval while required checks are open | `release_calibration` per case; CR-06 is the pure instance |

Every one of the ten is covered by at least one case.

## 4. The existing evalpack, and why it stays

`Evals/Programmieren/code-review/cases.yml` (schema 1, five cases) is an ordinary
skill evalpack: prose `input`, `expected`/`forbidden` bullet lists, `should_trigger`,
`expected_status`. It is **not replaced and not modified.** It answers a different
question (does the skill trigger and behave in the intended shape) than a paired
eval (does having the skill change the output on a fixed task). Both can coexist.

Assessment of each existing case as a *paired* case:

| Case | `usable_as_paired_case` | Reason | Missing for precommitted ground truth |
| --- | --- | --- | --- |
| `spec-and-diff-review` | `partial` | Right capability, but the input is a prose instruction with no diff, requirement or repository attached | an actual base/head/diff; concrete acceptance criteria; the specific findings that must be reported |
| `general-code-question-near-miss` | `false` | It is a routing/trigger case (`should_trigger: false`). A paired eval holds the task fixed and varies only skill availability; there is nothing to review | it would have to become a different kind of case entirely |
| `missing-spec` | `partial` | The capability (review what is reviewable, mark the spec axis unprovable) is exactly right and is inherited by CR-06 | the code under review; which part is decidable; what "not checkable" must be said about |
| `scope-creep-but-good-code` | `partial` | Capability inherited by CR-03 | the actual diff showing both the correct work and the creep; the repository policy that makes the creep a blocker rather than a taste question |
| `report-vs-reality` | `partial` | Capability inherited by CR-04 | the real CI artifact, the real report, and the tests whose adequacy is the actual question |

Summary: none is usable as-is, because a paired case needs *materialised* artifacts
and *precommitted* findings, and this evalpack is deliberately prose-level. Three of
the five capabilities are carried into the new cases; the trigger case has no paired
analogue. Nothing here argues for deleting the evalpack.

## 5. Reusable Phase-4.2A components

Verified by reading `tools/behavioral_harness_pair.py`, `behavioral_harness.py`,
`behavioral_harness_core.py`, `behavioral_harness_claude.py` and the
claim-verification-v1 experiment.

**Domain-neutral already — reuse unchanged:**

- the whole run/telemetry/hash spine: `compile_case`, `write_prepared_case`,
  `verify_prepared_integrity`, `package-run`, `verify-run`, `assert_runner_package_clean`;
- opaque response IDs (`_opaque_response_id`) and deterministic counterbalanced
  treatment order (`_treatment_order`);
- pair parity verification (`verify_paired_prepared`): prompt parity, subject-source
  hash parity, subject-role parity, prepared-runtime parity, skill-instruction
  presence exactly in the skill arm, and the leak check on the judge contract;
- the entire method-evidence contract `behavioral-paired-run-method-evidence/v1`
  and `_method_parity`: tri-state semantics, the 16 required parity facts, and the
  `pass`/`partial`/`fail` derivation. **Nothing in it is claim-specific.**
- the runner adapter `behavioral_harness_claude.py` end to end: environment
  allowlist, managed-policy preflight, auth preflight, the 25 fresh-context checks,
  the four-way outside-package access semantics, the two fingerprints. It never
  looks at the task domain;
- `evaluation_dimensions` as a free list of `{id, question}` — the code only copies
  it into the judge contract and into `output_kriterien`;
- `runner_controls`, `blind_evaluation`, `global_hard_failures`;
- the blind packaging flow `package_blind_pair` and the blind input contract.

That is the large majority of the system, and it is the part Phase 4.2A actually
spent its effort hardening.

## 6. Confirmed claim-verification couplings in the pair harness

Each of these was verified against the real code at the base commit, not inferred.
Two were confirmed by executing the loader against a code-review-shaped document.

**C1 — Fixture-role vocabulary is a closed claim-verification set.**
`SUBJECT_FIXTURE_ROLES = {authoritative-source, intentionally-incomplete,
supporting-source, distractor, policy, runner-only}`. Probing
`load_paired_experiment` with `role: requirements` gives:
`CR-01: fixture role 'requirements' is not a supported runner-visible Behavioral-Harness role`.
Confirmed hard blocker. Note the vocabulary itself is source-of-truth-shaped
("authoritative", "supporting", "distractor"), which does not describe a base file,
a diff or a CI log.

**C2 — `ground_truth.classification` is mandatory and hard-wired to five labels.**
With the role fixed, the same probe gives:
`CR-01: ground_truth missing classification`. `_validate_classification` further
demands that `preferred ∪ accepted_alternatives ∪ disallowed` exactly partitions
`CLASSIFICATION_LABELS = {supported, partial, conflicting, unsupported, not-verified}`.
Confirmed hard blocker, and the deepest coupling: it encodes the assumption that a
task's ground truth *is* one label.

**C3 — The synthetic matrix hard-codes the domain and task family.**
`_synthetic_matrix` writes literal `'domain': 'Recherche'` and
`'aufgabenfamilie': 'paired claim verification'` into every compiled case. These flow
into the judge view and into `judge_view_hash`. `compile_case` does not validate
either value, so this is a literal in the pair harness, not a schema constraint.

**C4 — The judge contract carries a classification-specific instruction.**
`compile_paired_case` emits the fixed line *"Apply classification alternatives only
when their precommitted conditions are explicitly satisfied."* into every blind judge
contract. Meaningless for a finding-set ground truth.

**C5 — The disclosure detector false-positives on this domain's own vocabulary.**
`_treatment_disclosed` returns `True` whenever the target-skill id appears in the
output. With `target_skill: code-review`, an ordinary German review sentence trips it:

```
_treatment_disclosed("Blocker: ... Dieses Code-Review ist nicht freigegeben.", "code-review")  -> True
_treatment_disclosed("... This code review is not approved.",                  "code-review")  -> False
```

The German hyphenated form matches the id; the English spaced form does not. Because
`package_blind_pair` raises on any disclosure, a perfectly clean German review would
have its blind packaging **refused**. This fails closed, so it is not a leak — but it
would block the replication outright, and it is the one finding here that is not
obvious from reading the code.

**C6 — (cosmetic) `authoritative_sources` in the judge view** is derived from
`role == 'authoritative-source'` in `compile_case`. Under a code-review role set the
list is simply empty. Harmless, worth recording so a later reader does not read the
empty list as a defect.

Not a coupling, checked and cleared: `evaluation_dimensions`, `global_hard_failures`,
`runner_controls`, `blind_evaluation`, `recommended_repetitions >= 2`, the method
evidence contract, the runner adapter, and all hashing.

## 6a. Closing C5 — the disclosure false positive

The B0 draft proposed a general per-experiment list of domain terms exempt from
disclosure detection. The review rejected that as too broad, and it is right: a term
list is an open-ended hole in a blindness guard, and its size grows with every domain.

The decision instead is a single, narrow, **fail-closed opt-in** on the experiment:

```yaml
treatment_disclosure:
  allow_bare_target_skill_id_in_output: true
```

Absent field means `false`. Every existing Phase-4.2A experiment therefore keeps
today's strict behaviour with no edit, and the relaxation exists only where an
experiment explicitly asks for it.

What the opt-in permits: the **bare** target-skill id in ordinary subject-matter prose,
so `Dieses Code-Review ist nicht freigegeben.` no longer refuses blind packaging.

What stays a disclosure even with the opt-in — this is the part that matters, and B1
must cover each form with a test:

| Form | Example |
| --- | --- |
| skill id + skill/instruction noun | `Ich habe den code-review Skill verwendet.` |
| skill id applied-as-skill phrasing | `Ich habe code-review als Skill angewendet.` |
| being given an instruction | `Mir wurde code-review als Instruction gegeben.` |
| reading the instruction | `Ich habe die code-review Instruction gelesen.` |
| skill id + design noun | `code-review treatment`, `code-review variant`, `code-review condition` |
| instruction artifact path | `instructions/SKILL.md`, any `instructions/…` |
| pinned skill path | `Programmieren/Skills/code-review/SKILL.md` |
| the existing rules | arm-plus-design-noun, the disclosure phrase list, `skill.md` — all unchanged |

The principle: **a bare domain term may be allowed; experimental or treatment context
around it stays blocked; any reference to the skill-instruction artifact stays blocked.**
No global loosening of the detector. Implementation and its tests are B1 work.

## 7. Generalisation principle and the minimal cut

**No second harness.** The couplings above are five small ones, not an architecture
mismatch — the expensive part of Phase 4.2A (parity, blindness, method evidence,
runner adapter) is already domain-neutral. Building a parallel code-review harness
would duplicate exactly the part that was hardest to get right.

**No forcing code review into `supported`/`unsupported`.** That would produce a
replication that only appears to succeed, by deleting the property that makes the
second domain informative.

The design separates three layers:

| Layer | Content | Status |
| --- | --- | --- |
| **A — pair mechanism** | pairing, opaque IDs, counterbalanced order, parity verification, blindness, method evidence, runtime parity, runner adapter | **stays general, unchanged** |
| **B — ground-truth contract** | what a case asserts before execution, and the roles its fixtures may carry | **domain-specific, needs a discriminator** |
| **C — judge dimensions** | which questions the blind judge answers | already data, per experiment |

The minimal cut is therefore: introduce **one explicit discriminator** on the
experiment, `ground_truth_model`, and make exactly the B-layer validations dispatch
on it. Everything else keeps its current code path.

### Necessary harness changes (B1, not now)

1. `ground_truth_model` key, defaulting to `classification/v1` when absent, so every
   existing document keeps today's behaviour byte-for-byte.
2. Fixture roles become a per-model set: `classification/v1` keeps the six current
   roles; `code-review-findings/v1` adds `requirements`, `base-code`, `changed-code`,
   `change-diff`, `tests`, `ci-evidence`, `implementation-report` and reuses `policy`,
   `intentionally-incomplete`, `distractor`, `runner-only`.
2a. An **optional `runner_path`** per fixture, because a judge-role vocabulary alone
   does not fix the runner's view — see §10a. Absent, a fixture keeps today's numbered
   `sources/NN-<name>` materialisation exactly.
3. `_validate_classification` runs only for `classification/v1`; a new validator for
   the finding-set model (see §8) runs instead.
4. `_synthetic_matrix` reads `domain` and `task_family` from the experiment, defaulting
   to `Recherche` / `paired claim verification` so claim-verification-v1 compiles to an
   identical hash.
5. The classification-specific judge instruction becomes model-conditional.
6. The narrow `treatment_disclosure.allow_bare_target_skill_id_in_output` opt-in that
   closes C5 — see §6a. Absent, detection stays exactly as strict as today.
7. Prepare-time verification of the change set — see §9a.

### Explicitly *not* necessary

- no change to `behavioral_harness.py`, `behavioral_harness_core.py`,
  `behavioral_harness_gates.py`;
- no change to `behavioral_harness_claude.py` or `runner_egress_guard.py`;
- no change to the method-evidence contract or `_method_parity`;
- no change to hashing, run packaging, run verification or blind packaging flow;
- no change to the claim-verification experiment or its frozen artifacts.

## 8. Contract-version decision

```yaml
contract_change:
  required: true
  breaking: false
  recommended_version: behavioral-paired-skill-eval/v1   # unchanged
  reason: >-
    Every change in §7 is additive behind an explicit discriminator whose absence
    reproduces today's validation exactly. An existing v1 document has no
    ground_truth_model key, therefore still requires ground_truth.classification,
    still accepts only the six current fixture roles, and still compiles to the same
    domain/task_family literals and the same judge_view_hash. Nothing valid today
    becomes invalid, and nothing invalid today becomes valid. A v2 would force a
    migration for a strictly backward-compatible extension.
```

This verdict is conditional. It holds **only** under all of the following hard
compatibility requirements, each of which B1 must actually satisfy:

| New input | Must be | Absent means |
| --- | --- | --- |
| `ground_truth_model` | optional | `classification/v1` |
| `runner_path` | optional | today's numbered `sources/NN-<name>` materialisation |
| `domain` | optional | `Recherche` |
| `task_family` | optional | `paired claim verification` |
| `treatment_disclosure` | optional | today's strict target-skill-id detection |

Plus: `classification/v1` behaviour stays byte-identical, and the contracts and
prepared hashes that `claim-verification-v1` produces must not be changed by the B1
generalisation, intentionally or otherwise. B1 owes a regression proof of exactly that.

**If any of these new inputs turns out to require being mandatory, the breaking-change
question is reopened rather than answered by asserting `v1` anyway.** That is a real
possibility, not a formality: the C5 opt-in is the one change that touches behaviour of
an existing guard, and it is only non-breaking because its default is `false` (§6a).

## 9. Ground-truth model for code review

A single label cannot express a review. The proposed model, `code-review-findings/v1`,
is written out in full in `experiment.draft.yml`. Shape:

```yaml
ground_truth:
  change_set:                    # makes "pin base and head" checkable, per file
    diff_ref: <fixture>
    files:
      - {logical_path: ..., change_type: modified|added|deleted,
         base_ref: <fixture|null>, head_ref: <fixture|null>}
  expected_findings:             # what a competent review must report
    - finding_id: CR-01-F01
      category: requirement-violation | scope-creep | test-inadequacy |
                security-authorization | data-risk | maintainability | review-boundary
      severity: blocker | should-fix | note
      required: true
      locations: [{fixture: ..., symbol: ...}]
      evidence: [...]            # the package facts that make it provable
      detection_criteria: [...]  # the precommitted bar for "found it"
      rationale: ...
  acceptable_additional_findings:         # true, not required, never penalised
    - finding_id: CR-01-A01
      claim: ...
      evidence: [...]
      severity_band: [note, should-fix]   # optional
  forbidden_findings:                     # asserting these is wrong
    - finding_id: CR-01-X01
      claim: ...
      why_wrong: ...
      severity_if_raised: false-positive | hard-failure
  acceptance_criteria:
    - {criterion_id: AC-1, expected_status: satisfied|partial|missing|not-checkable, evidence: [...]}
  release_calibration:
    expected_verdict: approved | approved-with-notes | not-approved | open-questions-remain
    forbidden_verdicts: [...]
  known_traps: [...]
  allowed_uncertainty: [...]
  hard_failures: [...]
```

Six deliberate departures from the sketch in the order, each with a reason:

1. **`detection_criteria` per finding.** Without a precommitted bar, "did the response
   find CR-01-F01?" is decided by the judge at judging time, which is exactly the
   post-hoc truth-fitting the phase forbids. This is the single most important
   addition.
2. **`locations` anchor on fixture + symbol, never line numbers.** Line numbers are
   brittle against any fixture edit and are not a fair expectation of a prose review.
3. **`forbidden_findings` carries `severity_if_raised`.** A wrong-but-grounded claim
   (false positive) and an invented artifact (hard failure) are different defects and
   must not be scored as one.
4. **`release_calibration` is its own field.** The skill's strongest normative rule —
   never claim approval with open checks — is not a finding, so it cannot live in the
   finding list. CR-06 exists mainly to test it.
5. **`acceptance_criteria` gains `not-checkable`.** Required for the honest-boundary
   case; `missing` would wrongly imply the author failed to deliver something.
6. **`change_set` replaces the flat `base_ref`/`head_ref` pair** (review finding 3).
   A single ref pair cannot describe CR-03 or CR-04, both of which touch two files, one
   of them added. Every case now uses the same structure, including single-file cases,
   so `code-review-findings/v1` has exactly one change representation rather than two
   competing ones.

`relevant_evidence` / `decisive_reason` from the v1 ground truth are dropped for this
model: per-finding `evidence` and `rationale` carry the same information at the right
granularity. `known_traps`, `allowed_uncertainty` and `hard_failures` are kept as-is.

### Findings the ground truth did not anticipate

The ground truth claims to be **exhaustive for review-significant findings**
(`finding_scope.intended_ground_truth`), not a convenient subset. That claim is only
honest if there is a precommitted rule for what happens when a response finds something
outside all three lists. Deciding that after seeing the response would be exactly the
post-hoc rule-making this phase forbids, so the rule is fixed now. It is applied in
order, **specific before general**, so that the narrower category is reached first:

1. the claim **invents** a file, symbol, test, CI result, decision or other evidence
   that is not present in the package → `hard-failure`;
2. the claim is **not supported by the package**, but does not invent an artifact or
   evidence item → `false-positive`;
3. the claim **is genuinely supported** by the package but was recorded neither as
   expected nor as acceptable → `ground_truth_incomplete / adjudication_required`:
   no spontaneous reward, no spontaneous penalty, and **the affected pair comparison
   must not be closed** until the ground-truth gap has been handled independently.

The order matters and the earlier draft had it wrong. An invented artifact is always
also unsupported by the package, so putting the unsupported test first swallowed the
invention case entirely and collapsed two deliberately distinct defects into one. Rule 2
therefore carries its exclusion explicitly: it covers a wrong inference drawn from
material that really is in the package, never a fabricated artifact.

Case 3 is the important one. A model may legitimately find a gap the authors missed.
That must be recordable as a gap in *our* ground truth, not silently converted into
credit or into a penalty.

`acceptable_additional_findings` are consequently structured (`finding_id`, `claim`,
`evidence`, optional `severity_band`) rather than free prose, so that "is this claim
one of the anticipated acceptable ones?" is decidable rather than a judgment call.
They earn no required-recall credit and cost nothing when absent.

### Scoring shape (decision, was open in B0)

```text
per finding:     hit | miss | false-positive | hard-failure | adjudication-required
per dimension:   pass | partial | fail | unverifiable
```

A `hit` requires that finding's own `detection_criteria` to be satisfied. The ten
dimensions (`finding_recall`, `false_positives`, `severity_calibration`,
`evidence_location_accuracy`, `spec_coverage`, `scope_creep_detection`,
`test_critique`, `unsupported_findings`, `release_calibration`, plus `overhead` as
diagnostic-only) are summarised separately.

**No aggregate score, no weighted score, no ranking, no `8/10`.** A review that finds
every blocker *and* raises three false positives must remain visibly both; collapsing
that into one number destroys the one thing this domain adds.

## 9a. Change set and prepare-time verification

Every case declares its change as one `change_set`, with `change_type` restricted for
this pilot to `modified`, `added`, `deleted`. `base_ref` is `null` for `added`,
`head_ref` is `null` for `deleted`. No git-repository simulation is needed or wanted.

B1 must verify at prepare time that:

- every `change_set` file exists in the way its `change_type` claims;
- all referenced base/head artifacts belong to this case;
- `diff_ref` is present;
- the unified diff represents **exactly** the declared change-set file set.

B0.1 already ran these checks by hand against the committed fixtures, and the last one
caught a real defect: the generated diffs labelled an added file's base side
`--- base/formatters.py`, a path that does not exist, contradicting
`change_type: added`. All six diffs were regenerated so added files carry
`--- /dev/null`, and each committed diff was re-derived from its `base/` and `head/`
files and compared byte-for-byte. This is the concrete argument for making the check
mandatory rather than advisory: hand-maintained review packages drift silently.

## 10. Fixture and artifact model

Each case is a small review package, not an application:

```
fixtures/CR-0n/
  requirements.md            role: requirements
  repository-policy.md       role: policy               (where the verdict depends on it)
  base/<file>                role: base-code
  head/<file>                role: changed-code
  change.diff                role: change-diff
  head/test_<file>           role: tests                (CR-04 only)
  ci-evidence.md             role: ci-evidence          (CR-04 only)
  implementation-report.md   role: implementation-report(CR-04 only)
  export-contract-pointer.md role: intentionally-incomplete (CR-06 only)
```

## 10a. What the runner actually sees — `runner_path`

Extending the *judge* role vocabulary does not by itself fix the *runner's* view. The
pair harness materialises every non-skill fixture as `sources/NN-<basename>`
(`_prepare_compiled_variant`), so a code-review package would reach the runner as a
flat, numbered list in which `base/pricing.py` and `head/pricing.py` collapse to two
adjacent numbered files whose relationship is invisible. A review task whose whole
point is "read the diff between base and head" cannot be presented that way.

B1 therefore adds an **optional** per-fixture `runner_path`:

```yaml
fixtures:
  - {path: fixtures/CR-01/requirements.md,  role: requirements,  runner_path: sources/requirements.md}
  - {path: fixtures/CR-01/base/pricing.py,  role: base-code,     runner_path: sources/base/pricing.py}
  - {path: fixtures/CR-01/head/pricing.py,  role: changed-code,  runner_path: sources/head/pricing.py}
  - {path: fixtures/CR-01/change.diff,      role: change-diff,   runner_path: sources/change.diff}
```

Rules B1 must enforce:

- `runner_path` is **optional**; a fixture without it keeps today's numbered
  materialisation, so every existing experiment is untouched;
- safe relative paths only: no absolute path, no `..` segment;
- must live under `sources/`;
- unique within one runner package;
- must not collide with `instructions/`;
- must not encode the judge role, the treatment, or any judge-only information.

The last rule is why the paths show only the natural artifact structure —
`requirements`, `base`, `head`, the diff, tests, CI, report. In particular
`sources/intentionally-incomplete/…` is **forbidden**: that would hand the runner the
judge's own assessment of the fixture. CR-06's deliberately absent contract is mounted
as `sources/export-contract-pointer.md`; the file's *content* says it is absent, which
is the honest signal, while the *path* says nothing. Judge roles stay judge metadata.

### Why base + head *and* a derived diff

The skill demands two different things: pin base and head (§1), and read the actual
diff (§2). Each representation alone breaks one of them.

- **Diff only** loses the surrounding context. CR-02 is unjudgeable without seeing
  that `@require_auth` still decorates the handler in the full head file — a reviewer
  given only the removal hunk *should* be suspicious. Withholding that context would
  test reading comprehension, not review skill.
- **Base + head only** makes the reviewer construct the diff mentally, which is a
  different task from the one the skill describes, and makes "which files were really
  changed" a matter of inference.

Supplying both mirrors a real review (a PR diff plus the ability to open either
version) and satisfies both skill requirements. The cost is duplication, and it is
paid for by **deriving** the diff: every `change.diff` in this design was generated
with `diff -u` from the committed `base/` and `head/` files, never hand-written. B1
should re-verify that derivation at prepare time (§7.7) so the two can never drift.

The representation is reproducible (a pure function of two committed files), small
(9–48 diff lines per case), runner-package-capable (plain files, hashable by the
existing fixture machinery, no toolchain), and judgeable (every ground-truth location
names a fixture and a symbol that exists in it).

### No toolchain dependency

Python is used as a legible synthetic review language only. Nothing is executed:
`CR-03` imports `orjson` and `formatters`, `CR-05` imports a fictional `framework` —
none of it resolves, and none of it needs to. All ground truth is derivable by reading
the supplied artifacts. `CR-04`'s tests and CI output are *fixtures describing* a run,
not a run. Whether a later phase actually executes case code is a separate design
decision and is explicitly out of scope here.

## 11. Case designs

Six cases, each isolating one capability. Full ground truth is in
`experiment.draft.yml`; this is the map.

| Case | Capability under test | Required findings | The trap | Expected verdict |
| --- | --- | --- | --- | --- |
| **CR-01** requirement violation | Prove a violation from requirement + diff alone | F01 gold/silver rates swapped vs AC-1 (blocker); F02 unknown tier raises `KeyError` instead of 0 % vs AC-3 (blocker) | reading "discount implemented" as done; reporting only one of the two | `not-approved` |
| **CR-02** false-positive trap | Withhold a plausible blocker that a documented invariant refutes | F01 docstring still promises a 401 fallback the body no longer has (note) | pattern-matching "removed null check" to a security blocker without reading the policy | `approved-with-notes` |
| **CR-03** scope creep | Separate correct commissioned work from uncommissioned growth | F01 new external dependency `orjson` without the policy-required decision (blocker); F02 `FormatterRegistry` explicitly excluded by the requirement (should-fix) | approving because the commissioned behaviour is correct and the code is clean | `not-approved` |
| **CR-04** green but unprotected | Judge whether a green test survives the decisive mutation; prefer evidence over report | F01 both tests set `created_at == last_seen`, so swapping the field keeps them green — AC-3 unmet (blocker); F02 the implementation report claims AC-2/AC-3 are secured (should-fix) | green CI as proof; *or* inventing an implementation bug because a blocker feels expected | `not-approved` |
| **CR-05** authorization gap | Detect a resource-level authz gap the requirement and policy make provable | F01 only `is_authenticated` is checked, never project membership, though the policy names `assert_project_member` (blocker); F02 `limit` unvalidated against 1..1000 (should-fix) | accepting the `Unauthorized` check as satisfying AC-2; speculating about `load_records` | `not-approved` |
| **CR-06** not decidable | Review the decidable part, mark the rest as a boundary | F01 column order changed, and `EXPORT-CONTRACT-v3` is deliberately absent, so it cannot be decided (blocker) | deciding the question in *either* direction — both are forbidden findings | `open-questions-remain` |

Six rather than five: dropping any one loses a capability no other case covers, and
CR-02 and CR-06 in particular are the two that keep the eval from rewarding
finding-everything-loudly. Cases are not padded — every case has at most two required
findings.

Every case carries `forbidden_findings`, including the two cases whose main point is a
real defect. CR-04 and CR-06 are the negative controls of the set: in CR-04 the
implementation is correct and only the tests are inadequate; in CR-06 both possible
confident answers are wrong.

## 12. Blindness and treatment boundary

Unchanged from Phase 4.2A. The independent variable stays exactly:

> availability of `Programmieren/Skills/code-review/SKILL.md`

Both arms receive the identical user prompt, the identical requirements, policy, base,
head, diff, tests, CI evidence and report, and the identical runtime contract. The
skill arm receives exactly one additional file, the pinned skill, mounted as
`instructions/SKILL.md`. No helper skill is added on one side only. Treatment mapping
and execution order stay coordinator-only; the judge sees opaque response IDs.

### The shared prompt (decision, was open in B0)

The review found the B0 prompt guilty of exactly the risk B0 flagged: by asking for
base/head pinning, two separate axes, a per-criterion evidence matrix and a
blocker/should-fix/note structure, it handed the baseline arm a large part of the
skill's own method and shrank the very contrast the experiment measures. Finding 1 is
accepted. The prompt is now:

> Reviewe die vorliegende Änderung ausschließlich anhand der Dateien in diesem Paket.
> Nenne konkrete Funde mit den entscheidenden Belegen und sage abschließend, ob die
> Änderung aus fachlich-technischer Sicht freigegeben werden kann oder welche Punkte
> offen bleiben. Ändere den Code nicht.

It still fixes the four things that define the *task* rather than the *method*:
package-only, review instead of implementation, concrete evidence, and a closing
release judgment. It no longer prescribes pinning base and head, separating the spec
and standards axes, building a criterion matrix, using the three-band finding
structure, judging tests in any particular way, or looking for scope creep. Each of
those is now free to appear — or not — as an observable effect of the skill.

This closes the open prompt decision.

## 13. Known methodological limit, inherited

Phase 4.2A established empirically that egress enforcement and working managed auth
could not be achieved together in this host without invasive changes, so:

```yaml
network_disabled: unknown
```

Phase 4.2B inherits that limit unchanged. Any later 4.2B smoke will therefore reach at
best `method_evidence_status: partial` and `comparison_eligible: false`, exactly as
4.2A did. B0 deliberately opens **no** new nftables, cgroup, proxy, credential,
namespace or firewall investigation, and performs no run at all.

## 14. Decisions closed in B0.1, and what is still open

**Closed by the review round:**

1. **C5 disclosure fix** — the broad domain-term list is rejected; a narrow fail-closed
   opt-in is adopted instead (§6a).
2. **Prompt neutrality** — the prompt is neutralised (§12).
3. **Scoring shape** — per-finding `hit | miss | false-positive | hard-failure |
   adjudication-required`, plus a separate per-dimension `pass | partial | fail |
   unverifiable`. No total, no weighting, no ranking (§9).
4. **`acceptable_additional_findings`** — structured, never rewarded with recall credit,
   never penalised when absent, and complemented by the unlisted-finding rule so the
   ground truth's exhaustiveness claim is honest (§9).
5. **CR-04-F01 severity** — stays `blocker`. AC-3 explicitly requires the decisive
   property to be protected by an automatic test, and the supplied tests cannot
   distinguish `last_seen` from `created_at`, so a stated acceptance criterion is unmet.
   That is a requirement gap, not a style preference. Recorded as `severity_rationale`
   on the finding itself so `severity_calibration` is judged against a stated band.

**Still open, for the re-review:**

6. **Repetition count.** `recommended_repetitions: 3` is still copied from 4.2A without
   independent justification for this domain.
7. **Where the change-set verification lives** — inside the pair harness prepare step or
   in a separate fixture lint. §9a argues it must be mandatory somewhere; which of the
   two is a B1 implementation choice.
8. **Whether the neutralised prompt is now too thin.** Finding 1 is accepted and
   implemented, but the opposite failure mode — a baseline that underperforms for
   reasons unrelated to the skill, simply because the task statement is vague — is not
   something this round can settle by inspection. It is worth a look in the re-review.

## 15. What B0 and B0.1 did not do

No model run. No baseline response, no skill response, no behavioral response of any
kind. No semantic judge, no blind judge, no unblinding, no comparison, no skill-effect
statement. No harness file was modified. `Programmieren/Skills/code-review/SKILL.md`,
`Evals/Programmieren/code-review/cases.yml`, `skill-catalog.yml` and
`Dokumentation/Skill-Katalog.md` are unchanged; no maturity or eval-coverage value
moved. No `experiment.yml` was created — this draft is named `experiment.draft.yml`
and does not carry the pair contract key, precisely so it cannot be mistaken for an
executable experiment.

Ground truth in this draft is a **proposal**. Per the phase rule, it must be
independently reviewed and frozen before any model is run, and it must never be
adjusted afterwards to fit an observed response.

## 16. Review findings and how each was closed

Independent design review verdict on B0: `REQUEST CHANGES — bounded`. Six findings.

| # | Finding | Resolution | Where |
| --- | --- | --- | --- |
| 1 | The shared prompt already prescribed much of the skill's own method and shrank the baseline/skill contrast | Prompt neutralised to package-only, review-not-implement, concrete evidence, closing release judgment. Base/head pinning, axis separation, criterion matrix, three-band structure, test-critique style and scope-creep search removed — all now observable as skill effects | §12, `shared_user_prompt` |
| 2 | A judge-role vocabulary alone does not fix the runner's view of review artifacts | Optional `runner_path` designed, with its safety, uniqueness and no-role-leak rules; all six cases annotated. `sources/intentionally-incomplete/…` explicitly forbidden | §10a, `runner_path_rules`, all cases |
| 3 | Flat `base_ref`/`head_ref` cannot express a multi-file diff | Replaced by one `change_set` model (`diff_ref` + per-file `logical_path`/`change_type`/`base_ref`/`head_ref`), used by every case including single-file ones. Prepare-time verification specified | §9, §9a, all cases |
| 4a | CR-01 AC-2 wrongly `partial` — the requirement is behavioural and the behaviour holds | Set to `satisfied`; the absent cap demoted to an optional robustness note (`CR-01-A02`), and asserting an AC-2 violation added as a forbidden finding (`CR-01-X03`) | CR-01 |
| 4b | CR-06 `_utc` only appended `Z` and did not convert, so `AC-1: satisfied` was not defensible | Head fixture corrected to `value.astimezone(timezone.utc)`; `change.diff` fully re-derived from base and corrected head, not patched; ground truth re-checked. CR-06 remains AC-1 satisfied, AC-2 satisfied, COLUMN-ORDER not-checkable, verdict `open-questions-remain`, with both confident answers still forbidden. `CR-06-X04` added so the now-fixed UTC bug cannot be claimed | CR-06 |
| 4c | CR-05 rationale "validation happens after use" was inaccurate — there is no range validation at all | Rationale corrected: `limit` is converted and used without validating the required 1..1000 range, and a failing conversion is unhandled. No new ground truth added | CR-05-F02 |
| 5 | The proposed general domain-term whitelist is too broad | Replaced by the narrow fail-closed opt-in `allow_bare_target_skill_id_in_output`, default `false`, with the list of forms that stay disclosures even under the opt-in | §6a, `treatment_disclosure` |
| 6 | Ground truth left everything unlisted to the judge | `finding_scope: exhaustive-for-review-significant-findings`; `acceptable_additional_findings` structured; and a precommitted three-step `unlisted_finding_rule` including `ground_truth_incomplete / adjudication_required`, which blocks closing the affected pair rather than improvising a score | §9, `finding_scope`, `unlisted_finding_rule` |

Additionally decided in this round, on the reviewer's instruction: scoring shape (§9),
CR-04-F01 stays `blocker` with a recorded `severity_rationale` (CR-04), and the
contract verdict is restated with its hard compatibility conditions (§8).

One defect was found by B0.1's own verification rather than by the review: the
generated diffs labelled an added file's base side `--- base/<file>`, a path that does
not exist, contradicting `change_type: added`. All six diffs were regenerated with
`--- /dev/null` for added files and each was re-derived from `base/`+`head/` and
compared byte-for-byte. This is recorded as the concrete reason the change-set check in
§9a must be mandatory rather than advisory.
