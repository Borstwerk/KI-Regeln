# Dokumentation

Dieser Bereich erklärt, wie das Repository praktisch verwendet, gepflegt und verstanden wird.

Er richtet sich vor allem an Menschen, die:

- das Repository neu kennenlernen;
- verstehen möchten, was einzelne Skills bedeuten;
- Regeln in eigene Projekte übernehmen wollen;
- den Bestand regelmäßig auf Aktualität prüfen möchten;
- nachvollziehen möchten, welche externen Skills und Quellen aktiv beobachtet werden;
- Reifegrad und Evalabdeckung von Skills einschätzen möchten.

## Inhalte

- `Nutzung-des-Repositories.md` – erklärt, wie das Repository in echten Projekten eingesetzt wird;
- `Skill-Handbuch.md` – erklärt die allgemeinen Skills in verständlicher Sprache;
- `Skill-Handbuch-Context-und-Long-Horizon.md` – erklärt Context Engineering, Context Audit, Compaction und Session-Handoffs für längere Agentenläufe;
- `Skill-Handbuch-Wissensmanagement.md` – erklärt Design, Ingest, Distillation, Synthese, Query, Maintenance und Review persistenter Wissensbasen;
- `Skill-Handbuch-Schnittstellen-und-Vertraege.md` – erklärt Interface Design, HTTP-/Event-Contracts, Compatibility Change Review und Interface Review;
- `Skill-Handbuch-Infrastruktur-und-DevOps.md` – erklärt Infrastructure as Code, Change Review, CI, Container Builds, Deploymentstrategien, GitOps und Infrastrukturreview;
- `Skill-Handbuch-Reliability-und-System-Observability.md` – erklärt SLO Design, System-Observability, Alerting, Incident Response, Postmortems, Capacity, Resilience-Experimente und Reliability Review;
- `Skill-Handbuch-Data-Engineering.md` – erklärt Pipeline Design, Ingestion, Transformation, analytische Modellierung, Data Quality, Data Contracts, Lineage, Orchestrierung und Data-Engineering-Review;
- `Skill-Handbuch-Software-Architecture-und-System-Design.md` – erklärt Architecture Baseline, System Design, Dekomposition, Trade-off-Analyse, Evolution, Conformance und Architecture Review;
- `Skill-Handbuch-Requirements-und-Spezifikations-Engineering.md` – erklärt Requirements Baseline, Elicitation, Specification, Acceptance Criteria, Traceability, Change Analysis, Validation und Requirements Review;
- `Skill-Handbuch-Social-Media-und-Content-Praesenz.md` – erklärt Presence Baseline, Social Content Strategy, Editorialplanung, Social Content Design, Plattformadaption, Repurposing, Community Engagement, Performanceanalyse und Presence Review;
- `Skill-Handbuch-Dokumentationserstellung.md` – erklärt die Skills des Bereichs `Dokumentationserstellung/`;
- `Skill-Handbuch-Datenbanken.md` – erklärt die engine-neutralen Datenbank-Skills und ihre Abgrenzung;
- `Skill-Handbuch-Testing-und-QA.md` – erklärt Teststrategie, Testdesign, Integration, Contracts, E2E, Flakiness, Failure Testing und Test-Suite-Review;
- `Skill-Handbuch-Meta-und-Sicherheit.md` – erklärt Skill-Engineering- und Security-Skills;
- `Skill-Katalog.md` – erklärt Maturity und den maschinenlesbaren Skill-Katalog;
- `../skill-catalog.yml` – Inventar der zentralen Skills mit Reifegrad und Evalabdeckung;
- `../Evals/` – wiederholbare Trigger-, Behavior-, Outcome- und Regressionsevals;
- `../Workflows/` – Recipes für wiederkehrende Skill-Ketten;
- `Pflege-und-Aktualisierung.md` – beschreibt Pflegeprozess, Review-Rhythmus und den Umgang mit neuen Quellen und Entwicklungen;
- `Quellenregister.md` – erklärt Quellenklassen, Monitoring-Arten und den Umgang mit veränderlichen Upstreams;
- `upstream-sources.yml` – maschinenlesbare Liste aktiv beobachteter Upstreams mit Monitoring-Modus, Cadence, geprüftem SHA/Stand und lokalem Einfluss;
- `Upstream-Audit-2026-08-23.md` – dokumentiert den ersten vollständigen Audit der damaligen Fachbereiche;
- `Upstream-Audit-2026-08-23-Ergaenzung.md` – ergänzt den Audit um Skill Engineering, Sicherheit, Evals und Workflows.

