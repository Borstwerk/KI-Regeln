---
name: system-design
description: Entwirft oder entwickelt ein Softwaresystem aus bestätigten Requirements, Architecture Drivers, Invarianten, Workload-/Failure-Evidence, Systemkontext und expliziten Trade-offs. Verwenden für neue Systeme, größere strukturelle Änderungen oder schwer umkehrbare Plattform-/Topologieentscheidungen. Nicht als Patternkatalog-, Toolauswahl- oder Implementierungsskill verwenden.
---

# System Design

## Ziel

Die einfachste tragfähige Architektur entwerfen, die die bekannten Drivers und Invarianten erfüllt, und zusätzliche Verteilung oder Komplexität nur durch konkrete Evidence rechtfertigen.

## Voraussetzungen

- relevante Requirements/Constraints oder klar markierte Annahmen;
- Architecture Baseline bei bestehenden Systemen;
- fachliche Invarianten und Sources of Truth;
- bekannte kritische Flows und Failure Modes;
- Workload-/Capacity-/Kosten-Evidence soweit entscheidungsrelevant.

## Vorgehen

1. Scope, Drivers, Constraints und Annahmen explizit machen.
2. System Context und Verantwortung schließen.
3. Invarianten, authoritative State und kritische Flows festhalten.
4. entscheidungsrelevante Last-, Failure- oder Betriebsgrenzen berechnen beziehungsweise als Missing Evidence markieren.
5. die einfachste produktionsfähige Struktur als Baseline-Kandidat entwerfen.
6. weitere Kandidaten nur aufnehmen, wenn sie eine echte load-bearing Achse anders lösen.
7. Kandidaten anhand Quality-Szenarien, Failure Modes, Kosten, Operability und Migration vergleichen.
8. Empfehlung mit nachvollziehbarer Evidence Chain formulieren.
9. offene Sensitivity Points und Messungen benennen, die die Empfehlung ändern würden.
10. bei langfristiger Entscheidung an den vorhandenen `adr`-Skill übergeben.

## Evidence Chain

Eine wesentliche Empfehlung sollte auf mindestens einem dieser Gründe beruhen:

- bestätigter Requirement/Constraint;
- fachliche oder technische Invariante;
- gemessene/abgeleitete Last- oder Capacity-Grenze;
- benannter Failure Mode;
- Security-/Compliance-Grenze;
- belegte Ownership-/Lifecycle-Anforderung;
- belastbarer Migrations-/Betriebsconstraint.

## Nicht tun

- fehlende QPS-, SLO-, RTO/RPO-, Kosten- oder Teamwerte erfinden;
- automatisch drei Architekturvarianten produzieren;
- Microservices, Queue, Cache, Sharding, CQRS oder Event Sourcing als Standardbausteine verwenden;
- Patternnamen als Begründung einsetzen;
- Technologie vor Driver und Struktur auswählen;
- Architekturentscheidung als Implementierungs- oder Deploymentfreigabe behandeln.

## Ausgabe

```text
Scope / Drivers / Constraints / Assumptions
System Context
Invariants / State Ownership
Critical Runtime and Failure Flows
Decision-Relevant Envelope / Missing Evidence
Baseline Candidate
Additional Viable Candidates, if any
Trade-offs / New Failure Modes
Recommendation / Evidence Chain
Sensitivity Points
Migration / Handoffs
Decision Status
```

## Related

- `architecture-baseline`
- `architecture-decomposition`
- `architecture-tradeoff-analysis`
- `architecture-evolution`
- `architecture-review`
- `capacity-planning`
- `domain-modeling`
- `interface-design`
- `adr`

## Leitgedanke

> Architektur wird durch Invarianten, Grenzen und reale Kräfte entschieden – nicht durch Vibes oder Patternnamen.