# Skill Engineering

Dieser Bereich beschreibt, wie wiederverwendbare KI-Skills entworfen, strukturiert, geprüft, kombiniert und über ihren Lebenszyklus gepflegt werden.

## Grundsatz

> Ein Skill ist eine begrenzte Arbeitsdisziplin mit klarer Aktivierungslogik, klaren Grenzen und überprüfbarem Ergebnis.

Ein guter Skill soll:

- genau genug triggern, ohne angrenzende Aufgaben zu kapern;
- nur den Kontext laden, den er wirklich braucht;
- Anforderungen und lokale Projektwahrheit nicht ersetzen;
- benötigte Fähigkeiten und Fallbacks transparent machen;
- ein prüfbares Ergebnis erzeugen;
- mit anderen Skills kombinierbar bleiben;
- unabhängig review- und evaluierbar sein;
- einen nachvollziehbaren Lifecycle besitzen.

## Dateien

- `Skill-Schnitt-und-Verantwortung.md` – wann etwas ein eigener Skill sein sollte;
- `Skill-Struktur-und-Progressive-Disclosure.md` – Aufbau und kontextsparende Struktur;
- `Trigger-und-Description-Design.md` – Aktivierungslogik und Near-Miss-Abgrenzung;
- `Inputs-Outputs-und-Vertraege.md` – erwartete Eingaben, Ausgaben und Evidence;
- `Toolanforderungen-und-Fallbacks.md` – Capabilities, Rechte und degradierte Betriebsmodi;
- `Skill-Komposition-und-Abhaengigkeiten.md` – Beziehungen zwischen Skills;
- `Skill-Review-und-Evals.md` – Review- und Evaluationsregeln;
- `Skill-Lifecycle-und-Deprecation.md` – Reife, Änderung und Ablösung;
- `Evidence-getriebene-Skill-Verbesserung.md` – kontrollierte Verbesserung aus Failure-/Eval-Evidence ohne autonome Selbstfreigabe;
- `Quellen-und-Inspirationen.md` – externe Grundlagen und Abgrenzung;
- `Skills/skill-authoring/SKILL.md` – operativer Skill zum Erstellen/Überarbeiten von Skills;
- `Skills/skill-review/SKILL.md` – unabhängiger Review eines Skills.

## Empfohlener Prozess

```text
Bedarf erkennen
→ Skill-Grenze bestimmen
→ Trigger und Near-Misses definieren
→ Inputs / Outputs / Evidence festlegen
→ Capabilities + Fallbacks definieren
→ SKILL.md kompakt schreiben
→ References / Scripts nur bei Bedarf ergänzen
→ Review
→ Evals
→ Maturity festlegen
→ veröffentlichen / verwenden
→ beobachten
→ Failure-/Eval-Evidence bei Bedarf kontrolliert auswerten
→ weiterentwickeln / deprecaten
```

## Leitgedanke

> Gute Skills machen Agenten nicht nur fähiger, sondern ihr Verhalten vorhersagbarer und prüfbarer.
