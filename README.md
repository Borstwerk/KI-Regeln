# KI-Regeln

Dieses Repository sammelt allgemeine, wiederverwendbare Regeln, Arbeitsweisen, Skills, Evals und Workflows für die Zusammenarbeit mit generativer KI.

Ziel ist keine persönliche KI-Konfiguration und keine projektspezifische Wissenssammlung. Enthalten werden nur Regeln, die sich sinnvoll auf andere Nutzer, Projekte oder Aufgaben übertragen lassen.

## Grundprinzip

> Allgemeine Arbeitsweise zentral, konkrete Wahrheit lokal.

Das bedeutet:

- allgemeine Kommunikations-, Reflexions-, Recherche-, Wissensmanagement-, Schnittstellen-/Contract-, Infrastruktur-/DevOps-, Reliability-/System-Observability-, Data-Engineering-, Software-Architecture-/System-Design-, Dokumentations-, Schreib-, Bild-, Web-, Datenbank-, Testing-, Agenten-, Sicherheits- und Entwicklungsregeln liegen hier;
- projektspezifische Anforderungen, Architecture Drivers und Constraints, Systemgrenzen, Ownership, konkrete Architekturentscheidungen, Research-Fragen, interne Quellen, Wissensbestände, Fachmodelle, reale Schnittstellen/Consumer, Data-Engineering-Sources-of-Truth und Grains, Infrastrukturtools/Provider/Accounts/Cluster, reales Datenbankschema, konkrete Testumgebung, SLO-Werte, Alert-Schwellen, Severity-/On-Call-Modelle, RTO/RPO, Capacity Limits, Recovery-/Failover-Regeln, Markenregeln, visuelle Bibeln und Sonderregeln bleiben im jeweiligen Projekt;
- persönliche Profile oder unnötige personenbezogene Details gehören nicht in dieses Repository;
- ein Skill ersetzt niemals die tatsächliche Spezifikation oder Dokumentation eines Projekts.

## Neu hier?

Empfohlener Einstieg:

1. diese README für das Gesamtmodell;
2. `Dokumentation/Nutzung-des-Repositories.md` für den praktischen Einsatz;
3. `Dokumentation/Skill-Handbuch.md` zur Auswahl geeigneter Skills;
4. `Dokumentation/Skill-Katalog.md` für Reifegrad und Evalabdeckung;
5. danach nur die für das eigene Vorhaben relevanten Regeln, Skills und Workflows.

Nicht das komplette Repository muss für jede Aufgabe geladen werden.

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
├── Dokumentationserstellung/
├── Schreiben/
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

Allgemeine Regeln dürfen keine lokale fachliche, visuelle oder persönliche Wahrheit überschreiben.

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

Zusätzlich existieren ein konkretes Trace-Datenmodell und ein maschinenlesbares Trace-Event-Schema. Diese können optional auch Context-/Usage-Metadaten wie Input-/Output-Tokens, Cache-Signale, Context-Größe, Compaction oder Handoff-Ereignisse erfassen, ohne Promptinhalte standardmäßig zu speichern.

Agenten-Observability bezeichnet hier die Nachvollziehbarkeit von Auftrag, Agentenlauf, Tools, Artefakten, Evidence und Gates. Die Runtime-Observability laufender Produktsysteme gehört zu `Reliability-und-System-Observability/`.

> Autonomie innerhalb klarer Grenzen.

> Kontext ist Arbeitsmaterial, kein Archivdump.

## Recherche

Websuche und Deep Research mit:

- Fragezerlegung und Perspektiven;
- claimbezogener Quellenqualität;
- Claim-Evidence-Verknüpfung;
- Triangulation und Widerspruchsanalyse;
- Coverage statt bloßer Quellenanzahl;
- Synthese nach Erkenntnis;
- separatem Citation Audit;
- Web-Sicherheit und Prompt-Injection-Abgrenzung.

> Suchergebnisse sind Leads, keine Evidenz.

> Coverage vor Source Count.

## Wissensmanagement

Toolneutrale Regeln für persistente Wissensbasen und Personal-/Organizational-Knowledge-Management.

Der Bereich behandelt insbesondere:

- Wissensmodell, Scope und stabile Identität von Wissenseinheiten;
- Capture, Ingest und Triage mit `search before create`;
- Raw Sources, Provenance, Evidence und Source-of-Truth-Bezug;
- Granularität ohne Monolithen oder Notiz-Konfetti;
- Links, Relationen, Taxonomien und Navigation;
- Synthesen und Maps of Content mit nachvollziehbaren Eingaben;
- Widersprüche, Unsicherheit und Confidence;
- Aktualität, Staleness, Review und Lifecycle;
- Retrieval und Findability ohne Retrievalscore mit Wahrheit gleichzusetzen;
- Content Health mit Dubletten, Orphans, kaputten Links und Drift;
- Datenschutz, Sichtbarkeit und kontrolliertes Vergessen.

