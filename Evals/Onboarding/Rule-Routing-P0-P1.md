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

Baseline und Candidate: **NOT RUN** bis zur tatsächlichen Ausführung.
