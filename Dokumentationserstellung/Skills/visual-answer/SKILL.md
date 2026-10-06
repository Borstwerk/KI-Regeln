---
name: visual-answer
description: Strukturiert komplexe Antworten als visuell schnell erfassbares Artefakt oder Layout mit Kernaussage, Prioritäten, Beziehungen und gestuften Details. Verwenden bei Architektur/Flows, Mehrkriterien-Vergleichen, Hierarchien/Timelines, komplexen Plänen oder Reviews mit vielen Findings; nicht für kurze Faktenantworten, Smalltalk, reine Command-Ausgabe oder wenn der Nutzer Plain Text verlangt.
---

# Visual Answer

Nutze `../../Visuelle-Antworten-und-HTML-Artefakte.md`.

## Ziel

Optimiere die **Time-to-Signal** für Menschen.

Nicht:

> möglichst hübsches HTML

Sondern:

> wichtigste Aussage, Struktur und Handlungsbedarf schneller erfassbar machen.

## Trigger

Nutze den Skill bevorzugt bei:

- Architektur, Flow, Prozess oder Zustandsfolge;
- mindestens drei zusammenhängenden Konzepten, deren Beziehungen erklärt werden müssen;
- Vergleich über mehrere Kriterien;
- Hierarchie oder Timeline;
- Review mit mehreren Findings / Severity- oder Statusklassen;
- Plan mit Phasen, Abhängigkeiten oder Prioritäten;
- ausdrücklichem Wunsch nach visueller oder HTML-Aufbereitung.

## Near-Miss

Nicht triggern bei:

- kurzer Faktenantwort;
- ein bis zwei Sätzen;
- Smalltalk;
- reiner Command-/Logausgabe ohne Erklärbedarf;
- ausdrücklichem Wunsch nach Plain Text;
- bloßer Karten-Dekoration ohne Informationsgewinn.

## Prozess

1. **Kernaussage bestimmen**
   - Was soll nach drei Sekunden verstanden sein?
2. **Informationsform erkennen**
   - Flow, Sequence, Tabelle, Hierarchie, Timeline, Dashboard oder Callout.
3. **2–8 Informationsbereiche planen**
   - eine Einheit = eine erkennbare Frage;
   - Wichtiges zuerst.
4. **Semantische Hierarchie bauen**
   - Priorität, Severity, Empfehlung, Abhängigkeiten und Gates sichtbar machen;
   - Farbe nie als einziges Statussignal.
5. **Content-Fidelity prüfen**
   - keine neuen Claims;
   - Zahlen, Unsicherheit, Status und Gegenargumente erhalten.
6. **Runtime wählen**
   - native HTML-/Artefakterzeugung;
   - spezialisierter Renderer wie `answer-me-with-html`;
   - passendes Plugin/App;
   - sonst strukturierter Markdown-Fallback.
7. **Artefakt erzeugen**
   - bei HTML möglichst selbständig, responsiv und ohne unnötige Remote-Abhängigkeiten.
8. **Verifizieren**
   - Datei vorhanden;
   - Inhalt vollständig;
   - visuelle Prüfung nur behaupten, wenn tatsächlich erfolgt.
9. **Textantwort erhalten**
   - Kernaussage in der normalen Antwort nennen;
   - visuelles Artefakt ergänzt die Antwort, versteckt sie nicht vollständig.

## Qualitätsgate

PASS nur wenn:

- Kernaussage sofort sichtbar;
- zusammengehörige Information gruppiert;
- Prioritäten/Status scanbar;
- Detailtiefe gestuft;
- keine dekorative Wiederholung;
- keine Content-Verluste;
- Runtimegrenzen ehrlich ausgewiesen.

## Runtime-Grenze

Der Skill verlangt keinen bestimmten Renderer.

```text
fachlicher Kern
→ Struktur + visuelle Semantik

Runtime
→ HTML / Artifact / Plugin / Renderer / Markdown
```

`answer-me-with-html` ist eine mögliche Runtime-/Methodenreferenz, keine Pflichtdependency.

## Ausgabe

Mindestens:

- kurze textuelle Kernaussage;
- visuelles Artefakt oder sichtbar strukturierter Fallback;
- bei relevanter Einschränkung: nicht ausgeführte Visual-/Renderprüfung.
