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

Kriterien, Eingaben und Treiber waren vor den Modellaufrufen in
`6c8e015353150bd74887925d28fe59ad42bcac83` committed und veröffentlicht.
Die [vollständige Evidence](Codex-Product-Pilot-2026-10-15.json) bindet diesen Stand
einschließlich der ursprünglichen Protokollbeschreibung und enthält alle neun
Einzelbewertungen pro Antwort. Beide Dokumente bleiben unbearbeitet erhalten:
[Baseline](Codex-Product-Pilot-2026-10-15-baseline.md) und
[mit Skill-Bundle](Codex-Product-Pilot-2026-10-15-skill.md).

| Bedingung | C1–C5 | C6: Nutzung ohne zusätzliche Geschäftsregel | C7 | C8: Quellen und Abgleich | C9 | Produkturteil |
| --- | --- | --- | --- | --- | --- | --- |
| Baseline | pass | fail | pass | partial | pass | fail |
| Mit zwei Skills | pass | pass | pass | pass | pass | pass |

Beide Dokumente geben alle sechs Spalten, Nullability, expliziten Defaults,
Primary Key, benannten Check und Indexreihenfolge korrekt wieder. Beide lassen
Foreign Keys und Retention offen.

Die Baseline ergänzt bei `archived_at`: „bei nicht archivierten Einträgen `NULL`“.
Die Usage-Fixture bestätigt nur, dass archivierte Einträge ihren Datensatz behalten
und `archived_at` erhalten. Sie belegt keine allgemeine Regel für alle nicht
archivierten Einträge. Das nullable DDL ersetzt diesen fachlichen Nachweis nicht.
Damit verletzt die Baseline das vorher festgelegte C6 („Keine zusätzlichen
Geschäftsregeln“). Das ist eine unbelegte Verstärkung, kein Nachweis einer tatsächlich
falschen Datenbankbelegung. Außerdem fehlt die konkrete Bestätigung eines eigenen
Fixture-Abgleichs (C8 `partial`). Die Skill-Antwort vermeidet die Umkehrregel,
ordnet Quellen abschnittsweise zu und bestätigt den Abgleich ausdrücklich.
Der sichtbare Text und unser Quellenvergleich belegen Produkt und Aussage;
der interne Arbeitsprozess wird daraus nicht rekonstruiert.

Zusätzlicher Provenienzvorbehalt zur Baseline: „B-Tree, impliziter PostgreSQL-Standard“
setzt einen konkreten Enginekontext voraus, den die Fixtures nicht ausdrücklich
festlegen. Das wird nicht als weiterer C5-Fehler oder als falsche PostgreSQL-Aussage
gezählt. Es gibt keinen zusätzlichen Web- oder Datenbanknachweis.

| Aufwand laut CLI | Baseline | Mit zwei Skills |
| --- | --- | --- |
| Laufzeit | 25,95 s | 33,31 s |
| Input-Tokens | 12.280 | 12.968 |
| Output-Tokens | 996 | 1.131 |
| Reasoning-Output-Tokens (CLI-Feld) | 141 | 462 |

CLI-Version: `0.162.0-alpha.17.2`. Beide Aufrufe endeten mit Exit 0. Native Events
enthielten eine beziehungsweise zwei `agent_message`-Items und keine Tool-Items.
Insgesamt 59,26 Sekunden, 25.248 Input- und 2.127 Output-Tokens.
Die Modellidentität ist nur als angefordertes Modell gebunden, nicht unabhängig
serverseitig attestiert.

**Entscheidung:** Die Skill-Antwort bleibt in diesem Paar enger an den Quellen und
erfüllt die vorab festgelegte Produktrubrik. Das ist ein beobachteter Unterschied,
kein belastbarer allgemeiner oder kausaler Skill-Lift. Die Skills verbieten das
Erfinden von Fakten bereits; aus diesem Einzelpaar folgt keine zusätzliche
Regelverschärfung. Keine Skilländerung, Maturity-Hochstufung oder B2-Freigabe.
Natürliche Discovery und vollständige Golden-Task-Prozessqualität bleiben `NOT RUN`.
