# Paradigmen und Schnittstellenauswahl

## Keine Transportreligion

REST, GraphQL, RPC, Events, Webhooks und Streams sind unterschiedliche Vertragsformen. Keine davon ist universell überlegen.

Vor der Auswahl prüfen:

- Consumer und deren Tooling;
- synchrone vs. asynchrone Interaktion;
- Request-/Response- vs. Push-/Subscribe-Modell;
- benötigte Typisierung und Codegenerierung;
- Latenz- und Streaminganforderungen;
- Cache-/Intermediärverhalten;
- unabhängige Deployments;
- Evolution und Compatibility;
- Replay-/Ordering-/Delivery-Anforderungen;
- öffentliche, Partner- oder interne Nutzung.

## Typische Fits

### HTTP / REST-artig

Geeignet für breit interoperable Request-/Response-Schnittstellen, Ressourcen und Aktionen mit HTTP-Semantik.

### GraphQL

Geeignet, wenn Consumer flexible, typisierte Auswahl über ein Graphmodell benötigen und Schema-/Resolver-Governance beherrscht wird.

### RPC / IDL / gRPC

Geeignet für stark typisierte Methodenverträge, generierte Clients, Streaming oder interne Servicekommunikation mit kontrolliertem Tooling.

### Events / Messaging

Geeignet, wenn Produzenten Zustandsänderungen oder Nachrichten unabhängig von unmittelbarer Consumerantwort veröffentlichen und Delivery, Ordering oder Replay Teil des Vertrags sind.

### Webhooks / Callbacks

HTTP-basierte Provider→Consumer-Aufrufe. Sie verbinden HTTP-Vertragssemantik mit asynchroner Auslösung.

## Anti-Regeln

Nicht zentral festschreiben:

- öffentlich = REST;
- intern = gRPC;
- GraphQL ersetzt REST;
- Events sind immer entkoppelt;
- Microservices brauchen Messaging.

Die lokale Architektur und Consumerrealität entscheiden.

## Output einer Auswahl

Mindestens:

```text
Consumer
Provider
Capability
gewählter Interaktionsstil
warum dieser Stil passt
wichtigste Contract-Eigenschaften
Compatibility-Anforderungen
offene Architekturentscheidungen
```

## Leitgedanke

> Erst Kommunikationsproblem verstehen, dann Transport wählen.