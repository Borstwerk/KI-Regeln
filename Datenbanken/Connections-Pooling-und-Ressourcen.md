# Connections, Pooling und Ressourcen

## Zweck

Datenbankzugriffe sollen Verbindungen und Ressourcen bewusst behandeln. Connection Management ist Teil der Systemarchitektur, nicht bloß Client-Konfiguration.

## Grundprinzip

> Eine Datenbankverbindung ist eine begrenzte Ressource mit Lebenszyklus, Timeout- und Fehlerverhalten.

## Vor der Konfiguration klären

- wie viele parallele Requests / Worker existieren?;
- wie viele App-Instanzen greifen auf die DB zu?;
- welche Connection-Grenzen hat die reale Engine / Plattform?;
- verwendet der Client Pooling oder Multiplexing?;
- welche Operationen blockieren Verbindungen lange?;
- wie verhalten sich Serverless-/Auto-Scaling-Umgebungen?;
- welche Timeouts und Retries gelten bereits?

## Nicht eine Verbindung pro Request öffnen

Falls die verwendete Engine / Library persistente Verbindungen unterstützt, passende Pooling- oder Multiplexing-Mechanismen nutzen.

Konkrete Größenwerte nicht pauschal aus anderen Projekten übernehmen.

## Poolgröße systemweit denken

Nicht nur:

```text
Pool pro Instanz = 50
```

sondern:

```text
Pool pro Instanz
× maximale Instanzen
+ Admin / Jobs / Background Worker
= möglicher Gesamtverbrauch
```

Pools so wählen, dass die Datenbank nicht durch horizontales Scaling ungewollt erschöpft wird.

## Timeouts bewusst trennen

Je nach Client können relevant sein:

- Connect Timeout;
- Acquire / Pool Timeout;
- Query / Statement Timeout;
- Read / Socket Timeout;
- Transaction Timeout;
- Idle Timeout.

Ein höherer Timeout ist keine Diagnose für ein strukturelles Performanceproblem.

## Retry

Retries nur bei tatsächlich retrybaren Fehlern.

Prüfen:

- kann die Operation doppelt ausgeführt werden?;
- ist sie idempotent?;
- besteht Thundering-Herd-Risiko?;
- existiert Backoff / Jitter?;
- kann ein Retry eine überlastete DB weiter belasten?

## Round-Trips und Batching

Viele kleine unabhängige DB-Aufrufe können mehr kosten als eine passende Batch-/Set-basierte Operation.

Aber Batching nicht so groß machen, dass:

- Locks unnötig lang gehalten werden;
- Speicher explodiert;
- Fehlerbehandlung unhandlich wird;
- Timeouts wahrscheinlicher werden.

## Ressourcen-Evidence

Bei Connection-Problemen möglichst messen:

- aktive / wartende Verbindungen;
- Pool-Auslastung;
- Acquire-Wartezeiten;
- Query-Latenz;
- Timeout-/Retry-Rate;
- Transaktionsdauer;
- Instanzanzahl.

## Leitgedanke

> Connection Tuning ist Kapazitäts- und Concurrency-Management – keine einzelne magische Poolzahl.