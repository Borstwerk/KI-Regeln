# Begrenzter Auth-Messplan

Stand: 15.10.2026. Basis: `a31b8a939b5de3f582cb11ca336f1421d24b6b14`, einschließlich
des gemergten Transport-Schritts aus PR #83 und der Onboarding-Änderungen aus PR #84.
Status: **PLAN_ONLY; echte Credentials, Service-Authentifizierung und Modellaufrufe NOT RUN.**

Zielgruppe sind Maintainer und der spätere berechtigte Operator. Der Plan legt eine
kleine Auth-Connectivity-Messung fest; er implementiert oder autorisiert sie nicht.
Die Parameter und die nicht ausführbare Argv-Vorlage stehen in
[auth-measurement-plan.json](auth-measurement-plan.json). Das JSON ist ein Reviewartefakt,
keine Runtime-Konfiguration, kein Freigabetoken und keine Admission-Evidence. Es gibt
keinen produktiven Reader dafür. Änderungen seiner Felder können keine Gates öffnen.

## Zweck und Abgrenzung

Zu klären ist, ob genau der vorgesehene Subscription-OAuth-Pfad in einer frisch gebundenen
CLI-Umgebung tatsächlich am Dienst authentifiziert. Eine synthetische Invalid-Kontrolle
muss eine dem Dienst zurechenbare Auth-Ablehnung liefern; erst danach kommt eine kleine
Positivprobe infrage. Ein lokales `loggedIn`, ein erfolgreicher Exit von `auth status`
oder eine Modellbehauptung reichen nicht.

Beide späteren Sitzungen verwenden denselben kontrollierten Kontext und dieselbe feste,
öffentliche Prompt-Vorlage. Nur das Credential unterscheidet sich. Ein privater, leerer
Workspace ersetzt Produktfixtures; Repository-Inhalte, Nutzerdateien und Chatverlauf
gehören nicht in den Request. Built-in-Tools sind leer, MCP ist zusätzlich gesperrt.
Eine Erfolgsprobe würde nur diesen Auth-only-Kontext belegen. Sobald Toolrechte, Policy,
Binary, Transport oder View geändert werden, ist die relevante Evidence zu erneuern.
Für den B2-Pilot bleiben reale Bash-/Read-Probes und die vollständige Admission nötig.

## Quellenlage und aktueller Runtime-Stand

