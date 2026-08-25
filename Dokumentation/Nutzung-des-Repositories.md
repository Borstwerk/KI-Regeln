# Nutzung des Repositories

## Zweck

Dieses Dokument erklärt, wie `KI-Regeln` sinnvoll in echten Projekten eingesetzt wird.

Das Repository ist keine automatische Master-Steuerung. Es ist eine zentrale Bibliothek aus:

- allgemeinen Regeln;
- begrenzten Skills;
- wiederholbaren Evals;
- Workflows / Recipes;
- Quellen- und Upstream-Governance.

## Grundprinzip

> Allgemeine Arbeitsweise zentral, konkrete Wahrheit lokal.

Zentrale Regeln beschreiben **wie** gearbeitet wird. Projekte definieren **was** konkret gebaut, geschrieben, recherchiert, dokumentiert, geprüft oder freigegeben werden soll.

## Empfohlenes Nutzungsmodell

```text
Projektaufgabe
→ lokale Wahrheit / Anforderungen bestimmen
→ passenden Workflow prüfen
→ nur benötigte Skills auswählen
→ skill-catalog.yml auf Maturity, Capabilities und Evals prüfen
→ lokale Regeln ergänzen
→ arbeiten und Evidence erzeugen
→ passende Reviews / Gates
```

Nicht empfehlenswert:

- das komplette Repository ungefiltert in jeden Agentenkontext zu laden;
- alle Skills in jedes Projekt zu kopieren;
- Workflows als automatische Autorisierung aller enthaltenen Aktionen zu behandeln;
- immer ungeprüft den neuesten `main`-Stand zu übernehmen;
- allgemeine Regeln als Ersatz für Spezifikation, Architektur oder Source of Truth zu benutzen.

## Was ist was?

### Regel

Beschreibt allgemeine Leitplanken und Hintergründe.

### Skill

Beschreibt eine begrenzte Arbeitsdisziplin:

```text
Trigger
→ Prozess
→ Ergebnis / Evidence
```

### Workflow / Recipe

Verbindet mehrere Skills für ein größeres Ziel.

```text
Skill A
→ Handoff
→ Skill B
→ Review
→ Gate
```

### Eval

Prüft, ob ein Skill in typischen, schwierigen und negativen Fällen das erwartete Verhalten zeigt.

### Skill-Katalog

`../skill-catalog.yml` dokumentiert unter anderem:

- Skill-ID und Pfad;
- Maturity;
- Evalabdeckung;
- relevante Capabilities;
- verwandte Skills.

## Maturity richtig lesen

```text
experimental
→ candidate
→ stable
→ deprecated
→ retired
```

`experimental` bedeutet nicht „schlecht“. Es bedeutet: neue oder wesentlich umgebaute Logik, deren formale Praxis-/Evalbasis noch begrenzt ist.

`candidate` bedeutet: bereits praktisch oder konzeptionell bewährt, aber noch nicht breit genug für `stable` abgesichert.

`stable` soll bewusst verdient werden durch:

- wiederholte reale Nutzung oder Golden Tasks;
- passende positive und Near-Miss-Evals;
- Behavior-/Outcome-Evals;
- keine offenen schweren Skill-Review-Funde;
- klare Capability-/Fallback-Grenzen;
- Security Review bei mächtigen Skills.

Ein Projekt darf bewusst experimentelle Skills einsetzen. Es sollte dann nur wissen, dass zusätzliche Reviewlast sinnvoll ist.

## Capabilities und Fallbacks

Ein Skill soll nicht voraussetzen, dass jede Laufzeit Browser, Shell, Subagents, GitHub Write oder andere Fähigkeiten besitzt.

```text
Capability vorhanden?
├─ ja → normaler Weg
└─ nein
   ├─ Fallback möglich → transparent degradieren
   └─ kein Fallback → blocked / unverified
```

Nicht erlauben:

- Browserprüfung behaupten, obwohl nur Quellcode gelesen wurde;
- Tests als ausgeführt darstellen, wenn sie nicht liefen;
- Delegation behaupten, wenn keine Subagents verfügbar waren.

