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
   Netzwerkrechte, Shared-Runtime-Writes oder ACL-Änderungen.
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
