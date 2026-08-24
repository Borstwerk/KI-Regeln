# Contract First und maschinenlesbare Artefakte

## Contract First

Bei getrennt entwickelten Consumern und Providern ist es häufig sinnvoll, den Vertrag vor oder unabhängig von der Implementierung explizit zu machen.

Das ermöglicht:

- parallele Entwicklung;
- Review vor teurer Implementierung;
- Code-/SDK-Generierung, falls sinnvoll;
- Mocking/Fakes auf dokumentierter Basis;
- Contract Testing;
- Breaking-Change-Diffs;
- bessere Discoverability.

## Geeignete Artefakte

Beispiele:

- OpenAPI für HTTP APIs;
- GraphQL Schema/SDL;
- Protobuf/IDL;
- AsyncAPI für Event-/Messaging-Contracts;
- JSON Schema als Schema-Baustein;
- Markdown/RFC für Semantik, die ein Format nicht vollständig ausdrückt.

## Eine Source of Truth

Ein Projekt muss klar bestimmen, welches Artefakt kanonisch ist.

Mögliche Modelle:

```text
spec-first
→ Contract-Datei ist führend

code-first
→ Code/Annotations sind führend, Contract wird erzeugt

hybrid
→ explizite Ownership + Driftprüfung
```

Keine Variante ist universell überlegen. Gefährlich ist nur unklare Doppelwahrheit.

## Tooling

Linting, Schema-Diffs, Codegen und Compatibility-Tools können starke Evidence liefern. Sie ersetzen nicht die semantische Bewertung realer Consumerannahmen.

## Dokumentation

Maschinenlesbarer Contract und menschliche Erklärung ergänzen sich. Beispiele, Semantik, Migration und Failure-Verhalten müssen für Consumer verständlich bleiben.

## Leitgedanke

> Maschinenlesbar macht einen Vertrag prüfbar – nicht automatisch richtig.