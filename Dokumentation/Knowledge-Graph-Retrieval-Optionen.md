# Ideenkarte: Wissensgraph-Retrieval in KI-Regeln

**Status:** `CANDIDATE / DEFERRED` · **Dokumentiert:** 17.10.2026 ·
**Keine Implementierungs-/Admission-Freigabe**.

**Leitfrage:** Kann ein nachweisbar korrekter, quellgebundener Graph
die Auswahl und das Verständnis von KI-Regeln verbessern **und** Kontext
einsparen, ohne zusätzliche Wahrheiten oder unnötige Skills aufzubauen?

Dazu gibt es den geplanten
[KG-01-Dreifachpilot](../Evals/Agentenarbeit/Graph-Retrieval-Pilot/README.md).
Die zwei produktiven Zukunftswege **bleiben bewusst offen**:

## Option G – Externes Graphify-Projekt nutzen

**Kandidat:** [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify);
[Vorprüfung](Reviews/Graphify-Labs-graphify-2026-10-17.md).

**Einsatzidee:** Bei großen oder schwer überblickbaren Code-/Dokurepos
eine optionale, lokal und read-only betriebene Graph-Retrieval-Capability
mit `query`, `path`, `explain` und Quellprovenienz. Ein Agent nutzt
diese Capability nur für einen erkennbaren Retrievalbedarf.

**Was wir explizit NICHT übernehmen:**
- kein `graphify install` auf dem KI-Regeln-Arbeitsrepository;
- keine globalen Agenten-Instruktionen, Auto-Hooks, `PreToolUse`-Guards
  oder Änderungen an `AGENTS.md`;
- kein automatisches Semantik-/API-Scanning aller Markdown-Dokumente;
- keine ungeprüfte Übernahme von Upstream-Graphkanten als Norm;
- keine Abhängigkeit vom Cloud-Dienst oder 80-%-Marketingversprechen.

**Weiterverfolgen nur wenn:** Paket-/Dependency-/Hook-/MCP-Admission
separat bestanden; lokale Offline-Queries eine relevante Verbesserung
gegenüber bestehenden Suchen liefern; Token-/Aufwandsledger und
Quality-Gates das belegen. Im Fall eines späteren Einsatzes einen
**schmalen Runtime-Adapter** statt kopierter Upstream-Skills erwägen.

## Option N – KI-Regeln-eigene Graphlösung

**Projektidee:** Ein kleines, versioniertes, deterministisches
**Index-/Abfragemodul** für KI-Regeln, unabhängig von Graphify.

Die Quellwahrheit bleibt in `AGENTS.md`, `skill-catalog.yml`,
`workflow-index.yml`, `routing-overlays.yml`, den einzelnen
`SKILL.md` und Workflows. Ein Index bildet höchstens **verifizierte**
Metadatenbeziehungen ab. Er soll kein allgemeines GraphRAG, keinen
neuen Datenbankserver und keine dauernde LLM-Zusammenfassungsmaschine
werden.

**Mögliche Knoten:** `skill`, `workflow`, `area`, `source`,
`checkpoint`.

**Mögliche Kanten:** `registered_in`, `belongs_to`,
`related_to`, `referenced_by`, `indexed_workflow`,
`overlay_candidate_at`; `required_owner_of` **nur wenn**
im kanonischen Workflow ausdrücklich so bezeichnet.

**Minimale Provenienz:** `source_path`, `source_line`/
`yaml_key`, `source_sha256`, `edge_type`,
`confidence=EXPLICIT` (explizite Quelle) oder separat
`INFERRED` (unsichere Hypothese). Kein Rankingwert wird zu einer
Ermächtigung oder zu einem Pflichtrouting.

**Erforderliche Eigenschaften:**
- keine Runtime-Erweiterungen, bevorzugt bestehendes Python/PyYAML;
- stabile, OS-portable relative POSIX-Pfade (Windows/Linux);
- deterministische Indizes; keine Credentials, Netzwerkaufrufe,
  Agentenhooks oder privilegierten Git-Operationen;
- stale-check vor Verwendung, klare `NOT_INDEXED`-/`STALE`-Antwort
  und Fallback auf Originalquellen;
- keine Duplikation vollständiger Skill-/Workflowtexte im Graph,
  sondern Referenzen und kleine, explizit sourced Metadaten;
- messbare Indexgröße, Bau-/Updatezeit und Queryqualität;
- Index als **wegwerfbares Derived Artefact**, nicht in Katalog oder
  Routing-Registry als zusätzliche Wahrheit einschreiben.

