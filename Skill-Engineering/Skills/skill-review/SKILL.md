---
name: skill-review
description: Prüft einen bestehenden Agent-Skill unabhängig auf Skill-Schnitt, Triggerqualität, Near-Misses, Input-/Outputvertrag, Capabilities, Fallbacks, Komposition, Sicherheit, Evalbarkeit und Lifecycle. Verwenden bei Review oder Freigabe einer SKILL.md; nicht als automatischer Rewrite des geprüften Skills.
---

# Skill Review

## Rolle

Prüfe den Skill, ohne seine eigene Selbstbeschreibung als Qualitätsbeweis zu übernehmen.

## Reviewachsen

### 1. Verantwortung

- Ist die Arbeitsdisziplin klar begrenzt?
- Dupliziert der Skill einen bestehenden Skill?
- enthält er lokale Projektwahrheit?
- wäre ein Workflow statt eines größeren Skills sinnvoller?

### 2. Trigger

- beschreibt `description` Aufgabe und Einsatzsituation?
- triggert der Skill bei typischen Paraphrasen?
- gibt es plausible Near-Misses, die er fälschlich kapern würde?

### 3. Inputs / Outputs

- sind Pflichtinformationen erkennbar?
- kann fehlende Information zu Halluzination führen?
- ist ein prüfbares Ergebnis definiert?
- ist Evidence erforderlich, wo sie möglich ist?

### 4. Capabilities / Rechte

- sind Toolannahmen transparent?
- existieren Fallbacks?
- werden Rechte nach Least Privilege gewählt?
- behauptet der Skill Fähigkeiten, die eine Laufzeit nicht garantiert?

### 5. Prozess und Gates

- sind Stop-/Eskalationsbedingungen vorhanden?
- unterscheidet der Skill Durchführung und Erfolg?
- verhindert er Scope Creep?

### 6. Komposition

- sind Related, Precondition und Follow-up sauber getrennt?
- startet der Skill versteckt weitere Aufgaben?
- gibt es zyklische oder unnötig harte Abhängigkeiten?

### 7. Progressive Disclosure

- ist `SKILL.md` der operative Kern statt Wissensarchiv?
- könnten lange Spezialdetails in `references/` ausgelagert werden?
- wären deterministische Checks als `scripts/` robuster?

### 8. Evals

Prüfe, ob mindestens folgende Testklassen möglich bzw. vorhanden sind:

- positiver Trigger;
- paraphrasierter Trigger;
- Near-Miss-Negativfall;
- fehlende Capability;
- fehlende Pflichtinformation;
- schwieriger fachlicher Fall.

### 9. Lifecycle

- passt die angegebene Maturity zur vorhandenen Praxis und Evalabdeckung?
- gibt es bei Deprecation einen Ersatz-/Migrationsweg?

## Ausgabe

Funde priorisieren als:

- **BLOCKER** – unsicher, widersprüchlich, falscher Scope oder nicht prüfbar;
- **MAJOR** – relevante Trigger-/Vertrags-/Fallback-/Evalschwäche;
- **MINOR** – begrenzte Qualitätsverbesserung;
- **NIT** – rein redaktionell.

Danach:

- Freigabeurteil: `pass`, `pass-with-followups` oder `fail`;
- empfohlene Maturity;
- fehlende Evalfälle.

## Regel

Nicht automatisch umschreiben. Erst Befund und Wirkung benennen; Änderungen erfolgen im normalen Freigabeprozess.
