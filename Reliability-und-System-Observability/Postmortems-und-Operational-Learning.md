# Postmortems und Operational Learning

## Zweck

Postmortems machen aus einem relevanten Betriebsincident nachvollziehbares Lernen, ohne die Analyse auf Schuldzuweisung oder eine künstlich vereinfachte Einzelursache zu reduzieren.

## Zeitpunkt

Ein Postmortem gehört nach die aktive Stabilisierung.

```text
aktive Nutzerwirkung
→ Incident Response / Recovery
→ belastbarer Abschlusszustand
→ Postmortem / Learning
```

Ein Postmortem-Skill soll nicht während eines noch laufenden Incidents den Response-Prozess ersetzen.

## Wann ein Postmortem sinnvoll ist

Konkrete Trigger bleiben lokal, zum Beispiel:

- relevante Nutzer-/Businesswirkung;
- SLO-/Error-Budget-Ereignis;
- Datenintegritätsrisiko;
- ungewöhnlich schwierige oder lange Recovery;
- wiederkehrender Failure Mode;
- Near Miss mit hohem potenziellem Impact;
- erhebliche Detection-/Alerting-Lücke;
- Prozess- oder Ownership-Versagen;
- manuelle Notfallaktion mit hohem Risiko.

Keine universellen Severity- oder Zeitgrenzen zentral festlegen.

## Evidence zuerst

Ein gutes Postmortem trennt:

- bestätigte Fakten;
- Zeitpunkte;
- Hypothesen;
- Unsicherheiten;
- fehlende Evidence;
- spätere Rekonstruktion.

Quellen können sein:

- Incident State / Timeline;
- Alerts;
- Logs, Metrics, Traces, Events;
- Deploy-/Change-Historie;
- Tickets / Kommunikation;
- Runbook-/Toolereignisse;
- Datenbank-/Infra-/Provider-Evidence;
- Nutzer-/Consumerberichte.

Sensible Inhalte vor Weitergabe oder dauerhafter Speicherung prüfen.

## Mindeststruktur

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
Runbook / Process / Ownership Gaps
Reliability / Architecture / Testing Gaps
Open Questions
Follow-ups [owner, priority/rationale, evidence of completion]
```

## Contributing Factors statt Zwang zur Einzelursache

Komplexe Incidents entstehen häufig aus mehreren Bedingungen.

Mögliche Kategorien:

- Designannahme;
- Dependency;
- Capacity/Saturation;
- Change/Rollout;
- Konfiguration;
- Daten-/Contract-Verhalten;
- fehlende Isolation;
- Observability-Lücke;
- Alerting-Lücke;
- Runbook-/Prozesslücke;
- Ownership / Handoff;
- menschliche Entscheidung unter unvollständiger Information;
- äußeres Ereignis.

Methoden wie „5 Whys“ können lokal hilfreich sein, sind aber keine Pflicht und dürfen keine falsche lineare Kausalität erzwingen.

## Lernen ohne Schuldvereinfachung

Ziel ist, Systembedingungen und Entscheidungsumgebung zu verstehen.

Nicht hilfreich:

- „Person X hat Fehler gemacht“ als vollständige Erklärung;
- individuelle Schuld als Ersatz für technische oder organisatorische Ursachen;
- nachträgliche Gewissheit vortäuschen;
- eine Handlung im Kontext damaliger Informationen mit späterem Wissen bewerten, ohne diesen Unterschied sichtbar zu machen.

Das bedeutet nicht, Verantwortung aufzulösen. Ownership und Entscheidungen sollen nachvollziehbar bleiben.

## Detection, Response und Recovery getrennt lernen

Mindestens drei Fragen:

```text
Detection:
Haben wir früh und richtig erkannt, was relevant war?

Response:
Konnten wir Impact, Rollen, Evidence und Mitigation effizient koordinieren?

Recovery:
Konnten wir sicher wiederherstellen und den Erfolg belastbar verifizieren?
```

Dadurch wird verhindert, dass jedes Follow-up nur „Bug fixen“ lautet.

## Follow-ups

Ein Follow-up sollte enthalten:

- Problem / Risiko;
- gewünschte Wirkung;
- Owner;
- Priorität oder rationale Einordnung;
- geeignete Fachdomäne;
- Completion-/Verification-Evidence.

Mögliche Übergaben:

- Testing / Failure Testing;
- Reliability / SLO / Alert / Capacity;
- Observability;
- Infrastruktur / Deployment;
- Datenbank;
- Schnittstellen;
- Software Architecture;
- Security;
- Runbook / Dokumentation;
- Requirements.

Keine pauschale Regel „jeder Incident braucht N Action Items“.

## Abschluss von Follow-ups

Ticket geschlossen ist nicht automatisch Wirkung bewiesen.

Bei relevanten Maßnahmen später prüfen:

- wurde die technische Änderung tatsächlich umgesetzt?
- wurde das neue Signal/Alert getestet?
- wurde Recovery geprobt?
- wurde der Failure Mode reproduzierbar getestet?
- wurde das SLO/Runbook/Ownership aktualisiert?
- ist das ursprüngliche Risiko sichtbar reduziert?

## Leitgedanke

> Ein Postmortem soll erklären, warum das System und sein Betriebsprozess den Incident möglich oder schwer beherrschbar gemacht haben – und wie wir das nachweisbar verbessern.