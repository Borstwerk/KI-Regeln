---
name: incident-response
description: Strukturiert einen aktiven Produktions- oder Betriebsincident mit Impact, Scope, Rollen, Incident State, Evidence, Mitigation, Kommunikation, Handoff und Fresh Recovery Verification. Verwenden bei Outage, Degradation oder bestätigtem Incident. Nicht als generische Root-Cause-Analyse oder automatische Produktionsfreigabe verwenden.
---

# Incident Response

## Ziel

Reale Betriebswirkung kontrolliert begrenzen und einen verifizierten Servicezustand wiederherstellen, ohne Koordination, Diagnose und technische Autorisierung zu vermischen.

## Eingaben

- Alert / Nutzerbericht / Incidentmeldung;
- verfügbare Runtime-Evidence;
- betroffene Services/Flows;
- lokale Severity-/On-Call-/Escalation-Policy;
- vorhandene Runbooks;
- Produktionsrechte und Gates.

## Arbeitsweise

1. Incident beziehungsweise relevante Wirkung bestätigen oder Unsicherheit sichtbar machen.
2. Impact, Scope und Beginn so gut wie möglich bestimmen.
3. Ownership und benötigte Rollen/Funktionen klären.
4. gemeinsamen Incident State aufbauen oder aktualisieren.
5. bestätigte Fakten von Hypothesen trennen.
6. Stabilisierung/Mitigation vor vollständiger RCA priorisieren, wenn Nutzerwirkung läuft.
7. technische Diagnose gezielt an `diagnose`, DB-, Infra-, Interface- oder andere Fachskills übergeben.
8. Mitigation-Optionen mit Wirkung, Risiko und Reversibilität benennen.
9. reale Restart-/Rollback-/Failover-/Restore-/Traffic-/Config-/Data-Aktion nur bei gültiger lokaler Autorisierung ausführen lassen.
10. Recovery mit frischer Nutzer-/SLI-/Health-/Business-Evidence prüfen.
11. Kommunikation und Handoff aktualisieren.
12. Abschluss und Postmortem-Kriterium dokumentieren.

## Incident State

Mindestens:

```text
Impact / Scope
Confirmed Facts
Open Hypotheses
Current Health
Actions + Owners
Decisions / Gates
Mitigation Status
Recovery Evidence
Next Step
Communication Status
```

## Stop-/Übergaberegeln

- Security-Kompromittierung/Forensik → Security-Prozess;
- technische Root Cause → `diagnose` / Fachdomäne;
- fehlende Observability → als Gap markieren, nicht erfinden;
- fehlende Produktionsautorisierung → Mitigation Proposal liefern und blockieren;
- Incident stabil → gegebenenfalls `incident-postmortem`.

## Nicht tun

- SEV-Klassen oder Reaktionszeiten erfinden;
- jeden Alert automatisch zum Incident erklären;
- während aktiver Nutzerwirkung unnötig vollständige RCA vor Mitigation erzwingen;
- Restart/Failover/Rollback als pauschal niedriges Risiko einstufen;
- Incident-Dringlichkeit als Produktionsberechtigung behandeln;
- Service als recovered melden, nur weil ein Befehl erfolgreich war;
- Root Cause aus zeitlicher Korrelation behaupten.

## Ausgabe

```text
Incident Status
Impact / Scope
Confirmed Evidence
Hypotheses
Roles / Ownership
Mitigation Options / Decision
Authorization Status
Actions / Results
Fresh Recovery Evidence
Communication / Handoff
Open Risks
Postmortem Trigger
```

## Related

- `diagnose`
- `system-observability-design`
- `alert-design`
- `incident-postmortem`
- `database-operations`
- `infrastructure-change-review`
- `deployment-strategy`
- `tool-permission-review`

## Leitgedanke

> Erst Wirkung begrenzen und Recovery beweisen. Erklärung und Lernen folgen mit derselben Evidenzdisziplin.