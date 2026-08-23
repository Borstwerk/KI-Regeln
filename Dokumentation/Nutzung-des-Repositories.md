# Nutzung des Repositories

## Zweck

Dieses Dokument erklärt, wie `KI-Regeln` sinnvoll in echten Projekten eingesetzt wird.

Das Repository ist keine automatische Master-Steuerung für alle Projekte. Es ist eine zentrale Bibliothek allgemeiner Regeln, Arbeitsweisen und Skills.

## Grundprinzip

> Allgemeine Arbeitsweise zentral, konkrete Wahrheit lokal.

Das bedeutet:

- zentrale Regeln beschreiben **wie** gearbeitet wird;
- Projekte definieren **was** konkret gebaut, geschrieben, geprüft, erzeugt, recherchiert oder entschieden werden soll;
- lokale Projektregeln haben Vorrang vor allgemeinen Regeln, wenn sie verbindlich sind.

## Was das Repository liefert

Das Repository liefert beispielsweise:

- Kommunikations- und Zusammenarbeitsregeln;
- Denk- und Problemlösungsmuster;
- Reflexions- und Lernmethoden;
- Agentenarbeitsweisen;
- Recherche-, Websuche- und Deep-Research-Methoden;
- Schreibregeln;
- Bildarbeitsregeln;
- Webdesign- und Frontend-Regeln;
- Programmier-Skills.

## Was das Repository nicht liefert

Das Repository liefert nicht automatisch:

- Produktanforderungen;
- Projektarchitektur;
- Fachbegriffe eines konkreten Systems;
- projektspezifische Research-Fragen oder interne Quellen;
- Serienkanon;
- Charakterdesigns;
- Markenidentität oder konkrete `DESIGN.md`;
- reale Website-Inhalte;
- lokale Freigabeprozesse;
- reale Projektziele;
- persönliche Profile oder individuelle Entwicklungsverläufe.

Diese Dinge bleiben lokal im Projekt oder beim jeweiligen Nutzer.

## Empfohlenes Nutzungsmodell

Ein Projekt soll gezielt nur die benötigten Regeln und Skills übernehmen.

Nicht empfehlenswert:

- dem Agenten das komplette Repository ungefiltert als Kontext zu geben;
- alle Skills in jedes Projekt zu übernehmen;
- allgemeine Regeln als Ersatz für lokale Spezifikationen zu behandeln;
- automatisch immer die neueste zentrale Version einzuspielen.

Empfohlen:

1. Projektart und Aufgabe bestimmen;
2. passende zentrale Regeln und Skills auswählen;
3. lokale Projektregeln ergänzen;
4. verwendete zentrale Version dokumentieren;
5. Aktualisierungen bewusst prüfen und übernehmen.

## Beispiel: Softwareprojekt

Ein Softwareprojekt könnte beispielsweise verwenden:

- `Grundlagen/Zusammenarbeit-mit-KI.md`
- `Agentenarbeit/Skills/context-engineering/SKILL.md`
- `Agentenarbeit/Skills/delegation-contract/SKILL.md`
- `Agentenarbeit/Skills/verification-loop/SKILL.md`
- `Programmieren/Skills/domain-modeling/SKILL.md`
- `Programmieren/Skills/tdd/SKILL.md`
- `Programmieren/Skills/diagnose/SKILL.md`
- `Programmieren/Skills/code-review/SKILL.md`

Zusätzlich bleiben lokal beispielsweise:

- Architektur;
- Releaseprozess;
- Testumgebung;
- Freigabegates;
- Produktanforderungen.

## Beispiel: Research- oder Analyseprojekt

Je nach Tiefe können sinnvoll sein:

- `Grundlagen/Zusammenarbeit-mit-KI.md`
- `Agentenarbeit/Skills/context-engineering/SKILL.md`
- `Recherche/Skills/web-search/SKILL.md`
- `Recherche/Skills/research-plan/SKILL.md`
- `Recherche/Skills/deep-research/SKILL.md`
- `Recherche/Skills/source-evaluation/SKILL.md`
- `Recherche/Skills/claim-verification/SKILL.md`
- `Recherche/Skills/research-synthesis/SKILL.md`
- `Recherche/Skills/citation-audit/SKILL.md`

Ein möglicher Deep-Research-Ablauf:

```text
Hauptfrage
→ research-plan
→ deep-research
→ source-evaluation bei wichtigen Quellen
→ research-synthesis
→ claim-verification für zentrale oder strittige Claims
→ citation-audit
→ Final
```

Für eine kleine aktuelle Faktenfrage kann dagegen `web-search` allein genügen.

Zusätzlich lokal bleiben beispielsweise:

- konkrete Research-Frage;
- gewünschte Entscheidung oder Zielgruppe;
- interne Dokumente und Daten;
- zulässige Quellenbereiche;
- Freshness-Anforderungen;
- fachliche Spezialkriterien;
- Ergebnisformat.

## Beispiel: Schreibprojekt

Ein Schreibprojekt könnte verwenden:

