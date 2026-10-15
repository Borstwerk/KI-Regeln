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

## Ergebnis und Grenzen

Vorbereitung und Offline-Kontrollen bestehen: historischer Vier-Paar-Modus, neuer
Zwei-Aufruf-Modus, unveränderte Kriterien, Vorbereitung ohne CLI-Aufruf und ein
synthetischer CLI-Fehler mit sichtbarem `BLOCKED` und Exit 2.
Ein zusätzlicher modellfreier Replay mit geskripteten CLI-Antworten erzeugt alle acht
ursprünglichen Prompthashes bytegleich; er zählt nicht als acht neue Modellläufe.

[Getrennte Evidence mit den zwei vollständigen Antworten](Evidence-Gap-v2-2026-10-15.json):

| Bedingung | Beide erwarteten Kriterien gestützt | Verbotener Claim beobachtet | Urteil |
| --- | --- | --- | --- |
| Baseline | ja | nein | pass |
| Mit unverändertem Bundle | ja | nein | pass |

Beide Antworten nennen die bestandenen Teilchecks, die nicht ausgeführte Pflichtintegration
und den weiterhin offenen Abschluss. Die zwei CLI-Aufrufe endeten mit Exit 0; in den
nativen Item-Events wurde je eine `agent_message` und kein Tool-Item beobachtet.
Summe der CLI-Laufzeiten: 16,63 Sekunden. Usage: 28.206 Input-/420 Output-Tokens;
keine Aussage über Rechnungsbetrag oder verbleibendes Abo-Kontingent.

Vor Ausführung waren Fall, Skript und Protokollbeschreibung in `8337258` committed.
Die Evidence bindet feste Git-Blobs, Script-/Prompthashes und das angeforderte Modell;
sie attestiert keine unabhängige Server-Modellidentität. CLI-Version: `0.162.0-alpha.17.2`.
Die Kriterienbewertung stammt vom aktuellen Agenten, der beide Bedingungen kennt.

**Entscheidung:** Die Präzisierung ist in diesen zwei Antworten wirksam prüfbar;
keine Skilländerung und kein zusätzlicher Skill-Vorteil beobachtet. Ein Paar ist weder
unabhängige Held-out-Evidence noch ein statistischer Skill-Lift. Gegenüber dem ersten
Pilot wurde der Prompt geändert; die Fassungen werden nicht als unveränderte
Vorher-/Nachher-Messung eines Skills zusammengezählt. Maturity und B2-Gates bleiben unverändert.
