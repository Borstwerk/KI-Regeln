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

5. **Capabilities und Runtime-Grenze definieren**
   - benötigte Fähigkeiten;
   - optionale Fähigkeiten;
   - Fallbacks;
   - keine unnötigen Rechte;
   - eine fachliche Capability nicht unnötig an eine konkrete Plugin-/App-Marke binden;
   - berücksichtigen, dass dieselbe Capability nativ, über ein verbundenes Plugin/eine App oder über einen Fallback erfüllt werden kann;
   - externe READ-, WRITE- und ACTION-Wirkung getrennt betrachten;
   - fachlichen Skill-Kern von Modell-, Tool-, Turn-, Isolation- oder Clientkonfiguration trennen;
   - runtime-spezifische Einstellungen in Adapter oder klar gekapselte Metadaten auslagern, sofern die Plattform nicht selbst Gegenstand des Skills ist.

6. **Freiheitsgrad je Arbeitsschritt wählen**
   - hoher Freiheitsgrad für kontextabhängige Aufgaben mit mehreren gültigen Wegen;
   - mittlerer Freiheitsgrad für bevorzugte Templates/Pseudocode mit erlaubter Variation;
   - niedriger Freiheitsgrad für fragile, folgenreiche oder reproduzierbare Schritte;
   - wenn exakt gleiches Verhalten nötig ist, Script/Check statt immer mehr Prompttext bevorzugen.

7. **Struktur wählen**
   - operativer Kern in `SKILL.md`, als praktische Heuristik möglichst unter 500 Zeilen Body;
   - lange Details in `references/`;
   - Referenz-/Fachdokumente über ungefähr 100 Zeilen mit Inhaltsverzeichnis oder begründeter Navigationsausnahme;
   - benötigte Referenzen möglichst direkt aus `SKILL.md` erreichbar machen;
   - deterministische Arbeit ggf. in `scripts/`;
   - für Scripts Runtime, Packages/Tools, Availability Check und Fallback als Dependency Contract festhalten;
   - Templates/Ressourcen ggf. in `assets/`.

8. **Komposition prüfen**
   - Related / Precondition / Follow-up unterscheiden;
   - keine versteckte Workflow-Orchestrierung einbauen.

9. **Review- und Evalplan ergänzen**
   - Trigger-Positives;
   - Near-Miss-Negatives;
   - fehlende Capability;
   - schwieriger Fall;
   - erwartete Behavior-/Outcome-Kriterien;
   - tatsächlich vorgesehene Modell-/Runtime-Ziele benennen und Run-Evidence dort binden, nicht als allgemeine fachliche Frontmatter-Pflicht.

10. **Maturity setzen**
   - neue Skills starten standardmäßig `experimental`, sofern keine belastbare Praxis eine höhere Einstufung rechtfertigt.

## Harte Regeln

- Keine projektspezifische Wahrheit als allgemeine Skillregel erfinden.
- Fehlende Capability nicht simulieren oder behaupten.
- Keine unnötigen externen Schreib-/Ausführungsrechte verlangen.
- Kein Skill-Monster bauen, wenn ein Workflow mehrere unabhängige Skills verbinden sollte.
- Keine bestehende Skillverantwortung nur unter neuem Namen duplizieren.
- Keine vendor-/modell-spezifischen Runtime-Defaults als allgemeine Skillwahrheit festschreiben.
- Einen Workaround für ein einzelnes Modell nicht als allgemeine Prozessregel konservieren, wenn eine Adapterlösung oder eine allgemeinere Invariante ausreicht.
- Fehlende Script-Packages oder Tools nicht automatisch installieren; Verfügbarkeit, Runtime-Rechte und Fallback zuerst prüfen.
- Cross-Model-Kompatibilität nicht aus einem einzelnen erfolgreichen Modelllauf ableiten.

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
- `../../Portabler-Skill-Kern-und-Runtime-Adapter.md`
- `../../Skill-Komposition-und-Abhaengigkeiten.md`
- `../../Skill-Review-und-Evals.md`
- `../../Skill-Lifecycle-und-Deprecation.md`
