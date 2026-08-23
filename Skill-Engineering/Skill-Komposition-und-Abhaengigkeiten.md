# Skill-Komposition und Abhängigkeiten

## Zweck

Skills sollen kombinierbar sein, ohne sich gegenseitig stillschweigend zu verschachteln oder Scope zu vergrößern.

## Drei Beziehungstypen

### Related

Ein anderer Skill ist fachlich verwandt, aber nicht zwingend erforderlich.

### Precondition

Ein vorgelagerter Zustand muss existieren.

Beispiel:

```text
greybox
benötigt eine ausreichend klare Designrichtung
```

### Follow-up

Ein nachgelagerter Skill ist sinnvoll, aber nicht automatisch auszuführen.

Beispiel:

```text
research-synthesis
→ anschließend citation-audit empfohlen
```

## Keine versteckten Ketten

Ein Skill darf nicht unbemerkt eine lange Pipeline starten.

Wenn eine wiederkehrende Aufgabe mehrere Skills in fester Reihenfolge benötigt, gehört die Orchestrierung in `Workflows/`.

## Abhängigkeitsregeln

- zyklische harte Abhängigkeiten vermeiden;
- nur echte Voraussetzungen als Pflicht markieren;
- verwandte Skills nicht als Pflicht aufblasen;
- lokale Projektregeln nicht als zentrale Skillabhängigkeit modellieren;
- Capability-Abhängigkeiten separat von fachlichen Skillabhängigkeiten behandeln.

## Handoffs

Ein sauberer Handoff enthält möglichst:

- bisheriges Ziel;
- relevante Ergebnisse;
- Evidence;
- offene Unsicherheiten;
- freigegebenen Scope;
- nächsten erwarteten Output.

Der nächste Skill soll nicht die komplette Vorgeschichte neu rekonstruieren müssen.

## Kontextisolation

Unabhängige Review- oder Verifikationsskills profitieren häufig davon, nicht alle Bewertungen des erzeugenden Skills zu übernehmen.

Beispiele:

- Implementierung → Code Review;
- Synthese → Citation Audit;
- Bildgenerierung → Bildreview.

## Leitgedanke

> Skills sind Bausteine. Workflows verbinden sie; Abhängigkeiten dürfen sie nicht heimlich zu Monolithen machen.
