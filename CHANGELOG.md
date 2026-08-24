# Changelog

Dieses Dokument hält relevante Änderungen am Repository fest.

Die Versionierung ist datumsbasiert. Eine Version beschreibt einen bewusst nutzbaren Stand des zentralen Regelwerks.

## Unreleased

Noch nicht als eigener Versionsstand veröffentlichte Änderungen werden zunächst hier gesammelt.

### Reliability und System-Observability

Neuer tool- und providerneutraler Hauptbereich für Zuverlässigkeitsziele, System-Observability, Betriebsreaktion und Resilience:

- klare Trennung von Agenten-Observability und Runtime-/System-Observability;
- Reliability entlang der Ebenen Objectives, Sensing, Response sowie Learning & Resilience strukturiert;
- SLI-Spezifikation, Messimplementierung, SLO, Messfenster und Error Budget getrennt modelliert; konkrete Zielwerte werden nicht ohne lokale Anforderungsgrundlage erfunden;
- `SLO ≠ SLA ≠ RTO/RPO` als zentrale Grenze festgeschrieben;
- System-Observability als Fähigkeit modelliert, relevante Zustands- und Betriebsfragen aus externer Evidence beantworten zu können; Metrics, Logs, Traces und weitere Telemetrieformen sind mögliche Signale, keine Definition von Observability;
- Alerting nach Actionability, Nutzer-/Serviceimpact, Symptom-vs.-Cause, Noise, Fensterung und Runbook-/Next-Action-Bezug statt universeller Thresholds oder Severitymodelle;
- Incident Response mit Impact, Rollen, Incident State, Mitigation, Kommunikation, Handoff und Fresh Recovery Evidence; Incident-Dringlichkeit erweitert keine Rechte und ersetzt keine Human Gates;
- Postmortems mit Timeline, Evidence, beitragenden Faktoren, Detection-/Response-/Recovery-Gaps und Follow-ups statt erzwungener Einzelursache;
- Capacity Planning als eigene Arbeitsdisziplin zwischen gemessener Belastungsgrenze und technischer Provisionierung; Peak, Wachstum, Saturation, Failure Domains, Lead Time, Headroom und Unsicherheit werden explizit;
- Recovery-Ziele RTO/RPO bleiben lokale Business-/Requirement-Werte; Reliability operationalisiert und prüft sie, während Backup/Restore/Failover technisch in den zuständigen Domänen bleiben;
- Resilience über Failure Domains, Dependency Health, Graceful Degradation und Recovery-Verhalten beschrieben; konkrete Architekturpatterns bleiben bei Software Architecture;
- Chaos Engineering und Game Days als kontrollierte Hypothesenexperimente mit Steady State, Blast Radius, Abort und Recovery statt als destruktiver Stunt oder Produktionspflicht;
- Toil als Signal für nicht nachhaltigen Betrieb eingeordnet, ohne universelle Prozentziele;
- Operational Readiness als zusammengesetzte Evidence und Workflow statt als Mega-Skill modelliert;
- acht neue Skills `slo-design`, `system-observability-design`, `alert-design`, `incident-response`, `incident-postmortem`, `capacity-planning`, `resilience-experiment` und `reliability-review`;
- alle acht Skills starten `experimental` mit `partial` Evalabdeckung;
- 48 Evalfälle definiert, sechs je Skill, einschließlich SLO-/RTO-Grenzen, Telemetrie-/PII-Fällen, Alert-Noise, Incident-Gates, Capacity-Evidence, Failure-Testing-vs.-Chaos und unabhängigen Reliability-Reviews; die Fälle sind definiert, nicht automatisch als ausgeführt oder bestanden zu verstehen;
- fünf Workflows `Reliability-Baseline-und-SLOs.md`, `Produktionsincident.md`, `Post-Incident-Learning.md`, `Resilience-Game-Day.md` und `Operational-Readiness-Review.md`;
- neues menschliches `Dokumentation/Skill-Handbuch-Reliability-und-System-Observability.md`;
- neue Capability `controlled-fault-injection-gated` für ausdrücklich freigegebene Resilience-Experiment-Ausführung;
- bestehende Grenzen in `Testing-und-QA/`, `Infrastruktur-und-DevOps/`, `Schnittstellen-und-Vertraege/` und `Agentenarbeit/` auf den realen Reliability-Bereich umgestellt;
- `failure-testing` mit `resilience-experiment` und `deployment-strategy` mit `slo-design`, `system-observability-design` und `reliability-review` verbunden;
- Skill-Katalog auf 95 zentrale Skills erweitert;
- Quellenbasis aus Google SRE, CNCF/OpenTelemetry, Principles of Chaos Engineering, ISO/IEC 25010 sowie AWS-/Azure-/GCP-Gegenprüfungen und ausgewählten aktuellen öffentlichen Agent-Skills, ohne provider- oder toolgebundene Defaults zu universalisieren.

### Infrastruktur und DevOps

Neuer tool- und providerneutraler Hauptbereich für Infrastructure as Code, Delivery-Automation und kontrollierte Infrastrukturänderungen:

- klare Zustandsgrenze `Desired State ≠ Actual State` mit expliziter Ownership von Configuration, Tool-/Controller-State und realem Zielzustand;
- Infrastructure as Code als reviewbare und reproduzierbare Zustandsbeschreibung statt Terraform-spezifische Universalregel modelliert;
- Drift als Befund mit bewusster Entscheidung zwischen Übernahme in Desired State und Rückführung des Actual State statt automatischer Korrekturanweisung;
- Change Preview, Plan, Review, Gate und Apply als getrennte Schritte mit der Grundregel `Preview ≠ Apply` und `Plan Review ≠ Apply Authorization`;
- Freshness von Plans/Previews und Grenzen von Dry-Run-/Simulationsevidence ausdrücklich berücksichtigt;
- Risikoklassen `READ / VALIDATE`, `BUILD`, `PLAN / PREVIEW`, `CHANGE / DEPLOY` und `DESTRUCTIVE / STATE / RECOVERY`;
- Environment-Parität als kontrollierte, dokumentierte Unterschiede statt Dogma „nur Values dürfen differieren“;
- CI-Pipelines als Orchestrierung von Triggern, DAG, Artifacts, Caches, Credentials, Environment-Grenzen und Gates; Teststrategie bleibt `Testing-und-QA/`;
- Build-Artefakte, Identität, Provenance und Reproduzierbarkeit mit Trennung `Build ≠ Deploy ≠ Release`;
- Container Build und Runtime Contract ohne Dockerpflicht, einschließlich Build-/Runtime-Trennung, Base-/Dependency-Pinning, Secret-Hygiene, Signals, Health und Runtime-Konfiguration;
- Deploymentstrategien Rolling, Blue-Green, Canary, Shadow, Recreate und Feature-gated Release risikobasiert statt als Pflichtmuster;
- Promotion, Pause, Abort und Rollback mit lokaler Health-/SLO-Evidence; konkrete Health-Schwellen bleiben beim späteren Reliability-/Produktkontext;
- Rollback ausdrücklich nicht als Undo bereits erfolgter Datenänderungen, Events oder externer Nebenwirkungen behandelt;
- GitOps als eigener fachlicher Schnitt wegen Continuous Reconciliation und dauerhafter Controller-Autorität; Desired-State-Merge kann bei Auto-Reconcile eine extern wirksame Aktion sein;
- Kubernetes als wichtige Referenzplattform für Controller, Workloads und Rollouts, aber nicht als universelle Infrastrukturvoraussetzung;
- Policy as Code als technische Decision-/Enforcement-Schicht eingeordnet; Inhalt von Security Policies bleibt `Sicherheit/`;
- Secrets, Permissions und Execution Boundaries mit getrennten Rechten für Read/Validate, Build, Preview und reale Change-/Recovery-Aktionen;
- Skills `infrastructure-as-code`, `infrastructure-change-review`, `ci-pipeline-design`, `container-build`, `deployment-strategy`, `gitops-design` und `infrastructure-review`;
- alle sieben Skills starten `experimental` mit `partial` Evalabdeckung;
- Evalpacks für alle sieben Skills mit Drift-, stale-Preview-, destructive-Change-, Secret-/Fork-, Container-Runtime-, Rollback-, GitOps- und Evidence-Grenzfällen;
- Workflows `Workflows/Infrastruktur-Aenderung.md` und `Workflows/Build-Deploy-und-Promotion.md`;
- menschliches `Dokumentation/Skill-Handbuch-Infrastruktur-und-DevOps.md`;
- Quellenbasis aus Terraform, OpenTofu, Kubernetes, OpenGitOps, Argo CD/Rollouts, OPA, SLSA, Docker Build sowie aktuellen offiziellen und Community-Agent-Skills;
- keine provider-/tool-spezifischen Defaults, festen Canary-Schwellen oder automatischen Apply-/Deploy-Freigaben zur zentralen Wahrheit erklärt.

### Schnittstellen und Verträge

Neuer technologieübergreifender Hauptbereich für Interface- und Contract-Engineering:

- Schnittstellen als beobachtbare Zusage zwischen Provider und Consumer statt bloß als Transport oder Schema modelliert;
- klare Grenze zu späterem Software Architecture: Architektur entscheidet, warum und wo eine Grenze existiert; Interface Design definiert die Zusagen über diese Grenze;
- Interaktionsstile HTTP, GraphQL, RPC/IDL, Events sowie Webhooks/Callbacks nach Consumer- und Kommunikationsanforderungen statt Transportdogma eingeordnet;
- öffentliche Request-/Response-/Message-Repräsentationen bewusst von internen Datenbank-, Klassen- und Frameworkmodellen getrennt;
- Schema- und Feldsemantik einschließlich required/optional, nullable/absent, Defaults, Enums und Fehlerverträgen;
- HTTP API Design mit bewusster Method-/Statussemantik, Collections, Pagination, Filtering, Ordering, Idempotenz, Retry und Concurrency;
- GraphQL-Schemaevolution und Deprecation als eigene Fachregel ohne unnötigen Format-Skill;
- RPC-/IDL-/Protobuf-Regeln für Field Numbers, Reserved Fields, generierten Code und die Trennung von Source- und Wire-Kompatibilität;
- Event-/Async-Verträge mit Producer/Consumer, Envelope/Payload, Delivery, Ordering, Duplicate-Verhalten, Replay, Dead Letter, Correlation und Schemaevolution;
- Webhooks und Callbacks als HTTP-basierte asynchrone Contracts eingeordnet; provider-spezifische Signatur-/Replay-Security bleibt lokal beziehungsweise in `Sicherheit/`;
- Auth-, Scope- und Tenant-Grenzen als beobachtbare Contract-Semantik;
- providerneutrales Compatibility-Modell aus Source-, Wire- und semantischer Kompatibilität plus realen Consumer-/Deploymentbedingungen;
- Change-Verdicts `COMPATIBLE`, `ROLLOUT-SENSITIVE`, `BREAKING` und `UNVERIFIED`;
- additive Syntax ausdrücklich nicht mit bewiesener semantischer Rückwärtskompatibilität gleichgesetzt;
- Versionierung, Deprecation, Migration, Sunset und Removal-Gates ohne universelle `/v1`-, SemVer- oder Supportfenster-Pflicht;
- Contract-First und maschinenlesbare Artefakte wie OpenAPI, GraphQL SDL, Protobuf/IDL und AsyncAPI mit eindeutiger lokaler Source of Truth;
- Skills `interface-design`, `http-api-design`, `event-contract-design`, `contract-change-review` und `interface-review`;
- alle fünf Skills starten `experimental` mit `partial` Evalabdeckung;
- Evalpacks für alle fünf Skills mit Architecture-/Framework-Near-Misses, DB-Leaks, Versionierungsdogma, Async-Delivery, Additive-vs.-Semantic-Compatibility, Source-/Wire-Trennung, rollout-sensitive Changes und fehlenden Baselines;
- vorhandenen Testing-Skill `contract-testing` mit `contract-change-review` und `interface-review` verbunden, ohne Design und Verifikation zusammenzulegen;
- Workflow `Workflows/Schnittstellenvertrag-Entwerfen-und-Aendern.md`;
- menschliches `Dokumentation/Skill-Handbuch-Schnittstellen-und-Vertraege.md`;
- Quellenbasis aus OpenAPI, HTTP RFCs, Google AIPs, GraphQL, Protobuf/gRPC, AsyncAPI, CloudEvents und aktuellen API-/Event-Agent-Skills;
- aktive Upstreams aus OpenAPI, Google AIPs, GraphQL, Protobuf und AsyncAPI semantisch sowie drei tatsächlich einflussreiche API-/Event-Skills per Blob-SHA registriert.

### Wissensmanagement / Knowledge Bases

Neuer toolneutraler Hauptbereich für persistente Wissensbasen und Knowledge Management:

- klare Trennung zwischen Recherche, Persistent Knowledge, Context Engineering, Dokumentation und technischer Retrieval-/RAG-Implementierung;
- Wissensmodell aus Raw Source, Derived Knowledge Unit, Synthese und Navigation;
- Capture, Ingest und Triage mit `search before create` und Update-vs.-Create statt Append-only-Wachstum;
- Provenance, Evidence und Source-of-Truth-Bezug mit Rückführbarkeit von Synthesen auf Eingabeeinheiten und Quellen;
- Wissensgranularität als eigenständig verwertbare Einheit statt maximaler Fragmentierung;
- Links, Relationen, Taxonomien, kontrolliertes Vokabular und Navigation ohne toolabhängige Pflichtmechanismen;
- Synthesen und Maps of Content mit sichtbaren Eingaben, Gegenbelegen und Unsicherheit;
- Widerspruchsbehandlung mit Trennung von Zeit-, Scope- und Definitionsunterschieden;
- Aktualität, Staleness und Lifecycle mit risikobasiertem Review statt universeller Prüffrist;
- Retrieval und Findability mit expliziter Regel `Retrievalscore ≠ Wahrheit` und `No-Hit ≠ sichere Abwesenheit`;
- Content Health für Dubletten, Orphans, kaputte Links, fehlende Provenance und Taxonomie-/Schema-Drift;
- Datenschutz und sensitives Wissen mit stärkerer Persistenzprüfung als bei kurzfristigem Kontext; Secrets gehören nicht als normale Wissenseinheiten in die Knowledge Base;
- Obsidian, Notion, Vector Stores, RAG und Knowledge Graphs als mögliche Adapter eingeordnet statt zu zentralen Standards erklärt;
- Skills `knowledge-base-design`, `knowledge-ingest`, `knowledge-distill`, `knowledge-synthesis`, `knowledge-maintenance`, `knowledge-query` und `knowledge-base-review`;
- alle sieben Skills starten `experimental` mit `partial` Evalabdeckung;
- Evalpacks für alle sieben Skills mit Tool-Bias-, Search-before-Create-, Provenance-, Bulk-Gate-, Distillation-, Synthesis-, Duplicate-/Orphan-, Query- und Review-Coverage-Fällen;
- Workflow `Workflows/Wissensbasis-Aufbauen-und-Pflegen.md` einschließlich Research-to-Knowledge- und Context-Übergang;
- menschliches `Dokumentation/Skill-Handbuch-Wissensmanagement.md`;
- Quellenbasis aus KCS, W3C PROV, ISO 30401, offiziellen Obsidian-/Notion-Mechanismen, OpenAI Retrieval sowie aktuellen Knowledge-Base-Skills;
- aktive Upstreams: KCS und OpenAI Knowledge Retrieval semantisch sowie `Ar9av/obsidian-wiki`, `obsidian-second-brain` und `knowledge-distill` per Blob-SHA.