Scope-Grenze:

```text
Recherche
→ neues Wissen finden und verifizieren

Wissensmanagement
→ Wissen dauerhaft strukturieren, verbinden und pflegen

Context Engineering
→ den richtigen Ausschnitt für die aktuelle Aufgabe laden

Dokumentation
→ Wissen zielgruppengerecht vermitteln

RAG / Vector Search
→ mögliche technische Retrieval-Implementierung
```

Operative Skills:

- `knowledge-base-design`;
- `knowledge-ingest`;
- `knowledge-distill`;
- `knowledge-synthesis`;
- `knowledge-maintenance`;
- `knowledge-query`;
- `knowledge-base-review`.

Obsidian, Notion, Vektorstores oder Knowledge Graphs sind mögliche Adapter. Ihre konkreten Mechanismen werden nicht zur universellen Wissensmanagementregel erklärt.

> Eine Wissensbasis soll nach einem Ingest nicht nur größer, sondern besser werden.

## Schnittstellen und Verträge

Technologieübergreifende Regeln für langlebige Zusagen zwischen Providern und Consumern.

Der Bereich behandelt insbesondere:

- Consumer-/Provider- und Ownership-Modell;
- Wahl zwischen HTTP, GraphQL, RPC/IDL, Events und Webhooks nach realem Kommunikationsproblem;
- Contract-Schemas, Defaults, Nullability, Enums und Fehlersemantik;
- HTTP API Design ohne REST- oder Versionierungsdogma;
- GraphQL-Schemaevolution;
- RPC-/Protobuf-Verträge mit Source-/Wire-Aspekten;
- Event-/Async-Contracts mit Delivery, Ordering, Replay und Dead Letter;
- Webhooks und Callbacks;
- Idempotenz, Retry und Concurrency;
- Auth-, Scope- und Tenant-Grenzen im beobachtbaren Vertrag;
- Source-, Wire- und semantische Compatibility;
- Versionierung, Deprecation, Sunset und Removal-Gates;
- Contract-First und maschinenlesbare Artefakte.

Scope-Grenze:

```text
Software Architecture
→ warum und wo eine Systemgrenze existiert

Schnittstellen und Verträge
→ was über diese Grenze zugesichert wird

Data Engineering
→ welche veröffentlichten Datasets und Datenprodukte Consumer mit Grain, Quality und Lifecycle erwarten dürfen

Contract Testing
→ ob Consumer und Provider den Vertrag tatsächlich einhalten

Reliability und System-Observability
→ ob das resultierende Gesamtsystemverhalten unter Störung tragfähig bleibt
```

Operative Skills:

- `interface-design`;
- `http-api-design`;
- `event-contract-design`;
- `contract-change-review`;
- `interface-review`.

GraphQL, RPC/IDL/Protobuf und Webhooks besitzen eigene Fachregeln, aber zunächst keine eigenen Skills. Ein anderes Vertragsformat allein ist noch keine neue Arbeitsdisziplin.

> Ein Contract ist eine beobachtbare Zusage – nicht bloß ein Schema.

## Infrastruktur und DevOps

Tool- und providerneutrale Regeln für Infrastructure as Code, Automationspipelines, Build-Artefakte, Deployments und Continuous Reconciliation.

Der Bereich behandelt insbesondere:

- Desired State, Ownership und IaC;
- State, Actual State, Drift und Reconciliation;
- Validate, Plan/Preview, Review, Gate und Apply als getrennte Schritte;
- Environment-Grenzen, Konfiguration und Artifact Promotion;
- CI-Pipelines, DAGs, Artifacts, Caches, Credentials und Gates;
- reproduzierbare Build-Artefakte und Provenance;
- Container Builds und Runtime-Verträge;
- Deploymentstrategien, Promotion, Pause, Abort und Rollback;
- GitOps und Continuous Reconciliation;
- Kubernetes als wichtige Referenzplattform ohne Kubernetes-Pflicht;
- Policy as Code und technische Guardrails;
- Secrets, Permissions und Execution Boundaries.

Scope-Grenze:

```text
Software Architecture
→ welche Plattformen und Systemtopologien existieren sollen

Infrastruktur und DevOps
→ wie gewünschte Umgebungen beschrieben, gebaut, geändert und ausgeliefert werden

Data Engineering
→ welche Datenflüsse, Data Intervals, Replay-/Publish-Semantik und datenfachliche Evidence auf dieser Runtime laufen

Testing und QA
→ welche Qualitätsrisiken wie geprüft werden

Reliability und System-Observability
→ was gesund, resilient und betrieblich akzeptabel bedeutet

Sicherheit
→ welche Rechte, Trust Boundaries und Security Policies gelten
```

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
Continuous Reconciliation ≠ einmalige Änderung
```

Terraform, OpenTofu, Pulumi, CloudFormation, Ansible, Kubernetes, Argo CD, Flux, Docker, GitHub Actions oder andere Tools bleiben konkrete Adapter.

> Automatisierung reduziert manuelle Arbeit, vergrößert aber gleichzeitig die Reichweite einer Fehlentscheidung.

## Reliability und System-Observability

Tool- und providerneutrale Regeln dafür, was bei laufenden Systemen gesund, zuverlässig, beobachtbar, recoverable und unter Störung akzeptabel bedeutet.

Der Bereich behandelt insbesondere:

- kritische Nutzer-/Consumerflows als Ausgangspunkt für Reliability;
- SLI-Spezifikation, Messimplementierung, SLOs und Error Budgets;
- System-Observability als Fähigkeit, relevante Betriebsfragen mit Runtime-Evidence zu beantworten;
- Health-Modelle, Telemetrie, Korrelation, Coverage und Blind Spots;
- actionable Alerting, Signalbasis, Threshold-Begründung, Fenster und Alert Noise;
- Incident Response mit Impact, Rollen, Incident State, Mitigation, Kommunikation und Fresh Recovery Evidence;
- Postmortems mit beitragenden Faktoren statt erzwungener Einzelursache;
- Capacity, Saturation, Headroom, Dependencies, Quotas und Failure Domains;
- Recovery-Ziele wie RTO/RPO und Disaster-Recovery-Readiness;
- Graceful Degradation, Failure Isolation und Cascading-Failure-Risiken;
- kontrollierte Resilience-Experimente, Chaos Engineering und Game Days;
- Toil und nachhaltiger Betrieb;
- Operational Readiness als zusammengesetzte Evidence statt Mega-Skill.

Scope-Grenze:

```text
Requirements / lokale Business-Policy
→ wie zuverlässig ein Flow sein muss und welche RTO/RPO gelten

Reliability und System-Observability
→ wie Ziele operationalisiert, beobachtet und unter Betrieb/Störung geprüft werden

Data Engineering
→ definiert Datenbedeutung sowie pipeline-spezifische Freshness-, Completeness-, Lag-, Backlog- und Reconciliation-Evidence

Software Architecture
→ welche Struktur und Patterns das gewünschte Failure-Verhalten ermöglichen

Infrastruktur und DevOps
→ wie Capacity, Deployment, Rollback, Failover und technische Zielzustände umgesetzt werden

Testing und QA
→ reproduzierbare Tests und Failure Cases im Testscope

Agentenarbeit / Observability
→ Nachvollziehbarkeit von Agentenläufen und Arbeitsprozessen
```

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
Load Testing ≠ Capacity Planning
Failure Testing ≠ Resilience Experiment
Reliability Requirement ≠ Architecture Pattern
Backup ≠ bewiesene Recovery
```

OpenTelemetry, Prometheus, Grafana, Datadog, PagerDuty, Elastic, Splunk, New Relic, CloudWatch, Azure Monitor, Google Cloud Operations, Kubernetes und andere Produkte bleiben konkrete Adapter.

SLO-Werte, Alert-Schwellen, Severity-/On-Call-Modelle, RTO/RPO, Capacity Limits, Recovery-/Failover-Regeln und Produktionsgates bleiben projektspezifisch.

> Reliability ist die Verbindung aus relevanten Zielen, glaubwürdiger Runtime-Evidence, kontrollierter Reaktion und nachweisbarem Lernen.

## Data Engineering

Tool- und plattformneutrale Regeln für systemübergreifende Datenflüsse und analytische Datenprodukte von der autoritativen Quelle bis zum Consumer.

Der Bereich behandelt insbesondere:

- Source of Truth und Ownership;
- Batch-, Micro-Batch- und Streaming-Verarbeitung;
- Ingestion, Snapshots, CDC, Cursor, Offsets und Replay;
- Transformationen, Incrementalität und Backfills;
- analytische Datenmodellierung mit Grain, Measures, Dimensionen und Historisierung;
- Data Quality, Freshness, Completeness und Reconciliation;
- Data Contracts für veröffentlichte Datasets;
- Schema- und Semantikevolution;
- Lineage, Provenance und Change Impact;
- Orchestrierung, Data Intervals, Retries, Catchup und Reprocessing;
- Event Time, Processing Time, Watermarks und Late Data;
- Publish, Retention und Lifecycle;
- pipeline-spezifische Runtime-/Freshness-/Lag-/Backlog-Evidence.

