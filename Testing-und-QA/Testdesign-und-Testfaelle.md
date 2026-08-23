# Testdesign und Testfälle

## Grundsatz

> Gute Testfälle entstehen aus Verhalten, Risiken und Invarianten – nicht aus der Struktur des Produktionscodes.

## Quellen für Testideen

- Anforderungen und Akzeptanzkriterien;
- Domäneninvarianten;
- Nutzerflows;
- bekannte Fehler und Regressionen;
- Zustandsmodelle;
- Grenzwerte und Datenbereiche;
- Berechtigungs- und Scope-Grenzen;
- Failure Modes;
- reale Produktions- oder Supporterfahrungen, sofern zulässig.

## Geeignete Techniken

Je nach Problem können helfen:

### Äquivalenzklassen

Eingaben in Gruppen mit voraussichtlich gleichem Verhalten teilen.

### Grenzwertanalyse

Werte direkt an und um relevante Grenzen testen.

### Entscheidungstabellen

Kombinationen mehrerer Bedingungen und erwarteter Ergebnisse systematisch abdecken.

### Zustandsübergänge

Prüfen, welche Aktionen aus welchem Zustand erlaubt sind und welcher Folgezustand entstehen muss.

### Pairwise / kombinatorische Auswahl

Bei vielen Dimensionen gezielt relevante Kombinationen abdecken, statt blind das kartesische Produkt zu testen.

### Property-based Testing

Eigenschaften oder Invarianten für einen Eingaberaum formulieren und viele generierte Beispiele prüfen.

Geeignet insbesondere, wenn eine allgemeine Eigenschaft wichtiger ist als wenige handgeschriebene Beispiele.

## Positive und negative Fälle

Nicht nur den erwarteten Happy Path prüfen.

Je nach Risiko berücksichtigen:

- ungültige Eingaben;
- fehlende Daten;
- Duplikate;
- Grenzen;
- falsche Reihenfolge;
- nicht erlaubte Zustandsübergänge;
- konkurrierende Änderungen;
- partielle Fehler;
- Wiederholung / Idempotenz.

## Oracle / Erwartungswert

Ein Test braucht eine belastbare Erwartung.

Nicht einfach Produktionslogik im Test nachbauen und damit dieselbe Fehlannahme zweimal implementieren.

Bevorzugt:

- fachlich unabhängige erwartete Werte;
- bekannte Beispiele;
- Invarianten;
- Vertragsdefinitionen;
- Referenzimplementierung, wenn sie wirklich unabhängig ist.

## Verhalten statt private Struktur

Tests sollen Refactoring überleben, wenn das zugesicherte Verhalten gleich bleibt.

Private Methoden, interne Call-Reihenfolgen oder konkrete Objektstruktur nur dann prüfen, wenn sie tatsächlich Teil eines relevanten Vertrags oder Risikos sind.

## Brechprobe

Bei kritischen Regeln kann eine kontrollierte Mutation oder Brechprobe prüfen, ob der Test das relevante Fehlverhalten tatsächlich erkennt.

Danach den Ausgangszustand vollständig wiederherstellen und erneut grün verifizieren.