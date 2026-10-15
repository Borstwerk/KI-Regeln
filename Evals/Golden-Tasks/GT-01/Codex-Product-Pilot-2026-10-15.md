# GT-01: begrenzter Codex-Produktpilot

## Vorab festgelegter Vergleich

Ziel ist eine tatsächlich erzeugte Tabellenreferenz aus den unveränderten beiden
GT-01-Fixtures. Genau ein Paar frischer Codex-Abo-Sitzungen: zuerst Baseline ohne
KI-Regeln-Skilltext, danach derselbe Auftrag mit `reference-docs` und
`technical-writing`. Beide Skills haben keine verpflichtenden Referenzdateien.
Modell und Reasoning bleiben `gpt-6.1-sol` / `high`.

Die Fixtures stehen vollständig im Prompt; die Antwort ist das Markdown-Artefakt.
Keine Tools, Dateioperationen, weiteren Agenten oder Webrecherche. `task.yml` wird
nur lokal zur Projektion von Assignment und Fixtures sowie für die Judge View
gelesen. Erwartungen, Rubrik, Skillliste und sonstige Judge-Metadaten gelangen nicht
in den Aufgabenprompt. Nur die Behandlung erhält zusätzlich die zwei Skilltexte.

Das ist **forced invocation mit Produktprüfung**, kein vollständiger Golden-Task-
Behavioral-Run: natürliches Routing, Bootstrap, Skill-Reads, echte Datenbankausführung
und technisch erzwungene Dateisystem-Isolation werden nicht nachgewiesen.
Die angeforderte read-only CLI-Sandbox ersetzt keinen solchen Nachweis.

## Unveränderte Bewertungsbasis

Alle Kriterien werden für beide Antworten einzeln anhand von
[DDL](table-schema.sql), [Nutzung](usage.md) und [Taskdefinition](task.yml) geprüft.
Semantisch gleichwertige Formulierungen zählen; reine Stichworttreffer genügen nicht.

| ID | Erforderlicher Nachweis im Dokument |
| --- | --- |
| C1 | Genau die sechs Spalten: `id BIGINT`, `customer_id BIGINT`, `body TEXT`, `visibility VARCHAR(16)`, `created_at TIMESTAMPTZ`, `archived_at TIMESTAMPTZ`. |
| C2 | Nullability korrekt: die ersten fünf nicht nullable, `archived_at` nullable. `id` ist durch den Primary Key nicht nullable. |
| C3 | Explizite Defaults: `visibility = 'internal'`, `created_at = now()`; keine erfundene ID-Automatik oder anderen expliziten Defaults. Implizites NULL ist zulässig, wenn als solches erkennbar. |
| C4 | Primary Key auf `id`; benannter Check `ck_customer_note_visibility` erlaubt genau `internal` und `shared`. Keine zusätzlichen Constraints. |
| C5 | Index `ix_customer_note_customer_created` auf `(customer_id, created_at DESC)`, Reihenfolge und absteigender Zeitanteil erkennbar. |
| C6 | Bestätigte Nutzung: textuelle Hinweise im Kundenkontext; Archivierung behält den Datensatz und setzt `archived_at`. Keine zusätzlichen Geschäftsregeln. |
| C7 | Nicht definierter Foreign Key und unbekannte Retention/Löschfristen sichtbar; keine erfundenen Beziehungen oder Fristen. |
| C8 | DDL-Schemafakten und bestätigte Nutzung nachvollziehbar getrennt; konkreter Abgleich gegen beide Fixtures sowie keine zusätzlichen Spalten/Constraints erkennbar bestätigt. Ein eigener Satz mit exakt dieser Wortwahl ist nicht nötig. |
| C9 | Scanbare technische Referenz für Entwickler; Iststand statt Redesign/Migration. Keine Behauptung, SQL oder Beispiele in einer Datenbank ausgeführt zu haben. |

Urteil je Kriterium: `pass`, `partial` (unvollständig, ohne widersprechenden Claim),
`fail` (falsche oder verbotene Aussage), `unverified` (Antwort fehlt).
Produkturteil: alle Kriterien `pass` → `pass`; mindestens ein `fail` → `fail`;
sonst `partial` beziehungsweise ohne Antwort `unverified`.
Die Bewertung übernimmt der aktuelle Agent mit Kenntnis beider Bedingungen;
sie ist weder blind noch ein unabhängiger zweiter Modell-Judge.
Es gibt keinen neuen automatischen semantischen Grader.

## Reproduktion und Grenzen

Der [bestehende feste Pilot-Treiber](../../Agentenarbeit/verification-loop/codex_instruction_pilot.py)
erhält dafür nur den festen Modus `--gt01`, keinen neuen Runtime-Adapter:

```powershell
.validation/runtime/venv/Scripts/python.exe Evals/Agentenarbeit/verification-loop/codex_instruction_pilot.py --gt01
```

Ohne `--run` wird nur `.validation/codex-gt01-pilot-20261015/protocol.json`
vorbereitet. Mit zusätzlichem `--run` höchstens zwei Sitzungen, je 90 Sekunden,
kein Retry/Fallback, nur bestehender ChatGPT-Login. API-Schlüssel und Endpoint-
Overrides werden aus der Kindprozessumgebung entfernt. CLI-Fehler stoppen den Batch.
Ein Startmarker verhindert auch bei einem unterbrochenen Lauf einen automatischen
Neustart desselben Batches. Vorhandene Antworten bleiben erhalten.

Feste öffentliche Git-Blobs binden alle fünf Eingabedateien; das Protokoll bindet
zusätzlich Script, Prompts und Commit. Frische temporäre Arbeitsverzeichnisse,
`--ignore-user-config`, `--ephemeral` und `project_doc_max_bytes=0` reduzieren
unbeabsichtigten Projektkontext. Native Events werden nur als Typzählungen und Usage
veröffentlicht; keine Thread-IDs, Credentials oder rohen Reasoning-Traces.

Ein Paar zeigt nur den beobachteten Unterschied dieser zwei Antworten. Keine
statistische Wirkung, unabhängige Held-out-Evidence, Maturity-Hochstufung oder
Änderung von B2-Gates. Reihenfolge, Modellstochastik und Plattformkontext können den
Vergleich beeinflussen. Laufzeit und Tokenusage sind Aufwandssignale, keine
Abrechnung oder Aussage zum verbleibenden Abo-Kontingent.

## Ergebnisse

Noch nicht ausgeführt. Kriterien und Eingaben werden vor den zwei Modellaufrufen
committed; die vollständigen Antworten und die Bewertung werden danach ergänzt.
