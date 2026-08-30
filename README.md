# KI-Regeln

Dieses Repository sammelt allgemeine, wiederverwendbare Regeln, Arbeitsweisen, Skills, Evals und Workflows für die Zusammenarbeit mit generativer KI.

Ziel ist keine persönliche KI-Konfiguration und keine projektspezifische Wissenssammlung. Enthalten werden nur Regeln, die sich sinnvoll auf andere Nutzer, Projekte oder Aufgaben übertragen lassen.

## KI-Regeln in 60 Sekunden

KI-Regeln ist ein Werkzeugkasten für kontrollierte KI-Arbeit. Nicht das ganze Repository wird in jeden Prompt geladen. Stattdessen beginnt die Arbeit mit einem konkreten Auftrag und der lokalen Projektwahrheit; danach werden nur die passenden Regeln, Skills oder Workflows herangezogen.

```text
konkreter Auftrag
→ lokale Projektwahrheit / Sources of Truth
→ passenden Workflow oder Skill wählen
→ KI arbeitet innerhalb dieser Grenzen
→ Evidence / Review / Verification
→ Human Gate, wenn eine Entscheidung oder Außenwirkung es erfordert
```

Die allgemeinen Regeln helfen beim **Wie**. Das konkrete Projekt bestimmt weiterhin das **Was**.

- Praktischer Einstieg: [`PRAXISBEISPIELE.md`](PRAXISBEISPIELE.md)
- Nutzung in eigenen Projekten: [`Dokumentation/Nutzung-des-Repositories.md`](Dokumentation/Nutzung-des-Repositories.md)
- Einstieg für KI-Agenten: [`AGENTS.md`](AGENTS.md)

## Reife und Anspruch

KI-Regeln ist ein experimenteller, systematisch gepflegter Werkzeugkasten für kontrollierte KI-Arbeit. Der Umfang des Katalogs beschreibt das vorhandene Inventar, nicht die Qualität oder Produktionsreife jedes einzelnen Skills.

Reife und Prüfstand werden deshalb getrennt sichtbar gemacht: Skills besitzen explizite Maturity-Level wie `experimental` oder `candidate`, daneben wird die Eval Coverage mit Stufen wie `none` oder `partial` dokumentiert. Ein definierter Evalfall ist noch kein ausgeführter Test, ein ausgeführter Test ist nicht automatisch bestanden, und Same-Model-Smoke-Läufe ersetzen keinen unabhängigen Benchmark.

Zum System gehören außerdem Provenance, Routing, Gates und Evidence. Sie sind keine Begleitdokumentation zu Prompt-Dateien, sondern Teil der Regeln dafür, wann ein Skill eingesetzt werden soll, worauf Aussagen gestützt sind und welche Grenzen oder Freigaben gelten.

## Grundprinzip

> Allgemeine Arbeitsweise zentral, konkrete Wahrheit lokal.

Das bedeutet:

- allgemeine Kommunikations-, Reflexions-, Recherche-, Wissensmanagement-, Schnittstellen-/Contract-, Infrastruktur-/DevOps-, Reliability-/System-Observability-, Data-Engineering-, Software-Architecture-/System-Design-, Requirements-/Specification-Engineering-, Social-Media-/Content-Präsenz-, Dokumentations-, Schreib-, Story-/Fiktions-, Finanz-, Bild-, Web-, Datenbank-, Testing-, Agenten-, Sicherheits- und Entwicklungsregeln liegen hier;
- projektspezifische Anforderungen, Stakeholderentscheidungen, Zielwerte, Architecture Drivers und Constraints, Systemgrenzen, Ownership, konkrete Architekturentscheidungen, Research-Fragen, interne Quellen, Wissensbestände, Fachmodelle, reale Schnittstellen/Consumer, Data-Engineering-Sources-of-Truth und Grains, Infrastrukturtools/Provider/Accounts/Cluster, reales Datenbankschema, konkrete Testumgebung, SLO-Werte, Alert-Schwellen, Severity-/On-Call-Modelle, RTO/RPO, Capacity Limits, Recovery-/Failover-Regeln, Markenregeln, Zielgruppen, Content-Ziele, Plattformaccounts/-rollen, reale Analyticsdefinitionen, Publishing-/Approval-Regeln, visuelle Bibeln und Sonderregeln bleiben im jeweiligen Projekt;
- persönliche Profile oder unnötige personenbezogene Details gehören nicht in dieses Repository;
- ein Skill ersetzt niemals die tatsächliche Spezifikation oder Dokumentation eines Projekts.

