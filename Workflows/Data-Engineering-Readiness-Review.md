# Workflow – Data Engineering Readiness Review

## Ziel

Vor Go-Live, größerem Cutover oder relevanter Änderung unabhängig prüfen, ob ein Datenfluss fachlich, technisch und betrieblich ausreichend belegt ist.

## Ablauf

```text
lokale Specs / Contracts / Pipelineevidence
→ data-engineering-review
→ gezielte Fachskills für Findings
→ aktualisierte Evidence
→ erneuter Review
→ lokales Publish-/Change-Gate
```

## Reviewbasis

Mindestens soweit relevant:

- Business-/Consumerziel;
- Sources of Truth und Ownership;
- Grain / Keys / Semantik;
- Ingestion / Change / Delete / Replay;
- Transformation / Incremental / History;
- analytisches Modell;
- Quality / Freshness / Reconciliation;
- Data Contract und Consumerimpact;
- Lineage / Provenance;
- Orchestrierung / Backfill;
- Publish / Retention / Lifecycle;
- Runtime-/Freshness-/Backlog-Evidence;
- Security-/Privacy-/Execution-Grenzen.

## Evidence-Regel

Repo-, DAG-, SQL- oder Contractdateien belegen Design. Produktionsreife benötigt dort, wo relevant, frische Runtime-/Daten-Evidence.

## Findings

`data-engineering-review` kennzeichnet Evidence als:

- `CONFIRMED`;
- `LIKELY`;
- `UNVERIFIED`;
- `CONFLICTING`.

Tiefe Findings gehen an die spezialisierten Data-Engineering-Skills oder Nachbardomänen.

## Verdict

- `READY_FOR_LOCAL_GATE`
- `READY_WITH_FINDINGS`
- `BLOCKED`
- `UNVERIFIED`

Das Verdict ist keine Freigabe für Deploy, Publish, Backfill oder Cutover.

## Ergebnis

```text
Scope / Sources of Truth
Prioritized Findings
Evidence Status
Data / Consumer Risks
Required Handoffs
Open Gates
Review Verdict
Local Decision Status
```

## Leitgedanke

> Production-ready ist ein Datenfluss erst, wenn nicht nur Code und Jobs, sondern auch Datenbedeutung, Consumerwirkung und Recovery ausreichend belegt sind.