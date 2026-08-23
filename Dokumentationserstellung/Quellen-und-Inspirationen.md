# Quellen und Inspirationen – Dokumentationserstellung

## Zweck

Diese Datei dokumentiert Grundlagen, öffentliche Skills und Werkzeuge, die bei der Entwicklung des Bereichs `Dokumentationserstellung/` berücksichtigt wurden.

Externe Quellen sind Inspiration und Vergleichsbasis, keine automatisch gültigen Regeln.

Mutable Skill-Quellen werden zusätzlich im zentralen `Dokumentation/Quellenregister.md` verfolgt.

Letzte inhaltliche Prüfung dieser Quellenbasis: **2026-08-23**.

## Diátaxis

Quelle:

`https://diataxis.fr/`

Besonders relevant:

`https://diataxis.fr/start-here/`

Nützliche Konzepte:

- vier unterschiedliche Dokumentationsbedürfnisse: Tutorial, How-to, Reference und Explanation;
- Lern- und Arbeitskontext unterscheiden;
- Dokumenttypen nicht unnötig vermischen;
- Reference möglichst an der Struktur des beschriebenen Systems ausrichten.

Übernommen wurde das allgemeine Modell der vier Leserbedürfnisse.

## Google Developer Documentation Style Guide

Quelle:

`https://developers.google.com/style/`

Besonders relevant:

- klare, direkte Sprache;
- aktive Stimme, wenn sie Verantwortlichkeit verdeutlicht;
- zweite Person in Anleitungen;
- Bedingungen vor Aktionen;
- beschreibende Links;
- globale Verständlichkeit und Accessibility;
- lokale Projektregeln haben Vorrang, wenn Klarheit und Konsistenz dies verlangen.

Die Google-spezifischen Sprach- und Formatkonventionen werden nicht vollständig als allgemeine Regeln übernommen.

## Write the Docs – Docs as Code

Quelle:

`https://www.writethedocs.org/guide/docs-as-code/`

Nützliche Konzepte:

- Plain Text und Git;
- Issue- und Reviewprozesse;
- automatisierte Tests für Dokumentation;
- Dokumentation enger mit Produktentwicklung koppeln;
- gemeinsame Ownership von Entwicklern und Dokumentationsverantwortlichen.

## The Good Docs Project

Quelle:

`https://www.thegooddocsproject.dev/template`

Nützliche Vorlagen und Konzepte unter anderem für:

- README;
- Quickstart;
- Tutorial;
- How-to;
- Reference;
- Concept / Explanation;
- Installation;
- Troubleshooting;
- Release Notes;
- Style Guides.

Die Vorlagen dienen als Strukturinspiration. Sie werden nicht als starres universelles Schema behandelt.

## Vale

Dokumentation:

`https://docs.vale.sh/`

Agent Skills:

`https://vale.sh/skills`

Nützliche Konzepte:

- prose linting als technischer Teil eines Docs-Harness;
- projektlokale Stil- und Terminologieregeln automatisierbar machen;
- Markup bewusst behandeln;
- Linting, Fix, Triage, Vocabulary und CI als getrennte Aufgaben;
- Linter nicht durch Regelabschwächung „grün machen“.

Vale wird als mögliches Werkzeug eingeordnet, nicht als verpflichtender Bestandteil jedes Projekts.

## Matteo Collina – `documentation`

Quelle:

`https://github.com/mcollina/skills/blob/main/skills/documentation/SKILL.md`

Beobachteter Stand am 2026-08-23:

- Branch: `main`
- Blob SHA: `dae5144584a07b60287eac57f0786665b38b3559`

Nützliche Konzepte:

- Diátaxis-Klassifikation vor dem Schreiben;
- typspezifische Validierungsfragen;
- Tutorial, How-to, Reference und Explanation klar trennen;
- Dokumente über Querverweise integrieren statt Modi innerhalb eines Abschnitts zu vermischen.

## mblode – `docs-writing`

Quelle:

`https://github.com/mblode/agent-skills/blob/main/skills/docs-writing/SKILL.md`

Beobachteter Stand am 2026-08-23:

- Branch: `main`
- Blob SHA: `1d9a8530f20ae6dda523fc87e85a66e24ed49473`
- Skill beschreibt aktuell 48 Regeln in 9 Kategorien.

Nützliche Konzepte:

- Schreib- und Auditmodus trennen;
- Dokumenttyp vor Regelanwendung klassifizieren;
- Regeln nach Relevanz und Schweregrad progressiv laden;
- Beispiele ausführen, Links prüfen und Parameter gegen Implementierung verifizieren;
- Review nicht durch ungefragten Rewrite ersetzen.

## JPeetz / Skill Foundry – `technical-documentation`

Quelle:

`https://github.com/JPeetz/agent-skills/blob/main/technical-documentation/SKILL.md`

Beobachteter Stand am 2026-08-23:

- Branch: `main`
- Blob SHA: `3616059286b7d7f84adc5e91ba1498114aeb53f1`
- im Skill ausgewiesene Version: `1.0.0`

Nützliche Konzepte:

- Artefakttypen mit unterschiedlicher Zielgruppe und Lifecycle unterscheiden;
- README, ADR, API-Dokumentation, Runbook, Onboarding, Changelog und Knowledge Base unterschiedlich behandeln;
- Dokumentationsaudit nach fachlicher Auswirkung priorisieren;
- Source-of-Truth- und Wartungsfragen in technische Dokumentation integrieren.

Einzelne konkrete Vorgaben dieses Skills, etwa universelle Verzeichnisnamen, feste Reviewintervalle oder technologiespezifische API-Konventionen, werden nicht automatisch übernommen.

## Eigene Synthese

Aus der Recherche wurde insbesondere diese Trennung entwickelt:

```text
Dokumentationsmodus
Tutorial / How-to / Reference / Explanation
        ≠
Artefakttyp
README / ADR / Runbook / API Docs / ...
        ≠
Fachliche Source of Truth
Code / Schema / Entscheidung / Betrieb / ...
        ≠
Qualitätssicherung
Review / Tests / Links / Linter / Driftprüfung
```

Diese Vierfachtrennung ist eine Synthese dieses Repositories und wird nicht einer einzelnen externen Quelle zugeschrieben.

## Übernahmekriterien

Externe Dokumentationsregeln werden bevorzugt übernommen, wenn sie:

1. fachliche Korrektheit erhöhen;
2. Leserbedürfnisse klarer trennen;
3. Dokumentationsdrift reduzieren;
4. Verifikation und Wartbarkeit verbessern;
5. tool- oder projektspezifische Vorgaben sinnvoll generalisieren lassen;
6. nicht bloß mehr Dokumentation erzeugen.

## Leitgedanke

> Gute Dokumentation ist ein gepflegtes Interface zwischen Systemwissen und Leseraufgabe – kein Textarchiv.
