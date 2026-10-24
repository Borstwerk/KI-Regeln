# Kandidatenradar: Token-Filter, Session-Kanarienvogel und Agenten-Toolkits

**Status:** `IDEA REGISTERED / STATICALLY SCOUTED / NOT ADMITTED / NOT RUN`
· **Erfasst:** 24.10.2026.

## Ziel

Die [deutschsprachige Guide-Bibliothek von alanbuildz](https://alanbuildz.com/#bibliothek)
nennt über 125 **Guides**, nicht 125 unabhängige Skills.
Sie dient als **Entdeckungshilfe**; Werbe- und Prozentangaben
sind keine reproduzierte Evidence. Die Kandidaten wurden auf ihren
Original-Repositories stichprobenartig statisch geprüft.
**Weder die Guides noch Fremd-Skills wurden kopiert oder installiert.**

Diese Karte hält drei voneinander getrennte **Forschungsfragen** fest:

1. [TE-01 – Token-/Tooloutput-Fidelity](../Evals/Agentenarbeit/Token-Effizienz-Pilot/README.md):
   Headroom vs. RTK vs. kein Filter; bedingte Kombination mit
   dem bestehenden [KG-01-Graph-Pilot](../Evals/Agentenarbeit/Graph-Retrieval-Pilot/README.md).
2. [SQ-01 – Session-Kanarienvogel](../Evals/Agentenarbeit/Session-Quality-Pilot/README.md):
   erkennt ein synthetisches Kontrollsignal verlässlich
   **echte** Qualitätsverschlechterung bei langen Sessions?
3. [OR-01 – Toolkits und Orchestrierung](../Evals/Agentenarbeit/Orchestrierung-Pilot/README.md):
   welche **Methode** von gstack/ECC verbessert vorhandene
   KI-Regeln-Workflows, ohne Dutzende Rollen oder Hooks zu duplizieren?

## Herkunftsschnappschüsse – nur Methodeninspiration

| Originalprojekt | Branch/SHA (beobachtet) | Zweck und vorläufige Einordnung |
| --- | --- | --- |
| [Headroom](https://github.com/headroomlabs-ai/headroom) | `main` / `3fef15d376d9899f77a28464e2e91f8b99514930` | Vor-Modell-Kompression von Logs, JSON, Code und mehr; Apache-2.0 laut Repo. **WATCH: externe Proxy-/MCP-Modi und Cache/Privacy** |
| [RTK](https://github.com/rtk-ai/rtk) | `develop` / `32b2ec4386d90f27255ec984ea7b45ba42bf4694` | CLI-Output-Filter. **Lizenz beachten:** `rtk-oss` Apache-2.0; Voll-Engine/Proxy gesondert BUSL-1.1. **WATCH: Hook-/Routing-Wirkungen** |
| [gstack](https://github.com/garrytan/gstack) | `main` / `00100f1598dcfc192f0f0f2d3345b6825737932a` | Rollen, Reviews, QA und Release-Gates; MIT laut Repo. **WATCH: Installer, Browser, automatische Updates, Multi-Agent-Rechte** |
| [ECC](https://github.com/affaan-m/ECC) | `main` / `90606c8315ee09cafc303515c5f33024db6b9882` | Großes Multi-Harness-Toolkit mit Skills/Agents, Hooks und Memory; MIT laut Repo. **WATCH: sehr breite Install-/Instruktionsoberfläche** |

Die **Lizenz pro ausgeliefertem Paket** muss vor Ausführung/Import
nochmals geprüft werden; GitHub-Metadaten allein sind kein Audit.
ECC-Quelle ist `affaan-m/ECC`, nicht aus fremden Mirrors beziehen.

**Kanarienvogel-Sonderfall:** Der Guide „Der Kanarienvogel:
sieh, wann deine Claude-Session kippt“ beschreibt eine
`CLAUDE.md`-/Chat-basierte Früherkennung von Session-Degradation.
Dieser Guide ist **kein verifiziertes Repository oder reproduzierter
Qualitätsbenchmark**. Die [gstack-`canary`-Funktion](https://github.com/garrytan/gstack/tree/main/canary)
überwacht **nach einem Deployment** und ist **nicht**
derselbe Ansatz. SQ-01 übernimmt nur die zu testende Hypothese.

## Was KI-Regeln schon besitzt

| Beobachteter Bedarf | Existierende Owner/Verträge |
| --- | --- |
| Kleinster ausreichender Kontext | `context-engineering` / `AGENTS.md` |
| Tooloutput-Bloat, Größe und Kosten | `context-audit` |
| Fidelity-schonende Verdichtung | `context-compaction` |
| Fortsetzungsfähigkeit | `session-handoff` |
| Delegieren mit Scope und Human Gates | `delegation-contract` |
| Unabhängige Outcome-/Prozessvergleiche | `agent-eval` |
| Security-/Tool-Admission | `skill-security-review` und `tool-permission-review` |
| Wissensgraph-basierte Vorauswahl | KG-01 **geplant**, noch nicht ausgeführt |

`related` aktiviert keinen Skill. **Neue Skills sind keine
Pilotvorbedingung.** Falls TE-01 einen Mehrwert zeigt, zunächst
Tool-/Adapterfähigkeit erwägen; SQ-01 könnte als Checkpoint in
`context-audit` passen; OR-01 eher als Workflow-Verbesserung
statt eigener universal Orchestrator-Skill.

## Gemeinsame Grenzen

- **Keine Installationen**, Shell-Hooks, globalen Plugins,
  Agenten-CLI-Profile, `AGENTS.md`-/`CLAUDE.md`-Änderungen,
  Provider-Proxys, Portlistener oder Cloud-Konten.
- **Keine** Live-Tokens, Nutzung von Account-Credentials,
  echten privaten Logs, Klinik-, Patienten-, Finanz- oder
  Obsidianinhalten bei den ersten Experimenten.
- Bei später genehmigtem Tooltest erst gepinnte Version,
  SBOM/Transitive-Dependencies, Package-Lizenz, Cache- und
  Telemetrieoptionen, Cleanup, File-Write-/Netz-/Credential-Scope
  und **echte** Runtime-Rechte separat prüfen.
- Synthetische Pass-/Fail-Fälle und unabhängige Ground Truth
  müssen bereits vor dem Runnerlauf feststehen. `TESTS PASS`
  heißt nicht automatisch „Qualität verbessert“.
- Ersparnis bezieht sich **zuerst** auf Bytes/geschätzte
  Eingangstokens einzelner Inhalte; **niemals** aus einem
  Marketingprozentsatz auf Kosten des vollständigen Agentenlaufs
  schließen.
- Standard-Routing, Pflichtreads, Safety- und Freigabe-Gates
  bleiben vollständig erhalten.

## Entscheidungstore

Nach **separater Zustimmung** zu ausführbaren Piloten:
1. TE-01 vor SQ-01 und OR-01, weil Verlust von kritischem Kontext
   die anderen Verfahren beeinflussen würde.
2. SQ-01 nur bei belegbarem Langzeit-/Session-Use-Case und
   neutralen Alarm-/False-Positive-Kriterien.
3. OR-01 als **Methodenvergleich**, nicht gstack/ECC-Komplettinstallation.
4. Erst danach **optional** TE-01+KG-01 koppeln:
   Retrieval-Kandidaten **und** kompakte Toolausgaben als getrennte
   Faktoren testen; keinen gemischten, nicht zurechenbaren Lift behaupten.

**Mögliche Entscheidungen:** `KEEP BASELINE`, `ADOPT ADAPTER`,
`METHOD TRANSFER`, `ITERATE`, `INCONCLUSIVE`, `REJECT`.
Es gibt noch keinen tatsächlichen Ergebnisbericht.
