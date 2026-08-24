# HTTP API Design

## Basis

HTTP APIs sollen HTTP-Semantik bewusst verwenden statt sie nur als Transporttunnel zu behandeln.

Die lokale Schnittstelle bestimmt Ressourcen und Aktionen; RFC 9110 bleibt Source of Truth für Method-, Status- und Headersemantik.

## Operationsdesign

Für jede Operation mindestens definieren:

- Consumer-Task;
- Methode und URI;
- Requestparameter und Body;
- Response und Status;
- Fehler;
- Auth-/Scope-/Tenant-Grenzen;
- Idempotenz und Retry;
- Concurrency-/Precondition-Verhalten;
- Pagination/Ordering bei Collections;
- Versionierungs-/Deprecationstatus.

## Ressourcen und Aktionen

Ressourcenorientierte Formen sind ein guter Default, aber keine Religion. Fachliche Aktionen oder Long-running Operations dürfen explizit modelliert werden, wenn CRUD die Bedeutung verschleiern würde.

Nicht die Datenbanktabellen 1:1 in URLs oder JSON spiegeln, nur weil es technisch bequem ist.

## Safe und idempotent

HTTP-Semantik unterscheidet safe und idempotent. Retryentscheidungen müssen zur tatsächlichen Operation passen.

Ein POST kann über einen expliziten Idempotency-Contract faktisch wiederholbar gemacht werden; das ist dann Teil des API-Vertrags und nicht nur Implementierungsdetail.

## Collections

Definieren:

- stabile Sortierung;
- Paginationstil;
- Cursor-/Offset-Semantik;
- Filter und erlaubte Werte;
- Sortierfelder;
- leere Ergebnisse;
- Counts: exakt, approximativ oder nicht vorhanden;
- Änderungen während der Traversierung, wenn relevant.

## Fehler

Statuscode und strukturierter Fehler sollen dem Consumer helfen zu entscheiden:

```text
retry
reauth
request korrigieren
conflict auflösen
abwarten
nicht erneut versuchen
```

## Deprecation

HTTP bietet standardisierte Mechanismen wie `Deprecation` und ergänzend `Sunset`/Links. Ein deprecated Endpoint bleibt zunächst funktionsfähig; Deprecation ist Kommunikation und Lifecycle, nicht sofortige Entfernung.

## Machine-readable Contract

OpenAPI ist ein geeigneter Standard für maschinenlesbare HTTP-Verträge. Ob die Beschreibung handgeschrieben, generiert oder hybrid gepflegt wird, ist eine lokale Toolingentscheidung. Entscheidend ist, dass die kanonische Contract-Quelle eindeutig ist und Drift geprüft wird.

## Leitgedanke

> HTTP-Status und -Methoden sind Consumer-Semantik, nicht Dekoration.