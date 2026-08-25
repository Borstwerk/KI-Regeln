---
name: task-graph
description: Zerlegt komplexe Agentenarbeit in abhängige, überprüfbare Knoten und macht echte Abhängigkeiten, Parallelisierung und Stop-Bedingungen sichtbar. Verwenden bei komplexen Aufgaben mit mehreren abhängigen oder parallelisierbaren Arbeitsschritten.
---

# Task Graph

Nutze `../../Task-Graph-und-Loops.md`.

## Vorgehen

1. Gesamtziel und Scope bestimmen.
2. Arbeit in kleine überprüfbare Knoten zerlegen.
3. Für jeden Knoten Eingaben, Ergebnis und Akzeptanzbedingungen definieren.
4. Echte Abhängigkeiten als Kanten markieren.
5. Unabhängige Knoten identifizieren, die gefahrlos parallel laufen können.
6. Für jeden Knoten Stop- und Eskalationsbedingungen festlegen.

## Bevorzugte Schnitte

Wenn möglich, vertikale Slices statt rein technischer Schichten verwenden.

Ein guter Knoten liefert einen schmalen, aber vollständigen überprüfbaren Fortschritt.

## Parallelisierung

Nicht parallelisieren, wenn Knoten:

- dieselben Dateien oder Daten konkurrierend ändern;
- von derselben noch offenen Entscheidung abhängen;
- eine noch nicht festgelegte Schnittstelle teilen;
- sich fachlich gegenseitig beeinflussen.

## Fehler

Bei einem späteren Fehler den frühesten fehlerhaften Übergang suchen.

Reparatur möglichst dort ansetzen, wo der falsche Zustand entstanden ist, statt den gesamten Graph neu auszuführen.

## Ausgabe

Der Graph soll mindestens enthalten:

- Knotenname;
- Ziel;
- Abhängigkeiten;
- erwartetes Ergebnis;
- Nachweis;
- Stop-/Eskalationsbedingung.

Der Skill implementiert nicht automatisch. Er strukturiert ausführbare Arbeit.