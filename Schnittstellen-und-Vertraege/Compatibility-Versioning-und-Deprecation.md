# Compatibility, Versioning und Deprecation

## Mehrdimensionale Compatibility

### Source Compatibility

Alter Consumercode kann gegen neue Contract-/Clientdefinitionen weiter gebaut und ausgeführt werden.

### Wire Compatibility

Alt und neu können weiterhin korrekt serialisieren, übertragen und deserialisieren.

### Semantic Compatibility

Ein bestehender Consumer beobachtet weiterhin eine vernünftigerweise erwartbare Bedeutung.

Keine Dimension ersetzt die anderen.

## Change Verdicts

### COMPATIBLE

Die Änderung ist unter den bekannten Consumer- und Deploymentbedingungen rückwärtskompatibel.

### ROLLOUT-SENSITIVE

Die Änderung kann funktionieren, benötigt aber kontrollierte Reihenfolge, Feature-Nutzung, Wertebereich, Consumerupgrade oder andere Rolloutbedingungen.

### BREAKING

Mindestens ein bekannter bestehender Consumer kann nicht mehr bauen, kommunizieren oder dieselbe Bedeutung beobachten.

### UNVERIFIED

Baseline, Consumerinventar, Tooling oder Semantik reichen für eine sichere Klassifikation nicht aus.

## Additiv ist nur der Anfang der Prüfung

Neue optionale Felder, neue Endpoints oder neue Schemaelemente sind häufig kompatibel. Aber Defaults, Enums, Ordering, Pagination, Limits oder unbekannte Werte können alte Consumer trotzdem brechen.

> Additive Syntax ≠ bewiesene semantische Compatibility.

## Consumer Deployment zählt

Eine intern koordinierte Schnittstelle kann andere Evolutionregeln haben als eine öffentliche API mit unbekannten Consumer-Releases. „Intern“ ist jedoch kein Freibrief für stille Breaking Changes.

## Versionierung

Keine universelle zentrale Regel für `/v1`, Header, Datumsversionen oder SemVer.

Erforderlich ist stattdessen:

- definierte Compatibility Policy;
- klarer Versions-/Stabilitätsbegriff, wenn Versionen verwendet werden;
- eindeutige Baseline;
- Migration bei Breaking Changes;
- nachvollziehbare Consumer-Kommunikation.

## Deprecation Lifecycle

```text
ACTIVE
→ DEPRECATED
→ MIGRATION WINDOW
→ SUNSET
→ REMOVED
```

Deprecated bedeutet nicht entfernt.

Für HTTP existiert mit RFC 9745 ein standardisierter `Deprecation`-Header; `Sunset` und Links können den Lifecycle ergänzen.

## Removal Gate

Vor Removal mindestens prüfen:

- bekannte Consumer;
- Nutzung/Telemetry, falls verfügbar;
- dokumentierte Migration;
- vereinbarte Frist oder Policy;
- Contract Tests / Compatibility Checks;
- explizite lokale Freigabe.

## Leitgedanke

> Die gefährlichsten Breaking Changes ändern nicht immer das Schema – manchmal ändern sie nur die Bedeutung.