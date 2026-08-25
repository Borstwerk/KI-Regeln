# Skill-Katalog und Maturity

## Zweck

`../skill-catalog.yml` ist das maschinenlesbare Inventar der zentralen Skills.

Das menschliche `Skill-Handbuch.md` beantwortet vor allem:

> Welcher Skill hilft mir bei welcher Aufgabe?

Der Skill-Katalog beantwortet zusätzlich:

> Welche Skills existieren, wo liegen sie, wie reif sind sie und welche Fähigkeiten benötigen sie?

## Aktueller Bestand

Der Katalog enthält aktuell 119 zentrale Skills:

- Arbeitsweisen: 3;
- Agentenarbeit: 8;
- Schreiben: 3;
- Bildarbeit: 4;
- Programmieren: 4;
- Webentwicklung: 8;
- Recherche: 7;
- Wissensmanagement: 7;
- Schnittstellen und Verträge: 5;
- Infrastruktur und DevOps: 7;
- Reliability und System-Observability: 8;
- Data Engineering: 9;
- Software Architecture und System Design: 7;
- Requirements und Spezifikations-Engineering: 8;
- Dokumentationserstellung: 10;
- Skill Engineering: 2;
- Sicherheit: 3;
- Datenbanken: 7;
- Testing und QA: 9.

Die Zahl ist kein Qualitätsziel. Neue Skills werden nur aufgenommen, wenn ein eigener belastbarer Schnitt statt bloßer Themenabdeckung entsteht.

## Maturity

```text
experimental
→ candidate
→ stable
→ deprecated
→ retired
```

### experimental

Neue oder wesentlich umgebaute Skilllogik. Quellen und Design sind plausibel, aber Praxis-/Evalabdeckung ist noch begrenzt.

### candidate

Bereits praktisch verwendet oder mehrfach geprüft, aber noch nicht durch ausreichende Regressionsevals als stabil abgesichert.

### stable

Wiederholt praktisch bewährt und mit relevanten Evalklassen abgesichert. Keine bekannten schweren Trigger-, Scope-, Sicherheits- oder Outputprobleme.

### deprecated

Für neue Nutzung nicht mehr empfohlen. Ersatz oder Migration ist dokumentiert.

### retired

Nicht mehr aktiv angeboten. Historie bleibt nachvollziehbar.

## Eval Coverage

Empfohlene Werte:

- `none` – keine formalen Evalfälle im zentralen Evalbestand;
- `partial` – einige zentrale Trigger-/Behavior-/Outcome-Fälle vorhanden;
- `core` – wesentliche positive, negative und schwierige Kernfälle vorhanden;
- `broad` – zusätzlich umfangreiche Regressionen und Varianten.

Maturity und Eval Coverage sind nicht identisch. Ein Skill kann viel Praxis haben und trotzdem noch unzureichende formale Evals besitzen.

Aktuell besitzt `context-engineering` als bestehender `candidate` `partial` Evalabdeckung. Die ergänzten Context-Skills, alle sieben Wissensmanagement-Skills, alle fünf Schnittstellen-/Contract-Skills, alle sieben Infrastruktur-/DevOps-Skills, alle acht Reliability-/System-Observability-Skills, alle neun Data-Engineering-Skills, alle sieben Software-Architecture-/System-Design-Skills und alle acht Requirements-/Specification-Skills starten beziehungsweise bleiben bewusst `experimental` mit `partial` Evalabdeckung.

Für Reliability sind sechs Startfälle je Skill definiert, insgesamt 48. Der erste Same-Model-Smoke-Lauf wurde am 2026-08-24 ausgeführt; das ersetzt keinen unabhängigen verblindeten Benchmark und rechtfertigt allein keine Hochstufung.

Für Data Engineering sind sechs Startfälle je Skill definiert, insgesamt 54. Diese 54 Fälle sind derzeit **definiert, aber noch nicht ausgeführt oder bestanden**.

Für Software Architecture und System Design sind sechs Startfälle je Skill definiert, insgesamt 42. Der erste Same-Model-Smoke-Lauf wurde am 2026-08-25 gegen `78abce4ade2e1d92dfc47f6169dcd2551d8d0f09` ausgeführt. Alle 42 Fälle entsprachen dem erwarteten Verhalten und Status (30× `pass`, 6× `partial`, 6× `blocked`, 0 verbotene Verhaltensweisen). Das ersetzt keinen unabhängigen verblindeten Benchmark und rechtfertigt allein keine Hochstufung.

Für Requirements und Spezifikations-Engineering sind sechs Startfälle je Skill definiert, insgesamt 48. Diese 48 Fälle sind derzeit **definiert, aber noch nicht ausgeführt oder bestanden**.

## Capabilities

Der Katalog kann Fähigkeiten nennen, die für einen Skill relevant sind, z. B.:

- `web-required`;
- `browser-required`;
- `repository-read`;
- `code-execution`;
- `source-of-truth-access`;
- `context-metrics-preferred`;
- `working-state-access-required`;
- `knowledge-base-read-required`;
- `knowledge-base-write-gated`;
- `contract-source-access-required`;
- `contract-baseline-required`;
- `infrastructure-source-access-required`;
- `infrastructure-preview-preferred`;
- `infrastructure-write-gated`;
- `deployment-write-gated`;
- `runtime-observability-access-preferred`;
- `incident-evidence-access-preferred`;
- `capacity-evidence-access-preferred`;
- `controlled-fault-injection-gated`;
- `data-source-access-preferred`;
- `data-runtime-evidence-preferred`;
- `data-contract-source-access-preferred`;
- `lineage-metadata-access-preferred`;
- `architecture-source-access-preferred`;
- `architecture-runtime-evidence-preferred`;
- `requirements-source-access-preferred`;
- `requirements-source-access-required`;
- `requirements-baseline-required`;
- `downstream-artifact-access-preferred`;
- `stakeholder-interaction-optional`.

Diese Angaben ersetzen nicht die detaillierten Fallback- und Rechte-Regeln des Skills.

## Pflege

Bei folgenden Änderungen `skill-catalog.yml` prüfen:

- neuer Skill;
- Skill umbenannt oder verschoben;
- Maturity geändert;
- Evalabdeckung verändert;
- Capability-Anforderung wesentlich geändert;
- Skill deprecated oder retired.

## Reife-Gate

Eine Hochstufung soll begründet werden.

Insbesondere `stable` erfordert mindestens:

1. wiederholte reale Nutzung oder belastbare Golden Tasks;
2. relevante positive und Near-Miss-Trigger-Evals;
3. Behavior-/Outcome-Prüfung der Kernfunktion;
4. keine offenen Blocker aus `skill-review`;
5. dokumentierte Capability-/Fallback-Grenzen;
6. Sicherheitsreview, wenn der Skill externe Inhalte, Tools oder Schreib-/Ausführungsrechte nutzt.

Für Context-/Compaction-Skills sollte zusätzlich reale Fortsetzungsfähigkeit beziehungsweise Outcome nach Context-Änderungen geprüft werden. Eine reine Tokenreduktion reicht nicht als Maturity-Beleg.

Für Wissensmanagement-Skills sollte zusätzlich an realen Wissensbasen geprüft werden, ob Ingest und Pflege tatsächlich Dubletten, Provenance-Verlust und Retrieval-Drift reduzieren. Die Existenz synthetischer Evalcases allein reicht nicht für eine Hochstufung.

Für Schnittstellen-Skills sollte an realen Contracts geprüft werden, ob Consumerannahmen, Breaking Changes und rollout-sensitive Änderungen zuverlässig erkannt werden. Ein grüner Schema-Diff allein reicht nicht als Maturity-Beleg.

Für Infrastruktur-/DevOps-Skills sollte an realen, kontrollierten Projekten geprüft werden, ob Plan-/Actual-State-Abweichungen, destructive Changes, GitOps-Gates und Deployment-/Rollback-Grenzen zuverlässig erkannt werden. Ein grüner Plan, Build oder Pipeline-Lauf allein reicht nicht als Maturity-Beleg.

Für Reliability-/System-Observability-Skills sollte zusätzlich an realen Services beziehungsweise belastbaren Betriebs-/Incident-/Game-Day-Szenarien geprüft werden, ob SLO-Grenzen, Runtime-Evidence, Alert-Actionability, Incident-Gates, Capacity-Annahmen und Resilience-Safety zuverlässig erkannt werden. Ein vorhandenes Dashboard oder definierter Evalcase allein reicht nicht als Maturity-Beleg.

Für Data-Engineering-Skills sollte zusätzlich an realen Datenflüssen beziehungsweise belastbaren Pipeline-/Backfill-/Consumer-Szenarien geprüft werden, ob Source-of-Truth-Lücken, Grainfehler, CDC-/Replay-Grenzen, semantische Contractänderungen, Data-Quality-Blind-Spots, Lineage-Lücken und Reprocessing-Gates zuverlässig erkannt werden. Ein grüner DAG, SQL-Lauf oder definierter Evalcase allein reicht nicht als Maturity-Beleg.

Für Software-Architecture-/System-Design-Skills sollte zusätzlich an realen Systemen oder belastbaren Architekturentscheidungen geprüft werden, ob Architecture 0 korrekt rekonstruiert, Drivers und Missing Evidence sauber getrennt, unnötige verteilte Komplexität vermieden, echte Trade-offs erkannt, Migrationszwischenzustände erklärt und lokale Architekturregeln ohne Patterndogma geprüft werden. Ein schönes Diagramm, ein ADR oder ein Same-Model-Smoke-Lauf allein reicht nicht als Maturity-Beleg.

Für Requirements-/Specification-Skills sollte zusätzlich an realen Spezifikationen und Stakeholder-/Source-Evidence geprüft werden, ob Soll-Baselines korrekt rekonstruiert, Inferenz sichtbar bleibt, keine Zielwerte erfunden, Acceptance und Traceability sinnvoll getrennt, Changes mit Downstream-Impact erkannt und Validation/Review nicht mit Product Approval verwechselt werden. Ein ausgefülltes PRD, 100 Prozent Traceability oder definierte Evalcases allein reichen nicht als Maturity-Beleg.

## Leitgedanke

> Der Katalog sagt nicht nur, was wir haben – sondern wie viel Vertrauen der aktuelle Reifegrad rechtfertigt.
