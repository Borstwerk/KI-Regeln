# Tool-Scopes, Isolation und Berechtigungsgrenzen

## Erst Autorisierung, dann technische Capability

Analysegegenstand, Eigentümer-/Lizenzbedingungen, rechtlich zulässige Nutzung, Datenklassifizierung und externe Datenweitergabe zuerst klären. Die Regeln unterscheiden grundsätzlich legitime Interoperabilität, eigene Software, freigegebene Prüfung und ungeklärte Drittartefakte. Kein pauschales „alle Binaries sind frei analysierbar“.

Das Dokument erteilt keine rechtliche Freigabe.

## Wirkungsgrenzen

| Stufe | Beispiel | Standard |
|---|---|---|
| READ | Hash, Metadaten, Disassembly, Xrefs, dekompilierte Sicht | Nur freigegebene Artefakte; vorzugsweise isoliert und ohne Netz |
| WRITE (Analyseprojekt) | Rename, Kommentare, Datentypen, Bookmarks | Separater Workspace-/Projekt-Write-Scope; Original geschützt |
| WRITE (Binary) | Patch, Rebuild, veränderte ausführbare Datei | Gesonderte Freigabe, diffbare Änderung, Backout |
| ACTION | unbekannte Datei starten, debugger attach, instrumentieren, live memory lesen, Netzverkehr | Explizite Autorisierung, starke Isolation, begrenzte Ziele und Human Gate |

Keine automatisch hochprivilegierte Ausführung, nur weil Analyse mit READ nicht ausreicht. `READ` in einem MCP-Tool bedeutet nicht automatisch, dass dessen **Serverprozess** keine lokalen Rechte besitzt.

## MCP / Plugin Admission

Basierend auf `../Sicherheit/MCP-und-externe-Tools.md`:
- Provenienz, License, Release/Commit-Pinning und Transitive Dependencies;
- lokale Ports, Bind-Adresse, Authentisierung, Dateizugriff und Netzwerkrouten prüfen;
- Toolinventar nach tatsächlich verfügbaren READ/WRITE/ACTION-Funktionen aufnehmen;
- Scripts/Arbitrary Code, Import-/Delete-/Export-Endpunkte und Debugger-Rechte gesondert blocken;
- Least Privilege: zunächst nur die benötigten READ-Tools sichtbar machen; kein Auto-Approve für Mutation;
- ein MCP-Server ohne Skills ist nicht automatisch ein Skill-Bundle; ein Paket mit `SKILL.md` dagegen schon.

Ghidra-MCP-Varianten unterscheiden sich erheblich. Ein Server mit Funktionsannotationen, Schreibrechten und Scriptausführung ist nicht allein durch seinen Namen „read-only“.

## Unbekannte Binaries

- nur Kopien/immutable Inputs untersuchen;
- kein Doppelklick, kein ungefragtes Ausführen, Import/Parsing wenn möglich in separater Umgebung;
- Sandbox ohne vertrauliche Host-Daten/Secrets und standardmäßig ohne ausgehendes Netzwerk;
- Log-/Dump-Inhalte auf Geheimnisse und personenbezogene Daten prüfen;
- beim Export von Decompilation/Strings an externe KI-Provider Datenschutz und Vertraulichkeit beachten;
- dynamische Instrumentierung nur im vereinbarten begrenzten Scope, keine Evasion-/Bypass-Ketten.

## Ergebnisse

Wenn Capability, Rechte oder Isolation fehlen: read-only Auszug unter Einschränkung diskutieren oder `BLOCKED`/ `UNVERIFIED` ausgeben. Kein verschleierter Toolwechsel als Umgehung einer Grenze.
