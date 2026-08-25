# Software Architecture und System Design

Dieser Bereich beschreibt allgemeine, technologie- und providerneutrale Arbeitsweisen für die strukturelle Gestaltung, Bewertung und evolutionäre Veränderung von Softwaresystemen.

## Grundprinzip

> Architektur ist die begründete Verteilung von Verantwortung, Abhängigkeit, Zustand und Laufzeitverhalten unter konkreten Anforderungen und Constraints.

Architektur wird nicht aus Patternnamen abgeleitet. Ein Pattern, ein Framework oder ein verteilter Mechanismus muss sich durch einen konkreten Driver, eine Invariante, einen Failure Mode, eine messbare Grenze oder einen nachvollziehbaren Trade-off rechtfertigen.

## Scope

`Software-Architecture-und-System-Design/` behandelt insbesondere:

- Architecture Drivers, Constraints, Annahmen und offene Unsicherheiten;
- System Context, Akteure, externe Systeme und Verantwortungsgrenzen;
- Dekomposition in Module, Komponenten, Services und Plattformgrenzen;
- Dependency Direction, Ownership und Zustandsverantwortung;
- kritische Runtime-Flows, State, Coordination und Failure Paths;
- Architekturstyles und Patterns als Optionen mit Voraussetzungen und Trade-offs;
- Quality Attributes über konkrete Szenarien statt abstrakter Schlagwörter;
- Vergleich strukturell unterschiedlicher Kandidaten;
- Technologieauswahl als Folge von Anforderungen statt Ausgangspunkt;
- evolutionäre Architekturänderungen, Migrationen und Zwischenzustände;
- Architektur-Views, Diagramme, ADR-Anbindung und nachvollziehbare Evidence;
- Architecture Conformance, Fitness Functions und Drift;
- unabhängige Architektur- und Readiness-Reviews.

## Nicht der Scope

- **Requirements und Spezifikations-Engineering:** definiert in `../Requirements-und-Spezifikations-Engineering/` Stakeholderbedarfe, Scope, funktionale und qualitative Requirements, verbindliche Zielwerte, Acceptance-/Verification-Intent und Requirements-Lifecycle. Architecture konsumiert diese bestätigte Sollgrundlage und darf fehlende Zielwerte nicht erfinden.
- **Domain Modeling:** `../Programmieren/Skills/domain-modeling/` klärt Fachbegriffe, Fachobjekte und Invarianten. Architecture nutzt diese Wahrheit für Systemgrenzen, ersetzt aber nicht die Fachmodellierung.
- **Schnittstellen und Verträge:** `../Schnittstellen-und-Vertraege/` definiert konkrete Provider-/Consumer-Verträge, Compatibility, Delivery-, Retry- und Idempotenzsemantik. Architecture entscheidet, warum eine Grenze existiert und welche Interaktionsform strukturell passt.
- **Datenbanken:** besitzt internes Datenbankdesign, Query-Performance, Transaktionen, Migration und DB-Betrieb.
- **Data Engineering:** besitzt Source-to-Consumer-Datenflüsse, Data Contracts, Lineage, Replay und Data Quality.
- **Reliability und System-Observability:** operationalisiert bestätigte Reliability-Ziele in SLI/SLO-, Health-, Incident-, Capacity- und Resilience-Evidence. Architecture entscheidet, welche Struktur diese Eigenschaften ermöglichen soll.
- **Infrastruktur und DevOps:** baut und betreibt die gewählte Runtime-, Deployment- und Infrastrukturmechanik.
- **Testing und QA:** besitzt allgemeine Teststrategie und Testmethodik. Architecture kann prüfbare Architekturregeln und Fitness-Function-Ziele formulieren.
- **Sicherheit:** besitzt Threat Modeling, Security Controls und Security Testing im Detail.
- **Dokumentationserstellung:** besitzt den allgemeinen `adr`-Skill und die Dokumentationsmethodik.
- **Programmieren / Code Review:** besitzt Implementierungsdetails, Klassen-/Methodendesign und konkrete Codeänderungen.

