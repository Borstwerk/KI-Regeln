---
name: architecture-tradeoff-analysis
description: Vergleicht ernsthafte Architekturvarianten anhand konkreter Quality-Szenarien, Constraints, Failure Modes, Kosten, Operability, Migration und Sensitivity Points. Verwenden bei schwer umkehrbaren Architekturentscheidungen oder konkurrierenden Systemdesigns. Nicht als generische Pro/Contra-Liste oder Scoregenerator verwenden.
---

# Architecture Tradeoff Analysis

## Ziel

Sichtbar machen, welche Architektur unter den bekannten Drivers welche Eigenschaften gewinnt, welche Kosten sie erzeugt und welche Annahmen die Entscheidung kippen könnten.

## Eingaben

- bestätigte Drivers und Constraints;
- konkrete Quality-Szenarien;
- zwei oder mehr tatsächlich viable Kandidaten;
- relevante Workload-/Failure-/Kosten-Evidence;
- Migrations- und Betriebsbedingungen.

## Vorgehen

1. prüfen, ob überhaupt mehrere ernsthafte Kandidaten existieren.
2. Kandidaten auf echte strukturelle Unterschiede reduzieren.
3. Quality-Szenarien und Invarianten als Bewertungsachsen verwenden.
4. je Kandidat Vorteile, ehrliche Schwächen und neue Failure Modes erfassen.
5. Betriebs-, Team-, Kosten- und Migrationsfolgen bewerten, soweit belegt.
6. Sensitivity Points und Missing Evidence markieren.
7. Optionen ausschließen, wenn Requirement/Invariante sie bereits schließt.
8. Empfehlung als nachvollziehbare Evidence Chain statt Gesamtscore formulieren.

## Szenarioformat

```text
Stimulus / Environment
→ betroffener Systemteil
→ erwartete Reaktion
→ beobachtbares Ergebnis
```

## Ergebnisstatus

- `RECOMMENDABLE` – Evidence reicht für eine begründete Empfehlung;
- `CONDITIONAL` – Empfehlung hängt sichtbar von einer offenen Annahme/Messung ab;
- `UNVERIFIED` – entscheidungsrelevante Evidence fehlt;
- `BLOCKED` – kein Kandidat erfüllt einen verbindlichen Constraint oder eine Invariante.

## Nicht tun

- Kandidaten nur zur Vollständigkeit erfinden;
- Quality Attributes als ungewichtete Checkliste behandeln;
- undurchsichtige Gesamtpunktzahl als Entscheidung verwenden;
- fehlende Zielwerte oder Benchmarks erfinden;
- populäres Pattern automatisch besser bewerten;
- Review/Empfehlung als Autorisierung für Architekturänderung behandeln.

## Ausgabe

```text
Decision / Drivers
Viable Candidates
Quality Scenarios
Per-Candidate Strengths / Weaknesses
Failure Modes / Operability
Migration / Cost Considerations
Sensitivity Points / Missing Evidence
Closed Options and Why
Recommendation / Evidence Chain
Status
```

## Related

- `system-design`
- `architecture-decomposition`
- `architecture-evolution`
- `architecture-review`
- `capacity-planning`
- `slo-design`
- `adr`

## Leitgedanke

> Ein Trade-off ist eine bewusste Entscheidung zwischen relevanten Eigenschaften – keine Tabellenzeile mit Plus und Minus.