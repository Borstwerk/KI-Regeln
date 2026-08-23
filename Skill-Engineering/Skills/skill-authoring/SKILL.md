---
name: skill-authoring
description: Entwirft oder überarbeitet einen wiederverwendbaren Agent-Skill mit klarer Verantwortung, Triggerlogik, Inputs/Outputs, Capabilities, Fallbacks und prüfbarem Ergebnis. Verwenden wenn ein neuer SKILL.md entstehen oder ein bestehender Skill strukturell verbessert werden soll; nicht für projektspezifische Anweisungen, die nur lokal gelten.
---

# Skill Authoring

## Ziel

Erzeuge einen kleinen, klar verantworteten Skill, der zuverlässig aktiviert, portabel ausführbar und unabhängig prüfbar ist.

## Ablauf

1. **Bedarf klären**
   - Welche wiederkehrende Arbeitsdisziplin soll der Skill abdecken?
   - Warum reicht keine bestehende Regel oder kein vorhandener Skill?

2. **Grenze setzen**
   - eine Verantwortung definieren;
   - angrenzende Aufgaben und Near-Misses benennen;
   - Projektwahrheit entfernen oder lokal belassen.

3. **Trigger entwerfen**
   - `name` kompakt und kebab-case;
   - `description` beschreibt Aufgabe und Einsatzsituation;
   - mindestens zwei positive Triggerfälle und zwei Near-Miss-Negatives gedanklich prüfen.

4. **Vertrag definieren**
   - required / preferred / discoverable Inputs;
   - erwarteter Output;
   - Evidence und Abschlussstatus;
   - Stop-/Eskalationsbedingungen.

5. **Capabilities definieren**
   - benötigte Fähigkeiten;
   - optionale Fähigkeiten;
   - Fallbacks;
   - keine unnötigen Rechte.

6. **Struktur wählen**
   - operativer Kern in `SKILL.md`;
   - lange Details in `references/`;
   - deterministische Arbeit ggf. in `scripts/`;
   - Templates/Ressourcen ggf. in `assets/`.

7. **Komposition prüfen**
   - Related / Precondition / Follow-up unterscheiden;
   - keine versteckte Workflow-Orchestrierung einbauen.

8. **Review- und Evalplan ergänzen**
   - Trigger-Positives;
   - Near-Miss-Negatives;
   - fehlende Capability;
   - schwieriger Fall;
   - erwartete Behavior-/Outcome-Kriterien.

9. **Maturity setzen**
   - neue Skills starten standardmäßig `experimental`, sofern keine belastbare Praxis eine höhere Einstufung rechtfertigt.

## Harte Regeln

- Keine projektspezifische Wahrheit als allgemeine Skillregel erfinden.
- Fehlende Capability nicht simulieren oder behaupten.
- Keine unnötigen externen Schreib-/Ausführungsrechte verlangen.
- Kein Skill-Monster bauen, wenn ein Workflow mehrere unabhängige Skills verbinden sollte.
- Keine bestehende Skillverantwortung nur unter neuem Namen duplizieren.

## Ergebnis

Mindestens:

- gültiger Skillname;
- klare Description;
- kompakter `SKILL.md`-Entwurf;
- bekannte Near-Misses;
- Capability-/Fallback-Hinweise;
- Evalkandidaten;
- vorgeschlagene Maturity.

## Relevante Regeln

- `../../Skill-Schnitt-und-Verantwortung.md`
- `../../Skill-Struktur-und-Progressive-Disclosure.md`
- `../../Trigger-und-Description-Design.md`
- `../../Inputs-Outputs-und-Vertraege.md`
- `../../Toolanforderungen-und-Fallbacks.md`
- `../../Skill-Komposition-und-Abhaengigkeiten.md`
- `../../Skill-Review-und-Evals.md`
- `../../Skill-Lifecycle-und-Deprecation.md`
