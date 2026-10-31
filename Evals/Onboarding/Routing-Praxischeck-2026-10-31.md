# Routing-Praxischeck: Zusammenspiel und Aufwand

Stand: 31.10.2026, Produktrevision `03cdee52bdd38955e81b48d6f46f585db8e18c17`.
Explorativer Check, kein vorab eingefrorener Benchmark und kein Held-out-Eval.
Die nachfolgenden Queries wurden bei der Untersuchung gewählt; ihre Resultate
belegen weder vollständigen Recall noch eine automatische Skillauswahl.

## Bereits vorhandene Evidence

- [P4](Rule-Routing-P4.md): ein Planungsfall, ein Mehrjob-Fallback ohne QMD und
  ein trivialer Direktpfad bestanden im jeweiligen Fallumfang. Je ein Versuch;
  keine allgemeine Zuverlässigkeits- oder Effizienzaussage.
- [Repaired Comparison](Rule-Routing-Repaired-Comparison.md): zwei technisch
  saubere Sessions für denselben Planungsfall. Beide erfüllten das fallbezogene
  Oracle; angeleitete Suche benötigte in diesem Paar mehr Zeit und Inputtokens.
  Feste Reihenfolge, Caches und Stochastik verhindern einen allgemeinen Vergleich.
- [Acceptance Fix](Rule-Routing-Acceptance-Fix.md): der zuvor fehlende Treffer
  wurde durch eine präzise Katalogkorrektur gefunden; 16/16 bestehende
  Entwicklungs-/Regressionsfälle im dokumentierten Kandidatenlauf. Keine
  unabhängige Bestätigung allgemeiner Recallqualität.
- Frischer modellfreier P1-Kandidatenlauf mit demselben festgelegten
  Katalog-Overlay `faa53e3`: **16 PASS, 0 FAIL, 8 NOT RUN**, Exit 0;
  Rohbericht `.validation/rule-routing-candidate-rdzg4jfm`. Das ist eine
  Wiederholung auf dem historischen Quellenpaket mit diesem Overlay, kein Test
  des gesamten aktuellen Repository-Snapshots und kein neuer Agentenlauf.

## Explorative Suchproben auf dem aktuellen Index

Ausführung mit `Search-KI-Regeln.ps1 -Routing -Query`, Standardlimit, Indexstatus
jeweils `ready`, Fingerprint
`c359dc0c490140c876d0eb118451607fc2a47d728fbbf93167465f2ffb4a0c30`.
Die Tabelle zeigt Skill-IDs; bei der Grenztestfrage gab es zusätzlich einen
Treffer, der kein Skill war. Alle Abfragen meldeten `has_more: false`.

| Suchtext | Skill-Treffer | Einordnung |
| --- | --- | --- |
| `Datenbank Tabelle dokumentieren` | `database-design` | Referenzdokumentation fehlt. Der Treffer beschreibt Datenmodellentwurf/-review, nicht reine Dokumentation. |
| `Schema Referenzdokumentation` | keine | Kein passender Kandidat trotz naheliegender Umschreibung. |
| `Schema dokumentieren` | `database-design`, `reference-docs`, `data-contract-design`, `integration-testing`, `data-ingestion-design`, `agent-eval` | Der passende Kandidat ist auffindbar, aber muss fachlich ausgewählt werden. |
| `reference docs schema` | `reference-docs` | Englische Formulierung findet den Kandidaten. |
| `Tabelle dokumentieren` | `database-design`, `data-contract-design`, `data-transformation-design` | Zusätzlich Treffer `CONTRIBUTING.md`; `reference-docs` fehlt. |
| `Akzeptanzkriterien beobachtbar` | `acceptance-criteria-design`, `delegation-contract` | Bekanntes Reparaturziel gefunden; Delegation folgt nicht allein aus dem Treffer. |
| `Grenzwerte Testfälle` | `test-design` | Passender Kandidat für den getrennten Testfall-Job gefunden. |
| `Rechtschreibung Zeichensetzung` | `korrekturlektorat` | Passender enger Kandidat gefunden. |
| `zzroutingabsentf72ea4bd` | keine | Künstliche Negativkontrolle für Leertreffer. |

Die Source-of-Truth-Abgrenzung ist in den kanonischen Descriptions nachlesbar:
`reference-docs` deckt Nachschlageinformationen zu Schemas ab;
`database-design` betrifft Modellentwurf und -review. Für reine Dokumentation
einer vorhandenen Tabelle begründet die erforderliche Schema-Expertise für sich
noch keinen Datenmodellierungsauftrag. Es handelt sich um eine beobachtete
Retrievallücke, nicht um einen nachgewiesenen Fehler der tatsächlichen
Agentenauswahl: Katalog, Workflow und alternative Suchbegriffe bleiben verfügbar.