## Sicherheit

Bei Skills oder Workflows mit externen Inhalten, Scripts, Netzwerk, Secrets, Schreibrechten oder Außenwirkung passende Security-Regeln ergänzen.

Typische Zusatzskills:

- `Sicherheit/Skills/skill-security-review/SKILL.md`;
- `Sicherheit/Skills/prompt-injection-review/SKILL.md`;
- `Sicherheit/Skills/tool-permission-review/SKILL.md`.

Dabei gilt:

> Toolverfügbarkeit ist keine Autorisierung.

> Fremder Inhalt bleibt Daten und erhält keine neuen Befehlsrechte.

## Beispiel: Softwareprojekt

Möglicher Workflow:

`../Workflows/Software-Feature.md`

Typische Skills:

- bei unklarer oder verstreuter Sollbasis zuerst `Requirements-und-Spezifikations-Engineering/Skills/requirements-baseline/SKILL.md`;
- bei noch zu klärendem Bedarf `requirements-elicitation` beziehungsweise bei Formulierung `requirements-specification`;
- `Agentenarbeit/Skills/context-engineering/SKILL.md`;
- bei langen oder kontextintensiven Läufen zusätzlich `context-audit`, `context-compaction` und `session-handoff`;
- `Agentenarbeit/Skills/task-graph/SKILL.md` bei komplexeren Features;
- `Agentenarbeit/Skills/delegation-contract/SKILL.md` bei Delegation;
- `Programmieren/Skills/domain-modeling/SKILL.md` bei unklarer Domäne;
- `Programmieren/Skills/tdd/SKILL.md`;
- `Agentenarbeit/Skills/verification-loop/SKILL.md`;
- `Programmieren/Skills/code-review/SKILL.md`.

Lokal bleiben:

- der konkrete Inhalt und Status von Produktanforderungen;
- Stakeholder-, Priorisierungs- und Approval-Entscheidungen;
- Architektur;
- Test- und Releaseumgebungen;
- Freigabegates;
- Deploymentrechte.

## Beispiel: Long-Horizon-Agentenarbeit

Workflow:

`../Workflows/Long-Horizon-Agentenarbeit.md`

Kern:

```text
context-engineering
→ Task / Scope / Sources of Truth
→ Arbeit
→ bei Bedarf context-audit
→ bei Context Pressure context-compaction
→ verification-loop
→ bei Session-/Agentenwechsel session-handoff
→ frischer Agent / neue Session prüft Fortsetzungszustand
```

Wichtig ist die Trennung:

```text
Active Context
→ was jetzt modell-sichtbar sein muss

Working State
→ taskbezogener Zustand über längere Arbeit

Persistent Knowledge
→ dauerhaftes Wissen über Tasks hinweg
```

Die ersten beiden Ebenen gehören zur Agentenarbeit. Persistent Knowledge wird über den Bereich `Wissensmanagement/` gepflegt und ist kein Ersatz für Context Engineering.

Context-/Token-Effizienz bedeutet dabei nicht, Tokens um jeden Preis zu minimieren. Relevante Constraints, Entscheidungen, Evidence und Sources of Truth dürfen nicht für eine künstliche Zielquote weggekomprimiert werden.

Lokal bleiben insbesondere:

- konkretes Modell und Kontextfenster;
- providerabhängige Tokenpreise;
- Prompt-Cache-Verhalten;
- verfügbare Usage-Metriken;
- Session-/Thread-Persistenz der Laufzeit;
- projektspezifische Handoff- und Retention-Regeln.

## Beispiel: Bugdiagnose

Workflow:

`../Workflows/Bugdiagnose.md`

Kern:

```text
diagnose
→ Root Cause / Fix
→ verification-loop
→ code-review
```

Logs, HARs und Traces vor Weitergabe auf Secrets und personenbezogene Daten prüfen.

## Beispiel: Datenbankänderung

Workflow:

`../Workflows/Datenbank-Aenderung.md`

Kern:

```text
database-design
→ schema-migration
→ optional transaction-review
→ database-query-review
→ optional query-performance / database-operations
→ database-review
→ Human Gate
→ lokale Ausführung
→ Post-Change-Verifikation
```

