# Technologieauswahl und Reversibilität

## Zweck

Technologie ist eine Architekturentscheidung, wenn sie relevante Constraints, Failure Modes, Betriebsmodelle, Daten- oder Integrationssemantik festlegt. Sie ist aber nicht der Ausgangspunkt des Systemdesigns.

## Reihenfolge

```text
Problem / Driver
→ benötigte Eigenschaften
→ strukturelle Entscheidung
→ Technologieanforderungen
→ konkrete Optionen
→ Evidence / PoC / Benchmark, falls nötig
```

## Auswahlkriterien

Je nach Entscheidung können relevant sein:

- funktionaler Fit;
- Konsistenz-, Delivery- oder Durability-Semantik;
- Last- und Capacity-Grenzen;
- Betriebs- und Observability-Modell;
- Security und Compliance;
- Skills und Ownership im Team;
- Ecosystem, Support, Lizenz und Lifecycle;
- Portabilität und Exit-/Migration-Pfad;
- Kosten unter realistischem Nutzungsprofil;
- Compatibility mit bestehendem System.

## Reversibilität

Nicht jede Entscheidung ist gleich schwer umkehrbar.

Grob unterscheiden:

- leicht lokal austauschbar;
- mit begrenzter Migration austauschbar;
- strukturell bindend;
- daten-/contract-/betriebsseitig schwer reversibel.

Je schwerer die Reversibilität, desto stärker müssen Alternativen, Evidence, Migrationspfad und langfristige Konsequenzen sichtbar sein.

## PoC und Benchmark

Ein PoC beweist nur die geprüften Eigenschaften im geprüften Kontext. Ein Benchmark ohne reale Lastform, Datenverteilung oder Betriebsconstraint darf nicht zur allgemeinen Architekturwahrheit werden.

## Anti-Regeln

- keine Technologie allein aufgrund Popularität oder Cloud-Vendor-Referenzarchitektur wählen;
- keine neue Datenbank nur wegen eines einzelnen Access Patterns einführen, bevor bestehende Optionen geprüft sind;
- keine Message Queue einsetzen, nur um Komponenten vermeintlich zu entkoppeln;
- keine Plattformmigration als Architekturverbesserung verkaufen, wenn der Driver unklar bleibt;
- Vendor Lock-in weder pauschal verbieten noch ignorieren.

## Leitgedanke

> Technologie soll eine begründete Architektur tragen – nicht nachträglich erklären, warum sie ohnehin schon gewählt wurde.