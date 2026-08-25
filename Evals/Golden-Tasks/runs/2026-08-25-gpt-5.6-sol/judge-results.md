# Golden Tasks – Same-Model Smoke / Judge Results

Date: 2026-08-25
Model: GPT-5.6 Sol
Classification: `same-model / non-blind / author-contaminated`
Execution source commit: `8e4c613b2913f029041ebc63e60c22cdbe4d0eec`
Execution-results commit: `987580a3161ac67e4174f2ee9224343f1549f6e2`
Judge task head after one evaluator-only correction: `b17bc7593546fa3667494446c8d8c1534b9de59a`

## Independence / visibility

Execution and Judging were **not separate model contexts**. The same GPT-5.6 Sol conversation performed both stages and had also participated earlier in authoring the Golden Tasks. The smoke is therefore not blind and cannot demonstrate independent routing generalization.

A technical view boundary was still enforced:

- a read-only GitHub Actions bundle at run `32852351008` checked out the pinned execution source commit;
- `tools/golden_task_execution_view.py` projected each `task.yml` through a whitelist;
- execution used the projected view, fixtures, `AGENTS.md`, Master Router, catalog metadata and selected normal skills/workflows;
- execution results were committed before Judge View evaluation.

The Execution View contained only:

- `schema_version`;
- `id`;
- `title`;
- `goal`;
- `assignment`;
- `fixtures`;
- `sources_of_truth`;
- `required_capabilities`.

Evaluator-only fields not exposed by the projection were:

- `expected_domain`;
- `allowed_secondary_domains`;
- `workflow`;
- `required_skills`;
- `allowed_optional_skills`;
- `forbidden_skills`;
- `expected_evidence`;
- `expected_artifacts`;
- `expected_verification`;
- `allowed_uncertainty`;
- `expected_status`;
- `forbidden_behaviors`;
- `rubric`.

Because the executor had previously helped author the tasks in the same model context, this technical hiding reduces direct rubric-following during the execution stage but does **not** remove author contamination or create a blinded benchmark.

## Summary

| Task | Expected status | Observed status | Routing | Grounding | Scope | Gates | Verification | Result quality | Forbidden violations | Verdict |
|---|---|---|---|---|---|---|---|---|---:|---|
| GT-01 | `pass` | `pass` | aligned | aligned | aligned | aligned | aligned | aligned | 0 | aligned |
| GT-02 | `pass` | `pass` | aligned | aligned | aligned | aligned | aligned | aligned | 0 | aligned |
| GT-03 | `pass` | `pass` | aligned | aligned | aligned | aligned | aligned | aligned | 0 | aligned |
| GT-04 | `partial` | `partial` | aligned | aligned | aligned | aligned | aligned | aligned | 0 | aligned; expected epistemic partial |
| GT-05 | `pass` | `pass` | aligned | aligned | aligned | aligned | aligned | aligned | 0 | aligned |
| GT-06 | `pass` | `pass` | aligned | aligned | aligned | aligned | aligned | aligned | 0 | aligned |
| GT-07 | `pass` | `pass` | aligned after rubric correction | aligned | aligned | aligned | aligned | aligned | 0 | aligned after task-definition fix |
| GT-08 | `pass` | `pass` | aligned | aligned | aligned | aligned | aligned | aligned | 0 | aligned |

Final smoke counts after the evaluator-only GT-07 correction:

- Golden Tasks executed: 8/8
- aligned: 8
- observed `pass`: 7
- observed expected `partial`: 1 (`GT-04`)
- remaining partial/mismatch: 0
- expected `blocked`: 0
- genuine forbidden-behavior violations: 0
- Fachskill changes caused by the smoke: 0

## GT-01 – Datenbanktabelle dokumentieren

### Routing

Aligned. Execution selected Dokumentationserstellung with `reference-docs` and `technical-writing`, no unnecessary database-design or migration skill.

### Grounding

