# Skill-Handbuch – Context und Long-Horizon-Agentenarbeit

Dieser Leitfaden erklärt die Context-Skills des Bereichs `Agentenarbeit/`.

## Grundmodell

```text
context-engineering
→ richtigen aktiven Kontext auswählen

context-audit
→ Context-Footprint und Signalqualität prüfen

context-compaction
→ gewachsenen Verlauf mit hoher Fidelity verdichten

session-handoff
→ Zustand an neue Session oder neuen Agenten übergeben
```

## `context-engineering`

Verwenden, wenn entschieden werden muss, welche Informationen ein Agent jetzt benötigt.

Typische Fragen:

- Welche Sources of Truth gehören in den Lauf?
- Was ist nur Hintergrund?
- Was kann später gezielt geladen werden?
- Was gehört in Working State statt Active Context?

Nicht für dauerhafte Wissensorganisation verwenden.

## `context-audit`

Verwenden, wenn der Kontext selbst zum Untersuchungsobjekt wird.

Beispiele:

- ungewöhnlich hoher Tokenverbrauch;
- lange Tooloutputs;
- viele gleichzeitig sichtbare Skills oder Tools;
- Wiederholungen, Altstände oder Context Rot;
- Qualitätsverlust in langen Läufen.

Wenn echte Tokenmetriken fehlen, dürfen relative Größen als Approximation dienen. Keine erfundenen exakten Tokenzahlen.

## `context-compaction`

Verwenden, wenn ein gewachsener Verlauf verdichtet werden soll.

Wichtig:

> Die relevante Frage lautet nicht „Wie kurz wurde es?“, sondern „Kann die Arbeit danach korrekt weitergehen?“

Deshalb harte Constraints, Entscheidungen, offene Probleme, Sources of Truth, Evidence und Gates erhalten.

## `session-handoff`

Verwenden bei:

- neuem Chat;
- neuer Session;
- Agentenwechsel;
- geplantem späteren Fortsetzen.

Das Handoff muss eigenständig verständlich sein und darf keine Freigabe oder Evidence erfinden.

## Active Context, Working State, Persistent Knowledge

```text
Active Context
→ jetzt modell-sichtbar

Working State
→ task-/threadbezogen über längere Arbeit

Persistent Knowledge
→ dauerhaftes Wissen über Tasks hinweg
```

Die ersten beiden Ebenen gehören zur Agentenarbeit. Persistent Knowledge gehört in einen separaten Wissensmanagement-Bereich, der als nächster eigener Fachbereich aufgebaut wird; bis dahin ist `Wissensmanagement/` kein vorhandener Repository-Pfad.

## Zusammenspiel mit anderen Skills

Bei längerer Arbeit typischerweise:

```text
context-engineering
→ task-graph
→ delegation-contract bei Bedarf
→ Arbeit
→ context-audit / context-compaction bei Bedarf
→ verification-loop
→ session-handoff bei Übergabe
```

Siehe `../Workflows/Long-Horizon-Agentenarbeit.md`.

## Maturity

Der vorhandene `context-engineering`-Skill ist bereits ein etablierter Kernskill und wird durch neue Evals geschärft.

Neue Skills wie `context-audit`, `context-compaction` und `session-handoff` starten konservativ als `experimental` und müssen sich in realen Läufen und weiteren Evals bewähren.