Die ersten sechs Anfragen dauerten in dieser Umgebung jeweils ungefähr fünf
Sekunden inklusive Prozessstart. Gleichzeitig liefen ein nativer Regressionstreiber
und anfangs der Quick-Harness; diese Werte sind deshalb keine saubere
Geschwindigkeitsmessung und nicht mit direktem Routing vergleichbar.

## Kleine Folgeprüfung vor einer Suchänderung

Neue Fälle zuerst samt Quellstand, Aufgaben, Queries, Oracle und Grenzen festlegen;
dann alte und neue Bedingung auf identischer Runtime vergleichen. Die obigen
Formulierungen sind Entwicklungsmaterial, keine unabhängige Testmenge.

| Fall | Erwartete fachliche Jobs | Gegenprobe |
| --- | --- | --- |
| Bestehende Datenbanktabelle als Referenz dokumentieren; Schema und Migrationen liegen vor | Referenzdokumentation gegen tatsächliches Schema, passende Workflowphasen; Modellreview nur bei zusätzlichem Reviewauftrag | Ein Datenmodellentwurf darf nicht allein wegen des Wortes „Datenbank“ als Pflicht gelten. |
| Für bestehende Importanforderung Akzeptanzkriterien und danach Grenztests formulieren | `acceptance-criteria-design` und `test-design`, in dieser Reihenfolge | Nur Akzeptanzkriterien verlangt keine konkreten Tests; nur Tests verlangt keine Neuerfindung der Kriterien. |
| Fertigen Text ausschließlich auf Schreibfehler prüfen | `korrekturlektorat` | Stilrewrite und Research sind keine geforderten Jobs. |
| Ein Komma in einem kurzen Text mechanisch ergänzen | Direktpfad, kein Skill nötig | Kein nichttrivialer Bootstrap erzwingen. |

Für einen echten Agentenlauf die Aufgaben ohne erwartete IDs oder Queries in
isolierte Sessions geben. Ergebnisqualität, tatsächliche Router-/Description-Reads,
Jobs und ihre Reihenfolge sowie unnötige Aktivierungen getrennt prüfen. Erst bei
gleichwertigem Ergebnis und sauberen Bedingungen Zeit, Tooloutput und Tokenusage
vergleichen. Ein Lauf je Bedingung liefert nur Einzelbeobachtungen. Triviale Fälle
dürfen bewusst keine Router-Reads benötigen. Suchtreffer sind Kandidaten, nicht
automatische Aktivierungen; fachliche Bewertung verlangt Review der Antwort und
der tatsächlich gelesenen Quellen. Kein neues generelles Routing-Gate ableiten.

**Status:** neue Agentenfälle und unabhängige Effizienzmessung `NOT RUN`;
allgemeiner Recall und Agentenqualität `UNVERIFIED`. Die konkrete Suchlücke ist
ein Entwicklungshinweis. Kein Skill-, Suchlogik- oder Maturity-Edit aus dieser
explorativen Probe abgeleitet. Der folgende separate Reparaturversuch ändert
allerdings den Katalogzweck.

## Nachtrag: begrenzter Katalogkandidat

Auf ausdrücklichen Folgeauftrag wurde der `purpose` von `reference-docs` um
fachlich passende Begriffe für Datenbanken, Tabellen und Schemas ergänzt. Die
kanonische Skill-Description deckt Schemas bereits ab. Die Suchableitung übernimmt
den Katalogzweck in das indizierte Suchdokument. Die vorherigen Fehlertreffer und
das Auffinden mit `Schema dokumentieren` sprechen für eine lexikalische Lücke;
sie beweisen keine allgemeine Ursache für alle möglichen Umschreibungen.

Vor Ausführung war der Vergleichsvertrag in
[`run_reference_docs_routing.py`](run_reference_docs_routing.py) festgelegt:
identisches Git-Quellenpaket, genau ein zugelassener Katalogzweck-Edit, fünf
gezielte Queries, eine Leertrefferkontrolle und die 16 vorhandenen P1-Fälle.
Die neue Auswahl ist Entwicklungs-Evidence, kein Held-out-Satz. Der Treiber
erstellt zwei getrennte lokale Git-Fixtures und verwendet vorhandenes QMD;
er installiert nichts und ruft kein Modell auf. Die Kandidatenbytes werden mit
dem Git-normalisierten Arbeitsverzeichnis abgeglichen. Zwei Vorstarts scheiterten
vor dem Indexaufbau an fehlendem Manifest beziehungsweise CRLF-Normalisierung;
beide wurden im Treiber korrigiert und sind keine Suchergebnisse.

