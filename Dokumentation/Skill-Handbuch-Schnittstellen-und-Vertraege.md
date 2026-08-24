# Skill-Handbuch – Schnittstellen und Verträge

## Wann dieser Bereich hilft

Wenn mehrere Komponenten, Dienste, Teams oder externe Consumer dieselbe Schnittstelle unterschiedlich interpretieren könnten.

## `interface-design`

Nutzen bei:

- neuer Systemgrenze mit noch zu wählender Interaktionsform;
- Consumer-/Provider-Vertrag über HTTP, GraphQL, RPC, Events oder Webhooks;
- Fragen wie „welche Zusagen müssen wir explizit machen?“

Nicht nutzen, um die komplette Systemarchitektur neu zu schneiden.

## `http-api-design`

Nutzen für konkrete HTTP-Verträge:

- Methoden/URIs;
- Request/Response;
- Status/Errors;
- Pagination/Filter/Ordering;
- Idempotenz/Retry;
- Auth/Tenant;
- Versionierung/Deprecation.

Nicht mit FastAPI-/Spring-/DRF-Implementierung verwechseln.

## `event-contract-design`

Nutzen wenn Delivery, Ordering, Replay, Duplicate-Verhalten oder unabhängige Consumer zum Vertrag gehören.

Typische Fälle:

- Kafka-/AMQP-/PubSub-Events;
- Event Streams;
- eventartige Webhooks.

## `contract-change-review`

Nutzen vor Änderungen an bereits genutzten Contracts.

Der Skill unterscheidet:

```text
Source
Wire
Semantic
```

und vergibt:

```text
COMPATIBLE
ROLLOUT-SENSITIVE
BREAKING
UNVERIFIED
```

Ein Schema-Diff allein reicht nicht für das Urteil.

## `interface-review`

Unabhängiger Gesamtcheck für einen Contract oder eine Schnittstellenfamilie.

Besonders sinnvoll vor:

- Partner-/Public-Releases;
- größeren Brownfield-Änderungen;
- Deprecation;
- Übergabe an andere Teams;
- Migrationen zwischen Contract-Versionen.

## Zusammenspiel mit Testing

```text
Schnittstellen-und-Vertraege
→ Sollvertrag definieren

contract-testing
→ Consumer-/Provider-Kompatibilität verifizieren

integration-testing
→ reales technisches Zusammenspiel prüfen
```

## Zusammenspiel mit Architektur

```text
Software Architecture
→ Wo liegt die Grenze?

interface-design
→ Was gilt über die Grenze?
```

## GraphQL, RPC und Webhooks

Sie besitzen eigene Regeldateien, aber noch keine eigenen Skills. Erst wenn reale Nutzung zeigt, dass die Arbeitsweise einen eigenständigen wiederkehrenden Skill rechtfertigt, wird der Skill-Schnitt neu bewertet.

## Maturity

Alle fünf neuen Skills starten `experimental` mit `partial` Evalabdeckung. Das bedeutet: strukturierte Start-Evals existieren, aber breite reale Regressionserfahrung fehlt noch.

## Leitgedanke

> Je unabhängiger Consumer deployen, desto teurer wird unklare oder stille Contract-Evolution.