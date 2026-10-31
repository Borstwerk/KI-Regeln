# P5 – Abschlussabnahme und begrenzter Suchpfadvergleich

Vorabvertrag vom 31.10.2026. Basis `c066cc3`, Merge von P4 / PR #116.
Methoden: `agent-eval`, `test-design`, `context-audit`, `verification-loop`;
unabhängiger Reviewer mit `delegation-contract` für Oracle und Evidence.

## 1. Bestehende 24 Fälle

Die eingefrorene [Falldatei](rule-routing-cases.json), Queries und Oracles bleiben
unverändert. Drei vorhandene native Treiber werden am fixierten Codezustand erneut
ausgeführt und in einem Bericht zusammengeführt:

- `run_rule_routing_comparison.py --run --label candidate`: 16 direkte P1-Suchfälle
  auf dem unveränderten Quellenpaket `6b80949`; gleiches Top-10-Budget, historische
  Kernpaketidentität und separat ergänzte Workflowabhängigkeiten;
- `run_rule_routing_p2_native.py --run`: drei technische Verträge mit nativer
  Pagination, Staleness und QMD-freier Auflistung; definierte synthetische Quellen;
- `run_rule_routing_p3_native.py --run`: fünf Beziehungs-/Quellenverträge aus den
  übrigen vier Beziehungsfällen und dem ungültigen strukturierten Ziel.

Damit wird jede der 24 IDs genau einmal ihrer Prüfart zugeordnet. Verschiedene
Quellen und synthetische Fixtures bleiben ausdrücklich verschieden. Keine
Gesamterfolgsquote aus technischen Verträgen, Retrieval und Agentenreview bilden.
Frische Ergebnisse mit historischen vergleichen; der bekannte P1-Fehlfall darf
weiter FAIL bleiben. Exit 2 des P1-Treibers ist bei diesem offenen Fall sichtbar.
Keine historische Evidence überschreiben und keine Schwelle nach dem Lauf ändern.

## 2. Genau zwei frische CLI-Sessions

Der vorhandene [P4-Treiber](run_rule_routing_p4.py) erhält ausschließlich einen
festen `--compare`-Modus; kein weiterer allgemeiner Runner. Vorbereitung ist der
Default, Modellaufrufe nur mit `--compare --run`.

Beide Bedingungen verwenden exakt die P4-Entwicklungsaufgabe, denselben kanonischen
Produktsnapshot, vorhandenen CLI-/ChatGPT-Login, `gpt-6.1-sol` mit `high`, gleiches
Outputschema, gleiche Tools/Rechte und vorgebauten QMD-Index. Ein eigener leerer
Arbeits-/Cachezustand pro Bedingung; Basisdateien und Indexfingerprints müssen
identisch sein. Evaluationsdateien, Tests, alte Antworten und Umsetzungsplan fehlen
im Snapshot. Die Bewertungsregeln erreichen den Modellprompt nicht.

Reihenfolge: **free**, dann **guided**. Free erhält freie Werkzeugwahl. Guided
erhält zusätzlich ausschließlich die Anweisung, nach Pflicht-Reads den vorhandenen
Routing-Suchpfad und belegte Beziehungshinweise zu benutzen. Keine Query, Skill-ID
oder richtige Antwort wird vorgegeben. Der genaue Zusatz wird vor Modellstart im
Protokoll gespeichert. Guided ist **angeleitete Toolnutzung**, kein natürlicher
Discovery-Nachweis. Free darf ebenfalls den Index verwenden.

Je Bedingung genau ein Modellversuch, höchstens 240 Sekunden. Kein Resume,
Nachprompten, Best-of oder automatischer Ersatzlauf. Laufzeit-/Auth-/Quotafehler
bleiben BLOCKED; ohne zwei auswertbare Ergebnisse kein Effizienzvergleich.
Byte-/Read-only-Gegenprobe vor dem ersten Modellaufruf. Keine Installation, direkte
Modell-API oder neuen Dienste. Dieselbe grobe Sandbox-/Junction-Grenze wie in P4;
Quellhashes und Gitstatus danach prüfen, keine vollständige Oracleabschottung behaupten.

