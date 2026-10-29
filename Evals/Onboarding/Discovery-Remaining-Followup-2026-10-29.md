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

Vorabprotokoll; noch keine Qualitätsantworten dieses Folgebatches.
