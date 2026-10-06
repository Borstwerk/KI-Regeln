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

1. **Kernaussage und Dringlichkeit bestimmen**
   - Was soll nach drei Sekunden verstanden sein?
   - Gibt es Incident-/Meeting-/Zeitdruck, der zuerst eine direkte Entscheidung verlangt?
2. **Kleinste ausreichende Eskalationsstufe wählen**
   - Level 0: Direct;
   - Level 1: Compact Visual;
   - Level 2: Visual Explanation;
   - Level 3: Visual Artifact.
3. **Informationsform erkennen**
   - Flow, Sequence, Tabelle, Hierarchie, Timeline, Dashboard, Chart oder Callout.
4. **Nutzungsform bestimmen**
   - Monitoring → Dashboard;
   - Argument + Evidence → Report/Explanation;
   - Print → One-Pager;
   - Live Talk → Slides-Workflow;
   - Exploration → explorable Artifact.
5. **Semantische Hierarchie bauen**
   - Wichtiges zuerst;
   - eine visuelle Einheit = eine erkennbare Frage;
   - Priorität, Severity, Empfehlung, Abhängigkeiten und Gates sichtbar machen;
   - Farbe nie als einziges Statussignal.
6. **Content- und Visual-Fidelity prüfen**
   - keine neuen Claims;
   - Zahlen, Unsicherheit, Status und Gegenargumente erhalten;
   - keine fehlenden Werte als Null erfinden;
   - Titel, Einheiten, Achsen und Proportionen müssen die Daten ehrlich tragen.
7. **Interaktion gaten**
   - nur wenn `Reader Question → User Action → sichtbare neue Erkenntnis`;
   - Kernaussage muss im Defaultzustand verständlich sein;
   - erfasste Nutzerentscheidungen/Edits brauchen einen nutzbaren Export-/Übergabepfad.
8. **Runtime wählen**
   - native Visual-/HTML-/Artefakterzeugung;
   - spezialisierter Renderer wie `answer-me-with-html`;
   - passendes Plugin/App;
   - sonst strukturierter Markdown-Fallback.
9. **Artefakt erzeugen**
   - bei HTML möglichst selbständig, responsiv und ohne unnötige Remote-Abhängigkeiten.
10. **Verifizieren**
   - Datei vorhanden;
   - Inhalt vollständig;
   - Interaktion funktional;
   - visuelle Prüfung nur behaupten, wenn tatsächlich erfolgt.
11. **Textantwort erhalten**
   - Kernaussage in der normalen Antwort nennen;
   - visuelles Artefakt ergänzt die Antwort, versteckt sie nicht vollständig.

## Qualitätsgate

PASS nur wenn:

- Eskalationsstufe zur Aufgabe passt;
- Kernaussage sofort sichtbar;
- zusammengehörige Information gruppiert;
- Prioritäten/Status scanbar;
- Detailtiefe gestuft;
- keine dekorative Wiederholung;
- keine Content-Verluste;
- Daten/Charts visuell ehrlich bleiben;
- Interaktion eine echte Leserfrage beantwortet;
- Hauptaussage ohne Interaktion zugänglich bleibt;
- Runtimegrenzen ehrlich ausgewiesen.

Wenn dauerhafte App-Funktion, Auth, Multi-User-State oder produktive CRUD-Workflows nötig werden, an Web-/Softwareentwicklung routen statt `visual-answer` zum Mini-Produkt auszudehnen.

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
