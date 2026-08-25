# Golden Tasks – Execution Results

Run: 2026-08-25 / GPT-5.6 Sol
Execution source commit: `8e4c613b2913f029041ebc63e60c22cdbe4d0eec`
Execution bundle workflow run: `32852351008`

## Method note

This execution stage used the projected Execution View plus local fixtures, `AGENTS.md`, the Master Router, catalog metadata and only the skills/workflows selected during routing.

The projected view exposed only `schema_version`, `id`, `title`, `goal`, `assignment`, `fixtures`, `sources_of_truth` and `required_capabilities`. Evaluator-only routing expectations, expected status, forbidden behavior lists and rubric were not used during this execution stage.

This is nevertheless not a blind benchmark: the same model context participated earlier in creating the Golden Tasks. The later run report must therefore classify the smoke as `same-model / non-blind / author-contaminated`.

---

## GT-01 – Datenbanktabelle dokumentieren

### Selected route

- Primary area: Dokumentationserstellung
- Workflow: none; the task is narrow enough for direct skill composition
- Skills: `reference-docs`, `technical-writing`

### Result

# `customer_note` reference

Purpose: stores textual notes in a customer context.

| Column | Type | Nullability | Default / constraint |
|---|---|---|---|
| `id` | `BIGINT` | not null via primary key | primary key |
| `customer_id` | `BIGINT` | `NOT NULL` | none defined |
| `body` | `TEXT` | `NOT NULL` | none defined |
| `visibility` | `VARCHAR(16)` | `NOT NULL` | default `'internal'`; allowed values `internal`, `shared` |
| `created_at` | `TIMESTAMPTZ` | `NOT NULL` | default `now()` |
| `archived_at` | `TIMESTAMPTZ` | nullable | none defined |

Constraint: `ck_customer_note_visibility` enforces `visibility IN ('internal', 'shared')`.

Index: `ix_customer_note_customer_created` on `(customer_id, created_at DESC)`.

Confirmed usage notes:

- `internal` is the default visibility; `shared` is the second allowed value.
- Archiving retains the row and sets `archived_at`.

Explicit unknowns:

- No foreign-key relationship is defined in the supplied schema; none is claimed.
- Retention and deletion periods are not known from the fixtures.

### Verification

Every listed column, type, nullability/default, constraint and index was cross-checked against `table-schema.sql`; usage statements were limited to `usage.md`. No schema redesign or mutation was performed.

---

## GT-02 – Code- und PR-Review

### Selected route

- Primary area: Programmieren
- Workflow: none; one focused diff is sufficient
- Skill: `code-review`

### Result

**BLOCKER – Tenant isolation is removed from the order lookup.**

The diff changes the query from `WHERE id = :order_id AND tenant_id = :tenant_id` to `WHERE id = :order_id` and removes the `tenant_id` parameter. The confirmed project requirement states that every database access for `GET /orders/{id}` must constrain both values and must not expose another tenant's order or even confirm its existence.

Impact: an authenticated caller can cause the endpoint to fetch an order solely by ID without the required tenant boundary. That directly violates the confirmed security/API requirement and creates a cross-tenant read/existence-disclosure risk.

No code change is proposed or applied because this is a review task.

### Verification boundary

The finding is directly supported by the supplied diff and project requirement. No test suite or runtime evidence was supplied, so no claim is made that a particular test currently fails or passes.

---

## GT-03 – Requirements zu Interface Contract

### Selected route

- Primary area: Schnittstellen und Verträge
- Supporting truth: confirmed Requirements
- Workflow: `Workflows/Schnittstellenvertrag-Entwerfen-und-Aendern.md`
- Skills: `interface-design`, `http-api-design`

### Result

Proposed HTTP contract, with tenant identity derived from authenticated context rather than caller-supplied tenant data:

**Start export**

`POST /exports`

Request body:

```json
{
  "request_key": "client-stable-key"
}
```

New requests create one asynchronous export resource and return an `export_id`. Reuse of the same `request_key` within the same tenant must resolve to the same logical export and must not create a second export. The exact repeat-response status code should follow the project's HTTP convention; the idempotency invariant is the contractual requirement.

Response representation:

```json
{
  "export_id": "exp_123",
  "status": "queued"
}
```

**Read export status**

`GET /exports/{export_id}`

Response representation:

```json
{
  "export_id": "exp_123",
  "status": "queued|running|succeeded|failed",
  "error_category": null
}
```