Lokal bleiben insbesondere reale Engine und Version, Schema, Migrationstool, Datenklassifikation, RPO/RTO, Credentials und Produktionsfreigaben.

## Beispiel: Teststrategie und QA

Workflow:

`../Workflows/Teststrategie-und-QA.md`

Kern:

```text
bestätigte Requirements / Acceptance Criteria / Risiken
→ test-strategy
→ test-design
→ passende Integration-/Contract-/E2E-/Failure-Tests
→ optional exploratory-testing
→ bei Bedarf flaky-test-diagnosis
→ test-suite-review
→ verification-loop mit frischer Evidence
→ lokales Release-/Quality-Gate
```

Requirements Engineering definiert dabei das gewünschte Soll und dessen Akzeptanzbedingungen. Testing und QA entscheidet, mit welchem Testportfolio und welcher Evidence das relevante Risiko geprüft wird.

Lokal bleiben konkrete Testframeworks, Testdaten, Testumgebungen, Coverage-/Releaseziele und Befugnisse für produktive Testaktionen.

## Beispiel: Deep Research

Workflow:

`../Workflows/Deep-Research.md`

Kern:

```text
research-plan
→ deep-research
→ source-evaluation
→ research-synthesis
→ claim-verification bei kritischen Claims
→ citation-audit
```

Für eine kleine aktuelle Faktenfrage kann dagegen `web-search` allein genügen.

Lokal bleiben:

- konkrete Research-Frage;
- interne Quellen;
- zulässige Datenräume;
- Freshness;
- fachliche Bewertungskriterien.

## Beispiel: Wissensbasis

Workflow:

`../Workflows/Wissensbasis-Aufbauen-und-Pflegen.md`

Kern:

```text
knowledge-base-design
→ knowledge-ingest
→ knowledge-distill
→ optional knowledge-synthesis
→ knowledge-query
→ wiederkehrend knowledge-maintenance
→ bei größeren Meilensteinen knowledge-base-review
```

Wenn das Wissen erst extern erarbeitet werden muss:

```text
research-plan / deep-research
→ source-evaluation
→ research-synthesis
→ knowledge-ingest
→ knowledge-distill
```

Für den Agentenlauf gilt anschließend:

```text
Persistent Knowledge
→ knowledge-query / Retrieval
→ context-engineering
→ Active Context
```

Lokal bleiben insbesondere:

- konkretes Tool wie Obsidian, Notion oder eine andere Knowledge Base;
- Ordner-, Property-, Relation- oder Taxonomieschema;
- reale Sources of Truth und erlaubte Quellräume;
- Datenschutz-, Sichtbarkeits- und Retention-Regeln;
- technische Retrieval-/RAG-Implementierung;
- Freigaben für Bulk-Ingest, Mass-Merge, Rewrites und Delete.

## Beispiel: Schnittstellenvertrag

Workflow:

`../Workflows/Schnittstellenvertrag-Entwerfen-und-Aendern.md`

Für einen neuen Vertrag:

```text
bestätigte Requirements + lokale Architektur-/Domain-Sources-of-Truth
→ interface-design
→ je nach Stil http-api-design / event-contract-design / passende Fachregeln
→ Contract Artifact
→ Implementierung
→ contract-testing
→ optional integration-testing
→ interface-review
→ lokales Gate
```

Für einen bestehenden Vertrag:

```text
Baseline + Consumer
→ contract-change-review
→ COMPATIBLE / ROLLOUT-SENSITIVE / BREAKING / UNVERIFIED
→ Migration / Deprecation nach Verdict
→ Implementierung
→ contract-testing
```

Lokal bleiben insbesondere:

- reale Consumer und deren Deployment-/Upgradefreiheit;
- Architekturgrenzen und Ownership;
- tatsächlicher Transport/Framework/IDL;
- kanonische Contract-Dateien;
- Compatibility- und Versionierungs-Policy;
- Auth-/Tenant-Mechanismen;
- Support-, Migration-, Deprecation- und Removal-Gates.

