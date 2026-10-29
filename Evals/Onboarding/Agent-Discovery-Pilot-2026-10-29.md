# Auffindbarkeits-Pilot: drei Bereiche

## Ziel und Vorabkriterien

Kleine, problemorientierte Einstiege verbinden Projektübersicht, Beiträge und die
vorhandenen fachlichen Quellen. Pilot: Skill-Engineering, Sicherheit, Testing/QA.
Der verbindliche Bootstrap und die Skill-Trigger bleiben unverändert.

Basis vor Änderung: `1e85c80eacb1bf46aea51b07d2f68900ddc87c18`.
Die bisherige Manifestauswahl umfasst vier allgemeine Markdown-Einstiege.
Die neue Auswahl soll relevante Quellen innerhalb des vorhandenen Suchvertrags
erschließen, ohne Eval-Antworten oder unkontrollierte Archive einzubeziehen.

## Entwicklungsfragen (Evaluator-Sicht)

Diese bekannten Fragen sind weder ein unabhängiger Benchmark noch Held-out-Gold.
Erwartungen gelangen nicht in den Kontext einer ausführenden Kaltlese-Sitzung.

| ID | Alltagsfrage | Vorab erwarteter Beleg / Grenze |
| --- | --- | --- |
| D1 | Ich möchte einen neuen Skill beitragen. Wo beginne ich, was gehört zur Prüfung? | Skill-Engineering/skill-authoring, Katalog, Evals, Contribution und vorhandener lokaler Harness; nichts ohne Auftrag schreiben |
| D2 | Ein bestehender Skill scheitert wiederholt. Wo finde ich den Verbesserungsweg? | Evidence-getriebener Verbesserungsworkflow; Ursache/Baseline statt unbelegtem Skill-Edit |
| D3 | Ich möchte einen externen MCP-Server mit zusätzlichen Rechten verwenden. Ändert sich der Prüfweg, wenn das Paket auch Skills mitliefert? | Ohne Skills: MCP-Baseline und tool-permission-review; mit Skills: skill-security-review, zusätzliche Rechteprüfung nur bei eigenständigem Job; keine automatische Aktionsfreigabe |
| D4 | Brauche ich eine Teststrategie oder konkrete Grenzwertfälle? | test-strategy und test-design anhand der jeweils benötigten Arbeit unterscheiden |
| D5 | Ein geplanter Test konnte nicht laufen. Darf ich den Abschluss trotzdem als geprüft melden? | Nicht ausgeführt sichtbar; Teilchecks tragen keinen vollständigen Claim; kein automatischer Loop-Zwang |
| D6 | Ich möchte einen Workflow ergänzen. Welche Datei ist maßgeblich? | Workflows/README, workflow-index.yml, tatsächliche Workflow-Datei |
| D7 | Ich möchte „Zugriffe prüfen“. Welcher Skill passt? | Prüfobjekt und Ziel sind mehrdeutig: gezielt klären, nicht automatisch Skill-Admission oder Produktionszugriff unterstellen |
| D8 | Formatiere nur diesen Text: „eins,zwei“ → „eins, zwei“. | Trivialer Direktpfad; keine künstliche Skill-/Workflow-Aktivierung |

D3 und D7 prüfen insbesondere Objekt-/Scope-Mehrdeutigkeit; D8 ist eine
No-Skill-Kontrolle. Statische Linkprüfungen bewerten diese Semantik nicht.

## Begrenzte Kaltlese

Höchstens zwei frische Codex-Abo-Sitzungen: eine am Basisstand, eine am integrierten
Pilotstand. Beide erhalten identisch nur die Fragen D1, D3 und D5 in Alltagssprache
und einen operativen read-only Repository-Snapshot. Keine Rubrik, erwarteten
Dateipfade oder Eval-Berichte. Angefordertes Modell/Reasoning und Werkzeuge konstant.
Kein API-Schlüssel, keine direkte Modell-API, kein Retry/Fallback, keine weiteren
Agenten in den Sitzungen. Antworten und beobachtete native Events getrennt erfassen.

Ein Produktkriterium gilt als erfüllt, wenn die Antwort den richtigen fachlichen
Pfad anhand tatsächlicher Quellen benennt und seine Grenze erhält. Unvollständige
Antwort ohne falsche Aussage: `partial`; falscher Owner oder erfundene Freigabe/
Ausführung: `fail`; fehlender Lauf: `NOT RUN`. Reads nur aus beobachteten erfolgreichen
Toolereignissen ableiten, keinen Routing- oder Denkprozess aus Selbstauskunft erfinden.
Bei unvollständiger Telemetrie bleibt der betreffende Prozessnachweis `UNVERIFIED`.
Die koordinierende Instanz bewertet mit Kenntnis beider Bedingungen, nicht blind.

Reproduktionsdaten nach Ausführung: beide Git-SHAs, identische Promptbytes,
Snapshot-Umfang/-Hash, CLI-Version, angeforderte Konfiguration, native Laufzeiten/
Usage, unveränderte Antworten und kriterienspezifische Bewertung. Keine
Credential-/Thread-IDs oder rohen Reasoning-Traces veröffentlichen.
Kein statistischer Lift oder Tokenersparnisclaim aus diesem einen Paar.

Konstante CLI-Konfiguration: `gpt-6.1-sol`, Reasoning `high`,
`exec --ignore-user-config --ephemeral --sandbox read-only --skip-git-repo-check`,
`model_provider="openai"`, `forced_login_method="chatgpt"`, `web_search="disabled"`.
Je Sitzung höchstens 180 Sekunden; native Befehle dürfen nur lesen/suchen.
Der unveränderte Bootstrap liegt in beiden Snapshots und wird nicht durch eine
Test-Skillliste ersetzt. Keine technische Gesamtisolation wird attestiert.

Die Snapshots werden mit `git archive <SHA>` erzeugt, nicht aus einem veränderlichen
Arbeitsbaum. In beiden dieselbe Auswahl: Root-Dateien `AGENTS.md`, `PROJECT.md`,
`CONTRIBUTING.md`, `README.md`, `START-HIER.md`, `START-HERE.md`, `mara-project.json`,
`skill-catalog.yml`, `workflow-index.yml`, `routing-overlays.yml`, `ki-regeln.yml`;
die operativen Ordner `Agentenarbeit`, `Dokumentation`, `Dokumentationserstellung`,
`Sicherheit`, `Skill-Engineering`, `Testing-und-QA`, `Workflows` sowie
`Evals/README.md`. Sonstige Evals, diese Rubrik, Antworten, Tests, `.git` und lokale
Arbeitsdaten werden nicht exportiert. Das ist ein begrenzter Navigationssnapshot,
kein vollständiger Repository-/Runtime-Test.

## Arbeitsteilung

Zwei getrennte Pakete bearbeiten nur die drei Bereichs-READMEs beziehungsweise
`mara-project.json`. Gemeinsame Einstiege, Prüfer und Git-Integration liegen bei
der Koordination. Eine weitere Instanz reviewed den integrierten Diff und die
Nachweise. Verträge nennen Basis, Datei-Allowlist, Quellen, Akzeptanz und Stop.
Keine konkurrierenden Schreibrechte auf denselben Dateien und keine rekursive
Agentenverzweigung. Pflicht-Discovery bleibt auch für kleine Kontextpakete erhalten.

## Ergebnisstand

Vorabprotokoll; Ausführung und Abnahme werden getrennt ergänzt. Lokale QMD-/
Embedding-Laufzeit, Mara-Oberfläche und tatsächliche Aktualisierung eines lokalen
Suchindex sind nicht Teil dieser Repository-Prüfung und bleiben `NOT RUN`.
