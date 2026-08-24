---
name: event-contract-design
description: Entwirft oder prüft asynchrone Event- und Message-Verträge zwischen Producer und Consumern. Verwenden bei Topics/Channels, Event Envelope, Payload, Delivery, Ordering, Retry, Idempotenz, Replay, Dead Letter, Correlation und Schemaevolution. Nicht für Domain-Event-Discovery oder reine HTTP-Endpunkte verwenden.
---

# Event Contract Design

## Ziel

Asynchrone Kommunikation so explizit machen, dass unabhängige Producer und Consumer dieselbe Bedeutung, Delivery- und Evolutionserwartung teilen.

## Eingaben

- fachliches Ereignis / Message-Zweck;
- Producer und Owner;
- bekannte/erwartete Consumer;
- Broker/Transport, soweit lokal vorgegeben;
- Delivery-/Ordering-/Replay-Anforderungen;
- bestehende Eventschemas und Consumer bei Brownfield.

## Arbeitsweise

1. Producer, Owner, Consumer und fachliche Bedeutung benennen.
2. Event Type von Topic/Channel unterscheiden.
3. Envelope und Payload mit required/optional/null/Version definieren.
4. Delivery-, Ordering- und Duplicate-Semantik explizit machen.
5. Idempotenz, Retry, Replay, Retention und Dead Letter nur soweit zugesichert definieren.
6. Correlation, Causation und Tracebezug festlegen, wenn nötig.
7. Compatibility- und Deprecation-Regeln definieren.
8. AsyncAPI/Schema/Fixtures als Contract-Artefakte bestimmen.
9. positive und relevante negative Contract-Test-Erwartungen nennen.

## Nicht tun

- Domain-Event-Discovery mit Contract-Design verwechseln;
- „at least once“ oder globale Reihenfolge behaupten, wenn die Infrastruktur das nicht garantiert;
- Brokerdefaults zur fachlichen Contract-Wahrheit erklären;
- Consumer durch unnötige interne Felder koppeln;
- Webhook-Signatursecurity detailliert erfinden.

## Ausgabe

```text
Producer / Owner
Consumers
Event Type
Channel / Topic
Envelope / Payload
Delivery / Ordering
Retry / Idempotency
Replay / Dead Letter
Compatibility
Contract Artifact / Tests
```

## Related

- `interface-design`
- `contract-change-review`
- `contract-testing`
- `failure-testing`