## Neu hier?

Empfohlener Einstieg:

1. diese README für das Gesamtmodell;
2. `PRAXISBEISPIELE.md` für einen konkreten realen Arbeitsablauf;
3. `Dokumentation/Nutzung-des-Repositories.md` für den praktischen Einsatz;
4. `Dokumentation/Skill-Handbuch.md` zur Auswahl geeigneter Skills;
5. `Dokumentation/Skill-Katalog.md` für Reifegrad und Evalabdeckung;
6. danach nur die für das eigene Vorhaben relevanten Regeln, Skills und Workflows.

Nicht das komplette Repository muss für jede Aufgabe geladen werden.

## Public Entry Path

Für eine spätere öffentliche Nutzung sind zusätzlich diese Einstiege maßgeblich:

- `LICENSE` – MIT-Lizenz für das projekt-eigene KI-Regeln-Material;
- `CONTRIBUTING.md` – Beitrags- und Reviewprozess;
- `SECURITY.md` – Security-Policy und Public-Release-Voraussetzungen;
- `ACKNOWLEDGEMENTS.md` – methodische Referenzräume ohne künstliche Lizenzübertragung;
- `THIRD-PARTY-NOTICES.md` – tatsächlich redistribution-relevante Drittmaterial-Notices;
- `Dokumentation/open-source-readiness.yml` – maschinenlesbarer Readiness- und Release-Gate-Status;
- `Dokumentation/Open-Source-Readiness-2026-08-25.md` – menschenlesbarer Phase-3-Auditbericht.

Die Root-Projektlizenz ist MIT und gilt für das projekt-eigene KI-Regeln-Material. Drittmaterial wird dadurch nicht automatisch unter MIT gestellt; für redistribution-relevante Drittmaterialien bleiben `THIRD-PARTY-NOTICES.md` und die dokumentierte Provenance maßgeblich.

Der Public-Release-Status wird weiterhin ausschließlich über `Dokumentation/open-source-readiness.yml` bestimmt. Aus einer vorhandenen Root-`LICENSE` darf daher keine Veröffentlichungsfreigabe abgeleitet werden: Solange `release_gate.status` nicht `ready` ist, ist der Public Release Gate nicht freigegeben.

## Struktur

```text
KI-Regeln/
├── Grundlagen/
├── Arbeitsweisen/
├── Agentenarbeit/
├── Recherche/
├── Wissensmanagement/
├── Schnittstellen-und-Vertraege/
├── Infrastruktur-und-DevOps/
├── Reliability-und-System-Observability/
├── Data-Engineering/
├── Software-Architecture-und-System-Design/
├── Requirements-und-Spezifikations-Engineering/
├── Social-Media-und-Content-Praesenz/
├── Dokumentationserstellung/
├── Schreiben/
├── Storyentwicklung-und-Fiktion/
├── Finanzen/
├── Bildarbeit/
├── Webentwicklung/
├── Programmieren/
├── Datenbanken/
├── Testing-und-QA/
├── Skill-Engineering/
├── Sicherheit/
├── Evals/
├── Workflows/
├── Dokumentation/
├── Vorlagen/
├── skill-catalog.yml
├── LICENSE
├── CHANGELOG.md
└── THIRD-PARTY-NOTICES.md
```

Die Detailstruktur der Fachbereiche steht in deren jeweiligen README- und Regeldateien.

## Vorrangregeln

Bei der Anwendung gilt grundsätzlich:

```text
konkreter Nutzerauftrag
→ verbindliche Projektanforderung / Spezifikation / Kanon
→ gültige Projektentscheidungen und Projektdokumentation
→ freigegebener Plan, Research-Plan oder Produktionsbrief
→ lokale Repository-Regeln und freigegebene Referenzen / Quellenräume
→ allgemeine Agenten-, Fach- und Arbeitsregeln aus diesem Repository
```

Allgemeine Regeln dürfen keine lokale fachliche, visuelle, markenbezogene oder persönliche Wahrheit überschreiben.

# Fach- und Methodenbereiche

## Grundlagen

Regeln für verlässliche Zusammenarbeit mit KI unabhängig vom Fachgebiet: Kommunikation, Datenschutz, Kontext, Unsicherheit, kalibriertes Vertrauen und Denkautonomie.

> KI soll Denken unterstützen, nicht unbemerkt an dessen Stelle treten.