## Grundsatz

> Allgemeine Arbeitsweise zentral, konkrete Wahrheit lokal.

Das Repository liefert wiederverwendbare Methoden. Projektziele, Stakeholder-/Requirements-Quellen, Fachlogik, Kanon, Architektur, Marken-/Audience-Wahrheit, reale Plattformaccounts, Content-Ziele und lokale Anforderungen bleiben im jeweiligen Projekt.

## Skills und Reife

Ein Skill besitzt neben seiner fachlichen Beschreibung einen expliziten Reifegrad:

```text
experimental
→ candidate
→ stable
→ deprecated
→ retired
```

`stable` ist kein Standardwert. Die Einstufung soll durch reale Nutzung, passende Evals und – bei relevanten Capabilities – Security Review gestützt sein.

## Quellen und Upstreams

Fachbereiche besitzen eigene `Quellen-und-Inspirationen.md`-Dateien. Sie beantworten:

> Welche externen Konzepte haben diesen Bereich beeinflusst?

Das zentrale Quellenregister beantwortet zusätzlich:

> Welche veränderlichen Quellen beobachten wir aktiv auf Updates?

Aktuell gibt es zwei Monitoring-Arten:

- `exact-sha` für konkrete GitHub-Dateien;
- `semantic-review` für lebende Web- und Produktdokumentation.

Zusätzlich unterscheiden wir zwischen monatlich und quartalsweise zu prüfenden Quellen.

Dabei gilt:

> Upstream-Änderung = Review-Signal, nicht automatischer Sync.

## Für Einsteiger

Wer das Repository zum ersten Mal verwendet, sollte in dieser Reihenfolge lesen:

1. `../README.md`
2. `Nutzung-des-Repositories.md`
3. `Skill-Handbuch.md`
4. bei Auswahl oder Bewertung von Skills `Skill-Katalog.md`
5. bei längerer Agentenarbeit oder Context-/Tokenfragen zusätzlich `Skill-Handbuch-Context-und-Long-Horizon.md`
6. bei persistenter Wissensarbeit zusätzlich `Skill-Handbuch-Wissensmanagement.md`
7. bei Schnittstellen-/API-/Contract-Arbeit zusätzlich `Skill-Handbuch-Schnittstellen-und-Vertraege.md`
8. bei Infrastruktur-/DevOps-/IaC-Arbeit zusätzlich `Skill-Handbuch-Infrastruktur-und-DevOps.md`
9. bei Reliability-/Observability-/SRE-Arbeit zusätzlich `Skill-Handbuch-Reliability-und-System-Observability.md`
10. bei Data-Engineering-/ETL-/CDC-/Warehouse-Arbeit zusätzlich `Skill-Handbuch-Data-Engineering.md`
11. bei Software-Architecture-/System-Design-Arbeit zusätzlich `Skill-Handbuch-Software-Architecture-und-System-Design.md`
12. bei Requirements-/Specification-Arbeit zusätzlich `Skill-Handbuch-Requirements-und-Spezifikations-Engineering.md`
13. bei Social-Media-/Content-Präsenz-Arbeit zusätzlich `Skill-Handbuch-Social-Media-und-Content-Praesenz.md`
14. bei Dokumentationsarbeit zusätzlich `Skill-Handbuch-Dokumentationserstellung.md`
15. bei Datenbankarbeit zusätzlich `Skill-Handbuch-Datenbanken.md`
16. bei Testing-/QA-Arbeit zusätzlich `Skill-Handbuch-Testing-und-QA.md`
17. bei Skill-/Security-Arbeit zusätzlich `Skill-Handbuch-Meta-und-Sicherheit.md`
18. erst danach die für das eigene Vorhaben relevanten Regel-, Skill- und Workflow-Dateien.

Nicht das komplette Repository muss für jede Aufgabe geladen oder übernommen werden. Gute Nutzung bedeutet gezielte Auswahl.