# Sicherheit

Dieser Bereich bündelt allgemeine Sicherheitsregeln für KI-Agenten, Skills, externe Inhalte, Tools, Dateien und agentische Workflows.

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
