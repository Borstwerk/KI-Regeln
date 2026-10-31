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

## Technischer Admissionbefund vor dem endgültigen Paar

Ein erster Kandidatenstart auf `faa53e3` stoppt vor `resolve_node` und QMD-Aufbau:
`relation-related` aus den acht NOT-RUN-Fällen bindet den ursprünglichen gesamten
Kataloghash. Der erste Treiber prüfte diesen Pin erst nach dem erlaubten Overlay.
Dieser Start bleibt **BLOCKED vor Workerstart**, nicht als Retrievalergebnis.

Korrigierter Ablauf, separat per Same-Model-Planreview geprüft: zuerst alle
unveränderten Evidencepins aller 24 Fälle gegen das eingefrorene Basispaket
prüfen; danach denselben strengen Katalogguard anwenden und die effektiven
Pakethashes berechnen. Kein Pin wird ausgelassen oder ersetzt. Der ursprüngliche
Corepaketumfang bleibt erhalten. Ein neuer Admissiontest reproduziert die falsche
Reihenfolge rot; seine Gegenprobe mit falschem Pin in einem NOT-RUN-Fall muss vor
Overlay und Runtime stoppen. Das endgültige Paar wird mit derselben korrigierten
Treiberfassung ausgeführt; frühere Starts bleiben gesondert erhalten.

## Ergebnis des endgültigen Vergleichs

Ausgeführt auf `39eabd2`, Katalogkandidat `faa53e3`, eingefrorene übrige Quellen
aus `6b80949`. [Öffentliche Evidence](Rule-Routing-Acceptance-Fix.json) enthält beide
vollständigen Berichte, Roh-/Protokollhashes, Codebindungen und die getrennt
ausgewiesenen früheren Starts. Der oben dokumentierte Vertrag samt Admission-
korrektur ist im Ausführungscommit archiviert; dieser Ergebnisanhang entstand
nach dem Lauf. Keine historischen Ergebnisdateien wurden verändert.

```powershell
.validation/runtime/venv/Scripts/python.exe Evals/Onboarding/run_rule_routing_comparison.py --run --label baseline
.validation/runtime/venv/Scripts/python.exe Evals/Onboarding/run_rule_routing_comparison.py --run --label candidate --catalog-revision faa53e3
```

| Nachweis | Baseline | Katalogkandidat |
| --- | --- | --- |
| 16 unveränderte P1-Retrievalfälle | 15 PASS, 1 FAIL | 16 PASS, 0 FAIL |
| `jobs-acceptance-tests` | FAIL: Akzeptanzkriterien-Owner fehlt | PASS: beide Owner gefunden |
| Zielskill bei `Akzeptanzkriterien beobachtbar` | fehlt | Rang 1 |
| Regression bisher erfolgreicher Fälle | – | keine |
| Acht P2-/P3-Fälle in diesem Treiber | NOT RUN | NOT RUN |
| Quellen während des jeweiligen Laufs | unverändert | unverändert |
| Nativer Index | ready, 165 Dokumente / 155 Skills | ready, 165 Dokumente / 155 Skills |
| Exitcode | 2 wegen bekanntem FAIL | 0 |

Beide Bedingungen nutzen dieselben sieben Code-/Vertragsbindungen, QMD 2.8.3,
Node v24.22.1, zehn Treffer je Query und Case-SHA256
`b29da5a3e7b817dbb7d37485e7628bd38a58f89a0377a1e13414343699b123df`.
Die vollständige Falldatei und der Grader bleiben unverändert. Die nativen Läufe
wurden parallel in getrennten Fixtures ausgeführt; Laufzeiten werden nicht als
Leistungs- oder Effizienzvergleich ausgewertet.

**Quellenvertrag:** Genau `skill-catalog.yml` unterscheidet sich, mit exakt einer
UTF-8-Ersetzung im festgelegten `purpose`. Die übrigen 219 Paketdateien sind
bytegleich, ebenso sämtliche 155 kanonischen Skills. Ein einziges abgeleitetes
Suchdokument ändert sich: das des Zielskills. Sein kanonischer Quellenhash bleibt
gleich, sein Suchdokumenthash ändert sich. Katalog-, Paket-, Fixture- und
Fingerprintwerte sind folgerichtig verschieden. Diese Unterschiede sind kein
Beleg für ein unverändertes Gesamtpaket.

**Weitere Prüfungen:** 80 relevante lokale Tests bestehen ohne Skip, darunter
fünf Admissiontests. Rot/Grün wurde für fehlende Katalogadmission sowie die falsche
Pin-Reihenfolge beobachtet. Zwei Memory-only-Brechproben erkennen umgangene
Katalogadmission und eine entfernte Evidence-Pin-Prüfung; keine Produktdateien
wurden dafür mutiert. Full Harness besteht mit vorhandenen Near-Miss-Warnungen.
Der separate Same-Model-Review hat Code, Rohdaten, öffentliche Bindungen und
Claims ohne Blocker geprüft; keine unabhängige Zertifizierung.

Die beiden vorläufigen Baselinereproduktionen bleiben mit jeweils 15/16 erhalten.
Der erste Kandidatenstart bleibt BLOCKED vor Workerstart; er war kein negativer
Retrievalbefund. Das endgültige Paar ist davon getrennt. Insgesamt wurden in
diesem Slice keine Agenten-CLI-Modellsessions oder direkten Modell-API-Aufrufe
gestartet; die nativen Evals sind modellfrei.

**Entscheidung:** Der Katalogfix erfüllt den bekannten Development-/Regressionsfall.
Suche bleibt optional; allgemeiner Recall und natürliche Agentenauswahl sind
dadurch nicht bewiesen. Keine Änderung an Maturity, Skill-Verträgen, Suchlogik
oder Evaloracles. Die historischen P1-/P5-Urteile bleiben FAIL/PARTIAL für ihre
damaligen Quellenstände. Keine weitere Suche nach Synonymen oder Ausweitung der
Testplattform in diesem Slice.
