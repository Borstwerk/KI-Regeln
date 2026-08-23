# Quellen und Inspirationen – Skill Engineering

## Zweck

Diese Datei dokumentiert externe Grundlagen, die beim Aufbau der allgemeinen Skill-Engineering-Regeln berücksichtigt wurden.

Externe Spezifikationen und Beispiele sind Referenz und Vergleichsmaterial. Sie ersetzen nicht die lokale Bewertung, ob ein Skill für dieses Repository sinnvoll geschnitten und sicher ist.

## Agent Skills Specification

Quelle:

https://agentskills.io/specification

Repository:

https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx

Beobachteter Stand am 2026-08-23:

- Branch: `main`
- Blob SHA: `d9a2db099d905da8b879a5c6f996728073985279`

Relevante Konzepte:

- Skill als Verzeichnis mit mindestens `SKILL.md`;
- YAML-Frontmatter mit `name` und `description` als Pflichtfeldern;
- optionale `scripts/`, `references/` und `assets/`;
- `description` beschreibt sowohl Fähigkeit als auch Einsatzsituation;
- optionale Compatibility- und Toolmetadaten.

Übernommen wird die interoperable Grundstruktur, nicht jede experimentelle Metadatenerweiterung als zentrale Pflicht.

## Anthropic Skills

Quelle:

https://github.com/anthropics/skills

Relevante Beobachtung:

- öffentliche Skills zeigen kompakte operative Anweisungen und ergänzende Ressourcen;
- die frühere Agent-Skills-Spezifikation verweist inzwischen auf `agentskills.io`.

## Bestehende Skill-Sammlungen dieses Repositories

Für die Regeln wurden außerdem die bereits ausgewerteten Sammlungen aus Programmieren, Recherche, Webentwicklung und Dokumentationserstellung als Praxisbeispiele betrachtet.

Daraus stammen insbesondere die allgemeinen Anforderungen an:

- Near-Miss-Negatives;
- explizite Exit-/Verification-Gates;
- Fallbacks bei fehlenden Capabilities;
- getrennte Review-Skills;
- kleine, klar verantwortete Skillbausteine.

## Eigene Synthese

Dieses Repository ergänzt die reine Dateiformatfrage bewusst um:

```text
Format
≠ Triggerqualität
≠ fachlicher Skill-Schnitt
≠ Capability-Vertrag
≠ Sicherheitsmodell
≠ Evalqualität
≠ Lifecycle
```

Die Spezifikation beantwortet, wie ein Skill technisch beschrieben werden kann. `Skill-Engineering/` beantwortet zusätzlich, wann ein Skill gut entworfen ist.

## Leitgedanke

> Interoperables Format ist die Basis. Vorhersagbares Verhalten ist das eigentliche Qualitätsziel.
