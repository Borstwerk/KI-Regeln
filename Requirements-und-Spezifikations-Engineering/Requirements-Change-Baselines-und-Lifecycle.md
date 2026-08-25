# Requirements Change, Baselines und Lifecycle

## Zweck

Requirements ändern sich. Gute Pflege macht sichtbar, was sich geändert hat, warum, wer betroffen ist und welcher Stand weiterhin gültig ist.

## Statusmodell

Ein Projekt kann eigene Statuswerte verwenden. Sinnvolle Zustände können beispielsweise sein:

- `DRAFT`
- `IN_REVIEW`
- `APPROVED`
- `SUPERSEDED`
- `REJECTED`
- `DEFERRED`

Die Begriffe sind weniger wichtig als klare Semantik und lokale Entscheidungskompetenz.

## Baseline

Eine Baseline ist ein bewusst referenzierbarer Requirements-Stand. Sie verhindert nicht Change, sondern macht Change relativ zu einem bekannten Stand prüfbar.

```text
Baseline A
→ Change Request / neue Evidence
→ Impact Analysis
→ Entscheidung
→ Baseline B oder dokumentierte Ablehnung
```

## Change Impact

Bei relevanten Änderungen prüfen:

- Quelle und Grund der Änderung;
- betroffene Ziele und Stakeholder;
- geänderte Semantik und Acceptance Criteria;
- Architektur-/Interface-/Daten-/Security-/Reliability-Auswirkung;
- bestehende Implementierung und Tests;
- Migration, Kompatibilität oder Rollout;
- Dokumentation, Betrieb und Support;
- bereits getroffene Downstream-Entscheidungen.

Nicht jede Textänderung ist semantisch; nicht jede kleine Formulierungsänderung ist harmlos.

## Supersession statt Geschichtsverlust

Wenn ein Requirement ersetzt wird, sollte nachvollziehbar bleiben:

- welcher Stand ersetzt wurde;
- wodurch;
- ab wann;
- warum;
- welche Downstream-Links aktualisiert oder bewusst historisch bleiben.

Historische Requirements nicht einfach löschen, wenn Auditability oder Change-Verständnis sie benötigt.

## Priorität und Reihenfolge

Priorisierung ist eine lokale Produkt-/Governanceentscheidung. Requirements Engineering kann Konsequenzen und Dependencies sichtbar machen, aber keine universelle `Must/Should/Could`-, RICE- oder P0/P1/P2-Policy festlegen.

## Execution-Grenze

`requirements-change-analysis` analysiert und dokumentiert Change. Es ändert nicht automatisch Code, Contract, Datenmodell, Test, Deployment oder produktive Konfiguration.

## Leitgedanke

> Requirements dürfen sich ändern – aber nicht unsichtbar.