## Arbeitsweisen

Wiederverwendbare Denk-, Problemlösungs- und Lernmuster wie Hypothesenbildung, Reflexion, Entscheidungsunterstützung und Zielarbeit.

> Verstehen → ausprobieren → Erfahrung sammeln → reflektieren → anpassen.

## Agentenarbeit

Kontrollierte Agentenautonomie mit Context Engineering, Harness Engineering, Task Graphs, Verification Loops, Delegation, Evidence, Evals, Observability, Human Gates und Entropiemanagement.

Context Engineering wurde um die technische Long-Horizon-Schicht erweitert:

- Context Budget und Token-Effizienz statt bloßer Token-Minimierung;
- Context Rot, Duplikate, Altstände und Signalqualität;
- Context Compaction mit Fortsetzungsfähigkeit als Qualitätskriterium;
- Long-Horizon-Handoffs zwischen Sessions oder Agenten;
- Tool-Output-Offloading statt unnötiger Rohdaten im Modellkontext;
- providerneutrale Regeln für Prompt Caching und stabile Kontextpräfixe;
- klare Grenze zwischen Active Context, taskbezogenem Working State und dauerhaftem Persistent Knowledge.

Operative Context-Skills:

- `context-engineering`;
- `context-audit`;
- `context-compaction`;
- `session-handoff`.

Zusätzlich existieren ein konkretes Trace-Datenmodell und ein maschinenlesbares Trace-Event-Schema. Agenten-Observability bezeichnet hier die Nachvollziehbarkeit von Auftrag, Agentenlauf, Tools, Artefakten, Evidence und Gates. Die Runtime-Observability laufender Produktsysteme gehört zu `Reliability-und-System-Observability/`.

> Autonomie innerhalb klarer Grenzen.

> Kontext ist Arbeitsmaterial, kein Archivdump.

## Recherche

Websuche und Deep Research mit Fragezerlegung, claimbezogener Quellenqualität, Claim-Evidence-Verknüpfung, Triangulation, Coverage, Synthese und separatem Citation Audit.

> Suchergebnisse sind Leads, keine Evidenz.

> Coverage vor Source Count.

## Wissensmanagement

Toolneutrale Regeln für persistente Wissensbasen und Personal-/Organizational-Knowledge-Management: Wissensmodell, Ingest, Provenance, Granularität, Relationen, Synthesen, Konflikte, Staleness, Retrieval, Content Health und Datenschutz.

Operative Skills:

- `knowledge-base-design`;
- `knowledge-ingest`;
- `knowledge-distill`;
- `knowledge-synthesis`;
- `knowledge-maintenance`;
- `knowledge-query`;
- `knowledge-base-review`.

> Eine Wissensbasis soll nach einem Ingest nicht nur größer, sondern besser werden.

## Schnittstellen und Verträge

Technologieübergreifende Regeln für langlebige Zusagen zwischen Providern und Consumern: HTTP, GraphQL, RPC/IDL, Events, Webhooks, Schemas, Fehlersemantik, Idempotenz, Retry, Auth, Compatibility, Versionierung und Contract-First-Artefakte.

Scope-Grenze:

```text
Requirements und Specification Engineering
→ welche fachliche Capability und beobachtbaren Akzeptanzbedingungen benötigt werden

Software Architecture
→ warum und wo eine Systemgrenze existiert

Schnittstellen und Verträge
→ was über diese Grenze zugesichert wird
```

Operative Skills:

- `interface-design`;
- `http-api-design`;
- `event-contract-design`;
- `contract-change-review`;
- `interface-review`.

> Ein Contract ist eine beobachtbare Zusage – nicht bloß ein Schema.

## Infrastruktur und DevOps

Tool- und providerneutrale Regeln für Infrastructure as Code, Desired/Actual State, CI, Artifacts, Container Builds, Deployments, GitOps, Policy as Code, Secrets und Execution Boundaries.

Operative Skills:

- `infrastructure-as-code`;
- `infrastructure-change-review`;
- `ci-pipeline-design`;
- `container-build`;
- `deployment-strategy`;
- `gitops-design`;
- `infrastructure-review`.

Zentrale Zustandsregeln:

```text
Desired State ≠ Actual State
Preview ≠ Apply
Plan Review ≠ Apply Authorization
Build ≠ Deploy ≠ Release
Rollback ≠ Undo aller Nebenwirkungen
```

