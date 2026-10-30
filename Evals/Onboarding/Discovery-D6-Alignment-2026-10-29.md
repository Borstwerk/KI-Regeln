# D6: Orientierungsfrage und Beitragsablauf trennen

## Befund und Entscheidung

Die Frage „Ich möchte einen Workflow ergänzen. Welche Datei ist maßgeblich?“
blieb unverändert. Ihr Bewertungsumfang wurde jedoch zwischen zwei
Vorabprotokollen erweitert:

| Stand | Vor Ausführung festgelegte Erwartung |
| --- | --- |
| [Pilot, Commit 341bc3c](https://github.com/Borstwerk/KI-Regeln/blob/341bc3cdfba50fa3b658567655d0c551a7ad70de/Evals/Onboarding/Agent-Discovery-Pilot-2026-10-29.md#L26) | Workflow-README, Workflow-Index und tatsächliche Workflow-Datei finden |
| [Verbliebene Fragen, Commit 047b7c6](https://github.com/Borstwerk/KI-Regeln/blob/047b7c632a74f68ddcd63d94731da6f97c3dce33/Evals/Onboarding/Discovery-Remaining-2026-10-29.md#L47) | zusätzlich den Contribution-/Validierungsweg unterscheiden |

Die Erweiterung wurde vor den betroffenen Live-Versuchen veröffentlicht. Sie
ist keine nachträgliche Manipulation eines bereits gelaufenen Tests. Sie blieb
aber ohne entsprechende Präzisierung der natürlichen Frage. Eine knappe
Dateiorientierung und eine vollständige Beitragsanleitung sind verschiedene
Leseraufgaben.

Die spätere Überschrift „Unveränderte fachliche Erwartung“ ist für D6 deshalb
unpräzise. Dieser Vermerk berichtigt die Einordnung; das eingefrorene Protokoll
und seine Urteile bleiben als historische Evidence erhalten.

Die beiden archivierten D6-Antworten nennen jeweils Index, Workflow-Datei und
Workflow-README: [erster Folgelauf](Discovery-Remaining-Followup-2026-10-29-answers.md)
und [gezielte Nachprüfung](Discovery-D6-Recheck-2026-10-29-answer.md). Das deckt
die drei ursprünglichen Orientierungspunkte ab. Die zusätzlichen Validierungs-
und PR-Schritte fehlen in der Antwort weiterhin. Das ist ein retrospektiver
Inhaltsabgleich, kein neuer Modelllauf oder neues PASS-Urteil.

**Entscheidung:** Aus diesen Antworten wird kein weiterer Bootstrap-, Routing-
oder Skill-Fix abgeleitet. Der Abgleich belegt eine Anforderungsverschiebung
zwischen den Rubriken; ein verursachender Routingdefekt ist damit nicht
nachgewiesen. Die bereits ergänzte Workflow-Navigation bleibt ein verifizierter
Verweis auf bestehende Contribution-Regeln, kein nachgewiesener allgemeiner
Qualitätsgewinn.

## Historische Evidence erhalten

Die zwei `partial`-Urteile unter der später eingefrorenen Rubrik bleiben
unverändert. Antworten, JSON-Evidence, Promptbytes, Rohdaten und Runner werden
nicht umgeschrieben. Die begrenzte Reparatur-/Nachprüfungsschleife bleibt
beendet; die alte Bewertung wird nicht durch eine weichere Schwelle grün gerechnet.

Die folgenden getrennten Fallentwürfe betreffen ausschließlich künftige Läufe.
Sie sind keine neue Registry oder Harness-Funktion und erhöhen keine Coverage.

## Künftige getrennte Fallentwürfe

### D6-NAV-v1 – Orientierung

**Auftrag:** „Ich möchte einen Workflow ergänzen. Welche Datei ist maßgeblich?“

**Erwartung:** Workflow-Datei unter `Workflows/`, Registrierung im
`workflow-index.yml` und Workflow-README als Einstieg korrekt unterscheiden und
an tatsächlich gelesene Quellen binden. Weitere passende Hinweise sind erlaubt;
eine vollständige Validierungs-/PR-Anleitung ist für diesen Auftrag keine
Pflicht. Falsche Zuständigkeit oder eine unterstellte Änderungsfreigabe bleiben
Fehler.

**Status:** `NOT RUN` als eigener neuer Fall. Die historischen Antworten sind
keine frisch ausgeführte unabhängige Baseline dieses Entwurfs.

### D6-CONTRIB-v1 – vollständiger Beitragsweg

**Auftrag:** „Ich möchte einen neuen Workflow zu KI-Regeln beitragen. Erkläre
mir den Weg von der Workflow-Datei über die Registrierung und lokale Prüfung
bis zum Pull Request und Review. Nenne die maßgeblichen Quellen; ändere keine
Dateien und führe keine Tests aus.“

**Erwartung:** Vorhandenen Bedarf/Ablauf prüfen, Workflow-Datei und Index
unterscheiden, den vorhandenen lokalen Harness mit passender Prüfung benennen
und PR nach `main` samt fachlichem Review erklären. Kanonische Quellen sind
[CONTRIBUTING.md](../../CONTRIBUTING.md), das [Workflow-README](../../Workflows/README.md)
und der [Local Validation Harness](../../Dokumentation/Local-Validation-Harness.md).
Eine Wegbeschreibung ist kein ausgeführter Test, erstellter PR oder Merge.

**Status:** `NOT RUN`. Kein Ergebnis aus den früheren Orientierungsantworten
ableiten; sie wurden nicht mit diesem Auftrag erzeugt.

## Grenzen und nächster Einsatz

Vor einem künftigen Lauf dessen Quellencommit, genaue Promptbytes, Rubrik,
Rechte, Zeit-/Startgrenze und Prozessnachweise festlegen. Verschiedene Aufträge
nicht als Vorher-/Nachher-Vergleich oder Skill-Lift auswerten. Die Bewertung
dieses Vermerks kennt sämtliche Antworten und ist weder blind noch statistisch.

Für diesen Abgleich sind keine weiteren Modellaufrufe erforderlich. Skills,
Gates, Maturity und technische Testinfrastruktur bleiben unverändert. Eine
optionale Suchanbindung oder ein tatsächlicher Index-Refresh in Mara ist ein
separater Nachweis und wurde hier nicht ausgeführt.
