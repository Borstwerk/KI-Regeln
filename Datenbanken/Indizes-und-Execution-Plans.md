# Indizes und Execution Plans

## Zweck

Performanceänderungen sollen auf gemessenen Zugriffspfaden beruhen statt auf reflexhaftem Indexbau oder pauschalen Tuningregeln.

## Grundprinzip

> Erst messen, dann den tatsächlichen Ausführungsweg verstehen, dann gezielt ändern und erneut messen.

## Diagnoseablauf

```text
Symptom / langsame Query
→ relevante Query + Parameter erfassen
→ vorhandene Indizes / Strukturen prüfen
→ Execution Plan / Diagnose-Evidence lesen
→ Engpass-Hypothese formulieren
→ kleinste sinnvolle Änderung
→ erneut messen
```

## Vor einem neuen Index

Prüfen:

- existiert bereits ein passender oder überlappender Index?;
- welche Query-Formen profitieren tatsächlich?;
- ist die Selektivität ausreichend?;
- passt Feld-/Schlüsselreihenfolge zum Filter-/Sortiermuster?;
- entstehen zusätzliche Schreib-, Speicher- und Wartungskosten?;
- kann ein bestehender Index angepasst statt ein weiterer ergänzt werden?

> Mehr Indizes sind nicht automatisch mehr Performance.

## Execution Plan statt Bauchgefühl

Je nach Engine können unterschiedliche Diagnosemittel existieren.

Allgemein relevant:

- Scan vs. gezielter Lookup;
- erwartete vs. tatsächliche Zeilen/Dokumente/Keys;
- Sortier-/Join-/Lookup-Kosten;
- Filterselektivität;
- gelesene vs. zurückgegebene Datensätze;
- temporäre Strukturen / Spill / Memory;
- Round-Trips;
- Lock- oder Wait-Anteile.

Die konkrete Terminologie bleibt enginespezifisch.

## Achtung bei ausführender Analyse

Ein Analysebefehl kann je nach Engine die Query tatsächlich ausführen.

Deshalb vor produktionsnaher Diagnose klären:

- read-only oder mutierend?;
- erwartete Laufzeit / Datenmenge?;
- Lock-/Last-Risiko?;
- sichere Alternative mit Planner-only / Sampling / Staging vorhanden?

Beispielprinzip:

> `EXPLAIN` und `EXPLAIN ANALYZE` sind nicht automatisch gleich risikolos.

## Schemafehler nicht mit Indexen kaschieren

Wenn das Datenmodell strukturell nicht zum Zugriffsmuster passt, kann ein weiterer Index nur Symptome verschieben.

Bei wiederkehrenden Problemen prüfen:

- Datenmodell;
- Partitionierung / Sharding / Dokumentgrenzen;
- Query-Shape;
- Zugriffsmuster;
- Caching;
- Datenvolumen und Lifecycle.

## Performance-Evidence

Empfohlen:

```text
Baseline
→ Plan / Metrik
→ Änderung
→ neuer Plan / Metrik
→ Wirkung
→ Nebenwirkungen
```

Ohne Vorher-/Nachher-Evidence keine starke Performancebehauptung.

## Leitgedanke

> Ein Index ist ein Trade-off mit Kosten – kein Zauberpflaster.