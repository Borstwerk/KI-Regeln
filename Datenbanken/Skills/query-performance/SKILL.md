---
name: query-performance
description: Diagnostiziert langsame oder ressourcenintensive Datenbankabfragen anhand realer Messwerte, vorhandener Indizes und Execution-Plan-Evidence. Verwenden bei langsamen Queries, hohem Scan-/I/O-Aufwand, Indexfragen oder Performance-Regressionen. Nicht für reine Query-Erstellung ohne Performanceproblem verwenden.
compatibility: Bevorzugt Zugriff auf reale Query, vorhandene Indizes, Execution Plan und Messwerte. Ohne diese nur Hypothesen und nächste Messschritte liefern.
---

# Query Performance

## Ziel

Den tatsächlichen Engpass einer Query nachweisen und die kleinste sinnvolle Änderung mit Vorher-/Nachher-Evidence bewerten.

## Workflow

1. Problem und Baseline erfassen.
2. Reale Query/Parameter und Workload verstehen.
3. Bestehende Indizes / physische Strukturen prüfen.
4. Sicheren Execution Plan bzw. Engine-Diagnose abrufen.
5. Ursache hypothesenbasiert eingrenzen.
6. Schemafehler vs. Queryfehler vs. Index-/Ressourcenproblem unterscheiden.
7. Kleinste sinnvolle Änderung vorschlagen.
8. Änderung nur im freigegebenen Scope ausführen.
9. Erneut messen und Nebenwirkungen prüfen.

## Regeln

- Kein reflexhafter Indexbau.
- Vor neuem Index überlappende/bestehende Indizes prüfen.
- Lesegewinn gegen Schreib-, Speicher- und Wartungskosten abwägen.
- Ausführende Analysebefehle auf Last-/Write-Risiko prüfen.
- Keine starke Aussage „wird schneller“ ohne neue Messung.
- Wenn keine Messfähigkeit besteht: als `unverified hypothesis` kennzeichnen.

## Evidence

```text
Baseline
Execution-/Diagnose-Evidence
Ursachenhypothese
Änderung
Post-Change-Evidence
Nebenwirkungen
```

## Gate

Index-/Schemaänderung in einer realen DB ist keine automatische Folge der Diagnose. Vor Write/Migration passende Freigabe verlangen.

## Leitgedanke

> Performance wird gemessen, nicht herbeigeredet.