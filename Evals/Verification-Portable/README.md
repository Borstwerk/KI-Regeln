# Native Verification Pilot – Praxisprobe (PR C)

Dieser bewusst eng begrenzte Pilot prüft die Verbindung aus nativer Projektprüfung,
optionalem verification-run-v1-Evidence-Vertrag und dem Offline-HTML-Renderer.
Es ist **kein** universeller Test-Runner und **kein** automatischer Agenten-Test.

## Echte Prüfungen

| Szenario | Laufzeit | Erwartetes Ergebnis |
| --- | --- | --- |
| powershell | PowerShell 7: eigener Discount-Code plus native Assertions | PASS bei Exitcode 0 und Abschlussmarker |
| dotnet | .NET SDK 8: C#-Konsolenprojekt mit eingebauten Assertions | PASS bei Exitcode 0 und Abschlussmarker |
| missing-runtime | absichtlich nicht existierender Toolname | NOT_RUN ohne Exitcode und ohne Evidence |

Das dritte Szenario ist eine **kontrollierte Negativprobe**: Sein Wrapper
verlässt den Prozess nur deshalb mit 0, damit CI den erwarteten NOT_RUN-Datensatz
prüfen kann. Bei tatsächlich fehlendem PowerShell-/dotnet-Tool endet der normale
Prüfaufruf mit Code 2 und **nicht** mit PASS.

## Lokale Ausführung (PowerShell 7)

```powershell
pwsh -NoProfile -File Evals/Verification-Portable/Run-Pilot.ps1 -Scenario powershell -Report .validation/pilot/powershell.json
pwsh -NoProfile -File Evals/Verification-Portable/Run-Pilot.ps1 -Scenario dotnet -Report .validation/pilot/dotnet.json
pwsh -NoProfile -File Evals/Verification-Portable/Run-Pilot.ps1 -Scenario missing-runtime -Report .validation/pilot/missing-runtime.json
```

Der C#-Check benötigt das .NET-8-SDK. Der Pilot installiert keine Laufzeiten
oder Testpakete. C# verwendet eingebaute Assert-Logik, **nicht** xUnit oder NUnit;
PowerShell verwendet eigene Assertions, **nicht** Pester.

Der gebundene SHA-256-Snapshot umfasst ausschließlich die benannten
Fixture-Quelldateien und Run-Pilot.ps1: sortierte Zeilen
relative/path:sha256(file), UTF-8 mit LF und abschließendem LF.
Das ist kein attestierter Git-Tree und kein Beweis gegen manipulierte Tools.

## Bericht

```powershell
python tools/verification_report_html.py --input .validation/pilot/powershell.json --output .validation/pilot/powershell.html
```

Der Renderer zeigt bestehende Daten an, bewertet aber keine Tests neu.
GitHub Actions prüft Windows und Linux separat und stellt JSON/HTML als
kurzlebige Artifacts bereit. Die generierten Log-Dateien bleiben lokal und
werden **nicht** als GitHub-Artifact hochgeladen. Bei echten Projekten dürfen
unbereinigte Logs, Secrets oder produktive Daten nie automatisch publiziert werden.

## Grenzen

- Diese Ergebnisse betreffen ausschließlich kleine Test-Fixtures, nicht beliebige Projekte.
- Vorhandene Projekt-/OS-Befehle haben Vorrang; dynamische Fremdskripte werden nicht ausgeführt.
- Es wird kein Gesamt-PASS abgeleitet, keine Releasefreigabe gegeben.
- B2-Behavioral-/Auth-Piloten werden nicht gestartet und bleiben unverändert.
- Browserdarstellung und Benutzerverständlichkeit benötigen noch einen visuellen Human-Check.