> Automatisierung reduziert manuelle Arbeit, vergrößert aber gleichzeitig die Reichweite einer Fehlentscheidung.

## Reliability und System-Observability

Tool- und providerneutrale Regeln für SLI/SLO, Observability, Alerting, Incident Response, Postmortems, Capacity, Recovery, Resilience, Toil und Operational Readiness.

Operative Skills:

- `slo-design`;
- `system-observability-design`;
- `alert-design`;
- `incident-response`;
- `incident-postmortem`;
- `capacity-planning`;
- `resilience-experiment`;
- `reliability-review`.

Zentrale Trennungen:

```text
SLI-Spezifikation ≠ Messimplementierung
SLO ≠ SLA ≠ RTO/RPO
Telemetry ≠ Observability
Alert ≠ Incident
Mitigation Proposal ≠ Produktionsautorisierung
```

> Reliability ist die Verbindung aus relevanten Zielen, glaubwürdiger Runtime-Evidence, kontrollierter Reaktion und nachweisbarem Lernen.

## Data Engineering

Tool- und plattformneutrale Regeln für Source-to-Consumer-Datenflüsse, Ingestion/CDC, Transformation, analytische Datenmodelle, Data Quality, Data Contracts, Lineage, Orchestrierung, Batch/Streaming, Replay und Publish/Lifecycle.

Operative Skills:

- `data-pipeline-design`;
- `data-ingestion-design`;
- `data-transformation-design`;
- `analytical-data-modeling`;
- `data-quality-design`;
- `data-contract-design`;
- `data-lineage-analysis`;
- `data-orchestration-design`;
- `data-engineering-review`.

> Eine Pipeline ist nicht korrekt, weil sie lief, sondern wenn richtige Daten mit nachvollziehbarer Semantik und Evidence beim vorgesehenen Consumer ankommen.

## Software Architecture und System Design

Technologie- und providerneutrale Regeln für Architecture Drivers, System Context, Dekomposition, Runtime-Flows, Styles/Patterns, Quality-Szenarien, Trade-offs, Technologieauswahl, Evolution, Views/ADRs und Conformance.

Operative Skills:

- `architecture-baseline`;
- `system-design`;
- `architecture-decomposition`;
- `architecture-tradeoff-analysis`;
- `architecture-evolution`;
- `architecture-conformance-review`;
- `architecture-review`.

Zentrale Trennungen:

```text
Pattern ≠ Architekturentscheidung
Diagramm ≠ Architektur
Soll-Architektur ≠ Ist-Architektur
Bounded Context ≠ Microservice
Teamgröße ≠ Service-Split-Gate
Architecture Review ≠ Implementierungsfreigabe
Migrationsplan ≠ Cutover-Autorisierung
```

> Erst Driver und Invarianten, dann Struktur, dann Technologie.

## Requirements und Specification Engineering

Tool- und formatneutrale Regeln dafür, wie Bedürfnisse, Ziele und Constraints in nachvollziehbare, prüfbare Soll-Aussagen überführt und über ihren Lebenszyklus gepflegt werden.

Operative Skills:

- `requirements-baseline`;
- `requirements-elicitation`;
- `requirements-specification`;
- `acceptance-criteria-design`;
- `requirements-traceability`;
- `requirements-change-analysis`;
- `requirements-validation`;
- `requirements-review`.

Zentrale Trennungen:

```text
Stakeholderwunsch ≠ automatisch verbindliches Requirement
Ist-Verhalten ≠ automatisch gewünschtes Soll
Requirement ≠ Lösung
Acceptance Criterion ≠ Test Case
Traceability ≠ Korrektheit
Validation ≠ Approval
Requirements Readiness ≠ Implementierungsfreigabe
```

Für die acht Requirements-Skills sind 48 Startfälle definiert. Sie sind derzeit **definiert, aber noch nicht als Behavioral Evals ausgeführt oder bestanden**.

> Nicht mehr Text macht ein Requirement besser, sondern mehr gemeinsame, prüfbare Bedeutung.

## Social Media und Content-Präsenz

Plattform- und toolneutrale Regeln für eine glaubwürdige, konsistente und lernfähige öffentliche Content-Präsenz.

Der Bereich behandelt insbesondere:

- Presence Baseline aus Profilen, Content-Historie, Zielen und verfügbarer Analytics-Evidence;
- Ziel, Audience, Positionierung und glaubwürdige Themenräume;
- Content-Säulen und Formate ohne starre Quoten;
- Editorialplanung, Kadenz, Ressourcen und Content-Backlog;
- Social-Content-Design mit Aussage, Hook, Struktur und optionalem CTA;
- plattformnative Adaption mit aktuell geprüften Features/Limits statt Algorithmusfolklore;
- Repurposing mit Provenance, Originalität und Claim-Treue;
- Community-Dialog, Moderation und Eskalation;
- Performanceanalyse mit realen Metriken, definierten Fenstern und begrenzter Kausalität;
- Claims, Disclosure, Rechte, Privacy und externe Publishing-Gates;
- unabhängigen Content-/Presence-Review.

Scope-Grenze:

```text
Requirements / lokale Business- und Brand-Policy
→ Ziele, Audience, Marke, verbindliche Claims/Constraints und Erfolgskriterien

Recherche
→ externe Fakten, Trends und Quellen verifizieren

Social Media und Content-Präsenz
→ Presence-Strategie, Social-Formate, Plattformadaption, Editorialsystem, Community und Performance-Lernen

Schreiben
→ natürliche sprachliche Ausarbeitung

Bildarbeit
→ visuelle Assets und Bildreview

lokales Publishing-Gate
→ reale Posts, Replies, DMs, Deletes, Blocks oder andere Außenaktionen autorisieren
```

Operative Skills:

- `content-presence-baseline`;
- `social-content-strategy`;
- `editorial-planning`;
- `social-content-design`;
- `platform-content-adaptation`;
- `content-repurposing`;
- `community-engagement`;
- `content-performance-analysis`;
- `content-presence-review`.

Zentrale Trennungen:

```text
Reichweite ≠ Wirkung
Follower ≠ Community
Impressions ≠ Aufmerksamkeit
Engagement ≠ Geschäftserfolg
Korrelation ≠ Kausalität
Algorithmus-Tipp ≠ Plattformwahrheit
Cross-Posting ≠ Copy-Paste
Repurposing ≠ Low-Value-Reupload
Draft / Review ≠ Publishing-Freigabe
```

Postingfrequenzen, beste Uhrzeiten, Hashtagzahlen, Content-Pillar-Prozente, Rankinggewichte und Plattform-KPI-Zielwerte sind keine zentralen Defaults. Plattformmechaniken sind mutable Evidence und werden bei Materialität aktuell geprüft.

Für die neun Social-Media-/Content-Präsenz-Skills sind 54 Startfälle definiert; erwartete Verteilung 36× `pass`, 9× `partial` und 9× `blocked`. Sie sind derzeit **definiert, aber noch nicht als Behavioral Evals ausgeführt oder bestanden**.

> Ziel, Publikum und belegte Aussage vor Algorithmusfolklore.

## Dokumentationserstellung

Technische und projektbezogene Dokumentation mit Trennung von Leserzustand, Dokumentzweck, Source of Truth, Schreibqualität, Verifikation und Wartbarkeit.

> Eine gut geschriebene falsche Anleitung ist schlechter als eine knappe korrekte.

## Schreiben

Allgemeine Regeln für natürliche Texte, kreative Prosa und Stilreviews. KI-typische Muster werden als Warnsignale und nicht als mechanische Verbotsliste behandelt.

## Storyentwicklung und Fiktion

Toolneutrale Regeln für fiktionale Erzählprojekte über einzelne Szenen hinaus: narrativer Kanon, Figuren und Beziehungen, Weltregeln, Plot/Arcs, Setup/Payoff sowie Langzeitkontinuität und Story-State.

Operative Skills:

- `story-bible`;
- `figurenentwicklung`;
- `plot-und-storystruktur`;
- `worldbuilding`;
- `story-kontinuitaet`.

Zentrale Trennungen:

```text
Kanon ≠ Planung
Planung ≠ bereits erzählte Tatsache
Storystruktur ≠ Pflicht-Framework
Worldbuilding ≠ Lore-Menge
Kontinuitätscheck ≠ Stilreview
Review ≠ Änderungsfreigabe
```

Die fünf Story-Skills starten `experimental` mit `partial` Evalabdeckung. Für sie sind 25 Startfälle definiert; diese Fälle sind **definiert, aber noch nicht als Behavioral Evals ausgeführt oder bestanden**.

> Eine Geschichte ist mehr als gute Prosa. Narrative Wahrheit muss über Zeit, Figuren, Wissen und Konsequenzen nachvollziehbar bleiben.

