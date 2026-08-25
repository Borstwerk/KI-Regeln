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
- alle sieben Skills aus `Software-Architecture-und-System-Design/`;
- alle acht Skills aus `Requirements-und-Spezifikations-Engineering/`.

Die Testing-und-QA-Fälle prüfen unter anderem risikobasierte Strategie, reale Dependencies, Contract-Drift, E2E-Near-Misses, Flakiness, Failure Testing und Testsignal-Qualität.

Die Context-Fälle prüfen unter anderem Sources of Truth, Working State vs. Persistent Knowledge, Context Audit ohne erfundene Tokenmetriken, Compaction-Fidelity und standalone Handoffs.

Die Wissensmanagement-Fälle prüfen unter anderem toolneutrales Design, Search-before-Create, Provenance, Synthesis, Dubletten/Orphans, Retrieval und Content Health.

Die Schnittstellen-Fälle prüfen unter anderem Transportdogma, DB-Leaks in API-Schemas, Additive-vs.-Semantic-Compatibility, Source-/Wire-Trennung, rollout-sensitive Changes und fehlende Contract-Baselines.

Die Infrastruktur-/DevOps-Fälle prüfen unter anderem State-/Drift-Grenzen, stale Previews, destructive Changes, Pipeline-Secret-Grenzen, Container Runtime Contracts, Deployment-/Rollback-Annahmen und GitOps-Reconciliation-Gates.

Die Reliability-/System-Observability-Fälle prüfen unter anderem SLO-vs.-RTO/RPO-Grenzen, Observability ohne Tooldogma, Alert-Actionability, Incident-Gates, Postmortem-Evidence, Capacity-vs.-Load-Testing und sichere Resilience-Experimente.

Für jeden der acht Reliability-Skills sind sechs Startfälle definiert, insgesamt 48. Der erste Same-Model-Smoke-Lauf wurde am 2026-08-24 gegen den damaligen gepinnten `main`-Stand ausgeführt; das ersetzt keinen unabhängigen verblindeten Benchmark und hebt den Reifegrad nicht automatisch an.

Die Data-Engineering-Fälle prüfen unter anderem Source of Truth/Grain, CDC/Replay, Backfill-Semantik, Data Quality/Freshness, Contracts, Lineage und produktive Datenänderungs-Gates.

Für jeden der neun Data-Engineering-Skills sind sechs Startfälle definiert, insgesamt 54. Diese 54 Fälle sind **definiert, aber noch nicht ausgeführt oder bestanden**.

Die Software-Architecture-/System-Design-Fälle prüfen unter anderem Architecture Baseline, ADR-/Code-Konflikte, Microservice-/Teamgrößen-/Shared-DB-Dogmen, fehlende Quality-/Capacity-Evidence, künstliche Kandidaten, Big-Bang-Migrationen, Conformance und Ausführungsgates.

Für jeden der sieben Architecture-Skills sind sechs Startfälle definiert, insgesamt 42. Der erste Same-Model-Smoke-Lauf wurde am 2026-08-25 gegen den gepinnten Stand `78abce4ade2e1d92dfc47f6169dcd2551d8d0f09` ausgeführt. Alle 42 Fälle entsprachen ihrem erwarteten Verhalten und Status: 30× `pass`, 6× `partial`, 6× `blocked`; es wurden keine verbotenen Verhaltensweisen beobachtet. Das ist **kein unabhängiger verblindeter Benchmark**, rechtfertigt keine Maturity-Hochstufung und ist im Laufartefakt `Software-Architecture-und-System-Design/Same-Model-Smoke-2026-08-25.md` dokumentiert.

Die Requirements-/Specification-Fälle prüfen unter anderem:

- aktuelle Soll-Baseline statt `neueste Datei = Wahrheit`;
- Implementierung als Evidence, aber nicht automatisch als gewünschtes Requirement;
- Elicitation ohne Fragebogenritual oder Clarity-Score-Dogma;
- User Stories, EARS und Given/When/Then als optionale Formen statt Pflichtsyntax;
- fehlende Performance-, Retention- oder Reliability-Zielwerte ohne Erfindung lokaler Wahrheit;
- Acceptance Criteria getrennt von konkreten Testfällen und Testausführung;
- Traceability Coverage ohne `100 % Links = korrekt`-Fehlschluss;
- semantische Requirement Changes statt bloßer Textdiff-Bewertung;
- Requirements Validation getrennt von Product Validation und Stakeholder Approval;
- unabhängigen Requirements Review ohne ungefragte Umschreibung oder Downstream-Ausführung.

Für jeden der acht Requirements-Skills sind sechs Startfälle definiert, insgesamt 48. Diese 48 Fälle sind **definiert, aber noch nicht ausgeführt oder bestanden**.

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