## 3. Vorab fixierte Bewertung

Produkt und Prozess separat. Für beide Bedingungen gilt das unveränderte
P4-Development-Oracle: Software-Workflow; eigenständige Jobs für `task-graph`,
`delegation-contract`, `context-engineering`, `test-design`, `code-review` und
geeignete Implementierungs-/Verifikationsdisziplin. Geplante Phasen sind keine
bereits ausgeführte Implementierung. TDD oder begründete Alternative nach
Description-Prüfung, wie im ursprünglichen Oracle. Pflicht-Reads und Owner-
Descriptions anhand tatsächlicher Tooloutputs prüfen. Reviewer liest Ergebnis
gegen Aufgabe und Quellen; mechanische Checks getrennt von qualitativer Bewertung.

Gleiche Ergebnisqualität setzt voraus: dieselben erforderlichen Jobs abgedeckt,
Abhängigkeiten/Dateieigentum von zwei Agenten geklärt, konkrete Grenztests,
Kontext-/Nachladeplan, unabhängiger Codecheck und ehrlicher Ausführungsstatus.
Mehr Tokens bei schlechterem Ergebnis sind ebenso wenig Erfolg wie weniger
Tokens bei verlorenen Pflicht-Reads oder fehlenden Ownern. Guided erhält zusätzlich
eine eigene Bewertung der tatsächlich beobachteten Such-/Hinweisnutzung; fehlende
Nutzung macht diesen Pfad nicht nachgewiesen. Einzelne unbenutzte Funktionen wie
Pagination bleiben NOT RUN, wenn sie für die Aufgabe nicht benötigt werden.

Erfassen je Session: Dauer, Commandzahl, UTF-8-Größe der tatsächlich aufgezeichneten
Tooloutputs, gemeldete Input-/Cached-Input-/Outputtokens, Owner-/Workflow-/Overlay-
Reads, Such-/Relations-/Pagingnutzung, Quellintegrität und Reviewbefunde. Große oder
wiederholte Outputs anhand der Traces nennen; Zeichen-/Bytezahlen nicht in geschätzte
Tokens umrechnen. Tokenusage summiert Modellschritte und ist keine einmalige
Kontextgröße. Keine Geld-/Preis- oder Cache-Abrechnungsannahmen.

Einmalige feste Reihenfolge, Provider-Caches und stochastisches Verhalten bleiben
Störfaktoren. Kein randomisierter, wiederholter oder Held-out-Versuch. Höchstens ein
**beobachteter Unterschied in diesem Paar** bei vergleichbarem Outcome; kein
kausaler/generaliserbarer Spar-Lift und kein neuer universeller Grenzwert.

## 4. Abschluss und Entscheidung

Bestehende relevante lokale Tests und Full Harness frisch ausführen. Kontrollierte
Gegenproben müssen fehlende Pflicht-Reads und eine fälschliche positive Einstufung
ohne Suchnutzung erkennen. Originale Traces bleiben lokal; öffentliche Evidence
enthält geprüfte Auszüge/Digests ohne Reasoning, Credentials oder private Pfade.

Nach Evidence entscheiden, ob eine kleine Routingänderung fachlich begründet ist.
Aus einer einzigen Paarung entsteht keine automatische Regelpromotion. Bei
gemischtem/offenem Ergebnis bleibt die Suche optional; ein möglicher Folgeschritt
wird mit konkretem Befund statt spekulativer neuer Infrastruktur beschrieben.
Suchcode, AGENTS, kanonische Skills und Oracles werden in diesem Slice nicht geändert.

Status vor Ausführung: **NOT RUN**. Allgemeine semantische Vollständigkeit bleibt
UNVERIFIED. Frühere P4-Ergebnisse bleiben historische getrennte Prozess-Evidence.

## Ergebnis vom 31.10.2026: Gesamtabnahme PARTIAL