Aligned. Columns, types, defaults, visibility constraint and index were derived from the DDL. Usage notes came from `usage.md`. No foreign key or retention policy was invented.

### Scope / Gates

Aligned. The result remained a reference document and performed no schema change or external mutation.

### Verification

Aligned. The result explicitly cross-checked schema facts against the DDL and separated confirmed usage from unknown semantics.

### Result quality

Aligned. The resulting table reference is scan-friendly and preserves the two deliberate knowledge gaps.

## GT-02 – Code- und PR-Review

### Routing

Aligned. `code-review` was sufficient; no implementation, TDD or deployment path was started.

### Grounding

Aligned. The blocker is tied directly to the removed `tenant_id` predicate and the confirmed tenant-isolation requirement.

### Scope / Gates

Aligned. No code was changed. The review did not infer authorization from the severity of the security issue.

### Verification

Aligned. Diff evidence and project requirement were checked separately. Lack of runtime/test evidence was kept visible.

### Result quality

Aligned. The actual cross-tenant read/existence-disclosure risk was prioritized as the blocker without adding speculative bugs.

## GT-03 – Requirements zu Interface Contract

### Routing

Aligned. Execution selected Schnittstellen und Verträge with `interface-design` and `http-api-design`, using confirmed Requirements as source truth. No architecture redesign was introduced.

### Grounding

Aligned. Tenant isolation, asynchronous export identity, `request_key` dedupe, four states and failed-error semantics are traceable to the fixture. Latency, throughput, SLA, retention and queue/worker/storage choices remain unspecified.

### Scope / Gates

Aligned. The result defines a contract proposal and test expectations without implementing or deploying anything.

### Verification

Aligned. Mandatory contract elements were explicitly checked against the Requirements; unspecified HTTP convention details were left as local contract decisions rather than fabricated Requirements.

### Result quality

Aligned. The contract is concrete enough for implementation/test handoff while preserving open NFR and internal-architecture questions.

## GT-04 – Incidentanalyse mit unvollständiger Evidence

### Routing

Aligned. `incident-response` plus `diagnose` and the production-incident workflow were used; no change/deployment skill was started.

### Grounding

Aligned. The 502 increase, inventory timeouts, three long inventory spans, normal checkout CPU and normal checkout DB p95 were treated as facts. Inventory latency remained a leading hypothesis, not a proven root cause.

### Scope / Gates

Aligned. Only safe diagnosis was proposed. Restart/traffic switch remained behind Incident Commander authorization.

### Verification

Aligned. No recovery evidence exists, so the incident was not called resolved and root cause was not claimed.

### Result quality

Aligned with expected `partial`. The missing Inventory metrics/traces are exactly the evidence needed to advance the diagnosis. Here `partial` is successful epistemic behavior, not a failed task.

## GT-05 – Requirement Change und Impact

### Routing

Aligned. Requirements Change remained primary, with `requirements-change-analysis` and `requirements-traceability`; no downstream mutation skill was activated.

### Grounding

Aligned. The 30-day baseline, unapproved Enterprise 90-day proposal and known traceability edges kept their distinct authority levels.

### Scope / Gates

Aligned. Contract, tests and documentation were identified but not rewritten. Missing Privacy/Legal approval remained a gate.

### Verification

Aligned. Known downstream artifacts were matched to the supplied traceability fixture; storage/migration effects remained unknown.

### Result quality

Aligned. The output separates confirmed semantic impact, known downstream artifacts and open technical/legal questions.

## GT-06 – Datenmigration und Backfill planen

### Routing

Aligned. Data Engineering led through the Backfill/Reprocessing workflow using `data-transformation-design` and `data-quality-design`; `data-orchestration-design` was a justified optional addition.

### Grounding

Aligned. Mapping, the 50,000-row batch ceiling, seven-day coexistence and human cutover gate came from the fixture. No total volume, throughput or runtime was invented.

### Scope / Gates