Der native Vergleich liegt unter `.validation/reference-docs-routing-81f7if9c`:

| Query | Baseline: Rang | Kandidat: Rang |
| --- | ---: | ---: |
| `Datenbank Tabelle dokumentieren` | nicht gefunden | 2 |
| `Schema Referenzdokumentation` | nicht gefunden | 1 |
| `Tabelle dokumentieren` | nicht gefunden | 2 |
| `Schema dokumentieren` | 2 | 2 |
| `reference docs schema` | 1 | 1 |

Die Leertrefferkontrolle blieb leer. Die 16 vorhandenen P1-Fälle bestanden sowohl
in der Baseline als auch im Kandidaten, nach demselben Suchtreffer-Oracle. Das ist
kein Urteil über ungeeignete Kandidaten, spätere Skillaktivierung oder Verhalten
eines Agenten. Die 17 gezielten Routing-/Katalog-Unittests bestanden ebenfalls.
Allgemeiner Recall, natürliche Agentenauswahl und Effizienz bleiben `UNVERIFIED`.

Der reguläre Suchindex verwendet festgeschriebene Git-Snapshots; zum Zeitpunkt
dieses ersten Laufs war der Arbeitsverzeichnis-Kandidat dort nicht automatisch aktiv. Nach
Übernahme muss der Index gemäß bestehender Dokumentation neu gebaut werden.
Skillvertrag, Suchalgorithmus, Reife und bestehende Oracles wurden nicht geändert.

## PR-Review: reproduzierbarer Folgelauf

Der Folgeauftrag übernimmt den Beitrag `81493b7` auf den aktuellen Main-Stand
`4939eef`; dessen unveränderter Produktdiff liegt hier in `d07334e`.
Reviewmethoden: `code-review`, `agent-eval` und `verification-loop`. Die fachliche
Katalogerweiterung passt zur kanonischen Description von `reference-docs`.
`database-design` bleibt ein anderer Job, ohne automatische Pflichtaktivierung.

Ein Repro des ursprünglichen Treibers auf seinem committed Stand `81493b7`
bricht vor dem Indexaufbau ab: `HEAD` enthält bereits den neuen Katalogzweck,
während die Admission dort noch den alten Text erwartet. Der damalige Lauf aus
einem veränderten Arbeitsverzeichnis war damit nach dem Commit nicht direkt
wiederholbar. Der frühere Bericht bleibt als explorative Development-Evidence
erhalten; seine fehlenden Code-/Versionsbindungen werden nicht rückwirkend
als nachgewiesen ausgegeben.

**Vorabvertrag für den frischen Lauf:**

- Basisquellen fest aus `03cdee5`, Kandidatenkatalog fest aus `d07334e` lesen,
  statt `HEAD` und uncommittete Checkoutbytes zu mischen. Weitere Quellen des
  Kandidatencommits werden nicht übernommen. Der exakte Byteguard erlaubt nur
  die oben beschriebene Ersetzung des einen Katalogzwecks.
- Dieselben fünf Zielqueries, dieselbe Leertrefferkontrolle und dieselben 16
  P1-Fälle mit unverändertem Zehnerbudget prüfen. Falldatei aus der gepinnten
  Basis lesen und deren P1-Evidence gegen die Originalquellen prüfen. Den bereits
  vorhandenen P1-Grader wiederverwenden; keine neuen Fall-Erwartungen festlegen.
- Beide Bedingungen in getrennten Fixtures ausführen; alle Quellen während
  jedes Laufs unverändert halten. Die Leertrefferkontrolle muss beidseitig leer
  bleiben. Keine Regression eines bisher erfolgreichen P1-Falls.
- Ausführungscommit, Code-/Vertragshashes, vollständiges Basis-Quellinventar,
  effektive Paketdigests, Kataloghashes, Casehash, Node-/QMD-Version und Budget
  protokollieren. Rohberichte zusätzlich als öffentliche JSON-Evidence liefern.
- Die Admissiontests müssen den zulässigen Edit akzeptieren und zusätzliche,
  fehlende oder mehrdeutige Änderungen zurückweisen. Vorhandene Suchtests und
  Full Harness verwenden. Keine Installationen und keine Agenten-CLI-Modellläufe.

Die Korrektur betrifft den Eval-Treiber und seine Nachweise. Der Produktdiff des
zweiten Agenten bleibt unverändert: ein `purpose`-Feld, keine Skill-Description,
Suchlogik, Routingregel oder Maturityänderung. Bekannte Entwicklungsfälle sind
keine unabhängige Bestätigung allgemeiner Auswahlqualität. Neuer Lauf: **NOT RUN**.
