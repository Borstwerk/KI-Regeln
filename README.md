# KI-Regeln

> **Du bringst die Aufgabe. Der Werkzeugkasten liefert die passende Arbeitsweise.**

KI-Regeln ist ein offener Werkzeugkasten für Menschen, die generative KI für konkrete Aufgaben einsetzen möchten, ohne sich zuerst tief in Prompt Engineering, Agentensysteme oder einzelne KI-Werkzeuge einarbeiten zu müssen.

Der Ausgangspunkt ist **nicht** ein Skill-Name.

Der Ausgangspunkt ist ein reales Problem:

- „Ich möchte etwas recherchieren.“
- „Ich muss einen technischen Fehler verstehen.“
- „Ich möchte einen Text oder eine Dokumentation erstellen.“
- „Ich möchte eine Geschichte mit konsistenten Figuren entwickeln.“
- „Ich möchte meine Finanzen strukturierter analysieren.“
- „Ich möchte eine Website oder eine Bildserie bauen.“

KI-Regeln hilft der KI dabei, aus dem vorhandenen Werkzeugkasten die **kleinste ausreichende Kombination aus Regeln, Skills und Workflows** auszuwählen und kontrolliert anzuwenden.

## Neu hier? Start hier.

Wenn du das Repository einfach benutzen möchtest, ohne seine interne Architektur zu lernen:

**→ [`START-HIER.md`](START-HIER.md)**

Dort steht der problemorientierte Einstieg samt Beispielauftrag.

Weitere Einstiege:

- Reale Arbeitsbeispiele: [`PRAXISBEISPIELE.md`](PRAXISBEISPIELE.md)
- Ausführlichere Nutzung: [`Dokumentation/Nutzung-des-Repositories.md`](Dokumentation/Nutzung-des-Repositories.md)
- Technischer Einstieg für KI-Agenten: [`AGENTS.md`](AGENTS.md)
- Skill-Routing: [`Dokumentation/Skill-Handbuch.md`](Dokumentation/Skill-Handbuch.md)
- Reife und Evalabdeckung: [`Dokumentation/Skill-Katalog.md`](Dokumentation/Skill-Katalog.md)

## KI-Regeln in 60 Sekunden

```text
Du beschreibst dein Problem oder Ziel
→ vorhandene Informationen / Dateien / Projektregeln werden als lokale Wahrheit bestimmt
→ die KI ordnet die Aufgabe ein
→ sie wählt den kleinsten ausreichenden Workflow-/Skill-Satz
→ fehlende, wirklich notwendige Informationen werden geklärt
→ die Aufgabe wird bearbeitet
→ Ergebnis und Evidence werden geprüft
→ Human Gate, wenn eine Entscheidung oder Außenwirkung es erfordert
```

Du musst dafür weder die Namen der Skills kennen noch das komplette Repository in einen Prompt laden.

Die allgemeinen Regeln helfen beim **Wie**. Das konkrete Projekt bestimmt weiterhin das **Was**.

## Was möchtest du tun?

| Beispielhafte Aufgabe | Typischer Bereich |
|---|---|
| recherchieren, Quellen bewerten, Behauptungen prüfen | Recherche |
| Texte schreiben, überarbeiten oder adressatengerecht formulieren | Schreiben |
| Figuren, Plot, Welt oder Kontinuität einer Geschichte entwickeln | Storyentwicklung und Fiktion |
| Cashflow, Rücklagen, Schulden, Vermögensszenarien oder Anlagen analysieren | Finanzen |
| Bilder oder konsistente Bildserien entwickeln und prüfen | Bildarbeit |
| Websites gestalten, umsetzen oder reviewen | Webentwicklung |
| Code entwickeln oder Fehler diagnostizieren | Programmieren |
| Datenbanken analysieren, dokumentieren oder ändern | Datenbanken |
| Anforderungen klären und spezifizieren | Requirements und Spezifikations-Engineering |
| technische Dokumentation erstellen | Dokumentationserstellung |
| Wissen langfristig strukturieren und pflegen | Wissensmanagement |
| Datenpipelines, Architektur, Infrastruktur oder Reliability bearbeiten | jeweiliger technischer Fachbereich |