Scope-Grenze:

```text
Datenbanken
→ Zustand und Verhalten innerhalb eines operativen Datenspeichers

Schnittstellen und Verträge
→ operative APIs, Messages und Event-Contracts

Data Engineering
→ Source-to-Consumer-Datenflüsse und veröffentlichte Datasets mit Grain, Quality, Lineage, Replay und Lifecycle

Testing und QA
→ allgemeine Testmethodik und Teststrategie

Reliability und System-Observability
→ systemweite SLOs, Alerts, Incidents, Capacity und Resilience

Infrastruktur und DevOps
→ Scheduler-, Compute-, Storage- und Deployment-Runtime

Software Architecture
→ Systemgrenzen, Ownership und strukturelle Plattform-/Deployable-Entscheidungen
```

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

Zentrale Trennungen:

```text
Job grün ≠ Daten korrekt
Schema kompatibel ≠ Semantik kompatibel
Streaming ≠ exactly-once
Watermark ≠ garantierte Vollständigkeit
Retry ≠ Replay/Backfill
DB-Migrations-Backfill ≠ systemübergreifendes Pipeline-Reprocessing
Design Lineage ≠ Runtime Lineage
Backfill-Plan ≠ Backfill-Autorisierung
```

Airflow, Dagster, dbt, Kafka, Flink, Spark, Beam, Snowflake, BigQuery, Databricks, Iceberg, Delta Lake, OpenLineage und andere Produkte bleiben konkrete Adapter.

Sources of Truth, Grain, Qualitäts-/Freshness-Regeln, Retention, reale Consumer, Data-Contract-Zusagen, Backfill-/Replay-Scope und Publish-/Execution-Gates bleiben projektspezifisch.

> Eine Pipeline ist nicht korrekt, weil sie lief, sondern wenn richtige Daten mit nachvollziehbarer Semantik und Evidence beim vorgesehenen Consumer ankommen.

## Software Architecture und System Design

Technologie- und providerneutrale Regeln für Systemstruktur, Verantwortungsgrenzen, Runtime-Flows, Trade-offs und evolutionäre Architekturänderungen.

Der Bereich behandelt insbesondere:

- Architecture Drivers, Constraints, Annahmen und Missing Evidence;
- System Context, Akteure, externe Systeme und Verantwortungsgrenzen;
- Module, Komponenten, Services, Ownership und Dependency Direction;
- kritische Runtime- und Failure-Flows sowie State-/Coordination-Fragen;
- Architecture Styles und Patterns als Optionen statt Reifeleiter;
- konkrete Quality-Szenarien, Sensitivity Points und Trade-offs;
- einfachstes tragfähiges Systemdesign vor unnötiger Verteilung;
- Technologieauswahl nach Drivers und Struktur;
- evolutionäre Migration, Compatibility und Zwischenzustände;
- C4-/Runtime-/Deployment-Views und ADR-Anbindung als Evidence;
- Architecture Conformance, Fitness Functions und Drift;
- unabhängige Architektur- und Readiness-Reviews.

Scope-Grenze:

```text
Requirements / lokale Stakeholderziele
→ was das System leisten und welche Qualitätsziele es erfüllen muss

Software Architecture und System Design
→ welche Struktur diese Drivers und Invarianten mit welchen Trade-offs erfüllt

Schnittstellen / Datenbanken / Data Engineering / Reliability / Infrastruktur
→ wie die jeweiligen Fachmechaniken konkret ausgestaltet und betrieben werden

Programmieren
→ konkrete Implementierung innerhalb der freigegebenen Struktur
```

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

Microservices, Modular Monolith, Layered, Hexagonal, DDD, CQRS, Event Sourcing, Saga, Strangler, Event-driven und andere Styles/Patterns bleiben Werkzeuge. Kein Pattern ist zentraler Pflichtdefault.

Architecture Drivers, Quality-Ziele, Systemgrenzen, Ownership, akzeptierte ADRs, Last-/Recoverygrenzen, Plattformconstraints sowie Migration-/Cutover-Gates bleiben projektspezifisch.

> Erst Driver und Invarianten, dann Struktur, dann Technologie.

## Dokumentationserstellung

Technische und projektbezogene Dokumentation mit Trennung von:

