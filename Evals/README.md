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
- alle sieben Skills aus `Infrastruktur-und-DevOps/`.

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
