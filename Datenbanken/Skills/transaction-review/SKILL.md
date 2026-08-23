---
name: transaction-review
description: Prüft Transaktionsgrenzen, Isolation, Locking, Race Conditions und Retry-Verhalten gegen konkrete fachliche Invarianten. Verwenden bei Lost Updates, Deadlocks, konkurrierenden Writes, mehrstufigen atomaren Abläufen oder Isolation-Fragen. Nicht für einfache Query-Performanceprobleme verwenden.
compatibility: Konkrete Isolationseigenschaften müssen gegen Engine und Version verifiziert werden; Concurrency-Tests oder reale Diagnose sind bevorzugt.
---

# Transaction Review

## Ziel

Prüfen, ob ein konkurrierender Datenbankablauf die benötigten Invarianten tatsächlich erhält.

## Workflow

1. Fachliche Invariante benennen.
2. Konkurrierende Read-/Write-Pfade identifizieren.
3. Benötigte Atomicity und Sichtbarkeit bestimmen.
4. Reale Isolation-/Consistency-Semantik der Engine prüfen.
5. Locking, Konflikte und Deadlock-Risiken analysieren.
6. Retry-/Idempotenzstrategie prüfen.
7. Transaktionsdauer und externe Seiteneffekte prüfen.
8. Reproduzierbare Concurrency-Tests definieren oder ausführen.

## Regeln

- Transaktion nicht als Ersatz für unpassendes Datenmodell verwenden.
- Keine Isolation-Garantie aus generischem Wissen behaupten.
- Längere Timeouts sind keine Deadlock-Lösung.
- Retry nur bei retrybaren Fehlern und sicher wiederholbaren Operationen.
- Netzwerk-/User-Interaktion nicht unreflektiert innerhalb einer offenen DB-Transaktion halten.

## Output

```text
Invariante
konkurrierende Pfade
Transaktionsgrenze
Isolation / Consistency
Lock-/Conflict-Risiko
Retry / Idempotenz
Tests / Evidence
Restrisiko
```

## Leitgedanke

> Die Invariante bestimmt die Transaktion – nicht umgekehrt.