### Option N2 – Eigener Skill `graph-retrieval` (nur Designkandidat)

**Bewusst getrennt vom Projektmodul:** Ein möglicher eigener
`SKILL.md` wäre ein **fachlicher Nutzungskontrakt** für
„Finde/erkläre belegte Beziehungen in einem bereits existierenden
Wissensgraphen, liefere Pfad und Originalquellen“.

- **Positive Trigger:** ausdrückliche Abfrage eines vorhandenen Graphen,
  Pfad-/Impact-Analyse, quer über viele Quellen verteilte
  Beziehungen mit belegter Retrieval-Notwendigkeit.
- **Near-Misses:** triviale Textsuche, normale Fachaufgabe,
  allgemeines Context Engineering, `knowledge-query` ohne echten
  Graph-Mehrwert, Build/Installation eines Graphen.
- **Inputs:** konkrete Graph-Capability, Snapshot/Schema, erlaubte
  Datenbasis, Frage, Scope und Provenance.
- **Output:** kleinster passender Subgraph, explizite Pfade und
  Quellreferenzen, Unschärfe-/Staleness-Hinweise, `NOT_RUN` wenn
  Graph nicht verfügbar.
- **Rechte:** nur READ; Indexbau/Installationen/Scanning und
  Autoaktivierung sind **nicht** Skill-Aufgaben.
- **Owner-Kollision prüfen:** zunächst `knowledge-query`
  (Retrieval), `context-engineering` (aktiver Kontext) und
  `skill-authoring` (falls Skill nötig) gegenüberstellen.
- **Admission-Kriterium:** erst eigenständigen beobachtbaren Job
  plus zuverlässigen positiven und negativen Trigger sowie einen
  nachgewiesenen Mehrwert gegenüber bestehender Komposition belegen.
  Ohne diesen Nachweis **kein neuer Skill**, sondern Tool-Adapter /
  `knowledge-query`-Workflow-Ergänzung.

**Aktuell existiert keine `graph-retrieval/SKILL.md`, kein Eintrag
im `skill-catalog.yml` und kein globales Overlay.** Das ist
absichtlich der Status: **Idee sichtbar, Architektur noch offen**.

## Entscheidung nach KG-01

| Befund | Handlung |
| --- | --- |
| A erreicht gleiche Qualität billiger/schneller | Kein Graph, Konzept zurückstellen |
| B liefert Vorteil, Scope/Sicherheit geprüft | Graphify als **optionales externes Tool** pilotieren |
| C liefert Vorteil ohne zusätzliche Runtime-Komplexität | Kleines natives Indexmodul gesondert umsetzen |
| B und C sind auf verschiedenen Corpusarten nützlich | Optionale Adapter nach Corpusart; keine globale Pflicht |
| Nachgewiesener eigener `graph-retrieval`-Job | Erst dann Skill-Design und separate Skill-Evals |
| Unklare Daten / geringe Stichprobe / schlechtere Gates | `INCONCLUSIVE` oder `REJECT`; keine Promotion |

**Wichtig:** Ein Graphindex ersetzt kein Problem-first Routing.
`AGENTS.md`, der verbindliche Bootstrap-Read-Vertrag und aktuelle
kanonische Originalquellen behalten Vorrang.

## Schnittstellen zu bestehenden Bausteinen

- [Context Engineering](../Agentenarbeit/Skills/context-engineering/SKILL.md)
  – aktiven Kontext begrenzen, nicht Indexinhalt zum Wahrheitsersatz erheben;
- [Context Audit](../Agentenarbeit/Skills/context-audit/SKILL.md)
  – echten Context-/Token-/Latency-Effekt messen;
- [Knowledge Query](../Wissensmanagement/Skills/knowledge-query/SKILL.md)
  – auf Provenienz und Frische grounded antworten;
- [Knowledge Base Design](../Wissensmanagement/Skills/knowledge-base-design/SKILL.md)
  – langlebiges Modell und Beziehungen entwerfen;
- [Agent Eval](../Agentenarbeit/Skills/agent-eval/SKILL.md)
  – A/B/C mit natürlichen und negativen Routingfällen prüfen.

**Nächste Entscheidung:** KG-01-Versuchspaket reviewen,
Security-Admission von Graphify vorbereiten und erst nach
expliziter Pilotfreigabe Runner oder Indexcode bauen.