Diese Tabelle ist Orientierung, keine starre Routingmatrix. Ein reales Problem kann mehrere Bereiche berühren, und manchmal ist gar kein spezieller Skill nötig.

## Warum gibt es KI-Regeln?

KI-Regeln entstand aus einer einfachen Beobachtung: Viele Menschen können ihre Arbeit und private Projekte mit generativer KI verbessern, möchten aber nicht zuerst selbst zu KI-Spezialisten werden.

Das Repository soll diese Lücke schließen. Statt für jede denkbare Aufgabe einen fertigen „Superprompt“ anzubieten, werden wiederverwendbare Arbeitsweisen so strukturiert, dass eine KI von einem konkreten Problem zu den passenden Werkzeugen routen kann.

Das Ziel ist:

```text
Problem
→ passende Werkzeuge
→ kontrollierte Bearbeitung
→ überprüfbares Ergebnis
```

Dabei bleiben Quellen, Annahmen, Unsicherheiten, Prüfungen und erforderliche menschliche Entscheidungen sichtbar.

## Grundprinzip

> **Allgemeine Arbeitsweise zentral, konkrete Wahrheit lokal.**

KI-Regeln enthält allgemeine Methoden. Es kennt nicht automatisch die Wahrheit deines Projekts.

Lokal beziehungsweise beim Nutzer bleiben je nach Aufgabe zum Beispiel:

- reale Anforderungen und Ziele;
- vorhandene Dateien, Daten und interne Quellen;
- gültige Projektentscheidungen;
- fachliche oder visuelle Vorgaben;
- konkrete Systeme, Versionen, Schemas und Toolzustände;
- Zielwerte und Messdefinitionen;
- persönliche Präferenzen, soweit sie für die Aufgabe relevant sind;
- Freigaben für Veröffentlichungen, Käufe, Deployments oder andere Außenaktionen.

Allgemeine Regeln dürfen diese konkrete Wahrheit nicht durch plausible Annahmen ersetzen.

## Was passiert unter der Haube?

Der Werkzeugkasten besteht aus mehreren Ebenen:

- **Regeln** beschreiben allgemeine Leitplanken und Arbeitsweisen.
- **Skills** beschreiben begrenzte, wiederverwendbare Fähigkeiten.
- **Workflows** verbinden mehrere Skills für größere Aufgaben.
- **Routing** hilft, vom Problem zum kleinsten ausreichenden Werkzeug-Satz zu gelangen.
- **Evidence und Verification** machen prüfbar, worauf Ergebnisse gestützt sind.
- **Human Gates** trennen Analyse oder Vorschlag von realen, freigabepflichtigen Aktionen.
- **Maturity und Eval Coverage** zeigen Reife und vorhandenen Prüfstand.
- **Provenance** dokumentiert relevante externe methodische Einflüsse und Drittmaterial.

Der Skill-Katalog ist damit der **Werkzeugschrank hinter der Werkstatt**. Die normale Nutzung beginnt nicht dort, sondern beim Problem.

## Reife und Anspruch

KI-Regeln ist ein experimenteller, systematisch gepflegter Werkzeugkasten für kontrollierte KI-Arbeit.

Die Anzahl vorhandener Skills ist **Inventar, kein Qualitätsnachweis**.

Skills besitzen explizite Maturity-Level wie `experimental` oder `candidate`; daneben wird die Eval Coverage mit Stufen wie `none` oder `partial` dokumentiert.

Dabei gilt ausdrücklich:

```text
definierter Evalfall
≠ ausgeführter Test

 ausgeführter Test
≠ automatisch bestanden

Same-Model-Smoke
≠ unabhängiger Benchmark
```

Maturity, Eval Coverage, Toolverfügbarkeit oder ein Review-Verdict erweitern keine Autorisierung.

