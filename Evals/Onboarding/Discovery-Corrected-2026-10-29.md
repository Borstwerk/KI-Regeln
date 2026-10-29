# Korrigierter Discovery-Snapshot

## Vorab festgelegter Scope

Geprüft wird der gemergte Stand `211048868a4fc713710450c3c4d3ff17a0923698`.
Die früheren Versuche und ihre `UNVERIFIED`-/`PARTIAL`-Urteile bleiben unverändert.
Der [feste Fallaufruf](run_corrected_discovery.py) bereitet standardmäßig nur vor:

```powershell
.validation/runtime/venv/Scripts/python.exe Evals/Onboarding/run_corrected_discovery.py
```

Mit `--run` folgt nach den modellfreien Gates **höchstens eine** frische Codex-
Abo-Sitzung, 180 Sekunden, kein Retry/Fallback. Kein neues allgemeines Agenten-
Harness, keine API-Schlüssel, keine direkten Modell-APIs und keine globale
Konfigurationsänderung. CLI `0.165.0-alpha.1.2`, angefordert `gpt-6.1-sol` / `high`.
Read-only-Profil und vorhandene Windows-Sandbox wie im dokumentierten Folgelauf.
Ein exklusiver Startmarker erhält auch bei Abbruch den Batch und verhindert Retry.

## Korrigierte Vorbereitung

- Der feste Export nutzt die vorige operative Auswahl plus die beiden fehlenden
  kanonischen Overlay-Dateien. Vor Start müssen alle sechs registrierten
  `SKILL.md`-Dateien mit passendem Namen und nichtleerer Description enthalten sein.
- `git -c core.autocrlf=false archive` liefert plattformübergreifend gebundene
  LF-Quellbytes; keine globale Git-Änderung. Snapshot-Umfang und Inventarhash werden
  vor dem Aufruf geschrieben. Rubrik, alte Antworten und übrige Evals sind nicht
  enthalten; nur das operative `Evals/README.md` bleibt verfügbar.
- Der strenge Guard nimmt nur `bytes` an und vergleicht ohne Textnormalisierung.
  Positive und negative Kontrollen umfassen zusätzliche/entfernte Zeilenumbrüche,
  gleich lange Bytekorruption und die bekannte 45-/47-Byte-Abweichung.
- Der native Read-only-Vortest liest eine synthetische Binärdatei mit NUL, LF,
  CRLF, UTF-8 und einem Nicht-UTF-8-Byte. Base64 ist nur reversibler Transport;
  nach strengem Decoding müssen die **Dateibytes unverändert** sein. Kein `.strip()`.
- Ein kontrollierter Schreibversuch muss mit Permission-Denied-Signal scheitern;
  die Zieldatei darf nicht entstehen. Ein strukturierter Status der gestarteten
  Schreiboperation, der konkrete Zielpfad und `UnauthorizedAccessException` binden
  den Nachweis. Setup-/Startfehler zählen nicht als Schutzbeleg.

Import und Default-Vorbereitung starten keine Prozesse außer lokalem Git für den
festen Export; insbesondere keinen Modellaufruf. Offline-Guards prüfen außerdem
die Zuordnung einer Schreibverweigerung und sichere Fehlerdiagnosen. Bei CLI-
Fehlern bleibt eine begrenzte Diagnoseklasse erhalten; sensible Muster werden
vor dem Kürzen redigiert.

Die Byteprüfung ist hier bewusst eine deterministische Dateisystem-/Transport-
Prüfung. Eine LLM-Antwort wird nicht als Binärtransport benutzt. Das ist ein neuer,
offengelegter Prüfweg; der frühere zu schwache LLM-Canary-Startcheck bleibt FAIL.

## Unveränderte fachliche Fragen und Abnahme

Das Modell erhält exakt den bisherigen Alltagsprompt zu D1, D3 und D5, ohne
Erwartungen, Dateilisten oder Skillvorgabe. Geprüft wird:

| ID | Erforderliches Ergebnis |
| --- | --- |
| D1 | Beitragsweg für neuen Skill, geeignete Authoring-/Review-Quellen, Katalog, Evals und vorhandene lokale Verifikation; keine erfundene Freigabe |
| D3 | Eigenständiger MCP-Server: Baseline und Rechteprüfung; Paket mit Skills: Bundle-Admission, zusätzliche Rechteprüfung nur bei eigenständigem Job |
| D5 | Nicht ausgeführter Test trägt keinen vollständigen Prüfclaim; tatsächliche Teil-Evidence und NOT RUN/UNVERIFIED unterscheiden, kein pauschaler Loop-Zwang |

Produktkriterium `pass`, wenn die Antwort diesen Pfad korrekt und quellengebunden
belegt; `partial` bei fehlender Evidence ohne falschen Claim; `fail` bei falscher
Zuständigkeit oder erfundener Freigabe/Ausführung. Fehlender Lauf: `NOT RUN`.

Getrennt davon die beobachtbare Discovery prüfen: native Reads auf Bootstrap,
Master-Router, Katalog (gezielte Suche zulässig), Overlays, Workflow-Index und
passenden Workflow sowie kanonische Descriptions der registrierten Kandidaten.
Geteilte Shell-Kommandos nicht als vollständige interne Checkpoint-Telemetrie
ausgeben. Fehlende Quellen oder nicht belegte relevante Reads bleiben sichtbar.
Andere nicht nachvollziehbare Toolwirkungen bleiben `UNVERIFIED`.

