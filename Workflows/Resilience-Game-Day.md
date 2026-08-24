# Workflow – Resilience Game Day

## Ziel

Eine systemische Failure-/Resilience-Hypothese kontrolliert planen, freigeben, gegebenenfalls ausführen und gegen Fresh Evidence bewerten.

## Ablauf

```text
Failure Risk / offene Annahme
→ resilience-experiment [PLAN]
→ Steady State + Hypothese
→ Fault / Environment / Blast Radius
→ Observation
→ Abort + Recovery
→ Permission / Safety Review
→ lokales Execution Gate
→ Experiment nur wenn autorisiert
→ Beobachtung
→ Abort / Cleanup / Recovery
→ Fresh Verification
→ Hypothese bewerten
→ Follow-ups
```

## 1. Scope und Hypothese

Definieren:

- kritischen Flow;
- Steady State;
- realistische Störung;
- erwartetes Systemverhalten;
- messbare Abweichung.

## 2. Test-vs.-Experiment-Grenze

Wenn ein gezielter reproduzierbarer Failure Mode innerhalb eines Testscopes genügt, `failure-testing` verwenden.

Game Day nur, wenn systemische Wechselwirkungen, Failure Domains, realistischer Blast Radius oder emergentes Verhalten relevant sind.

## 3. Safety Design

Vor Gate mindestens:

- Zielumgebung;
- betroffener Scope;
- Blast Radius;
- Daten-/Statewirkung;
- Observation/Telemetry;
- Abort Criteria;
- Recovery/Cleanup;
- zuständige Owner;
- benötigte Rechte.

## 4. Gate

`resilience-experiment` im PLAN-Modus autorisiert keine Fault Injection.

```text
Plan reviewed
≠
experiment execution authorized
```

Bei produktiver Wirkung zusätzlich lokale Change-/Security-/On-Call-Regeln anwenden.

## 5. Ausführung

Nur mit geeigneter Capability und expliziter Autorisierung.

Währenddessen:

- Steady State beobachten;
- Blast Radius kontrollieren;
- unerwartete Effekte erfassen;
- Abortbedingungen respektieren;
- keine spontane Scope-Ausweitung ohne neues Gate.

## 6. Recovery

Nach Fault Removal Fresh Evidence erzeugen.

Prüfen:

- kritischer Flow;
- SLO/Health;
- Dependencies;
- Backlogs;
- Daten-/Statekonsistenz;
- verbleibende Nebenwirkungen.

## 7. Ergebnis

```text
supported
→ Beobachtung war mit der Hypothese vereinbar

disproved
→ relevante Abweichung widerlegt die Hypothese

inconclusive
→ Evidence reicht nicht für belastbare Bewertung
```

Keinen PASS nur daraus ableiten, dass kein sichtbarer Incident entstand.

## Leitgedanke

> Der Game Day ist ein kontrolliertes Experiment mit Rückweg, kein Überraschungsangriff auf das eigene System.