Vorabvertrag und ausgeführter Code: `4e301fe`. Der [JSON-Bericht](Rule-Routing-P5.json)
verbindet alle 24 IDs mit frischen Rohberichten und bindet Code, Quellen,
Protokolle, Antworten und Tooloutputs per SHA256. Alte Berichte und Oracles bleiben
unverändert. Zwei Modellantworten wurden aufgezeichnet; keine Wiederholungen oder
nachträgliche Auswahl aus mehreren Antworten.

### Bestehende Fälle frisch geprüft

| Prüfart | Ergebnis | Geltungsbereich |
| --- | --- | --- |
| P1, 16 direkte Suchfälle | 15 PASS, 1 FAIL; PARTIAL | unverändertes Quellenpaket `6b80949`, aktueller Code; alle Fallpayloads, Ränge, Scores und Inhaltshashes identisch zur vorherigen Regression |
| P2, drei technische Verträge | 3 PASS | 14 native Treffer auf vier Seiten, globale Ordnung; 155 Descriptions auf sieben Seiten; stale/alte Cursor vor Worker abgewiesen |
| P3, fünf Beziehungs-/Quellenverträge | 5 PASS | gerichtete Beziehungen, expliziter Workflow-/Checkpointpfad, Leertreffer und ungültige Ziele mit Herkunfts-/Quellguards |

Jede ID ist genau einmal zugeordnet; diese verschiedenen Prüfarten werden nicht
zu einer Qualitätsquote vermischt. Einziger offener Retrievalfall bleibt
`jobs-acceptance-tests`: `acceptance-criteria-design` fehlt für die eingefrorene
Query. Der P1-Treiber endet deshalb weiterhin mit Exit 2. P1 ist ein frischer
Code-Regressionslauf auf dem alten Paket, kein Suchlauf auf den inzwischen
geänderten Router-Dokumenten. Die 220 kanonischen P3-Quellpfade und operativen
Suchdateien sind gegenüber der P4-Basis bytegleich. Allgemeiner Recall bleibt
UNVERIFIED.

### Freie und angeleitete Werkzeugwahl

Beide vorbereiteten Arbeitsverzeichnisse enthalten dieselben 578 Quelldateien;
ihre vorgebauten Indexmetadaten einschließlich Fingerprint sind identisch. Beide
Sessions enden mit Exit 0 und liefern einen Plan mit den erwarteten Ownern,
Dateigrenzen für zwei Agenten, Abhängigkeiten, Grenztests, Nachladeplan und
unabhängigem Codecheck. Die tatsächlichen Router-/Workflow-/Owner-/Overlay-Reads
wurden von Integrator und unabhängigem Review-Agenten geprüft. Das ist keine
menschliche Blindabnahme oder automatische Judge-Pipeline.

| Bedingung | Produkt-/fachliches Routing-Oracle | Striktes technisches Sauberkeits-Gate |
| --- | --- | --- |
| free | PASS im festen Planungsfall | PASS |
| guided | PASS im festen Planungsfall | **FAIL**: `?? tools/__pycache__/` |

Alle ursprünglichen Quelldateien bleiben unverändert. Guided erzeugte jedoch zwei
ungetrackte `.pyc`-Dateien für `check_public_entrypoints` und `rule_relations`.
Die Artefakte sind mit einem Python-Importeffekt vereinbar; eine bewusste direkte
Quellschreiboperation ist im Trace nicht beobachtet. Das strikte Git-Gate wird
trotzdem nicht nachträglich gelockert: **Batch-Exit 2 bleibt bestehen**.

Zusätzlich meldete die erste tatsächliche Guided-Abfrage `missing`, obwohl der
Vorbau außerhalb der Agentensandbox ready gemeldet hatte. Der Agent baute den Cache
explizit neu auf und suchte danach weiter. Eine ergänzende **modellfreie Read-only-
Probe** kann den vorbereiteten Free-Pointer lesen, erhält aber AccessDenied für
dessen Snapshot und SQLite-Datei. Diese Probe unterstützt einen Zusammenhang mit
dem Ausführungskontext beziehungsweise Cachezugriff; sie benutzt einen anderen
Read-only-Pfad und beweist nicht die genaue Ursache der ursprünglichen
Workspace-write-Abfrage. Diese Ursache bleibt UNVERIFIED.

