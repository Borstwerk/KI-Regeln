# Reverse Engineering und Binäranalyse

## Auftrag und Grenzen

Diesen Bereich verwenden, wenn das tatsächliche Programmverhalten, die Schnittstellen oder die Unterschiede von **kompilierten Artefakten ohne vertrauenswürdigen Quellcode** untersucht werden sollen. Typische Inputs: EXE/ELF/Mach-O, native DLL, .NET-Assembly, Firmware oder Unity-IL2CPP-Build.

Nicht automatisch zuständig für:
- Review einer vorhandenen Quellcodeänderung → `code-review`;
- Diagnose eines reproduzierbaren Defekts in einer Codebasis → `diagnose`;
- bloße Dateimetadaten oder Provenienzprüfung → passende Sicherheits-/Metadatenarbeit;
- Malware-Containment, produktive Incident-Reaktion oder Umgehung von Zugriffskontrollen → separate Safety-/Security-Gates.

**Scope:** Verstehen und belegen, nicht automatisch ausführen, patchen, Schutzmechanismen umgehen oder Software weiterverteilen.

## Problem-first Routing

| Frage | Primärowner |
|---|---|
| „Was für ein Binary ist das und was können wir damit prüfen?“ | `binary-triage` |
| „Was macht diese Funktion / dieser Pfad im kompilierten Programm?“ | `binary-analysis`; `binary-triage` nur wenn Format/Toolpfad noch unklar |
| „Meine Anwendung wirft einen reproduzierbaren Fehler, Code liegt vor“ | `diagnose`, kein Binary-Skill automatisch |
| „Prüfe diese Änderung im Quellcode“ | `code-review` |
| „Welche Analyse-Rechte benötigt ein neuer MCP-Server?“ | `tool-permission-review` + allgemeine MCP-Admission, nur bei eigenständiger Rechtescope-Frage |
| „Wie unterscheiden sich zwei Binärversionen?“ | `binary-analysis` mit unabhängiger Diff-Evidence; kein neuer Spezialskill ohne separate Eval-Evidence |

Workflow `../Workflows/Binaerdatei-verstehen.md` benutzen, wenn Triage, Untersuchung, Verifikation und Bericht als zusammenhängender Prozess gebraucht werden. Bei klar begrenzter Einzelfrage genügt der passende Skill.

## Fachliche Grundlagen

- `Binaerformate-und-Analysepfade.md` – Native / Managed .NET / Unity IL2CPP.
- `Decompiler-Evidence-und-Hypothesen.md` – Herkunft, Sicherheit der Aussage, Widersprüche.
- `Tool-Scopes-und-Isolation.md` – Autorisierung, READ/WRITE/ACTION, Sandbox und untrusted Samples.
- `Runtime-Capability-Matrix.md` – Optionen und Grenzen der externen Laufzeiten, **keine Installationsanweisung**.

## Was als Evidence zählt

```text
Artifact Hash + Format / Architektur
→ konkrete Fundstelle (Adresse, RVA/Method Token, Referenz)
→ beobachteter Befund
→ daraus abgeleitete Hypothese
→ möglichst unabhängige Gegenprüfung
→ Urteil mit Status und Unsicherheit
```

**Decompiler-Pseudocode ≠ Originalquellcode ≠ beobachtetes Laufzeitverhalten.**

Verifizierte Binärbeobachtung, Decompiler-Interpretation und ungeprüfte Vermutung niemals gleichsetzen. Wenn nur ein Textauszug vorliegt, kann ausschließlich dieser Auszug interpretiert werden; keinen tatsächlichen Binary-Scan behaupten.

## Startstatus

Zwei experimentelle Skills mit definierten, aber nicht automatisch bestandenen Evals. Kein externer Adapter wird bei Repo-Aufnahme installiert oder aktiviert. Die lokale Projektwahrheit (Artefakt, Lizenz/Autorisierung, Symbolstände, Toolversionen) geht allgemeinen Heuristiken vor.