### Context, Token-Effizienz und Long-Horizon-Agentenarbeit

`Agentenarbeit/` um die technische Betriebsseite von Context Engineering erweitert:

- Context Budget und Token-Effizienz als Optimierung von Informationswert, Qualität, Latenz und Kosten statt bloßer Token-Minimierung;
- providerneutrale Messsignale für Input-/Output-Tokens, Cache-Nutzung, Kontext- und Tool-Output-Größen, soweit die jeweilige Runtime diese tatsächlich liefert;
- Context Rot, Duplikate, Altstände, Widersprüche und Signalqualität als eigene Prüfachse;
- Context Compaction mit Fortsetzungsfähigkeit und Erhalt harter Constraints, Entscheidungen, Evidence, Sources of Truth und Gates als Qualitätskriterium;
- Long-Horizon-Handoffs für neue Sessions oder Agenten mit eigenständig verständlichem Fortsetzungszustand;
- Tool-Output-Offloading: deterministische Filterung, Aggregation oder Reduktion großer Rohresultate außerhalb des Modellkontexts, wenn dadurch kein benötigtes Signal verloren geht;
- providerneutrale Regeln für Prompt Caching und stabile Kontextpräfixe, ohne konkrete Cache-Semantik oder Modellgrenzen zentral festzuschreiben;
- klare Trennung `Active Context → Working State → Persistent Knowledge`; dauerhafte Wissensbasen werden nicht mit taskbezogenem Agentenzustand vermischt;
- vorhandenen Skill `context-engineering` geschärft und mit `partial` Evalabdeckung versehen;
- neue Skills `context-audit`, `context-compaction` und `session-handoff`, zunächst `experimental` mit `partial` Evalabdeckung;
- Evalpacks für alle vier Context-Skills mit Near-Miss-, Messfähigkeits-, Informationsverlust-, Handoff- und Knowledge-Base-Grenzfällen;
- Workflow `Workflows/Long-Horizon-Agentenarbeit.md`;
- menschliches `Dokumentation/Skill-Handbuch-Context-und-Long-Horizon.md`;
- Trace-Datenmodell und `trace-event.schema.yml` um optionale, metadata-first Context-/Usage-Signale und Compaction-/Handoff-Ereignisse erweitert;
- aktive Context-Upstreams aus Anthropic, OpenAI, LangChain und OpenTelemetry sowie die konkret verwendeten Skills `context-doctor` und OpenClaw `handoff` im zentralen Monitoring registriert;
- keine festen universellen Tokenquoten, Fenstergrenzen, Cachewerte oder Modellpreise als zentrale Wahrheit übernommen.

### Testing und QA

Neuer technologie- und frameworkneutraler Hauptbereich für Softwaretesting und Qualitätsevidence:

- risikobasierte Teststrategie statt pauschaler Testmengen oder Coverage-Ziele;
- Testebenen als Portfolio mit der kleinsten belastbaren Ebene für das jeweilige Risiko;
- Testdesign über Äquivalenzklassen, Grenzwerte, Entscheidungstabellen, Zustandsübergänge, kombinatorische Auswahl und Property-based Testing;
- klare Regeln für Test-Seams, Test Doubles und reale Dependencies ohne universelle Mocking-Doktrin;
- Testdaten, Isolation, Hermetik, Zeit-/Randomness-Kontrolle und Parallelisierung;
- Integration Testing und Contract Testing als getrennte Prüfachsen;
- End-to-End-Tests auf ausgewählte kritische Nutzer-/Geschäftsflows begrenzt;
- Flaky Tests als Defekt am Qualitätssignal; Retry ist Diagnose-/Mitigationswerkzeug und kein Root-Cause-Fix;
- kontrollierte Failure-/Recovery-Tests für Timeout, Teilfehler, Retry, Idempotenz und Recovery;
- klare Grenze zu späterem Reliability-/Chaos-Engineering;
- Coverage als Ausführungssignal, Mutation/Brechprobe als mögliche Wirksamkeitsprüfung;
- exploratives Testen mit Charter, Mission, Scope und Zeitbox;
- Release-Evidence mit `PASS`, `FAIL`, `BLOCKED`, `NOT RUN` und sichtbarer Restunsicherheit; Releaseentscheidung bleibt beim lokalen Gate;
- `verification-loop` um die Pflicht zu frischer, zum Completion Claim passender Evidence geschärft statt einen redundanten `verification-before-completion`-Skill anzulegen;
- Skills `test-strategy`, `test-design`, `integration-testing`, `contract-testing`, `e2e-testing`, `flaky-test-diagnosis`, `failure-testing`, `exploratory-testing` und `test-suite-review`;
- alle neun Skills zunächst `experimental` mit `partial` Evalabdeckung;
- Evalpacks für alle neun Skills mit positiven, Near-Miss-, Drift-, Flakiness-, Production-Safety- und Release-Gate-Fällen;
- Workflow `Workflows/Teststrategie-und-QA.md`;
- Quellenbasis aus ISTQB, Playwright, Pact, Testcontainers, Hypothesis, Stryker, Testing Library, Fowler, Google Testing Blog sowie aktuellen Testing-Agent-Skills von Anthropic, Currents und Superpowers.

