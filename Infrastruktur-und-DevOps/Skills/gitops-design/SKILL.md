---
name: gitops-design
description: Entwirft oder prüft GitOps-Workflows mit versioniertem Desired State, Pull-/Controller-Reconciliation, Sync, Drift, Prune, Self-Heal, Repository-/Branch-Gates und Controller-Rechten. Verwenden bei Argo CD, Flux oder ähnlichen Continuous-Reconciliation-Systemen. Nicht für allgemeine Git-Nutzung oder einmalige IaC-Applies verwenden.
---

# GitOps Design

## Ziel

Continuous Reconciliation so gestalten, dass Source of Truth, Änderungsautorität und Blast Radius eindeutig sind.

## Arbeitsweise

1. Desired-State-Source und Ownership bestimmen.
2. Controller, Zielumgebung und Berechtigungen erfassen.
3. Pull-/Sync-/Reconcile-Verhalten klären.
4. Branch-/Merge-/Environment-Gates gegen reale Außenwirkung prüfen.
5. Prune, Self-Heal, Drift Ignore und Retry explizit bewerten.
6. Render-/Schema-/Policy-Validation vor Merge/Reconcile einplanen.
7. Secrets und untrusted Contributions prüfen.
8. Revert-/Rollbackpfad und Reconciliation-Latenz berücksichtigen.

## Nicht tun

- jede deklarative Pipeline als GitOps bezeichnen;
- Git Commit als harmlose Aktion behandeln, wenn Auto-Reconcile Produktion ändert;
- Prune/Self-Heal ohne Blast-Radius-Review aktivieren;
- Controllerrechte aus Bequemlichkeit auf Cluster-Admin setzen;
- Live-Clusterzustand aus Repo-Dateien erfinden.

## Ausgabe

```text
Desired State Source
Controller / Targets
Reconciliation Model
Permissions
Prune / Self-Heal
Validation / Policies
Drift Model
Change Gates
Rollback / Revert
Open Risks
```

## Related

- `infrastructure-as-code`
- `infrastructure-change-review`
- `ci-pipeline-design`
- `tool-permission-review`
- `infrastructure-review`