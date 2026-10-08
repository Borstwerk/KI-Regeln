# Upstream-Audit – Reverse Engineering und Binäranalyse – 2026-10-08

## Auftrag

Prüfung, ob KI-Regeln neben Quellcode-Review und Bugdiagnose eine eigene Fachdisziplin für **autorisierte Binäranalyse ohne verlässlichen Quellcode** benötigt. Die Repositories sind Methoden- und Adapterreferenzen, **keine** unmittelbar zur Installation freigegebenen Abhängigkeiten.

## Ergebnis

**Neuer, schmaler Fachbereich mit zwei Skills und einem Workflow**, kein Skill pro Tool. Die fachliche Trennung ist sinnvoll: `binary-triage` identifiziert Format/Capability und `binary-analysis` untersucht konkrete Verhaltens-/Datenflussfragen. Beide bleiben experimentell. Tool-/Runtime-Integration ist kein automatischer Security Pass.

## Geprüfte öffentliche Upstreams

| Repository | Stand (SHA-Präfix) | Lizenzmetadatum | Relevanz |
|---|---|---|---|
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | `c7bc89dd29ee` | Apache-2.0 | native Analyse, Headless/Scripting, breite Binärformate |
| [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP) | `27f316f80139` | Apache-2.0 | lokale MCP-Bridge zum Ghidra-Projekt |
| [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | `59c3d90a2a9b` | Apache-2.0 | breite MCP-Funktionen bis Write/Scripts/Debugger; Scope-Risiko |
| [Hex-Rays IDA MCP](https://github.com/HexRaysSA/ida-mcp) | `2e62361d4c47` | MIT | offizieller IDA-Agentenpfad; passende IDA-Version/Lizenz nötig |
| [ILSpy](https://github.com/icsharpcode/ILSpy) | `accbd3eda041` | MIT | Managed-.NET-/IL-Dekompilation, `ilspycmd` ohne MCP |
| [Cpp2IL](https://github.com/SamboyCoding/Cpp2IL) | `b5ad444b8226` | MIT | Unity IL2CPP, Entwicklungs-/Rekonstruktionsvorbehalte |
| [BinDiff](https://github.com/google/bindiff) | `13c437afa074` | Apache-2.0 | binary diff und heuristische Funktionskorrespondenz |
| [capa](https://github.com/mandiant/capa) | `d4cf889f2083` | Apache-2.0 | statische/dynamische Fähigkeitsindikatoren, Packing-Grenze |
| [FLOSS](https://github.com/mandiant/flare-floss) | `8617d875abae` | Apache-2.0 | rekonstruiert/entdeckt versteckte Strings |

SHA-Präfixe beziehen sich auf die jeweils zum Audit beobachteten Default-Branches. Sie sind **Quellenstände**, keine garantierten stabilen Releases. Lizenzangaben stammen aus Repository-Metadaten; Transitivlizenzen und konkrete Binary-Releases sind bei einer späteren tatsächlichen Installation separat zu prüfen.

## Gegenüber bestehendem KI-Regeln

Bereits vorhanden:
- `Programmieren/Skills/diagnose` für reproduzierbare Bugs mit Feedback-Loop;
- `Programmieren/Skills/code-review` für Quellcodeänderungen/Diffs;
- MCP-Admission und Least-Privilege-Gates in `Sicherheit/`;
- Agent-Tool-Verträge (Capability, Outputs, Fehler, Acceptance) in `Skill-Engineering/`;
- Run-/Trace-Verträge in `Agentenarbeit/`.

**Fehlte:** Routing nach Binärformat, Decompiler-Evidence als schwache Rekonstruktion, Address-/Method-Token-Provenienz, Unknown-Binary-Isolation und sichere Durchleitung von RE-Ergebnissen zu einer begrenzten Verhaltensaussage.

## Adopt / Don't Adopt

Übernehmen:
- Format-/Capability-getriebene Runtime-Wahl (native vs. .NET vs. IL2CPP);
- Evidence-Chain: Artefakt → Fundstelle → Beobachtung → Hypothese → Gegenprüfung;
- klare Trennung von READ, Analyseprojekt-WRITE, Binary-Patch-WRITE und dynamischer ACTION;
- Tooloutputs/Binary-Strings als untrusted Daten;
- explizite Stop-/Unverified-Zustände bei fehlender Binary-Evidence.

Nicht übernehmen:
- Fremd-Skillbundle, Pluginmarketplace, Installations- und Autoupdate-Anweisungen;
- automatische Aktivierung mächtiger MCP-Endpunkte;
- Hersteller-/Produktnamen als fachliche Trigger-Wahrheit;
- Annahme, dass ein Decompiler ursprünglichen Code oder ausgeführtes Verhalten garantiert;
- „keine Treffer“ als Abwesenheitsbeweis.

## Evaluationsgrenze

Neu definierte Evalcases und GT-18 sind **Testdefinitionen, keine ausgeführten Behavioral-Pässe**. Repo-Validator und Blind-Package-Vorbereitung prüfen nur Struktur/Blindness. Die eigentliche fachliche Verbesserung muss in einem unabhängigen frischen Agentenlauf geprüft werden.

## Nächste Ausbaustufe – bewusst nicht in diesem PR

- optional eigener Binärvergleichs-Skill erst nach echtem Nachfrage-/Eval-Signal;
- echte selbst kompilierte, unkritische Testbinaries mit dokumentierten Symbol-/Optimierungsvarianten für End-to-End-Grounding;
- isolierter Runtime-/MCP-Test nur nach expliziter Admission, Version-Pinning und Permission-Review.
