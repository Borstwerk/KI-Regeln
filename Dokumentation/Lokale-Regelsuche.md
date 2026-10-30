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
Nur die explizite Auswahl in [mara-project.json](../mara-project.json) wird gesucht.
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

`tests.test_rule_search` prüft den Controller mit echten temporären Git-Repos
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
