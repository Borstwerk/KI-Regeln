# Agentenarbeit

Dieser Bereich beschreibt allgemeine Regeln für die Steuerung, den Kontext und die kontrollierte Autonomie von KI-Agenten.

Er liegt bewusst oberhalb einzelner Fachbereiche wie Programmierung oder Schreiben. Ein Agent kann innerhalb eines Fachbereichs arbeiten, benötigt aber zusätzlich Regeln dafür, **welchen Kontext er erhält, welche Schritte er ausführen darf, wie Ergebnisse geprüft werden und wann menschliche Freigabe nötig ist**.

## Grundprinzip

> Autonomie innerhalb klarer Grenzen.

Ein guter Agentenprozess definiert nicht jeden einzelnen Tastendruck. Er definiert:

- Ziel und Scope;
- relevante Quellen der Wahrheit;
- erlaubte Aktionen und Blast Radius;
- überprüfbare Zwischen- und Endzustände;
- Abhängigkeiten zwischen Arbeitsschritten;
- Wiederholungs- und Reparaturschleifen;
- geforderte Evidence;
- Observability und Traceability;
- Stop-Kriterien;
- Human-Gates für Entscheidungen, die nicht autonom getroffen werden sollen.

## Bausteine

### Context Engineering

Der Agent erhält den kleinsten ausreichenden Kontext für die aktuelle Aufgabe. Projektwissen wird möglichst aus seinen kanonischen Quellen geladen und nicht unnötig dupliziert.

Siehe `Context-Engineering.md`.

### Harness Engineering

Regeln werden nach Möglichkeit durch Werkzeuge, Tests, Linter, Schemas, Berechtigungen, Isolation oder andere technische Grenzen unterstützt. Textanweisungen allein sind die schwächste Form einer durchsetzbaren Regel.

Parallelität benötigt bei veränderlichem Zustand einen ausreichend isolierten Workspace.

Siehe `Harness-Engineering.md`.

### Task Graph und Loops

Komplexe Arbeit wird in abhängige, überprüfbare Knoten zerlegt. Ein Knoten darf intern iterieren, bis seine klaren Akzeptanzbedingungen erfüllt sind oder ein Stop-Kriterium greift.

Der Graph steuert Abhängigkeiten und Grenzen, nicht jeden einzelnen Implementierungsschritt.

Siehe `Task-Graph-und-Loops.md`.

### Delegation und Evidence

Vor relevanter Delegation werden Ziel, Scope, Quellen der Wahrheit, Befugnisse, Akzeptanzbedingungen und Stop-Kriterien geklärt.

Nach der Arbeit liefert der Agent ein Evidence Bundle statt eines bloßen Fertig-Status.

Siehe `Delegation-und-Evidence.md`.

### Agent Evals

Produktprüfungen und Agentenprüfungen werden getrennt betrachtet.

Agent Evals prüfen beispielsweise, ob ein Agent Scope, Gates, Quellen, Tests und Evidence zuverlässig behandelt – auch in Situationen, in denen korrektes Verhalten bewusstes Stoppen bedeutet.

Siehe `Agent-Evals.md`.

### Observability und Traceability

Relevante Agentenarbeit soll später nachvollziehbar sein:

```text
Intent
→ Delegation
→ Agentenlauf
→ Evidence
→ Diff / Artefakt
→ Review
→ Freigabe
```

Die Session erklärt den Weg, ersetzt aber keine kanonische Projektdokumentation.

Siehe `Observability-und-Traceability.md`.

### Human Gates

Nicht jede Entscheidung soll autonom fallen. Änderungen mit hohem Risiko, unklarer Spezifikation, Architekturwirkung, Datenverlustpotenzial oder externer Veröffentlichung benötigen eine ausdrücklich definierte Freigabe.

Der Mensch beziehungsweise die Governance bleibt auf dem äußeren Why Loop; der Agent kann innerhalb des freigegebenen How Loops selbstständig arbeiten.

Siehe `Human-Gates-und-Freigaben.md`.

### Entropie und Garbage Collection

Agenten verstärken Muster, die sie im Repository vorfinden. Deshalb gehört kontrollierte Drift-Erkennung zur langfristigen Agentenqualität.

Bereinigung erfolgt in kleinen bestätigten Repair-Slices und nicht als automatische Großsanierung.

Siehe `Entropie-und-Garbage-Collection.md`.

## Innerer und äußerer Loop

Ein Agent darf innerhalb eines freigegebenen Arbeitsschritts selbstständig iterieren:

```text
Arbeiten
→ Prüfen
→ Diagnose
→ Korrigieren
→ erneut prüfen
```

Der äußere Prozess bleibt davon getrennt:

```text
Intent / Anforderung
→ Delegation / Planung
→ Freigabe
→ agentische Ausführung
→ Evidence
→ Review
→ menschliche oder definierte Freigabe
```

Ein innerer Loop darf keinen äußeren Gate überspringen.

## Leitgedanken

- Agenten sollen nicht raten, wenn eine Quelle der Wahrheit vorhanden ist.
- Kontext soll relevant und aktuell sein, nicht maximal groß.
- Ein Delegation Contract beschreibt Ziel, Grenzen und erwarteten Nachweis.
- Unabhängige Arbeit darf parallelisiert werden; abhängige Arbeit nicht.
- Parallel arbeitende Agenten benötigen ausreichend isolierte veränderliche Workspaces.
- Jeder wichtige Übergang braucht einen prüfbaren Ausgangszustand.
- Fehler werden möglichst am frühesten fehlerhaften Übergang repariert.
- Wiederholung braucht ein Budget oder Stop-Kriterium.
- Ein Agent darf fehlende Spezifikation nicht stillschweigend durch eine eigene Entscheidung ersetzen.
- Automatisch prüfbare Regeln sollten möglichst automatisch geprüft werden.
- Ein erfolgreich ausgeführter Agentenlauf ist noch keine Freigabe.
- Produktqualität und Agentenprozessqualität können getrennt evaluiert werden.
- Agentenläufe sollen nachvollziehbar sein, ohne unnötige sensible Daten zu protokollieren.
- Der Repository-Zustand prägt spätere Agentenarbeit; Drift sollte deshalb bewusst gepflegt werden.

## Skills

Unter `Skills/` liegen kompakte Arbeitsdisziplinen für konkrete Agenteneinsätze:

- `context-engineering` – relevanten Kontext auswählen und Quellen der Wahrheit erhalten;
- `task-graph` – komplexe Arbeit in abhängige, überprüfbare Knoten zerlegen;
- `verification-loop` – Arbeit innerhalb eines freigegebenen Scopes iterativ prüfen und reparieren;
- `delegation-contract` – Auftrag, Scope, Rechte, Stop-Bedingungen und Evidence vorab definieren;
- `agent-eval` – reproduzierbar prüfen, ob Agenten Ergebnis- und Prozessanforderungen einhalten.

Diese Skills ersetzen keine fachlichen oder projektspezifischen Regeln.

## Quellen

Externe Ansätze und ihre Einordnung sind in `Quellen-und-Inspirationen.md` dokumentiert.

> Konzepte werden übernommen, wenn sie Arbeit besser machen – nicht weil sie ein gutes Buzzword ergeben.