### Datenbanken

Neuer engine-neutraler Hauptbereich für Datenbankarbeit:

- Datenmodellierung anhand von Domäne, Invarianten und realen Zugriffsmustern;
- reales Schema und verwendete Engine-/Driver-/ORM-Version als Source of Truth statt plausibler Annahmen;
- Schema-, Constraint- und Integritätsregeln;
- Query-Korrektheit, Parametrisierung, Tenant-/Scope-Sicherheit und Write-Wirkung;
- messungsbasierte Query-Performance mit bestehenden Indizes und Execution-Plan-Evidence;
- Transaktionen, Isolation, Locking, Race Conditions, Idempotenz und Retry;
- Migrationen, Backfills, Expand–Migrate–Contract, Rollback und Forward Fix;
- Connections, Pooling, Timeouts und Ressourcen als systemweite Kapazitätsfrage;
- Least Privilege und getrennte Diagnose-/Write-/Adminrechte;
- Backup, Restore und Recovery mit getestetem Restore statt bloß grünem Backup-Job;
- Monitoring und Ursachen-Diagnose;
- klare Scope-Grenze: Zustand innerhalb eines operativen Datenspeichers gehört zu `Datenbanken/`, systemübergreifende ETL-/ELT-/CDC-Pipelines zu einem späteren `Data Engineering/`;
- Risikoklassen `READ`, `WRITE`, `MIGRATION` und `DESTRUCTIVE / RECOVERY` mit steigenden Evidence- und Human-Gate-Anforderungen;
- Skills `database-design`, `database-query-review`, `query-performance`, `schema-migration`, `transaction-review`, `database-operations` und `database-review`;
- alle sieben Skills zunächst `experimental` mit `partial` Evalabdeckung;
- Evalpacks mit positiven, Near-Miss- und Safety-/Gate-Fällen;
- Workflow `Workflows/Datenbank-Aenderung.md`;
- Quellenbasis aus Supabase/Postgres, Neon, MongoDB, Redis, Prisma und lebender Primärdokumentation, ohne deren enginespezifische Regeln zu universalisieren.

### Skill Engineering

Neuer Meta-Bereich für Entwurf und Pflege von Agent-Skills:

- klare Skill-Schnitte und Verantwortungen;
- Progressive Disclosure mit kompaktem `SKILL.md` und optionalen `references/`, `scripts/` und `assets/`;
- Trigger- und Description-Design mit Near-Miss-Negativfällen;
- Input-/Output-/Evidence-Verträge;
- Capability Detection, Least-Privilege-nahe Anforderungen und ehrliche Fallbacks;
- Skill-Komposition ohne versteckte Mega-Orchestrierung;
- Review- und Evalregeln;
- Lifecycle `experimental → candidate → stable → deprecated → retired`;
- Skills `skill-authoring` und `skill-review`;
- Agent Skills Specification als externe Formatgrundlage eingeordnet.

### Skill-Katalog und Maturity

Neu beziehungsweise erweitert:

- `skill-catalog.yml` als maschinenlesbares Skill-Inventar;
- expliziter Maturity-Status je Skill;
- Evalabdeckung `none`, `partial`, `core`, `broad`;
- Capability- und Related-Hinweise für relevante Skills;
- `Dokumentation/Skill-Katalog.md` als menschliche Erläuterung;
- konservative Einstufung: neue Bereiche zunächst `experimental`, ältere praktisch genutzte Skills überwiegend `candidate`; `stable` wird nicht automatisch vergeben;
- Datenbank- und Testing-und-QA-Skills als `experimental` mit `partial` Evalabdeckung;
- `context-engineering` bleibt `candidate` und erhält `partial` Evalabdeckung;
- `context-audit`, `context-compaction` und `session-handoff` als `experimental` mit `partial` Evalabdeckung;
- sieben Wissensmanagement-Skills als `experimental` mit `partial` Evalabdeckung ergänzt;
- fünf Schnittstellen-/Contract-Skills als `experimental` mit `partial` Evalabdeckung ergänzt;
- sieben Infrastruktur-/DevOps-Skills als `experimental` mit `partial` Evalabdeckung ergänzt;
- Gesamtbestand auf 87 zentrale Skills erweitert.

### Evals

Bereich `Evals/` erweitert:

- gemeinsames Evalfall-Schema;
- Trigger-, Behavior-, Outcome- und Regressionsevals;
- Near-Miss-Negative als eigener Qualitätsbestandteil;
- erste Evalpacks für `deep-research`, `docs-review`, `frontend-design`, `diagnose`, `code-review` und `skill-authoring`;
- zusätzliche Evalpacks für alle sieben Datenbank-Skills mit Schema-Source-of-Truth-, Query-Safety-, `EXPLAIN ANALYZE`-, Migration-, Concurrency-, Restore- und Review-Gate-Fällen;
- zusätzliche Evalpacks für alle neun Testing-und-QA-Skills, unter anderem zu fehlendem Oracle, Mock-/Contract-Drift, E2E-Near-Misses, Flakiness trotz Retry, Failure Testing vs. Chaos Engineering und Testsignal-Review;
- zusätzliche Evalpacks für `context-engineering`, `context-audit`, `context-compaction` und `session-handoff`, unter anderem zu fehlender Tokenmessung, Context Bloat, Compaction-Verlust, erfundenen Freigaben und Persistent-Knowledge-Near-Misses;
- zusätzliche Evalpacks für alle sieben Wissensmanagement-Skills, unter anderem zu Tool-Bias, Search-before-Create, Provenance, sensibler Persistenz, Bulk-Gates, Distillation, Synthese-Evidence, Duplicate-/Orphan-Entscheidungen, Retrieval und Review-Coverage;
- zusätzliche Evalpacks für alle fünf Schnittstellen-/Contract-Skills, unter anderem zu Transportdogma, Framework-Near-Misses, Datenbankmodell-Leaks, unbekannten Enum-Werten, Source-/Wire-Trennung, rollout-sensitive Changes und fehlenden Baselines;
- zusätzliche Evalpacks für alle sieben Infrastruktur-/DevOps-Skills, unter anderem zu Drift, State-Sensitivität, stale Previews, destructive Replacements, CI-Secret-Grenzen, Container-Runtime-Verträgen, Rollback-Grenzen und GitOps-Reconciliation;
- Skill-Katalog für diese Skills auf `eval_coverage: partial` aktualisiert.

### Sicherheit

Neuer Hauptbereich für agentische und Skill-Sicherheit:

- Prompt Injection und untrusted Input;
- Toolrechte und Least Privilege;
- Secrets und Datenexfiltration;
- Skill Supply Chain, Provenance, Pinning und Update Drift;
- MCP und externe Tools;
- Sandbox und Isolation;
- externe Aktionen und Bestätigung;
- Logging, Datenschutz und Telemetrie;
- Security Review für Skills;
- Skills `skill-security-review`, `prompt-injection-review` und `tool-permission-review`;
- OWASP Agentic Skills Top 10 und Agentic Applications Top 10 als Sicherheitsreferenzen eingeordnet.

### Workflows / Recipes

Bereich zur bewussten Skill-Komposition mit Recipes für:

- Deep Research;
- technische Dokumentation;
- Website-Neuentwicklung;
- Review bestehender Websites;
- Software Feature;
- Bugdiagnose;
- Bildserie;
- Datenbankänderung;
- Teststrategie und QA;
- Long-Horizon-Agentenarbeit;
- Aufbau und Pflege persistenter Wissensbasen;
- Entwurf und Änderung von Schnittstellenverträgen;
- kontrollierte Infrastrukturänderungen;
- Build, Deploy und Promotion.

Grundregel: Skills bleiben begrenzte Disziplinen; wiederkehrende Skill-Ketten werden als Workflow statt als Mega-Skill modelliert.

### Observability und Traceability

Erweitert:

- `Agentenarbeit/Trace-Datenmodell.md` für Task → Run → Skill/Workflow → Tool/Event → Evidence → Gate → Artefakt → Outcome;
- `Agentenarbeit/trace-event.schema.yml` als toolneutrale maschinenlesbare Ereignisstruktur;
- optionale Context-/Usage-Metadaten für Input-/Output-Tokens, Cache-Signale, Context- und Tool-Output-Größen sowie Compaction-/Handoff-Ereignisse ergänzt;
- Inhaltslogging bleibt optional und datenschutzsensibel; Metadaten sind vom vollständigen Prompt-/Toolinhalt getrennt.

### Dokumentationserstellung

Neuer Hauptbereich für technische und projektbezogene Dokumentation:

- Zielgruppe, Leserzustand und Dokumentzweck vor dem Schreiben klären;
- Dokumentationsmodus nach Tutorial, How-to, Reference und Explanation unterscheiden;
- Artefakttypen wie README, ADR und Runbook getrennt vom Diátaxis-Modus behandeln;
- Source-of-Truth- und Fachkorrektheitsregeln gegen plausible, aber erfundene Dokumentation;
- technischer Schreibstil mit stabiler Terminologie, Scanbarkeit und Accessibility;
- Beispiele, Befehle, Links und Parameter als verifizierbare Bestandteile behandeln;
- Navigation und Informationsarchitektur;
- Docs as Code, Ownership, Wartung und automatisierbare Checks;
- Dokumentationsreview mit Drift-Typen und Schweregraden;
- Vorlagen für README, ADR, Runbook, How-to und Tutorial;
- Skills `docs-plan`, `technical-writing`, `readme`, `tutorial`, `how-to`, `reference-docs`, `explanation-docs`, `adr`, `runbook` und `docs-review`.

