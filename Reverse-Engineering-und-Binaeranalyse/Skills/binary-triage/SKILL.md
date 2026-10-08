---
name: binary-triage
description: Verwenden, wenn ein kompiliertes Artefakt ohne gesicherten Quellcode zunächst read-only nach Datei-/Containerformat, Architektur, .NET vs. nativ vs. IL2CPP und passendem Toolpfad einzuordnen ist. Nicht für gewöhnliches Quellcode-Review oder reine Bugdiagnose.
---

# Binary Triage

Ziel: Eine unbekannte Binärartefakt-Frage **vor** tiefer Funktionsanalyse in einen überprüfbaren Analysepfad übersetzen.

## Trigger und Nichttrigger

Anwenden, wenn:
- ein Binary/Assembly/Firmware-/Unity-Build vorliegt oder dessen Format und Analysefähigkeit unklar sind;
- zunächst geklärt werden muss, was vorliegt und welche sichere Runtime passt;
- vor größerer RE-Arbeit Unsicherheit über Architektur, Packed-/Obfuskationsstatus oder Datenlage besteht.

**Nicht** als Standardvorstufe jeder Funktionsanalyse laden. Wenn Format, Zielmethode und geeignete Laufzeit bereits verlässlich feststehen, `binary-analysis` direkt verwenden. Keine automatische Aktivierung für Code-Review, normale Fehlerdiagnose oder reine Metadatenhygiene.

## 1. Grenzen festlegen

- Autorisierung, Vertraulichkeit, Zweck, relevante rechtliche/vertragliche Grenzen und Außenwirkung klären.
- Analyseobjekt gegen laufendes Produktivsystem abgrenzen.
- Original nicht mutieren und keine unbekannten Binaries zum „Mal sehen“ ausführen.
- Installation, Debugger, Patch oder Script-Ausführung sind kein stiller Fallback.

## 2. Artifact Fingerprint

Bei echtem Dateizugriff, soweit verfügbar:
- Dateigröße, SHA-256, konkreter Datei-/Buildstand;
- PE/ELF/Mach-O/managed assembly/Unity IL2CPP/sonstige Container;
- CPU-Architektur, Bitness, Endianness, Laufzeithinweise;
- Imports/Exports, verfügbare Symbole, Metadaten;
- Indikatoren für Packing/Obfuskation – ausdrücklich nur Hinweise.

Bei lediglich gepostetem Output diese Daten **nicht erfinden**. Solche Werte als `not observed` kennzeichnen.

## 3. Runtime als Capability wählen

- Managed .NET IL → ILSpy/ILSpyCmd, sofern verfügbar.
- Native PE/ELF/Mach-O → Ghidra/IDA oder gleichwertige nachweisbar verfügbare Native-Analyse.
- Unity IL2CPP → native Untersuchung plus bei passenden Artefakten optional Cpp2IL; generierte Stubs nicht als rekonstruierte Logik verkaufen.
- Format unklar → nur read-only Probe/Metadaten, keinen unbegründeten Decompiler-Fallback.

`Runtime-Capability-Matrix.md` nutzen. Konkrete Produkte sind Adapter, nicht die fachliche Skill-Wahrheit.

## 4. Triage-Evidence liefern

Minimal:
- welche Datei / welcher Auszug wirklich geprüft wurde;
- erkannte vs. nur vermutete Artefaktklasse;
- konkret verfügbare READ-Capabilities;
- Fundstellen und Einschränkungen;
- empfohlener nächster begrenzter Untersuchungsschritt;
- relevante WRITE/ACTION-Gates.

## 5. Stop-Regeln

Bei fehlendem Artefakt, unklarer Autorisierung, fehlender sicherer Runtime oder nur inferierten Ergebnissen: `PARTIAL` / `BLOCKED` / `UNVERIFIED` entsprechend benennen. Keine Aussage wie „erfolgreich dekompiliert“ ohne nachgewiesenen Tool-Read.

## Handoff

An `binary-analysis` ausschließlich übergeben: Auftrag, Artefaktidentität, Objektklasse, verfügbare Runtime, beobachtete Fundstellen, verbotene Aktionen und offene Hypothesen. Kein selbst erzeugter Dateipfad oder Symbolname ohne Provenienz.
