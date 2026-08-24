# Architekturstile und Patterns

## Zweck

Architekturstile und Patterns sind Lösungsformen für wiederkehrende Kräfte. Sie sind keine Qualitätsstempel und keine Ausgangspunkte einer Architekturentscheidung.

## Auswahlmodell

```text
Driver / Constraint / Failure Mode
→ benötigte Eigenschaft
→ passende strukturelle Optionen
→ Kosten und neue Failure Modes
→ lokale Entscheidung
```

## Typische Styles und Patterns

Je nach Problem können unter anderem relevant sein:

- Monolith / Modular Monolith;
- Layered Architecture;
- Ports-and-Adapters / Hexagonal;
- Service-oriented / Microservices;
- Event-driven Architecture;
- Pipes and Filters;
- CQRS;
- Event Sourcing;
- Saga / Process Manager;
- Strangler Fig;
- Broker, Queue, Log oder Stream-basierte Koordination.

Die Liste ist ein Werkzeugkasten, keine Reifeleiter.

## Pattern-Profil

Wenn ein Pattern ernsthaft betrachtet wird, mindestens festhalten:

```text
Problem / Driver
Voraussetzungen
gewonnene Eigenschaften
zusätzliche Komplexität
neue Failure Modes
Betriebs- und Observability-Kosten
Migrationskosten
wann nicht verwenden
Evidence, die die Entscheidung später widerlegen könnte
```

## Beispiel Microservices

Ein Service-Split kann sinnvoll sein bei nachgewiesener unabhängiger Ownership, Failure-Isolation, stark unterschiedlicher Skalierung oder notwendigem unabhängigen Lifecycle.

Er erzeugt zugleich Kosten durch:

- Netzwerk- und Partial-Failure-Semantik;
- verteilte Datenkonsistenz;
- Contract Evolution;
- zusätzliche Deployments und Runtime-Evidence;
- Incident- und Debugging-Komplexität.

Ohne einen Driver, der diese Kosten rechtfertigt, ist ein modularer In-Process-Schnitt oft die einfachere tragfähige Grenze.

## Anti-Regeln

- Microservices nicht nach Teamgröße allein auswählen;
- DDD nicht mit Microservices gleichsetzen;
- Hexagonal nicht als notwendige Form wartbarer Software behandeln;
- CQRS nicht allein wegen unterschiedlicher Reads und Writes einführen;
- Event Sourcing nicht mit Audit Logging verwechseln;
- Events nicht automatisch als lose Kopplung behandeln;
- Kubernetes oder Cloud nicht als Architekturstil behandeln.

## Leitgedanke

> Ein Pattern ist gut, wenn es einen konkreten Druck besser trägt als seine Alternativen – nicht weil sein Name bekannt ist.