# Kubernetes Workloads und Rollouts

## Einordnung

Kubernetes ist eine wichtige Referenzplattform, aber kein universeller Infrastrukturstandard.

Dieser Text sammelt allgemeine Punkte, die bei Kubernetes-basierten Deployments häufig contractrelevant sind.

## Workload-Vertrag

Prüfen:

- gewünschte Replikate/Controller;
- Update Strategy;
- Readiness und Liveness;
- Graceful Termination;
- Ressourcenrequests/-limits;
- Config-/Secret-Bezug;
- Service-/Ingress-Abhängigkeiten;
- Storage/Persistence;
- Security Context als Übergabe an Security Policy.

## Rollout

Deploymentcontroller können Rolling Updates, Status und Rollback unterstützen. Das ersetzt nicht die Prüfung, ob Daten, Contracts oder Nebenwirkungen rückwärtskompatibel sind.

## Readiness ≠ Liveness

Readiness entscheidet, ob Traffic angenommen werden soll. Liveness entscheidet, ob ein Prozess als nicht mehr funktionsfähig gilt und neugestartet werden soll. Beide nicht gedankenlos mit denselben externen Dependencychecks koppeln.

## Rendered State

Bei Helm/Kustomize/Operatoren möglichst den effektiv gerenderten Zustand prüfen, nicht nur Base-Dateien.

## CRDs

Bei Drittanbieter-CRDs Feldnamen und Version gegen tatsächliche Schema-/Produktdokumentation prüfen. YAML-Struktur nicht aus Erinnerungen erfinden.

## Leitgedanke

> Kubernetes automatisiert Rollouts – es beweist nicht, dass der ausgerollte Zustand fachlich oder betrieblich sicher ist.