# Quellen und Inspirationen – Software Architecture und System Design

Dieser Bereich basiert auf mehreren methodischen Quellen. Keine einzelne Quelle ist verbindliche Architekturlehre für das Repository.

## Fachliche Referenzen

### C4 Model

- Quelle: https://c4model.com/diagrams
- Nutzung: Abstraktionsebenen und zielgerichtete Architekturviews.
- Übernommen: Context-/Container-/Component-/Code-Denken und die Idee, nur notwendige Sichten zu erzeugen.
- Nicht übernommen: Pflicht zur vollständigen Diagrammhierarchie.

### arc42

- Quelle: https://docs.arc42.org/home/
- Nutzung: Coverage-Inspiration für verständliche Architekturdokumentation.
- Übernommen: Ziele/Constraints, Context, Strategy, Building Blocks, Runtime, Deployment, Decisions, Quality und Risks als nützliche Informationsachsen.
- Nicht übernommen: arc42 als verpflichtendes Projekttemplate.

### Carnegie Mellon SEI – Architecture Tradeoff Analysis Method (ATAM)

- Quelle: https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/
- Nutzung: Quality Attributes als konkurrierende Kräfte, Szenarien, Sensitivity Points und Trade-offs.
- Übernommen: Architekturentscheidungen anhand konkreter Qualitätsziele und Szenarien prüfen.
- Nicht übernommen: vollständiger formaler ATAM-Prozess als Pflicht für jede Aufgabe.

### Microsoft Azure Architecture Center – Architecture Styles

- Quelle: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/
- Nutzung: Architekturstile als Optionen mit Constraints, Benefits und Trade-offs.
- Übernommen: Driver vor Stil, Trade-off vor Patternreinheit.
- Nicht übernommen: Azure-spezifische Plattformentscheidungen als globale Defaults.

## Öffentliche Agent-Skills als aktive Inspiration

### pinchen147/system-design-skill – system-design

- Repository: https://github.com/pinchen147/system-design-skill
- Datei: `skills/system-design/SKILL.md`
- Nutzung: evidenzbasiertes Systemdesign aus Invarianten, Workload-Zahlen, Failure Modes und Constraints; einfachstes tragfähiges Design zuerst; Alternativen nur bei echter struktureller Differenz.
- Nicht übernommen: dessen konkretes HTML-/JSON-Artefaktformat, verpflichtende Rendermechanik oder vollständige Skill-Bundle-Struktur.

### lx-wnk/skills – architecture-design

- Repository: https://github.com/lx-wnk/skills
- Datei: `skills/architecture-design/SKILL.md`
- Nutzung: System-Level-Scope, Modul-/Context-Grenzen, Dependency Direction und zurückhaltende ADR-Nutzung.
- Nicht übernommen: künstliche Pflicht zu zwei oder drei Kandidaten und hostspezifische Toolannahmen.

### lx-wnk/skills – architecture-review

- Repository: https://github.com/lx-wnk/skills
- Datei: `skills/architecture-review/SKILL.md`
- Nutzung: read-only Review, Dependency Cycles, Boundary Violations, Shared-Model-Pollution und ADR-Drift.
- Nicht übernommen: stackspezifische Importparser oder hostspezifische Findings-UI als allgemeine Regel.

## Weitere Inspiration

`eligapris/software-architect` und insbesondere `references/fitness-functions.md` lieferten nützliche Ideen zu automatisierten Architekturregeln und Drift-Erkennung. Der Gesamt-Skill wird bewusst nicht als aktiver Kern-Upstream verwendet, da er mehrere zu starre globale Pattern-/Team-/Toolregeln enthält.

## Bewertungsprinzip

> Externe Quellen liefern Modelle, Prüffragen und Gegenbeispiele. Die lokale Architekturentscheidung bleibt vom konkreten System, seinen Requirements, Invarianten und seiner Evidence abhängig.