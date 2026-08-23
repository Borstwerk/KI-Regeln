# Transaktionen, Isolation und Concurrency

## Zweck

Transaktionen sollen konkrete Konsistenz- und Atomicity-Anforderungen erfüllen. Sie sind kein pauschaler Ersatz für gutes Datenmodell oder saubere Nebenläufigkeitslogik.

## Grundprinzip

> Nicht zuerst fragen „Wie packe ich das in eine Transaktion?“, sondern „Welche Invariante muss unter Konkurrenz erhalten bleiben?“

## Vor dem Design klären

- welche Operationen müssen atomar sein?;
- welche Zwischenzustände dürfen andere Prozesse sehen?;
- welche konkurrierenden Schreib- und Lesepfade existieren?;
- sind Lost Updates, Write Skew oder doppelte Verarbeitung möglich?;
- welche Konflikte dürfen mit Retry gelöst werden?;
- welche Locks oder Isolationseigenschaften bietet die reale Engine?

## Isolation ist enginespezifisch

Begriffe wie Read Committed, Snapshot, Repeatable Read oder Serializable können je nach Datenbankmodell unterschiedlich umgesetzt sein.

Darum:

- nicht aus allgemeinem Modellwissen auf konkrete Guarantees schließen;
- Dokumentation der verwendeten Engine und Version prüfen;
- tatsächliches Verhalten durch geeignete Tests verifizieren.

## Transaktionsumfang klein und bewusst halten

Lange oder unnötig breite Transaktionen können:

- Locks verlängern;
- Konflikte erhöhen;
- Ressourcen binden;
- Retry-Kosten vergrößern;
- Deadlocks wahrscheinlicher machen.

Externe Netzwerkaufrufe oder langsame Nutzerinteraktion gehören normalerweise nicht unreflektiert in eine offene DB-Transaktion.

## Retry ist Teil des Designs

Bei optimistischer Konkurrenz oder serialisierbaren Konflikten kann ein korrekter Ablauf legitime Abbrüche erzeugen.

Dann prüfen:

- ist die Operation idempotent oder sicher wiederholbar?;
- welche Fehler sind retrybar?;
- wie viele Retries sind sinnvoll?;
- gibt es Backoff / Jitter?;
- was passiert nach ausgeschöpftem Retry-Budget?

## Deadlocks und Locking

Bei Locking-Problemen nicht nur Timeout erhöhen.

Stattdessen:

1. konkurrierende Operationen identifizieren;
2. Lock-Reihenfolge und Dauer verstehen;
3. unnötig große Transaktionen verkleinern;
4. Zugriffspfade / Indizes prüfen;
5. reproduzierbare Concurrency-Tests bauen;
6. erst dann Timeout-/Retry-Parameter anpassen.

## Distributed / Multi-Document Transactions

Nur einsetzen, wenn die fachliche Invariante dies verlangt.

Vorher prüfen, ob ein besseres Datenmodell oder ein anderes Konsistenzmuster die Notwendigkeit reduziert.

## Review-Output

```text
Invariante
→ konkurrierende Pfade
→ benötigte Atomicity
→ Isolation / Consistency
→ Lock-/Conflict-Risiken
→ Retry-Strategie
→ Verifikation
```

## Leitgedanke

> Concurrency-Korrektheit entsteht aus expliziten Invarianten und beobachtetem Verhalten – nicht aus dem Wort „Transaction“.