## Beispiel: Infrastrukturänderung

Workflow:

`../Workflows/Infrastruktur-Aenderung.md`

Kern:

```text
lokale Architektur / Desired State
→ infrastructure-as-code
→ READ / VALIDATE
→ PLAN / PREVIEW
→ infrastructure-change-review
→ lokales Apply-/Execution-Gate
→ reale Änderung
→ Fresh Verification
→ Actual State / Drift prüfen
```

Besonders wichtig:

```text
Preview
≠ Apply

SAFE_TO_PROCEED_TO_GATE
≠ APPLY AUTHORIZED
```

Lokal bleiben insbesondere:

- IaC-Tool und Provider;
- Accounts, Subscriptions, Cluster, Regionen und Namespaces;
- State-Backend und Ressourcenzuordnung;
- Credentials und Execution Identities;
- Backup-/Recovery-Anforderungen;
- Policy-Enforcement;
- Apply-/Destroy-/State-/Recovery-Gates.

## Beispiel: Build, Deploy und Promotion

Workflow:

`../Workflows/Build-Deploy-und-Promotion.md`

Kern:

```text
Source
→ ci-pipeline-design
→ Build
→ optional container-build
→ Test-/Security-Evidence
→ identifizierbares Artifact
→ deployment-strategy
→ Deploy Gate
→ Deployment
→ Fresh Health-/Business-Evidence
→ Promote / Pause / Abort
→ Release
```

Bei GitOps kann stattdessen eine Desired-State-Änderung nach `gitops-design` durch einen Controller reconciliert werden. In diesem Fall kann bereits ein Merge in die produktive Desired-State-Quelle extern wirksame Folgen haben.

Lokal bleiben insbesondere:

- Pipeline- und Runnerplattform;
- Artifact Registry;
- Container-/Build-Tooling;
- Release- und Trafficmechanik;
- reale Health-/SLO-/Business-Schwellen;
- GitOps-Controller und dessen Rechte;
- Deployment-/Promotion-/Rollback-Gates.

## Beispiel: Reliability Baseline und SLOs

Workflow:

`../Workflows/Reliability-Baseline-und-SLOs.md`

Kern:

```text
bestätigte lokale Requirements / Critical Journeys
→ slo-design
→ system-observability-design
→ alert-design
→ optional capacity-planning
→ reliability-review
→ lokales Reliability-/Produkt-Gate
```

Wichtig ist die Trennung:

```text
Requirements / Business
→ warum und wie zuverlässig ein Flow sein muss

Reliability
→ wie das Ziel messbar und betrieblich prüfbar wird
```

Lokal bleiben insbesondere:

- konkrete SLO-Ziele und Messfenster;
- SLAs und vertragliche Konsequenzen;
- Alert-Schwellen, Severity- und On-Call-Modelle;
- konkrete Telemetrie-/Monitoringprodukte;
- RTO/RPO;
- Capacity Limits, Quotas und Kostenbudgets.

## Beispiel: Produktionsincident

Workflow:

`../Workflows/Produktionsincident.md`

Kern:

```text
Signal / tatsächlicher Impact
→ incident-response
→ diagnose / passende Fachskills
→ Mitigation Proposal
→ Human-/Execution-Gate
→ autorisierte technische Aktion
→ Fresh Recovery Evidence
→ Abschluss / Postmortem-Trigger
```

Besonders wichtig:

```text
Incident-Dringlichkeit
≠ Produktionsautorisierung
```

`incident-response` koordiniert. Root-Cause-Diagnose, Datenbank-, Infra-, Interface- oder Security-Arbeit bleibt bei den jeweiligen Fachdomänen.

Restart, Rollback, Restore, Failover, Traffic Switch, Scaling und andere reale Betriebsaktionen bleiben lokal gated.

## Beispiel: Resilience Game Day

Workflow:

`../Workflows/Resilience-Game-Day.md`

Kern:

```text
Failure-Risiko / Annahme
→ resilience-experiment [PLAN]
→ Steady State + Hypothese
→ Fault / Environment / Blast Radius
→ Observation + Abort + Recovery
→ Permission / Execution Gate
→ Experiment nur wenn autorisiert
→ Fresh Recovery Evidence
→ Hypothese bewerten
```

Ein gezielter reproduzierbarer Fault innerhalb eines Testscopes bleibt `failure-testing`.

Produktion ist kein notwendiges Reifeziel. Die gewählte Umgebung soll die benötigte Aussagekraft bei vertretbarem Risiko liefern.

## Beispiel: Operational Readiness

Workflow:

`../Workflows/Operational-Readiness-Review.md`

Kern:

```text
Critical Journeys / Objectives
+ Observability / Alerts
+ Capacity / Dependencies
+ Recovery / Runbooks
+ Testing / Resilience Evidence
+ Deployment / Rollback Evidence
+ Security / Permissions
+ Ownership / On-Call
→ reliability-review
→ Findings / Missing Evidence
→ lokales Go / No-Go
```

Operational Readiness ist bewusst ein Workflow und kein Mega-Skill.

Lokal bleiben insbesondere:

- tatsächliche Go-/No-Go-Entscheidung;
- verbindliche Reliability-/Recovery-Ziele;
- Owner und On-Call-Struktur;
- Produktionsrechte;
- Release-/Promotion-/Failover-Gates.

## Beispiel: Data Pipeline Baseline und Design

Workflow:

`../Workflows/Data-Pipeline-Baseline-und-Design.md`

Kern:

```text
lokaler Business-/Consumerkontext + bestätigte Requirements
→ data-pipeline-design
→ data-ingestion-design
→ data-transformation-design
→ optional analytical-data-modeling
→ data-quality-design
→ data-contract-design
→ data-lineage-analysis
→ data-orchestration-design
→ data-engineering-review
→ lokales Implementierungs-/Publish-Gate
```

Lokal bleiben insbesondere Source of Truth, Consumer, Grain, Freshness-/Qualityanforderungen, Security/Privacy, Retention, Plattform- und Kostenentscheidungen.

## Beispiel: Neue Datenquelle und Ingestion

Workflow:

`../Workflows/Neue-Datenquelle-und-Ingestion.md`

Kern:

```text
Source-/Consumerkontext
→ data-ingestion-design
→ data-contract-design
→ data-quality-design
→ data-lineage-analysis
→ data-orchestration-design
→ lokales Implementierungs-/Publish-Gate
```

`updated_at`, CDC oder ein bestimmter Streamingstack sind keine automatische Garantie für verlustfreie oder exactly-once Verarbeitung. Source-Capabilities, Deletes, Ordering, Offset/Checkpoint, Retention und Replay bleiben konkret zu prüfen.

## Beispiel: Datenqualitätsstörung

Workflow:

`../Workflows/Datenqualitaetsstoerung-und-Reconciliation.md`

Kern:

```text
Daten-/Consumerproblem
→ data-quality-design
→ data-lineage-analysis
→ data-transformation-design / data-ingestion-design
→ bei aktivem Impact incident-response
→ Reconciliation
→ optional kontrolliertes Reprocessing
→ Fresh Verification
```

Ein grüner Scheduler- oder Jobstatus beweist weder Vollständigkeit noch fachliche Korrektheit des Datasets.

## Beispiel: Backfill und Reprocessing

Workflow:

`../Workflows/Backfill-und-Reprocessing.md`

Kern:

```text
Reprocessingbedarf
→ Transformations-/Ingest-Semantik
→ Lineage / Consumerimpact
→ Quality / Reconciliation
→ Orchestrierungsplan mit bounded scope
→ lokales Execution Gate
→ autorisiertes Reprocessing
→ Fresh Reconciliation / Publish
```

Besonders wichtig:

```text
Backfill-Plan
≠ Backfill-Autorisierung
```

Lokal bleiben Zeitraum/Partitionen, historische Semantik, Write-/Idempotenzstrategie, Parallelität, Source-/Target-Last, Consumerkommunikation, Rollback/Recovery und reale Ausführungsrechte.

## Beispiel: Data Engineering Readiness