## Zentrale Modelle

```text
bestätigtes Requirement / Driver / Constraint
→ Invarianten und Quality-Szenarien
→ System Context und aktuelle Architektur
→ einfachste tragfähige Struktur
→ echte Alternativen nur bei relevantem Trade-off
→ Entscheidung / Evolution
→ Conformance-Evidence
```

```text
Pattern
≠
Architekturentscheidung
```

```text
Diagramm
≠
Architektur
```

```text
Dokumentierte Soll-Architektur
≠
Tatsächliche Architektur
```

## Keine Architekturreligion

Nicht zentral festschreiben:

- Microservices seien moderner oder grundsätzlich besser als ein Monolith;
- ein Monolith sei automatisch ein Big Ball of Mud;
- DDD, Clean Architecture oder Hexagonal Architecture seien Pflicht;
- Event-driven sei automatisch entkoppelt;
- CQRS oder Event Sourcing verbesserten jedes komplexe System;
- jede Anwendung brauche mehrere Architekturvarianten;
- jede Architekturentscheidung brauche ein ADR;
- jedes System brauche alle C4-Ebenen oder ein vollständiges arc42-Dokument;
- Cloud, Kubernetes, Kafka oder ein bestimmter Datenbanktyp seien Architekturziele.

## Risikomodell

```text
READ / BASELINE
→ bestehende Architektur, Abhängigkeiten, Drivers und Evidence erfassen

DESIGN / COMPARE
→ Kandidaten, Trade-offs und Migrationspfade entwerfen

DECISION-SENSITIVE
→ schwer umkehrbare Systemgrenzen, Plattform-, Daten- oder Integrationsentscheidungen

EVOLUTION / MIGRATION
→ bestehende Struktur schrittweise verändern; Zwischenzustände und Compatibility beachten

IMPLEMENT / DEPLOY
→ reale Code-, Daten-, Infrastruktur- oder Produktionsänderungen; gehören in die jeweiligen Fachprozesse und lokalen Gates
```

Ein Architektur-Verdict oder eine Empfehlung autorisiert keine Implementierung, Migration oder Produktionsänderung.

## Operative Skills

- `architecture-baseline`
- `system-design`
- `architecture-decomposition`
- `architecture-tradeoff-analysis`
- `architecture-evolution`
- `architecture-conformance-review`
- `architecture-review`

## Evalstatus

Für die sieben Skills sind 42 Startfälle definiert. Der erste Same-Model-Smoke-Lauf wurde am 2026-08-25 gegen den gepinnten Stand `78abce4ade2e1d92dfc47f6169dcd2551d8d0f09` ausgeführt.

Ergebnis:

- 42/42 Fälle entsprachen dem erwarteten Verhalten und Status;
- 30× `pass`;
- 6× `partial`;
- 6× `blocked`;
- 0 beobachtete verbotene Verhaltensweisen.

Der Lauf ist im Eval-Artefakt `../Evals/Software-Architecture-und-System-Design/Same-Model-Smoke-2026-08-25.md` dokumentiert. Da dasselbe Modell die Kriterien sehen und das Verhalten bewerten konnte, ersetzt der Lauf keinen unabhängigen verblindeten Benchmark und verändert weder `maturity: experimental` noch `eval_coverage: partial`.

## Leitgedanken

> Erst bestätigte Drivers und Invarianten, dann Struktur, dann Technologie.

> Die einfachste tragfähige Architektur ist der Ausgangspunkt, nicht der langweilige Kandidat.

> Verteilte Mechanismen müssen ihren Preis durch einen echten Bedarf rechtfertigen.

> Quality Attributes werden über konkrete Szenarien und Trade-offs belastbar.

> Architektur muss evolutionär veränderbar und gegen ihre eigenen Regeln prüfbar sein.

> Allgemeine Arbeitsweise zentral, konkrete Architektur lokal.