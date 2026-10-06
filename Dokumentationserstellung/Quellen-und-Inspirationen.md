# Quellen und Inspirationen – Dokumentationserstellung

## Zweck

Diese Datei dokumentiert Grundlagen, öffentliche Skills und Werkzeuge, die bei der Entwicklung des Bereichs `Dokumentationserstellung/` berücksichtigt wurden.

Externe Quellen sind Inspiration und Vergleichsbasis, keine automatisch gültigen Regeln.

Mutable Skill-Quellen werden zusätzlich im zentralen `Dokumentation/Quellenregister.md` verfolgt.

Letzte inhaltliche Prüfung dieser Quellenbasis: **2026-10-06**.

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

## QingYunA – `answer-me-with-html`

Quelle:

`https://github.com/QingYunA/answer-me-with-html`

Geprüfter Repository-Stand:

- Commit: `f3082c912c1637d7eff38e7a4c356545b756c75f`
- Skill-Blob: `54a48115184f6c8625c633890a0bb5c004cbf90a`
- Lizenz des Codes am geprüften Stand: MIT

Methodisch relevant sind insbesondere:

- visuelle Ausgabe nur dann wählen, wenn Informationsstruktur davon profitiert;
- Flows, Vergleiche, Hierarchien, Timelines und Reviews nach Informationsform statt nach Dekoration strukturieren;
- Kernaussage zuerst und eine erkennbare Aufgabe pro Panel;
- Modell schreibt primär Inhalt und Beziehungen, ein Renderer kann Layout und Diagrammgeometrie übernehmen;
- kurze Antworten bewusst in Plain Text lassen;
- strukturierte Markdown-/DSL-Ausgabe als mögliche Zwischenschicht vor einem deterministischen Renderer;
- Renderfehler als konkrete reparierbare Evidence zurückmelden.

Nicht als lokale Wahrheit übernommen werden:

- Always-on-Modus;
- eine Pflicht zur `am`-CLI;
- konkrete Themes oder Syntax;
- konkrete Token-, Zeit- oder Kosten-Benchmarks;
- die Annahme, HTML sei für jede Antwort besser.

KI-Regeln generalisiert daraus einen provider- und rendererunabhängigen `visual-answer`-Skill. `answer-me-with-html` bleibt eine mögliche Runtime-Implementierung, keine Dependency.

Am 2026-10-06 wurden zusätzlich drei lokale Zero-Install-A/B-Vergleiche durchgeführt. Die HTML-Fassung wurde vom menschlichen Reviewer bei Architektur/Überblick, Mehrkriterien-Entscheidung und Multi-Finding-Review jeweils bevorzugt. Diese Beobachtung wird als explorative Human-Evidence behandelt, nicht als formaler Benchmark.

Details: `Visual-Answer-Explorativer-AB-Test-2026-10-06.md`.

## Maksim-Burtsev – `visual-teacher`

Quelle:

`https://github.com/Maksim-Burtsev/visual-teacher`

Geprüfter Repository-Stand:

- Commit: `a8bd4382a79f47b3388ac4d48a40470317ddafb5`
- Skill-Blob: `5d590a7b17267ebd8d10d095690cb2ed78ae0937`
- Decision-Rubric-Blob: `2697b30c8de31aa89ece0fb3cb4aa4c0fa30799b`
- Lizenz: MIT

Methodisch relevant:

- visuelle Eskalation statt binärem „Text oder HTML“;
- kleinste ausreichende Visualisierung;
- Visualisierung nach Erklärform statt Themenliste;
- Whiteboard-Test für Reihenfolge, Topologie, Zustände, Entscheidungen und Kausalität;
- Urgency Override: bei Incident/Meeting Entscheidung zuerst;
- harte Negativtrigger für kurze, lokale oder ausdrücklich textuelle Fragen;
- Trigger-Evals getrennt von Outputqualität.

Nicht übernommen:

- konkrete Punktwerte und Thresholds des Upstream-Rubrics;
- Mermaid als universelle Pflicht;
- konkrete Level-Namen als Produkt-API;
- Upstream-Benchmarks als lokale Evidence.

