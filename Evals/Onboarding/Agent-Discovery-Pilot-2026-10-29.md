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
`skill-catalog.yml`, `workflow-index.yml`, `routing-overlays.yml`,
`Validate-KI-Regeln.ps1`, `Validate-KI-Regeln.cmd`;
die operativen Ordner `Agentenarbeit`, `Dokumentation`, `Dokumentationserstellung`,
`Sicherheit`, `Skill-Engineering`, `Testing-und-QA`, `Workflows`, `Vorlagen`, `Schemas`,
`tools/local_validation` sowie `tools/repo_validator.py` und `Evals/README.md`.
Historische Dokumentations-Reviews, Praxisbeispielpakete und Upstream-Audits werden
aus dieser Auswahl entfernt. Sonstige Evals, diese Rubrik, Antworten, Tests, `.git` und lokale
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

Implementierung und Vorabkriterien wurden vor der Kaltlese in `512923a` und
`341bc3cdfba50fa3b658567655d0c551a7ad70de` committed und veröffentlicht.
Die [maschinenlesbare Evidence](Agent-Discovery-Pilot-2026-10-29.json) bindet
Prompt, Git-Stände, Snapshot-Hashes, CLI-Konfiguration und beide unbearbeiteten
Antworten: [bisheriger Stand](Agent-Discovery-Pilot-2026-10-29-baseline.md) und
[Pilotstand](Agent-Discovery-Pilot-2026-10-29-pilot.md).

### Strukturelle Evidence und Review

- Projektkarte und Contribution-Wegweiser verweisen direkt auf die drei Pilotbereiche.
  Deren Arbeitsfragen verlinken die zuständigen kanonischen Quellen.
- Die optionale Suchauswahl wächst von 4 auf 72 explizite Markdown-Dateien:
  im Windows-Checkout 373.506 UTF-8-Bytes insgesamt, maximal 32.396 Bytes je Datei. Die Umfangsprüfung
  besteht innerhalb der festgelegten Grenzen; keine Retrieval-Wirkung daraus ableiten.
- Der bestehende Prüfer und seine Tests decken fehlende Ziele, Traversal, Globs in
  der expliziten Auswahl, ausgeschlossene Quellen, Duplikate, UTF-8 und Größen ab.
  20 Testfälle: 19 `PASS`, eine echte Symlink-OS-Probe wegen fehlender Windows-Rechte
  `SKIP`. Junction-Verhalten ist nicht praktisch erprobt.
- Zwei getrennte Agentenpakete lieferten die Bereichsnavigation und das Manifest.
  Eine dritte Instanz reviewed den integrierten Diff. Ein Befund zu nicht greifenden
  Root-Ausschlüssen wurde korrigiert: fnmatch behandelt `**/` nicht automatisch als
  null Pfadsegmente. Die expliziten Root-Muster und sechs Root-/verschachtelte
  Negativproben sind nachgeprüft; die Semantik bleibt mit dem Consumer konsistent.

Nach dem eingefrorenen Kaltlesestand wurden ausschließlich zwei defensive
Root-Ausschlussmuster und ihre Negativkontrolle ergänzt. Die 72 ausgewählten
Markdown-Inhalte und die Navigation blieben unverändert; eine Consumer-Ausführung
dieser Manifestkorrektur wird nicht behauptet.

### Kaltlese: kein nachgewiesener Findbarkeitsgewinn

Beide CLI-Sitzungen endeten mit Exit 0 und lieferten eine Antwort. Beide melden
jedoch, dass lokale Lesebefehle durch ihre Ausführungsrichtlinie blockiert wurden.
Sie stützen sich deshalb ausschließlich auf den eingeblendeten Bootstrap-Text;
die konkrete Blockadeursache ist nicht unabhängig attestiert.

In der aufgezeichneten nativen Telemetrie fehlen abgeschlossene
`command_execution`-Events. Die Pilot-Sitzung enthält zusätzlich zwei
`mcp_tool_call`-Items; die veröffentlichten Typzählungen belegen weder deren
vollständige Semantik noch erfolgreiche Fachquellen-Reads. Daher bleibt der
erforderliche Discovery-/Quellenread-Nachweis **UNVERIFIED**.

| Frage | Bisheriger Stand | Pilotstand | Aussagegrenze |
| --- | --- | --- | --- |
| D1: Skill beitragen | unvollständige Orientierung, ehrlich begrenzt | ebenso | konkreter Beitragsweg nicht anhand geöffneter Fachquellen geprüft |
| D3: MCP vs Skill-Bundle | Antwort mit Bootstrap-Regel vereinbar | ebenso | kein zusätzlicher Read der Baseline oder Skill-Description nachgewiesen |
| D5: nicht gelaufener Test | kein unbelegter PASS | ebenso | Textverhalten; kein tatsächlich ausgeführter Test |

CLI: `0.165.0-alpha.1.2`; angefordert `gpt-6.1-sol` / `high`, keine unabhängige
Server-Modellattestation. Baseline 59,11 s, Pilot 50,69 s; Summe 109,80 s.
Native Usage-Felder insgesamt: 314.240 Input-, 246.272 Cached-Input-,
3.129 Output- und 885 Reasoning-Output-Tokens. Keine Aussage über Abrechnung,
verbleibendes Abo-Kontingent oder eine nachgewiesene Einsparung.

Die CLI-Navigationssnapshots enthalten jeweils 240 operative Dateien einschließlich
Register, Schemas und Scripts; sie sind ausdrücklich **nicht** mit den 72 Markdown-
Dateien der Mara-Suchauswahl gleichzusetzen. Die Rubrik war nicht enthalten.
Reproduktion über die in JSON angegebenen Archive-Pfade, Filter, exakten Promptbytes
und CLI-Argumente; es wurde kein zusätzlicher Repository-Runtime-Adapter eingeführt.

**Entscheidung:** Die strukturell geprüfte Navigation und begrenzte Suchauswahl
bereitstellen. Live-Findbarkeit bleibt `UNVERIFIED`; kein Vorher-/Nachher-Lift,
keine weiteren Modellversuche und kein Ausbau der Testplattform aus diesem Lauf.
D2/D4/D6/D7/D8 wurden nicht live ausgeführt. Lokale QMD-/Embedding-Laufzeit,
Mara-Oberfläche und Aktualisierung eines lokalen Suchindex bleiben `NOT RUN`.

Der [separate Lese-Folgelauf](Discovery-Read-Followup-2026-10-29.md) liefert später
beobachtete Fachquellen-Reads. Seine Abweichungen und sein `PARTIAL`-Urteil ändern
weder die alten Antworten noch deren hier dokumentierten Status.