## Praxis statt Prompt-Magie

Die Praxisbeispiele zeigen reale Arbeitsweisen und auch deren Fehler, Korrekturen und Grenzen:

**→ [`PRAXISBEISPIELE.md`](PRAXISBEISPIELE.md)**

Ein Praxisbeispiel ist dabei weder Benchmark noch Garantie noch Beweis, dass ein einzelner Prompt genügt.

## Fach- und Methodenbereiche

Der Werkzeugkasten umfasst unter anderem:

```text
Grundlagen
Arbeitsweisen
Agentenarbeit
Recherche
Wissensmanagement
Schnittstellen und Verträge
Infrastruktur und DevOps
Reliability und System-Observability
Data Engineering
Software Architecture und System Design
Requirements und Spezifikations-Engineering
Social Media und Content-Präsenz
Dokumentationserstellung
Schreiben
Storyentwicklung und Fiktion
Finanzen
Bildarbeit
Webentwicklung
Programmieren
Datenbanken
Testing und QA
Skill Engineering
Sicherheit
```

Die jeweils verbindliche Skill-Inventarliste liegt in [`skill-catalog.yml`](skill-catalog.yml). Bereichs-READMEs und Fachdateien enthalten die Detailregeln.

## Für KI-Agenten

Ein Agent soll nicht das komplette Repository laden und den Nutzer anschließend mit Skill-Namen befragen.

Der technische Bootstrap steht in [`AGENTS.md`](AGENTS.md). Kernidee:

```text
Nutzerproblem
→ lokale Wahrheit
→ fachlich einordnen
→ Workflow prüfen
→ kleinsten Skill-Satz wählen
→ nur notwendige Lücken klären
→ arbeiten
→ verifizieren
→ erforderliche Gates sichtbar machen
```

Der Master-Router steht in [`Dokumentation/Skill-Handbuch.md`](Dokumentation/Skill-Handbuch.md).

## Für Contributors und tiefere technische Nutzung

- [`Dokumentation/Skill-Katalog.md`](Dokumentation/Skill-Katalog.md) – Maturity und Eval Coverage
- [`skill-catalog.yml`](skill-catalog.yml) – maschinenlesbares Skill-Inventar
- [`workflow-index.yml`](workflow-index.yml) – vorhandene Workflows
- [`Dokumentation/Quellenregister.md`](Dokumentation/Quellenregister.md) – Quellen-/Upstream-Governance
- [`CONTRIBUTING.md`](CONTRIBUTING.md) – Beitrags- und Reviewprozess
- [`SECURITY.md`](SECURITY.md) – Security-Policy

## Public Entry Path und Lizenz

Die Root-Projektlizenz ist MIT und gilt für das projekt-eigene KI-Regeln-Material. Drittmaterial wird dadurch nicht automatisch unter MIT gestellt.

Maßgeblich sind zusätzlich:

- [`ACKNOWLEDGEMENTS.md`](ACKNOWLEDGEMENTS.md) – methodische Referenzräume;
- [`THIRD-PARTY-NOTICES.md`](THIRD-PARTY-NOTICES.md) – redistribution-relevante Drittmaterial-Notices;
- [`Dokumentation/open-source-readiness.yml`](Dokumentation/open-source-readiness.yml) – maschinenlesbarer Readiness-/Release-Gate-Status;
- [`Dokumentation/Open-Source-Readiness-2026-08-25.md`](Dokumentation/Open-Source-Readiness-2026-08-25.md) – historischer Phase-3-Auditbericht.

Eine vorhandene Root-`LICENSE` ist keine automatische Veröffentlichungsfreigabe. Der Public-Release-Status wird weiterhin ausschließlich über `Dokumentation/open-source-readiness.yml` bestimmt.

---

> **Du musst den Werkzeugkasten nicht kennen, bevor du ihn benutzen kannst. Beschreibe die Aufgabe – die Werkzeugauswahl ist Teil der Arbeit.**
