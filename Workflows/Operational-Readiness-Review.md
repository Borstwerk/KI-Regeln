# Workflow – Operational Readiness Review

## Ziel

Vor Launch, größerem Release oder Betriebsübergang zusammengesetzte Evidence prüfen, ohne Operational Readiness in einen Mega-Skill zu verwandeln.

## Ablauf

```text
Service / Release Context
→ lokale Requirements / Critical Journeys
→ Reliability Objectives
→ Observability / Alerts
→ Capacity / Dependencies
→ Recovery / Runbooks
→ Testing / Resilience Evidence
→ Infra / Deployment / Rollback Evidence
→ Security / Permissions
→ Ownership / On-Call
→ reliability-review
→ Findings / Missing Evidence
→ lokales Go / No-Go
```

## 1. Scope

Klären:

- Service / Release / Betriebsübergang;
- kritische Nutzer-/Consumerflows;
- lokale Requirements;
- Owner;
- Zielumgebung und reale Außenwirkung.

## 2. Reliability Objectives

Je nach Scope `slo-design` beziehungsweise vorhandene lokale Ziele prüfen.

Keine Zielwerte nur für die Checkliste erfinden.

## 3. Observability und Alerts

Prüfen:

- relevante Health-/Diagnosefragen beantwortbar;
- Blind Spots bekannt;
- Telemetrie verifiziert;
- actionable Alerts vorhanden, soweit nötig;
- Runbook-/Routing-Einstieg geklärt.

## 4. Capacity und Dependencies

Bei relevantem Risiko `capacity-planning` einbinden.

Prüfen:

- Peaks / Growth;
- Limits / Quotas;
- Failure Domains;
- Dependency Capacity;
- Scaling/Provisioning Lead Time.

## 5. Recovery

Lokale RTO/RPO-/Recovery-Ziele und aktuelle Evidence prüfen.

Backupexistenz allein genügt nicht.

Runbookqualität kann über `runbook` beziehungsweise `docs-review` geprüft werden.

## 6. Testing und Resilience

Vorhandene Evidence aus `Testing-und-QA/` einbeziehen.

Bei systemischer Unsicherheit optional `resilience-experiment` planen beziehungsweise vorhandene Game-Day-Evidence prüfen.

## 7. Deployment / Rollback

Aus `Infrastruktur-und-DevOps/` einbeziehen:

- Artifact-/Versionidentität;
- Deploymentstrategie;
- Promotion/Pause/Abort;
- Rollbackgrenzen;
- tatsächliche Zielumgebung;
- erforderliche Gates.

## 8. Security / Permissions

Prüfen:

- Production Identities und Rechte;
- Secrets / Trust Boundaries;
- externe Aktionen;
- Human Gates;
- Security Findings.

## 9. Ownership

Mindestens:

- wer betreibt den Scope;
- wer reagiert auf relevante Incidents;
- wo Runbooks/Evidence liegen;
- welche Eskalation lokal gilt;
- welche offenen manuellen Risiken/Toil existieren.

## 10. Unabhängiger Review

`reliability-review` bewertet die zusammengesetzte Evidence.

Mögliche Verdicts:

- `READY_FOR_LOCAL_GATE`
- `READY_WITH_FINDINGS`
- `BLOCKED`
- `UNVERIFIED`

Keines dieser Verdicts autorisiert automatisch Deploy oder Release.

## Lokales Gate

Das tatsächliche Go/No-Go bleibt Projekt-/Produktentscheidung.

Ein kleiner risikoarmer Scope darf den Workflow begründet verkürzen; ein kritischer Scope kann zusätzliche Compliance-, Security- oder Fachgates benötigen.

## Leitgedanke

> Operational Readiness entsteht aus zusammenpassender Evidence und Ownership – nicht aus einem einzelnen grünen Test, Dashboard oder Formular.