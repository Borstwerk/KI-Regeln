# Lokale Regelsuche: Runtime und Skill-Routing

## Vorabkriterien

Getrennte Erweiterung des [72-Dokumente-Nachweises](Local-Rule-Search-2026-10-30.md),
ohne dessen Evidence zu überschreiben. Die optionale BM25-Suche soll alle
katalogisierten kanonischen Skills als mögliche Routing-Kandidaten verfügbar
machen. Kein Modellaufruf, keine direkte API, keine allgemeine Agentenplattform.

1. Der Routing-Build enthält alle 155 Katalog-Skills und zehn Einstiegsdokumente;
   alle erwarteten aktiven QMD-Pfade müssen vorhanden sein. Die vorhandenen
   Manifestbudgets bleiben unverändert, der Inhaltsindex getrennt.
2. Treffer liefern kanonische Skill-Description, ID, Maturity, Eval-Coverage,
   Quellpfad und Revision, höchstens zehn Kandidaten je Anfrage. Keine automatische
   Ownerwahl. `AGENTS.md` und Master-Router erklären Nutzung, Originalprüfung und
   Fallback auch bei leeren oder unpassenden Treffern.
3. Katalog, Workflow-Index und Overlay-Registry sind Quellenabhängigkeiten.
   Geänderte Abhängigkeiten, ungültige Descriptions, fehlende oder doppelte
   Katalogquellen dürfen keinen bereiten Index ergeben.
4. Normale Windows-PowerShell ohne Codex-PATH kann eine bereits vorhandene
   Runtime verwenden. Ein expliziter ungültiger Node-Pfad wird nicht ersetzt.
   Setup verändert den dauerhaften PATH nicht und aktiviert keine Installationsskripte.
5. Vier bekannte Entwicklungsfragen müssen den erwarteten Skill unter höchstens
   zehn Treffern enthalten; alle vier Skills liegen außerhalb des Inhalts-Piloten.
   Ein vorab benannter nicht vorhandener Begriff muss null Treffer liefern.
   Originalbytes bleiben unverändert.

| Suchbegriff | Erwarteter Skill |
| --- | --- |
| `Rechtschreibung Zeichensetzung` | `korrekturlektorat` |
| `DCF Comparable Companies` | `bewertungsanalyse` |
| `Figuren Motivation Agency` | `figurenentwicklung` |
| `Architekturentscheidungen Alternativen Konsequenzen` | `adr` |
| `zzroutingabsentf72ea4bd` | leere Trefferliste |

Der feste [native Prüflauf](run_rule_routing_native.py) installiert nichts und
schreibt Protokoll und Ergebnis je Ausführung unter `.validation/native-rule-routing-*/`:

```powershell
.validation/runtime/venv/Scripts/python.exe Evals/Onboarding/run_rule_routing_native.py --run
```

Controller-Tests mit synthetischen Git-Repos und Fake-Worker sind von den echten
QMD-Läufen getrennt. Quellenabdeckung bedeutet keine vollständige Relevanz pro
Anfrage. Die Fälle sind aus lokalen Quellen abgeleitete Entwicklungsfragen,
kein unabhängiger Retrieval-Benchmark. Agentische Skill-Auswahlqualität,
semantische Suche und andere Plattformen bleiben separat `NOT RUN`/`UNVERIFIED`.

## Ergebnis

Die Ausführung und ihre Commit-/Codebindung werden nach dem eingefrorenen
Vorabstand ergänzt. Bis dahin: **NOT RUN** für den erweiterten nativen Routinglauf.