- `Grundlagen/Zusammenarbeit-mit-KI.md`
- `Schreiben/Skills/natuerliches-schreiben/SKILL.md`
- `Schreiben/Skills/kreatives-schreiben/SKILL.md`
- `Schreiben/Skills/stilreview/SKILL.md`

Zusätzlich lokal:

- Figuren;
- Weltlogik;
- Serienkanon;
- Zielgruppe;
- Tonalität;
- Kapitelplanung.

## Beispiel: Bildprojekt

Ein Bildprojekt könnte verwenden:

- `Grundlagen/Zusammenarbeit-mit-KI.md`
- `Bildarbeit/Skills/bild-prebrief/SKILL.md`
- `Bildarbeit/Skills/entitaetsbibel/SKILL.md`
- `Bildarbeit/Skills/serien-kontinuitaetscheck/SKILL.md`
- `Bildarbeit/Skills/bildreview/SKILL.md`

Zusätzlich lokal:

- Charakterreferenzen;
- Stilanker;
- Kanonbilder;
- Szenenlisten;
- Kontinuitätsdetails.

## Beispiel: Webprojekt

Ein neues Webprojekt könnte je nach Umfang verwenden:

- `Grundlagen/Zusammenarbeit-mit-KI.md`
- `Agentenarbeit/Skills/context-engineering/SKILL.md`
- `Webentwicklung/Skills/frontend-design/SKILL.md`
- `Webentwicklung/Skills/design-system/SKILL.md`
- `Webentwicklung/Skills/greybox/SKILL.md`
- `Webentwicklung/Skills/web-content/SKILL.md`
- `Webentwicklung/Skills/accessibility-review/SKILL.md`
- `Webentwicklung/Skills/frontend-performance/SKILL.md`
- `Webentwicklung/Skills/visual-verification/SKILL.md`
- `Webentwicklung/Skills/web-design-review/SKILL.md`
- bei komplexerer Logik zusätzlich passende Skills aus `Programmieren/`.

Ein möglicher Ablauf:

```text
Produkt / Zielgruppe
→ frontend-design
→ design-system
→ greybox
→ web-content
→ Implementierung
→ accessibility-review
→ frontend-performance
→ visual-verification
→ web-design-review
```

Zusätzlich lokal:

- Marke und Designrichtung;
- `DESIGN.md` oder vergleichbare Designquelle;
- tatsächlicher Content;
- Informationsarchitektur;
- Framework und Komponentenbibliothek;
- Browseranforderungen;
- Performancebudgets;
- Hosting, Release und Deployment.

Nicht jedes Webprojekt benötigt alle Skills. Für eine kleine bestehende Seite kann beispielsweise `visual-verification → web-design-review → gezielte Korrektur` genügen.

## Beispiel: Reflexion und Selbstverbesserung

Je nach Ziel können sinnvoll sein:

- `Grundlagen/Mensch-KI-Interaktion.md`
- `Grundlagen/Vertrauen-und-Denkautonomie.md`
- `Arbeitsweisen/Skills/reflektierender-dialog/SKILL.md`
- `Arbeitsweisen/Skills/entscheidungsunterstuetzung/SKILL.md`
- `Arbeitsweisen/Skills/ziel-reflexions-loop/SKILL.md`

Persönliche Notizen und individuelle Verläufe bleiben außerhalb des zentralen Regelwerks.

## Skill-Manifest pro Projekt

Für Projekte empfiehlt sich eine lokale Datei, die festhält, welche zentrale Version und welche Regeln beziehungsweise Skills verwendet werden.

Vorlage: `../Vorlagen/ki-regeln.template.yml`

Beispiel:

```yaml
source: Borstwerk/KI-Regeln
version: v2026.08

rules:
  - Grundlagen/Zusammenarbeit-mit-KI.md

skills:
  - Agentenarbeit/Skills/context-engineering
  - Agentenarbeit/Skills/delegation-contract
  - Agentenarbeit/Skills/verification-loop
  - Programmieren/Skills/domain-modeling
  - Programmieren/Skills/tdd
  - Programmieren/Skills/diagnose
  - Programmieren/Skills/code-review
```

## Verteilprinzip

- **Zentrale Fassung** = allgemeine kanonische Arbeitsweise;
- **lokale Fassung** = projektspezifisch übernommene Kopie oder Adapter;
- **lokale Projektregeln** = konkrete Wahrheit des Projekts.

## Updates bewusst übernehmen

Ein Projekt sollte nicht automatisch auf jede Änderung von `main` springen.

Besser:

```text
neue zentrale Version
→ Changelog lesen
→ relevante Diffs prüfen
→ lokale Auswirkungen bewerten
→ bewusst übernehmen
```

Das verhindert, dass sich Agentenverhalten in laufenden Projekten unbemerkt ändert.

## Wichtige Warnung

Ein Skill ersetzt niemals:

- eine Spezifikation;
- eine Architekturentscheidung;
- eine Research-Frage oder fachliche Definition;
- einen Serienkanon;
- eine Marken- oder Designentscheidung;
- eine Projektfreigabe;
- menschliche Verantwortung.

## Leitgedanke

> Nicht möglichst viele Regeln laden, sondern die richtigen Regeln für die aktuelle Aufgabe.