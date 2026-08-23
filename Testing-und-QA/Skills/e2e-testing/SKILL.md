---
name: e2e-testing
description: Entwirft oder führt ausgewählte End-to-End-Tests für wichtige Nutzer- oder Geschäftsflows über mehrere Systemgrenzen aus. Verwenden, wenn kleinere Testebenen das relevante Gesamtrisiko nicht zuverlässig abdecken. Nicht für visuelle Detailprüfung oder jede einzelne Fachregel verwenden.
---

# End-to-End Testing

## Ziel

Kritische Gesamtflows aus beobachtbarer Nutzer-/Geschäftsperspektive prüfen.

## Voraussetzungen

Möglichst bekannt:

- Flow und erwartetes Ergebnis;
- relevante Rollen / Berechtigungen;
- Testumgebung;
- Testdaten;
- benötigte Browser-/Client-/System-Capabilities;
- erlaubte externe Aktionen.

## Arbeitsweise

1. Kritischen Flow und zu prüfendes Risiko benennen.
2. Prüfen, ob kleinere Testebenen geeigneter sind; E2E nur für zusätzliche Gesamtevidence verwenden.
3. Reproduzierbaren Ausgangszustand herstellen.
4. Über nutzersichtbare oder ausdrücklich zugesicherte Schnittstellen interagieren.
5. Auf beobachtbare Zustände statt feste Sleeps synchronisieren.
6. Fachliches Endergebnis verifizieren.
7. Relevante Fehlerklasse ergänzen, wenn sie nur im Gesamtflow sichtbar ist.
8. Diagnoseartefakte sichern, soweit zulässig.
9. Testdaten / Seiteneffekte sauber zurücksetzen oder verwerfen.

## Regeln

- fragile Implementierungsdetails vermeiden;
- E2E-Anzahl bewusst begrenzen;
- produktive Systeme nur mit expliziter lokaler Autorisierung verwenden;
- UI-funktional grün ≠ visuell verifiziert;
- Third-Party-Mocking nicht pauschal, sondern nach Risiko-/Seam-Regeln entscheiden.

## Related

- `visual-verification`
- `integration-testing`
- `failure-testing`