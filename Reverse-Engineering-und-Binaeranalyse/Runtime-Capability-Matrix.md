# Runtime-Capability-Matrix für Reverse Engineering

Diese Matrix ist **Discovery-Metadatum**, kein Aktivierungsbefehl. Tools nur nach lokal verfügbarer Version, Format, Lizenz/Autorisierung und konkret geprüften Rechten einsetzen. Die Links sind Upstream-Referenzen, keine Installations- oder Supply-Chain-Freigabe.

| Runtime | Schwerpunkt | Agentenpfad | Caveats / Rights |
|---|---|---|---|
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | native PE/ELF/Mach-O, Disassembly, Decompilation, Xrefs | GUI, Scripting/PyGhidra, optional MCP | Versionsabhängige Parser/Advisories; Skripte und Projektschreibrechte nicht READ |
| [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP) | Bridge von Ghidra zum Agenten | MCP / lokale Bridge | Plugin + Python Bridge, Ports/Host und angebotene Mutation einzeln prüfen |
| [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | breite Ghidra-Agentenautomation | MCP + GUI/Headless | viele Tools inkl. Write/Script/Debugger; deshalb strikte Whitelist |
| [IDA MCP (offiziell)](https://github.com/HexRaysSA/ida-mcp) | IDA/Hex-Rays Datenbank und Decompiler | MCP/idalib | benötigt geeignete IDA-Lizenz/Version; konkrete Rechte prüfen |
| [ILSpy](https://github.com/icsharpcode/ILSpy) | Managed .NET IL/Metadata/C# | ILSpyCmd, Bibliothek/PowerShell | dekompiliertes C# ist Rekonstruktion; keine generische Native-Route |
| [Cpp2IL](https://github.com/SamboyCoding/Cpp2IL) | Unity IL2CPP Metadaten / IL-Rekonstruktion | CLI | Work in Progress; Version/Format und Coverage nachweisen, Stubs ≠ Originalcode |
| [BinDiff](https://github.com/google/bindiff) | differenzielle Binär-/Funktionsanalyse | Export/CLI/GUI je Runtime | Matching heuristisch; Versionsunterschied nicht automatisch Ursache |
| [capa](https://github.com/mandiant/capa) | regelbasierte Erkennung möglicher Fähigkeiten | CLI | Packen/Obfuskation kann False Negatives erzeugen; Match mit Fundstellen prüfen |
| [FLOSS](https://github.com/mandiant/flare-floss) | Strings/decoded Strings | CLI | Stringbefund ≠ Reachability/Ausführung |
| [angr](https://github.com/angr/angr) | weiterführende symbolische Analyse | Python | Ressourcen-/Constraint-Kosten, nicht Default für einfache Triage |

**Adapterwahl:** Native vs. Managed .NET vs. IL2CPP zuerst unterscheiden. Ein Tool muss real verfügbar sein; kein ungefragtes Installieren. Ghidra und IDA sind Alternativen für denselben nativen Analysejob; nicht standardmäßig beide laden. CLI ohne MCP reicht, wenn sie den Job sicher und reproduzierbar erfüllt.

**Acceptance:** Toolresultat allein ≠ Binary-Verhalten bewiesen. Siehe `../Skill-Engineering/Agent-Tool-Vertraege.md` und `Decompiler-Evidence-und-Hypothesen.md`.
