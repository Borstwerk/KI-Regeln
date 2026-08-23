# Entropie und Garbage Collection

## Zweck

Agenten lernen stark aus vorhandenen Mustern einer Codebasis. Gute Muster werden dadurch verstärkt – schlechte leider ebenfalls.

Entropiemanagement beschreibt die bewusste Pflege eines Repositories, damit Inkonsistenzen, Doppelstrukturen und provisorische Muster nicht schleichend zur Vorlage für weitere Agentenarbeit werden.

## Grundprinzip

> Der aktuelle Repository-Zustand ist Trainingsmaterial für den nächsten Agentenlauf.

Wenn ein schlechter Workaround dreimal vorhanden ist, kann der nächste Agent ihn als etabliertes Muster interpretieren. Deshalb gehört kontrollierte Pflege zur Agentenstrategie.

## Typische Formen von Drift

Beispiele:

- mehrere unterschiedliche Wege für dieselbe fachliche Operation;
- doppelte Validierungslogik;
- wachsende Zahl ähnlicher Helper oder Manager;
- veraltete Adapter, die neue Implementierungen trotzdem kopieren;
- widersprüchliche Namenskonventionen;
- tote Feature-Flags;
- Dokumentation, die nicht mehr zum Code passt;
- Tests, die nur noch die alte Architektur absichern;
- temporäre Workarounds ohne klaren Abbaupfad;
- parallele Abstraktionen für dieselbe Verantwortung.

## Golden Principles

Für wiederkehrende Architektur- und Qualitätsregeln können wenige klare Prinzipien definiert werden.

Beispiele:

- eine fachliche Wahrheit hat eine kanonische Quelle;
- neue Abhängigkeiten benötigen einen konkreten Nutzen;
- Persistenzverträge werden nicht beiläufig verändert;
- öffentliche Schnittstellen bleiben klein und bewusst;
- Validierung wird nicht dupliziert, wenn eine zentrale Regel existiert;
- temporäre Ausnahmen besitzen einen erkennbaren Abbaupfad.

Golden Principles sollen kurz, überprüfbar und projektnah sein.

## Drift erkennen, nicht sofort alles umbauen

Ein Scan oder Agentenlauf darf zunächst nur Fundstellen erzeugen.

Ablauf:

```text
Repository beobachten
→ mögliche Drift finden
→ Fund gegen Golden Principles prüfen
→ tatsächlichen Schaden bewerten
→ kleinen Repair-Scope bilden
→ normaler Plan / Review / Freigabeprozess
```

Keine großflächige automatische Bereinigung allein aufgrund einer Heuristik.

## Kleine Garbage-Collection-Slices

Bereinigung bevorzugt in kleinen, nachvollziehbaren Paketen durchführen.

Ein guter Cleanup-Slice:

- hat ein konkretes Problem;
- verändert möglichst wenig fachliches Verhalten;
- besitzt einen klaren Nachweis;
- reduziert Doppelstrukturen oder Inkonsistenz;
- ist getrennt von einer fachlich großen Feature-Änderung, wenn möglich.

Nicht aus jedem Feature nebenbei ein Architektur-Sanierungsprojekt machen.

## Kein Refactoring aus Geschmacksgründen

Nicht ändern, nur weil ein anderer Stil theoretisch eleganter wäre.

Ein Repair braucht einen nachvollziehbaren Nutzen, beispielsweise:

- weniger doppelte Wahrheit;
- weniger Fehlerquellen;
- klarere Schnittstelle;
- leichter prüfbare Invariante;
- Entfernung tatsächlich toter Strukturen;
- Reduktion von Agentenverwirrung durch widersprüchliche Muster.

## Vibe Architecting vermeiden

Agenten können durch lokale Entscheidungen unbeabsichtigt Architektur erzeugen.

Besonders aufmerksam prüfen, wenn eine Änderung einführt:

- neues Framework;
- neue Persistenzform;
- neuen Service oder Layer;
- neue zentrale Abstraktion;
- neue Infrastrukturkomponente;
- neues Datenformat;
- neue öffentliche Schnittstelle;
- neue Sicherheits- oder Berechtigungslogik.

Eine funktionierende Implementierung ist noch keine freigegebene Architekturentscheidung.

Wenn eine solche Entscheidung nicht bereits durch Plan oder Projektentscheidung gedeckt ist:

```text
STOP
→ Auswirkungen beschreiben
→ Optionen nennen
→ Architektur-Gate / neue Planung
```

## Agenten können bei Pflege helfen

Geeignete Aufgaben für Agenten:

- doppelte Muster lokalisieren;
- veraltete Dokumentationsstellen markieren;
- ungenutzte öffentliche Schnittstellen identifizieren;
- ähnliche Helper gruppieren;
- mögliche Regelverletzungen gegen Golden Principles auflisten;
- kleine Repair-Vorschläge erzeugen;
- Regressionstests für einen geplanten Cleanup ergänzen.

Die Entscheidung, ob ein Fund wirklich bereinigt wird, bleibt Teil des normalen Review- und Freigabeprozesses.

## Regelmäßige Pflege statt Großsanierung

Bei stark agentisch entwickelten Repositories kann eine kleine wiederkehrende Drift-Prüfung sinnvoller sein als seltene Großrefactorings.

Beispiel:

```text
Feature-Arbeit
→ Drift-Scan
→ kleine bestätigte Repair-Slices
→ Review
→ stabilerer Ausgangszustand
→ nächste Feature-Arbeit
```

## Qualitätscheck

Bei einem Drift- oder Garbage-Collection-Fund prüfen:

1. Ist es ein echtes Qualitätsproblem oder nur eine Stilpräferenz?
2. Welche Golden Principle oder konkrete Invariante ist betroffen?
3. Verursacht der Zustand Doppelwahrheit, Fehlergefahr oder Agentenverwirrung?
4. Kann der Repair klein und verhaltensneutral bleiben?
5. Gibt es einen Nachweis, dass nach dem Cleanup nichts Wesentliches beschädigt wurde?
6. Wird eine neue Architektur eingeführt, die ein eigenes Gate benötigt?
7. Sollte der Fund sofort behoben, geplant oder nur dokumentiert werden?

## Leitgedanke

> Agenten verstärken die Muster, die sie vorfinden. Deshalb ist Repository-Pflege Teil der Agentenqualität.