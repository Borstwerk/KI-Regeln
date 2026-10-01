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

## Addy Osmani Agent Skills – Portabilität und Eval-Ratcheting

Repository:

https://github.com/addyosmani/agent-skills

Geprüfter Stand:

- Release-/Repository-Stand: `0.6.11`
- Repository-Commit: `2686b620fc1fed2e8f60c704839c766b8594c6b6`
- `docs/advanced-per-agent-configuration.md`: Blob-SHA `d06a87b7cec0c657ee321fbcd8d910d074ee5954`
- `evals/README.md`: Blob-SHA `4f501cdb0da265812458c43f2bc433b056fb357b`
- Lizenz am geprüften Stand: MIT

Methodisch relevant sind zwei getrennte Muster:

1. **Portabler Skill-Kern / Runtime-Adapter**  
   Fachliche Skilllogik bleibt hostübergreifend; Modellrouting, konkrete Tools, Turn-Limits und client-spezifische Orchestrierung werden als Runtime-Konfiguration behandelt.

2. **Eval-Ratchet**  
   Ein reproduzierbar gemessener Routing-/Qualitätsstand kann als Floor geschützt werden, damit spätere Änderungen den gemessenen Stand nicht still verschlechtern.

KI-Regeln übernimmt daraus bewusst **keine** konkreten Vendor-Felder, Modellnamen, Toollisten, TF-IDF-Routinglogik oder die dortige CI-Schwelle. Lokal generalisiert werden nur die Trennung Kern/Adapter sowie die Ratchet-Governance auf einer vergleichbaren, eigenen Messbasis.

## Evidence-getriebene Skill-Evolution

### EvoSkill

Paper:

https://arxiv.org/abs/2603.02766

Repository:

https://github.com/sentient-agi/EvoSkill

Geprüfter Repository-Stand:

- Commit: `36f6f04952293d7054145550c2b9f0b0411bff1c`
- README-Blob-SHA: `61565ea29a63b42242dbe33d4ba3df3cec752c85`
- Lizenz am geprüften Stand: Apache-2.0

Methodisch relevant sind Failure Analysis, explizite Änderungskandidaten und getrennte Validierung auf nicht zur Änderung verwendeten Aufgaben.

Nicht übernommen wird autonome Skill-Selbständerung als Freigabemechanismus. In KI-Regeln erzeugt Failure Evidence nur einen reviewbaren Kandidaten.

### SkillClaw

Paper:

https://arxiv.org/abs/2604.08377

Repository:

https://github.com/AMAP-ML/SkillClaw

Geprüfter Repository-Stand:

- Commit: `3938f7537645c961d94498a0a79fc0a977019595`
- README-Blob-SHA: `9158146e42a17247e15934879f7f5265bdbd6484`
- Lizenz am geprüften Stand: MIT

Methodisch relevant ist, wiederkehrende Session-/Trajektorien-Signale zu aggregieren, zu deduplizieren und als Input für Skillpflege zu verwenden.

Nicht übernommen werden automatische globale Verteilung oder selbstautorisierte Updates einer gemeinsamen Skill-Library.

### Trajectory Poisoning als Gegenbeleg

Paper:

https://arxiv.org/abs/2608.05563

Die Arbeit untersucht, wie manipulierte Nutzungstrajektorien bei selbst-evolvierenden Skill-Systemen in dauerhafte Instruktionen übergehen können. Methodisch relevant ist deshalb die zusätzliche Trust Boundary zwischen beobachteter Erfahrung und ihrer Promotion in persistente Skillregeln.

KI-Regeln leitet daraus ab:

- Field-/Trajectory-Evidence bleibt untrusted;
- Wiederholung ist kein Vertrauensbeweis;
- Provenance und Quellenunabhängigkeit müssen vor Promotion betrachtet werden;
- autonome Evolution erhält keine eigene Freigabeautorität.

### SkillAudit und verwandte Forschung

Paper:

https://arxiv.org/abs/2606.14239

Methodisch relevant ist der Vergleich mit/ohne Kandidat und die Trennung von Verbesserung und Reparatur, besonders wenn perfekte Ground Truth fehlt.

Ergänzende aktuelle Arbeiten zu Skill-Evolution bestätigen außerdem das Risiko von Drift, Overfitting und unnötigem Skillwachstum. KI-Regeln übernimmt daraus keine Benchmark- oder Framework-Defaults, sondern die Governance-Regel:

> Änderungssignal, Änderungskandidat, unabhängige Evidence und Freigabe bleiben getrennte Rollen.

Diese Paper sind datierte Forschungsquellen und werden nicht künstlich als mutable Upstream-Dependencies registriert.

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
