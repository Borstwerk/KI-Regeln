---
name: interface-review
description: Auditiert einen bestehenden oder geplanten Schnittstellenvertrag unabhängig auf Consumer-Fit, Semantik, Fehler, Compatibility, Evolution, Auth-Grenzen, Idempotenz, Discoverability und Testbarkeit. Verwenden für Gesamtfreigaben oder Brownfield-Audits. Nicht als Implementierungs- oder Penetrationstest verwenden.
---

# Interface Review

## Ziel

Eine Schnittstelle als Consumervertrag prüfen und Findings priorisiert sichtbar machen.

## Prüfachsen

1. **Ownership und Consumer Fit** – Provider, Owner, Consumer, Tasks und Stabilität klar?
2. **Semantik** – Operationen/Messages und Feldbedeutung eindeutig?
3. **Schema** – required/optional/null/defaults/enums sauber?
4. **Failure Contract** – Fehler und Recovery maschinenlesbar?
5. **Idempotenz/Retry/Concurrency** – Wiederholung und Konflikte definiert?
6. **Async-Semantik** – Delivery, Ordering, Replay, Dead Letter, falls relevant?
7. **Auth/Tenant** – beobachtbare Berechtigungsgrenzen explizit?
8. **Compatibility** – bestehende Consumer und Change Policy berücksichtigt?
9. **Evolution** – Deprecation/Migration/Sunset handhabbar?
10. **Artifacts/Discoverability** – kanonischer Contract auffindbar und driftarm?
11. **Testbarkeit** – Contract-/Integrationstests können Zusagen verifizieren?

## Arbeitsweise

- zuerst kanonische lokale Sources of Truth lesen;
- keine Redesign-Ideen vor Findings stellen;
- Findings nach Auswirkung priorisieren;
- bei fehlenden Consumern/Baseline nicht raten;
- Security-, Architecture- oder Reliability-Funde an deren Bereiche verweisen.

## Ausgabe

```text
Scope
Sources of Truth
Findings [severity, evidence, impact]
Compatibility Risks
Missing Contract Elements
Open Questions
Required Tests / Gates
Verdict
```

## Verdict

- `PASS`
- `PASS_WITH_FINDINGS`
- `BLOCKED`
- `FAIL`

Ein Review-Verdict ist keine produktive Deploymentfreigabe.

## Related

- `interface-design`
- `contract-change-review`
- `contract-testing`
- `code-review`