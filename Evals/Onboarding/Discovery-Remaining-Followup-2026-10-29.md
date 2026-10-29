# Verbliebene Discovery-Fragen – separater Folgelauf

## Vorabprotokoll

Der in [PR #110 dokumentierte Versuch](Discovery-Remaining-2026-10-29.md) bleibt
unverändert `BLOCKED`. Er wird weder wiederholt noch überschrieben. Nach dessen
Merge ist der koordinierende Quellenstand
`39f1c32` maßgeblich; der zu prüfende Snapshot bleibt für Vergleichbarkeit
`cc8f8b6b945bc1cd0d5078433d67c03fb97e97d9`.

### Zugang vor Wiederaufnahme

Modellfreie native READ-Abfragen bestätigen den vorhandenen ChatGPT-Login, den
Katalogeintrag `gpt-6.1-sol` mit `high` und verfügbare Basisgrenzen. Das ist keine
vollständige Entitlement-Prüfung für einen konkreten Modellaufruf. Die
[offizielle CLI-Dokumentation](https://learn.chatgpt.com/docs/app-server)
beschreibt die verwendeten `account/read`, `model/list` und
`account/rateLimits/read`-Abfragen. Der App-Server lädt Nutzerkonfiguration;
sein Read-Ergebnis ist deshalb kein identischer `exec --ignore-user-config`-Lauf.

Ein getrennt aufgezeichneter Zugriffs-Repro mit dem bestehenden `run_one` war
anschließend erfolgreich: Prompt „Antworte ausschließlich mit OK.“, keine
bereitgestellten Repository-Dateien, `gpt-6.1-sol` / `high`, 45 s Deadline,
höchstens ein Start, Exit 0 nach 5,34 s, Antwort „OK“, keine beobachteten
Tool-Commands. Normale CLI-Basisinstruktionen bleiben vorhanden. Ein frischer
Byte-/zielgebundener Schreibschutz-Vortest bestand. Der Repro nutzt dieselben
expliziten Auth-/Read-only-/Windows-Parameter wie die Qualitätsfälle und entfernt
die bekannten API-Key-/Provider-Override-Variablen aus der Kindumgebung.

Dieser Repro ist **kein Qualitätsnachweis für KI-Regeln**. Es gab keinen
Login-/Accountwechsel, keine Konfigurationsänderung, keinen Resetverbrauch und
keinen Modell-/API-Fallback. Er belegt aktuellen Zugriff für genau diesen
Aufruf; die Ursache des früheren Fehlers bleibt `UNVERIFIED`. Lokale Diagnose-
und Repro-Artefakte bleiben unter `.validation/`; private Kontodetails werden
nicht veröffentlicht.

### Fester Qualitätsbatch

Der bestehende [Fallaufruf](run_corrected_discovery.py) läuft ohne weitere
Änderung in einem separaten lokalen Git-Checkout unter
`.validation/discovery-followup-checkout-20261029/`. Dessen eigener
`.validation/discovery-remaining-20261029/`-Ordner ist vor Beginn leer.
Der alte Batch-Ordner und dessen Startmarker im ursprünglichen Checkout bleiben
erhalten. Kein neuer allgemeiner Runner und keine Änderung des Standardmodus.

```powershell
# Im frischen Checkout; Python aus dem vorhandenen lokalen Validation Harness:
<harness-python> Evals/Onboarding/run_corrected_discovery.py --remaining --run
```

Vor dem ersten Qualitätsaufruf werden dieses Protokoll und der verwendete
Skriptstand committed und veröffentlicht. Der native Zugriffs-Repro liegt zeitlich
davor; daraus werden keine Fragen, Kriterien oder Prompts angepasst.

Unverändert gelten die
[vorher festgelegten Produkt- und Prozesskriterien](Discovery-Remaining-2026-10-29.md):

| Sitzung | Fragen | Grenze |
| --- | --- | --- |
| Orientierung | D2 / D4 / D6 | 180 s |
| Mehrdeutigkeit | D7, ausschließlich die ursprüngliche Alltagsfrage | 120 s |
| Trivialer Direktpfad | D8, ausschließlich die ursprüngliche Texttransformation | 45 s |

Gleicher Snapshot mit 242 operativen Dateien und sechs Overlay-Descriptions,
gleiche Promptbytes, Modell-/Reasoning-Anforderung und Read-only-Gates. Jede
Sitzung hat einen frischen temporären Kontext ohne die Antworten anderer Fälle.
Keine alten Antworten, Rubriken oder Diagnoseartefakte im geprüften Snapshot.
Höchstens drei Starts; technischer Fehler stoppt den Batch, kein Retry/Fallback.

Bewertung erst nach Antworten: fachliche Ergebnisqualität und tatsächliche
Discovery getrennt ausweisen. Bei D7 ist eine gezielte Klärung ein gültiges
Ergebnis; D8 braucht keine Skills oder beobachteten Toolaufrufe. Fehlende Reads
bleiben auch bei plausiblen Antworten ein Prozessbefund. Der koordinierende
Reviewer kennt die Rubrik; Subagentenreview ist keine blinde oder unabhängige
Statistik. Keine Maturity-/Gate-Hochstufung, kein allgemeiner Skill-Lift-Claim.
QMD/Mara und tatsächlicher Index-Refresh bleiben getrennte Aufgaben.

## Ergebnis

Der Qualitätsbatch lief am vorab veröffentlichten Commit
`b72e66da066c01b62b0b4aaf960d7ed6e10fa1d4` mit unverändertem `cc8f8b6`-Snapshot.
[Evidence](Discovery-Remaining-Followup-2026-10-29.json) und
[Antworten](Discovery-Remaining-Followup-2026-10-29-answers.md) sind getrennt.
Bei den veröffentlichten Antworten sind ausschließlich temporäre absolute
Snapshot-Links auf den unveränderlichen `cc8f8b6`-Quellenstand mit gleicher
Zeilenangabe gepinnt.

| Frage | Produkt | Beobachtung |
| --- | --- | --- |
| D2 | pass | Verbesserungsworkflow, Ursachenprüfung, Evidence und menschliche Freigabe gefunden |
| D4 | pass | Strategie und konkrete Fälle unterschieden; keine Grenzwerte ohne Fachanforderung erfunden |
| D6 | partial | Workflow-Datei und Index gefunden; Validierungs- und PR-/Reviewweg in der Antwort fehlen |
| D7 | pass | bedingte Empfehlung und gezielte Klärung des Prüfobjekts |
| D8 | pass | exakt `eins, zwei`; keine beobachteten Tool-Items |

Alle drei CLI-Sitzungen lieferten mit Exit 0 Antworten: Orientierung 54,34 s,
Mehrdeutigkeit 33,88 s und trivialer Fall 6,22 s. Der getrennte Zugriffs-Repro
ist zusätzlich zu diesen drei Qualitätssitzungen zu zählen, insgesamt vier neue
Modellsitzungen. Kein Retry; keine direkte API oder Account-/Konfigurationsänderung.

Der getrennte Prozessreview bestätigt die beobachtbaren Router-, Workflow- und
Description-Reads. In der Orientierung gab es trotz Shell-Exit 0 vier Teilfehler:
einen falschen Skill-Pfad, ein nicht aufgelöstes `*.md` und zwei nicht vorhandene
allgemeine Regeldateien. Die tatsächlich erforderlichen Quellen wurden gelesen;
der kanonische `verification-loop`-Pfad wurde später korrekt nachgeladen. Die
Evidence benennt diese Fehler ausdrücklich. D7 enthält keinen zusätzlichen nativen
`AGENTS.md`-Read; bereitgestellter Bootstrap wird nicht als Tool-Read umgedeutet.
D8 hat ein `agent_message` und keine anderen Tool-Items. Interne Entscheidungen
oder vollständige Filesystem-Isolation werden damit nicht zertifiziert.

Produkt und Prozess wurden getrennt durch Subagenten mit bekannter Rubrik
geprüft (Same-Model-Review). Kein Blindbenchmark und keine statistische
Erfolgsquote. Die fünf Dateien des alten blockierten Batches samt Marker sind
in Namen und SHA-256 unverändert. Frühere Urteile bleiben erhalten.

## Gezielte Nachprüfung von D6 – Vorabprotokoll

D6 bleibt nach der unveränderten Rubrik `partial`. Die Antwort las
`CONTRIBUTING.md`, verwies jedoch nur auf Bedarf/Indexregistrierung und ließ
dessen Validierungs-/PR-Schritte weg. Das beweist keine alleinige Ursache.
Ein konkreter Navigationsbefund ist aber überprüfbar: Im ebenfalls gelesenen
`Workflows/README.md` fehlte ein direkter Beitrags-/Validierungseinstieg.

Die kleine Änderung ergänzt dort ausschließlich Links auf den kanonischen
Index, `CONTRIBUTING.md` und den Local Validation Harness sowie den vorhandenen
`-Quick`-Befehl und PR-/Reviewweg. Keine Skill-, Gate-, Prompt- oder Rubrikänderung.
Für diese Navigation dienen `readme` und `technical-writing`; `docs-review`
prüft Quellen und Links.

Vor der Nachprüfung werden Änderung und dieses Protokoll committed und
veröffentlicht. Der Ausführungscommit ist zugleich der neue geprüfte Quellenstand.
Eine einzelne frische Orientierungssitzung wiederholt **denselben D2/D4/D6-Prompt**
und dieselben drei Kriterien, nicht eine um Validierungshinweise erweiterte Frage.
Gleicher vorhandener `prepare`/`run_one`-Pfad, Modell/Reasoning, erlaubte Aktionen,
neues Byte-/Write-Gate, 180 s Deadline, maximal ein Start, kein Retry.
Nur `Workflows/README.md` darf zwischen den beiden operativen Snapshots abweichen;
die Differenz wird vor Start geprüft. Neue Rohdaten liegen separat unter
`.validation/discovery-d6-recheck-20261029/`.

Ein möglicher Pass wäre eine gezielte Entwicklungsgegenprobe nach Kenntnis des
Fehlers. Er ersetzt das ursprüngliche `partial` nicht und belegt weder allgemeinen
Lift noch Wiederholungsstabilität. D7/D8 werden damit nicht erneut am neuen
Quellenstand geprüft. Bei erneut unvollständiger Antwort bleibt der Befund offen;
keine weitere Reparatur-/Testschleife in diesem Paket.
