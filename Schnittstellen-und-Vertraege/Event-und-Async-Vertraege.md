# Event- und Async-Verträge

## Warum eigener Schnitt

Asynchrone Verträge besitzen Eigenschaften, die bei klassischem Request/Response nicht bloß Zusatzfelder sind:

- Producer-/Consumer-Unabhängigkeit;
- Channel/Topic;
- Delivery;
- Ordering;
- Retry;
- Idempotenz;
- Replay;
- Dead Letter;
- Schemaevolution;
- Correlation/Causation;
- zeitliche Entkopplung.

Deshalb existiert der eigene Skill `event-contract-design`.

## Ein Event Contract beschreibt mindestens

- Producer und Owner;
- bekannte/erwartete Consumer;
- Event Type / Message Type;
- fachliche Bedeutung;
- Envelope und Payload;
- Channel-/Topic-Semantik;
- erforderliche/optionale Felder;
- Ordering-Garantien;
- Delivery-Garantie bzw. Erwartung;
- Duplicate-Verhalten und Idempotenz;
- Retry / Backoff, soweit Teil des Vertrags;
- Replay und Retention, soweit relevant;
- Dead-Letter-/Failure-Verhalten;
- Compatibility und Deprecation;
- Correlation-/Causation-/Trace-Bezug.

## AsyncAPI

AsyncAPI 3.x trennt Channels, Messages und Operations und beschreibt Sender-/Receiver-Verträge. Protokollspezifische Bindings bleiben bewusst transportlokal.

## CloudEvents

CloudEvents kann ein interoperables Modell für gemeinsame Eventmetadaten liefern. Es ist ein möglicher Envelope-Standard, keine Pflicht für jede Eventarchitektur.

## Event Discovery ≠ Event Contract

```text
Domain-/Event Discovery
→ Was passiert fachlich?

Event Contract Design
→ Was wird exakt veröffentlicht und garantiert?
```

## Leitgedanke

> Sobald ein unabhängiger Consumer ein Event nutzt, wird aus einer internen Nachricht ein evolvierbarer Vertrag.