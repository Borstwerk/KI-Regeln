# Reparatur der lokalen Routing-Fixture

Basis: `69b97f4` (Merge P5 / PR #117). Scope: zwei technische Defekte der
Testvorbereitung; keine neue Modellmessung, Produkt-/Skilländerung oder Promotion.
P5 bleibt mit seinen ursprünglichen Gates und Antworten erhalten.

## Repro und Ursache vor dem Fix

Eine neue Fixture mit denselben 578 öffentlichen Quelldateien bestätigt ohne
Modellaufruf beide Symptome im nativen Codex-Profil `:workspace`:

- Hostbau meldet ready; Sandboxabfrage meldet missing und erzeugt zwei `.pyc`-Dateien.
- Dieselben Quelldateien bleiben bytegleich; Git meldet `?? tools/__pycache__/`.
- Der Host kann den vorgebauten Index weiterhin als ready lesen. Ein direkter
  Sandbox-OpenRead desselben Snapshots liefert `System.UnauthorizedAccessException`.
- Die temporäre Builddirectory besitzt geschützte Zugriffsregeln. Ein Cachebau
  innerhalb des Sandboxprofils und eine **getrennte** nachfolgende Sandboxabfrage
  liefern beide ready mit unverändertem Revision-/Fingerprintwert.

Damit ist der Host→Sandbox-Zugriffsübergang für den Cache reproduziert. Der Cache
ist für den Host vollständig; Daten-/Quellen-/Fingerprintfehler erklären diesen
Repro nicht. Der Fix soll den ausführenden Kontext angleichen, keine ACLs lockern.
Die `.pyc`-Artefakte entstehen beim Pythonimport der Fixture-Module; der Repro
verwendet die reale PowerShell-/Python-/QMD-Kette.

## Kleiner Reparaturplan

1. Im vorhandenen P4/P5-Treiber Bytecodeschreiben für Vorbereitung und spätere
   Agententools explizit abschalten (`PYTHONDONTWRITEBYTECODE=1`). Den Git-Guard
   unverändert lassen; keine zusätzlichen Ignore-Regeln für den Test einführen.
2. Den modellfreien Vorbau über `codex sandbox --permission-profile :workspace`
   ausführen. Den tatsächlichen Agentenlauf auf dasselbe explizite Profil binden;
   Read-only-Fälle bleiben read-only. Keine neuen Profile, globalen Einstellungen,
   Netzwerkrechte, Shared-Runtime-Writes oder manuellen ACL-Änderungen.
3. Vor einem Modellstart aus einem **separaten** Sandboxprozess eine feste leere
   Canaryquery ausführen. Ready, Revision/Fingerprint, Dokumentzahl und saubere
   Fixture prüfen. Fehlender/falscher Probe-Status blockiert vor Modellaufruf.
4. Portable Adapter-/Guardtests und einen explizit aktivierten nativen
   Windows-Regressionstest ergänzen. Native Prüfung modellfrei: unveränderter
   Hostbau als negative Kontrolle, Sandboxbau als positive Kontrolle, getrennte
   Folgeabfrage und strikter Git-/Quelldatei-Guard. Keine reparierten Cachewerte
   in alte P5-Tracefiles schreiben.

Akzeptanz: keine `.pyc`-Artefakte, sauberes Git, alle 578 Quellen bytegleich,
Sandbox-Query nach Sandbox-Vorbau ready und an denselben Snapshot gebunden.
Fehlerhafte/abweichende Probe muss den Adapter stoppen. Default-P4 und P5-Oracle,
Prompts, Modellklasse und Attemptgrenzen bleiben erhalten. Kein Livevergleich
wird als Nebenwirkung dieses Fixes ausgeführt.

Die vorhandenen zwei alten Modellbatches werden nicht wiederholt oder überschrieben.
Ein künftiger Vergleich benötigt ein neues ausdrücklich versioniertes Laufziel und
eine eigene Freigabe für die Modellaufrufe. Hier wird nur die Vorbereitung repariert.

## Risiken, Backout und Review

Betroffene Dateien: vorhandener Eval-Treiber, eine kleine Unit-/Native-Testdatei,
CI-Testeinbindung und diese Evidence. Produkt-Suchcode und historische Berichte
bleiben unverändert. Backout: diesen Slice zurücknehmen; alte Artefakte bleiben
verfügbar. Gescheiterte Checks bleiben sichtbar; keine Guard-/Oracle-Abschwächung.

Vor dem Fix erfolgt ein separater Agentenreview des Plans und der Repro-Evidence.
Dieser Reviewer verwendet dieselbe Modellfamilie; er wird ausdrücklich als
Same-Model-Review und nicht als unabhängig zertifizierende Prüfung ausgewiesen.

Die CLI-Parameter sind gegen die installierte CLI und die offizielle
[Permissions-Dokumentation](https://learn.chatgpt.com/docs/permissions) sowie
[Umgebungs-Konfiguration](https://learn.chatgpt.com/docs/config-file/config-reference)
geprüft. Kein dauerhaftes User-Config-Write.

Status vor Umsetzung: Repro bestätigt; Fix und Regression **NOT RUN**.

### Planpräzisierung nach erstem nativen Regressionstest

Die portable Umsetzung ist grün; der erste native Lauf stoppte zusätzlich an
Windows PowerShell 5: Dort ist die Skriptausführung deaktiviert. Die rohe
Fehlermeldung enthält `PSSecurityException` und erzeugte mit UTF-8-Capture zunächst
einen Decoderfehler. Kein Gate wird deshalb gelockert und keine Execution-Policy
umgangen. Die früheren tatsächlichen Agententools benutzen bereits PowerShell 7.

Der Adapter soll daher diese vorhandene CLI-PowerShell-7-Runtime bevorzugen,
alternativ eine bereits installierte `pwsh`-Runtime. Fehlt beides, stoppt die
Vorbereitung sichtbar; keine Installation und kein PowerShell-5-/Bypass-Fallback.
Der Plan wird vor dieser Anpassung erneut separat im selben Modell geprüft.

## Ergebnis: technischer Fixture-Fix nachgewiesen

Implementierung und Teststand: `96c3528`. Die [maschinenlesbare Evidence](Rule-Routing-Fixture-Runtime-Fix.json)
bindet ausgeführte Code-/Testbytes, Gitblobs, Quelleninventar und Rohberichte.
Private Pfade sind ersetzt; historische P5-Berichte und Fälle sind unverändert.

| Kontrolle | Tatsächliches Ergebnis |
| --- | --- |
| alte Host-Vorbereitung, gleiche PowerShell 7 / gleiches Workspaceprofil | Host ready, Sandbox missing; zwei `.pyc`, Git unsauber; Originalquellen unverändert |
| reparierte Vorbereitung | Sandboxbau und getrennte Folgeabfrage ready; identische Revision/Fingerprintwerte zur Negativkontrolle |
| Quelldateien | in beiden Fixtures alle 578 Dateien bytegleich |
| striktes positives Git-Gate | leerer Gitstatus, keine `.pyc`; keine Bereinigung oder zusätzlichen Ignore-Regeln |
| tatsächliche Runtime | PowerShell 7.6.5, Profil `:workspace`; null Modellaufrufe |

Sieben portable Guardtests bestehen. Sie prüfen einen echten Pythonimport mit
negativer Kontrolle, Profil-/Umgebungstransport, fehlende Runtime, fehlerhafte
Antworten sowie unvollständige oder abweichende Cache-Probes. Der breite Lauf
meldet **111 Tests, OK mit zwei Skips**: bestehende Windows-Symlink-Grenze und
explizit zu aktivierender nativer Fixturetest. Letzterer wurde separat tatsächlich
ausgeführt: **ein nativer Test OK**, keine Skips, 24,104 Sekunden.

Zwei ausschließlich im Speicher entfernte Guards werden erkannt: fehlender
Bytecode-Schalter und fehlende Fingerprintbindung. Je eine Testassertion, keine
Testfehler; Produktionsbytes unverändert. Der enge Lauf ist nach Wiederherstellung
wieder grün. Die früheren roten Schritte und der zusätzliche PowerShell-5-Fehler
bleiben als Development-Evidence erhalten.

Plan, Code und native Evidence wurden separat durch einen Agenten derselben
Modellfamilie geprüft: **Same-Model-Review ohne erkannten Blocker, keine unabhängige
Zertifizierung**. Dieser technische Nachweis ist kein neuer Effizienzvergleich und
kein neuer Live-Agentenlauf. P5 bleibt rückwirkend PARTIAL; sein Retrievalfehlfall
und die Grenzen seines damaligen Vergleichs bleiben bestehen.

Portable Prüfung:

```powershell
.validation/runtime/venv/Scripts/python.exe -m unittest tests.test_rule_routing_fixture_runtime
```

Die native Klasse benötigt die bereits vorhandene Windows-Codex-Sandbox,
PowerShell 7, portable Python- und gepinnte QMD-Runtime. Sie installiert nichts und
startet keine Modell- oder Loginaktion. Explizite Aktivierung in einer temporären Shell:

```powershell
$env:KI_REGELN_NATIVE_FIXTURE = '1'
.validation/runtime/venv/Scripts/python.exe -m unittest tests.test_rule_routing_fixture_runtime.NativeFixtureRuntimeTests
Remove-Item Env:KI_REGELN_NATIVE_FIXTURE
```

Ein künftiger Modellvergleich ist hier **NOT RUN**. Er muss separat versioniert
und nach den technischen Checks ohne parallele Lasttests gestartet werden; aus
diesem Fixture-Fix allein wird keine Einsparung oder Suchpflicht abgeleitet.
