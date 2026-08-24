# Chaos Engineering und Game Days

## Zweck

Chaos Engineering und Game Days prüfen systemische Resilience-Hypothesen unter kontrollierten Störungen.

Sie sind keine Lizenz, beliebig Dinge kaputtzumachen.

## Kernmodell

```text
Steady State definieren
→ Hypothese formulieren
→ realistischen Failure / Variable wählen
→ Environment + Blast Radius bestimmen
→ Observation / Telemetry prüfen
→ Abort + Recovery festlegen
→ Berechtigungen / Gate
→ Experiment
→ Zustand frisch verifizieren
→ Hypothese bewerten
→ Follow-ups
```

## Steady State

Vor der Störung muss klar sein, welcher beobachtbare Zustand als normal beziehungsweise akzeptabel gilt.

Mögliche Bestandteile:

- SLI/SLO;
- Nutzer-/Consumerflow;
- Business-/Domain-Signal;
- Queue-/Freshness-/Lag-Zustand;
- Dependency-Health;
- Capacity-/Saturation-Signal.

Steady State ist nicht automatisch „alle Komponenten grün“.

## Hypothese

Eine belastbare Hypothese beschreibt:

- was gestört wird;
- welches relevante Systemverhalten trotzdem erwartet wird;
- woran Abweichung erkannt wird.

Beispiel:

> Wenn Dependency X für fünf Minuten nicht erreichbar ist, bleibt kritischer Flow Y verfügbar und Requests auf Feature Z degradieren kontrolliert, ohne Queue Q unbeschränkt wachsen zu lassen.

Konkrete Zeiten und Grenzen bleiben lokal.

## Realistische Störungen

Mögliche Variablen:

- Dependency unavailable / slow;
- Netzwerkverlust / Latenz;
- Resource Saturation;
- Prozess-/Node-Ausfall;
- Zone-/Failure-Domain-Ausfall;
- Queue-/Backlog-Störung;
- Rate Limit / Quota;
- Control-Plane-Ausfall;
- Clock-/Time-Anomalie;
- Storage-/DB-Failure;
- Credential-/Certificate-Ausfall, soweit sicher und autorisiert;
- Trafficspike.

Die Störung muss zur Hypothese passen.

## Grenze zu Failure Testing

`../Testing-und-QA/Skills/failure-testing/SKILL.md` behandelt reproduzierbare Failure Modes innerhalb eines Testscopes.

Chaos/Resilience Experiment ist passend, wenn:

- Systemverhalten über mehrere Komponenten relevant ist;
- eine Steady-State-Hypothese geprüft wird;
- realistischer Blast Radius eine Rolle spielt;
- Wechselwirkungen, Recovery oder emergentes Verhalten untersucht werden.

Ein Unit-/Integrationstest wird nicht dadurch zu Chaos Engineering, dass ein Fehler injiziert wird.

## Environment

Experimente können je nach Reife und Ziel stattfinden in:

- lokaler/synthetischer Umgebung;
- Test/Staging;
- isolierter produktionsnaher Umgebung;
- Produktion.

Produktion ist kein universelles Ziel und kein Reifeabzeichen.

Die Wahl folgt der Frage:

> Welche Umgebung liefert die benötigte Aussagekraft bei vertretbarem Risiko?

## Blast Radius

Vor Ausführung explizit begrenzen:

- betroffene Nutzer/Consumer;
- Region/Zone/Cluster;
- Tenant;
- Workload;
- Trafficanteil;
- Dauer;
- Daten-/Statewirkung;
- Downstream-Dependencies.

Wenn der Blast Radius nicht verstanden oder begrenzbar ist, Experiment blockieren oder in sicherere Umgebung verlagern.

## Abort Criteria

Vorher definieren, wann das Experiment sofort beendet wird.

Mögliche Gründe:

- unerwarteter Nutzer-/Businessimpact;
- Datenintegritätsrisiko;
- unkontrollierter Capacity-/Retry-/Backlog-Effekt;
- Verlust der benötigten Observability;
- Security-/Compliance-Risiko;
- Recovery-Pfad funktioniert nicht;
- Blast Radius überschreitet den freigegebenen Scope.

Keine universellen Schwellen festlegen.

## Recovery

Vor der Störung klären:

- wie die injizierte Variable entfernt wird;
- wie der Normalzustand wiederhergestellt wird;
- welche realen Nebenwirkungen bleiben können;
- welche Fresh Evidence Recovery bestätigt;
- wer Recovery ausführen darf.

## Authorization

Planung und Review sind nicht Ausführung.

```text
Experimentdesign
→ Safety / Permission Review
→ explizites lokales Gate
→ Ausführung nur mit Capability und Autorisierung
```

Toolverfügbarkeit ist keine Autorisierung.

Ein Agent darf ein produktives Experiment nicht aus allgemeinem „Chaos Engineering“-Auftrag ableiten, wenn Zielumgebung, Scope und Freigabe nicht eindeutig sind.

## Kontinuierliche Experimente

Automatisierung kann sinnvoll sein, wenn:

- Hypothese und Scope stabil sind;
- Blast Radius begrenzt ist;
- Abort/Recovery automatisiert und verifiziert sind;
- lokale Governance diese Automatisierung ausdrücklich freigegeben hat.

Keine zentrale Pflicht zu kontinuierlichem Chaos.

## Evidence

Nach dem Experiment dokumentieren:

```text
Hypothesis
Steady State
Fault / Variable
Environment
Blast Radius
Execution Status
Observed Evidence
Abort / Recovery
Result: supported / disproved / inconclusive
Unexpected Findings
Follow-ups
```

„Kein Incident entstanden“ beweist allein nicht, dass die Hypothese geprüft wurde.

## Leitgedanke

> Ein gutes Resilience-Experiment versucht eine konkrete Annahme sicher zu widerlegen – nicht möglichst spektakulär Störungen zu erzeugen.