# Skill-Handbuch – Software Architecture und System Design

Dieses Handbuch hilft bei der Auswahl der sieben Skills aus `Software-Architecture-und-System-Design/`.

## Schnellauswahl

| Wenn die Aufgabe lautet … | Primärer Skill |
|---|---|
| bestehende Architektur zuerst belastbar verstehen | `architecture-baseline` |
| ein neues oder wesentlich verändertes System ganzheitlich entwerfen | `system-design` |
| Modul-/Service-/Dependency-Grenzen schneiden | `architecture-decomposition` |
| mehrere echte Architekturvarianten vergleichen | `architecture-tradeoff-analysis` |
| eine bestehende Architektur schrittweise migrieren | `architecture-evolution` |
| Soll-Architektur gegen Code/Dependencies/ADRs prüfen | `architecture-conformance-review` |
| einen breiten unabhängigen Architektur- oder Readiness-Audit durchführen | `architecture-review` |

## Auswahlregeln

### `architecture-baseline`

Verwenden, wenn die Frage zuerst lautet: **Was existiert tatsächlich?**

Der Skill rekonstruiert System Context, Komponenten, Ownership, Dependencies, Flows, Entscheidungen und Evidence-Konflikte. Er entwirft noch keine Zielarchitektur.

### `system-design`

Verwenden, wenn eine strukturelle Zielentscheidung nötig ist. Voraussetzung sind bestätigte Drivers/Constraints oder klar markierte Annahmen.

Wichtig:

- einfachste tragfähige Architektur zuerst;
- weitere Kandidaten nur bei echter struktureller Alternative;
- verteilte Mechanismen müssen ihren Platz begründen;
- fehlende Zielwerte werden nicht erfunden.

### `architecture-decomposition`

Verwenden für Boundary-Fragen: Module, Services, Ownership, Public Surfaces und Dependency Direction.

Ein Service-Split braucht einen realen Driver. Bounded Context, Teamgröße oder Patternpräferenz reichen nicht.

### `architecture-tradeoff-analysis`

Verwenden, wenn mindestens zwei **viable** Kandidaten existieren und die Entscheidung von mehreren Quality Attributes oder Failure-/Betriebsbedingungen abhängt.

Keine künstlichen Kandidaten und keine opaque Gesamtpunktzahl.

### `architecture-evolution`

Verwenden, wenn eine Architektur nicht nur entschieden, sondern von Architecture 0 zu einem Zielbild migriert werden muss.

Der Skill plant Zwischenzustände, Compatibility, Evidence, Abort/Rollback und Retirement. Er führt keine produktive Migration aus.

### `architecture-conformance-review`

Verwenden bei Architekturdrift, Dependency-/Boundary-Regeln, ADR-Compliance und Architecture Fitness Functions.

Er braucht ein gültiges lokales Referenzmodell. Ohne Soll-Regel kann er beobachtete Struktur beschreiben, aber keine eigene Architekturregel erfinden.

### `architecture-review`

Verwenden für den breiten unabhängigen Schlussaudit eines Systemdesigns oder vor einem lokalen Readiness-Gate.

Er prüft Drivers, Kontext, Grenzen, State, Flows, Trade-offs, Pattern-Fit, Technologie, Evolution, Evidence und Conformance. Findings werden nicht implementiert.

## Wichtige Handoffs

| Tieferes Thema | Zuständiger Bereich / Skill |
|---|---|
| Fachbegriffe und Fachobjekte | `domain-modeling` |
| API-/Event-/Message-Contract | `interface-design`, `event-contract-design`, `contract-change-review` |
| DB-Schema, Query, Transaction | Datenbanken |
| Datenpipeline / Dataset / Backfill | Data Engineering |
| SLO, Capacity, Incident, Resilience | Reliability und System-Observability |
| Deployment-/IaC-Mechanik | Infrastruktur und DevOps |
| Teststrategie | Testing und QA |
| Architekturentscheidung dauerhaft dokumentieren | `adr` |
| Klassen-/Methoden-/Implementierungsqualität | Programmieren / `code-review` |

## Patterns sind keine Skills

Microservices, Modular Monolith, Layered, Hexagonal, DDD, CQRS, Event Sourcing, Saga, Strangler und Event-driven sind Optionen beziehungsweise Patterns. Sie werden durch die Architektur-Skills ausgewählt oder verworfen, nicht als eigene Arbeitsdisziplinen automatisch aktiviert.

## Evals

Für jeden der sieben Skills existieren sechs definierte Evalfälle unter:

`Evals/Software-Architecture-und-System-Design/`

Damit sind **42 Evalfälle definiert**. Definiert bedeutet nicht ausgeführt oder bestanden.

## Leitgedanke

> Der richtige Architektur-Skill richtet sich nach der Entscheidung, die getroffen oder geprüft werden muss – nicht nach dem Patternnamen im Prompt.