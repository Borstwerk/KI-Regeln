---
name: verification-loop
description: Führt innerhalb eines freigegebenen Scopes einen kontrollierten Arbeiten-Prüfen-Diagnose-Korrigieren-Loop mit klaren Stop-Kriterien aus. Verwenden bei iterativer Umsetzung, wenn nach jedem Änderungsschritt reproduzierbare Nachweise möglich sind.
---

# Verification Loop

Nutze `../../Task-Graph-und-Loops.md` und `../../Human-Gates-und-Freigaben.md`.

## Voraussetzungen

Vor dem Start müssen klar sein:

- freigegebener Scope;
- erwarteter Ausgangszustand;
- konkrete Nachweise;
- Stop- und Eskalationsbedingungen.

## Loop

```text
Arbeiten
→ Prüfen
→ bestanden? → fertig
→ nicht bestanden → Diagnose
→ Korrektur
→ erneut prüfen
```

## Regeln

- Nur innerhalb des freigegebenen Scopes korrigieren.
- Fehlerursache vor Symptombehandlung prüfen.
- Tests oder Validierungen nicht abschwächen, um den Loop zu beenden.
- Fehlende Spezifikation nicht eigenmächtig ersetzen.
- Einen nicht ausgeführten Nachweis nicht als bestanden behandeln.
- Nach jeder Korrektur denselben relevanten Nachweis erneut ausführen.

## Fresh Evidence vor Completion Claims

Eine Erfolgs-, Fertig- oder Pass-Aussage benötigt einen **aktuellen Nachweis für genau den behaupteten Zustand**.

Nicht ausreichend sind:

- ein Testlauf vor der letzten relevanten Änderung;
- ein früherer CI-Lauf;
- nur ein Teilcheck, wenn der Claim die vollständige Prüfung betrifft;
- die Erfolgsmeldung eines anderen Agenten ohne unabhängige Verifikation;
- „sollte jetzt gehen“, „wahrscheinlich grün“ oder ähnliche Extrapolation.

Vor einem Completion Claim:

1. bestimmen, welcher Nachweis den Claim tatsächlich trägt;
2. diesen Nachweis frisch und vollständig ausführen;
3. Ergebnis, Fehlerzahl und Exit Status lesen;
4. prüfen, ob die Evidence den Claim wirklich stützt;
5. Claim auf die tatsächlich verifizierte Aussage begrenzen.

Wenn ein Nachweis nicht ausführbar ist, Status als `blocked`, `not run` oder entsprechend lokal definiert melden – nicht als bestanden.

## Stoppen und eskalieren, wenn

- eine neue Architektur- oder Produktentscheidung nötig wird;
- notwendiger Kontext fehlt;
- die Ursache außerhalb des Scopes liegt;
- mehrere Versuche ohne belastbare Annäherung scheitern;
- die Prüfung selbst unzuverlässig oder nicht ausführbar ist;
- eine riskante oder irreversible Aktion nötig würde.

## Abschluss

Ein Loop endet erfolgreich nur mit überprüfbarem, aktuellem Nachweis.

Angeben:

- erreichten Ausgangszustand;
- frisch ausgeführte Prüfungen;
- relevante Korrekturschritte;
- nicht ausgeführte oder blockierte Prüfungen;
- verbleibende Risiken oder manuelle Prüfungen.

Ein erfolgreicher Verification Loop ersetzt kein nachgelagertes Review oder Human Gate.