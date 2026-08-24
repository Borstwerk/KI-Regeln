---
name: deployment-strategy
description: Plant oder prüft eine kontrollierte Softwareauslieferung mit Rolling, Blue-Green, Canary, Shadow, Recreate oder Feature-gated Release einschließlich Promotion, Pause, Abort und Rollback. Verwenden bei riskanten Releases oder Zero-/Low-Downtime-Fragen. Nicht zur Erfindung von SLO-/Health-Schwellen verwenden.
---

# Deployment Strategy

## Ziel

Den Blast Radius einer Änderung kontrollieren und vor vollständiger Freigabe belastbare Health-/Business-Evidence gewinnen.

## Eingaben

- Artifact/Version;
- Zielumgebung;
- Reversibilität;
- Daten-/Contract-Kompatibilität;
- verfügbare Routing-/Flag-/Rolloutmechanik;
- lokale Health-/SLO-/Produktkriterien.

## Arbeitsweise

1. Build, Deploy und Release voneinander trennen.
2. Risiko, Blast Radius und Reversibilität bestimmen.
3. Versionsüberlappung und Kompatibilität prüfen.
4. passende Strategie wählen und begründen.
5. Promotion/Pause/Abort-Signale definieren; Schwellen aus lokaler Policy übernehmen.
6. Rollbackpfad und nicht rückgängig machbare Nebenwirkungen nennen.
7. lokale Deploy-/Release-Gates explizit halten.
8. Fresh Evidence nach jeder relevanten Stufe verlangen.

## Nicht tun

- Canary/Blue-Green pauschal erzwingen;
- Health-Schwellen erfinden;
- Rollback als Undo von Migrationen/Events/externer Wirkung darstellen;
- Deployfreigabe aus Build-/Testgrün ableiten;
- reale Deploymentaktion ohne Autorisierung ausführen.

## Ausgabe

```text
Strategy
Risk / Blast Radius
Compatibility
Promotion Criteria
Pause / Abort
Rollback
Non-reversible Effects
Required Evidence
Gates
```

## Related

- `infrastructure-change-review`
- `contract-change-review`
- `schema-migration`
- `failure-testing`
- `verification-loop`