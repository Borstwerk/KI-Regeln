---
name: exploratory-testing
description: Plant und dokumentiert fokussierte explorative Test-Sessions für neue, komplexe oder unzureichend spezifizierte Bereiche. Verwenden, wenn lernendes manuelles Testen zusätzliche Risiken und unbekannte Zustände untersuchen soll. Nicht als zufälliges Herumklicken verwenden.
---

# Exploratory Testing

## Ziel

Mit einer klaren Mission lernend testen und neue Defekte, Risiken und Testideen entdecken.

## Charter

Vor Beginn festlegen:

- Mission;
- Scope;
- zentrale Risiken / Fragen;
- relevante Personas / Rollen;
- Testdaten;
- Heuristiken;
- Zeitbox;
- Umgebung.

## Arbeitsweise

1. Kritische oder unbekannte Bereiche priorisieren.
2. Ausgehend vom Charter gezielt variieren:
   - Eingaben;
   - Reihenfolge;
   - Rollen;
   - Zustände;
   - Grenzen;
   - Recovery;
   - ungewöhnliche Nutzerpfade.
3. Beobachtungen und Überraschungen laufend festhalten.
4. Defekte reproduzierbar dokumentieren.
5. Neue Risiken oder automatisierbare Regressionstests ableiten.
6. Am Ende Charter gegen tatsächliche Coverage prüfen.

## Ausgabe

```text
Charter
Umgebung
untersuchte Pfade
Findings / Defekte
neue Risiken
neue Testideen
offene Fragen
Evidence
```

## Regeln

- keine erfundene Coverage behaupten;
- Session nicht allein nach Zahl gefundener Defekte bewerten;
- sensible Produktionsdaten oder -aktionen nur im lokal erlaubten Scope verwenden;
- Exploratives Testen ergänzt Automatisierung, ersetzt sie nicht automatisch.