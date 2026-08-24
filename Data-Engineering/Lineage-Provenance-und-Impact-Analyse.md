# Lineage, Provenance und Impact Analysis

## Zweck

Lineage macht nachvollziehbar, welche Datasets durch welche Verarbeitung aus welchen Inputs entstehen. Provenance ergänzt die Frage, welche konkrete Version, Ausführung und Evidence einem Ergebnis zugrunde liegt.

## Kernmodell

Ein nützliches minimales Modell ist:

```text
Dataset
→ Job / Transformation
→ Run / Ausführung
→ Output Dataset
```

OpenLineage verwendet ein ähnliches, erweiterbares Dataset-/Job-/Run-Modell. Das ist eine hilfreiche Referenz, aber keine Pflichtimplementierung.

## Lineage-Ebenen

Je nach Bedarf:

- Dataset-/Table-Level;
- Column-/Field-Level;
- Job-/Transformation-Level;
- Runtime-/Run-Level;
- fachliche Abhängigkeit zwischen Kennzahlen oder Datenprodukten.

Mehr Granularität ist nicht automatisch besser. Sie muss eine konkrete Frage beantworten.

## Typische Fragen

Lineage sollte beispielsweise helfen bei:

- Welche Outputs hängen von dieser Quelle ab?
- Welche Pipeline erzeugte diesen Datensatz?
- Welche Code-/Contract-Version lief?
- Welche Inputs waren für diesen Run relevant?
- Welche Consumer sind von einer Änderung betroffen?
- Wo könnte ein fehlerhaftes Feld weitergegeben worden sein?

## Design Lineage vs. Runtime Lineage

Unterscheiden:

- **Design Lineage:** erwartete Abhängigkeiten aus Code, SQL, Metadaten oder Konfiguration;
- **Runtime Lineage:** tatsächlich beobachtete Inputs/Outputs und Runs.

Designabsicht ist keine vollständige Runtime-Evidence.

## Impact Analysis

Vor relevanten Änderungen:

1. geändertes Dataset/Feld/Semantik bestimmen;
2. bekannte Downstream-Abhängigkeiten ermitteln;
3. Consumer und Materialisierungen identifizieren;
4. bekannte Lineage-Lücken markieren;
5. Compatibility und Reprocessingbedarf bewerten;
6. Migrations-/Kommunikationsbedarf ableiten.

Fehlende Lineage bedeutet `UNVERIFIED`, nicht automatisch „keine Downstreams“.

## Provenance

Für kritische Ergebnisse kann relevant sein:

- Source-Version oder Snapshot;
- Code-/Git-Version;
- Job-/Run-ID;
- Contract-/Schema-Version;
- Parameter und Datenintervall;
- Quality-/Reconciliation-Evidence.

## Nicht tun

- ein hübsches DAG-Diagramm mit vollständiger Lineage gleichsetzen;
- statischen Code als Beweis für tatsächlich verarbeitete Runtime-Daten behandeln;
- fehlende Metadaten als fehlende Abhängigkeit interpretieren;
- vollständige sensible Payloads nur für Lineage speichern;
- Column-Level-Lineage überall erzwingen, wenn Dataset-Level die Frage beantwortet.