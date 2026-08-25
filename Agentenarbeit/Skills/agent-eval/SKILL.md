---
name: agent-eval
description: Entwirft reproduzierbare Evals für Agentenverhalten und trennt dabei Produktqualität von Prozessqualität. Verwenden beim Entwurf oder Review von Evals für Agentenverhalten.
---

# Agent Eval

Dieser Skill nutzt `../../Agent-Evals.md`.

## Ziel

Prüfe nicht nur, ob das erzeugte Produkt korrekt ist, sondern ob der Agent zuverlässig nach den vorgesehenen Regeln arbeitet.

## Eval aufbauen

1. Konkretes Agentenverhalten benennen.
2. Reproduzierbaren Ausgangszustand festlegen.
3. Auftrag und erlaubten Scope definieren.
4. Erwartetes Ergebnis und erwartetes Prozessverhalten getrennt beschreiben.
5. Deterministische Grader verwenden, wo möglich.
6. Negative Fälle und bewusstes `STOP` beziehungsweise `REQUEST GATE` einbauen.
7. Ergebnisse so erfassen, dass Skill- oder Prozessversionen vergleichbar werden.

## Zwei Prüfachsen

### Ergebnisqualität

- fachlich korrekt;
- technisch korrekt;
- erwartete Tests und Artefakte vorhanden.

### Prozessqualität

- Scope eingehalten;
- Quellen der Wahrheit genutzt;
- keine notwendigen Gates übersprungen;
- Tests und Validierung nicht abgeschwächt;
- Unsicherheiten korrekt benannt;
- geforderte Evidence geliefert.

## Grader

Bevorzugen:

- Testresultate;
- Schemaprüfungen;
- Datei- oder Diff-Prüfungen;
- statische Regeln;
- reproduzierbare Messungen;
- explizite Status- oder Artefaktprüfungen.

LLM-Bewertung nur verwenden, wenn das relevante Qualitätsmerkmal nicht sinnvoll deterministisch prüfbar ist.

## Negative Evals

Mindestens dort einsetzen, wo korrektes Verhalten **Nicht-Weiterarbeiten** bedeutet:

- widersprüchliche Spezifikation;
- neue Architekturentscheidung;
- verbotene Scope-Erweiterung;
- fehlender Validator;
- unklare Review-Basis;
- nicht freigegebener riskanter Zugriff.

## Vergleich von Skills

Bei Skill-Änderungen dieselbe Eval-Suite gegen alte und neue Fassung ausführen.

Nicht nur Gesamterfolg vergleichen, sondern auch:

- Scope-Verstöße;
- unnötige Änderungen;
- Testqualität;
- Gate-Verhalten;
- Evidence-Vollständigkeit.

## Leitgedanke

> Ein guter Eval zeigt nicht nur, ob der Agent etwas geschafft hat, sondern ob er es auf eine verlässliche Weise geschafft hat.