# Evals

Dieser Bereich enthält wiederholbare Testfälle für zentrale Skills.

## Ziel

> Skillqualität wird an beobachtbarem Verhalten geprüft, nicht nur an plausiblen Anweisungen.

Evals sollen insbesondere Regressionen erkennen bei:

- Triggerung und Nichttriggerung;
- Scope-Treue;
- Tool- und Capability-Verhalten;
- Evidence- und Quellenhygiene;
- Stop-/Eskalationsgates;
- Outputqualität;
- Sicherheitsgrenzen.

## Eval-Klassen

### Trigger

Prüft, ob ein Skill bei passenden Aufgaben gewählt wird und bei Near-Misses nicht.

### Behavior

Prüft den Arbeitsprozess, z. B.:

- öffnet Quellen statt nur Snippets zu verwenden;
- reproduziert einen Bug vor Hypothesenbildung;
- schreibt bei Review nicht ungefragt um;
- behauptet keine Capability, die nicht verfügbar ist.

### Outcome

Prüft das Ergebnis gegen konkrete Akzeptanzkriterien.

### Regression

Vergleicht bekannte Skillstände oder Verhalten vor/nach einer Änderung.

## Verzeichnisstruktur

```text
Evals/
├── README.md
├── eval-case.schema.yml
└── <Bereich>/
    └── <skill-id>/
        └── cases.yml
```

## Aktuelle größere Evalpacks

Neben einzelnen Kernskills bestehen inzwischen vollständige Startpacks für:

- alle sieben Skills aus `Datenbanken/`;
- alle neun Skills aus `Testing-und-QA/`;
- die Context-/Long-Horizon-Skills `context-engineering`, `context-audit`, `context-compaction` und `session-handoff`;
- alle sieben Skills aus `Wissensmanagement/`;
- alle fünf Skills aus `Schnittstellen-und-Vertraege/`;
- alle sieben Skills aus `Infrastruktur-und-DevOps/`;
- alle acht Skills aus `Reliability-und-System-Observability/`;
- alle neun Skills aus `Data-Engineering/`;
- alle sieben Skills aus `Software-Architecture-und-System-Design/`.

Die Testing-und-QA-Fälle prüfen unter anderem risikobasierte Strategie, reale Dependencies, Contract-Drift, E2E-Near-Misses, Flakiness, Failure Testing und Testsignal-Qualität.

Die Context-Fälle prüfen unter anderem Sources of Truth, Working State vs. Persistent Knowledge, Context Audit ohne erfundene Tokenmetriken, Compaction-Fidelity und standalone Handoffs.

Die Wissensmanagement-Fälle prüfen unter anderem toolneutrales Design, Search-before-Create, Provenance, Synthesis, Dubletten/Orphans, Retrieval und Content Health.

Die Schnittstellen-Fälle prüfen unter anderem:

- Interface Design ohne Transportdogma oder versteckte Re-Architektur;
- HTTP-Verträge ohne `/v1`- oder Pagination-Dogma;
- Trennung öffentlicher Repräsentation vom Datenbankschema;
- Async Contracts mit Delivery, Ordering, Replay und Idempotenz;
- additive Änderungen, unbekannte Enum-Werte und semantische Compatibility;
- Wire-vs.-Source-Kompatibilität bei Protobuf;
- `ROLLOUT-SENSITIVE`, `BREAKING` und `UNVERIFIED` als explizite Verdicts;
- grüne Contract Tests nicht als vollständige Designfreigabe.

Die Infrastruktur-/DevOps-Fälle prüfen unter anderem:

- Desired State ohne versteckte Re-Architektur oder ungefragtes Apply;
- Drift als Befund statt automatische Rückführung;
- State-/Plan-Artefakte als potenziell sensible Evidence;
- frische Preview statt stale Plan;
- `SAFE_TO_PROCEED_TO_GATE` ausdrücklich nicht als Apply-Autorisierung;
- CI-Orchestrierung ohne Teststrategie-Duplizierung oder Secret-Leaks an untrusted Code;
- Container-Build vs. Runtime-/Security-Grenzen;
- Deployment-Rollback ohne Zeitmaschinenannahme;
- GitOps-Commit-/Merge-Gates bei Continuous Reconciliation;
- Repo-Evidence nicht als Live-Cluster-Health ausgeben.

Die Reliability-/System-Observability-Fälle prüfen unter anderem:

- SLI-Spezifikation vs. Messimplementierung sowie fehlende Businessbasis für SLO-Ziele;
- RTO/RPO als Recovery-Ziele statt SLO-Near-Miss;
- Observability ohne Tool- oder Three-Pillars-Dogma;
- Telemetrie-Coverage, sensible Daten und Runtime-Evidence;
- Alert-Actionability, Low-Traffic-/Threshold-Grenzen und produktive Change-Gates;
- Incident-Mitigation vor vollständiger RCA ohne implizite Restart-/Failover-Autorisierung;
- Postmortems mit widersprüchlicher Evidence und beitragenden Faktoren;
- Capacity Planning vs. Load Testing und fehlende Ceiling-Evidence;
- Failure Testing vs. systemisches Resilience-Experiment;
- Blast Radius, Abort, Recovery und produktive Fault-Injection-Gates;
- Reliability Review ohne versteckte Re-Architecture oder Production Changes.

