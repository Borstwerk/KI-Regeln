# Workflow – Build, Deploy und Promotion

## Ziel

Source kontrolliert in ein identifizierbares Artefakt überführen und dieses mit passender Evidence und Deploymentstrategie ausliefern.

## Ablauf

```text
Source Commit
→ ci-pipeline-design
→ Build
→ optional container-build
→ Testing-/Security-Evidence
→ identifizierbares Artifact
→ Promotion
→ deployment-strategy
→ Deploy Gate
→ Deployment
→ Fresh Health-/Business-Evidence
→ Promote / Pause / Abort
→ Release
```

## Build

- Inputs/Toolchain kontrollieren;
- Artifact Identity erfassen;
- Provenance/Evidence soweit projektspezifisch benötigt;
- kein Rebuild pro Environment, wenn Promotion desselben Artefakts möglich und gewünscht ist.

## Testing und Security

Teststrategie bleibt `Testing-und-QA/`. Supply-Chain-, Credential- und Security-Policies bleiben `Sicherheit/`.

## Deployment

Vor realer Außenwirkung:

- Zielumgebung;
- Artifact Identity;
- Compatibility;
- Rollback;
- Promotion/Abort-Kriterien;
- lokales Gate.

## GitOps-Variante

```text
Desired-State-Änderung
→ gitops-design
→ Repo-/Merge-Gate
→ Controller-Reconciliation
→ Sync-/Health-Evidence
```

Bei Auto-Reconciliation kann bereits Merge/Commit die wirksame Änderung autorisieren.

## Leitgedanke

> Dasselbe Artefakt soll auf seinem Weg zur Produktion mehr Evidence sammeln – nicht bei jeder Stufe seine Identität wechseln.