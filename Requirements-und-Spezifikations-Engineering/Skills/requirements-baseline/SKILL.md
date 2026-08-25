---
name: requirements-baseline
description: Erfasst bestehende Requirements, Stakeholder-/Quellenbezug, Scope, Status, Annahmen, Konflikte, Acceptance-/Traceability-Abdeckung und offene Lücken als belastbare Ausgangslage. Verwenden vor Änderungen an bestehenden Spezifikationen oder wenn unklar ist, welche Anforderungen aktuell tatsächlich gelten. Nicht als neue Elicitation, Re-Spezifikation oder Implementierungsskill verwenden.
---

# Requirements Baseline

## Ziel

Den aktuellen Requirements-Stand aus realen Quellen rekonstruieren, ohne Dokumentexistenz mit fachlicher Gültigkeit gleichzusetzen.

## Eingaben

- Nutzerauftrag und Scope;
- Requirements-/Produkt-/Projektartefakte;
- relevante Tickets, Entscheidungen und Änderungsverläufe;
- Stakeholder-/Owner-Information;
- gültige Fach-/Policy-/Contract-Sources;
- Downstream-Artefakte, soweit für Konflikte oder Traceability relevant.

## Vorgehen

1. betrachteten Scope und gewünschten Baseline-Zeitpunkt klären.
2. Requirements Sources inventarisieren und nach Autorität/Aktualität einordnen.
3. Requirement Candidates und stabile IDs/Status erfassen.
4. Ziele, Stakeholder, Constraints, Annahmen und Non-Goals zuordnen.
5. widersprüchliche oder supersedete Aussagen markieren.
6. Acceptance-/Verification-Intent und Traceability-Coverage erfassen, soweit vorhanden.
7. aktuelle Downstream-Nutzung prüfen, wenn sie die Gültigkeit einer Aussage beeinflusst.
8. Missing Evidence, Orphans und offene Entscheidungen dokumentieren.

## Evidence Status

- `CONFIRMED`
- `INFERRED`
- `UNVERIFIED`
- `CONFLICTING`
- `SUPERSEDED`

## Nicht tun

- neueste Datei automatisch zur gültigen Baseline erklären;
- implementiertes Verhalten automatisch zum gewünschten Requirement machen;
- fehlende Ziele, Prioritäten oder Acceptance Criteria erfinden;
- Konflikte still durch Auswahl der bequemsten Quelle lösen;
- Requirements ungefragt umschreiben oder Code ändern.

## Ausgabe

```text
Scope / Baseline Point
Sources / Authority / Freshness
Current Requirements / Status
Goals / Stakeholders / Constraints
Assumptions / Non-Goals
Acceptance / Verification Coverage
Traceability / Orphans
Conflicts / Superseded Items
Missing Evidence / Open Decisions
Baseline Confidence
```

## Related

- `requirements-elicitation`
- `requirements-specification`
- `requirements-traceability`
- `requirements-change-analysis`
- `requirements-validation`
- `requirements-review`

## Leitgedanke

> Erst wissen, was heute wirklich gilt, bevor morgen etwas geändert wird.