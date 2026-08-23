# Agentenarbeit

Dieser Bereich beschreibt allgemeine Regeln für die Steuerung, den Kontext und die kontrollierte Autonomie von KI-Agenten.

Er liegt bewusst oberhalb einzelner Fachbereiche wie Programmierung oder Schreiben. Ein Agent kann innerhalb eines Fachbereichs arbeiten, benötigt aber zusätzlich Regeln dafür, **welchen Kontext er erhält, welche Schritte er ausführen darf, wie Ergebnisse geprüft werden und wann menschliche Freigabe nötig ist**.

## Grundprinzip

> Autonomie innerhalb klarer Grenzen.

Ein guter Agentenprozess definiert nicht jeden einzelnen Tastendruck. Er definiert:

- Ziel und Scope;
- relevante Quellen der Wahrheit;
- erlaubte Aktionen;
- überprüfbare Zwischen- und Endzustände;
- Abhängigkeiten zwischen Arbeitsschritten;
- Wiederholungs- und Reparaturschleifen;
- Stop-Kriterien;
- Human-Gates für Entscheidungen, die nicht autonom getroffen werden sollen.

## Vier Bausteine

### Context Engineering

Der Agent erhält den kleinsten ausreichenden Kontext für die aktuelle Aufgabe. Projektwissen wird möglichst aus seinen kanonischen Quellen geladen und nicht unnötig dupliziert.

### Harness Engineering

Regeln werden nach Möglichkeit durch Werkzeuge, Tests, Linter, Schemas, Berechtigungen oder andere technische Grenzen unterstützt. Textanweisungen allein sind die schwächste Form einer durchsetzbaren Regel.

### Task Graph und Loops

Komplexe Arbeit wird in abhängige, überprüfbare Knoten zerlegt. Ein Knoten darf intern iterieren, bis seine klaren Akzeptanzbedingungen erfüllt sind oder ein Stop-Kriterium greift.

### Human Gates

Nicht jede Entscheidung soll autonom fallen. Änderungen mit hohem Risiko, unklarer Spezifikation, Architekturwirkung, Datenverlustpotenzial oder externer Veröffentlichung benötigen eine ausdrücklich definierte Freigabe.

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
Auftrag / Anforderung
→ Planung
→ Freigabe
→ agentische Ausführung
→ Nachweis
→ Review
→ menschliche oder definierte Freigabe
```

Ein innerer Loop darf keinen äußeren Gate überspringen.

## Leitgedanken

- Agenten sollen nicht raten, wenn eine Quelle der Wahrheit vorhanden ist.
- Kontext soll relevant und aktuell sein, nicht maximal groß.
- Unabhängige Arbeit darf parallelisiert werden; abhängige Arbeit nicht.
- Jeder wichtige Übergang braucht einen prüfbaren Ausgangszustand.
- Fehler werden möglichst am frühesten fehlerhaften Übergang repariert.
- Wiederholung braucht ein Budget oder Stop-Kriterium.
- Ein Agent darf fehlende Spezifikation nicht stillschweigend durch eine eigene Entscheidung ersetzen.
- Automatisch prüfbare Regeln sollten möglichst automatisch geprüft werden.
- Ein erfolgreich ausgeführter Agentenlauf ist noch keine Freigabe.

## Skills

Unter `Skills/` liegen kompakte Arbeitsdisziplinen für konkrete Agenteneinsätze:

- `context-engineering` – relevanten Kontext auswählen und Quellen der Wahrheit erhalten;
- `task-graph` – komplexe Arbeit in abhängige, überprüfbare Knoten zerlegen;
- `verification-loop` – Arbeit innerhalb eines freigegebenen Scopes iterativ prüfen und reparieren.

Diese Skills ersetzen keine fachlichen oder projektspezifischen Regeln.