---
name: verification-loop
description: Führt innerhalb eines freigegebenen Scopes einen kontrollierten Arbeiten-Prüfen-Diagnose-Korrigieren-Loop mit klaren Stop-Kriterien aus.
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

## Stoppen und eskalieren, wenn

- eine neue Architektur- oder Produktentscheidung nötig wird;
- notwendiger Kontext fehlt;
- die Ursache außerhalb des Scopes liegt;
- mehrere Versuche ohne belastbare Annäherung scheitern;
- die Prüfung selbst unzuverlässig oder nicht ausführbar ist;
- eine riskante oder irreversible Aktion nötig würde.

## Abschluss

Ein Loop endet erfolgreich nur mit überprüfbarem Nachweis.

Angeben:

- erreichten Ausgangszustand;
- ausgeführte Prüfungen;
- relevante Korrekturschritte;
- verbleibende Risiken oder manuelle Prüfungen.

Ein erfolgreicher Verification Loop ersetzt kein nachgelagertes Review oder Human Gate.