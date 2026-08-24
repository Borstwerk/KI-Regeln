# Datenfluss, Quellen, Ziele und Verantwortung

## Zweck

Ein Datenfluss beginnt nicht beim Scheduler, sondern bei einer fachlichen Frage: Welche Information soll von welcher autoritativen Quelle zu welchem Consumer gelangen und welche Bedeutung muss dabei erhalten bleiben?

## Source of Truth

Vor Pipelineentwurf klären:

- welche Quelle für welche Felder oder Ereignisse autoritativ ist;
- ob Daten vollständig oder nur ausschnittsweise verfügbar sind;
- ob Deletes, Korrekturen und historische Änderungen sichtbar werden;
- welche Zeitzone, Identifier und fachlichen Zustände gelten;
- welche Consumer das Ergebnis verwenden;
- wer Source, Pipeline und Output fachlich beziehungsweise technisch verantwortet.

Ein technisch bequem erreichbarer Export ist nicht automatisch die fachliche Source of Truth.

## Datenflussmodell

```text
Business Intent
→ Source of Truth
→ Capture / Ingestion
→ Raw / Landing, falls sinnvoll
→ Transformation / Enrichment
→ Quality / Reconciliation
→ Publish
→ Consumer
→ Feedback / Incident / Evolution
```

Nicht jede Pipeline braucht jede Stufe. Die Struktur folgt dem realen Bedarf.

## Ownership

Ownership sollte mindestens unterscheiden:

- Source Owner – verantwortet Bedeutung und Bereitstellung der Quelldaten;
- Pipeline Owner – verantwortet Verarbeitung und technische Betriebsfähigkeit;
- Dataset/Data-Product Owner – verantwortet veröffentlichtes Ergebnis und Consumerzusagen;
- Consumer Owner – verantwortet bekannte Nutzung und Migrationsbedarf.

Eine Person oder ein Team kann mehrere Rollen tragen. Die Rollen dürfen aber nicht implizit bleiben.

## Semantische Grenzen

Bei jeder Stufe dokumentieren:

- Input Grain;
- Output Grain;
- Schlüssel / Identität;
- Filter und Exclusions;
- Ableitungen und Defaults;
- Null-/Unknown-Semantik;
- Zeitbezug;
- Verlust oder Aggregation von Information.

## Nicht tun

- Quelle aus Namensähnlichkeit erraten;
- Landing-/Raw-Daten automatisch als fachlich korrekt behandeln;
- technische Owner mit fachlicher Autorität gleichsetzen;
- unbekannte Consumer als Beweis für fehlende Consumer verwenden;
- Transformationen ohne dokumentierte Bedeutungsänderung als rein technisch darstellen.

## Evidence

Belastbare Evidence kann sein:

- Quellschema und reale Samples;
- fachliche Definitionen;
- Data Contract;
- Lineage;
- Consumerabfragen;
- Produktionsmetriken und Reconciliation;
- dokumentierte Ownership.

Fehlende Evidence wird als Gap markiert, nicht durch Modellwissen ersetzt.