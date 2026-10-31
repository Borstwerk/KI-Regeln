# Separater Vergleich nach Reparatur der Fixture

Vorabvertrag vom 31.10.2026, Basis `6284bda` (Merge PR #118). Methoden:
`agent-eval`, `context-audit`, `verification-loop`; separater Same-Model-Review,
keine unabhängige Zertifizierung.

## Fester Umfang vor Modellstart

Genau zwei neue frische Codex-CLI-Sessions über das bestehende ChatGPT-Abo:
**free**, dann **guided**. Je ein Versuch, höchstens 240 Sekunden, kein Resume,
Nachprompten oder Best-of. Keine direkten Modell-APIs oder Installationen.
Neue Ausgabe `.validation/routing-repaired-comparison-20261031`; alte P4-/P5-
Antworten und der fehlgeschlagene erste Vergleich bleiben unverändert erhalten.

Beide Bedingungen verwenden unverändert die P4-Entwicklungsaufgabe und ihr Oracle:
Arbeitsplan für einen CSV-Import, zwei Agenten mit getrenntem Dateibesitz, konkrete
Grenztests, Kontext-/Nachladeplan, unabhängiger Codecheck und ehrlicher Status.
Erwartete Jobs: `task-graph`, `delegation-contract`, `context-engineering`,
`test-design`, `code-review`, geeignete Implementierung und `verification-loop`.
TDD oder begründete Alternative nach Prüfung seiner Workflow-Core-Description;
die späteren Phasen dürfen geplant sein und gelten nicht als ausgeführt.

Aufgabenwortlaut, Guided-Zusatz, Modell `gpt-6.1-sol` mit `high`, Schema, Rechte und
Budget bleiben gegenüber dem ersten Paar gleich. Der Zusatz nennt nur die
Suchmethode, keine Queries oder erwarteten Skill-IDs. Free darf ebenfalls suchen;
Guided ist angeleitete Nutzung und kein natürlicher Discovery-Nachweis.

Der Produktsnapshot wird vom gemergten Fixstand bezogen. Die 578 exportierten
Produktdateien müssen mit dem vorherigen Snapshot bytegleich sein. Evaluations-
artefakte, Tests, alte Antworten und Umsetzungsplan fehlen im Modellarbeitsraum.
Kein Claim technisch vollständiger Dateisystem- oder Oracleabschottung.

## Technische Admission und Ablauf

Die reparierte Vorbereitung bleibt unverändert: Bytecode-Schalter in Native-Env
und Tool-Shellpolicy; explizites Profil `:workspace`; Sandboxbau und getrennte
Canaryquery vor jedem Modellstart. Beide Vorbauten müssen identische Metadaten
einschließlich Fingerprint besitzen. Quellenhashes und Gitstatus müssen vor und
nach jeder Session sauber sein. Keine Cachebereinigung zum Bestehen des Gates.

Portable/native Guards und Strukturchecks vor dem Paar abschließen. Während beider
Modellsessions startet der Integrator keine anderen Tests, nativen Treiber oder
Review-Agenten. Nur kurze Statuslesungen/Updates; Detailauswertung erst danach.
Nach dem Paar folgen getrennt Evidence-Checks und Same-Model-Review.

Bei Admission-, Quota-, Auth-, Transport- oder Laufzeitfehler: BLOCKED beziehungsweise
FAIL mit Ursache, keine weiteren Ersatzversuche. Ohne zwei auswertbare Antworten
und bestandene technische Gates kein qualifizierter Aufwandsvergleich.

## Bewertung vorab fixiert

Produkt, Routingprozess und technische Gates getrennt beurteilen. Pflicht-Reads,
Workflowkern, Original-Descriptions und späte Overlays anhand tatsächlicher
Tooloutputs prüfen. Alle erforderlichen Jobs und Dateigrenzen müssen erhalten
bleiben. Bloßes Nennen eines Skills oder ein Selbstbericht genügt nicht.

Erfassen: Laufzeit, Toolkommandos, ausdrücklich als UTF-8 gelesene und gezählte
Tooloutputs, gemeldete Input-/Cached-Input-/Outputtokens, verwendete Owner und
Such-/Hinweis-/Relations-/Pagingpfade. Unbenutzte optionale Funktionen bleiben NOT
RUN. Mechanische Checks plus qualitative Prüfung durch Integrator und separaten
Review-Agenten; kein zusätzlicher Judge-CLI-Lauf und keine menschliche Blindabnahme.

Nur bei vergleichbarem fachlichem Outcome und sauberen technischen Gates werden
die beobachteten Aufwandswerte nebeneinandergestellt. Usage summiert mehrere
Modellschritte, keine einmalige Kontextgröße; keine Zeichen→Token- oder Preisformel.
Feste Reihenfolge, Provider-Caches, unkontrollierte externe Rechnerlast und
Stochastik begrenzen ein einzelnes Paar weiterhin. Kein kausaler oder allgemeiner
Spar-Lift und keine universelle Routingpromotion daraus ableiten.

## Abschlussgrenze

Die bisherigen 24 Fälle/Oracles und der bekannte Retrieval-FAIL bleiben erhalten.
Kein neuer Plattformbau, kein Pflicht-Suchgate, keine Skill-/Maturityänderung.
Dieses Paar anschließend abschließen; die Akzeptanzkriterien-Suchlücke wäre ein
separater Bug-Slice. Vor Veröffentlichung Hash-/Redaktionsprüfung und Full Harness.

Status vor Ausführung: **NOT RUN**.

## Ergebnis des fixierten Laufs

Ausgeführt am 31.10.2026 mit Controller-/Vertragsstand `380c4ed`, Produktsnapshot
`6284bda`. [Öffentliche Evidence](Rule-Routing-Repaired-Comparison.json) bindet
Protokoll, CLI-Version, Code, Quellinventar und Rohantworten über Hashes. Der oben
stehende Vorabvertrag ist in `380c4ed` unverändert archiviert; dieser Ergebnisanhang
entstand erst danach. Keine zusätzlichen Modellversuche.

**Technik: PASS.** Beide frischen Antworten mit Exitcode 0; der strikte Batch endet
ebenfalls mit 0. Alle 578 Quellen je Fixture sind unverändert, beide Gitstatus leer.
Sandboxvorbauten und getrennte Canaryproben sind untereinander identisch. Sämtliche
sechs tatsächlichen BM25-Antworten sind `ready`, keine Cache-Reparatur erforderlich.
Die erste Alltagsquery liefert keine Treffer; die anschließende Query `task graph`
liefert Kandidaten. Ein leerer Treffer ersetzt keine fachliche Prüfung.

**Produkt und Routing: PASS im festen Planungsfall.** Beide Pläne decken die fünf
festen Ownerjobs, TDD und geplante Verifikation ab; sie trennen Dateibesitz, konkrete
Grenztests, initialen Kontext, Nachladen und einen Codecheck durch den anderen
Agenten. Beide lesen Master-Router, Katalog, Workflowindex, Feature-Workflow und
Original-Descriptions tatsächlich. Späte Overlay-Descriptions und Registry sind
in den Tooloutputs vorhanden. Implementierung, Tests und Codecheck sind in beiden
Antworten ausdrücklich nur geplant. Die Bewertung bezieht sich auf diesen einen
bekannten Auftrag, nicht auf generelle Skill-Auswahlqualität.

Free verwendet ausschließlich direkte Dateien. Guided liefert sechs Suchantworten
(eine leer), 52 zurückgegebene Hinweisinstanzen und einen expliziten Relationsabruf
mit fünf Kanten. Alle 57 Kanteninstanzen stimmen mit den kanonischen Quellen
überein. Paging und Descriptorlisting als Agentenpfade bleiben **NOT RUN**.
Die mechanischen Evidence-Checks erkennen entferntes Master-Router-Output und
entfernte erfolgreiche Suche in kontrollierten Kopien der tatsächlichen Traces.
Diese Kontrollen sind kein automatischer semantischer Judge.

| Beobachtung | Free | Guided |
| --- | ---: | ---: |
| Sessionlaufzeit in Sekunden | 128,39 | 190,98 |
| Toolkommandos | 32 | 11 |
| Tooloutput in UTF-8-Bytes | 204.022 | 223.165 |
| Gemeldete Inputtokens, über Modellschritte summiert | 296.545 | 489.464 |
| Davon Cached-Inputtokens | 233.856 | 417.536 |
| Gemeldete Outputtokens | 3.517 | 5.018 |

Die Werte dürfen für dieses technisch saubere Paar nebeneinanderstehen. Guided
bündelt mehrere Reads und Queries in einzelne Kommandos; die kleinere Kommandomenge
belegt daher keine Aufwandsersparnis. In diesem Paar sind Laufzeit, Outputbytes und
Inputtokens sogar höher. Input-Usage ist keine einmalige Kontextgröße; feste
Reihenfolge, Provider-Caches, Stochastik und externe Rechnerlast verhindern eine
kausale oder verallgemeinerbare Effizienzaussage. Integratortests, native Treiber und
Review-Agenten liefen während beider Sessions nicht.

Vor dem Paar: portable Tests **16 Tests, OK mit einem Skip** des separat ausgeführten nativen
Opt-in-Tests; nativer Fixturetest **1 OK**, modellfrei; Full Harness **PASS** mit
bestehenden Near-Miss-Warnungen. Qualitative Prüfung durch Integrator und separaten
Same-Model-Review sowie mechanische Evidence-Prüfung; keine unabhängige
Zertifizierung und keine menschliche Blindabnahme.

**Entscheidung:** Suche bleibt optional. Angeführte Nutzung von Suche und Relations
ist beobachtet; ein allgemeiner Effizienzgewinn bleibt **UNVERIFIED**. Keine
Routing-/Maturitypromotion, keine Änderung an Skills, Suchlogik oder den 24 alten
Fällen. Der historische P5-Status bleibt PARTIAL; der bekannte Retrieval-FAIL wird
in einem getrennten nächsten Slice bearbeitet. Dieser Vergleich ist abgeschlossen.
