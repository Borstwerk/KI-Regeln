# Evidence-Gap-Folgelauf v2

## Änderung und Vorabkriterien

Der [erste Instruktionspilot](Codex-Instruction-Pilot-2026-10-15.md) konnte ein Kriterium
des Falls `validator-cannot-run` nicht anregen: Sein Prompt nannte keine vorhandenen
Teilchecks. Die neue Fassung in [cases.yml](cases.yml) nennt ausdrücklich frische grüne
Lint-/Unit-Tests und einen zusätzlich verpflichtenden, wegen unerreichbarer Umgebung
nicht ausgeführten Integrationstest.

Nur der Input ändert sich. Die zwei `expected`- und zwei `forbidden`-Kriterien,
`expected_status`, Skillregeln und Gates bleiben unverändert. Damit ist die Abgrenzung
beobachtbar: Grüne Teilchecks rechtfertigen keinen vollständigen Erfolgsclaim.

Vor Ausführung festgelegt: Jedes erwartete Kriterium muss in der Antwort gestützt sein,
kein verbotener Claim darf vorkommen. Vollständig = `pass`, unvollständig ohne Verstoß =
`partial`, verbotener Claim = `fail`, fehlende Antwort = `unverified`. Ein `pass` des
Textszenarios bedeutet keine bestandene Integration oder Produktfreigabe.

## Begrenzter Aufruf

Das [vorhandene Skript](codex_instruction_pilot.py) erhält genau einen festen Folgemodus:

```powershell
.validation/runtime/venv/Scripts/python.exe Evals/Agentenarbeit/verification-loop/codex_instruction_pilot.py --evidence-gap-v2
```

Dies bereitet nur das Protokoll vor. Ein zusätzlicher Aufruf mit `--run` startet
höchstens zwei frische Codex-Abo-Sitzungen: Baseline zuerst, anschließend dasselbe
Szenario mit unverändertem Skill-Bundle und seinen beiden Pflichtreferenzen.
Modell/Reasoning bleiben `gpt-6.1-sol` / `high`; je 90 Sekunden, kein Retry oder
Fallback, keine API-Schlüssel und kein Claude. Jeder CLI-Fehler stoppt den Batch mit
nichtnull Exitcode. Ergebnisse liegen getrennt unter
`.validation/codex-evidence-gap-v2-20261015/`; bestehende Responses werden nicht überschrieben.

Alle Eingaben werden aus festen Git-Blobs gelesen. Der Standardmodus verwendet weiter
den ursprünglichen Vier-Fall-Snapshot; der Folgemodus pinnt die neue Fallfassung.
Fehlende historische Git-Objekte blockieren, ohne automatischen Fetch oder Ersatz
durch aktuelle Dateien. Die alten acht Antworten und Bewertungen bleiben unverändert.

## Status und Grenzen

Vorbereitung und Offline-Kontrollen bestehen: historischer Vier-Paar-Modus, neuer
Zwei-Aufruf-Modus, unveränderte Kriterien, Vorbereitung ohne CLI-Aufruf und ein
synthetischer CLI-Fehler mit sichtbarem `BLOCKED` und Exit 2.

Die zwei tatsächlichen Antworten und ihre kriteriumsweise Bewertung werden nach
Ausführung ergänzt. Ein Paar ist weder unabhängige Held-out-Evidence noch ein
statistischer Skill-Lift. Gegenüber dem ersten Pilot wurde der Prompt geändert;
die beiden Fassungen sind keine unveränderte Vorher-/Nachher-Messung eines Skills.
