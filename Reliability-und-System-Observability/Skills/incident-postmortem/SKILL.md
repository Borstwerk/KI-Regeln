---
name: incident-postmortem
description: Erstellt oder prüft ein evidenzbasiertes Postmortem nach einem stabilisierten Incident mit Timeline, Impact, Detection, Response, Recovery, beitragenden Faktoren und verifizierbaren Follow-ups. Verwenden nach relevanten Betriebsstörungen. Nicht zur Führung eines noch aktiven Incidents oder zur erzwungenen Einzelursache verwenden.
---

# Incident Postmortem

## Ziel

Aus einem abgeschlossenen oder stabilisierten Incident nachvollziehbares Operational Learning ableiten, ohne Schuldvereinfachung oder erfundene Kausalität.

## Eingaben

- Incident State / Timeline;
- Alerts, Logs, Metrics, Traces und Events;
- Change-/Deploy-Historie;
- Nutzer-/Consumerimpact;
- Mitigation-/Recovery-Evidence;
- lokale Postmortem-Trigger und Ownership.

## Arbeitsweise

1. Prüfen, dass der aktive Incident ausreichend stabilisiert ist.
2. Quellen und Evidence sammeln; sensible Daten begrenzen.
3. Timeline aus bestätigten Ereignissen rekonstruieren und Unsicherheiten markieren.
4. Impact und Dauer aus geeigneter Evidence beschreiben.
5. Detection, Response und Recovery getrennt analysieren.
6. beitragende Faktoren und Wechselwirkungen identifizieren.
7. festhalten, was gut funktioniert und was die Bearbeitung erschwert hat.
8. Observability-, Alerting-, Runbook-, Ownership-, Testing-, Reliability- und Architektur-Gaps ableiten.
9. Follow-ups mit gewünschter Wirkung, Owner, Fachdomäne und späterer Completion-Evidence formulieren.
10. offene Fragen ausdrücklich offen lassen, wenn Evidence fehlt.

## Kausalität

Zeitliche Nähe ist keine automatische Ursache.

Nicht erzwingen:

- genau eine Root Cause;
- genau fünf Whys;
- eine Person als Endpunkt der Erklärung;
- perfekte Rekonstruktion trotz fehlender Daten.

## Follow-ups

Gute Follow-ups beschreiben nicht nur Aktivität, sondern gewünschte Risikoreduktion.

```text
Gap / Risiko
→ Maßnahme
→ Owner
→ fachlicher Zielbereich
→ Verification Evidence
```

## Stop-/Übergaberegeln

- Incident noch aktiv → `incident-response`;
- tiefe technische Ursache unklar → `diagnose` / Fachdomäne;
- Security-Kompromittierung → Security-Prozess;
- Runbookänderung → `runbook`;
- systemisches Failure-Experiment → `resilience-experiment`.

## Nicht tun

- Schuldzuweisung als Ursachenanalyse verkaufen;
- Hypothesen als Fakten formulieren;
- aus einem fehlenden Log schließen, dass ein Ereignis nicht passiert ist;
- beliebige Action Items erzeugen, nur damit die Liste lang ist;
- Ticketabschluss mit bewiesener Risikoreduktion gleichsetzen;
- sensible Incidentdaten ungeprüft in dauerhafte Dokumentation kopieren.

## Ausgabe

```text
Summary
Impact
Timeline
Detection
Response / Mitigation
Recovery
Contributing Factors
What Worked
What Made It Harder
Observability / Alerting Gaps
Process / Runbook / Ownership Gaps
Reliability / Testing / Architecture Gaps
Open Questions
Follow-ups [owner, domain, desired effect, verification]
```

## Related

- `incident-response`
- `diagnose`
- `reliability-review`
- `system-observability-design`
- `alert-design`
- `runbook`

## Leitgedanke

> Das Postmortem verbessert System und Betriebsprozess, indem es belegte Zusammenhänge und Lücken sichtbar macht – nicht indem es im Nachhinein eine einfache Geschichte erfindet.