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

### 5. Portabilität / Runtime-Adapter

- ist die fachliche Disziplin unabhängig vom konkreten Client verständlich?
- stehen Modellwahl, konkrete Toolnamen, Turn-Limits, Isolation oder Hostmechanik unnötig im Kern?
- ist ein modellspezifischer Workaround fälschlich zur allgemeinen Regel geworden?
- erhalten Adapter die fachlichen Sicherheits-, Scope- und Human-Gates?

### 6. Freiheitsgrad und Determinismus

- passt der Instruktionsgrad je wesentlichem Schritt zu Variabilität, Fragilität und Fehlerfolge?
- ist ein kreativer oder kontextabhängiger Schritt unnötig überbestimmt?
- ist ein fragiler Schritt zu frei formuliert, obwohl Script, Check oder enger Vertrag robuster wäre?
- werden Human-/Safety-Gates unabhängig vom Freiheitsgrad erhalten?

### 7. Prozess und Gates

- sind Stop-/Eskalationsbedingungen vorhanden?
- unterscheidet der Skill Durchführung und Erfolg?
- verhindert er Scope Creep?

### 8. Komposition

- sind Related, Precondition und Follow-up sauber getrennt?
- startet der Skill versteckt weitere Aufgaben?
- gibt es zyklische oder unnötig harte Abhängigkeiten?

### 9. Progressive Disclosure

- ist `SKILL.md` der operative Kern statt Wissensarchiv?
- bleibt der Body als praktische Heuristik möglichst unter ungefähr 500 Zeilen?
- könnten lange Spezialdetails in `references/` ausgelagert werden?
- besitzen Referenz-/Fachdokumente über ungefähr 100 Zeilen ein Inhaltsverzeichnis oder eine begründete Navigationsausnahme?
- sind für die Ausführung wichtige Referenzen direkt aus `SKILL.md` erreichbar statt nur über tiefe Referenzketten?
- wären deterministische Checks als `scripts/` robuster?
- deklarieren Scripts Runtime-/Package-/Toolabhängigkeiten und einen ehrlichen Fallback?

### 10. Evals

Prüfe, ob mindestens folgende Testklassen möglich bzw. vorhanden sind:

- positiver Trigger;
- paraphrasierter Trigger;
- Near-Miss-Negativfall;
- fehlende Capability;
- fehlende Pflichtinformation;
- schwieriger fachlicher Fall.

Zusätzlich bei mehreren beabsichtigten Modell-/Runtime-Zielen:

- ist sichtbar, welche Kombinationen tatsächlich ausgeführt wurden?
- bleiben nicht getestete Ziele `NOT RUN`/`UNVERIFIED`?
- wird ein einzelner erfolgreicher Lauf nicht als allgemeine Cross-Model-Evidence ausgegeben?
- wurde bei relevanten Skilländerungen – sofern reproduzierbar – gegen eine Kontrollbedingung ohne Skill oder gegen den bisherigen Skillstand verglichen?
- sind Instruktionsqualität (Skill sicher aktiv) und Discovery/Trigger (natürliche Auswahl) getrennt geprüft?
- ist ein behaupteter Qualitätsgewinn als beobachtbares Delta belegt statt nur durch einen grünen Einzellauf?

### 11. Release- und Evidence-Bindung

Wenn der Review eine Freigabe oder Veröffentlichung tragen soll:

- ist eindeutig, **welcher Skillstand** fachlich reviewed wurde?
- entspricht der evaluierte Stand dem reviewed Stand?
- entspricht der zur Freigabe vorgesehene Stand wiederum diesem Stand?
- umfasst die Bindung neben `SKILL.md` auch verhaltensrelevante Scripts, References, Assets und Konfigurationen?
- werden Änderungen nach Review/Eval als neue Evidence-Pflicht behandelt statt still von der alten Freigabe abgedeckt?
- ist bei höherem Assurance-Bedarf ein reproduzierbarer Bundle-Fingerprint, Manifest oder vergleichbare Integritätsbindung sinnvoll?

Ein Release- oder Skill-Card-Artefakt kann Reviewzustand, Evalstand, geprüfte Capabilities, bekannte Grenzen und Bundle-Identität zusammenfassen. Das ist eine Dokumentationsoption, keine Pflicht zu einem bestimmten Vendorformat oder Signaturverfahren.

### 12. Lifecycle

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