Workflow:

`../Workflows/Data-Engineering-Readiness-Review.md`

Kern:

```text
Sources / Grain / Semantik
+ Ingestion / Transformation
+ Quality / Freshness / Reconciliation
+ Contract / Lineage
+ Orchestrierung / Replay
+ Publish / Lifecycle
+ Runtime-Evidence
→ data-engineering-review
→ Findings / Missing Evidence
→ lokales Go / No-Go beziehungsweise Publish-Gate
```

Repo-, SQL-, DAG- und Contractdateien belegen Design. Wo Produktionsreife von realem Datenzustand abhängt, bleibt Runtime-/Daten-Evidence notwendig.

## Beispiel: Architektur-Baseline und Systemdesign

Workflow:

`../Workflows/Architektur-Baseline-und-Systemdesign.md`

Kern:

```text
bestätigte lokale Requirements / Constraints
→ architecture-baseline bei bestehendem System
→ Drivers / Invarianten / Critical Flows
→ system-design
→ optional architecture-tradeoff-analysis
→ architecture-review
→ optional adr
→ lokales Implementierungs-/Entscheidungsgate
```

Die Baseline trennt aktuelle Implementierung, gültige ADRs, Dokumentation und Runtime-Evidence. Ein altes Diagramm oder eine plausible Ordnerstruktur reicht nicht als bestätigte Ist-Architektur.

Lokal bleiben insbesondere Architecture Drivers, Qualitätsziele, Last-/Recoverygrenzen, System Boundary, Ownership, akzeptierte ADRs, Plattformconstraints und technische Freigaben.

## Beispiel: Architekturentscheidung und Trade-off

Workflow:

`../Workflows/Architekturentscheidung-und-Tradeoff.md`

Kern:

```text
Decision Scope / bestätigte Drivers
→ viable Kandidaten
→ konkrete Quality-Szenarien
→ architecture-tradeoff-analysis
→ Sensitivity Points / Missing Evidence
→ architecture-review
→ optional adr
```

Nur ernsthafte Alternativen werden verglichen. Ein Kandidat, den ein verbindlicher Constraint bereits ausschließt, wird nicht künstlich als Peer bewertet. Eine undurchsichtige Gesamtnote ersetzt keine Evidence Chain.

## Beispiel: Systemgrenze und Dekomposition

Workflow:

`../Workflows/Systemgrenze-und-Dekomposition.md`

Kern:

```text
System Context
→ domain-modeling bei Bedarf
→ architecture-decomposition
→ Public Surfaces / Dependency Direction
→ Service-Split-Gate
→ interface-design für konkrete Verträge
→ optional architecture-tradeoff-analysis
```

Ein Bounded Context, eine Teamgröße, ein Shared-DB-Befund oder das Wort „Microservices“ erzwingt keinen eigenen Service. Erst die logische Verantwortungsgrenze begründen, danach Deployment-/Servicegrenzen entscheiden.

## Beispiel: Evolutionäre Architekturänderung

Workflow:

`../Workflows/Evolutionaere-Architekturaenderung.md`

Kern:

```text
Architecture 0
→ Zielentscheidung / Drivers
→ architecture-evolution
→ Migrationsslices und Zwischenzustände
→ Contract-/Data-/Deployment-Handoffs
→ Success Evidence / Abort / Rollback
→ architecture-conformance-review
→ lokales Cutover-/Execution-Gate
```

Besonders wichtig:

```text
Migrationsplan
≠ Cutover-Autorisierung
```

Codeänderungen, Datenmigrationen, Deployments, Traffic Switches und Retirement bleiben bei den zuständigen Fachprozessen und lokalen Gates.

## Beispiel: Architektur Readiness

Workflow:

`../Workflows/Architektur-Readiness-Review.md`

Kern:

```text
Requirements / Drivers
+ Architecture Baseline / Zielbild
+ Conformance / Drift
+ relevante Fach-Evidence
→ architecture-review
→ Findings / Missing Evidence
→ READY_FOR_LOCAL_GATE / READY_WITH_FINDINGS / BLOCKED / UNVERIFIED
→ lokales Go / No-Go außerhalb des Reviews
```

