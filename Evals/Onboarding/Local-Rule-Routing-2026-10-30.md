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

Der Code und die Kriterien wurden vor Ausführung in
`ebe392e803e4b47c7bdc64238385be8da028681e` eingefroren. Die
[maschinenlesbare Evidence](Local-Rule-Routing-2026-10-30.json) enthält das
vollständige native Ergebnis, normale PowerShell-Proben und den gesonderten
Follow-up. Code-, Lockfile-, Protokoll- und Rohbericht-Hashes bleiben darin gebunden.

| Teil | Beobachtung | Status |
| --- | --- | --- |
| Vollständiger nativer Bestand | 165 aktive Dokumente, alle 155 katalogisierten Skills | PASS Quellenabdeckung |
| Rechtschreibung, Bewertung, Figuren | erwartete Skills jeweils unter den zehn Kandidaten | PASS für diese drei Fragen |
| Architekturfrage wie vorab formuliert | null Treffer; `adr` nicht gefunden | FAIL Retrievalfall |
| Nicht vorhandener Begriff | null Treffer | PASS |
| Originalbytes | alle 165 ausgewählten Quelldateien vor/nach dem Lauf unverändert | PASS |
| Normale PowerShell ohne Node/pnpm im PATH | Setup Exit 0, Inhaltsbuild 72 Dokumente, ursprüngliche Anfrage fünf Treffer | PASS lokal Windows |
| Expliziter ungültiger Node-Pfad | Exit 2, `runtime-missing`, kein Ersatz durch vorhandene Runtime | PASS |
| Prozess-PATH nach Setup und Suche | unverändert | PASS |

Der vorab definierte native Fragensatz ist damit **PARTIAL**, nicht vollständig
bestanden: drei von vier positiven Suchfällen gelingen, der Leertrefferfall gelingt.
Der feste Runner behält den fehlgeschlagenen Fall und seinen Fehlerexit bei.

### Gesonderter Follow-up nach dem Fehlfall

Die Frage `Architekturentscheidungen Alternativen Konsequenzen` findet den Skill
nicht. Die kanonische Description verwendet „Architektur-“ und „Architecture
Decision Record“. BM25 behandelt diese Formulierungen nicht als gleichbedeutend.
Nach Kenntnis dieses Fehlers wurde separat geprüft:

- `rg -n -i 'Architekturentscheidungen' skill-catalog.yml` findet den Katalogeintrag `adr`;
- `Architecture Decision Record Alternativen` findet `adr` mit echtem QMD.

Das belegt den dokumentierten Katalog-Fallback und einen begrifflich präzisierten
Suchfall. Es verbessert den ursprünglichen Wert **nicht rückwirkend** und ist
keine unabhängige Qualitätsmessung. Die Suche bleibt optional; Pflicht-Discovery,
kanonische Descriptions und Workflow-/Overlay-Checks tragen das Routing.

### Controller- und Review-Evidence

69 relevante lokale Unit-Tests: OK, ein bestehender Windows-Symlink-Skip.
Davon 29 Suchcontroller-/Runtime-Methoden und zwölf Routingmethoden mit
synthetischen Git-Repositories bzw. prozessfreien Runtime-Fixtures; keine davon
ist ein QMD-Engine-Nachweis. Ein zunächst durch Windows-Pfadaliasing maskierter
ID-Duplikat-Test wurde isoliert, tatsächlich rot beobachtet und durch kanonische
ID-/Duplikatprüfung korrigiert. Ein leerer expliziter Node-Override ist ebenfalls
regressionsgeprüft. Ein getrenntes Source-Review meldet keine offenen P1/P2.

Agentische Skill-Auswahlqualität und vollständiger Recall bleiben **UNVERIFIED**;
Semantik und andere Plattformen **NOT RUN**. Keine Maturity-Hochstufung.
