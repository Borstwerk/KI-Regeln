# Skill-Handbuch – Requirements und Spezifikations-Engineering

Dieses Handbuch hilft bei der Auswahl der acht Skills aus `Requirements-und-Spezifikations-Engineering/`.

## Schnellauswahl

| Wenn die Aufgabe lautet … | Primärer Skill |
|---|---|
| bestehenden Sollstand und gültige Anforderungen rekonstruieren | `requirements-baseline` |
| Bedarfe, Stakeholder, Constraints und offene Fragen herausarbeiten | `requirements-elicitation` |
| bestätigte Bedarfe als belastbare Requirements formulieren | `requirements-specification` |
| beobachtbare Erfüllungsbedingungen definieren | `acceptance-criteria-design` |
| Sources, Ziele, Requirements und Downstream-Artefakte verknüpfen | `requirements-traceability` |
| eine Requirement-Änderung und ihre Folgen analysieren | `requirements-change-analysis` |
| Requirements gegen Bedarf, Qualität und Verifizierbarkeit validieren | `requirements-validation` |
| einen breiten unabhängigen Requirements-/Readiness-Audit durchführen | `requirements-review` |

## Auswahlregeln

### `requirements-baseline`

Wenn zuerst die Frage lautet: **Was gilt heute tatsächlich?**

Der Skill liest bestehende Requirements Sources, Status, Approvals/Supersession, Annahmen, Acceptance und Traceability. Er spezifiziert noch nichts neu.

### `requirements-elicitation`

Wenn der Bedarf noch unklar, unvollständig oder widersprüchlich ist.

Der Skill wählt die Elicitation-Technik nach Informationsproblem und nutzt vorhandene Evidence, bevor neue Fragen gestellt werden. Inferenz bleibt sichtbar.

### `requirements-specification`

Wenn ausreichend bestätigte Bedarfe bereits vorliegen und in Requirements überführt werden sollen.

Der Skill besitzt die semantische Spezifikation. PRD, BRD, SRS, User Story oder Tabelle sind nur mögliche Container.

### `acceptance-criteria-design`

Wenn klar ist, **was** gelten soll, aber noch nicht, woran Erfüllung beobachtbar beurteilt wird.

Er definiert Acceptance Criteria und Verification Intent. Konkrete Testfälle, Testdaten und Automation gehören zu `Testing-und-QA/`.

### `requirements-traceability`

Wenn Herkunft, Coverage, Orphans oder Downstream-Wirkung nachvollziehbar werden sollen.

100 Prozent Links sind kein Beweis für richtige Requirements.

### `requirements-change-analysis`

Wenn ein bestehendes oder baseliniertes Requirement semantisch geändert werden soll.

Der Skill analysiert Upstream-/Downstream-Impact und Supersession. Er ändert weder Code noch Contracts oder Produktion.

### `requirements-validation`

Wenn geprüft werden soll, ob die Requirements den relevanten Bedarf ausreichend klar, konsistent, vollständig und verifizierbar beschreiben.

Requirements Validation ist nicht Product Validation und nicht Testausführung.

### `requirements-review`

Für unabhängige breite Readiness- oder Handoff-Reviews.

Er prüft das Paket als Ganzes und bleibt read-only. `READY_FOR_LOCAL_GATE` ist keine Approval- oder Execution-Autorisierung.

## Wichtige Near-Misses

| Aufgabe | Stattdessen |
|---|---|
| Fachbegriffe/Invarianten modellieren | `domain-modeling` |
| System-/Service-Struktur entwerfen | `system-design` / Architecture-Skills |
| API-/Event-Verträge definieren | Interface-Skills |
| konkrete Testfälle/Testautomation | Testing-und-QA-Skills |
| Produktwirkung im Feld validieren | lokaler Product-/UX-/Operations-Prozess |
| SLO-/Alert-/Runtime-Modell | Reliability-Skills |
| Requirement-Dokument nur sprachlich/formatlich reviewen | `docs-review` / `technical-writing` |

## Keine Pflichtformate

Zentral nicht vorgeschrieben:

- PRD, BRD oder SRS;
- User Story;
- Given/When/Then;
- EARS;
- MoSCoW, RICE oder P0/P1/P2;
- bestimmte Requirement-ID-Schemata;
- numerische Clarity-/Readiness-Scores.

Lokale Standards dürfen solche Formate selbstverständlich festlegen.

## Empfohlene Skill-Ketten

### Neue oder vage Initiative

```text
requirements-elicitation
→ requirements-specification
→ acceptance-criteria-design
→ requirements-traceability
→ requirements-validation
```

### Bestehendes Produkt

```text
requirements-baseline
→ requirements-elicitation für Lücken
→ requirements-specification / Change Analysis
→ requirements-validation
```

### Requirement Change

```text
requirements-baseline
→ requirements-change-analysis
→ requirements-traceability
→ optional neue Specification / Acceptance Criteria
→ requirements-validation
```

### Unabhängiger Handoff-Audit

```text
requirements-baseline
→ requirements-validation
→ requirements-traceability
→ requirements-review
→ lokales Gate
```

## Leitgedanke

> Requirements Engineering hält fest, was und warum gelten soll. Die nachgelagerten Disziplinen entscheiden, wie es umgesetzt und nachgewiesen wird.