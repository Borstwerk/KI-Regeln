# Architekturevidence, Views, ADRs und Dokumentation

## Zweck

Architekturdokumentation soll Entscheidungen und relevante Systemzusammenhänge nachvollziehbar machen. Sie ist kein Selbstzweck und kein Ersatz für die tatsächliche Implementierung.

## Evidence-Typen

Je nach Frage können relevant sein:

- Source Code und Dependency Graph;
- Runtime-/Deployment-Konfiguration;
- APIs, Events und Datenverträge;
- Schema- und Datenownership;
- ADRs und bestehende Designentscheidungen;
- C4-/Runtime-/Deployment-Views;
- Tests und Architecture Fitness Functions;
- Runtime-/Reliability-Evidence;
- Change History und Migrationsartefakte.

Code ist nicht automatisch alleinige Wahrheit: bei Widerspruch zwischen Spezifikation, ADR und Implementierung den Konflikt sichtbar machen statt still eine Quelle zu bevorzugen.

## Views nach Frage

Mögliche Sichten:

- System Context – Außenwelt und Verantwortung;
- Container / Deployable – wesentliche Laufzeiteinheiten;
- Component / Module – relevante interne Verantwortung;
- Runtime – kritische Interaktion oder Fehlerfluss;
- Deployment – Zuordnung zu Runtime-/Infrastrukturgrenzen;
- Data / State – authoritative Stores, derived Views und Flüsse;
- Decision View – Drivers, Optionen und Trade-offs.

Nur die Views erstellen, die für die Entscheidung oder Kommunikation tatsächlich Erkenntnis liefern.

## C4

C4 ist eine nützliche, leichtgewichtige Sprache für Abstraktionsebenen. Es ist keine Pflicht, alle vier Ebenen zu erzeugen. Ein gutes Context- oder Containerdiagramm ist wertvoller als ein vollständiges, aber irrelevantes Diagrammpaket.

## arc42

arc42 dient als Coverage-Inspiration für Architekturkommunikation, unter anderem für Ziele/Constraints, Kontext, Solution Strategy, Building Blocks, Runtime, Deployment, Cross-Cutting Concepts, Entscheidungen, Quality und Risiken.

Das Repo übernimmt arc42 nicht als Pflichttemplate.

## ADRs

Architekturentscheidungen mit langfristigen, überraschenden oder schwer umkehrbaren Konsequenzen können mit dem vorhandenen `adr`-Skill dokumentiert werden.

Nicht jede kleine Strukturentscheidung braucht ein ADR. ADRs dokumentieren Entscheidungshistorie; sie treffen die Entscheidung nicht selbst.

## Evidence-Status

Bei Reviews und Baselines unterscheiden:

- `CONFIRMED`
- `LIKELY`
- `UNVERIFIED`
- `CONFLICTING`

Diagramme oder alte ADRs dürfen nicht automatisch als aktuelle Ist-Architektur behandelt werden.

## Leitgedanke

> Gute Architekturdokumentation beantwortet konkrete Fragen und hält Entscheidungen nachvollziehbar – sie beweist nicht durch Umfang ihre Qualität.