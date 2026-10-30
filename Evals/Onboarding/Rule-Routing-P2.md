# Routing-Suche P2: Trefferseiten und vollständige Beschreibungslisten

Vorabvertrag vom 30.10.2026, Basis `14ff7c8` nach Merge von PR #113.
Scope: P2 des [Umsetzungsplans](../../Dokumentation/Skill-Routing-Suche-Umsetzungsplan.md).
P3-Beziehungen und semantisches Ranking sind kein Teil dieses Slices.

## Vertrag vor Implementierung

- `search(root, query, node=None, worker=call_worker, routing=False, limit=None, cursor=None)` bleibt für alte Aufrufe kompatibel. Neue Pagingparameter nur im Routing-Modus.
- Routing fragt den Worker bis zur Anzahl erlaubter Corpus-Dokumente ab, prüft alle gelieferten Treffer einschließlich solcher außerhalb der angezeigten Seite und weist Dubletten zurück. Ordnung global nach Score absteigend, dann kanonischem Pfad.
- Default zehn Routing-Treffer pro Seite; `limit` explizit 1–50, bool ist kein int. Der Inhaltsmodus bleibt bei fünf Treffern ohne Pagingoptionen.
- Routing-Antworten ergänzen `total_matches`, `offset`, `page_size`, `has_more`, `next_cursor`. Die Gesamtzahl bezieht sich auf die begrenzte native BM25-Ergebnismenge, nicht alle semantisch relevanten Skills.
- Cursor bindet Format, Quellenfingerprint, Aktion, exakte Query, Seitengröße, globale Ergebnismenge und nächste Position. Fortsetzung ohne erneut angegebene Größe übernimmt die Cursorgröße; eine widersprüchliche Größe scheitert.
- Cursor sind lokale Fortsetzungsdaten mit Kontrollsumme und Kontextprüfung, keine Autorisierungstoken oder geheim signierte Nachweise. Beschädigte, strukturell ungültige oder zum Request unpassende Cursor werden sichtbar als `invalid-cursor` zurückgewiesen. Kein Sessiondienst oder zusätzlicher Secret-Speicher.
- Kontextfehler sollen vor dem Worker auffallen; eine veränderte Ergebnismenge trotz gleichem Quellstand stoppt spätestens vor Ausgabe der Folgeseite. Quellen werden weiterhin vor und nach dem Zugriff geprüft.

## Vollständige Auflistung

`list_skills(root, limit=None, cursor=None)` liest geprüfte kanonische Gitquellen
direkt. Dafür sind weder ein bereiter QMD-Index noch Node/QMD-Aufrufe erforderlich.
Die vorhandenen lokalen Schreibrechte für Snapshotvalidierung und Lock bleiben nötig.

Antwort: `status: ready`, `mode: catalog`, Revision/Fingerprint, `skills`,
`total_skills`, `offset`, `page_size`, `has_more`, `next_cursor`,
`assessment_performed: false`, `candidates_only: true` und Router-Verweise.
Default 25 Einträge, explizit 1–50. Ordnung nach kanonischer ID.

Je Skill: `id`, `path`, kanonische `description`, Katalog-`purpose` und `area`,
`maturity`, `eval_coverage`, `capabilities`, `related`, kanonischer
`content_sha256` und `sources` mit Original-/Kataloghash und Feldherkunft.
Optionale Listen ohne Katalogeintrag werden als leere Listen ausgegeben;
vorhandene Listen müssen eindeutige Strings gemäß kanonischem Typvertrag enthalten.

Jede ID erscheint über alle Seiten genau einmal. Ausliefern heißt nicht lesen
oder fachlich beurteilen. Eignung, Near-Miss und Aktivierung bleiben Agentenarbeit.
Leere oder unpassende Suchtreffer rechtfertigen weiterhin kein ungeprüftes `none`.

Geplante zusätzliche CLI-Parameter:

```powershell
.\Search-KI-Regeln.ps1 -Routing -Query 'Skill' -Limit 10
.\Search-KI-Regeln.ps1 -Routing -Query 'Skill' -Cursor '<next_cursor>'
.\Search-KI-Regeln.ps1 -Routing -ListSkills -Limit 25
.\Search-KI-Regeln.ps1 -Routing -ListSkills -Cursor '<next_cursor>'
```

Python: `--routing --limit 25 list-skills` bzw.
`--routing --cursor '<next_cursor>' search -- '<query>'`.
Setup/Build/Status akzeptieren keine Pagingoptionen; nicht unterstützte Kombinationen
stoppen vor Installation oder Indexmutation. Kein neuer automatischer Modellstart.

## Abnahme und Evidence

Die eingefrorenen Fälle `contract-pagination`, `contract-stale` und
`contract-descriptors` aus [rule-routing-cases.json](rule-routing-cases.json)
tragen die fachliche Grundlage. Ihre Kriterien werden nicht geändert.

Controller-Tests: mehr als zehn Treffer, Gleichstände, nicht überlappende Seiten,
vollständige Vereinigung, End-/Leertrefferseite, ungültige Größen/Cursor,
Query-/Aktions-/Snapshotwechsel, falscher Hash außerhalb der sichtbaren Seite,
vollständige kanonische Descriptor-Abdeckung und verbotene Node-/Worker-Aufrufe.

