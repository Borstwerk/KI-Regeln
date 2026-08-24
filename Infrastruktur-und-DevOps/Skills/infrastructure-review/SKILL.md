---
name: infrastructure-review
description: Auditiert eine Infrastruktur-/DevOps-Lösung unabhängig auf Desired State, Ownership, Drift, State, Environments, CI, Build-Artefakte, Deployment, GitOps, Permissions, Policies, Recovery und Evidence. Verwenden für größere Brownfield- oder Release-Audits. Nicht als Pentest, SLO-Review oder tatsächliche Infrastrukturänderung verwenden.
---

# Infrastructure Review

## Ziel

Infrastruktur- und Deliverymechanik systematisch prüfen, ohne sie ungefragt umzubauen oder auszuführen.

## Prüfachsen

1. Desired State und Ownership;
2. State / Actual State / Drift;
3. Environment-Grenzen;
4. Preview / Plan / Change Gates;
5. Secrets / Permissions / Execution Boundaries;
6. CI-/Automation-Reproduzierbarkeit;
7. Build-Artefakte / Identity / Provenance;
8. Container Runtime Contract, falls relevant;
9. Deployment / Promotion / Rollback;
10. GitOps / Continuous Reconciliation, falls relevant;
11. Policy Enforcement;
12. Recovery / Fresh Evidence.

## Arbeitsweise

- lokale Sources of Truth zuerst;
- Preview-/Runtime-Evidence nicht erfinden;
- Findings nach Blast Radius und Reversibilität priorisieren;
- Security-, Database-, Testing-, Architecture- und Reliability-Themen an deren Bereiche übergeben;
- keine Apply-/Deploy-/Destroy-Aktion aus einem Review ableiten.

## Ausgabe

```text
Scope
Sources of Truth
Findings [severity, evidence, impact]
State / Drift Risks
Change / Deployment Risks
Permission / Secret Risks
Recovery Gaps
Missing Evidence
Verdict
```

## Verdict

- `PASS`
- `PASS_WITH_FINDINGS`
- `BLOCKED`
- `FAIL`

Review-Verdict ist keine Apply-/Deploy-Autorisierung.

## Related

- `infrastructure-change-review`
- `code-review`
- `tool-permission-review`
- `test-suite-review`