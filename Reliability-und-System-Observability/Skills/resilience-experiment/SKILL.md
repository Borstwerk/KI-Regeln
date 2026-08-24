---
name: resilience-experiment
description: Plant oder prüft kontrollierte systemische Resilience-Experimente mit Steady State, Hypothese, realistischer Störung, Environment, Blast Radius, Observation, Abort, Recovery, Gates und Evidence. Verwenden für Chaos Engineering und Game Days. Nicht als gewöhnlichen Failure-Test oder ungefragte produktive Fault Injection verwenden.
---

# Resilience Experiment

## Ziel

Eine konkrete Resilience-Hypothese unter kontrollierter Störung sicher und nachvollziehbar prüfen.

## Betriebsmodi

```text
PLAN / REVIEW
→ Standardmodus

EXECUTE
→ nur mit expliziter Autorisierung,
   geeigneter Capability,
   freigegebenem Scope,
   Blast Radius,
   Abort und Recovery
```

## Eingaben

- zu prüfendes Reliability-/Failure-Risiko;
- kritischer Flow / Steady-State-Evidence;
- System-/Failure-Domain-Kontext;
- gewünschte Störung;
- Zielumgebung;
- verfügbare Observability;
- Recoverymechanik;
- lokale Produktions-/Security-/Change-Gates.

## Arbeitsweise

1. relevanten Steady State messbar definieren.
2. falsifizierbare Hypothese formulieren.
3. Failure Variable wählen, die zur Hypothese passt.
4. geeignetste Umgebung mit ausreichend Aussagekraft und vertretbarem Risiko bestimmen.
5. Blast Radius explizit begrenzen.
6. benötigte Telemetrie/Observation verifizieren oder Experiment als unzureichend beobachtbar markieren.
7. Abort Criteria vor der Störung definieren.
8. Recovery-/Cleanup-Pfad und dessen Owner/Rechte festlegen.
9. Permissions und Human/Execution Gate prüfen.
10. nur bei expliziter Ausführungsautorisierung Störung injizieren.
11. während des Experiments Abweichungen und unerwartete Wirkung erfassen.
12. nach Ende Recovery mit Fresh Evidence bestätigen.
13. Hypothese als `supported`, `disproved` oder `inconclusive` bewerten.
14. Follow-ups nach Fachdomäne weitergeben.

## Grenze zu Failure Testing

`failure-testing` ist passend für gezielte, reproduzierbare Failure Modes innerhalb eines kontrollierten Testscopes.

`resilience-experiment` ist passend, wenn systemische Wechselwirkung, realistischer Blast Radius, Steady State oder emergentes Verhalten untersucht werden.

## Ausführungsgate

Eine produktive oder anderweitig real wirksame Fault Injection benötigt:

- eindeutige Zielumgebung;
- freigegebenen Failure Scope;
- explizite Autorisierung;
- geeignete Tool-/Fault-Injection-Capability;
- Abort/Recovery;
- erreichbare Owner/Responder nach lokaler Policy.

Toolverfügbarkeit allein genügt nicht.

## Nicht tun

- Chaos als „brich irgendetwas und schau was passiert“ behandeln;
- Produktion als notwendiges Reifeziel ansehen;
- Blast Radius erst während des Experiments herausfinden;
- Experiment ohne glaubwürdige Observation starten;
- Security-/Credential-Störungen ohne passende Securityfreigabe ableiten;
- Unit-/Integration-Fault-Test künstlich als Chaos Engineering labeln;
- automatisierte kontinuierliche Experimente ohne explizite lokale Governance einführen;
- Recovery allein aus dem Ende der Fault Injection ableiten.

## Ausgabe

```text
Hypothesis
Steady State
Fault / Variable
Environment
Blast Radius
Observation / Telemetry
Abort Criteria
Recovery / Cleanup
Permissions / Gate
Execution Status
Evidence
Result: supported / disproved / inconclusive
Unexpected Findings
Follow-ups
```

## Related

- `failure-testing`
- `system-observability-design`
- `slo-design`
- `capacity-planning`
- `incident-response`
- `reliability-review`
- `tool-permission-review`

## Leitgedanke

> Das Experiment soll eine wichtige Resilience-Annahme kontrolliert angreifen. Sicherheit, Beobachtbarkeit und Recovery gehören vor die Störung.