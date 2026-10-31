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
