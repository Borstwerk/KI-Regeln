# Workflow: Architekturentscheidung und Trade-off

## Ziel

Eine schwer umkehrbare Architekturentscheidung mit mehreren ernsthaften Optionen nachvollziehbar vergleichen und dokumentieren.

## Ablauf

```text
1. Decision Scope
→ 2. bestätigte Drivers / Constraints
→ 3. viable Kandidaten
→ 4. Quality-Szenarien / Failure Modes
→ 5. Trade-off-Analyse
→ 6. Recommendation / Sensitivity Points
→ 7. Review
→ 8. ADR-Handoff
```

## Skills

- `architecture-baseline` bei bestehendem System;
- `architecture-tradeoff-analysis` als Kern;
- `system-design`, wenn Kandidaten erst strukturell ausgearbeitet werden müssen;
- `architecture-review` für unabhängigen Gegencheck;
- `adr` für dauerhafte Entscheidungsdokumentation.

### Routing-Vertrag

Wenn dieser Workflow gewählt wird, ist `architecture-tradeoff-analysis` der verpflichtend zu prüfende Kernkandidat. Seine `SKILL.md` muss gelesen werden, bevor ein generischer Entscheidungs- oder Vergleichsskill an seine Stelle tritt.

Ein benachbarter Skill darf den Kern nur ersetzen, wenn die kanonische Description oder Near-Miss-Grenze von `architecture-tradeoff-analysis` den konkreten Auftrag ausschließt. Ein bloß allgemeineres „Optionen vergleichen“ ist kein ausreichender Ersatzgrund.

## Regeln

- Keine Alternativen erfinden, die Requirements bereits ausschließen.
- Keine undurchsichtige Gesamtnote als Entscheidungsersatz.
- Missing Evidence kann ein `CONDITIONAL` oder `UNVERIFIED` erzwingen.
- Die Entscheidung autorisiert keine Migration oder Produktionseinwirkung.

## Ergebnis

Eine begründete Entscheidung mit Trade-offs, Sensitivity Points, geschlossenen Optionen und klarer Evidence Chain.