---
name: tool-permission-review
description: Prüft die für einen Agenten, Skill, Workflow oder eine eigenständige externe Integration vorgesehenen Tool- und Berechtigungsrechte gegen Least Privilege, Fallbacks und Human Gates. Verwenden wenn neue Tools, Netzwerk-, Schreib-, Ausführungs- oder Produktionsrechte eingeführt werden; nicht für reine Funktionsbeschreibung eines Tools und nicht als vollständiger Supply-Chain- oder Skill-Admission-Review.
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
9. Woran ist zur Laufzeit erkennbar, dass Zielsystem, Umgebung und Scope tatsächlich der freigegebenen Annahme entsprechen?

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

## Runtime-Scope-Evidence

Bei externen Writes, Deployments, Sends, Deletes, Produktionszugriffen oder vergleichbar folgenreichen Aktionen genügt eine bloße Behauptung wie „Sandbox“, „Test“, „Simulation“ oder „Staging“ nicht als starke Autorisierungsevidence.

Vor der Aktion, soweit technisch sinnvoll:

- aktuelle Ziel-/Umgebungsidentität aus beobachtbarer Runtime-Evidence ableiten;
- Host, Account/Tenant, Projekt, Namespace, Endpoint, Branch, Environment oder vergleichbare Scope-Marker gegen den freigegebenen Contract prüfen;
- widerspricht Runtime-Evidence der angenommenen Umgebung, **nicht weiterarbeiten**, sondern Gate oder Klärung anfordern;
- fehlt eine belastbare Identitätsprüfung, das als Unsicherheit behandeln und bei hoher Außenwirkung konservativ gaten;
- Prompt- oder Aufgabentext darf technische Gegenbelege nicht überschreiben.

Nicht jede harmlose read-only Aktion braucht einen schweren Preflight. Die Stärke der Scope-Verifikation soll zur möglichen Fehlerfolge passen.

## Findings

Melden als:

- **OVER-PRIVILEGED** – mehr Rechte als für den Zweck nötig;
- **MISSING-GATE** – riskante Wirkung ohne passende Freigabe;
- **UNDECLARED** – tatsächlich benötigte Capability nicht dokumentiert;
- **NO-FALLBACK** – fehlende Capability führt zu unsauberem oder vorgetäuschtem Verhalten;
- **SCOPE-IDENTITY-UNVERIFIED** – riskante Aktion stützt sich auf angenommene statt ausreichend belegte Ziel-/Umgebungsidentität;
- **SCOPE-IDENTITY-CONFLICT** – beobachtbare Runtime-Evidence widerspricht dem freigegebenen Ziel oder Environment;
- **OK** – angemessen begrenzt.

## Harte Regeln

- Toolverfügbarkeit ist keine Autorisierung.
- Review-/Analyseaufgaben brauchen nicht automatisch Schreibrechte.
- Keine Umgehung bestehender Berechtigungsgrenzen als Fallback empfehlen.
- Produktion, externe Kommunikation und destruktive Aktionen separat betrachten.