KI-Regeln übernimmt das Prinzip als Level 0–3 und evaluiert die eigene Triggerlogik separat.

## Joshua David Thomas – `html-artifacts`

Quelle:

`https://github.com/joshuadavidthomas/agent-skills/tree/main/html-artifacts`

Geprüfter Repository-Stand:

- Commit: `516dee7a422b90937b2958d11c03694154ab9c09`
- Skill-Blob: `649206d0fa6213b99c7ff13026704fc5c8d84810`
- Lizenz: MIT

Methodisch relevant:

- Source/Evidence vor Artefaktdesign;
- die statische Defaultansicht muss die Hauptgeschichte vollständig tragen;
- Interaktion nur, wenn sie eine konkrete Leserfrage beantwortet;
- eigenständige Offline-Datei als robuste Defaultform;
- keine Veröffentlichung ohne ausdrücklichen Auftrag;
- Browser-/Renderprüfung vor Completion Claim;
- explorable document und presentation als unterschiedliche Nutzungsmodi.

Lokal verallgemeinert:

```text
Reader Question
→ User Action
→ sichtbar neue Erkenntnis
```

und:

> Interaktion darf vertiefen, aber nicht die Kernaussage verstecken.

## RoboNuggets – `html-it`

Quelle:

`https://github.com/robonuggets/html-it`

Geprüfter Repository-Stand:

- Commit: `c5a2a060da20881aa926d511adacd86f37b31527`
- Skill-Blob: `94577da4c17510badafcfbff364bc6f1a222e49e`
- Lizenz: MIT

Methodisch relevant:

- statische Dokumente, visuelle Artefakte und interaktive Artefakte als steigende Capability-/Aufwandsstufen behandeln;
- Interaktion, die Entscheidungen oder Edits sammelt, braucht einen Rückweg in weiterverwendbare strukturierte Ausgabe;
- ein Wegwerf-Artefakt darf leichtgewichtig bleiben;
- ab echter App-Funktion entsteht eine andere Aufgabenklasse.

Nicht übernommen werden:

- „HTML statt Markdown“ als Defaultdogma;
- feste Längen-/Zeilenschwellen;
- konkrete Designpalette oder Typografie;
- Level-4-Mini-App als Teil des `visual-answer`-Kerns.

Lokale Grenze:

> Temporäres Explorable Artifact kann `visual-answer` sein; dauerhafte App mit Auth, Persistenz oder Multi-User-State gehört in Web-/Softwareentwicklung.

## Raghuram Sirigiri – `chart-dashboard` und `chart-honesty`

Quelle:

`https://github.com/raghuramsirigiri/raghuram-skills`

Geprüfter Repository-Stand:

- Commit: `d8742edd530057dee76a57057682e81f14b5b183`
- `chart-dashboard`-Blob: `c7b81828288f563590749917cd7e6aded40e96b1`
- `chart-honesty`-Blob: `74edf3aeec4c5b6034abe86ec94a23d3cf03c255`
- Lizenz: MIT

Methodisch relevant:

- erst Datenform und Leseraufgabe bestimmen, danach Chart/Format wählen;
- Dashboard, Report, One-Pager, Snapshot und Präsentation erfüllen unterschiedliche Konsumaufgaben;
- fehlende Werte nicht als Null erfinden;
- geschätzte Werte nicht ununterscheidbar in Ist-Daten mischen;
- Charttitel gegen tatsächliche Daten prüfen;
- Einheiten sichtbar halten;
- 3D-, Dual-Axis- und abgeschnittene-Achsen-Risiken bewusst behandeln;
- bei Chartreview keine Werte oder Achsgrenzen aus Pixeln schätzen.

Nicht übernommen:

- konkrete Chartbibliothek;
- Template-/Gridmaße;
- feste Chart-Auswahltabellen als universelle Wahrheit;
- geschlossene Review-Testliste als vollständige Visual-QA.

KI-Regeln generalisiert daraus **Visual Fidelity**: korrekte Daten müssen auch proportional, nachvollziehbar und nicht irreführend dargestellt werden.

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
