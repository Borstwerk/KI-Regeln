---
name: architecture-review
description: Auditiert ein Softwaresystem oder Systemdesign unabhängig auf Drivers, Kontext, Grenzen, Ownership, Runtime-Flows, State, Quality-Trade-offs, Patterns, Technologie, Evolution, Evidence und Conformance. Verwenden für breite Architektur-, Systemdesign- oder Readiness-Reviews. Nicht als Implementierungs-, Code-Review- oder automatische Re-Architecture verwenden.
---

# Architecture Review

## Ziel

Systemische Architekturprobleme, unbelegte Annahmen und relevante Trade-offs unabhängig sichtbar machen, ohne Findings ungefragt zu implementieren oder eine Patternpräferenz als Qualitätsurteil auszugeben.

## Eingaben

- Scope und relevante Requirements/Drivers;
- Architecture Baseline oder aktuelle Repository-/Systemevidence;
- Architektur-/Design-/ADR-Dokumentation;
- Interfaces, Daten-/State-Ownership und kritische Flows;
- Quality-/Reliability-/Capacity-Evidence soweit relevant;
- Migrations-/Deployment-/Betriebsbedingungen.

## Prüfachsen

1. Scope / System Context / Actors;
2. Drivers / Constraints / Assumptions;
3. fachliche und technische Invarianten;
4. Verantwortungs-, Modul-/Service- und Dependency-Grenzen;
5. State-/Data-Ownership und Sources of Truth;
6. kritische Runtime- und Failure-Flows;
7. Quality-Szenarien und Trade-offs;
8. Pattern-/Style-Fit und unnötige Komplexität;
9. Technologieentscheidungen und Reversibilität;
10. Reliability-/Security-/Operability-Integration;
11. Evolution, Compatibility und Zwischenzustände;
12. ADRs / Views / Evidence Quality;
13. Architecture Conformance / Drift / Fitness Functions;
14. Missing, stale oder conflicting Evidence.

## Arbeitsweise

- lokale Sources of Truth und gültige Entscheidungen zuerst;
- aktuelle Implementierung, Soll-Architektur und Runtime-Evidence trennen;
- Findings mit Impact und Evidence-Status priorisieren;
- Patternnamen nicht als Qualitätsbeweis oder Defekt verwenden;
- tiefe Fachfragen an zuständige Skills übergeben;
- keine Re-Architecture oder produktive Änderung aus dem Review heraus ausführen.

## Evidence Status

- `CONFIRMED`
- `LIKELY`
- `UNVERIFIED`
- `CONFLICTING`

## Verdict

- `READY_FOR_LOCAL_GATE`
- `READY_WITH_FINDINGS`
- `BLOCKED`
- `UNVERIFIED`

Das Verdict autorisiert weder Implementierung, Merge, Deployment, Migration noch Release.

## Stop-/Übergaberegeln

- Klassen-/Methoden-/Codequalität → `code-review`;
- Fachmodell → `domain-modeling`;
- konkrete Schnittstellenverträge → Interface-Skills;
- DB-spezifisches Design/Query/Transaction → Datenbanken;
- Data-Pipeline-/Datasetsemantik → Data Engineering;
- SLO/Capacity/Incidents/Resilience → Reliability;
- konkrete Teststrategie → Testing und QA;
- Architekturentscheidung dokumentieren → `adr`.

## Nicht tun

- aus fehlenden Requirements eigene Qualitätsziele erfinden;
- Microservices, DDD, Hexagonal, Event-driven oder Cloud als Reifegradmaß verwenden;
- Repositorystruktur allein als vollständige Runtime-Architektur behandeln;
- Missing Runtime Evidence als PASS interpretieren, wenn sie für das Urteil erforderlich ist;
- Findings ungefragt implementieren;
- Toolzugriff als Autorisierung verstehen.

## Ausgabe

```text
Scope / Drivers / Evidence
Findings [priority, evidence status, impact]
Context / Boundary / Ownership Risks
Runtime / State / Failure Risks
Quality / Trade-off Risks
Pattern / Complexity Assessment
Technology / Reversibility Risks
Evolution / Migration Risks
Conformance / Drift / Fitness Functions
Missing / Conflicting Evidence
Required Handoffs
Verdict
```

## Related

- `architecture-baseline`
- `system-design`
- `architecture-decomposition`
- `architecture-tradeoff-analysis`
- `architecture-evolution`
- `architecture-conformance-review`
- `reliability-review`
- `infrastructure-review`
- `data-engineering-review`
- `interface-review`
- `database-review`
- `test-suite-review`

## Leitgedanke

> Ein gutes Architekturreview prüft Begründung, Struktur und tatsächliche Evidence – nicht die Nähe zu einem Lieblingspattern.