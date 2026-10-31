# Akzeptanzkriterien: begrenzter Katalogfix

Separater Folgeauftrag vom 31.10.2026, Basis `57736a7` nach Merge von PR #119.
Methoden: `diagnose`, `agent-eval`, `tdd`, `verification-loop`; separater
Same-Model-Planreview, keine unabhängige Zertifizierung. Keine Modellaufrufe.

## Diagnose und vorab begrenzter Reparaturplan

Der unveränderte P1-Treiber reproduziert **15 PASS, 1 FAIL, 8 NOT RUN**. Betroffen
ist weiterhin `jobs-acceptance-tests`, insbesondere die unveränderte Query
`Akzeptanzkriterien beobachtbar`. Der zweite Job `test-design` wird gefunden.

Das bestehende Suchdokument von `acceptance-criteria-design` enthält
`beobachtbare`, `Acceptance Criteria` und `Verification Intent`, aber nirgendwo
`Akzeptanzkriterien`. Das gilt auch für seinen Katalogzweck. QMD 2.8.3 verbindet
positive lexikalische Begriffe mit AND; die vorhandene FTS-Abfrage liefert für die
deutsche Kombination nur `delegation-contract`, während die englische Kombination
den Zielskill enthält. Damit fehlen keine Skillquellen im Index. Ein Rankinglimit
oder ein Flexionsproblem erklärt den fehlenden deutschen Begriff nicht.

**Kleinster Eingriff:** ausschließlich `purpose` des Katalogeintrags
`acceptance-criteria-design` in `skill-catalog.yml`:

```diff
-Beobachtbare Acceptance Criteria und Verification Intent für bestehende Requirements formulieren, ohne konkrete Testfälle vorwegzunehmen.
+Beobachtbare Akzeptanzkriterien (Acceptance Criteria) und Verification Intent für bestehende Requirements formulieren, ohne konkrete Testfälle vorwegzunehmen.
```

Die deutsche Fachbezeichnung drückt dieselbe Verantwortung aus. Description,
Near-Miss, Maturity, Related-Kanten und Fähigkeiten bleiben unverändert. Kein
Algorithmusfix, keine neue Aliasliste, keine Queryexpansion und keine Abhängigkeit.
Backout ist das Zurücknehmen dieses einen Feldedits.

Der historische P1-Vertrag verzichtete ausdrücklich auf nachträglich gepflegte
Synonyme. Diese frühere Entscheidung und ihr FAIL werden **nicht** umgeschrieben.
Dieser nun ausdrücklich beauftragte Folge-Slice prüft eine sichtbare fachliche
Metadatenkorrektur. Er ist datenabhängige Development-Arbeit, kein unabhängiger
Test der früheren unveränderten Quelle.

## Vorab festgelegter Nachweis

- Den vorhandenen P1-Vergleich minimal um eine explizite Katalogrevision ergänzen.
  Ein fail-closed Guard akzeptiert nur den oben festgelegten `purpose`-Edit;
  sämtliche anderen Katalogfelder und Einträge müssen mit dem eingefrorenen
  Basiskatalog übereinstimmen. Der Guard vergleicht geparstes YAML; der exakte
  einzeilige Commitdiff und die Hashbindung belegen zusätzlich den konkreten
  Byteumfang dieses Kandidaten. Unzulässige weitere Änderungen werden vor QMD
  zurückgewiesen; entsprechende Gegenproben gehören zum Guardtest.
- Vor dem Kandidatenlauf Controller, diesen Vertrag und exakten Katalogdiff
  committen. Beide Bedingungen mit derselben Treiberfassung und derselben
  Engine ausführen; Baseline ohne Override, Candidate mit gepinnter Katalogrevision.
- Alle bisherigen 24 Fälle, Queries, Grader und zehn Treffer pro Query unverändert
  lassen. P1 umfasst 16 Retrievalfälle; die übrigen acht technischen P2-/P3-Fälle
  bleiben in diesem Treiber **NOT RUN** und werden nicht als Sucherfolg gezählt.
- Alle übrigen Quellen im Paket identisch halten. Katalog-, Paket-, Suchdokument-
  und Fixturehashes dürfen sich wegen des Datenfixes unterscheiden und werden
  getrennt ausgewiesen. Kein Claim eines insgesamt unveränderten Quellenpakets.
  `original_bytes_unchanged` im Treiber bedeutet unverändert während des Laufs
  gegenüber dem jeweils zugelassenen Fixturepaket, nicht identisch zwischen den
  beiden Bedingungen.
- Ziel: der bekannte Mehrjob-Fall besteht; keine Regression der bisherigen 15
  erfolgreichen Fälle. Bei Scheitern kein weiteres Tuning oder Oraclelockerung
  im selben Plan, sondern Ergebnis offen dokumentieren und neu diagnostizieren.
- Vorhandene Controller-/Facet-/Paging-/Relations-Tests und Full Harness verwenden.
  Die bestehende Facet-Stalenessprüfung deckt veraltete Katalogindizes ab.
  Code-/Evidence-Review separat; keine zusätzlichen Agentenmodell-Evals nötig.

Ein möglicher 16/16-Erfolg belegt ausschließlich dieses bekannte Development-/
Regressionsset. Allgemeiner Recall, natürliche Agentenauswahl, Effizienz und
Maturity bleiben davon unberührt; Suche bleibt optional. Historische Berichte
bleiben unverändert. Ergebnisse werden erst nach Ausführung angehängt.

Status des neuen Kandidaten vor Ausführung: **NOT RUN**.
