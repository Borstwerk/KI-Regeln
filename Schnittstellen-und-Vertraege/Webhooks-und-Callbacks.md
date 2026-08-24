# Webhooks und Callbacks

## Einordnung

Webhooks sind HTTP-basierte, asynchron ausgelöste Provider→Consumer-Aufrufe. Sie liegen damit zwischen HTTP-Vertrag und Event-Semantik.

Sie bekommen zunächst keinen eigenen zentralen Skill.

## Unterscheidung

OpenAPI unterscheidet sinnvoll:

- **Callback:** Out-of-band Request, der durch eine vorherige API-Operation ausgelöst und mit ihr verknüpft ist;
- **Webhook:** Provider-initiierter Request, der unabhängig von einer unmittelbar vorhergehenden API-Operation auftreten kann.

## Contract-Inhalte

Mindestens definieren:

- wer Sender und Empfänger ist;
- Trigger / Event Type;
- Ziel-URL bzw. Registrierungsmechanismus;
- HTTP-Methode;
- Payload und Headers;
- Authentizitäts-/Signaturanforderungen als Contract-Oberfläche;
- Response-/Acknowledgement-Semantik;
- Timeout;
- Retry und Backoff;
- Duplicate-Verhalten / Idempotenz;
- Ordering, falls zugesichert;
- Event-ID / Correlation;
- Versionierung und Deprecation.

## Sicherheitsgrenze

Konkrete Signaturprüfung, Secret Rotation, Replay-Schutz, SSRF-/Callback-URL-Risiken und Provider-spezifische Securitymechanik gehören in die lokale Integration und `Sicherheit/`.

## Skillrouting

- allgemeine Wahl/Contract: `interface-design`;
- HTTP-Oberfläche: `http-api-design`;
- eventartige Delivery-/Replay-Fragen: `event-contract-design`;
- Änderung: `contract-change-review`.

## Leitgedanke

> Ein Webhook ist nicht „ein POST von außen“, sondern ein eigener Consumervertrag mit Failure- und Retry-Semantik.