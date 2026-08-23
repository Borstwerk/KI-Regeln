# Testebenen und Testportfolio

## Grundsatz

> Unterschiedliche Testebenen beantworten unterschiedliche Fragen. Redundanz ist nur sinnvoll, wenn sie zusätzliche Evidence liefert.

## Typische Ebenen

### Kleine / fokussierte Tests

Prüfen begrenztes Verhalten mit schnellem Feedback.

Geeignet für:

- Fachlogik;
- Berechnungen;
- Validierungsregeln;
- Zustandsübergänge;
- pure Funktionen;
- Fehlerbehandlung innerhalb einer klaren Einheit.

### Integrationstests

Prüfen reale Zusammenarbeit mehrerer Komponenten oder technischer Grenzen.

Geeignet für:

- Persistenz und Datenbankverhalten;
- Serialisierung;
- Framework-Konfiguration;
- Message Broker;
- Dateisystem;
- interne Services;
- reale technische Adapter.

### Contract Tests

Prüfen die Erwartungen an einer Schnittstelle zwischen Consumer und Provider.

Geeignet für:

- HTTP-/Event-Verträge;
- Schema- und Payload-Kompatibilität;
- Versionierungs- und Breaking-Change-Risiken.

Contract Tests ersetzen weder die fachlichen Tests des Providers noch End-to-End-Flows.

### End-to-End-Tests

Prüfen einen wichtigen Flow über mehrere reale Systemgrenzen aus Nutzungs- oder Geschäftsperspektive.

Sie sind besonders wertvoll für Risiken, die kleinere Tests nicht zuverlässig abdecken können.

Sie sind typischerweise teurer, langsamer und schwieriger zu isolieren als kleinere Tests.

## Auswahlregel

```text
Kann das Risiko auf kleinerer Ebene
zuverlässig und realistisch erkannt werden?

├─ ja → dort testen
└─ nein → nächstgrößere geeignete Ebene
```

## Kein starres Mengenverhältnis

Testpyramide, Test Trophy und ähnliche Modelle sind Heuristiken.

Keine universellen Prozentvorgaben für Unit-, Integration- oder E2E-Tests festschreiben.

Das passende Portfolio hängt unter anderem ab von:

- Architektur;
- Veränderungsgeschwindigkeit;
- Fehlerkosten;
- Integrationsdichte;
- Tooling;
- Testlaufzeit;
- benötigter Feedbackgeschwindigkeit.

## Duplikation

Dieselbe fachliche Regel muss nicht auf jeder Ebene identisch erneut getestet werden.

Mehrere Ebenen sind dann sinnvoll, wenn sie unterschiedliche Risiken absichern, zum Beispiel:

```text
Preisberechnung
→ fokussierter Fachlogiktest

API-Serialisierung des Preises
→ Integration / Contract

kompletter Checkout
→ ausgewählter E2E-Flow
```

## Leitfrage

> Welche neue Fehlermöglichkeit kann diese zusätzliche Testebene erkennen, die wir sonst nicht zuverlässig sehen?