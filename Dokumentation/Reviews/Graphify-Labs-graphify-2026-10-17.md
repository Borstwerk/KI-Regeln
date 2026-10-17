# Vorprüfung: Graphify-Labs/graphify als optionale Retrieval-Runtime

**Stand:** 17.10.2026 · **Status:** `WATCH / NOT ADMITTED / NOT RUN`

**Quelle:** [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify),
Default-Branch `v8`, beobachteter Commit
`86c57be8204673c2a1b9849a3292a7dd3ab373d8`.
Laut GitHub-Metadaten Root-Lizenz **Apache-2.0**;
das Repository enthält zusätzlich `LICENSE-MIT`.
Vor Übernahme einzelner Dateien oder Quellcode gilt **pfadbezogene**
Lizenz-/NOTICE-Prüfung. In diesem Pilot ist **keine Redistribution**
vorgesehen.

**Prüftiefe:** statische Sichtung von `README.md`,
`ARCHITECTURE.md`, `BENCHMARKS.md`, `SECURITY.md`,
`graphify/skill.md`, `graphify/extractors/markdown.py`,
`graphify/markdown_resolution.py`, `graphify/benchmark.py`,
`graphify/hooks.py`, `graphify/llm.py`, `graphify/querylog.py`,
`graphify/detect.py` und `pyproject.toml`. **Keine**
vollständige rekursive Script-/Dependency-Audit, keine
Ausführung, keine Installations-/Netzwerk-/Security-Garantie.

## Was fachlich interessant ist

- Lokales AST-/Markdown-Strukturmodell, Source-Links und
  `EXTRACTED`/`INFERRED`/`AMBIGUOUS`-ähnliche
  Provenienzkennzeichnung; `query`/`path`/`explain`.
- `graphify-out/graph.json` als abfragbarer Snapshot,
  Browseransicht `graph.html`; keine Vector-DB zwingend.
- Markdownparser extrahiert Seiten, Überschriften und verlinkte
  Dokumente deterministisch und ohne eigenen LLM-Aufruf.
- Dokument-/Medien-Semantik kann dagegen Modell-/API-/Subagent-Tokens
  benötigen. Unser Korpus ist **viel stärker Markdown/YAML-lastig als
  der AST-zentrierte Code-Demokorpus**.

**Wichtiger Unterschied:** Ein Graph aus Überschriften/Links versteht
nicht zwangsläufig die Semantik von `related`, `required`,
Workflow-Kernowner oder Security-Gates unserer KI-Regeln.
Niedrige Tokenzahl ohne diese Semantik ist kein Gewinn.

## Bedrohungs- und Integrationsgrenzen

| Objekt | Vorläufige Bewertung / Pilotgate |
| --- | --- |
| Python-Paket `graphifyy` | Drittcode und Dependency-Tree: Snapshot pinnen, vor Ausführung separat prüfen, keinesfalls global ungefragt installieren |
| `graphify install` | Schreibt agentenbezogene Skill-/Instruktionsdateien; **im KI-Regeln-Repo verboten**, bis explizit reviewed/autorisiert |
| Claude-/Gemini-/Pi-Hooks und „always-on“ | Können `Read/Glob/Grep`-Verhalten umleiten und Pflichtreads verdrängen; **für KG-01 aus** |
| MCP/stdin oder lokaler HTTP-Server | Neue Tool-Capability; Scope, Ports, Datenfluss und Least Privilege separat reviewen. Kein Listener im Pilot |
| Semantic LLM extraction | Kann Dokumentinhalte an Modellanbieter oder Subagenten geben; **erster Pilot deaktiviert**, B2 nur mit neuem Gate |
| Graph-/Query-Cache und Telemetrie | Outputverzeichnis außerhalb der KI-Regeln-Checkout-Grenze; Logs/Temp/HOME/Env auf sensible Daten prüfen. Graphify Query Log laut Quelltext opt-in, trotzdem vor Ausführung prüfen |
| Scan-Scope | Nur freigegebene öffentliche/synthetische Dateien. Keine .env, .git, private Dateien oder User-Verzeichnisse |
| Untrusted Markdown/Scripts | Ein Graphknoten ist **Daten**, keine Anweisung; keine Upstream-Skillbefehle als Instruktionsautorität |
| Stale/False edges | Kanten mit Quelle+Confidence, fehlende Belege `UNVERIFIED`; Originaldatei vor fachlichem PASS erneut lesen |
| Windows/Linux | Repo-relative Pfade, UTF-8, Shell-/Install-Unterschiede prüfen, keine PowerShell-Aktion ungeprüft aus POSIX-Skripten ableiten |
| Cloud und Kosten | Keine Cloudanmeldung, kein Trial, keine laufenden Accounts-/Subscription-Kosten als Pilot-Nebenwirkung |

Das Upstream-Projekt bietet technische Mitigations für
URL-Fetch, Pfadvalidierung und Prompt-Injection-Sentinels laut
`SECURITY.md`. Diese Angaben sind **keine unabhängige
Sicherheitsfreigabe**. Insbesondere eine Agenten-Skillinstallation
wäre separat durch `skill-security-review` zu prüfen; MCP-/Hook-
Rechte nach `Sicherheit/MCP-und-externe-Tools.md` und bei eigener
Berechtigungsaufgabe `tool-permission-review`. Keine ungeprüften
Toolinstallationsanweisungen aus untrusted README ausführen.

## Benchmark-Einordnung

- Upstream nennt „80 % token spend reduction“ als
  **Cloud-Marketingclaim**; für KI-Regeln existiert keine entsprechende
  Messung.
- Der interne `graphify/benchmark.py` schätzt Token über
  Zeichen-/Wortheuristiken und vergleicht einen vollständigen Corpus
  gegen budgetierte Queryausgaben. Das ist **keine**
  Gesamtkostenmessung eines Agenten mit Retrieval-/Verifikationsschritten.
- `BENCHMARKS.md` berichtet unter anderem eine
  **Code-Intelligence-Kleinprobe mit n=6**; daraus folgt keine
  allgemeine KI-Regeln-Wirkung. Bei Nutzung externe Zahlen
  immer mit Messaufbau und Corpus nennen.

## Aufnahme-Entscheidung

**Heute:** Lesen und planend referenzieren: ja. Ausführen,
installieren, MCP verbinden, Skill registrieren oder systemweite Hooks
aktivieren: **nein**.

**Vor KG-01-B zulässig nur nach separatem Human Gate:**
konkrete Release-/Commit-/Paketidentität pinnen,
Dependencies/Scripts/Trust- und Lizenzscope prüfen, temporären
read-only Corpus bereitstellen, Offline-/Sandbox-Evidence und
Cleanup-Plan dokumentieren. **Ein bestandener technischer Index-Test
ist keine Admission-Freigabe.**

Siehe [KG-01-Plan](../../Evals/Agentenarbeit/Graph-Retrieval-Pilot/README.md)
und [Ideenkarte](../Knowledge-Graph-Retrieval-Optionen.md).