### Quellen- und Upstream-Monitoring

Erweitert und vollständig auditiert:

- `Dokumentation/Quellenregister.md` auf Monitoring-Schema v2 erweitert;
- `Dokumentation/upstream-sources.yml` unterscheidet `exact-sha` für konkrete GitHub-Dateien und `semantic-review` für lebende Web-/Produktdokumentation;
- monatliche und quartalsweise Cadence für unterschiedlich volatile Quellen;
- vollständiger bereichsübergreifender Audit in `Dokumentation/Upstream-Audit-2026-08-23.md` dokumentiert;
- mutable Upstreams aus Programmieren, Schreiben, Bildarbeit, Webentwicklung, Recherche, Dokumentationserstellung und relevanten Grundlagen klassifiziert;
- `Schreiben/Quellen-und-Inspirationen.md` und `Programmieren/Quellen-und-Inspirationen.md` ergänzt;
- konkrete Matt-Pocock-Engineering-Skills für TDD, Diagnose, Code-Review und Domain Modeling per Blob-SHA registriert;
- lebende Adobe-/Midjourney-Bilddokumentation semantisch registriert;
- weitere tatsächlich verwendete Web- und Research-Skills mit geprüftem Blob-SHA ergänzt;
- langsamere Leitfäden wie HAX, Google Developer Style Guide, Write the Docs und Good Docs Project quartalsweise eingeordnet;
- Datenbank-Upstreams aus Supabase, Neon, MongoDB, Redis und Prisma sowie lebende Postgres-/Migration-Dokumentation in die Quellenpflege aufgenommen;
- Testing-und-QA-Upstreams aus Anthropic, Currents und Superpowers per Blob-SHA sowie ISTQB, Playwright, Pact und Testcontainers semantisch registriert;
- Context-/Long-Horizon-Upstreams aus Anthropic, OpenAI, LangChain und OpenTelemetry semantisch sowie `context-doctor` und OpenClaw `handoff` per Blob-SHA registriert;
- Wissensmanagement-Upstreams aus KCS und OpenAI Retrieval semantisch sowie `obsidian-wiki`, `obsidian-second-brain` und `knowledge-distill` per Blob-SHA registriert;
- Schnittstellen-/Contract-Upstreams aus OpenAPI, Google AIPs, GraphQL, Protobuf und AsyncAPI semantisch sowie drei konkret verwendete API-/Event-Skills per Blob-SHA registriert;
- Infrastruktur-/DevOps-Upstreams aus Terraform, OpenTofu, Kubernetes, OpenGitOps, Argo Rollouts, OPA, SLSA und Docker Build semantisch sowie HashiCorp-, Flux- und ausgewählte IaC/CI/Container/Deployment-Skills per Blob-SHA registriert;
- stabile HTTP-/Problem-Details-/Deprecation-RFCs und weitere formatbezogene Referenzen bewusst in der Fachquellendatei statt als künstliche schnelle Sync-Dependencies geführt;
- W3C PROV, ISO 30401 und toolbezogene Hilfedokumentation als stabile Fachreferenzen im Bereich dokumentiert statt künstlich als schnelle mutable Dependencies zu behandeln;
- Papers, datierte Research-Artikel und reine Discovery-Kataloge bewusst nicht als künstliche Sync-Dependencies behandelt;
- Grundregel bleibt: Upstream-Änderung ist Review-Signal, kein automatischer Sync;
- monatlicher `KI-Regeln Monatscheck` auf das Monitoring-Schema und Infrastruktur/DevOps als eigenes Fachfeld erweitert.

### Recherche

Neuer Hauptbereich für KI-gestützte Websuche und Deep Research:

- fünf Research-Modi von Lookup bis Literature Research;
- Rechercheplanung mit Teilfragen, Perspektiven und Coverage-Kriterien;
- claimbezogene Quellenstrategie mit Primärquellen-, Aktualitäts- und Unabhängigkeitsprüfung;
- Suchtreffer und Snippets ausdrücklich nur als Leads, nicht als Evidenz;
- Claim-Evidence-Ledger und Zitationshygiene;
- Triangulation, Widerspruchsanalyse und qualitative Confidence;
- Coverage Loop statt bloßer Quellenzählung;
- Synthese nach Erkenntnis statt nach Quellenliste;
- Web-Sicherheitsregeln gegen Prompt Injection und unerlaubte Aktionseskalation;
- Quellen- und Inspirationssammlung zu OpenAI Deep Research, Firecrawl, PracticalSwan, Hermes, STORM, LangChain DeepAgents, Microsoft Research Skills und weiteren öffentlichen Research-Skills;
- Skills `web-search`, `research-plan`, `deep-research`, `source-evaluation`, `claim-verification`, `research-synthesis` und `citation-audit`.

### Webentwicklung

Neuer Hauptbereich für Gestaltung und Entwicklung von Websites und Weboberflächen:

- Designrichtung und visuelle Identität vor Umsetzung;
- Informationsarchitektur und Greyboxing als eigene Phase;
- Typografie-, Farb-, Spacing- und Rhythmusregeln;
- Content- und Anti-Slop-Regeln gegen generische KI-Webtexte und Fake-Belege;
- responsive Gestaltung und Interaktionszustände;
- unabhängiger Webdesign-Review;
- Komponentenarchitektur mit Komposition vor Konfigurationsexplosion;
- Accessibility als Qualitätsgate;
- messungsbasierte Frontend-Performance;
- responsive Implementierung;
- Render- und Browser-Verifikation;
- Quellen- und Inspirationssammlung zu Anthropic `frontend-design`, Impeccable, Vercel Agent Skills und weiteren öffentlichen Skill-Sammlungen;
- Skills `frontend-design`, `design-system`, `greybox`, `web-content`, `web-design-review`, `accessibility-review`, `frontend-performance` und `visual-verification`.

### Dokumentation

Aktualisiert:

- Haupt-README um `Webentwicklung/`, `Recherche/`, `Wissensmanagement/`, `Schnittstellen-und-Vertraege/`, `Infrastruktur-und-DevOps/`, `Dokumentationserstellung/`, `Skill-Engineering/`, `Sicherheit/`, `Evals/`, `Workflows/`, `Datenbanken/` und `Testing-und-QA/` erweitert und um Context-/Long-Horizon-Agentenarbeit geschärft;
- menschliche Doku um Quellenregister, vollständigen Upstream-Audit, Skill-Katalog und zusätzliche Skill-Handbücher einschließlich `Skill-Handbuch-Context-und-Long-Horizon.md`, `Skill-Handbuch-Wissensmanagement.md`, `Skill-Handbuch-Schnittstellen-und-Vertraege.md` und `Skill-Handbuch-Infrastruktur-und-DevOps.md` ergänzt;
- Projektmanifest und Nutzungsanleitung um Research-, Wissensmanagement-, Schnittstellen-/Contract-, Infrastruktur-/DevOps-, Web-, Dokumentations-, Datenbank-, Testing-/QA- und Long-Horizon-Arbeit ergänzt.

## v2026.08

### Grundlagen

Hinzugefügt beziehungsweise zentralisiert:

- allgemeine Zusammenarbeit mit KI;
- Datenschutz und Kontext;
- Mensch-KI-Interaktion;
- kalibriertes Vertrauen und Denkautonomie;
- Quellen und Inspirationen für Human-AI-Interaction und Selbstentwicklung.

### Arbeitsweisen

Hinzugefügt:

- systematische Problemlösung;
- Reflexion und Selbstverbesserung als Lernloop;
- Zielarbeit und Umsetzung;
- Skills `reflektierender-dialog`, `entscheidungsunterstuetzung` und `ziel-reflexions-loop`.

### Agentenarbeit

Hinzugefügt:

- Context Engineering;
- Harness Engineering;
- Task Graphs und kontrollierte Loops;
- Delegation Contracts und Evidence Bundles;
- Agent Evals;
- Observability und Traceability;
- Human Gates;
- Entropie- und Driftmanagement;
- Skills `context-engineering`, `task-graph`, `verification-loop`, `delegation-contract` und `agent-eval`.

### Schreiben

Hinzugefügt beziehungsweise generalisiert:

- natürlicher Schreibstil;
- kreatives Schreiben;
- strukturelles Stilreview;
- Schutz einfacher Verben vor künstlicher Aufblähung;
- KI-typische Muster als Warnsignal statt Wort-Blacklist;
- Trennung von Meta-Kommunikation und Endprodukt;
- Skills `natuerliches-schreiben`, `kreatives-schreiben` und `stilreview`.

### Bildarbeit

Neuer Hauptbereich für konsistente Einzelbilder und Bildserien:

- Quellen- und Prioritätenlogik;
- getrennte Betrachtung von Identitäts-, Stil-, Struktur- und Kontinuitätskonsistenz;
- Entitätsbibeln;
- Szenenplanung und Bild-Pre-Briefs;
- Zustandsmatrizen;
- Bildreview und Freigabestufen;
- Serien- und Abschlussaudit;
- Skills `bild-prebrief`, `entitaetsbibel`, `serien-kontinuitaetscheck` und `bildreview`.

### Programmieren

Hinzugefügt beziehungsweise generalisiert:

- Fünf-Gate-Entwicklungsprozess;
- Agentenanweisungen für Softwarearbeit;
- Skills `domain-modeling`, `tdd`, `diagnose` und `code-review`.

### Dokumentation und Governance

Hinzugefügt:

- menschlich lesbare Nutzungsanleitung;
- Skill-Handbuch;
- definierter monatlicher Radar-Check;
- vierteljährlicher Repo-Audit;
- datumsbasierte Versionierung;
- Projektmanifest-Vorlage;
- Changelog als nachvollziehbare Änderungshistorie.

## Pflegehinweis

Rein redaktionelle Änderungen müssen nicht zwingend einen neuen Versionsstand erzeugen. Änderungen, die Verhalten, Prioritäten oder empfohlene Nutzung von Regeln und Skills beeinflussen, sollen dagegen im Changelog sichtbar werden.