Für jeden der acht Reliability-Skills sind sechs Startfälle definiert, insgesamt 48. Der erste Same-Model-Smoke-Lauf wurde am 2026-08-24 gegen den damaligen gepinnten `main`-Stand ausgeführt; das ersetzt keinen unabhängigen verblindeten Benchmark und hebt den Reifegrad nicht automatisch an.

Die Data-Engineering-Fälle prüfen unter anderem:

- Source of Truth, Consumer und Grain vor Toolstack;
- DB-/Event-Contract-/Testing-Near-Misses;
- CDC, Deletes, Cursor/Offsets, Replay und Ende-zu-Ende-Processing-Guarantees;
- `updated_at` und Kafka/exactly-once nicht als universelle Garantien;
- Full-vs.-Incremental-Semantik, historische Logik und Backfill-Gates;
- analytisches Grain, Measures, Aggregierbarkeit und Star-Schema-Dogma;
- Data Quality, Freshness-Zeitsemantik und Reconciliation ohne erfundene Thresholds;
- Data Contracts mit struktureller und semantischer Compatibility;
- Design Lineage vs. Runtime Lineage sowie unbekannte Consumer;
- Data Intervals, Retry, Catchup und bounded Reprocessing;
- Data-Engineering-Review ohne Tool-Re-Architecture oder ungefragte produktive Datenänderung.

Für jeden der neun Data-Engineering-Skills sind sechs Startfälle definiert, insgesamt 54. Diese 54 Fälle sind **definiert, aber noch nicht ausgeführt oder bestanden**.

Die Software-Architecture-/System-Design-Fälle prüfen unter anderem:

- Architecture Baseline aus mehreren Evidence-Typen statt Ordner- oder Diagrammgläubigkeit;
- Soll-/Ist-Konflikte zwischen ADR, Code, Config und Runtime-Evidence;
- einfachstes tragfähiges Systemdesign vor verteilten Standardbausteinen;
- fehlende QPS-, SLO-, RTO/RPO- oder andere Zielwerte ohne Erfindung lokaler Wahrheit;
- Teamgröße, Shared Database und Bounded Context nicht als automatische Microservice-Regeln;
- echte Quality-Szenarien und Trade-offs ohne künstliche Kandidaten oder opaque Gesamtscores;
- evolutionäre Migration mit Compatibility und Zwischenzuständen statt Big-Bang-Rewrite;
- Conformance gegen gültige lokale Architektur statt Patternpräferenz;
- Fitness Functions als nachweisbare Guardrails statt bloß konfigurierte Checks;
- Architekturreview ohne Pattern-Purity-Dogma oder implizite Implementierungs-/Deploymentfreigabe.

Für jeden der sieben Architecture-Skills sind sechs Startfälle definiert, insgesamt 42. Diese 42 Fälle sind **definiert, aber noch nicht ausgeführt oder bestanden**.

## Fallstruktur

Jeder Fall beschreibt mindestens:

- `id`;
- `class`;
- `input`;
- `should_trigger`;
- erwartete Verhaltenspunkte;
- verbotene Verhaltenspunkte;
- erwarteten Abschlussstatus.

Nicht jeder Eval muss vollautomatisch sein. Die Struktur soll jedoch so konkret sein, dass zwei Reviewer denselben Fall ähnlich beurteilen können.

## Minimalset für einen Kernskill

Mindestens:

1. typischer positiver Trigger;
2. paraphrasierter positiver Trigger;
3. Near-Miss-Negativfall;
4. fehlende Capability oder Pflichtinformation;
5. schwieriger fachlicher Fall.

## Bewertung

Empfohlene Statuswerte:

- `pass`;
- `partial`;
- `fail`;
- `blocked`.

Ein Skill gilt nicht automatisch als `stable`, nur weil wenige Beispielcases bestehen.

## Pflege

Bei verhaltensändernden Skilländerungen:

```text
betroffene Evals bestimmen
→ alten Stand ausführen / bekannte Baseline betrachten
→ neuen Stand ausführen
→ Regressionen prüfen
→ Skill-Maturity neu bewerten
→ Changelog
```

Bei Context-/Compaction-Evals ist ein besonders starker Outcome-Test die Fortsetzung derselben Aufgabe aus dem kompakten beziehungsweise übergebenen Zustand.

## Leitgedanke

> Ein Eval soll eine konkrete Fehlermöglichkeit sichtbar machen – nicht nur bestätigen, dass der Skill im Happy Path nett aussieht.