Native Evidence getrennt: synthetischer erlaubter Corpus mit mehr als zehn
gleichartigen Treffern; tatsächliche QMD-Gesamtmenge und globale Reihenfolge prüfen.
Zusätzlich vollständige Descriptor-Seiten des echten Katalogs ohne Node.
Vor Ausführung Code/Kriterien fixieren, Quellen-/Case-/Code-/Protokollhashes erhalten.
Historische P0/P1-Ergebnisse bleiben unverändert und werden nicht umgewertet.

## Controller- und Codeprüfung

85 relevante lokale Tests: OK mit einem bestehenden Windows-Symlink-Skip.
Neun neue Paging-/Descriptor-Methoden verwenden echte Git-Fixtures und kontrollierte
Worker, keinen simulierten Retrieval-Erfolg. Drei echte Red/Green-Schritte deckten
fehlende Pagingparameter, fehlende Descriptor-API und die noch fehlende CLI ab.

Das unabhängige Review fand eine PowerShell-Coercion: `[int]$Limit` akzeptierte
`1.5` als 2 und `$true` als 1. Beide Fälle wurden tatsächlich als ready/Exit 0
beobachtet. Der Wrapper reicht Werte jetzt als Text zum kanonischen Python-Parser;
beide Negativfälle liefern Exit 2. Ungültige Build-/Status-Pagingkombinationen und
Listing ohne Routing sind vor Dispatch regressionsgeprüft.

Zwei ausschließlich im Speicher entfernte Guards werden erkannt: Hashkontrolle
auch außerhalb der sichtbaren Seite (eine Assertion) und Cursor-Requestbindung
(drei Assertions). Keine Testfehler aus falscher Exception-Identität und keine
Änderung der Produktionsbytes. Die volle reguläre Suite bleibt grün.

Die frühere Routing-Fixture erwartet nun den vollständigen Worker-Abruf und
weiterhin höchstens zehn sichtbare Einträge in der Defaultseite. Elf gültige
Treffer sind mit P2 ein legitimer mehrseitiger Fall, kein zu verwerfender Workerfehler.
Das ist die explizite Vertragserweiterung aus dem freigegebenen Plan.

Unabhängiger Source-/Testreview: keine offenen P1/P2.

## Nativer Nachweis

Der Vorabvertrag wurde in `1900b68`, die Implementierung in `e51a7df` fixiert.
Der erste synthetische Fixture-Aufbau stoppte vor dem Worker: Windows hatte LF
beim Schreiben in CRLF umgewandelt, womit das kanonische Frontmatter ungültig war.
Seit `f23484e` schreibt der Treiber ausdrücklich LF. Produktionsguards und
Abnahmekriterien wurden dafür nicht verändert.

Der [feste Prüflauf](run_rule_routing_p2_native.py) installiert nichts:

```powershell
.validation/runtime/venv/Scripts/python.exe Evals/Onboarding/run_rule_routing_p2_native.py --run
```

Die [maschinenlesbare Evidence](Rule-Routing-P2.json) enthält den nativen Bericht,
Code-/Case-/Protokoll-/Rohbericht-Hashes, kompakte Regressionsergebnisse und die
kontrollierten Guard-Gegenproben. Die ausgeführten Checkoutbytes sind an die
jeweiligen Gitfassungen gebunden; abweichende CRLF/LF-Zeilenenden sind ausdrücklich
als äquivalent statt als bytegleich ausgewiesen. Katalogseiten speichern IDs und
Digests ihrer vollständig geprüften Descriptor-Payloads statt erneut alle Quellen
zu duplizieren.

| Kriterium | Tatsächliches Ergebnis |
| --- | --- |
| `contract-pagination` | 14 echte QMD-Treffer über vier Seiten, jede Quelle genau einmal, globale Score-/Pfadordnung; tatsächlich eine Score-Gleichstandsgruppe |
| `contract-stale` | Quellenedit ergibt stale; nach Rebuild ist der alte Cursor invalid-cursor; jeweils null Worker-Aufrufe |
| `contract-descriptors` | 155 kanonische Beschreibungen über sieben Seiten; Node-, QMD- und Ready-Index-Aufrufe durch verbotene Stubs gesperrt, null Aufrufe |
| Descriptions und Metadaten | unabhängig gegen YAML-Inventar und Originaldateien geprüft, Quellenhashes stimmen |
| Originaldateien | alle vor/nach dem Lauf geprüften Rohbytes unverändert |
| P1-Regression mit unverändertem Quellenpaket und Oracle | weiterhin 15/16 Suchfälle bestanden, keine Regression |

Die drei technischen P2-Vertragsfälle bestehen. Die fünf P3-Fälle bleiben **NOT
RUN**. Sie werden nicht mit Retrievalwerten zu einer allgemeinen Qualitätsquote
vermischt. Der P1-Retrievalstatus bleibt **PARTIAL**: `Akzeptanzkriterien beobachtbar`
findet weiterhin `acceptance-criteria-design` nicht. Der Skill ist in der
vollständigen Descriptor-Ausgabe erreichbar; das ist keine Verbesserung dieses
Suchfalls und keine bereits ausgeführte fachliche Prüfung.

Natürliche Agentenauswahl und semantischer Recall bleiben **NOT RUN / UNVERIFIED**.
Keine Maturity- oder allgemeine Recall-Hochstufung.
