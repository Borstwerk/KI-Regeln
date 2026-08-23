# Abfragen und Query-Sicherheit

## Zweck

Datenbankabfragen sollen fachlich korrekt, gegen das reale Schema geprüft, sicher parametriert und hinsichtlich ihrer Wirkung verstanden sein.

## Grundprinzip

> Eine syntaktisch plausible Query ist noch keine korrekte, sichere oder zulässige Query.

## Vor dem Schreiben oder Review

Soweit verfügbar prüfen:

- tatsächliches Schema und Feldnamen;
- Datentypen und Nullability;
- relevante Constraints und Beziehungen;
- erwartete Kardinalität;
- Mandanten-/Autorisierungsgrenzen;
- Engine-/Driver-/ORM-Version;
- vorhandene Query-Abstraktionen im Projekt.

Feld-, Tabellen-, Collection- oder Key-Namen nicht erfinden.

## Korrektheit

Prüfen:

- liefert die Query genau die intendierten Datensätze?;
- sind Join-/Reference-Bedingungen korrekt?;
- sind NULL / fehlende Felder / leere Mengen bedacht?;
- ist Sortierung deterministisch, wenn sie fachlich relevant ist?;
- sind Pagination und Limits robust?;
- sind Aggregationen und Gruppierungen fachlich korrekt?;
- können Duplikate oder Mehrfachtreffer entstehen?

## Sicherheit

Dynamische Werte werden über die sicheren Mechanismen der verwendeten Engine/Library gebunden.

Vermeiden:

- String-Konkatenation für untrusted Input;
- dynamische Identifier ohne Allowlist/Validierung;
- ungeprüfte freie Query-Fragmente aus Nutzereingaben;
- Umgehung bestehender Mandanten-/Berechtigungsfilter;
- Rückgabe sensibler Felder nur weil sie technisch vorhanden sind.

## Read ist nicht immer risikofrei

Auch reine Leseabfragen können problematisch sein:

- vollständige Scans großer Datenmengen;
- sehr teure Aggregationen;
- Locks oder Ressourcenbindung;
- sensible Datenexfiltration;
- unbegrenzte Resultsets;
- Abfragen gegen Produktionssysteme mit hoher Last.

Deshalb Read-Scope und Kosten berücksichtigen.

## Mutierende Queries

Vor UPDATE/DELETE/INSERT-artigen Aktionen zusätzlich:

1. Zielmenge bestimmen;
2. erwartete Anzahl betroffener Datensätze angeben;
3. Where-/Filter-Bedingung separat prüfen;
4. Transaktions-/Rollbackbedarf bewerten;
5. bei realer Datenbank passende Freigabe einholen.

Besonders gefährlich:

```text
UPDATE / DELETE ohne ausreichend selektiven Filter
Massenänderung ohne Preview
Datenkorrektur ohne Idempotenz-/Retry-Gedanken
```

## ORM / Query Builder

Ein ORM schützt nicht automatisch vor:

- N+1-Abfragen;
- falschen Beziehungen;
- ungewollt breiten Selects;
- fehlender Autorisierung;
- ineffizienter Pagination;
- falscher Transaktionsgrenze.

Generated SQL oder reale Query-Pläne bei relevanten Problemen prüfen.

## Output eines Query-Reviews

```text
Intent
Schema-Evidence
Korrektheitsbefund
Security-Befund
Wirkungs-/Scope-Befund
Performance-Risiken
Freigabe-/Testbedarf
```

## Leitgedanke

> Erst sicher wissen, was eine Query trifft und bewirkt – dann ausführen.