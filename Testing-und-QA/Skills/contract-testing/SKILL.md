---
name: contract-testing
description: Entwirft oder prüft Tests für die Kompatibilität zwischen Consumer und Provider an APIs, Events oder anderen Schnittstellen. Verwenden bei Breaking-Change-, Schema-, Payload- oder Consumer-Erwartungsrisiken. Nicht als vollständigen Functional- oder End-to-End-Test verwenden.
---

# Contract Testing

## Ziel

Beobachtbare Erwartungen an einer gemeinsamen Schnittstelle explizit und reproduzierbar verifizieren.

## Eingaben

- Consumer-Erwartungen;
- Provider-Schnittstelle;
- kanonische Spezifikation oder Schema, falls vorhanden;
- Versionierungs-/Kompatibilitätsregeln;
- reale verwendete Payloads/Events, sofern zulässig.

## Arbeitsweise

1. Consumer und Provider eindeutig bestimmen.
2. Vertrag auf tatsächlich benötigte Interaktionen begrenzen.
3. Request/Event, Response, Status-/Fehlersemantik und relevante Metadaten definieren.
4. Positive und relevante Fehlerinteraktionen abdecken.
5. Provider gegen den Contract verifizieren.
6. Prüfen, ob formale Schema-Kompatibilität semantische Änderungen übersieht.
7. Bei Änderungen Backward Compatibility und bestehende Consumer prüfen.
8. Contract-Drift sichtbar melden.

## Nicht tun

- gesamte fachliche Providerlogik im Contract nachtesten;
- alle möglichen Providerfeatures in einen Consumer-Contract ziehen;
- einen grün gemockten Consumer-Test als Provider-Verifikation ausgeben;
- neue Schnittstellenannahmen erfinden.

## Ausgabe

```text
Consumer
Provider
Contract Scope
Interaktionen
Kompatibilitätsrisiken
Verifikation
Drift / Breaking Changes
offene Consumer
```

## Related

- `integration-testing`
- `contract-change-review`
- `interface-review`
- Bereich `Schnittstellen-und-Vertraege/`