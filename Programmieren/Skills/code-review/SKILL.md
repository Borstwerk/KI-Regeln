---
name: code-review
description: Strukturiertes Code-Review für KI-gestützte Softwarearbeit. Verwenden, um einen Diff gegen festen Ausgangspunkt, Anforderung, freigegebenen Plan und Repository-Standards zu prüfen.
---

# Code Review

Ein grüner Testlauf ersetzt dieses Review nicht.

## 1. Ausgangspunkt festnageln

Vor dem Review festhalten:

- Basis-Commit beziehungsweise Merge-Base;
- Head;
- zugehörige Anforderung oder Aufgabenquelle;
- freigegebener Plan, soweit vorhanden;
- relevante Architektur-, Entscheidungs- und Testdokumente.

Wenn Basis oder Spezifikation unklar ist, zuerst klären beziehungsweise ausdrücklich als Review-Grenze benennen.

## 2. Diff tatsächlich lesen

Nicht nur Abschlussbericht oder Testzahl bewerten.

Prüfen:

- welche Dateien wirklich geändert wurden;
- ob nicht geplante Bereiche berührt wurden;
- ob neue Abhängigkeiten oder öffentliche Schnittstellen entstanden sind;
- ob Dateiformate, Persistenz, Migration oder Datenpfade betroffen sind;
- ob UI, Domain, Persistenz und veröffentlichte Projektionen konsistent bleiben;
- ob Dokumentation angepasst werden muss.

## 3. Zwei getrennte Review-Achsen

### A – Anforderung / Spezifikation

Für jedes Akzeptanzkriterium prüfen:

- vollständig umgesetzt;
- teilweise umgesetzt;
- fehlt;
- Verhalten implementiert, aber fachlich anders als gefordert;
- zusätzliches Verhalten ohne Auftrag beziehungsweise Scope Creep.

Akzeptanzkriterien jeweils einem konkreten Nachweis zuordnen.

### B – Code / Repository-Standards

Prüfen:

- KISS und bestehende Architektur;
- keine unnötige Generalisierung;
- keine zweite fachliche Wahrheit;
- keine unnötige Duplikation zentraler Definitionen;
- keine versteckten Heuristiken;
- keine Validierungsabschwächung;
- sprechende Begriffe aus dem Fachmodell;
- keine unnötigen Repository-, Service- oder Manager-Schichten;
- keine Seiteneffekte außerhalb des vereinbarten Slices.

Code-Smells als Hinweise benennen, aber nicht automatisch zu Blockern erklären. Projektanforderungen und gültige Entscheidungen haben Vorrang vor allgemeinen Stilpräferenzen.

## 4. Tests prüfen, nicht nur zählen

Für kritische Zusicherungen prüfen:

- testet der Test Verhalten oder nur Implementierungsform;
- könnte er trotz gebrochener Anforderung grün bleiben;
- stammen erwartete Werte aus einer unabhängigen Quelle;
- decken Persistenz- oder Migrationstests echte Pfade ab;
- wurde bei riskanten Eigenschaften eine Brechprobe durchgeführt;
- würde der Test die behauptete Mutation tatsächlich erkennen.

Eine große Testzahl ist kein Qualitätsnachweis, wenn die entscheidende Eigenschaft nicht geschützt wird.

## 5. Daten-, Sicherheits- und Historienrisiken

Besonders streng prüfen bei:

- Schemaänderungen;
- Migrationen;
- veröffentlichten oder eingefrorenen Zuständen;
- Ableitung neuer Arbeitsstände;
- Backup und Restore;
- Hashes oder Artefakten;
- Authentifizierung und Berechtigungen;
- Nutzereingaben, die still überschrieben werden könnten.

Keine historische Neuinterpretation oder stille Datenkorrektur ohne ausdrückliche Anforderung.

## 6. Scope Creep

Prüfen, ob der Diff Arbeiten enthält, die nicht für die Anforderung notwendig sind.

Typische Fälle:

- vorsorgliche Refactorings;
- neue Abstraktionen ohne aktuellen Bedarf;
- zusätzliche Funktionen;
- Änderungen an Nachbarmodulen;
- neue externe Abhängigkeiten;
- Format- oder Strukturänderungen weit außerhalb des Slices.

Scope Creep ist nicht automatisch falsch, muss aber bewusst entschieden statt unbemerkt mitgeliefert werden.

## 7. Ausgabe

Funde getrennt ausgeben als:

- **Blocker** – Anforderung verletzt, falsches Verhalten, relevantes Daten- oder Sicherheitsrisiko;
- **Sollte korrigiert werden** – relevante Qualitäts- oder Wartbarkeitsabweichung;
- **Hinweis** – kein Freigabehindernis.

Danach eine kurze Nachweismatrix:

```text
Akzeptanzkriterium
→ Code / Verhalten
→ automatischer Test
→ manuelle Prüfung, falls nötig
```

Abschließend ausdrücklich sagen, ob das Review aus fachlich-technischer Sicht bestanden ist oder welche Punkte offen bleiben.

Keine Freigabe behaupten, solange notwendige manuelle Prüfungen noch offen sind.