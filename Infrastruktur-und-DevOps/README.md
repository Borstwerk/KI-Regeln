# Infrastruktur und DevOps

## Zweck

Dieser Bereich beschreibt allgemeine, tool- und providerneutrale Regeln für reproduzierbare Infrastruktur, Build-/Delivery-Automation und kontrollierte Änderungen an Zielumgebungen.

Kernidee:

> Infrastruktur- und Delivery-Automation sollen gewünschte Zustände nachvollziehbar beschreiben, Änderungen vor Wirkung sichtbar machen und reale Außenwirkung nur über passende Gates ausführen.

## Scope

Behandelt werden insbesondere:

- Desired State und Infrastructure as Code;
- State Ownership, Drift und Reconciliation;
- Change Preview, Plan, Apply und Gates;
- Umgebungen, Konfiguration und Promotion;
- CI-Pipelines und Automatisierung;
- reproduzierbare Build-Artefakte und Provenance;
- Container Builds und Runtime-Verträge;
- Deploymentstrategien, Promotion, Abort und Rollback;
- GitOps und Continuous Reconciliation;
- Kubernetes als wichtige Referenzplattform für Workloads und Rollouts;
- Policy as Code und Guardrails;
- Secrets, Permissions und Execution Boundaries.

## Nicht der Scope

- **Software Architecture:** entscheidet, welche Systeme, Plattformen und Topologien existieren sollen.
- **Testing und QA:** entscheidet, welche Qualitätsrisiken mit welchen Tests geprüft werden.
- **Sicherheit:** definiert Threat Models, Secret-/Credential-Schutz, Supply-Chain-Vertrauen und Security Policies im Detail.
- **Reliability:** behandelt später SLOs, Incidents, Capacity, Resilience, Alerting und Chaos Engineering.
- **Datenbanken:** behandelt Schema-/Datenmigrationen und DB-spezifischen Betrieb.
- **Provider-/Toolsyntax:** Terraform, OpenTofu, Pulumi, CloudFormation, Ansible, Kubernetes, Helm, Kustomize, Argo CD, Flux, Docker oder GitHub Actions bleiben konkrete Adapter.

## Zentrale Zustandsmodelle

```text
Desired State
≠
Actual State
```

```text
Validate
→ Preview / Plan
→ Review
→ Gate
→ Change
→ Fresh Verification
```

```text
Build
≠
Deploy
≠
Release
```

```text
Rollback
≠
Undo aller Nebenwirkungen
```

## Risikoklassen

### READ / VALIDATE

Lesen, linten, rendern, Schema prüfen, Konfiguration analysieren.

### BUILD

Artefakt erzeugen, ohne eine Zielumgebung zu verändern.

### PLAN / PREVIEW

Geplante Wirkung gegen aktuellen Zustand berechnen oder simulieren, ohne die eigentliche Änderung auszuführen.

### CHANGE / DEPLOY

Reale Infrastruktur oder Zielumgebung verändern.

### DESTRUCTIVE / STATE / RECOVERY

Destroy, Prune, destructive Replacement, State-Manipulation, Restore, Rollback, Force-Reconcile oder andere besonders weitreichende Zustandsänderungen.

## Operative Skills

- `infrastructure-as-code`;
- `infrastructure-change-review`;
- `ci-pipeline-design`;
- `container-build`;
- `deployment-strategy`;
- `gitops-design`;
- `infrastructure-review`.

## Leitgedanken

> Preview ist Evidence, keine Autorisierung.

> Automatisierung reduziert manuelle Arbeit, vergrößert aber gleichzeitig die Reichweite einer Fehlentscheidung.