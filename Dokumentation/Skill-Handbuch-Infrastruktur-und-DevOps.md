# Skill-Handbuch – Infrastruktur und DevOps

## Wann dieser Bereich hilft

Bei Infrastructure as Code, CI/CD, Container Builds, Deployments, GitOps und größeren Infrastrukturreviews.

## `infrastructure-as-code`

Für Desired State, IaC, State/Ownership, Drift und Preview-Vorbereitung.

Nicht für Plattformarchitektur oder tatsächliches Apply ohne Gate.

## `infrastructure-change-review`

Für Plan-, Diff-, Preview- oder Change-Set-Reviews vor realer Außenwirkung.

Verdicts:

```text
SAFE_TO_PROCEED_TO_GATE
REVIEW_REQUIRED
DESTRUCTIVE
UNVERIFIED
```

Der erste Status bedeutet nicht `APPLY AUTHORIZED`.

## `ci-pipeline-design`

Für Pipeline-DAG, Trigger, Artifacts, Cache, Credentials, Environment-Grenzen und Gates.

Testing entscheidet weiterhin, welche Tests benötigt werden.

## `container-build`

Für reproduzierbare OCI-/Containerartefakte und deren Runtime-Vertrag.

Security entscheidet die zulässigen Privilegien und Supply-Chain-Anforderungen.

## `deployment-strategy`

Für Rolling, Blue-Green, Canary, Shadow, Recreate oder Feature-gated Releases.

Der Skill braucht lokale Health-/SLO-/Produktkriterien und erfindet keine universellen Schwellen.

## `gitops-design`

Für Systeme mit versioniertem Desired State und Continuous Reconciliation.

Wichtige Besonderheit:

> Wenn ein Controller Produktion automatisch reconciliert, kann bereits der Merge der Desired-State-Änderung eine extern wirksame Aktion sein.

## `infrastructure-review`

Unabhängiger Gesamtcheck über IaC, State/Drift, CI, Build, Deployment, GitOps, Permissions, Policies, Recovery und Evidence.

Kein Pentest, kein SLO-Design und kein Apply.

## Zwei Standardworkflows

### Infrastrukturänderung

`../Workflows/Infrastruktur-Aenderung.md`

```text
IaC
→ Validate
→ Preview
→ Change Review
→ Gate
→ Apply
→ Fresh Verification
```

### Build / Deploy / Promotion

`../Workflows/Build-Deploy-und-Promotion.md`

```text
Source
→ Pipeline
→ Build
→ Artifact
→ Evidence
→ Deployment Strategy
→ Gate
→ Deploy
→ Promote / Abort
```

## Tooladapter

Terraform, OpenTofu, Pulumi, CloudFormation, Ansible, Kubernetes, Helm, Argo CD, Flux, Docker, GitHub Actions usw. bleiben projektspezifisch. Ihre aktuellen Produktregeln können die allgemeinen Skills ergänzen.

## Maturity

Alle sieben Skills starten `experimental` mit `partial` Evalabdeckung. Die Evalpacks sind definiert, aber breite reale Regressionserfahrung muss erst entstehen.

## Leitgedanke

> Preview ist nicht Apply, Pipelinegrün ist nicht Deployfreigabe und Rollback ist keine Zeitmaschine.