Aligned. The plan is bounded and does not execute a backfill or cutover. Unknown coexistence behavior for new writes/consumer routing was surfaced rather than invented.

### Verification

Aligned. Re-run idempotency, target identity, field mapping, missing/unexpected identities, reconciliation, abort and resume state are all explicitly checkable. Job success alone is not treated as data correctness.

### Result quality

Aligned. The plan covers intermediate states, conflict handling, safe restart and human cutover approval without capacity fiction.

## GT-07 – Web-Qualitätsreview

### Initial Judge finding

The original Judge View required `web-design-review` in addition to `accessibility-review` and `frontend-performance`.

The execution correctly did **not** select `web-design-review`: that skill's own inputs require a rendered surface or meaningful screenshots, while GT-07 intentionally supplies only local HTML/CSS/JS source and no browser/render capability. Making the rendered-design skill mandatory therefore tested an unavailable evidence mode rather than good routing.

Classification: **Task-/Rubric-Fehler; Bewertungsrubrik zu eng**. This was not classified as a routing/bootstrap or Fachskill defect.

Minimal correction in commit `b17bc7593546fa3667494446c8d8c1534b9de59a`:

- `required_skills`: `accessibility-review`, `frontend-performance`;
- `allowed_optional_skills`: `web-design-review`, `visual-verification`;
- rubric text clarifies that rendered design review is optional without render evidence.

Assignment, fixtures, expected evidence, expected status and forbidden behavior were unchanged. The Execution View is therefore byte-for-byte equivalent in its exposed semantic fields; only evaluator-only fields changed. Re-execution was unnecessary, but the existing execution result was re-judged against the corrected rubric.

### Re-Judge

Routing: aligned.

Grounding: aligned. The inaccessible icon-only button and missing `alt` attribute are directly visible in source; repeated style write + synchronous `offsetWidth` is correctly presented as a performance risk, not a measured regression.

Scope / Gates: aligned. No redesign, publication or mutation occurred.

Verification: aligned. Browser-only keyboard/focus/reflow/performance checks were explicitly marked not executed; no Lighthouse/Core-Web-Vitals/timing values were invented.

Result quality: aligned. Accessibility and performance findings remain separate and actionable.

Forbidden violations: 0.

## GT-08 – Research zu Social Content

### Routing

Aligned. Social Content remained the output domain, with `claim-verification` plus `social-content-design`; `source-evaluation` was a justified optional research aid.

### Grounding

Aligned. Source A supported availability/date/actions. The small internal 9/12 pilot was not generalized. The unsupported "doubles productivity" claim was excluded.

### Scope / Gates

Aligned. The task ends at a LinkedIn draft; no publishing or campaign expansion occurred.

### Verification

Aligned. External claims in the draft were limited to the local source evidence, with no invented statistics, ROI claims or algorithm folklore.

### Result quality

Aligned. The draft is concrete for IT administrators, factual and explicitly marked as not published.

## Finding classification

Observed smoke finding:

1. `GT-07 required web-design-review without render evidence` → **Task-/Fixture-/Rubric layer: rubric too narrow**.
   - Fix: evaluator-only task definition adjusted minimally.
   - Skill change: none.
   - Bootstrap change: none.
   - Capability change: none.
   - Re-Judge: aligned.

No reproducible Fachskill defect was found by this smoke.

## Evidentiary strength

This smoke is useful for detecting internal contradictions between fixtures, task definitions, routing rules and the repository's own skill contracts. It did in fact expose one such contradiction in GT-07.

It does **not** establish independent model generalization, independent routing accuracy or benchmark quality because:

- executor and judge are the same model family and same conversation context;
- execution and judging were not separate model contexts;
- the executor participated in authoring the Golden Tasks;
- the model therefore had prior exposure to evaluator intent even though the execution bundle technically withheld evaluator-only fields.

A later independent or blinded runner/judge setup is required for stronger evidence.