## Finanzen

Tool- und jurisdiktionsneutrale Regeln für persönliche Finanzplanung, Vermögensentwicklung und sachliche Investmentanalyse mit expliziten Annahmen, aktuellem Datenstand und getrennten Human Gates für reale Finanzaktionen.

Operative Skills:

- `finanzstatus-und-cashflow`;
- `ruecklagenplanung`;
- `schuldenstrategie`;
- `vermoegensprojektion`;
- `portfolioanalyse`;
- `anlagevergleich`.

Zentrale Trennungen:

```text
Projektion ≠ Prognose ≠ Garantie
historische Rendite ≠ zukünftige Rendite
Modellannahme ≠ Fakt
Diversifikation ≠ Verlustschutz
Analyse / Review ≠ Finanzaktions-Autorisierung
aktuelle Steuer-/Produktregel ≠ zeitlose zentrale Wahrheit
```

Konkrete Markt-, Produkt-, Steuer- und Regulierungsdaten werden bei Materialität aktuell und jurisdiktionsbezogen geprüft. Die sechs Finanz-Skills starten `experimental` mit `partial` Evalabdeckung. Für sie sind 30 Startfälle definiert; diese Fälle sind **definiert, aber noch nicht als Behavioral Evals ausgeführt oder bestanden**.

> Ein guter Finanzplan macht Entscheidungen belastbarer. Er macht die Zukunft nicht sicher.

## Bildarbeit

Regeln für konsistente Einzelbilder und Bildserien mit getrennten Achsen für Identität, Stil, Struktur und Kontinuität.

> Konsistenz vor Zufall. Aussage vor Effekt. Referenz vor Neuerfindung.

## Webentwicklung

Webdesign und Frontend-Engineering mit Art Direction, Informationsarchitektur, Designsystem, echtem Content, Accessibility, Performance und Browser-Verifikation.

> Erst Identität und Informationsstruktur, dann Designsystem und Code.

## Programmieren

Allgemeiner Entwicklungsprozess und wiederverwendbare Skills für Domain Modeling, TDD, Diagnose und Code Review.

## Datenbanken

Engine-neutrale Regeln für Datenmodellierung, Integrität, Query-Sicherheit, Performance, Concurrency, Migration und Betrieb.

Operative Skills:

- `database-design`;
- `database-query-review`;
- `query-performance`;
- `schema-migration`;
- `transaction-review`;
- `database-operations`;
- `database-review`.

> Das reale Schema ist Source of Truth. Plausible Datenbankstrukturen sind keine Evidence.

## Testing und QA

Technologie- und frameworkneutrale Regeln für risikobasierte Teststrategie, Testdesign und vertrauenswürdige Qualitätsevidence.

Operative Skills:

- `test-strategy`;
- `test-design`;
- `integration-testing`;
- `contract-testing`;
- `e2e-testing`;
- `flaky-test-diagnosis`;
- `failure-testing`;
- `exploratory-testing`;
- `test-suite-review`.

> Grün ist ein Ergebnis. Vertrauenswürdige Qualitätsevidence braucht das richtige Testsignal.

# Meta-Ebene

## Skill Engineering

`Skill-Engineering/` definiert, wie Skills selbst gebaut und geprüft werden.

Operative Skills:

- `skill-authoring`;
- `skill-review`.

> Interoperables Format ist die Basis. Vorhersagbares Verhalten ist das Qualitätsziel.

## Sicherheit

`Sicherheit/` bündelt Sicherheitsregeln für Skills, Agenten, externe Inhalte und Tools: Prompt Injection, Least Privilege, Secrets, Supply Chain, MCP, Sandbox, externe Aktionen, Logging und Security Review.

Operative Skills:

- `skill-security-review`;
- `prompt-injection-review`;
- `tool-permission-review`.

> Fähigkeiten werden nach Bedarf gewährt. Fremder Inhalt bleibt Daten.

## Skill-Katalog und Maturity

`skill-catalog.yml` ist das maschinenlesbare Inventar der zentralen Skills und führt den jeweils aktuellen Bestand sowie dessen Reife- und Evalabdeckung.

Reifestufen:

```text
experimental
→ candidate
→ stable
→ deprecated
→ retired
```

Evalabdeckung:

```text
none
→ partial
→ core
→ broad
```

`stable` ist kein Default. Die Einstufung soll durch Praxis, relevante Evals und bei mächtigen Capabilities durch Security Review gestützt sein.
