# Test-Seams, Doubles und reale Abhängigkeiten

## Grundsatz

> Kontrolliere im Test nur das, was kontrolliert werden muss. Prüfe reales Verhalten dort, wo genau dieses Verhalten Teil des Risikos ist.

## Test Seam

Ein Test Seam ist eine bewusst kontrollierbare Grenze, an der eine Abhängigkeit für Tests ersetzt, konfiguriert oder beobachtet werden kann.

Gute Seams entstehen zum Beispiel durch:

- Dependency Injection;
- Ports / Interfaces;
- konfigurierbare Clock- oder Random-Quellen;
- austauschbare Transportadapter;
- kontrollierbare Dateisystem- oder Netzwerkgrenzen.

Produktionsarchitektur nicht ausschließlich für Test-Mocking verbiegen. Testbarkeit ist ein Qualitätsaspekt, aber nicht der einzige Architekturtreiber.

## Test Doubles

`Test Double` ist der Oberbegriff. Je nach Zweck können verwendet werden:

- Dummy;
- Stub;
- Fake;
- Spy;
- Mock.

Nicht jedes Double ist ein Mock.

## Wann ein Double sinnvoll ist

Typische Gründe:

- externe Abhängigkeit ist langsam oder nicht deterministisch;
- echte Nutzung wäre teuer, rate-limited oder unerwünscht;
- Test darf keine reale externe Aktion auslösen;
- schwer reproduzierbare Fehlerantworten sollen kontrolliert erzeugt werden;
- die eigene Einheit soll isoliert diagnostizierbar sein;
- Zeit, Zufall oder Umgebung müssen deterministisch kontrolliert werden.

## Wann reale Abhängigkeit wichtig ist

Wenn das reale Verhalten selbst Teil des Risikos ist, sollte eine geeignete Testebene mit realer oder realitätsnaher Dependency existieren.

Beispiele:

- Datenbanktreiber ↔ echte Datenbankengine;
- Serialisierung und Framework-Binding;
- Message Broker Semantik;
- Transaktionen;
- Dateisystemverhalten;
- eigene Service-zu-Service-Integration.

Temporäre isolierte Services oder Container können dafür geeigneter sein als gemeinsam genutzte Testumgebungen.

## Keine universelle Mocking-Doktrin

Nicht zentral festschreiben:

- „interne Services niemals mocken“;
- „externe Services immer mocken“;
- „alle Unit Tests müssen solitary sein“;
- „alle Unit Tests müssen reale Collaborators verwenden“.

Die richtige Entscheidung hängt vom Testziel und Risiko ab.

## Drift von Doubles

Ein Double kann grün bleiben, während die reale Dependency ihren Vertrag verändert hat.

Gegenmaßnahmen können sein:

- Contract Tests;
- Schema-/Spec-Validierung;
- periodische Tests gegen reale Sandbox-/Testsysteme;
- generierte Clients/Stubs aus kanonischen Verträgen;
- gezielte Vergleichstests.

## Leitfrage

> Prüfen wir gerade unsere Logik – oder behaupten wir durch ein Double versehentlich etwas über eine reale Dependency, das wir gar nicht verifiziert haben?