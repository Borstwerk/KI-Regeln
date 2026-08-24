# Workflow – Schnittstellenvertrag entwerfen und ändern

## Ziel

Neue oder bestehende Systemgrenzen mit expliziten, testbaren und evolvierbaren Verträgen bearbeiten.

## Neuer Contract

```text
Anforderung / Capability
→ lokale Architektur-/Domain-Sources-of-Truth
→ interface-design
→ je nach Stil:
   ├─ http-api-design
   ├─ event-contract-design
   └─ interface-design + passende GraphQL/RPC/Webhook-Fachregeln
→ Contract Artifact
→ Implementierung
→ contract-testing
→ integration-testing nach Risiko
→ interface-review
→ lokales Human-/Release-Gate
```

## Änderung eines bestehenden Contracts

```text
Baseline Contract + Consumerinventar
→ geplante Änderung
→ contract-change-review
→ COMPATIBLE?
   ├─ ja → Implementierung + Tests
   ├─ ROLLOUT-SENSITIVE → Reihenfolge/Migration + Tests + Gate
   ├─ BREAKING → Versionierung/Deprecation/Migration + Human Gate
   └─ UNVERIFIED → fehlende Evidence beschaffen
→ contract-testing
→ interface-review bei größeren Änderungen
```

## Breaking-/Deprecation-Lifecycle

```text
Breaking Need
→ Migration Strategy
→ neue/alternative Contract-Oberfläche
→ Deprecation
→ Consumer Migration
→ Usage/Evidence prüfen
→ Sunset
→ Removal Gate
```

## Sicherheit

Authentisierung, Scopes und Tenant-Grenzen gehören in den Contract. Detaillierte Security-Mechanik und Security Testing bleiben `Sicherheit/` und erhalten eigene Gates.

## Evidence

Je nach Änderung:

- Baseline und Target Contract;
- Contract Diff;
- Consumerliste/-annahmen;
- Compatibility Verdict;
- Migration/Deprecation;
- Contract-Test-Ergebnisse;
- offene Risiken;
- lokale Freigabe.

## Leitgedanke

> Erst Vertrag und Change-Risiko verstehen, dann implementieren.