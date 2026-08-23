---
name: tool-permission-review
description: Prüft die für einen Agenten, Skill oder Workflow vorgesehenen Tool- und Berechtigungsrechte gegen Least Privilege, Fallbacks und Human Gates. Verwenden wenn neue Tools, Netzwerk-, Schreib-, Ausführungs- oder Produktionsrechte eingeführt werden; nicht für reine Funktionsbeschreibung eines Tools.
---

# Tool Permission Review

## Inputs

- Aufgabe / Skillzweck;
- gewünschte Tools oder Capabilities;
- vorgesehene Rechte;
- bekannte Fallbacks;
- lokale Human Gates.

## Ablauf

Für jede Capability:

1. Welche konkrete Aufgabe benötigt sie?
2. Reicht eine schwächere Capability?
3. Ist sie `required`, `optional` oder nur für einen Sonderfall nötig?
4. Welche Daten kann sie lesen?
5. Welche Änderungen oder Außenwirkungen kann sie erzeugen?
6. Kann sie zeitlich oder räumlich weiter eingeschränkt werden?
7. Was passiert, wenn sie fehlt?
8. Welches Gate gilt vor riskanter Nutzung?

## Prüfmatrix

```text
Capability
→ Zweck
→ minimale Rechte
→ Datenzugriff
→ Außenwirkung
→ Fallback
→ Gate
```

## Findings

Melden als:

- **OVER-PRIVILEGED** – mehr Rechte als für den Zweck nötig;
- **MISSING-GATE** – riskante Wirkung ohne passende Freigabe;
- **UNDECLARED** – tatsächlich benötigte Capability nicht dokumentiert;
- **NO-FALLBACK** – fehlende Capability führt zu unsauberem oder vorgetäuschtem Verhalten;
- **OK** – angemessen begrenzt.

## Harte Regeln

- Toolverfügbarkeit ist keine Autorisierung.
- Review-/Analyseaufgaben brauchen nicht automatisch Schreibrechte.
- Keine Umgehung bestehender Berechtigungsgrenzen als Fallback empfehlen.
- Produktion, externe Kommunikation und destruktive Aktionen separat betrachten.