- Leserzustand und Dokumentzweck;
- Tutorial / How-to / Reference / Explanation;
- Artefakttyp wie README, ADR oder Runbook;
- Source of Truth;
- Schreibqualität;
- Verifikation;
- Wartbarkeit und Driftkontrolle.

> Eine gut geschriebene falsche Anleitung ist schlechter als eine knappe korrekte.

## Schreiben

Allgemeine Regeln für natürliche Texte, kreative Prosa und Stilreviews. KI-typische Muster werden als Warnsignale und nicht als mechanische Verbotsliste behandelt.

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

Der Bereich behandelt insbesondere:

- Domäne und reale Zugriffsmuster als Grundlage des Datenmodells;
- reales Schema sowie Engine-/Driver-/ORM-Version als Source of Truth;
- Constraints und Datenintegrität;
- Query-Korrektheit, Parametrisierung und Tenant-/Scope-Grenzen;
- Indizes und Execution Plans mit Vorher-/Nachher-Evidence;
- Transaktionen, Isolation, Locking und Retry;
- Migrationen, Backfills, Rollout und Recovery;
- Connections, Pooling und Ressourcen;
- Least Privilege für Datenzugriff;
- Backup, Restore, Monitoring und Diagnose.

Scope-Grenze:

```text
Datenbanken
→ Zustand und Verhalten innerhalb eines operativen Datenspeichers

Data Engineering
→ systematische Bewegung, Replikation, Transformation und Orchestrierung zwischen Systemen
```

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

Der Bereich behandelt insbesondere:

- Risiken und Failure Modes vor Testmenge;
- passende Testebenen statt starrer Unit-/Integration-/E2E-Quoten;
- Testdesign aus Anforderungen, Invarianten, Grenzwerten und Zuständen;
- Test-Seams, Doubles und reale Abhängigkeiten;
- Testdaten, Isolation und Hermetik;
- Integration und Contract Testing;
- ausgewählte kritische End-to-End-Flows;
- Flaky Tests als Defekt am Testsignal;
- kontrollierte Failure-/Recovery-Tests;
- Coverage und Mutation als unterschiedliche Wirksamkeitssignale;
- explorative Tests mit Charter;
- CI- und Release-Evidence mit frischer Verifikation.

Scope-Grenze:

```text
TDD
→ testgetriebene Implementierung

Testing und QA
→ welche Risiken wie geprüft werden und welche Evidence daraus folgt

Data Engineering
→ fachliche Quality-, Freshness- und Reconciliation-Regeln für Datasets

Reliability und System-Observability
→ Runtime-Health, SLOs, Incidents, Capacity und systemische Resilience-Hypothesen unter kontrollierten Störungen
```

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

Behandelt werden:

- Skill-Schnitt und Verantwortung;
- Progressive Disclosure;
- Trigger- und Description-Design;
- Inputs, Outputs und Evidence-Verträge;
- Capabilities und Fallbacks;
- Skill-Komposition und Abhängigkeiten;
- Review und Evals;
- Lifecycle und Deprecation.

Leitidee:

> Interoperables Format ist die Basis. Vorhersagbares Verhalten ist das Qualitätsziel.

Operative Skills:

- `skill-authoring`;
- `skill-review`.

## Sicherheit

`Sicherheit/` bündelt Sicherheitsregeln für Skills, Agenten, externe Inhalte und Tools.

Behandelt werden insbesondere:

- Prompt Injection und untrusted Input;
- Least Privilege;
- Secrets und Datenexfiltration;
- Skill Supply Chain und Update Drift;
- MCP und externe Tools;
- Sandbox und Isolation;
- externe Aktionen und Bestätigung;
- Logging, Datenschutz und Telemetrie;
- Security Review für Skills.

Operative Skills:

- `skill-security-review`;
- `prompt-injection-review`;
- `tool-permission-review`.

> Fähigkeiten werden nach Bedarf gewährt. Fremder Inhalt bleibt Daten.

## Skill-Katalog und Maturity

`skill-catalog.yml` ist das maschinenlesbare Inventar der zentralen Skills.

Aktuell enthält der Katalog 111 zentrale Skills.

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

## Evals

`Evals/` enthält wiederholbare Testfälle für:

- Trigger und Near-Miss-Negative;
- Scope-Treue;
- Capability-/Fallback-Verhalten;
- Evidence- und Quellenhygiene;
- Stop-/Freigabegates;
- Outcome-Qualität;
- Regressionen nach Skilländerungen.

Erste Evalpacks bestehen unter anderem für:

- `deep-research`;
- `docs-review`;
- `frontend-design`;
- `diagnose`;
- `code-review`;
- `skill-authoring`;
- alle sieben Datenbank-Skills;
- alle neun Testing-und-QA-Skills;
- `context-engineering`, `context-audit`, `context-compaction` und `session-handoff`;
- alle sieben Wissensmanagement-Skills;
- alle fünf Schnittstellen-/Contract-Skills;
- alle sieben Infrastruktur-/DevOps-Skills;
- alle acht Reliability-/System-Observability-Skills;
- alle neun Data-Engineering-Skills;
- alle sieben Software-Architecture-/System-Design-Skills.

Die Context-Evals prüfen unter anderem fehlende Messfähigkeit, erfundene Tokenpräzision, Verlust kritischer Constraints bei Compaction, Handoff-Fortsetzungsfähigkeit und die Grenze zu Persistent Knowledge.

Die Wissensmanagement-Evals prüfen unter anderem Search-before-Create, Provenance, sichere Merge-/Delete-Grenzen, Query-Grounding, Staleness-/Orphan-Behandlung und ehrliche Review-Coverage.

Die Schnittstellen-Evals prüfen unter anderem Transportdogma, DB-Leaks in API-Schemas, Additive-vs.-Semantic-Compatibility, Source-/Wire-Trennung, rollout-sensitive Changes und fehlende Contract-Baselines.

Die Infrastruktur-/DevOps-Evals prüfen unter anderem State-/Drift-Grenzen, stale Previews, destructive Changes, Pipeline-Secret-Grenzen, Container Runtime Contracts, Deployment-/Rollback-Annahmen und GitOps-Reconciliation-Gates.

Die Reliability-/System-Observability-Evals prüfen unter anderem SLO-vs.-RTO/RPO-Grenzen, Observability ohne Tooldogma, Alert-Actionability, Incident-Gates, Postmortem-Evidence, Capacity-vs.-Load-Testing und sichere Resilience-Experimente.

Für die acht Reliability-Skills sind 48 Startfälle definiert; der erste Same-Model-Smoke-Lauf wurde am 2026-08-24 ausgeführt und ersetzt keinen unabhängigen verblindeten Benchmark.

Die Data-Engineering-Evals prüfen unter anderem Source-of-Truth-/Grain-Lücken, DB-/Event-/Testing-Near-Misses, CDC/Replay, `updated_at`-/exactly-once-Dogmen, historische Backfill-Semantik, Star-Schema-Dogma, Freshness-/Quality-Evidence, Data-Contract-Compatibility, Design-vs.-Runtime-Lineage, Retry/Catchup und produktive Datenänderungs-Gates.

Für die neun Data-Engineering-Skills sind 54 Startfälle definiert. Diese 54 Fälle sind **noch nicht ausgeführt oder bestanden**.

Die Software-Architecture-/System-Design-Evals prüfen unter anderem alte Diagramme als unzureichende Ist-Evidence, ADR-/Code-Konflikte, Microservice-/Teamgrößen-/Shared-DB-Dogmen, erfundene Qualitätsziele, künstliche Kandidaten, opaque Architecture Scores, Big-Bang-Migrationen, Conformance ohne lokales Referenzmodell und implizite Implementierungs-/Deploymentfreigaben.

Für die sieben Architecture-Skills sind 42 Startfälle definiert. Der erste Same-Model-Smoke-Lauf wurde am 2026-08-25 gegen den gepinnten Stand `78abce4ade2e1d92dfc47f6169dcd2551d8d0f09` ausgeführt. Alle 42 Fälle entsprachen dem erwarteten Verhalten und Status: 30× `pass`, 6× `partial`, 6× `blocked`. Das ersetzt keinen unabhängigen verblindeten Benchmark und rechtfertigt keine automatische Hochstufung.

## Workflows / Recipes

`Workflows/` verbindet kleine Skills zu größeren, nachvollziehbaren Produktionsabläufen.

Enthalten sind Recipes für:

- Deep Research;
- technische Dokumentation;
- Website-Neuentwicklung;
- bestehende Website Reviews;
- Software Features;
- Bugdiagnose;
- Bildserien;
- Datenbankänderungen;
- Teststrategie und QA;
- Long-Horizon-Agentenarbeit;
- Aufbau und Pflege von Wissensbasen;
- Entwurf und Änderung von Schnittstellenverträgen;
- Infrastrukturänderungen;
- Build, Deploy und Promotion;
- Reliability Baseline und SLOs;
- Produktionsincidents;
- Post-Incident Learning;
- Resilience Game Days;
- Operational Readiness Reviews;
- Data Pipeline Baseline und Design;
- neue Datenquellen und Ingestion;
- Datenqualitätsstörungen und Reconciliation;
- Backfills und Reprocessing;
- Data Engineering Readiness Reviews;
- Architektur-Baseline und Systemdesign;
- Architekturentscheidungen und Trade-offs;
- Systemgrenzen und Dekomposition;
- evolutionäre Architekturänderungen;
- Architektur Readiness Reviews.

