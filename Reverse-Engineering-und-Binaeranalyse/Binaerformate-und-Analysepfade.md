# Binärformate und Analysepfade

## Vor dem Tool: Was liegt vor?

1. Auftrag, Berechtigung und Vertraulichkeit klären; Original in einen unveränderlichen Arbeitsstand übernehmen.
2. SHA-256 und Herkunft **nur bei tatsächlichem Dateizugriff** ermitteln; sonst als nicht vorliegend kennzeichnen.
3. Container/Dateiformat und CPU-Architektur unterscheiden: PE, ELF, Mach-O, Firmware/Raw, Managed .NET, Unity Mono, Unity IL2CPP oder unbekannt.
4. Signed/unsigned, Packer-/Obfuskationshinweise, Debug-Symbole, Ressourcen und Metadaten dokumentieren, soweit nachweisbar.
5. Analyzer und Capability anhand der realen Objektart wählen; bei Unsicherheit zunächst READ-only Metadaten/Triage.

## Pfade

| Artefakt | Primäre Analyseebene | Typische Runtime |
|---|---|---|
| PE/ELF/Mach-O nativ | Imports/Exports, Assembly, Disassembly, Xrefs, Kontrollfluss | Ghidra oder IDA; CLI/Headless nach Capability |
| Managed .NET (IL) | Metadaten, Typen, Methoden, IL, dekompilierter C# | ILSpy / ILSpyCmd |
| Unity Mono | Managed Assembly + passende Runtime-Metadaten | ILSpy; Unity-Spezifika separat |
| Unity IL2CPP | Native Code + separate IL2CPP-Metadaten | Cpp2IL als möglicher Metadaten-/Rekonstruktionspfad plus native Analyse |
| unbekannt/packed | Format-/Packersignale und Limitationen zuerst | Capability Detection; eventuell Spezialisten |

**Unity IL2CPP ist nicht einfach eine gewöhnliche .NET-DLL.** Aus generierten Stubs oder Metadaten folgt nicht, dass Methodenlogik vollständig rekonstruiert wurde. Cpp2IL ist versions- und buildabhängig; nur für die tatsächlich nachgewiesenen Outputs Aussagen machen.

Binärformate können verschachtelt sein. Bei .NET mit Native AOT, ReadyToRun und gemischten Modulen ist das Format allein keine Garantie für die beste Decompilerroute.

## Fallbacks und Status

- Datei/Tool fehlt → `BLOCKED` für tatsächliche Analyse; rein methodische Einordnung bleibt möglich.
- Nur geposteter Pseudocode/Strings/Logs → `PARTIAL`, Quelle als bereitgestellten Auszug kennzeichnen.
- Symbole fehlen → Adressen + beobachtete Struktur dokumentieren, Funktionsnamen als Hypothese markieren.
- Obfuskation/Packing erkannt → Abdeckungsgrenze und falsch-negative Analyseergebnisse benennen.
- Architektur/Format unklar → kein Tool willkürlich installieren oder ausführen.

## Nicht daraus ableiten

- Decompiler-Variable `password` beweist kein gespeichertes Passwort.
- Eine String-Konstante beweist nicht, dass der dazugehörige Code ausgeführt wird.
- Import/API-Xref beweist Möglichkeit, nicht tatsächlich ausgeführten Pfad.
- Ein fehlender Treffer einer Signaturregel beweist nicht die Abwesenheit der entsprechenden Funktion.