Die [offizielle CLI-Referenz](https://code.claude.com/docs/en/cli-reference) beschreibt
Print-Modus, Modellwahl, Turn-Limit, Toolauswahl und den geschätzten Dollar-Cap. Sie weist
ausdrücklich darauf hin, dass nicht alle Flags in `--help` erscheinen. Die lokale
credentialfreie Non-Root-Probe hat Version **2.1.292** und die Hilfe gelesen: Die übrigen
in der Vorlage verwendeten Flags waren sichtbar, `--max-turns` nicht. Das ist weder ein
Beleg fehlender Unterstützung noch ein Parsing-/Durchsetzungsnachweis. Die vollständige
Optionskombination und ihre Wirkung bleiben **UNVERIFIED**; kein Print-Aufruf wurde ausgeführt.

Die [Authentifizierungsdokumentation](https://code.claude.com/docs/en/authentication)
beschreibt `CLAUDE_CODE_OAUTH_TOKEN` für Subscription-Modellrequests und schließt diesen
Pfad im Bare-Modus aus. Daher enthält die Vorlage **kein `--bare`**. `--safe-mode` lässt
Managed Policy einschließlich bestimmter Hooks und Commands weiter gelten; es ersetzt
deren Prüfung nicht. Auch leere Tool-/MCP-Listen verhindern keine Policy-Commands vor
dem Modellstart. Hook-, Statusline-, File-Suggestion- und Credential-Provider-Ausführung
muss deshalb vor Secret-Intake im tatsächlichen CLI-View geklärt oder verweigert sein.

Der Modellkandidat `claude-haiku-5-5` ist in der
[Herstellerübersicht](https://platform.claude.com/docs/en/models/overview) dokumentiert.
Verfügbarkeit für das konkrete Konto ist **UNVERIFIED**. Kein Alias, Ersatzmodell oder
Fallback ist freigegeben. Das Auftauchen in Dokumentation oder Hilfe beweist keine
erfolgreiche Ausführung mit unserem Konto.

## Vorgeschlagene Grenzen – noch nicht genehmigt

| Größe | Vorschlag und Bedeutung |
| --- | --- |
| Umfang | Höchstens zwei neue CLI-Sitzungen: Invalid-Kontrolle, danach bedingte Positivprobe |
| Agentische Turns | Höchstens ein Turn pro Sitzung; Parsing und reale Durchsetzung vor Live-Freigabe prüfen |
| Zeit | Je 60 Sekunden plus höchstens 5 Sekunden Cleanup; gesamte Live-Stufe höchstens 150 Sekunden ab erstem CLI-Start |
| Orchestrierung | Keine Wiederholung, kein Resume/Continue, kein Modell-/Provider-Fallback |
| CLI-Kostenschätzung | Vorgeschlagener `--max-budget-usd` von 0,05 USD je Sitzung, 0,10 USD als Gesamt-Schätzrahmen |
| Geld / Kontingent | Kein nachgewiesener harter Rechnungs-Cap; Subscription-Quota-Effekt und tatsächliche Kostenzurechnung UNVERIFIED |
| Netzwerkrequests | Physische HTTP-Anzahl und CLI-interne Retries UNVERIFIED; zwei CLI-Starts bedeuten nicht zwei HTTP-Requests |

Der CLI-Cap basiert auf einer Schätzung und kann überschritten werden. Er ist weder
ein harter Rechnungsdeckel noch eine Zusage über Subscription-Verbrauch. Vor Live-Start
muss entweder eine geeignete Anbietergrenze nachgewiesen oder die verbleibende Kosten-/
Quota-Unsicherheit ausdrücklich vom Operator akzeptiert werden. Bisher ist keine dieser
Freigaben erteilt. Falls ein harter Gesamtbetrag verlangt wird, bleibt die Stufe ohne
nachgewiesene harte Grenze **BLOCKED**. Dies folgt aus den
[dokumentierten Budgetgrenzen](https://code.claude.com/docs/en/cli-reference).

Jeder erneute Versuch benötigt einen neuen Review-/Freigabevorgang. Eine zuvor unklare
Abrechnung oder ein Timeout wird nicht durch weitere Requests diagnostiziert. Auch
Client-Abbruch garantiert keine Rücknahme bereits beim Dienst laufender Arbeit.

## Eintrittsgates vor dem ersten Credential

Alle folgenden Punkte müssen für einen späteren ausführbaren Operator-Befehl erfüllt sein:

1. **Intake implementiert und reviewt:** private, begrenzte Eingabe ohne Shellargument,
   History, persistente Datei oder Credential-Hash; Transport nur im vorgesehenen View.
   Die aktuelle Credential-Verweigerung bleibt bis dahin bestehen.
2. **Effektive Policy bekannt:** tatsächliche lokale/Remote-Managed-Quellen, Hooks,
   Commands, Profile und Credential-Provider im CLI-Kontext geprüft. Keine implizite
   Auswahl aus API-Key, anderem Token, Profil oder Gateway; Mehrdeutigkeit blockiert.
3. **Live-Lifecycle nachgewiesen:** Cancellation auch bei Session-Detach und sonstigen
   Start-/Exitfehlern geprüft; die bisherigen festen Python-Kontrollen reichen dafür nicht.
4. **Collector implementiert:** begrenzte Bytes/Events, Fristen und reine In-Memory-
   Auswertung, keine ungefilterten stdout/stderr-/Debug-Dateien. Ein Überlauf bricht ab.
5. **Limits und Provenienz überprüfbar:** Pflichtflags und Kosten-/Zeitüberwachung wirken;
   Service-Auth-Fehler lassen sich von lokalen Parser-/Netzwerkfehlern unterscheiden.
6. **Operator-Freigabe konkret:** Binary-/Codezustand, Modell, Konto-/Abrechnungskontext,
   beide Sitzungen, Quota-/Kostenrahmen und Restunsicherheit ausdrücklich freigegeben.

Ein Genehmigungsfeld, ein gespeicherter Plan oder ein früherer Vorbereitungserfolg
ersetzen diese Beobachtungen nicht. Gegenwärtig sind die Gates **offen**. Es existiert
noch kein freigegebener Live-Auth-Controller oder Live-Operator-Befehl.

## Ablauf und Auswertung der späteren Live-Stufe

| Schritt | Akzeptanz | Stop / offener Status |
| --- | --- | --- |
| Kontext neu binden | Binary und relevante Code-/Konfigurationsbytes, gefilterte Umgebung, Endpoint/Provider, effektive Policy, View, Identitätsfloor und Sessiongrenzen frisch erfasst | Änderung oder Mehrdeutigkeit: BLOCKED, kein Secret-Intake |
| Invalid-Kontrolle | Vertrauenswürdiger Collector ordnet eine echte Auth-Ablehnung dem vorgesehenen Dienst und dem isolierten synthetischen Credential zu | Parserablehnung, bloßer Text `401`, Netz-/TLS-Fehler, Budgetlimit oder Timeout: UNVERIFIED; keine Positivprobe |
| Positivprobe | Nur nach erfolgreicher Negativkontrolle: authentifizierte frische Modellantwort über den einzigen zugelassenen Kanal; erwarteter öffentlicher Marker und strukturierte Ergebnis-/Usage-Daten passen | Abweichender Provider/Modell, Tool-/Hookaktion, unklare Credential-Auswahl oder Fehler: FAIL/UNVERIFIED, kein Retry |
| Abschluss | Geheimnisfreie Allowlist-Evidence außerhalb von Modellbehauptungen; vollständiger Context-Bind und expliziter Status je Beobachtung | Fehlende Aktion/Beobachtung bleibt NOT RUN/UNVERIFIED; keine Hochrechnung auf B2-Read-/Bash-Schutz |

Die beiden Varianten verwenden identische Binary, Args, Config, Policy und den gleichen
aufgelösten Endpoint. Ein nachweisbarer Wechsel invalidiert den Vergleich. Der Collector
darf Service-Origin nicht aus einer beliebigen Fehlerzeichenkette oder caller-supplied
Boolean ableiten. Bietet der CLI-Pfad keine hinreichende Beobachtung, bleibt das Ergebnis
offen; kein undokumentierter direkter HTTP-Aufruf mit Subscription-Credentials als Ersatz.

Persistierbar sind ausschließlich ein eigener Run-Identifier, Code-/Binary-Digests und
Digests einer ausdrücklich geheimnisfreien Allowlist-Projektion der Konfiguration,
zugelassene Modell-/Kontrollnamen, Credential-Kanal und Vorhandensein,
Status, gemessene Fristen und sanitierte Mengen/Kosten mit klarer Schätzkennzeichnung.
Keine Tokenwerte/-hashes, Konto-/Organisationstitel, Rohantworten, Systemprompts oder
beliebigen Fehlertexte. Ist sichere Redaktion nicht gewährleistet, wird nichts davon
geschrieben und der Versuch blockiert. Secret-Lebensdauer im Speicher bleibt begrenzt;
Root-, Host-, Swap- und Core-Dump-Grenzen aus dem Transportvertrag gelten weiter.

Vollständige Config-/Environment-Bytes dürfen nicht pauschal gehasht werden: Sie könnten
Credentials enthalten und damit indirekte Credential-Hashes erzeugen. Sensitiver Zustand
ist nur innerhalb der einmaligen Live-Transaktion im Speicher zu halten und auf Änderungen
zu prüfen. Eine persistierte Allowlist-Projektion beweist keine Identität sämtlicher
geheimnishaltiger Einstellungen und darf nicht als wiederverwendbare Admission dienen.

## Jetzt ausführbarer Operator-Schritt

Ohne echte Credentials, in der bestehenden dedizierten Ubuntu-Testkopie. Für den zweiten
Befehl ist der bereits verwendete Evaluator-Kontext mit Mountrechten nötig (in unserer
Testdistro `root`); der feste Payload wird innerhalb des Views auf UID/GID 1000 abgesenkt.
Als normaler Evaluator-Benutzer darf die fehlende Fähigkeit zu `BLOCKED` führen:

```bash
.validation/linux-venv/bin/python -m json.tool Evals/Verification-Surface/behavioral/auth-measurement-plan.json
.validation/linux-venv/bin/python tools/b2_auth_bootstrap.py --prepare-only --separated-runtime --report .validation/b2-auth-plan-preparation.json
```

Der erste Befehl prüft nur JSON-Syntax und zeigt die Reviewvorlage. Der zweite führt die
bestehende feste Python-Identitätsprobe aus. Erwartet: `PREPARED_ONLY` und beide
`may_start_*`-Felder `false`; unter fehlenden Rechten oder vorhandenen bekannten
Credential-Kanälen: `BLOCKED`. Kein Login, `setup-token`, `auth status` oder `claude -p`.

Die Argv-Liste im JSON ist **nur eine nicht ausgeführte Reviewvorlage** für einen späteren
Controller. Sie darf nicht direkt über eine Host-Shell gestartet werden: Das würde
Intake-, Lifecycle-, Collector-, Policy- und Freigabegates umgehen. Sie behauptet weder
aktuelle Ausführbarkeit noch einen vorhandenen Wrapper.

## Verifikation, Pflege und Rollback

Aktuell nachweisbar: JSON-Syntax/Konsistenz, Quellen-/Codeabgleich, credentialfreie
Version/Hilfe und die vorhandene Vorbereitung. **Nicht ausgeführt:** Optionskombination
im Print-Modus, echte Kosten-/HTTP-Messung, Auth, Invalid-Service-Control, Bash-/Read-
Enforcement, B2-Pilot oder Skill-Wirksamkeit. Bestehende historische Ergebnisse bleiben
an ihre ursprünglichen Quellstände gebunden.

Maintainer prüfen den Plan erneut bei Änderungen an CLI/Binary, Auth-Prioritäten,
Managed Policy, Modellverfügbarkeit, Budgetsemantik, Transport oder Operatorrechten.
Rollback entfernt Plan und Querverweise; Runtime, bisherige Tests, Trust-Pins und
Admission bleiben unverändert.
