# Workflow – Long-Horizon-Agentenarbeit

## Ziel

Größere Agentenaufgaben über viele Toolaufrufe, Context-Compactions, Sessions oder Agenten hinweg fortführen, ohne Sources of Truth, offenen Zustand oder Evidence zu verlieren.

## Ablauf

```text
context-engineering
→ task-graph / delegation-contract bei Bedarf
→ Arbeit
→ context-audit bei Context-/Effizienzproblemen
→ context-compaction bei gewachsenem aktiven Verlauf
→ verification-loop an relevanten Gates
→ session-handoff bei Session-/Agentenwechsel
→ frische Instanz liest Handoff + Sources of Truth
→ Arbeit fortsetzen
```

Nicht jeder Lauf benötigt Audit, Compaction oder Handoff. Sie werden an realen Grenzen eingesetzt.

## Phase 1 – Kontext setzen

Mit `context-engineering`:

- Ziel und Scope klären;
- Sources of Truth bestimmen;
- aktiven Kontext klein und signalstark halten;
- Working State von dauerhaftem Wissen trennen;
- Just-in-time-Retrieval bevorzugen, wenn sinnvoll.

## Phase 2 – Arbeit und Zustand

Bei komplexer Arbeit optional:

- `task-graph` für Abhängigkeiten;
- `delegation-contract` für Subagenten;
- persistente taskbezogene Notizen oder Artefakte als Working State.

Working State ersetzt keine kanonische Projektdokumentation.

## Phase 3 – Context Audit

`context-audit` verwenden, wenn zum Beispiel:

- Tokenverbrauch oder Latenz unerwartet steigt;
- alte Tooloutputs den Verlauf dominieren;
- Kontextfehler oder Wiederholungen auftreten;
- unklar ist, was aktiv bleiben muss.

Optimierungen immer gegen Outcome oder passende Evidence prüfen.

## Phase 4 – Compaction

`context-compaction` verwenden, wenn der aktive Verlauf sinnvoll verdichtet werden kann.

Erhalten:

- Constraints;
- Entscheidungen;
- Sources of Truth;
- Artefaktzustand;
- offene Probleme;
- Evidence;
- Gates;
- nächsten Schritt.

Compaction nicht allein an Kürze bewerten.

## Phase 5 – Session-/Agentenwechsel

Mit `session-handoff` einen standalone Fortsetzungszustand erzeugen.

Der empfangende Agent soll:

1. lokale Regeln und Sources of Truth erneut prüfen;
2. Handoff als Arbeitsstart, nicht als neue kanonische Wahrheit behandeln;
3. Evidence/Gates nicht ungeprüft hochstufen;
4. vom dokumentierten nächsten Schritt aus weiterarbeiten.

## Multi-Agent-Offloading

Subagenten können getrennte Kontextfenster für unabhängige Arbeit nutzen.

Nur einsetzen, wenn:

- echte Parallelität oder getrennte Informationsräume bestehen;
- Koordinationskosten gerechtfertigt sind;
- Delegation und Handoff klar sind.

Multi-Agent-Architektur kann Gesamttokenverbrauch erhöhen und ist kein universeller Effizienztrick.

## Abschluss

Ein langer Agentenlauf ist nicht deshalb erfolgreich, weil er beliebig lange weiterlaufen konnte.

Erfolgreich bedeutet:

- Taskfortschritt ist nachweisbar;
- Sources of Truth bleiben intakt;
- Handoffs sind fortsetzbar;
- Compaction verliert keine kritische Information;
- Context-Optimierungen verschlechtern Outcome nicht;
- Human Gates bleiben erhalten.

> Lange Arbeit braucht nicht unendlich viel aktiven Kontext, sondern zuverlässigen Zustand und gute Übergaben.