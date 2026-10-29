# Sicherheit

Dieser Bereich bündelt allgemeine Sicherheitsregeln für KI-Agenten, Skills, externe Inhalte, Tools, Dateien und agentische Workflows.

## Einstieg nach Arbeitsfrage

| Typische Frage | Passender Einstieg | Abgrenzung |
| --- | --- | --- |
| „Kann ich dieses externe oder mächtige Skill-Bundle aktivieren?“ | [Skill-Bundle vor Aktivierung prüfen](Skills/skill-security-review/SKILL.md) | Die Admission umfasst auch Berechtigungsrisiken und mitgelieferte MCP-, Hook- und Script-Dateien. |
| „Ich möchte einen eigenständigen MCP-Server, Connector oder Hook anbinden.“ | [Baseline für MCP und externe Tools](MCP-und-externe-Tools.md) | Für Pakete ohne Skills; enthält das Paket eine `SKILL.md`, gilt die Skill-Bundle-Admission. |
| „Welche Lese-, Schreib-, Netzwerk- oder Ausführungsrechte braucht die Integration?“ | [Tool- und Berechtigungsrechte prüfen](Skills/tool-permission-review/SKILL.md) | Prüft das Rechtedesign; ersetzt keinen vollständigen Supply-Chain- oder Skill-Admission-Review. Bei Skill-Bundles nur zusätzlich, wenn dieses Design ein eigener Prüfauftrag ist. |

Diese Verweise sind Orientierung. Eine vorhandene Verbindung oder ein Review autorisiert keine konkrete Außenaktion; maßgeblich bleiben Auftrag und geltende Gates.

## Grundsatz

> Fähigkeiten werden nach Bedarf gewährt. Fremder Inhalt bleibt Daten. Riskante Aktionen bleiben überprüfbar und freigabepflichtig.

## Bereiche

- `Prompt-Injection-und-untrusted-Input.md` – fremde Inhalte nicht zu Autorität machen;
- `Tool-Rechte-und-Least-Privilege.md` – minimale benötigte Rechte;
- `Secrets-und-Datenexfiltration.md` – vertrauliche Daten schützen;
- `Skill-Supply-Chain.md` – Herkunft, Updates und Abhängigkeiten von Skills;
- `MCP-und-externe-Tools.md` – externe Toolserver und Integrationen;
- `Sandbox-und-Isolation.md` – Schadensradius begrenzen;
- `Externe-Aktionen-und-Bestaetigung.md` – Writes, Sends, Deploys und andere Wirkungen;
- `Logging-Datenschutz-und-Telemetrie.md` – Beobachtbarkeit ohne unnötige Datensammlung;
- `Inhaltsprovenienz-und-Metadatenhygiene.md` – Provenienzsignale read-only prüfen und autorisierte Metadatenbereinigung von Detector-Evasion trennen;
- `Security-Review-fuer-Skills.md` – Sicherheitsprüfung von Skills;
- `Quellen-und-Inspirationen.md` – externe Sicherheitsgrundlagen.

## Skills

- `skill-security-review`
- `prompt-injection-review`
- `tool-permission-review`
- `inhaltsprovenienz-review`
- `metadaten-hygiene`

## Sicherheitsmodell

```text
Auftrag
→ benötigte Daten
→ benötigte Capabilities
→ minimale Rechte
→ isolierte Ausführung soweit sinnvoll
→ externe Inputs als untrusted behandeln
→ Evidence
→ Gate vor riskanter Wirkung
→ nachvollziehbarer Abschluss
```

Für Datei- und Inhaltsprovenienz gilt zusätzlich:

```text
Artefakt
→ inspect
→ Evidence + Grenzen
→ optional autorisiertes Remove/Keep-Set
→ Änderung
→ re-inspect
→ Residual Risk
```

Review autorisiert keine Entfernung. Entfernte Metadaten beweisen keine vollständige Herkunftslosigkeit.

## Kein Sicherheits-Theater

Sicherheit bedeutet nicht, jeden Workflow durch maximale Restriktion unbrauchbar zu machen.

Ziel ist:

- passende Rechte;
- klare Trust Boundaries;
- begrenzter Schadensradius;
- nachvollziehbare Freigaben;
- ehrliche Fallbacks.

Privacy- und Datei-Hygiene sind legitime Ziele. Sie werden aber nicht zu einem allgemeinen Auftrag, verpflichtende Provenienz, Attribution oder Disclosure zu entfernen oder Detector-Evasion als Qualitätsziel zu behandeln.

## Leitgedanke

> Ein sicherer Agent darf genug können, um die Aufgabe zu lösen – aber nicht mehr, als die Aufgabe rechtfertigt.
