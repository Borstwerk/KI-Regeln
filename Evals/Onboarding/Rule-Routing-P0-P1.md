# Routing-Suche P0/P1: Quellenvertrag und fairer Vergleich

Vorabstand vom 30.10.2026. Autorisierter Plan:
[Skill-Routing-Suche-Umsetzungsplan](../../Dokumentation/Skill-Routing-Suche-Umsetzungsplan.md).
Dieser Slice liefert zunächst P0 und P1; spätere Parameter und Beziehungen bleiben
separat abzunehmen. Historische Evidence wird nicht überschrieben.

## P1-Vertrag vor der Implementierung

- `read_snapshot()` liefert weiterhin unveränderte kanonische Dateien; `metadata.files` enthält ihre Original-SHA256-Werte.
- `metadata.skills` bleibt kompatibel. Ergänzend `routing_format: 2`, `routing_facets` mit `id`, `area`, `purpose` je Skill-Pfad und `search_documents` mit den Hashes aller tatsächlich indexierten Dokumente.
- `area` muss ein nichtleerer String sein, `purpose` den kanonischen nichtleeren Stringvertrag mit mindestens 20 Zeichen erfüllen. Ungültige Facets stoppen vor dem Worker.
- Pro Skill bleibt ein Suchdokument am gleichen Pfad. Es enthält die unveränderten Originalbytes am Anfang und einen deterministischen, als abgeleitet gekennzeichneten Kataloganhang. Guides bleiben bytegleich.
- Originalexport und tatsächlich erzeugter Suchcorpus durchlaufen den bestehenden Manifestvalidator. Keine Budgeterhöhung oder zweite gepflegte Registry.
- Der Workerhash wird gegen `search_documents` geprüft. Öffentliche Treffer behalten `content_sha256` als kanonischen Quellenhash; `search_document_sha256` bezeichnet separat die indexierten Bytes.
- `snippet_origin: derived-search-document` und `sources` mit Skill-/Katalogpfad, Originalhash und Feldreferenzen machen die Herkunft sichtbar. Ein generiertes Snippet ist kein Originalzitat.
- Der Fingerprint bindet Facets, Original- und Suchtexthashes. Alte Indizes werden stale. Der Inhaltsmodus bleibt unverändert.

## Vorher/Nachher

Der feste [Vergleichslauf](run_rule_routing_comparison.py) und die
[Falldatei](rule-routing-cases.json) werden vor Codeänderung eingefroren und ihre
Erwartungen unabhängig geprüft. Noch nicht implementierte P2/P3-Fälle werden
ausdrücklich NOT RUN, nicht als Retrievalerfolg gewertet.

```powershell
.validation/runtime/venv/Scripts/python.exe Evals/Onboarding/run_rule_routing_comparison.py --run --label baseline
# nach P1, mit unveränderter Falldatei und derselben Quellenbasis:
.validation/runtime/venv/Scripts/python.exe Evals/Onboarding/run_rule_routing_comparison.py --run --label candidate
```

Beide Läufe exportieren dieselben geprüften Originalquellen aus
`6b80949fea00a427303a8dad9a612b59d7fd04ca` in ein isoliertes temporäres Git-Repo.
Feste Git-Zeitstempel machen dessen Revision reproduzierbar. Quellenpaket-, Case-,
Protokoll-, Controller-, Worker- und Lockfile-Hashes sowie Node/QMD-Version werden
aufgezeichnet. Keine Installation, direkte API oder Modellaufrufe.

Je P1-Fall: unveränderte Queries, zehn Kandidaten je Query, Pflichtskills und
Alternativgruppen als Oracle. Mehrteilige Jobs verwenden vorher definierte einzelne
Queries; beide Varianten bekommen dieselben Queries und dasselbe Budget. Unpassende
Kandidaten sind Rauschen; erst ihre Aktivierung wäre ein Prozessfehler.

Der ursprüngliche ADR-Fall muss nach P1 den erwarteten Skill finden. Bereits
erfolgreiche historische Fälle dürfen nicht regressieren. Weitere unerfüllte
Erwartungen bleiben FAIL/PARTIAL, ohne nachträgliche Case- oder Schwellenänderung.
Der modellfreie Vergleich belegt keine natürliche Agentenauswahl oder allgemeine
semantische Vollständigkeit.

## Ergebnis