Guided hat den angeleiteten Suchpfad tatsächlich verwendet: zehn aufgezeichnete
Abfrageantworten, davon eine `missing`, eine erfolgreiche leere Wiederholung und
acht weitere erfolgreiche Abfragen. Die 70 gelieferten Hinweisinstanzen stimmen
mit den kanonischen Beziehungen überein, darunter `test-design → tdd` und
Skill-Nennungen im Software-Workflow. Free nutzte direkte Dateien. Expliziter
Relationsabruf, Paging und Descriptorlisting wurden von beiden Agenten nicht
verwendet und bleiben als Agentenpfade NOT RUN. Guided ist angeleitete Nutzung,
kein Nachweis spontan gewählter Suche.

### Aufwand: ausschließlich deskriptive Beobachtung

| Messwert | free | guided |
| --- | ---: | ---: |
| CLI-Laufzeit, Sekunden | 89,67 | 180,11 |
| Toolkommandos | 10 | 17 |
| aufgezeichnete Tooloutputs, UTF-8-Bytes | 185684 | 271747 |
| gemeldete Inputtokens | 219909 | 667761 |
| darin gemeldete Cached-Inputtokens | 167168 | 582784 |
| gemeldete Outputtokens | 2791 | 4550 |

Für die Bytezählung werden die Rohberichte ausdrücklich als UTF-8 gelesen und
die enthaltenen Outputstrings erneut als UTF-8 gezählt. Windows-Locale-Dekodierung
würde die Zeichen und damit die Bytezahlen verfälschen. Zeichen-/Bytezahlen werden
nicht in geschätzte Tokens umgerechnet; Usage summiert mehrere Modellschritte.

Die nativen Checks und lokalen Tests wurden parallel zum Paar gestartet und
können die Laufzeiten ungleich beeinflusst haben. Die Reihenfolge und
Provider-Caches waren ebenfalls nicht kontrolliert. Guided musste zusätzlich den
Cache neu aufbauen. Zusammen mit dem gescheiterten technischen Gate sind die
Bedingungen für einen belastbaren Effizienzvergleich **nicht erfüllt**. Die
höheren beobachteten Werte belegen weder eine allgemeine Ineffizienz der Suche
noch einen Spar-Lift. Doppelte Owner-Reads und breite Katalog-/Suchoutputs sind
konkrete Beobachtungen, keine isoliert nachgewiesene Ursache.

### Verifikation und Entscheidung

103 relevante lokale Tests: OK mit einem bestehenden Windows-Symlink-Skip.
Die Byte-/Read-only-Gegenprobe besteht. Mechanische Evidence-Checks bestätigen
Router- und Description-Reads separat; kontrollierte Kopien ohne tatsächlichen
Master-Router-Output beziehungsweise ohne erfolgreiche Suchantwort werden
zurückgewiesen. Das technische Guided-Gate bleibt dabei ausdrücklich FAIL.

Der unabhängige Abschlussreview bestätigt Fallzuordnung, Code-/Quellen-/Rohhashes,
öffentliche Auszüge, UTF-8-Metriken und Redaktion ohne Artefaktblocker. Dieses
bestandene Artefaktreview hebt weder den Retrieval-FAIL noch das technische
Guided-Gate oder die Grenze des Effizienzvergleichs auf.

**Keine Routingpromotion:** Suche bleibt optional. AGENTS, Skills, Suchlogik und
Maturity werden nicht geändert. Die Gesamtabnahme bleibt PARTIAL wegen der
bekannten Retrieval-Lücke und des nicht belastbaren Effizienzvergleichs.

Ein sinnvoller separater Folgeschritt ist ein kleiner technischer Fixture-Fix:
Bytecode-Artefakte vermeiden und den Cache im tatsächlichen Ausführungskontext
vorab auf Lesbarkeit prüfen. Erst danach wäre ein neuer, ausdrücklich abgegrenzter
Vergleich fachlich begründet. Diese beiden Modellantworten werden dafür weder
gelöscht noch als erfolgreiche Ausgangsbedingung umetikettiert.
