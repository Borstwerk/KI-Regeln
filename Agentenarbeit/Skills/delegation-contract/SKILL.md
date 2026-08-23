---
name: delegation-contract
description: Definiert vor relevanter Agentenarbeit Ziel, Scope, Rechte, Quellen, Akzeptanzbedingungen und geforderte Evidence und prüft anschließend das Evidence Bundle.
---

# Delegation Contract

Dieser Skill nutzt `../../Delegation-und-Evidence.md`.

## Vor der Delegation

Für nicht triviale Agentenarbeit klären:

1. **Ziel** – welcher beobachtbare Zustand soll erreicht werden?
2. **Scope** – was darf verändert werden und was ausdrücklich nicht?
3. **Quellen der Wahrheit** – welche Anforderungen, Entscheidungen, Dokumente oder Tests sind verbindlich?
4. **Befugnisse** – welche Tools und Aktionen sind erlaubt?
5. **Ergebnis** – welches Artefakt wird erwartet?
6. **Akzeptanzbedingungen** – woran ist Erfolg prüfbar?
7. **Evidence** – welche Nachweise müssen zurückkommen?
8. **Stop-Bedingungen** – wann muss der Agent eskalieren statt weiterarbeiten?
9. **Abnahmekontext** – wer oder was prüft den Ausgang?

## Während der Arbeit

- Scope nicht eigenmächtig erweitern.
- Neue Architektur- oder Produktentscheidungen nicht stillschweigend treffen.
- Fehlenden Kontext sichtbar machen.
- Evidence während der Arbeit sammeln statt nachträglich zu erfinden.
- Nicht behaupten, eine Prüfung sei bestanden, wenn sie nicht ausgeführt werden konnte.

## Evidence Bundle

Am Ende mindestens liefern:

- Ergebnis;
- tatsächlichen Scope beziehungsweise geänderte Artefakte;
- ausgeführte Tests und Prüfungen samt Status;
- Zuordnung wichtiger Akzeptanzkriterien zu Nachweisen;
- Abweichungen vom Contract oder Plan;
- offene Prüfungen;
- verbleibende Risiken und Unsicherheiten.

## Übergabe

Bei einem nachfolgenden Agentenknoten nur bestätigten Zustand, relevante Artefakte und offene Unsicherheiten übergeben.

Keine komplette Denkgeschichte als Ersatz für kanonische Projektdokumentation verwenden.

## Stop

Sofort stoppen oder Gate anfordern, wenn:

- der notwendige Repair außerhalb des Scopes liegt;
- eine neue Architekturentscheidung nötig wird;
- Quellen widersprüchlich sind;
- erforderliche Rechte oder Prüfungen fehlen;
- ein Verification Loop keinen belastbaren Fortschritt mehr erzeugt.

## Leitgedanke

> Ein guter Auftrag begrenzt die Arbeit. Gute Evidence macht sie abnehmbar.