# Quellen und Inspirationen

Dieser Bereich synthetisiert toolneutrale Prinzipien aus Primärquellen, Standards, Herstellerdokumentation und aktuellen Agent-Skills.

## Primär- und Standardquellen

### Terraform / HashiCorp

https://developer.hashicorp.com/terraform/cli/commands/plan
https://developer.hashicorp.com/terraform/tutorials/state

Für Plan-/Apply-Modell, State und Drift.

### OpenTofu

https://opentofu.org/docs/cli/commands/plan/

Für providerneutrale Gegenprüfung des Plan-/Preview-Modells und den Hinweis, dass gespeicherte Planfiles sensitive Daten enthalten können.

### Kubernetes

https://kubernetes.io/docs/concepts/architecture/controller/
https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
https://kubernetes.io/docs/concepts/security/pod-security-admission/

Für Continuous Reconciliation, Rollouts und die Grenze zwischen Workload-/Deploymentmechanik und Security Policy.

### OpenGitOps

https://opengitops.dev/

Für die Kernprinzipien deklarativ, versioned/immutable, pulled automatically und continuously reconciled.

### Argo CD / Argo Rollouts

https://argo-cd.readthedocs.io/
https://argoproj.github.io/rollouts/

Für GitOps-Reconciliation und progressive Delivery als aktuelle Implementierungsreferenzen.

### Open Policy Agent

https://www.openpolicyagent.org/docs

Für die Trennung von Policy Decision und Enforcement.

### SLSA

https://slsa.dev/spec/v1.2/provenance

Für Build Provenance und Artefaktherkunft.

### Docker Build

https://docs.docker.com/build/building/multi-stage/

Für Build-/Runtime-Trennung bei Containerimages.

## Skill-Inspirationen

### hashicorp/agent-skills – terraform-style-guide

Offizieller Terraform-Adapter mit konkreten HCL-/Provider-/State-/Security-Konventionen. Nur die toolübergreifend belastbaren Prinzipien werden zentral übernommen.

### fluxcd/agent-skills – gitops-repo-audit

Offizieller Flux-Skill mit guter Trennung von Repository-Audit, Schema-/Render-Validation und Live-Cluster-Debugging.

### arjunprabhulal/agent-skills – infrastructure-as-code

Nützliche Muster zu Plan Review, State, Drift und irreversiblen Änderungen; feste Environment-/Human-Review-Dogmen werden nicht universell übernommen.

### arjunprabhulal/agent-skills – ci-pipelines

Nützliche Muster zu Reproduzierbarkeit, Caching, Secrets und verständlicher Evidence. Testreihenfolge und Quality Gates bleiben projektspezifisch beziehungsweise Testing/QA.

### arjunprabhulal/agent-skills – containerization

Nützliche Trennung von Build und Runtime, Multi-Stage Builds, Secret-Hygiene und Runtime Contract.

### arjunprabhulal/agent-skills – deployment-strategies

Nützliche Trennung von Deploy und Release sowie Fokus auf Rollback, Promotion und Abort. Konkrete Schwellen und Strategien werden nicht universell festgeschrieben.

## Bewusst nicht übernommen

Nicht als universelle Wahrheit übernommen werden etwa:

- jedes Projekt müsse Terraform verwenden;
- jedes stateful Apply brauche immer manuellen Review;
- Umgebungen dürften sich nur in Values unterscheiden;
- jede App müsse containerisiert sein;
- jeder Release brauche Canary oder Blue-Green;
- GitOps sei immer besser als Push-Deployment;
- jede Policy müsse blockierend enforced werden;
- ein grüner Plan oder eine grüne Pipeline autorisiere automatisch Apply/Deploy.

## Grundsatz

> Tools liefern Mechanismen. Der zentrale Bereich übernimmt nur belastbare Arbeitsprinzipien und klare Gates.