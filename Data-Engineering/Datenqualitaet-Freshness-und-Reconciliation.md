# Datenqualität, Freshness und Reconciliation

## Zweck

Datenqualität beschreibt, ob ein Dataset für einen konkreten Consumerzweck ausreichend vertrauenswürdig ist. Sie ist mehrdimensional und kann nicht durch einen einzelnen grünen Check bewiesen werden.

## Typische Qualitätsachsen

Je nach Kontext relevant:

- Completeness;
- Conformity / Schema;
- Uniqueness;
- Validity;
- Accuracy gegen geeignete Referenz;
- Consistency zwischen Quellen oder Ableitungen;
- Freshness / Timeliness;
- Volume-/Distribution-Anomalien;
- Referential Integrity;
- fachliche Invarianten.

Keine zentrale Liste ist für jedes Dataset vollständig.

## Regelquelle

Eine Quality Rule braucht eine fachliche oder technische Begründung:

```text
Consumer-/Business-Invariante
oder
Source-/Contract-Zusage
oder
bekannter Failure Mode
oder
belastbare Baseline
→ Quality Rule
```

Schwellen nicht aus Gewohnheit erfinden.

## Freshness

Freshness muss den relevanten Zeitbezug benennen:

- Source Event Time;
- Source Update Time;
- Ingestion Time;
- Processing/Publish Time;
- Consumer Availability Time.

`MAX(timestamp)` allein beweist nicht automatisch vollständige Aktualität.

## Reconciliation

Reconciliation vergleicht Daten gegen eine passende unabhängige oder vorgelagerte Erwartung.

Mögliche Formen:

- Counts/Volumes nach definiertem Grain;
- Summen oder Salden;
- Kontrollsummen/Hashes bei geeigneter Semantik;
- Schlüsselmenge;
- Source-vs.-Target-Abgleich;
- Dual-Run-/Old-vs.-New-Vergleich;
- fachliche Kontrollzahlen.

Toleranzen müssen lokal begründet werden.

## Fehlende Daten vs. falsche Daten

Unterscheiden:

- Dataset ist noch nicht vollständig;
- Dataset ist verspätet;
- Dataset ist vollständig, aber semantisch falsch;
- Quality Check kann den Zustand nicht zuverlässig erkennen;
- Source selbst liefert bereits fehlerhafte Daten.

Die Reaktion kann je nach Consumer zwischen warnen, quarantänen, Publish blockieren oder bewusst weiterliefern variieren. Diese Policy bleibt lokal.

## Sensitive Data

Quality-Debugging ist keine Freigabe, komplette produktive Datensätze, PII oder Secrets in Logs, Tickets oder dauerhafte Reports zu kopieren.

## Nicht tun

- `row_count > 0` als allgemeine Qualitätsfreigabe behandeln;
- 0 % Nulls oder 100 % Uniqueness ohne fachliche Grundlage verlangen;
- Anomaly Detection als Beweis für Accuracy ansehen;
- fehlende Source-Qualität durch Target-Checks wegdefinieren;
- erfolgreich ausgeführte Quality Checks mit Consumerkorrektheit gleichsetzen;
- bei fehlender Baseline einen willkürlichen Threshold setzen.