> Skills bleiben klein. Workflows verbinden sie.

# Agentenautonomie und Evidence

Agenten dürfen innerhalb eines ausdrücklich oder durch den Projektprozess freigegebenen Scopes selbstständig iterieren.

Dabei gelten insbesondere:

- Kontext gezielt statt maximal laden;
- Context Budget wird nach Informationswert und Outcome optimiert, nicht nach einer künstlichen Token-Minimalzahl;
- gewachsener Kontext wird bei Bedarf auditiert oder verdichtet, ohne harte Constraints, Evidence und Gates zu verlieren;
- Session-Handoffs müssen eigenständig fortsetzbar sein und dürfen keine Freigaben erfinden;
- Delegation beschreibt Ziel, Scope, Rechte, Akzeptanzbedingungen und erwartete Evidence;
- unabhängige Arbeit darf parallelisiert werden, echte Abhängigkeiten nicht;
- parallele Agenten benötigen ausreichend isolierte veränderliche Workspaces;
- ein Loop benötigt Stop- und Eskalationsbedingungen;
- fehlende Spezifikation darf nicht durch stillschweigende Agentenentscheidungen ersetzt werden;
- automatisch prüfbare Invarianten sollten möglichst automatisch geprüft werden;
- riskante, irreversible oder extern sichtbare Aktionen benötigen die dafür definierte Freigabe;
- ein erfolgreicher Agentenlauf ist noch keine fachliche oder technische Freigabe;
- relevante Agentenarbeit soll mit Auftrag, Evidence und Ergebnis nachvollziehbar verbunden werden.

## Capability Detection

Skills sollen nicht stillschweigend ideale Laufzeitfähigkeiten voraussetzen.

```text
bevorzugte Capability
→ vorhanden?
   ├─ ja → verwenden
   └─ nein → definierter Fallback
              ├─ möglich → transparent degradieren
              └─ unmöglich → blocked / unverified
```

Fehlende Fähigkeiten dürfen nicht simuliert oder behauptet werden.

## Observability

Ein gemeinsames Trace-Modell für Agentenarbeit kann verbinden:

```text
Task
→ Run
→ Skill / Workflow
→ Tool Event
→ Evidence
→ Gate
→ Artefakt
→ Outcome
```

Zusätzlich können – sofern die Runtime sie liefert – providerneutrale Usage- und Context-Signale wie Input-/Output-Tokens, Cache-Reads/-Writes, Context-Größe, Tool-Output-Größe, Compaction- oder Handoff-Ereignisse erfasst werden.

Vollständige Prompts, Toolargumente oder Inhalte sind dabei kein Pflichtbestandteil. Metadaten und Datenschutz werden bewusst getrennt.

Diese Agenten-Observability ist nicht mit der System-Observability aus `Reliability-und-System-Observability/` gleichzusetzen.

# Nutzung in Projekten

KI-Agenten arbeiten normalerweise innerhalb eines konkreten Projektrepositories und lesen dieses zentrale Repository nicht automatisch.

Darum können benötigte Skills bewusst repo-lokal übernommen oder durch projektspezifische Agent-Dateien referenziert werden.

Dabei gilt:

- zentrale Fassung = allgemeine kanonische Arbeitsweise;
- lokale Fassung = verfügbare Kopie oder projektspezifischer Adapter;
- projektspezifische Ergänzungen bleiben lokal;
- Änderungen an zentralen Skills werden bewusst übernommen;
- nicht das komplette zentrale Repository ungefiltert in jeden Agentenkontext laden.

Für Datenbankarbeit gilt zusätzlich: Die zentralen Skills beschreiben Arbeitsweise und Gates; konkrete Engine, Version, reales Schema, Migrationstool, Credentials, Datenklassifikation, RPO/RTO und Produktionsfreigaben bleiben lokal.

Für Testing gilt zusätzlich: Die zentralen Skills definieren Methodik und Evidence; konkrete Frameworks, Testumgebungen, Testdaten, Coverage-Ziele, Releasekriterien und produktive Testbefugnisse bleiben lokal.

