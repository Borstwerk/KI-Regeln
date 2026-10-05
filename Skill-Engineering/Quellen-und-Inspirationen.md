# Quellen und Inspirationen – Skill Engineering

## Inhalt

- Zweck
- Agent Skills Specification
- Anthropic Skills
- Anthropic Skill authoring best practices
- Anthropic Prompting best practices
- OpenAI Plugins und Apps
- Bestehende Skill-Sammlungen dieses Repositories
- Addy Osmani Agent Skills – Portabilität und Eval-Ratcheting
- Evidence-getriebene Skill-Evolution
- Eigene Synthese
- Leitgedanke

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

## Anthropic Skill authoring best practices

Quelle:

https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices

Semantisch geprüft am 2026-10-03.

Methodisch relevant sind insbesondere:

- `SKILL.md` als kompakter operativer Einstieg und Progressive Disclosure für tiefere Details;
- praktische Zielgröße von unter 500 Zeilen für den `SKILL.md`-Body;
- direkt erreichbare Referenzen und Inhaltsverzeichnisse für lange Referenzdateien;
- unterschiedliche Freiheitsgrade je nach Variabilität und Fragilität eines Arbeitsschritts;
- Scripts für deterministische beziehungsweise besonders fragile Operationen;
- Tests auf den tatsächlich vorgesehenen Modellen statt impliziter Cross-Model-Annahmen;
- explizite Paket-/Toolvoraussetzungen und Prüfung ihrer Verfügbarkeit;
- Feedback-/Validationschleifen für qualitätskritische Arbeit.

KI-Regeln übernimmt daraus vier konkrete Hardening-Linien:

1. Referenz-/Fachdokumente über ungefähr 100 Zeilen sollen ein Inhaltsverzeichnis besitzen oder eine begründete Navigationsausnahme dokumentieren.
2. Skill-Authoring und -Review betrachten hohen, mittleren und niedrigen Freiheitsgrad pro wesentlichem Arbeitsschritt.
3. Modell-/Runtime-Kompatibilität wird über tatsächlich ausgeführte Eval-/Run-Evidence dokumentiert und nicht als herstellerspezifische Pflichtmetadaten in den portablen Skill-Kern eingebaut.
4. Scripts erhalten einen expliziten Dependency Contract; fehlende Packages bedeuten nicht automatisch Installationsautorisierung.

Bewusst **nicht** übernommen werden:

- eine bestimmte Anthropic-Modellfamilie als universelle Testpflicht für alle Hosts;
- ein generisches `model:`-Frontmatter-Feld als zentrale Skillwahrheit;
- unbedingte Paketinstallation bei fehlenden Dependencies;
- die vereinfachte Behauptung, Inhalt nach Zeile 100 sei grundsätzlich nicht sichtbar;
- autonome Selbstmutation produktiver Skills aus einem einzelnen erfolgreichen oder fehlgeschlagenen Lauf.

## Anthropic Prompting best practices

Quelle:

https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

Semantisch geprüft am 2026-10-03.

Für Skill-Engineering relevant ist die aktuelle Trennung:

- bei offenen Problemlösungen Ziel, Kontext und gewünschtes Ergebnis klar beschreiben, ohne unnötig einen internen Denk-/Lösungsweg vorzuschreiben;
- Beispiele und Referenzen gezielt einsetzen, wenn Format, Stil oder Struktur wichtig sind;
- nummerierte beziehungsweise sequenzielle Schritte dort verwenden, wo Reihenfolge oder Vollständigkeit tatsächlich zählt.

Das stützt die lokale Freiheitsgrad-Regel, ohne daraus das Dogma „nie Schritte verwenden“ abzuleiten.

## OpenAI Plugins und Apps

Offizielle Quellen:

https://help.openai.com/en/articles/20001256-plugins-in-chatgpt

https://help.openai.com/en/articles/11487775-apps-in-chatgpt

https://openai.com/business/plugins/

Semantisch geprüft am 2026-10-05.

Für das lokale Capability-Routing relevant sind:

- Plugins als paketierte Workflow-Erweiterungen, die Skills, Apps oder weitere Komponenten enthalten können;
- Apps als konkrete Verbindung zu externen Diensten, Daten und Aktionen;
- getrennte Zustände für Plugin-Installation und notwendige App-/Account-Autorisierung;
- Verfügbarkeit abhängig von Plan, Workspace, Rolle, Region und Oberfläche;
- Plugin-/App-Discovery über ein dynamisches Verzeichnis statt über eine lokal behauptet vollständige statische Liste;
- Verifizierungsstatus als nützliches Signal, aber nicht als Ersatz für organisationsspezifische Datenschutz-, Security- oder Vendorprüfung.

Daraus folgt lokal:

> Fachliche Capability zuerst bestimmen, dann native oder externe Runtime wählen. Verfügbarkeit erweitert Capability, nicht Autorisierung.

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