For `failed`, `error_category` is required and machine-readable. Internal stack traces are never part of the public response. For non-failed states the field may be absent or null according to the project's schema convention.

Tenant boundary: start and read operations are scoped to the authenticated tenant. A resource belonging to another tenant must not be exposed; the external not-found/error behavior should avoid revealing its existence.

Contract-level test expectations:

- same tenant + same `request_key` cannot produce two export IDs;
- another tenant cannot read the resource;
- only the four confirmed status values are emitted;
- `failed` carries a machine-readable category without internal stack traces.

Open / deliberately unspecified:

- latency, throughput, SLA/availability and retention;
- queue/worker technology;
- storage or deployment architecture;
- exact HTTP status choices where the requirements do not prescribe a local convention.

No architecture redesign or NFR target was invented.

---

## GT-04 – Incidentanalyse mit unvollständiger Evidence

### Selected route

- Primary area: Reliability und System-Observability
- Workflow: `Workflows/Produktionsincident.md`
- Skills: `incident-response`, with `diagnose` for the technical hypothesis path

### Result

**Incident state:** active degradation; not resolved.

Confirmed facts:

- Checkout error rate rose from 0.4% at 12:00 to 8–11% from 12:03, mainly HTTP 502.
- Affected application requests repeatedly log `inventory request timed out after 2000ms`.
- Three available trace IDs contain a long `inventory.reserve` span.
- Checkout CPU and Checkout DB p95 remain within the supplied normal ranges.
- Direct Inventory dashboards and complete distributed traces are unavailable.

Hypothesis, not root cause:

Inventory-side latency or a dependency on the `inventory.reserve` path is a strong next hypothesis because timeout logs and the available spans correlate with affected requests. The evidence does **not** establish why Inventory is slow or whether Inventory itself is the root cause.

Next safe diagnostics:

1. Obtain Inventory health, latency, timeout and error metrics for the incident window.
2. Expand tracing/log correlation for the supplied trace IDs and compare successful versus failing checkout requests.
3. Inspect Inventory dependency/network evidence and relevant recent runtime changes if such records exist.
4. Continue measuring checkout impact while diagnosis proceeds.

Gate:

A restart or traffic switch requires Incident Commander approval according to the supplied runbook. No production mutation is executed or treated as authorized by urgency alone.

Completion boundary:

There is no fresh recovery evidence, so the incident is not declared resolved. Root cause remains unconfirmed.

---

## GT-05 – Requirement Change und Impact

### Selected route

- Primary area: Requirements und Spezifikations-Engineering
- Workflow: `Workflows/Requirements-Change-und-Impact.md`
- Skills: `requirements-change-analysis`, `requirements-traceability`

### Result

Current baseline: all successful export files are deleted after 30 days; status exposes `expires_at`; operations documentation describes 30-day retention and cleanup.

Proposed semantic delta in CR-42: retention becomes customer-class dependent — 90 days for Enterprise customers, 30 days for Standard customers. CR-42 is requested but not part of the approved baseline.

Direct requirement impact:

- `RQ-17`: would change from one universal retention period to conditional retention.
- `RQ-18`: `expires_at` remains relevant, but its value would depend on the approved customer/retention rule.
- `RQ-19`: operations documentation would need to describe the conditional rule after approval.

Known downstream impact from traceability:

- `contracts/export-api.yml` / `ExportStatus.expires_at`;
- `tests/export_retention_test.py` / `test_export_deleted_after_30_days`;
- `docs/export-operations.md` / `Retention`.

Open impact/evidence:

- Privacy/Legal approval for 90 days is missing.
- Storage and migration consequences have not been analysed.
- Whether customer classification is already an authoritative input to cleanup/status calculation is not established by the fixture.

Decision/gates:

Do not modify the approved baseline or downstream artifacts yet. Obtain Privacy/Legal approval and technical impact evidence, then decide whether CR-42 is accepted/revised/deferred according to local policy; only after approval should supersession and downstream changes be planned.

---

## GT-06 – Datenmigration und Backfill planen

### Selected route

- Primary area: Data Engineering
- Workflow: `Workflows/Backfill-und-Reprocessing.md`
- Skills: `data-transformation-design`, `data-quality-design`, `data-orchestration-design`

### Result

**Objective:** backfill `legacy_events` into `events_v2` using only the confirmed mapping.

Bounded execution:

- Process deterministic source slices of at most 50,000 rows, preferably stable `id` ranges.
- Give each run/batch a stable `migration_batch` value for traceability.
- Record the exact source range and batch identifier before execution.

Transformation:

- `id` → `event_id`
- `account_id` → `tenant_id`
- parse confirmed-valid JSON from `payload` → `payload_json`
- `created_at` → `occurred_at`
- set `migration_batch` from the current backfill batch

Idempotency / partial state:

- Treat `event_id` as the target identity.
- Re-running a slice must not create duplicate rows.
- If an existing target row for the same `event_id` differs from the expected mapped values, stop that slice and reconcile rather than silently overwrite it.
- A failed slice is retried only after its partial-write state is known.

Reconciliation per slice:

- compare source IDs in the slice with target `event_id` coverage;
- require no missing or unexpected target identities for the slice;
- compare mapped values for sampled or fully queryable rows as appropriate to the execution environment;
- reconcile source-row count against the target rows attributable to the batch/range, without inventing a tolerance.

Coexistence:

Source and target must coexist for seven days. The fixture does not define how new writes are mirrored or which store consumers use during coexistence, so that operational behavior is an execution blocker that must be clarified before a real cutover/backfill plan is approved for production.

Abort / recovery:

Abort a slice on conflicting target content, unbounded source/target load, repeated write errors or failed reconciliation. Preserve the last completed range and batch evidence so the next run can resume from a known state.

Authorization:

No total record count or runtime estimate is invented. No backfill or cutover is executed. Final cutover remains behind the explicitly required human approval.

---

## GT-07 – Web-Qualitätsreview

### Selected route

- Primary area: Webentwicklung
- Workflow: none; the fixture supports a focused static review
- Skills: `accessibility-review`, `frontend-performance`

### Result

Confirmed static accessibility findings:

1. **Menu button has no accessible name.** Its only content is an SVG marked `aria-hidden="true"`; there is no text or `aria-label`.
2. **`status.png` lacks an `alt` attribute.** The source does not establish whether the image is decorative or informative, so the correct alternative text cannot be invented; the missing decision/attribute is the finding.

Static web-quality / reflow risk:

- `.card` has a fixed content width of 320px plus 16px padding on each side with default box sizing, so the rendered box can require 352px. That creates a concrete narrow-viewport overflow/reflow risk that should be checked in a browser.

Confirmed performance risk from source:

- The script performs 200 alternating style writes to `card.style.width` and synchronously reads `card.offsetWidth` after each write. This pattern can force repeated layout work (layout thrashing).
- No timing, Core Web Vitals or Lighthouse score is inferred from source alone.

Verification boundary:

The HTML/CSS/JS source was statically inspected. Keyboard/focus behavior, contrast, actual reflow and measured performance require a browser/runtime and are therefore not reported as passed.

No redesign or code mutation was performed.

---

## GT-08 – Research zu Social Content

### Selected route

- Primary areas: Recherche → Social Media und Content-Präsenz
- Workflow: none; one bounded claim check followed by one draft is sufficient
- Skills: `source-evaluation`, `claim-verification`, `social-content-design`

### Evidence decision

- Source A is the strongest direct source for availability and supported actions: the local fixture identifies it as the official release note and explicitly confirms EU availability from 1 August 2026 plus selection, bulk check and CSV export.
- Source B is limited pilot feedback (9/12 voluntary respondents) and explicitly non-representative; it is unnecessary for the requested availability/update message and is omitted from the draft.
- Source C's claim that the feature doubles productivity has no method, data or primary source and is not used as fact.

### Result – LinkedIn draft

**Draft – not published**

Bulk Policy Check ist seit dem 1. August 2026 für EU-Kunden verfügbar.

Wer regelmäßig mehrere Policy-Dateien prüft, kann jetzt:

- mehrere Dateien auswählen,
- einen gemeinsamen Check starten,
- die Ergebnisse als CSV exportieren.

Für IT-Administratoren ist das vor allem ein neuer gebündelter Arbeitsweg — ohne dass wir daraus unbelegte Produktivitäts- oder ROI-Versprechen ableiten.

Wenn die Funktion in eurem freigegebenen Produktzugang verfügbar ist, könnt ihr euch den neuen Ablauf dort ansehen.

### Boundary

No productivity statistic, usage-rate claim, benchmark or algorithm folklore was added. This artifact is a draft only; no publishing action was performed.
