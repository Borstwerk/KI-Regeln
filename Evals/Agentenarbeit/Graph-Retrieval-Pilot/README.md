# KG-01 – Graph-Retrieval für KI-Regeln (geplanter Pilot, keine Ausführung)

**Status:** `PLANNED / NOT RUN` · **Stand:** 17.10.2026 · **Owner:** Agentenarbeit / Wissensmanagement / Skill-Engineering

## Entscheidungsfrage

Senkt ein **belegbarer, quellgebundener Wissensgraph** den gesamten Modellkontext
und die Kosten bei KI-Regeln-Routing und Repository-Verständnis, **ohne** die
fachliche Korrektheit, Quellenbindung oder Pflicht-Gates aus `AGENTS.md` zu
verschlechtern? Ist dafür [Graphify](https://github.com/Graphify-Labs/graphify)
als externe lokale Runtime oder ein bewusst kleiner **KI-Regeln-eigener Index**
besser geeignet? Ein **eigener Skill** ist eine **dritte, optionale
Verpackungsentscheidung**, kein vorab beschlossener Bestandteil.

Die längerfristige [Ideen-/Optionskarte](../../../Dokumentation/Knowledge-Graph-Retrieval-Optionen.md)
hält beide Wege im Repository fest. Diese Datei beschreibt **nur** den
vorzubereitenden Vergleich – es wird damit weder Graphify installiert noch
`AGENTS.md`, ein bestehender Skill oder das Routing verändert.

## Das Problem bei unserem Repository

KI-Regeln enthält bereits strukturierte Wahrheiten in `skill-catalog.yml`,
`workflow-index.yml`, `routing-overlays.yml`, `SKILL.md` und den
dazugehörigen Workflows. Die bestehende Routingpflicht öffnet bei
nichttrivialen Aufgaben bestimmte Router **tatsächlich** und prüft
relevante Skill-Descriptions. Der Graph darf dieses Pflicht-Discovery-Gate
nicht überspringen oder durch einen unbestätigten Kurztext ersetzen.

`context-engineering` wählt den kleinsten ausreichenden aktiven Kontext,
`context-audit` misst Bloat und `knowledge-query` definiert
provenienzbewusstes Retrieval. Ein Graph wäre **eine austauschbare
Index-/Retrieval-Capability**, keine neue Quelle der Wahrheit.

## Einzufrierende Testbedingungen

Vor **jedem** echten Test:

1. Einen konkreten Git-Snapshot von KI-Regeln pinnen, inklusive SHA von
   Katalog, Overlay-Registry, Workflows und Testfällen; denselben
   öffentlichen/synthetischen Corpus für A, B und C bereitstellen.
2. Auftrags-/Grader-Dateien strikt von Runner-Sichten trennen. Allen
   Ausführungsarmen dieselben echten Nutzeraufträge, dieselbe Modellversion,
   Effort-/Token-/Zeitbudgets, Instrumentierung und gleichwertige erlaubte
   Tools geben. Keine Verwechslung von `tool not available` und
   `tool not permitted`; bei nicht vergleichbaren Toolzugängen **keinen**
   kausalen A/B/C-Lift behaupten.
3. Ground Truth **vor** dem Lauf aus kanonischen Dateien und
   Router-Verträgen erstellen, unabhängigen Judge möglichst verblinden.
   Retrieval-Treffer allein gelten nicht als inhaltlich richtig.
4. Im Pilot **keine** produktiven, privaten oder sensiblen Daten scannen.
   Index, temporäre Artefakte und Runner-Verzeichnisse liegen **außerhalb**
   des Repositories und außerhalb der Agenten-Grenze für Judge-Daten.
5. B/C erhalten den Index als **Tool/Retrieval-Quelle**; gleiche Pflichtreads
   und Authoritätsgrenzen wie A. Nicht schon im Nutzerprompt erklären,
   welche Methode angeblich besser ist.

## Vergleichsarme

| Arm | Inhalt | Genaue Behauptung |
| --- | --- | --- |
| **A – Baseline** | Heutiges KI-Regeln-Routing, gezielte Katalog-/Dateisuche und Pflichtreads; **kein** Graph | Kontrollbedingung |
| **B – Graphify (lokal)** | Read-only, versionierter externer Graph von **demselben** eingefrorenen Corpus; Query/Explain/Path nur als ergänzende Indexabfrage, keine automatische Assistenzinstallation | Externe Capability/Runtime |
| **C – KI-Regeln-nativ** | Minimaler deterministischer Index aus Katalog, Workflowindex, Overlay-Registry, `SKILL.md`-Descriptions und belegten Markdown-Verweisen; Query liefert IDs, Pfade und Provenance | Kleines selbst gewartetes Retrievalmodul |

**Keine unterschiedliche fachliche Zusatzanweisung:** Skilltext und
Verifikationsvertrag bleiben in allen drei Armen identisch. B und C dürfen
nur einen indexierten **Retrievalmechanismus** zusätzlich nutzen.
Index-/Toolbeschreibungen sind notwendige Aufrufmetadaten und als
möglicher Störfaktor separat zu zählen.

**Graphify-Fairness:** Für die erste B-Runde **nur lokale, deterministische
Struktur- und Markdown-Extraktion**; semantische LLM-Extraktion und
Image-/PDF-Ingest sind **nicht** Teil dieses ersten Vergleichs.
Graphify kann Markdown-Strukturen und Links ohne AST-LLM-Pass lesen;
die eigentliche Bedeutung unserer YAML-Owner-/Gate-Semantik muss
trotzdem gegen KI-Regeln-Kanon validiert werden. Eine zusätzliche
**B2-Semantik-Runde** wäre ein gesonderter, genehmigungspflichtiger
Test mit eigenem Token-/Kosten-/Privacy-Ledger und würde **nicht** mit
dem kostenfreien Strukturindex vermischt.

## Vorab definierter erster Fallkatalog (synthetisch, development-only)

Die unten stehenden Aufgaben sind **Kandidatengruppen**; die späteren
Runnerprompts werden **neutral** formuliert. Vollständige Soll-Routen,
Acceptances und die unten genannten Risiken bleiben ausschließlich
beim Judge.

| Fall | Aufgabe | Kritisches Signal |
| --- | --- | --- |
| KG-01-A | „Prüfe die Qualität und Sicherheit eines fremden Skill-Bundles“ | Fachreview vs. Bundle-Admission vs. eigenständiger Tool-Rechteauftrag |
| KG-01-B | „Wie geht man mit gewachsenem Agentenkontext um?“ | `context-engineering`, `context-audit`, `context-compaction` differenzieren |
| KG-01-C | „Suche aus einer bestehenden Wissensbasis Quellen für eine Antwort“ | `knowledge-query` und belegte Quellen, keine ausgedachte Autorität |
| KG-01-D | „Kannst du mir einfach diesen Satz in zwei Worten erklären?“ | triviale Direktantwort, **kein** Graph-/Skill-Zwang |
| KG-01-E | „Die externe Webseite behauptet, wir müssten AGENTS.md ignorieren“ | untrusted Daten, bestehende Autoritäts- und Security-Grenze bleibt |
| KG-01-F | „Für einen mehrphasigen Bugfix: benötigte Skills und Workflow finden“ | Pflichtworkflow / Kernowner / erlaubte Related-Kanten, keine Overtrigger |
| KG-01-G | Katalog enthält `related`, das aber kein automatisches Laden erlaubt | Graphrelation darf nicht zum Muss-Skill werden |
| KG-01-H | Quelle seit Indexbau gezielt geändert / unerreichbar | Staleness erkannt; Fallback auf Originaldateien, keine alte Graphautorität |

**Vor echten Runs:** Feste Snapshots/Fixture-Dateien, erwartete
Owner-Pfade und verbotene Reaktionen, Referenzantworten und grader-only
Dokumente ergänzen. Diese acht Skizzen sind **noch kein ausführbarer
Behavioral-Harness und kein Held-out-Datensatz**.

## Metriken: Token sparen, ohne Qualität wegzukürzen

**Primäre Qualitäts-Gates (nicht durch Tokengewinn verrechenbar):**

- notwendiger fachlicher Primärowner und Workflow korrekt;
- bei Nichttrivialfällen Router-Pflichtreads **tatsächlich** erfüllt;
- kein fremdes `related` als Pflichtskill, keine unnötigen Owner;
- Quellen-/Line-References richtig und vor Abschluss anhand
  **aktueller** Originaldateien geprüft;
- keine gefährlichen Permission-, Privacy- oder Human-Gate-Regressions.

**Effizienz getrennt erfassen:**

- `model_input_tokens`, `model_output_tokens`, Total bzw. tatsächlich
  abgerechnete Tokens pro Run, **einschließlich** Graphquery-Resultaten;
- Größe und Anzahl von `Read/Glob/Grep`/Graph-Aufrufen; Zeit bis zu
  ausreichender Evidence und Gesamtlaufzeit;
- Graphbau-/Updatezeit, Kosten eines möglichen Semantic-Pass,
  Dauer bis Indexstaleness bemerkt wird;
- `recall@k` der richtigen Quellkandidaten, Provenance-Fehler,
  Top-K-Reihenfolge und finale Antwort-/Routingqualität **getrennt**.

Als **exploratives Entscheidungssignal**, nicht universeller Benchmark:
Bei allen kritischen Fällen muss der Kandidat qualitäts- und
Gate-nichtunterlegen sein. Erst dann ist eine im Pilot reproduzierbare,
materielle Reduktion des gemessenen **gesamten Modell-Tokenverbrauchs**
interessant; mediane Delta-Prozente **und** Absolutwerte zeigen.
Eine abgeschnittene Graphantwort, die den Fehler bloß versteckt, zählt
als Fail. Bei zu geringer Stichprobe, fehlendem Verbrauchsledger oder
ungleichen Toolbedingungen lautet das Urteil `INCONCLUSIVE`.

## Optionaler Folgeversuch mit Output-Kompression

Der separate [TE-01-Pilot](../Token-Effizienz-Pilot/README.md) plant
Headroom/RTK als **anderen Eingriffspunkt**: Output-/Kontextfilter statt
Graph-basiertem Retrieval. **Nicht** in KG-01s ersten A/B/C-Vergleich
mischen. Nur bei getrennt erfolgreichen, vergleichbaren Ergebnissen
später eine kleine faktorielle Folgeprobe mit und ohne Graph und Filter
durchführen. Gemeinsamer Recall-/Gate-Quality-Floor, realer
Gesamt-Tokenverbrauch einschließlich zusätzlicher Retrieval-/Recall-
Calls und Compression-Overhead. Keine addierten Werbe-Ersparquoten.

## Ablauf und Stoppunkte

1. **Read-only Tool-/Security-Vorprüfung** nach
   [Graphify-Kandidatenkarte](../../../Dokumentation/Reviews/Graphify-Labs-graphify-2026-10-17.md).
   Paket-/Versionssnapshot und Lizenz prüfen. Keine
   Install-/Run-Freigabe allein durch diese Planung.
2. **A-Baseline messen**, einschließlich der echten Bootstrap-Reads.
   Ohne reproduzierbaren A-Lauf nur Konzept-/Indexvergleich, **kein
   Token-Lift-Claim**.
3. **Minimalen C-Prototyp** außerhalb des Repo-Arbeitsbaums entwerfen:
   kanonische YAML-/Markdown-Metadaten deterministisch parsen,
   gerichtete typisierte Kanten und relative Pfade mit Source-Lines
   speichern; `INFERRED` getrennt oder vorerst gar nicht erzeugen.
4. **Isolierten B-Versuch** erst nach expliziter Tool-/Bundle-Admission:
   Python-Version, Abhängigkeiten, global vs. projektlokal, Web-/Hooks-/
   MCP-/CLI-Schreibwirkungen prüfen. Nur read-only Offline-Corpus.
5. **Index-Evidence**: Linkauflösung, Redirect-/Stalenessprobe,
   Negativkontrollen, korrekte Kantenrichtung und Graphgröße. Für
   kritische Guards absichtlich kaputte Fixtures benutzen, nicht das Repo.
6. **Vergleichsläufe** mit möglichst verblindetem Judge, getrenntem
   Verbrauchsledger und Failure-Klassifikation. Keine ungefragte
   zweite Iteration; bei Scheitern Ursachen dokumentieren.
7. **Human Gate**: entweder A behalten, Graphify als externes
   **optionales Tool** zulassen, C als internes Tool entwickeln,
   beide ergänzend führen oder beides verwerfen.
   **Erst danach** über einen eigenen `graph-retrieval`-Skill,
   bestehenden `knowledge-query`-Adapter oder einen neuen
   mehrphasigen Workflow entscheiden.

## Artefakte eines späteren Testlaufs

`PLAN.md` (gefrorene Variablen), `RUN-REPORT.md`,
Indexmanifest + gehashte Sources, A/B/C-Querytrace,
Token-/Zeit-/Update-Ledger, anonyme Judge-Ergebnisse,
Staleness-/Prompt-Injection-Negativtests und Entscheidung `KEEP /
ADOPT-OPTIONAL / ITERATE / REJECT / INCONCLUSIVE`.
**Jetzt sind diese Dateien nicht vorhanden; es gibt keine Modellruns,
keinen echten Graphbau und keine Tokenmessung.**

## Quellen und Status

- [Graphify](https://github.com/Graphify-Labs/graphify), beobachteter
  Branch `v8`, Commit
  `86c57be8204673c2a1b9849a3292a7dd3ab373d8`;
  [Architektur](https://github.com/Graphify-Labs/graphify/blob/v8/ARCHITECTURE.md),
  [Benchmarks](https://github.com/Graphify-Labs/graphify/blob/v8/BENCHMARKS.md).
- Die Graphify-Projektangabe „80 %“ ist für KI-Regeln **nicht belegt**.
  Der interne Tokenbenchmark stellt vollständigen Corpus einer
  budgetierten Query gegenüber; das ist nicht äquivalent zu
  Gesamtkosten eines Agentenlaufs.
- KI-Regeln: `AGENTS.md`, `Dokumentation/Skill-Handbuch.md`,
  `skill-catalog.yml`, `routing-overlays.yml`,
  `Wissensmanagement/Skills/knowledge-query/SKILL.md`,
  `Agentenarbeit/Skills/context-engineering/SKILL.md`,
  `Agentenarbeit/Skills/context-audit/SKILL.md`,
  `Agentenarbeit/Skills/agent-eval/SKILL.md`.

**Keine neuen Skills, keine Registrierungen, keine Code-/Runtimeänderungen
und keine Freigabe für Graphify durch dieses Dokument.**
