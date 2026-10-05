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
2. Reproduzierbaren Ausgangszustand und relevante Baseline festlegen.
3. Auftrag und erlaubten Scope definieren.
4. Erwartetes Ergebnis und erwartetes Prozessverhalten getrennt beschreiben.
5. Deterministische Grader verwenden, wo möglich.
6. Negative Fälle und bewusstes `STOP` beziehungsweise `REQUEST GATE` einbauen.
7. Bei kritischen Guards prüfen, ob sie einen kontrolliert absichtlich eingebauten relevanten Fehler tatsächlich erkennen.
8. Ergebnisse so erfassen, dass Skill- oder Prozessversionen vergleichbar werden.
9. Für stabile wiederkehrende Messungen prüfen, ob eine reproduzierbare Baseline als Quality Floor/Ratchet geschützt werden soll.
10. Bei Skill-Evals nach Möglichkeit eine echte Kontrollbedingung ohne den zu prüfenden Skill vorsehen und den beobachtbaren Lift statt nur den absoluten Erfolg messen.
11. Instruktionsqualität und natürliche Discovery getrennt prüfen: erzwungene Skill-Nutzung testet primär den Skillinhalt; natürliche Auswahl testet zusätzlich Trigger und Routing.

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

## Harness- und Guard-Integrität

Ein vorhandener Check ist noch kein Nachweis, dass der Check die relevante Fehlersituation erkennen kann.

Für kritische deterministische Guards nach Möglichkeit mindestens eine kontrollierte Gegenprobe vorsehen:

```text
bekannter guter Fall
→ Guard akzeptiert

absichtlich relevanter Fehler
→ Guard schlägt fehl
→ aus dem erwarteten Grund
```

Dabei gilt:

- absichtlich kaputte Fixtures oder Mutationen nur in kontrollierter Testumgebung erzeugen;
- nicht irgendeinen Fehler provozieren, sondern den Fehler, gegen den der Guard schützen soll;
- nicht nur den Exitcode, sondern soweit möglich auch den erwarteten Fehlergrund prüfen;
- einen Guard, der bei der Gegenprobe nicht rot wird, nicht als wirksame Evidence behandeln;
- reale Produktionsdaten oder produktive Systeme nicht für solche Gegenproben mutieren.

Deliberate Breakage ist kein Pflichtschritt für jede triviale Evalregel. Es ist besonders wertvoll, wenn ein Guard einen wichtigen Completion-, Safety-, Scope- oder Quality-Claim tragen soll.

## Ratchets und Regression Floors

Bei stabilen, wiederholbaren Evalmetriken kann der aktuelle nachgewiesene Stand als Floor dienen.

Vor einem Ratchet prüfen:

- gleiche Metrik und gleiche Bedeutung;
- ausreichend gleiche Case-Population;
- relevante Runtime-/Modellstände dokumentiert;
- Baseline tatsächlich reproduziert;
- positive und negative/routing-nahe Fälle gemeinsam betrachtet.

Eine Änderung darf nicht dadurch „bestehen“, dass nach dem Scheitern nur Schwelle, Filter, Cases oder Grader gelockert werden.

Wenn sich der Maßstab selbst ändern muss, ist das eine separate, sichtbare Änderung mit neuer Baseline und begrenztem Vergleichsclaim.

## Negative Evals

Mindestens dort einsetzen, wo korrektes Verhalten **Nicht-Weiterarbeiten** bedeutet:

- widersprüchliche Spezifikation;
- neue Architekturentscheidung;
- verbotene Scope-Erweiterung;
- fehlender Validator;
- unklare Review-Basis;
- nicht freigegebener riskanter Zugriff.

## Vergleich, Baselines und Kalibrierung

Bei Skill-Änderungen dieselbe Eval-Suite gegen alte und neue Fassung ausführen, wenn ein reproduzierbarer Vergleich möglich ist.

Bei Skill-Evals ist – sofern technisch reproduzierbar – ein A/B-artiger Vergleich besonders aussagekräftig:

```text
gleiche Aufgabe + gleiche relevante Runtimebedingungen
→ ohne Skill / mit bisherigem Stand
→ mit geprüftem Skill
→ Delta in Ergebnis, Prozess, Triggerverhalten und Aufwand
```

Der Kontrolllauf darf nicht künstlich schlechter gemacht werden. Modell, Reasoning-/Budgetklasse, Fixtures, erlaubte Tools und Grader möglichst konstant halten oder Abweichungen sichtbar dokumentieren. Bei stochastischen Läufen Wiederholungen beziehungsweise pass@k nur mit dokumentierter Runzahl und identischen Vergleichsbedingungen interpretieren.

Nicht nur Gesamterfolg vergleichen, sondern auch:

- Scope-Verstöße;
- unnötige Änderungen;
- Testqualität;
- Gate-Verhalten;
- Evidence-Vollständigkeit.

Wenn Rubrik, Judge oder Schwellenwerte anhand bestimmter Fälle kalibriert werden, diese Fälle nicht anschließend als unabhängige Held-out-Evidence ausgeben. Kalibrierungsdaten und unabhängige Vergleichsdaten trennen, wenn aus dem Lauf ein Generalisierungs- oder Vergleichsclaim abgeleitet werden soll.

Für Skill-Routing zusätzlich unterscheiden:

- **forced invocation**: Skill ist sicher aktiv; prüft vor allem Instruktions- und Ausführungsqualität;
- **natural discovery**: Skill muss aus der Aufgabe korrekt gewählt werden; prüft Trigger, Routing und Near-Misses;
- **negative control**: Aufgabe darf den Skill nicht aktivieren oder muss bewusst stoppen.

Nullmodelle, Kontrollbedingungen, blindes oder double-blind Design können bei höherem Assurance-Bedarf sinnvoll sein. Sie sind keine universelle Pflicht und ersetzen keine passende Ground Truth oder reproduzierbare Baseline.

## Leitgedanke

> Ein guter Eval zeigt nicht nur, ob der Agent etwas geschafft hat, sondern ob er es auf eine verlässliche Weise geschafft hat – und ob der Prüfmechanismus relevante Fehler tatsächlich erkennen kann.