Patternreinheit ist kein Readiness-Kriterium. Wenn Produktionsreife von Runtime-, Capacity-, Failure-, Security- oder Daten-Evidence abhängt, reicht ein sauberes Repository oder ADR-Set nicht aus.

## Beispiel: Requirements-Baseline und Spezifikation

Workflow:

`../Workflows/Requirements-Baseline-und-Spezifikation.md`

Kern:

```text
bestehende Spezifikation / Tickets / Entscheidungen / Ist-Evidence
→ requirements-baseline
→ Lücken / Konflikte / Autorität klären
→ requirements-specification
→ acceptance-criteria-design
→ requirements-traceability
→ requirements-validation
→ requirements-review
→ lokales Approval-/Baseline-Gate
```

Brownfield-Code, Tests oder aktuelle UI können wertvolle Evidence für das Ist-Verhalten liefern. Sie werden aber nicht stillschweigend zum gewünschten Soll erklärt.

Lokal bleiben insbesondere Stakeholderautorität, kanonische Requirements-Quelle, Prioritäten, konkrete Zielwerte, regulatorische/vertragliche Vorgaben und Approval-Policy.

## Beispiel: Requirements Elicitation

Workflow:

`../Workflows/Requirements-Elicitation-und-Klaerung.md`

Kern:

```text
Problem / Ziel / vorhandene Evidence
→ Stakeholder- und Quellenmap
→ requirements-elicitation
→ Aussagen als confirmed / inferred / assumption / open question trennen
→ Scope / Constraints / Konflikte klären
→ bestätigte Requirement-Kandidaten
→ lokales Review
```

Elicitation ist kein Formularzwang. Interviews, Workshops, Dokumentanalyse, Beobachtung oder Repository-Evidence werden nach Kontext gewählt. Ein Vollständigkeitsscore ersetzt keine konkrete Lückenanalyse.

## Beispiel: Acceptance Criteria und Traceability

Workflow:

`../Workflows/Acceptance-und-Traceability.md`

Kern:

```text
bestätigte Requirements
→ acceptance-criteria-design
→ beobachtbare Akzeptanzbedingungen
→ requirements-traceability
→ Quellen / Ziele / Acceptance / downstream Evidence verbinden
→ Gap- und Konsistenzcheck
```

EARS, Given-When-Then oder Gherkin können helfen, wenn sie zur Art des Verhaltens passen. Kein Format ist Pflicht. Acceptance Criteria beschreiben Akzeptanzbedingungen; konkrete Testfälle und Testdaten gehören anschließend zu Testing und QA.

## Beispiel: Requirement Change

Workflow:

`../Workflows/Requirement-Aenderung-und-Impact.md`

Kern:

```text
Änderungsvorschlag
→ requirements-change-analysis
→ betroffene Ziele / Requirements / Acceptance / Trace Links
→ Downstream-Impact auf Architecture / Interfaces / Data / Reliability / Tests
→ Konflikte / Migration / offene Entscheidungen
→ lokales Change-/Approval-Gate
→ erst danach fachdomänenspezifische Umsetzung
```

Besonders wichtig:

```text
Requirement Change Analysis
≠ Downstream Change Authorization
```

Der Skill darf Auswirkungen benennen und Handoffs vorbereiten, aber keine Code-, Schema-, Contract-, Infrastruktur- oder Produktionsänderung eigenmächtig ausführen.

## Beispiel: Requirements Readiness

Workflow:

`../Workflows/Requirements-Readiness-Review.md`

Kern:

```text
Baseline / Sources / Stakeholder
+ Scope / Constraints / Assumptions
+ Functional / Quality Requirements
+ Acceptance Criteria
+ Traceability / offene Konflikte
→ requirements-validation
→ requirements-review
→ Findings / Missing Evidence
→ READY_FOR_LOCAL_GATE / READY_WITH_FINDINGS / BLOCKED / UNVERIFIED
→ lokales Approval außerhalb des Reviews
```

