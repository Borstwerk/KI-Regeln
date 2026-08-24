# Quellen und Inspirationen

Dieser Bereich synthetisiert allgemeine Schnittstellenprinzipien aus Primärquellen, Standards und aktuellen Agent-Skills. Hersteller- oder formatspezifische Regeln werden nur verallgemeinert, wenn sie auch außerhalb des jeweiligen Stacks belastbar sind.

## Primär- und Standardquellen

### OpenAPI Specification 3.2.0

https://spec.openapis.org/oas/v3.2.0.html

Für maschinenlesbare HTTP-Contracts, Webhooks, Callbacks und Deprecation-Felder.

### HTTP Semantics – RFC 9110

https://www.rfc-editor.org/rfc/rfc9110

Für Method-, Status-, Safe-/Idempotent- und Headersemantik.

### Problem Details – RFC 9457

https://www.rfc-editor.org/rfc/rfc9457

Für interoperable strukturierte HTTP-Fehler.

### Deprecation HTTP Response Header – RFC 9745

https://www.rfc-editor.org/rfc/rfc9745

Für standardisierte Deprecation-Signale.

### Google API Improvement Proposals

https://google.aip.dev/180
https://google.aip.dev/184
https://google.aip.dev/185
https://google.aip.dev/193

Besonders relevant: Source-, Wire- und semantische Compatibility sowie aktuelle Versionierungs- und Error-Patterns. Google-spezifische Versionierungsformate werden nicht zentral verallgemeinert.

### GraphQL Specification – September 2025

https://spec.graphql.org/September2025/

Für Schema, Deprecation und Type-System-Evolution.

### Protocol Buffers Documentation

https://protobuf.dev/programming-guides/
https://protobuf.dev/best-practices/dos-donts/

Für Wire-/Source-Evolution, Field Numbers, Reserved Fields und generierten Code.

### gRPC Guides

https://grpc.io/docs/guides/

Für RPC-, Streaming-, Deadline-, Retry- und Statuskonzepte.

### AsyncAPI 3.1.0

https://www.asyncapi.com/docs/reference/specification/v3.1.0

Für Channels, Messages, Operations und eventbasierte Contracts.

### CloudEvents

https://cloudevents.io/

Als interoperabler Referenzpunkt für Event-Metadaten.

## Aktuelle Skill-Inspirationen

### hazamashoken/api-design-ai-skills – api-design-principles

Frameworkneutraler Skill mit guter Trennung zwischen Contract-Entscheidung und Frameworkadapter. Besonders relevant für Consumer-Fit, Contract-Semantik und die Reihenfolge Design → Umsetzung.

### jacob-balslev/skills – api-design

Sehr detaillierter HTTP-API-Skill mit klaren Near-Miss-Grenzen zu Events, Datenbanken, Testing und Frameworkmechanik.

### jacob-balslev/skills – event-contract-design

Guter eigenständiger Schnitt für Producer/Consumer, Envelope, Ordering, Replay, Dead Letter und Compatibility.

## Bewusst nicht übernommen

Nicht als universelle Regel übernommen werden etwa:

- jede API müsse von Tag eins `/v1` oder Header-Versionierung nutzen;
- alte Versionen müssten immer eine feste Anzahl Monate unterstützt werden;
- OpenAPI müsse zwingend generiert statt handgeschrieben sein;
- additive Schemaänderungen seien automatisch non-breaking;
- öffentliche APIs müssten REST und interne APIs gRPC sein.

## Grundsatz

> Externe Skills liefern Muster und Gegenbeispiele. Standards und reale Consumerverträge entscheiden, was davon tragfähig ist.