# Workflow – Infrastrukturänderung

## Ziel

Eine Infrastrukturänderung von Desired State bis zur frischen Nachprüfung kontrolliert durchführen.

## Ablauf

```text
Anforderung / lokale Architektur
→ infrastructure-as-code
→ READ / VALIDATE
→ PLAN / PREVIEW
→ infrastructure-change-review
→ lokales Human-/Execution-Gate
→ CHANGE / APPLY
→ Fresh Verification
→ Actual State / Drift prüfen
→ bei größerem Scope infrastructure-review
```

## Vor dem Preview

Klären:

- Zielumgebung;
- Ownership;
- Tool-/Provider-Version;
- Current State / Drift;
- relevante Security-/Policy-Regeln;
- Recovery-/Backup-Voraussetzungen.

## Gate

`SAFE_TO_PROCEED_TO_GATE` aus dem Review ist keine Apply-Autorisierung.

Die lokale Projektgovernance entscheidet über Apply, Destroy, State-Operationen und Recovery.

## Nach der Änderung

Frische Evidence erzeugen:

- Exit-/Apply-Ergebnis;
- tatsächlicher Ressourcenstatus;
- relevante Health-/Smoke-Checks;
- erwartete vs. unerwartete Drift;
- offene manuelle Schritte.

## Destructive Changes

Bei Replace/Delete/Prune/State/Recovery zusätzliche Fachgates einbinden, z. B. `schema-migration`, `database-operations`, Security oder Reliability.

## Leitgedanke

> Eine Infrastrukturänderung ist erst abgeschlossen, wenn der tatsächliche Zustand gegen die beabsichtigte Wirkung geprüft wurde.