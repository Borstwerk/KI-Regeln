# Changelog

Dieses Dokument hält relevante Änderungen am Repository fest.

Die Versionierung ist datumsbasiert. Eine Version beschreibt einen bewusst nutzbaren Stand des zentralen Regelwerks.

## Unreleased

Noch nicht als eigener Versionsstand veröffentlichte Änderungen werden zunächst hier gesammelt.

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
- Gesamtbestand auf 75 zentrale Skills erweitert.

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
- Aufbau und Pflege persistenter Wissensbasen.

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
- W3C PROV, ISO 30401 und toolbezogene Hilfedokumentation als stabile Fachreferenzen im Bereich dokumentiert statt künstlich als schnelle mutable Dependencies zu behandeln;
- Papers, datierte Research-Artikel und reine Discovery-Kataloge bewusst nicht als künstliche Sync-Dependencies behandelt;
- Grundregel bleibt: Upstream-Änderung ist Review-Signal, kein automatischer Sync;
- monatlicher `KI-Regeln Monatscheck` auf das Monitoring-Schema und die neuen Discovery-Felder erweitert.

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

- Haupt-README um `Webentwicklung/`, `Recherche/`, `Wissensmanagement/`, `Dokumentationserstellung/`, `Skill-Engineering/`, `Sicherheit/`, `Evals/`, `Workflows/`, `Datenbanken/` und `Testing-und-QA/` erweitert und um Context-/Long-Horizon-Agentenarbeit geschärft;
- menschliche Doku um Quellenregister, vollständigen Upstream-Audit, Skill-Katalog und zusätzliche Skill-Handbücher einschließlich `Skill-Handbuch-Context-und-Long-Horizon.md` und `Skill-Handbuch-Wissensmanagement.md` ergänzt;
- Projektmanifest und Nutzungsanleitung um Research-, Wissensmanagement-, Web-, Dokumentations-, Datenbank-, Testing-/QA- und Long-Horizon-Arbeit ergänzt.

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
