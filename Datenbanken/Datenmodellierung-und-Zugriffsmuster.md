# Datenmodellierung und Zugriffsmuster

## Zweck

Datenmodelle sollen reale fachliche Beziehungen, Integritätsanforderungen und tatsächliche Lese-/Schreibmuster tragen.

## Grundprinzip

> Datenmodellierung beginnt nicht mit Tabellen, Collections oder Keys, sondern mit Domäne, Invarianten und Zugriffsmustern.

## Vor dem Entwurf klären

- Welche fachlichen Entitäten und Beziehungen existieren?
- Welche Daten gehören logisch zusammen?
- Welche Daten werden gemeinsam gelesen oder geschrieben?
- Welche Zugriffe sind häufig, welche selten?
- Ist die Last eher lese-, schreib- oder gemischtlastig?
- Welche Konsistenzanforderungen bestehen?
- Welche Datenmengen und Wachstumsrichtungen sind realistisch?
- Welche Lebenszyklen, Aufbewahrungs- oder Löschregeln bestehen?

## Reales System vor Annahmen

Bei bestehenden Systemen nicht aus Namen oder Gewohnheit auf das Schema schließen.

Bevor Änderungen vorgeschlagen werden, soweit verfügbar prüfen:

- Migrationen und Schema-Dateien;
- ORM-/ODM-Modelle;
- echte Schema-Introspection;
- relevante Queries im Code;
- Query-/Slow-Log-Statistiken;
- vorhandene Indizes und Constraints;
- tatsächliche Datenverteilung und Größenordnungen.

> Plausible Tabellen-, Spalten-, Collection-, Key- oder Feldnamen sind keine Evidence.

## Zugriffsmuster vor Dogma

Keine Modellierungsstrategie ist universell richtig.

Beispiele:

- Normalisierung kann Integrität und Änderbarkeit verbessern;
- gezielte Denormalisierung kann Round-Trips oder teure Joins reduzieren;
- Dokumente können zusammengehörige Daten bewusst einbetten;
- Key-Value-/In-Memory-Systeme wählen Datenstrukturen nach Operationen und Zugriffspfaden.

Darum gilt:

> Wähle die Modellierungsstrategie passend zu Datenbankmodell, Konsistenzanforderungen und Zugriffsmustern.

## Schreib- und Lesepfade gemeinsam betrachten

Eine Optimierung des Lesepfads darf nicht blind:

- Schreibkosten vervielfachen;
- unkontrollierte Datenkopien erzeugen;
- Integritätsregeln schwächen;
- Update-Fan-out erzeugen;
- Speicher- oder Indexkosten unverhältnismäßig erhöhen.

## Wachstum und Grenzen

Für jedes Modell relevante Wachstumsrichtungen prüfen:

- ungebundene Arrays oder Listen;
- Hot Keys / Hot Partitions;
- monotone Schlüssel oder ungleichmäßige Verteilung;
- sehr große Zeilen/Dokumente/Werte;
- historische Daten ohne Lifecycle;
- hohe Kardinalität;
- viele optionale oder polymorphe Strukturen.

Konkrete Grenzwerte bleiben enginespezifisch.

## Design-Evidence

Eine Modellierungsentscheidung sollte nachvollziehbar machen:

```text
fachliche Anforderung
→ relevante Zugriffsmuster
→ gewähltes Modell
→ zentrale Trade-offs
→ Integritätsstrategie
→ erwartetes Wachstum
→ offene Risiken
```

## Qualitätscheck

1. Ist das reale oder geplante Zugriffsmuster bekannt?
2. Sind Domänenbegriffe und Invarianten erkennbar?
3. Wurde keine SQL-/Document-/Key-Value-Konvention unnötig verallgemeinert?
4. Sind Lese- und Schreibkosten berücksichtigt?
5. Sind Wachstum und Lifecycle bedacht?
6. Ist klar, welche Annahmen noch verifiziert werden müssen?

## Leitgedanke

> Das beste Datenmodell ist nicht das theoretisch reinste, sondern dasjenige, das Domäne, Integrität, Zugriff und Betrieb gemeinsam tragfähig macht.