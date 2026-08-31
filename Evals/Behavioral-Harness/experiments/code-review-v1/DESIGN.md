# Phase 4.2B / B0 — Design: paired-eval replication for `code-review`

Status: **design only**. No model was run, no response was produced, no judge was
invoked, nothing was unblinded. Nothing in this document upgrades any Phase-4.2A
result.

Base commit for this design round: `1483c0c4afdc46a25ffdc8ab92d8bd221e2e3a51`.

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
| 1 | Pin base / merge-base and head before reviewing | every case ships `base/` and `head/`; `ground_truth.base_ref`/`head_ref` name them |
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
3. `_validate_classification` runs only for `classification/v1`; a new validator for
   the finding-set model (see §8) runs instead.
4. `_synthetic_matrix` reads `domain` and `task_family` from the experiment, defaulting
   to `Recherche` / `paired claim verification` so claim-verification-v1 compiles to an
   identical hash.
5. The classification-specific judge instruction becomes model-conditional.
6. C5 must be resolved before any code-review run — see the open decisions.
7. A prepare-time check that `change.diff` really is the diff of `base_ref` and
   `head_ref`, so the review package cannot become internally inconsistent.

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

Two caveats stated rather than smoothed over:

- This holds **only** if the discriminator defaults to `classification/v1`. If B1
  instead makes `ground_truth_model` mandatory, the change *is* breaking and a v2 is
  required. That is an implementation constraint, not a free choice.
- The C5 fix is the one change that alters behaviour for *existing* experiments
  (it relaxes a blindness guard). It is deliberately excluded from the
  "non-breaking" claim above and left as an open decision below.

## 9. Ground-truth model for code review

A single label cannot express a review. The proposed model, `code-review-findings/v1`,
is written out in full in `experiment.draft.yml`. Shape:

```yaml
ground_truth:
  base_ref: <fixture>            # makes "pin base and head" checkable
  head_ref: <fixture>
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
  acceptable_additional_findings: [...]   # true, not required, never penalised
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

Five deliberate departures from the sketch in the order, each with a reason:

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

`relevant_evidence` / `decisive_reason` from the v1 ground truth are dropped for this
model: per-finding `evidence` and `rationale` carry the same information at the right
granularity. `known_traps`, `allowed_uncertainty` and `hard_failures` are kept as-is.

**No aggregate score.** Ten dimensions are reported separately (`finding_recall`,
`false_positives`, `severity_calibration`, `evidence_location_accuracy`,
`spec_coverage`, `scope_creep_detection`, `test_critique`, `unsupported_findings`,
`release_calibration`, plus `overhead` as diagnostic-only). A review that finds every
blocker *and* raises three false positives must remain visibly both; collapsing that
into `7.4/10` destroys the one thing this domain adds.

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

The shared prompt (in the draft) deliberately paraphrases the *task*, never the
method: it asks for base/head, two axes, evidence per criterion, prioritised findings
and an explicit verdict, because that is what a reviewer is asked for in practice. It
does not name the skill or its section structure — if it did, the baseline arm would
be handed the skill's content in the prompt and the experiment would measure nothing.
This is a real risk in this domain and should be a focus of the independent review.

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

## 14. Open design decisions

These are genuinely open and are the agenda for the independent design review. None is
decided here.

1. **C5 — how to fix the disclosure false positive.** Options: (a) an explicit
   per-experiment list of domain terms that are not disclosure; (b) require the
   skill-id match to sit next to an experiment-design noun, as the arm/noun rule
   already does; (c) leave it strict and accept that German code-review outputs are
   refused. (c) blocks the phase; (a) is the most explicit and stays fail-closed by
   default; (b) is the least configuration but weakens the guard for every experiment.
   **Recommendation: (a).** This is the one change that touches a blindness guarantee,
   so it should be decided by review, not by the implementer.
2. **How much prompt to give.** See §12. A prompt too close to the skill's structure
   destroys the contrast; one too vague makes the baseline fail for reasons unrelated
   to the skill. The draft's wording is a proposal, not a decision.
3. **Judge dimension scoring shape.** Per-dimension ordinal, per-dimension pass/partial/fail,
   or per-finding hit/miss plus per-dimension summary. Only the "no single total" rule
   is settled.
4. **How to count `acceptable_additional_findings`.** Currently defined as never
   penalised, but also never rewarded. Whether recall credit should exist for them is
   open.
5. **Whether CR-04's severity for F01 is right.** Called a blocker because AC-3 is an
   explicit acceptance criterion; a reviewer could defensibly call it should-fix. The
   `severity_calibration` dimension is only fair if that band is agreed in advance.
6. **Repetition count.** `recommended_repetitions: 3` copied from 4.2A without
   independent justification for this domain.
7. **Whether the diff-vs-base/head consistency check (§7.7) belongs in the pair
   harness or in a fixture lint.**

## 15. What B0 did not do

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
