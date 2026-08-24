# Workflow – Produktionsincident

## Ziel

Einen aktiven Produktions- oder Betriebsincident von bestätigter Wirkung bis zu frisch verifizierter Recovery kontrolliert bearbeiten.

## Ablauf

```text
Signal / Report
→ tatsächlichen Impact bestätigen
→ incident-response
→ passende Diagnose-/Fachskills
→ Mitigation Proposal
→ bei realer Aktion Human-/Execution-Gate
→ autorisierte technische Aktion
→ Fresh Health-/Business-Evidence
→ Incident Closure / Handoff
→ Postmortem-Kriterium prüfen
```

## 1. Bestätigen und scopen

Nicht jeden Alert automatisch zum Incident erklären.

Erfassen:

- betroffene Nutzer/Consumer/Flows;
- Zeitpunkt / Dauer;
- aktuelle Evidence;
- tatsächliche oder drohende Wirkung;
- Ownership.

## 2. Incident Response

`incident-response` koordiniert:

- Incident State;
- Rollen/Funktionen;
- bestätigte Fakten vs. Hypothesen;
- Mitigationpriorität;
- Kommunikation;
- Handoffs.

## 3. Fachdiagnose

Je nach Symptom passende Skills einbinden, zum Beispiel:

- `diagnose`;
- `query-performance` / `database-operations`;
- `infrastructure-change-review`;
- `contract-change-review`;
- vorhandene Runbooks.

Incident Response ersetzt diese Fachanalyse nicht.

## 4. Mitigation und Gate

```text
Mitigation Option
→ Wirkung / Risiko / Reversibilität
→ benötigte Rechte
→ lokales Gate
→ technische Ausführung durch zuständige Domäne/Operator
```

Restart, Rollback, Restore, Failover, Traffic Switch, Scaling, Config- oder Datenänderung sind keine implizit autorisierten Incident-Schritte.

## 5. Recovery

Fresh Evidence aus relevanten Nutzer-/SLI-/Health-/Business-Signalen erzeugen.

Ein erfolgreicher Befehl ist keine Recovery-Evidence.

## 6. Abschluss

Dokumentieren:

- finalen Impact;
- Mitigation/Recovery;
- offene Risiken;
- Handoff, falls nötig;
- ob ein Postmortem nach lokaler Policy erforderlich ist.

## Security-Handoff

Bei Kompromittierung, Credential Leakage, Forensik oder regulatorischer Security-Kommunikation den Security-Prozess einschalten.

## Leitgedanke

> Im Incident wird koordiniert, stabilisiert und verifiziert. Dringlichkeit ersetzt keine fachliche Ownership und keine Autorisierung.