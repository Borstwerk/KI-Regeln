# Ergänzung zum Upstream-Audit – 2026-08-23

## Zweck

Diese Ergänzung dokumentiert die Quellenklassifikation für die nach dem ersten Voll-Audit hinzugekommenen Bereiche `Skill-Engineering/`, `Sicherheit/`, `Evals/` und `Workflows/`.

Sie ergänzt `Upstream-Audit-2026-08-23.md`; der ursprüngliche Audit bleibt als historischer Stand unverändert.

## Skill Engineering

### Agent Skills Specification

Quelle:

https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx

Klassifikation:

- mutable konkrete GitHub-Datei;
- `exact-sha`;
- monatlich.

Beobachteter Stand:

- Branch: `main`;
- Blob SHA: `d9a2db099d905da8b879a5c6f996728073985279`.

Begründung:

Die Spezifikation beeinflusst unmittelbar die interoperable Grundstruktur unserer Skills, insbesondere `SKILL.md`, Frontmatter und optionale Ressourcen. Änderungen können deshalb lokal relevant werden.

Entscheidung:

In `upstream-sources.yml` aufgenommen.

## Sicherheit

### OWASP Agentic Skills Top 10

Quelle:

https://owasp.org/www-project-agentic-skills-top-10/

Klassifikation:

- lebender Sicherheitsrahmen;
- `semantic-review`;
- monatlich.

Begründung:

Die Quelle behandelt explizit Skill-Supply-Chain, Over-Privilege, untrusted Instructions, Isolation, Update Drift und Governance. Änderungen können zentrale Sicherheitsregeln direkt beeinflussen.

Entscheidung:

In `upstream-sources.yml` aufgenommen.

### OWASP Top 10 for Agentic Applications 2026

Quelle:

https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

Klassifikation:

- breiterer lebender Sicherheitsrahmen;
- `semantic-review`;
- quartalsweise.

Begründung:

Relevante Änderungen sind wichtig, aber weniger eng an einzelne lokale Skilldateien gekoppelt als der Agentic-Skills-Rahmen.

Entscheidung:

In `upstream-sources.yml` aufgenommen.

### OpenTelemetry GenAI Observability

Berücksichtigte Quelle:

https://opentelemetry.io/blog/2026/genai-observability/

Klassifikation:

- datierter technischer Referenzartikel;
- kein eigener aktiver Upstream-Eintrag.

Begründung:

Der Artikel bestätigt die Richtung des toolneutralen Trace-Datenmodells. Unsere Regeln hängen jedoch nicht an diesem einzelnen Blogartikel oder einer konkreten OTel-Version. Änderungen an der lebenden OTel-Spezifikation können später über den allgemeinen Radar als Kandidat aufgenommen werden.

## Evals

Die initiale Evalstruktur dieses Repositories ist eine eigene Repository-Konvention.

Es wurde kein einzelner externer Eval-Framework-Stand als kanonische Dependency übernommen. Deshalb ist derzeit kein zusätzlicher Upstream nur für `Evals/` erforderlich.

Neue Evalmethoden werden über:

- Agentenarbeits-Radar;
- Skill-Engineering-Radar;
- reale Regressionserfahrungen

bewertet.

## Workflows

Die Recipes kombinieren ausschließlich bereits vorhandene lokale Skills und Regeln.

Sie besitzen aktuell keine eigenständige externe Dependency. Externe Änderungen wirken über die jeweils beteiligten Skills und deren Quellen.

## Abschlussurteil

Nach dieser Ergänzung sind auch die neu hinzugekommenen Meta- und Sicherheitsbereiche in das Quellenmodell eingeordnet.

```text
konkrete mutable Skill-/Spec-Datei
→ exact-sha

lebender Sicherheits-/Produktleitfaden
→ semantic-review

datierter Referenzartikel / Paper
→ Fachquelle, kein künstlicher Sync

lokale Synthese / Recipe
→ keine externe Dependency nur um der Dependency willen
```

## Leitgedanke

> Monitoring folgt tatsächlicher Abhängigkeit – nicht dem Wunsch, jede gelesene Webseite in ein Dependency-System zu pressen.
