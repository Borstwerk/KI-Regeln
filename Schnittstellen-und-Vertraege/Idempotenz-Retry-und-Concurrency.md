# Idempotenz, Retry und Concurrency

## Zweck

Wiederholung und konkurrierende Änderungen müssen Teil der beobachtbaren Schnittstellensemantik sein, wenn Consumer davon betroffen sind.

## Idempotenz

Für wiederholbare Mutationen klären:

- wodurch eine Operation eindeutig identifiziert wird;
- ob gleiche Identität + gleicher Inhalt dasselbe Ergebnis liefert;
- was gleiche Identität + anderer Inhalt bedeutet;
- wie lange die Identität gültig ist;
- welches Ergebnis bei Replay zurückgegeben wird;
- welche Seiteneffekte höchstens einmal bzw. mehrfach auftreten dürfen.

## Retry

Ein Retry ist nur sicher, wenn der Contract ausreichende Semantik liefert.

Definieren:

- welche Fehler retrybar sind;
- wer retried;
- ob Retry automatisch oder explizit ist;
- Backoff-/Retry-After-Signale, falls relevant;
- wie Doppelverarbeitung verhindert oder toleriert wird;
- wann ein Consumer aufgeben muss.

Keine pauschale Regel „Netzwerkfehler → erneut senden“.

## Concurrency

Bei konkurrierenden Writes können Contracts Mechanismen wie Versionsmarker, ETags, Preconditions oder fachliche Konfliktcodes anbieten.

Der Contract muss beschreiben, was ein verlorenes Update, stale Write oder Conflict für den Consumer bedeutet.

## Async

Bei Events zusätzlich:

- at-most-once / at-least-once / andere lokale Delivery-Erwartung;
- Duplicate-Erkennung;
- Ordering Scope;
- Replay;
- idempotente Consumerverarbeitung.

## Grenze zu Reliability

Dieser Bereich definiert die Schnittstellen-Zusagen.

`../Reliability-und-System-Observability/` prüft systemisch, ob das Gesamtsystem diese Zusagen unter realistischen Ausfällen, Overload, Retry Amplification oder Dependency-Störungen tatsächlich halten kann.

```text
Interface / Contract
→ was Retry, Idempotenz, Delivery und Concurrency bedeuten

Reliability / Resilience
→ ob das resultierende Gesamtsystemverhalten unter Störung tragfähig bleibt
```

## Leitgedanke

> Wiederholung ist nur dann sicher, wenn beide Seiten dasselbe unter „dieselbe Operation“ verstehen.