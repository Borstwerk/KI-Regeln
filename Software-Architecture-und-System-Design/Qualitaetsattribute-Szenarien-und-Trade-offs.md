# Qualitätsattribute, Szenarien und Trade-offs

## Zweck

Quality Attributes beeinflussen Architektur nur dann belastbar, wenn sie als konkrete Szenarien und nicht als abstrakte Wünsche formuliert werden.

## Szenariomodell

Angelehnt an scenario-based architecture analysis:

```text
Source / Actor
→ Stimulus
→ Environment
→ betroffener Architekturteil
→ Response
→ Response Measure / beobachtbares Ergebnis
```

Beispiele können Availability, Performance, Modifiability, Security, Recoverability, Scalability, Operability oder Cost betreffen.

## Trade-offs

Architekturentscheidungen optimieren selten alle Eigenschaften gleichzeitig.

Typische Spannungen:

- Konsistenz vs. Verfügbarkeit / Koordination;
- geringe Latenz vs. stärkere Durability oder Synchronisation;
- Failure Isolation vs. verteilte Betriebs- und Contractkosten;
- Flexibilität vs. einfache, enge öffentliche Oberfläche;
- unabhängige Deployments vs. Integrations- und Observability-Aufwand;
- Vorab-Abstraktion vs. einfache lokale Änderung;
- Kostenreserve vs. Capacity Headroom.

Ein Trade-off ist nicht automatisch schlecht. Er muss sichtbar, akzeptiert und an echte Drivers gebunden sein.

## Sensitivity Points

Kennzeichnen, welche Annahmen oder Zielwerte die Entscheidung kippen könnten.

Beispiel:

```text
Wenn Peak-Last < X bleibt
→ Kandidat A ausreichend

Wenn nachgewiesene Isolation / Independent Scaling nötig wird
→ Kandidat B neu bewerten
```

X darf nicht erfunden werden; fehlende Schwellen bleiben lokale offene Evidence.

## Kandidatenvergleich

Nur strukturell echte Alternativen vergleichen. Kein Design B erfinden, wenn ein Requirement oder eine Invariante es bereits ausgeschlossen hat.

Für jeden Kandidaten:

- stärkste Vorteile gegenüber den relevanten Szenarien;
- ehrliche Schwäche;
- neue Failure Modes;
- Betriebs-/Migrationskosten;
- Annahmen und Missing Evidence;
- Messung oder Ereignis, das die Empfehlung ändern würde.

Keine undurchsichtigen Gesamtscores als Ersatz für Begründung verwenden.

## Leitgedanke

> Architekturqualität entsteht nicht durch maximale Punktzahl, sondern durch bewusst akzeptierte Trade-offs gegenüber echten Szenarien.