Für Context-/Token-Arbeit gilt zusätzlich: konkrete Modellfenster, Tokenpreise, Cache-Semantik, Compaction-APIs, Thread-Persistenz, Tool-Schema-Kosten und Runtime-Grenzen bleiben provider- beziehungsweise projektspezifisch. Dauerhafte Wissensbasen werden nicht mit Working Context gleichgesetzt.

Für Wissensmanagement gilt zusätzlich: konkrete Knowledge-Base-Software, Ordner-/Property-Schema, Taxonomie, reale Sources of Truth, Zugriffs- und Datenschutzklassen, Retention-Regeln sowie Bulk-Write-/Delete-Freigaben bleiben lokal.

Für Schnittstellenarbeit gilt zusätzlich: reale Consumer, Architekturgrenzen, Protokolle, Toolchain, kanonische Contract-Artefakte, Compatibility-/Versionierungs-Policy, Auth-Mechanismen, Supportfenster sowie Deprecation-/Removal-Gates bleiben lokal.

Für Infrastruktur-/DevOps-Arbeit gilt zusätzlich: konkrete IaC-/CI-/GitOps-/Container-/Deploymenttools, Provider, Accounts, Cluster, State-Backends, Credentials, Environment-Konfiguration, Policy-Enforcement, Health-/SLO-Schwellen sowie Apply-/Deploy-/Destroy-/Recovery-Gates bleiben lokal. Preview, Plan, Build oder Pipeline-Grün autorisieren keine reale Außenwirkung automatisch.

Für Reliability-/System-Observability-Arbeit gilt zusätzlich: konkrete SLO-/SLA-Ziele, Alert-Schwellen, Severity-/On-Call-Modelle, RTO/RPO, Capacity-/Quota-Limits, Telemetrieprodukte, Dashboards, Runbooks, Recovery-/Failover-Regeln und Produktionsgates bleiben lokal. Incident-Dringlichkeit oder ein geplanter Game Day erweitern keine Tool- oder Produktionsrechte.

Für Data-Engineering-Arbeit gilt zusätzlich: reale Sources of Truth, fachlicher Grain, Consumer, Quality-/Freshness-/Reconciliation-Regeln, Data-Contract-Zusagen, Retention, Plattform-/Toolwahl, historische Semantik sowie Backfill-/Replay-/Publish-Gates bleiben lokal. Job-, DAG-, Contract- oder Quality-Grün autorisieren keine reale Datenänderung automatisch.

Für Software-Architecture-/System-Design-Arbeit gilt zusätzlich: Architecture Drivers, Constraints, fachliche und technische Invarianten, Quality-Ziele, Systemgrenzen, Ownership, akzeptierte ADRs, Last-/Recoverygrenzen, Plattformconstraints, Migrationsfenster und Cutover-/Implementierungsfreigaben bleiben lokal. Ein Architecture Verdict oder Pattern-Fit autorisiert keine reale Änderung automatisch.

Für Auswahl und Dokumentation zentraler Regeln kann `Vorlagen/ki-regeln.template.yml` als Ausgangspunkt verwendet werden.

# Aktualisierung und Quellen

Empfohlener Rhythmus:

- monatlicher Radar-Check;
- monatlicher gezielter Check schneller mutable Upstreams;
- quartalsweise Prüfung langsamer lebender Quellen;
- vierteljährlicher vollständiger Repo-Audit;
- zusätzliche Prüfung bei größeren Modell-, Tool-, Sicherheits- oder Forschungsentwicklungen.

Fachbezogene `Quellen-und-Inspirationen.md` dokumentieren den fachlichen Ursprung von Konzepten.

`Dokumentation/upstream-sources.yml` dokumentiert aktiv beobachtete veränderliche Quellen.

> Upstream-Änderung = Review-Signal, nicht automatischer Sync.

Relevante Änderungen stehen in `CHANGELOG.md`.

## Attribution

Übernommene oder adaptierte Drittinhalte werden in `THIRD-PARTY-NOTICES.md` dokumentiert. Externe Inspirationsquellen ohne übernommene Drittinhalte stehen in den jeweiligen `Quellen-und-Inspirationen.md`-Dateien.

# Pflegekriterium

Neue Regeln oder Skills sollen nur aufgenommen werden, wenn sie:

1. wiederverwendbar sind;
2. einen erkennbaren Qualitäts- oder Sicherheitsgewinn bringen;
3. nicht bloß persönliche oder projektspezifische Vorlieben verallgemeinern;
4. keine unnötigen personenbezogenen Daten enthalten;
5. möglichst konkret beschreiben, wann und wie sie anzuwenden sind;
6. in Skill-Katalog, Evals, Quellen- und Lifecycle-Modell sauber eingeordnet werden können.