`READY_FOR_LOCAL_GATE` bedeutet nur, dass der Requirements-Stand genügend Evidence für die nächste lokale Entscheidung besitzt. Es ist weder fachliche Abnahme noch Implementierungs-, Release- oder Produktionsfreigabe.

## Beispiel: Technische Dokumentation

Workflow:

`../Workflows/Technische-Dokumentation.md`

Kern:

```text
optional Recherche
→ docs-plan
→ passender Dokumenttyp-Skill
→ technical-writing
→ docs-review
```

Lokal bleiben reale Sources of Truth, Terminologie, Zielgruppen, Ownership und betriebliche Regeln.

## Beispiel: Website-Neuentwicklung

Workflow:

`../Workflows/Website-Neuentwicklung.md`

Kern:

```text
frontend-design
→ design-system
→ greybox
→ web-content
→ Implementierung
→ accessibility-review
→ frontend-performance
→ visual-verification
→ web-design-review
```

Lokal bleiben Marke, realer Content, `DESIGN.md`, Framework, Komponentenbibliothek, Performancebudgets, Hosting und Releaseweg.

Für eine bestehende Seite siehe `../Workflows/Bestehende-Website-Review.md`.

## Beispiel: Bildserie

Workflow:

`../Workflows/Bildserie.md`

Kern:

```text
entitaetsbibel
→ bild-prebrief
→ Generierung
→ bildreview
→ serien-kontinuitaetscheck
→ Abschlussaudit
```

Charakterbibeln, konkrete Referenzbilder und Welt-/Serienkanon bleiben lokal.

## Beispiel: Schreibprojekt

Typische Skills:

- `Schreiben/Skills/natuerliches-schreiben/SKILL.md`;
- `Schreiben/Skills/kreatives-schreiben/SKILL.md`;
- `Schreiben/Skills/stilreview/SKILL.md`.

Figuren, Weltlogik, Stimme und Projektkanon bleiben lokal.

## Beispiel: Skill-Entwicklung

Für einen neuen zentralen Skill:

```text
skill-authoring
→ skill-review
→ Evals
→ bei relevanten Capabilities skill-security-review
→ Maturity-Entscheidung
```

Neue zentrale Skills starten normalerweise `experimental`.

Ein projektspezifischer Sonderfall gehört dagegen eher in lokale Agentenregeln als in einen neuen zentralen Skill.

## Projektmanifest

Vorlage:

`../Vorlagen/ki-regeln.template.yml`

Das Manifest kann dokumentieren:

- gepinnte zentrale Version oder Commit;
- ausgewählte Regeln;
- ausgewählte Skills;
- ausgewählte Workflows;
- projektspezifische Qualitäts-/Maturity-Policy;
- lokale Projektregeldateien;
- optional projektspezifischen `requirements_context` und `architecture_context`, ohne deren Werte aus zentralen Defaults abzuleiten.

Beispiel:

```yaml
source: Borstwerk/KI-Regeln
version: "<released-version-or-commit>"

skills:
  - Programmieren/Skills/diagnose
  - Programmieren/Skills/code-review

workflows:
  - Workflows/Bugdiagnose.md

quality_policy:
  minimum_maturity: candidate
  require_security_review_for_powerful_skills: true
```

## Updates bewusst übernehmen

```text
neue zentrale Version / Upstream-Änderung
→ Changelog / Diff prüfen
→ betroffene Skills und Workflows identifizieren
→ Evals und Security-Auswirkung prüfen
→ bewusst übernehmen oder ablehnen
→ Projektmanifest aktualisieren
```

Ein Upstream-Update ist nur ein Review-Signal.

## Wichtige Warnung

Ein Skill oder Workflow ersetzt niemals:

- eine Spezifikation;
- eine Architekturentscheidung;
- eine Research-Frage oder fachliche Definition;
- eine reale Source of Truth;
- einen Serienkanon;
- eine Markenentscheidung;
- eine Projektfreigabe;
- menschliche Verantwortung.

## Leitgedanke

> Nicht möglichst viele Regeln laden, sondern die richtigen Regeln und die richtige Reife für die aktuelle Aufgabe wählen.