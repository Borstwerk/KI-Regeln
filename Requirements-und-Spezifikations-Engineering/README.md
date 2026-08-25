# Requirements und Spezifikations-Engineering

Dieser Bereich beschreibt allgemeine, technologie- und methodenneutrale Arbeitsweisen, um Stakeholderbedarfe in belastbare, nachvollziehbare und verifizierbare Anforderungen zu überführen und über ihren Lebenszyklus zu pflegen.

## Grundprinzip

> Eine Anforderung beschreibt einen begründeten Bedarf, ein erwartetes beobachtbares Verhalten oder einen verbindlichen Constraint – nicht vorschnell die technische Lösung.

Requirements Engineering reduziert Unsicherheit vor und während Design, Implementierung und Betrieb. Es erfindet keine lokale Produktwahrheit und ersetzt weder Stakeholderentscheidungen noch fachliche Sources of Truth.

## Scope

`Requirements-und-Spezifikations-Engineering/` behandelt insbesondere:

- Stakeholder, Ziele, Bedarfe und Requirements Sources;
- bestehende Requirements-Baselines und Konflikte zwischen Quellen;
- Elicitation mit Interviews, Workshops, Dokument-/Systemanalyse und geeigneten weiteren Techniken;
- Scope, Non-Goals, Annahmen, Constraints, Abhängigkeiten und offene Fragen;
- funktionale Anforderungen, Qualitätsanforderungen und Übergangs-/Betriebsanforderungen;
- präzise Requirement Statements und geeignete Artefaktformen;
- Szenarien, Use Cases, User Stories und andere Darstellungen als optionale Formen;
- messbare Qualitätsziele ohne erfundene Schwellen;
- Acceptance Criteria und Verifikationsabsicht;
- Traceability, Provenance, Coverage und Requirement-IDs;
- Priorisierung und Status nach lokaler Policy statt universeller Skala;
- Requirements Change, Baselines, Versionen und Supersession;
- Requirements Validation, Konfliktklärung und Readiness Reviews.

## Nicht der Scope

- **Software Architecture und System Design:** `../Software-Architecture-und-System-Design/` entscheidet, welche Struktur bestätigte Requirements, Drivers und Invarianten mit welchen Trade-offs erfüllt.
- **Domain Modeling:** `../Programmieren/Skills/domain-modeling/` klärt Fachbegriffe, Fachobjekte und fachliche Invarianten. Requirements referenzieren diese Wahrheit, erfinden sie aber nicht.
- **Schnittstellen und Verträge:** `../Schnittstellen-und-Vertraege/` konkretisiert beobachtbare Provider-/Consumer-Verträge über bereits begründete Systemgrenzen.
- **Testing und QA:** `../Testing-und-QA/` entwirft und führt Tests aus. Requirements definieren Akzeptanz- und Verifikationsabsicht, nicht die komplette Testimplementierung.
- **Reliability und System-Observability:** `../Reliability-und-System-Observability/` operationalisiert bestätigte Zuverlässigkeitsziele in SLI/SLO-, Alert-, Capacity- und Runtime-Evidence.
- **Sicherheit:** besitzt Threat Modeling, Security Controls und Security Testing im Detail. Security Requirements können hier erfasst werden, ihre fachliche Ausgestaltung gehört zur Sicherheitsdomäne.
- **Dokumentationserstellung:** besitzt allgemeine Dokumenttypen und Schreibmethodik. PRD, BRD, SRS, Backlog, Ticket oder Tabelle sind mögliche Container für Requirements, keine eigene fachliche Wahrheit.
- **Implementierung und Deployment:** ein freigegebenes Requirement oder Review-Verdict autorisiert keine Code-, Daten-, Infrastruktur- oder Produktionsänderung.

## Zentrales Modell

```text
Stakeholder / Source / Ziel / Problem
→ Bedarf / Erwartung / Constraint
→ Requirement Candidate
→ Klärung / Konflikt / Validation
→ bestätigtes Requirement + Acceptance-/Verification-Intent
→ Traceability zu Design / Contract / Test / Betrieb
→ Change / Supersession / Re-Validation
```

## Wichtige Trennungen

```text
Bedarf ≠ Requirement
Requirement ≠ Lösung
Requirement ≠ User Story
Acceptance Criterion ≠ Test Case
Verifizierbar ≠ bereits verifiziert
Requirements Validation ≠ Product Validation
Priorität ≠ objektiver Geschäftswert
Traceability ≠ Korrektheit
Dokument vollständig ≠ Anforderungen vollständig
```

## Keine Formatreligion

Nicht zentral festschreiben:

- jedes Requirement müsse als User Story formuliert sein;
- jedes Acceptance Criterion müsse Given/When/Then oder EARS verwenden;
- jedes Projekt brauche PRD, BRD und SRS gleichzeitig;
- jede Anforderung müsse exakt ein `shall` enthalten;
- MoSCoW, RICE oder eine andere Priorisierungsskala sei Pflicht;
- NFRs müssten in einer universellen Taxonomie vollständig sein;
- eine numerische Clarity-/Quality-Score-Schwelle beweise Readiness;
- jede Anforderung müsse direkt als automatisierter Test ausführbar sein;
- technische Constraints seien automatisch schlechte Requirements;
- mehr Dokumentation bedeute bessere Requirements.

## Evidence-Status

Für Quellen und Requirement-Aussagen können unter anderem genutzt werden:

- `CONFIRMED`
- `INFERRED`
- `UNVERIFIED`
- `CONFLICTING`
- `SUPERSEDED`

Inferenz bleibt sichtbar und wird nicht still zur Stakeholderaussage.

## Risikomodell

```text
READ / BASELINE
→ vorhandene Requirements, Sources, Status und Konflikte erfassen

ELICIT / SPECIFY
→ Bedarfe klären und Requirements formulieren

VALIDATE / REVIEW
→ Qualität, Stakeholder-Fit, Traceability und Missing Evidence prüfen

CHANGE-SENSITIVE
→ baselinierte oder downstream wirksame Requirements ändern / superseden

IMPLEMENT / VERIFY IN PRODUCT
→ reale Umsetzung und Produktverifikation; gehört in nachgelagerte Fachprozesse und lokale Gates
```

## Operative Skills

- `requirements-baseline`
- `requirements-elicitation`
- `requirements-specification`
- `acceptance-criteria-design`
- `requirements-traceability`
- `requirements-change-analysis`
- `requirements-validation`
- `requirements-review`

## Leitgedanken

> Erst Quelle und Bedarf verstehen, dann formulieren.

> Unsicherheit markieren ist besser als eine präzise klingende Erfindung.

> Ein gutes Requirement lässt erkennen, warum es existiert und woran Erfüllung beurteilt wird.

> Allgemeine Arbeitsweise zentral, konkrete Anforderungen lokal.