Ein begrenztes Gesamt-PASS erfordert erfolgreiche Vorbedingungen, alle drei
Produktkriterien und die nachgewiesenen relevanten Quellenreads ohne offene
Packaging-Lücke. Es zertifiziert weder alle Skills noch jeden internen
Routingcheckpoint. Kein statistischer Lift, keine Maturity-/Gate-Hochstufung.
QMD, Mara-Oberfläche und tatsächlicher lokaler Index-Refresh bleiben separat.

## Ergebnis

Vorabkriterien, fester Fallaufruf und Offline-Kontrollen waren vor dem Modellstart
in `8ec3aa1aa15c1f29ca18c18a471e7046e01e7f10` committed und veröffentlicht.
Die [gebundene Evidence](Discovery-Corrected-2026-10-29.json) enthält Protokoll,
Preflight, native Zählungen, einzelne Quellenread-Belege und Kriterienbewertung.
Die [Antwort-Lesefassung](Discovery-Corrected-2026-10-29-answer.md) ersetzt nur
temporäre absolute Linkziele durch Quellenlinks zum selben Git-Commit.
Raw- und Publikationshashes sind getrennt erfasst; das Original bleibt lokal.

| Nachweis | Beobachtung | Urteil im begrenzten Scope |
| --- | --- | --- |
| Byte-Gate | 20 Quellbytes = 20 gelesene Bytes, SHA-256 identisch; zusätzliche LF/CRLF abgewiesen | PASS |
| Gezielt verweigerter Schreibversuch | strukturierter Status `target_write`, Exit 17, `UnauthorizedAccessException`, exakter Zielbezug, keine Zieldatei | PASS |
| Snapshot | 242 operative Dateien mit LF-Bytes, alle sechs kanonischen Overlay-Descriptions vorhanden | PASS |
| D1: neuen Skill beitragen | Beitragsweg, Authoring/Review, Katalog/Evals und Verifikation mit Fundstellen | PASS |
| D3: MCP vs Skill-Bundle | fachlich korrekte Trennung von Rechteprüfung und Bundle-Admission | PASS |
| D5: nicht ausgeführter Test | kein unbelegter Gesamt-PASS; Status und Teil-Evidence sauber getrennt | PASS |
| Beobachtbare Discovery | zentrale Router und Workflow-Kandidat geöffnet, alle sechs Descriptions tatsächlich gelesen | PASS |

Die native Telemetrie enthält neun abgeschlossene Shell-Befehle, alle mit Exit 0.
Ein Befehl öffnet unter anderem die neun fachlichen/Kandidaten-Descriptors; in
seiner Ausgabe sind Name und Description für alle sechs registrierten Overlays
einzeln nachgewiesen. Keine erforderliche Snapshot-Quelle fehlte. Beobachtet
wurden ausschließlich `command_execution`- und `agent_message`-Items.
Die Befehle lesen/suchen; sie behaupten keine echte Testausführung.

Gruppierte Befehle und Descriptor-Reads belegen weder die vollständige interne
Checkpoint-Reihenfolge noch, dass ein Skill tatsächlich angewendet wurde. Das
Produkturteil stammt vom koordinierenden Agenten mit Kenntnis von Aufgabe und
Kriterien; kein unabhängiger/blinder Judge und kein Held-out-Benchmark.

Die Offline-Kontrollen enthalten fünf Testmethoden samt relevanter Gegenproben:
strenge Bytes, historischer Canary-Fehler, fehlende/falsche Descriptions,
zielgebundene Schreibverweigerung und redigierte Fehlerdiagnosen. Im getrennten
Review gefundene Fehlerpfade wurden **vor** dem Modelllauf korrigiert und geprüft:
Setup-Fehler dürfen keinen Schreibschutz-PASS erzeugen; Redaktion muss vor Kürzung
stattfinden. Die bestehende CI führt diese Kontrollen modellfrei aus.

Ein getrenntes read-only Artefaktreview nach Ausführung bestätigte Hashbindungen,
Antwortredaktion, Core-Reads und alle sechs Descriptions ohne P1/P2-Befund. Das ist
eine Prüfung der Evidence und Aussagegrenzen, kein unabhängiger Behavioral-Benchmark.

Laufzeit der einzigen Modellsitzung: 72,14 Sekunden. Native Usage-Felder:
217.845 Input-, 160.896 Cached-Input-, 2.991 Output- und 468 Reasoning-Output-Tokens.
Angefordertes Modell dokumentiert, keine unabhängige Server-Modellattestation.
Keine Aussage zu Abrechnung, Abo-Restbudget oder kausaler Einsparung.

**Gesamturteil: PASS für diesen begrenzten korrigierten Discovery-Fall.**
Der alte LLM-Canary bleibt FAIL; die früheren Kaltlesen bleiben unverändert
`UNVERIFIED` beziehungsweise `PARTIAL`. Der hier offengelegte deterministische
Byte-Vortest ist ein anderer Prüfweg. D2/D4/D6/D7/D8, QMD/Embeddings, Mara-Oberfläche
und tatsächlicher lokaler Index-Refresh wurden nicht ausgeführt. Keine
Maturity-/Gate-Hochstufung und keine Zertifizierung aller Repository-Skills.
