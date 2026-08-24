# Runtime-Flows, State und Koordination

## Zweck

Statische Kästen erklären nicht, wie ein System unter Last, Fehlern oder konkurrierenden Änderungen tatsächlich reagiert. Kritische Architekturentscheidungen brauchen deshalb Runtime-Sichten.

## Kritische Flows

Für relevante End-to-End-Flows beschreiben:

- Auslöser und Actor;
- beteiligte Komponenten;
- authoritative und derived State;
- synchrone und asynchrone Schritte;
- Commit-/Acknowledgement-Punkt;
- Idempotenz-/Retry-Verantwortung;
- Deadlines, Backpressure oder Queue Bounds;
- Partial Failure und Recovery;
- finalen fachlichen Effekt.

## State Ownership

Für autoritativen Zustand klären:

```text
Wer darf schreiben?
Wann gilt ein Write als akzeptiert oder durable?
Wer bestimmt Ordering?
Wie werden Konflikte erkannt oder aufgelöst?
Welche Views sind abgeleitet und wie werden sie rekonstruiert?
```

Die konkrete Persistenzmechanik gehört bei Bedarf an Datenbanken oder Data Engineering.

## Coordination

Koordination kostet Verfügbarkeit, Latenz, Komplexität oder Durchsatz. Deshalb erst klären, welche Invariante überhaupt globale oder verteilte Abstimmung benötigt.

Nicht pauschal `strong consistency`, `eventual consistency`, Locks, Consensus, Sagas oder Events wählen.

## Failure-Flows

Mindestens für kritische Pfade prüfen:

- Dependency langsam statt hart down;
- Duplicate Submit oder redelivered Message;
- Retry Storm;
- partieller Write;
- Consumer laggt;
- Queue/Backlog wächst schneller als Drain Capacity;
- Prozess stirbt nach Seiteneffekt, aber vor Acknowledgement;
- Cache oder abgeleitete View ist stale;
- Recovery erzeugt erneut Last.

## Handoffs

- Wire-/Delivery-/Retry-Vertrag → Schnittstellen und Verträge;
- konkrete DB-Transaktion/Isolation → Datenbanken;
- Dataset-Replay/Backfill → Data Engineering;
- SLO/Capacity/Incident/Resilience Evidence → Reliability;
- konkrete Fault Tests → Testing und QA.

## Leitgedanke

> Eine Architektur ist erst verstanden, wenn ihre kritischen Flows auch im Fehlerfall einen erklärbaren Zustand erreichen.