Die Kriterien wurden in `5bb94fe` eingefroren. Case-SHA256:
`b29da5a3e7b817dbb7d37485e7628bd38a58f89a0377a1e13414343699b123df`.
Ein erster Fixture-Aufbau stoppte vor dem Worker, weil ein Manifest-Einstieg
außerhalb der 165 Suchdokumente fehlte. Der Treiber ergänzt seit `fcd4ef5` auch
die verpflichtenden Manifest-Einstiege; Fälle und Grader blieben unverändert.

Der vollständige Vorher-Lauf auf dem unveränderten Controller ergab **13 PASS,
3 FAIL, 8 NOT RUN**. Fehlfälle: ursprüngliche ADR-Frage, Akzeptanzkriterien im
Mehrjob-Fall und Claim-/Quellenprüfung im Mehrjob-Fall. Die acht späteren Fälle
sind kein Bestandteil der P1-Retrievalquote.

Baseline-Rohbericht: `.validation/rule-routing-baseline-duasujmz/result.json`.
Quellenpaket-SHA256: `02575304ff5a45aea1bc2ab73c0051c1894525f4dcd17655057434deb53b4be2`.
Reproduzierte Fixture-Revision: `191baec96637be68e71da79c2a02bd959f01f5ab`.

Der Candidate-Lauf auf `055d0bb` ergab **15 PASS, 1 FAIL, 8 NOT RUN**.
Die [maschinenlesbare Evidence](Rule-Routing-P0-P1.json) enthält beide Rohberichte,
ihre Hashes und den fallweisen Vergleich. Der erste erfolgreiche Baseline-Lauf
ist an `fcd4ef5` gebunden. Die Codehashes binden die ausgeführten Checkoutbytes;
zur jeweiligen Git-Fassung ist entweder exakte Gleichheit oder dokumentierte
CRLF/LF-Äquivalenz geprüft. Nur der Suchcontroller unterscheidet sich unter den gebundenen
Code-/Worker-/Validator-/Lockfile-/Treiberdateien.

| Nachweis | Vorher | Nachher |
| --- | --- | --- |
| Ausgewertete P1-Suchfälle, inklusive Leertreffer | 13/16 bestanden | 15/16 bestanden |
| ursprüngliche ADR-Frage | FAIL | PASS |
| Claim-/Quellenprüfung als Mehrjob-Fall | FAIL | PASS |
| Akzeptanzkriterien als Teil eines Mehrjob-Falls | FAIL | FAIL |
| Regression bisher bestandener Fälle | – | keine |
| Acht spätere P2/P3-Fälle | NOT RUN | NOT RUN |
| Kanonische ausgewählte Originalbytes | unverändert | unverändert |

Die bisher erfolglose Query `Akzeptanzkriterien beobachtbar` findet weiterhin
`acceptance-criteria-design` nicht. Der Fall wird nicht umformuliert oder durch
nachträglich gepflegte Synonyme repariert. Die geplante vollständige Descriptor-
Prüfung bleibt ein eigener nächster Slice.

Quellenpaket, Casehash, Fixture-Revision, Node/QMD-Version und Querybudget stimmen
zwischen den beiden Läufen exakt überein. Der Verbesserungsclaim ist auf diese
bekannten Entwicklungsfälle begrenzt. **Gesamturteil bleibt PARTIAL**, kein
allgemeiner Recall- oder Agentenqualitätsnachweis.

## Controllerprüfung und Scope

75 relevante lokale Unit-Tests bestehen mit einem bestehenden Windows-Symlink-Skip.
Sechs zusätzliche Facet-Methoden prüfen Corpusableitung, Originalpräfix,
Hashtrennung, konkrete Facetfehler, Metadaten-Staleness und die tatsächlichen
Datei-/Gesamtbudgets vor dem Worker. Sie sind kein QMD-Retrievalnachweis.

Zwei echte Red/Green-Schritte: fehlende Ableitungsmetadaten und fälschlich
akzeptierter kanonischer Hash anstelle des indexierten Ableitungshashes. Die alte
Routing-Fixture wurde an den ausdrücklich genehmigten Anhangsvertrag angepasst:
Originalpräfix und Katalogtext werden geprüft; Guides bleiben bytegleich.
Keine Abschwächung des eigentlichen Herkunfts-/Budgetvertrags. Unabhängiger
Source- und Testreview: keine offenen P1/P2 im geprüften Scope.

P0 und der technische P1-Slice sind geliefert. Paging, vollständige Descriptor-
Enumeration, Beziehungsableitung und natürliche Agentenauswahl bleiben **NOT
IMPLEMENTED / NOT RUN**; die acht späteren Fälle werden nicht als PASS gezählt.
