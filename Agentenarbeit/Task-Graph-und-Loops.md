# Task Graph und kontrollierte Loops

## Zweck

Komplexe Agentenarbeit sollte nicht nur als lange lineare Aufgabenliste betrachtet werden.

Ein Task Graph beschreibt, welche Arbeitsschritte voneinander abhängen. Ein Loop beschreibt, wie ein einzelner freigegebener Arbeitsschritt iterativ verbessert und geprüft wird.

## Task Graph

Ein Knoten steht für einen klar abgegrenzten, überprüfbaren Arbeitsschritt.

Eine Kante bedeutet eine echte Abhängigkeit:

```text
A → B
```

bedeutet:

> B darf erst sinnvoll beginnen, wenn A einen definierten Ausgangszustand erreicht hat.

Nicht jede zeitliche Reihenfolge ist eine fachliche Abhängigkeit.

## Gute Knoten

Ein guter Knoten hat:

- klares Ziel;
- definierten Scope;
- benötigte Eingaben;
- erwartetes Ergebnis oder Artefakt;
- prüfbare Akzeptanzbedingungen;
- bekannte Abhängigkeiten;
- Stop- oder Eskalationsbedingungen.

Zu große Knoten wieder zerlegen.

## Vertical Slices bevorzugen

Wenn möglich, Arbeit nicht ausschließlich nach technischen Schichten zerlegen.

Schwächer:

```text
Datenbank
→ Service
→ UI
→ Tests
```

Häufig besser:

```text
kleines überprüfbares Verhalten A
→ vollständiger Nachweis

kleines überprüfbares Verhalten B
→ vollständiger Nachweis
```

Ein Slice soll möglichst einen schmalen, aber vollständigen Weg durch die benötigten Schichten bilden.

## Parallelisierung

Nur Knoten ohne notwendige gegenseitige Abhängigkeit parallel ausführen.

Vor Parallelisierung prüfen:

- bearbeiten die Knoten dieselben Dateien oder Daten?
- teilen sie eine noch nicht festgelegte Schnittstelle?
- hängt die fachliche Entscheidung eines Knotens vom Ergebnis des anderen ab?
- erzeugen parallele Änderungen Merge- oder Konsistenzrisiken?

Parallelität ist kein Qualitätsziel an sich.

## Verifikationsloop innerhalb eines Knotens

Ein freigegebener Knoten darf intern iterieren:

```text
Arbeiten
→ Prüfen
→ bestanden? ── ja → Knoten fertig
      │
     nein
      ↓
   Diagnose
      ↓
   Korrektur
      └────────→ Prüfen
```

Dieser Loop bleibt im Scope des Knotens.

## Stop-Kriterien

Ein Loop darf nicht unbegrenzt laufen.

Mögliche Stop-Kriterien:

- Akzeptanzbedingungen erfüllt;
- festgelegte Anzahl erfolgloser Versuche erreicht;
- Problem erfordert eine neue Architektur- oder Produktentscheidung;
- notwendiger Kontext fehlt;
- Fehler liegt außerhalb des freigegebenen Scopes;
- Prüfung kann technisch nicht zuverlässig durchgeführt werden;
- Risiko steigt über die zulässige Grenze.

In diesen Fällen stoppen und eskalieren statt immer größere Reparaturen zu versuchen.

## Repair am frühesten fehlerhaften Übergang

Wenn ein späterer Knoten scheitert, nicht automatisch den gesamten Graph neu bearbeiten.

Prüfen:

1. Welcher erwartete Eingangszustand ist falsch?
2. Welcher früheste Knoten hätte diesen Zustand liefern müssen?
3. Kann dort mit einem begrenzten Repair-Knoten korrigiert werden?

Reparatur möglichst dort durchführen, wo der falsche Zustand entstanden ist.

## Keine Gate-Flucht durch Loops

Ein Agent darf einen Loop nicht benutzen, um eine neue Spezifikation, Architekturentscheidung oder Scope-Erweiterung eigenmächtig einzuführen.

Wenn die richtige Korrektur außerhalb des freigegebenen Knotens liegt:

> STOP → neue Planung oder Freigabe.

## Nachweis

Ein Knoten gilt nicht als fertig, weil der Agent „fertig“ meldet.

Der definierte Ausgangszustand muss überprüfbar sein, beispielsweise durch:

- automatisierten Test;
- Build oder Linter;
- reproduzierbare Messung;
- Schema- oder Validatorprüfung;
- manuellen Test;
- tatsächlichen Diff gegen den erwarteten Scope.

## Leitgedanke

> Der Graph bestimmt, was ausführbar ist. Der Loop bestimmt, wie innerhalb eines freigegebenen Knotens gelernt und korrigiert wird.