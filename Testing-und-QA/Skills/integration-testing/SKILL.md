---
name: integration-testing
description: Plant oder prüft Tests für das reale Zusammenspiel mehrerer Komponenten oder technischer Grenzen. Verwenden bei Datenbank-, Broker-, Dateisystem-, Framework-, Adapter- oder Service-Integration. Nicht für reine Fachlogik oder vollständige Nutzerflows verwenden.
---

# Integration Testing

## Ziel

Reales Integrationsverhalten mit kontrollierter, reproduzierbarer Umgebung prüfen.

## Arbeitsweise

1. Konkrete Integrationsgrenze und Risiko benennen.
2. Entscheiden, welches reale Verhalten Teil des Testziels ist.
3. Nur nicht relevante oder unerwünschte Dependencies durch geeignete Doubles ersetzen.
4. Reale Dependencies möglichst kurzlebig und isoliert bereitstellen.
5. Ausgangszustand / Testdaten deterministisch herstellen.
6. Erfolgs- und relevante Fehlerpfade testen.
7. Cleanup und Parallelisierbarkeit prüfen.
8. Evidence und Umgebung/Version dokumentieren.

## Entscheidung Double vs. real

```text
Ist das Verhalten der Dependency Teil des Risikos?
├─ ja → reale / realitätsnahe Dependency bevorzugen
└─ nein → kontrolliertes Double kann geeigneter sein
```

Zusätzlich Kosten, Sicherheit, Rate Limits, Determinismus und Verfügbarkeit berücksichtigen.

## Regeln

- In-Memory-Ersatz nicht als Beweis für Verhalten einer anderen Produktionsengine ausgeben;
- gemeinsam genutzte Testsysteme nicht als automatisch isoliert betrachten;
- keine externen produktiven Seiteneffekte auslösen;
- wenn Doubles reale Contracts behaupten, Drift separat absichern.

## Related

- `contract-testing`
- `failure-testing`
- `database-query-review`
- `schema-migration`