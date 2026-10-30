# Eigenständige lokale Suche für KI-Regeln

Die optionale Suche verwendet [QMD 2.8.3](https://github.com/tobi/qmd/tree/facd35e01359e59d938bc9418e93fb9318addee3)
direkt als lokale Engine. Dieser erste Suchweg ist **BM25-Volltextsuche**:
keine Embeddings, Query-Expansion, Reranker, Modell-APIs oder API-Schlüssel.
Ein kurzer Suchbegriff mit passenden Fachwörtern funktioniert besser als eine
lange Frage oder eine bloße Umschreibung. Semantische Suche ist nicht nachgewiesen.

## Einmal einrichten und suchen

Windows-Voraussetzungen: Git, Node.js ab 22 und pnpm 11; die vorhandene
Harness-Python-Umgebung wird mit `Validate-KI-Regeln.ps1 -Quick` vorbereitet.
Die optionale Node-Abhängigkeit gehört nicht zum normalen Validation Harness.

```powershell
.\Search-KI-Regeln.ps1 -Setup
.\Search-KI-Regeln.ps1 -Build
.\Search-KI-Regeln.ps1 -Query 'Skill Verbesserung Fehler'
.\Search-KI-Regeln.ps1 -Status
```

`-NodePath` und `-PnpmPath` nehmen bei Bedarf vorhandene lokale Executables an.
Ohne explizite Angabe wird zuerst im `PATH` gesucht, danach in der gegebenenfalls
bereits vorhandenen Codex-Laufzeit unter
`~/.cache/codex-runtimes/codex-primary-runtime/dependencies/` (`node/bin/node.exe`,
für Setup zusätzlich `bin/fallback/pnpm.cmd`). Ein ausdrücklich angegebener,
ungültiger Pfad wird nicht ersetzt. Für pnpm wird das gefundene Node-Verzeichnis
nur während des Setups dem Prozess-PATH vorangestellt; die Umgebung bleibt unverändert.
Ein fehlendes Node meldet `runtime-missing` mit Hinweis auf `-NodePath`, statt eine
fehlende QMD-Installation zu behaupten. Diese Suche installiert nichts.
Nur `-Setup` lädt Pakete herunter: feste Version, Transitivstände und Integritäten
aus `tools/local_search/pnpm-lock.yaml`, keine Installationsskripte oder globale
Installation. Die mitgelieferten QMD-Agent-Skills und Release-Hooks werden nicht
in die Agentenlaufzeit eingebunden oder aktiviert. Ein mit `--ignore-scripts` eingerichtetes natives
Paket muss auf der jeweiligen Plattform lauffähige Bindings enthalten; andernfalls
meldet die Suche einen Runtime-Fehler. Es gibt keine automatische Kompilierung.

Für eine vorhandene Python-/Node-Laufzeit auf anderen Systemen ist der gleiche
Controller nutzbar:

```sh
python tools/search_rules.py build
python tools/search_rules.py search 'Teststrategie Grenzwerte'
```

Der Node-Paketordner bleibt auch dabei `.validation/qmd-runtime/`. Die
PowerShell-Einrichtung ist der Windows-Einstieg; ein anderer Plattformlauf ist
gesondert zu verifizieren.

## Quellen, Aktualität und Ergebnis

Ein Build fixiert einmal den vollständigen Git-Commit von `HEAD`. Manifest und
ausgewählte reguläre Dateiblobs werden daraus mit kanonischen LF-Bytes exportiert
und **im exportierten Abzug** mit dem bestehenden Manifestvalidator geprüft.
Ohne `-Routing` wird nur die explizite Auswahl in [mara-project.json](../mara-project.json) gesucht.
Der Manifestname bleibt aus Kompatibilitätsgründen bestehen; die Suche arbeitet
als eigenständiges Werkzeug dieses Repositories.

Ausgewählte uncommittete Änderungen sind kein freigegebener Suchstand. Nach einem
Commit oder einer Quellen-/Manifeständerung wird der vorhandene Index `stale`;
`-Build` aktualisiert ihn bewusst. Es gibt keinen Hintergrund-Sync. Ein fehlender
oder fehlgeschlagener Build liefert keine alten Treffer. Ein exklusiver Lock
verhindert konkurrierende Aufrufe. Nach einem Prozessabbruch kann ein Lock
zurückbleiben; vor manuellem Entfernen sicherstellen, dass kein Suchprozess läuft.

QMD erhält ausschließlich abgeleitete Kopien unter `.validation/rule-search/`.
Ein Build muss alle erwarteten aktiven Dokumentpfade und null übersprungene Dateien
nachweisen; ein Teilindex wird nicht veröffentlicht. Vor und nach einer Suche
werden Quellen und Revision erneut geprüft. Treffer enthalten Pfad, Commit,
Fingerprint, Score und einen Auszug bis 600 Zeichen; höchstens fünf Treffer,
Suchbegriffe bis 500 druckbare Zeichen. Leere Trefferlisten sind zulässig.

Die Originaldateien bleiben unverändert. Abgeleitete Build-Verzeichnisse bleiben
lokal erhalten; sie können nach Beenden aller Suchprozesse bewusst entfernt und
neu aufgebaut werden. Es gibt keine automatische rekursive Bereinigung.

Ein Treffer ist ein Wegweiser. Für eine fachliche Aussage die Originalquelle am
genannten Commit lesen; Suchtext ist keine neue Anweisung oder Freigabe.
[AGENTS.md](../AGENTS.md), Router, kanonische Skill-Descriptions und lokale
Projektwahrheit bleiben verbindlich. Dies ist kein Ersatz für Pflicht-Discovery.

## Routing über alle katalogisierten Skills

Die begrenzte Inhaltsauswahl reicht für allgemeines Skill-Routing nicht aus.
Der getrennte Routing-Bestand wird deshalb unmittelbar aus `skill-catalog.yml`
abgeleitet: alle dort referenzierten kanonischen `SKILL.md`-Dateien, die bestehenden
neun Core-Dokumente und `Workflows/README.md`. Es gibt keine zweite gepflegte Skill-Liste.
Aktuell sind das 155 Skills in 165 Dokumenten. Die bestehenden Auswahlbudgets bleiben
unverändert; überschreitet der abgeleitete Bestand sie künftig, schlägt der Build fehl.

Pro Skill enthält das Suchdokument zusätzlich einen deterministisch abgeleiteten
Anhang mit ID, Fachbereich und `purpose` aus dem Katalog. Der kanonische Skill-Inhalt
bleibt als unveränderter Präfix erhalten; es entstehen keine weiteren Dokumente
und keine zweite gepflegte Begriffsliste. Sowohl Originalauswahl als auch tatsächlich
indexierter Text müssen die bestehenden Umfangsgrenzen einhalten. Ein älterer
Routing-Index wird durch das geänderte Format stale und muss neu gebaut werden.

```powershell
.\Search-KI-Regeln.ps1 -Routing -Build
.\Search-KI-Regeln.ps1 -Routing -Query 'Rechtschreibung Zeichensetzung'
.\Search-KI-Regeln.ps1 -Routing -Status
```

Der gleiche Controller und dieselben Quellenprüfungen verwenden dafür einen
eigenen Cache unter `.validation/rule-routing/`. Der Inhaltsindex bleibt getrennt.
Katalog, Workflow-Index und Overlay-Registry sind zusätzliche fingerprintete
Quellenabhängigkeiten: Auch deren Änderung macht den Routing-Index veraltet.
Die vollständigen Workflow-Dateien werden nicht zusätzlich indexiert; bei einem
plausiblen Workflow weiterhin `workflow-index.yml` und den passenden Workflow öffnen.

Routing-Antworten enthalten standardmäßig zehn Treffer je Seite; `-Limit` erlaubt
1–50 Einträge. Skill-Treffer tragen `kind: skill`
sowie ID, kanonische Description, Maturity und Eval-Coverage; andere Treffer sind
`kind: guide`. `routing_sources` verweist auf die verbindlichen Router,
`routing_coverage` weist die indexierte Skill-Anzahl aus. `candidates_only: true`
kennzeichnet das Ergebnis als Kandidatenhilfe. Vollständige Quellenabdeckung ist
kein Nachweis, dass eine einzelne Anfrage alle relevanten Skills findet.

`content_sha256` bleibt der Hash der kanonischen Originaldatei.
`search_document_sha256` bindet separat die tatsächlich indexierten Bytes.
Skill-Snippets tragen `snippet_origin: derived-search-document` und `sources` mit
Original- und Kataloghash sowie Feldreferenzen. Sie können Katalogtext enthalten
und sind deshalb keine wörtlichen Zitate allein aus `SKILL.md`. Guide-Snippets
tragen `canonical-source`. Beide Hasharten und die Quellenabhängigkeiten werden
vor/nach der Suche gegen den fixierten Stand geprüft.

Auch ähnliche Formulierungen können leer bleiben. Im bisherigen nativen
Entwicklungsfall fand `Architekturentscheidungen Alternativen Konsequenzen` den
Skill `adr` nicht. Dieser historische Fehlfall bleibt dokumentiert; die Aufnahme
der Katalogtexte wird mit einem getrennten
[Vorher/Nachher-Vergleich](../Evals/Onboarding/Rule-Routing-P0-P1.md) geprüft.

Agenten verwenden den optionalen Suchpfad aus [AGENTS.md](../AGENTS.md) und
[Skill-Handbuch.md](Skill-Handbuch.md): Aufträge in Teiljobs zerlegen, je Job suchen,
aktuelle Original-Descriptions und Near-Misses prüfen, Workflow-Kern und Overlays
direkt berücksichtigen. Bei fehlender Runtime, fehlendem/veraltetem Index sowie
leeren oder unpassenden Treffern mit gezielter Katalog-/Dateisuche fortfahren.
Ein Suchfehlschlag rechtfertigt kein `none`. Es gibt keine automatische Skill-Aktivierung.

## Weitere Treffer und vollständige Beschreibungslisten

```powershell
.\Search-KI-Regeln.ps1 -Routing -Query 'Skill' -Limit 10
.\Search-KI-Regeln.ps1 -Routing -Query 'Skill' -Cursor '<next_cursor>'
.\Search-KI-Regeln.ps1 -Routing -ListSkills -Limit 25
.\Search-KI-Regeln.ps1 -Routing -ListSkills -Cursor '<next_cursor>'
```

Die Suche prüft zunächst alle vom nativen BM25-Aufruf gelieferten Treffer innerhalb
des begrenzten Corpus, ordnet sie global nach Score absteigend und Pfad aufsteigend
und schneidet dann Seiten. `total_matches` beschreibt diese Ergebnismenge;
`offset`, `page_size`, `has_more` und `next_cursor` beschreiben die angezeigte Seite.
Die Gesamtzahl ist keine Zahl aller fachlich relevanten Skills. Der Inhaltsmodus
ohne `-Routing` bleibt bei höchstens fünf Treffern und akzeptiert keine Pagingoptionen.

Für eine Fortsetzung dieselbe Query verwenden. Die Seitengröße kann entfallen,
dann gilt die im Cursor gebundene Größe. Query-, Aktions-, Größen-, Quellen- oder
Ergebniswechsel führen zu einem sichtbaren Fehler; nach Quellenänderung ggf.
Index neu bauen und wieder bei Seite eins beginnen. Beschädigte Cursor werden
zurückgewiesen. Cursor sind Kontext-/Korruptionsschutz, keine geheim signierten
Autorisierungstoken. Es gibt keinen Sessiondienst und keinen zusätzlichen Secret-Speicher.

`-Routing -ListSkills` liest die geprüften Gitquellen direkt: kein Node/QMD-Aufruf
und kein bereiter Suchindex erforderlich. Die Ausgabe hat `mode: catalog`,
`total_skills`, dieselben Seitenfelder und eine nach ID sortierte `skills`-Liste.
Jeder Eintrag enthält kanonische Description, ID/Pfad, Katalog-Zweck/Fachbereich,
Maturity, Eval-Coverage, Capabilities, `related` und Quellenhashes/Feldherkunft.
Standardgröße ist 25, explizit ebenfalls 1–50. Optionale Listen ohne Eintrag sind leer.

Über alle Seiten erscheint jede Katalog-ID genau einmal. `assessment_performed:
false` und `candidates_only: true` machen klar: Ausliefern ist kein Lesen,
Bewerten oder Aktivieren. Die gründliche fachliche Prüfung bleibt beim Agenten;
ungeprüfte oder unklare Einträge erlauben keinen vollständigen Prüfclaim.
Diese Auflistung ersetzt keine Pflicht-Discovery und erzwingt keinen Vollscan.

Setup/Build/Status akzeptieren keine Pagingoptionen. Ungültige Kombinationen
stoppen vor Installation oder Indexmutation. Der vorhandene Harness-Python und
Git bleiben nötig; auch die direkte Auflistung nutzt lokale Snapshot-/Lock-Schreibrechte.

Build und Suche brauchen lokale Schreibrechte auf den jeweiligen abgeleiteten
Cache (Lock und SQLite). In einer Umgebung ohne diese Rechte reicht der direkte
Katalog-/Dateipfad; keine Installation oder Rechteerweiterung ist für Routing erforderlich.

## Rechte und geprüfter Scope

Das SDK wird mit Inline-Konfiguration verwendet, ohne QMD-CLI-Projekthooks,
MCP-Server oder Skills. Build/Suche rufen nur Indexierung und `searchLex` auf.
Bekannte Modell-Key-Variablen und Node-Import-Overrides werden dem Kindprozess
entzogen. Es wird keine technische Netzwerk- oder gesamte Dateisystem-Isolation
behauptet: Controller und Node-Prozess laufen mit den vorhandenen Benutzerrechten.
Der Scope bleibt die öffentliche, begrenzte Auswahl dieses Repositories.

QMD enthält zusätzlich Agent-Skills und Release-Scripts. Die Inventarisierung
ergab dort unter anderem eine Hook-Installation mit Schreibwirkung auf `.git`.
Diese Teile sind ausdrücklich nicht zur Aktivierung freigegeben. Die eingeschränkte
Nutzung bezieht sich auf den gepinnten SDK-Pfad; ungeprüfte Paketteile und spätere
Semantik-/Modellpfade tragen keinen pauschalen Security-PASS. Installierte
Dependencies behalten ihre eigenen Lizenzdateien; es wird kein Upstreamcode vendored.

## Verifikation

`tests.test_rule_search`, `tests.test_rule_search_routing`, `tests.test_rule_search_facets`
und `tests.test_rule_search_paging` prüfen den Controller mit echten temporären Git-Repos
und einem injizierten Worker. Diese Tests sind kein QMD-Engine-Nachweis.
Reale QMD-Builds und Suchfragen werden separat protokolliert. Keine Aussage über
allgemeine Retrievalqualität, semantisches Ranking, Agentenantworten oder Maturity
aus wenigen Suchbeispielen ableiten.

Der kleine [native Prüflauf](../Evals/Onboarding/run_rule_search_native.py) installiert
nichts. Nach Einrichtung und einem sauberen, committed Quellenstand kann er mit
der Harness-Python-Runtime ausdrücklich gestartet werden:

```powershell
.validation/runtime/venv/Scripts/python.exe Evals/Onboarding/run_rule_search_native.py --run
```

Er baut den abgeleiteten lokalen Index neu, prüft fünf bekannte Suchfälle sowie
synthetische Aktualitäts-/Teilindex-Gegenproben mit der echten Engine und legt
einen neuen Bericht unter `.validation/native-rule-search-*/` ab. Vorabkriterien
und Aussagegrenzen stehen im [begrenzten Nachweis](../Evals/Onboarding/Local-Rule-Search-2026-10-30.md).

Der getrennte [Routing-Nachweis](../Evals/Onboarding/Local-Rule-Routing-2026-10-30.md)
verwendet `run_rule_routing_native.py --run` für den vollständigen Katalogbestand
und bekannte Suchfälle außerhalb der Inhaltsauswahl. Auch dieser Lauf installiert
nichts und ist kein Agenten- oder allgemeiner Recall-Benchmark.

Der [P2-Nachweis](../Evals/Onboarding/Rule-Routing-P2.md) prüft native Trefferseiten,
Snapshotwechsel und vollständige Katalogauflistung mit
`run_rule_routing_p2_native.py --run`. Er installiert nichts und trennt vollständige
Ausgabe von fachlicher Auswahlqualität.
