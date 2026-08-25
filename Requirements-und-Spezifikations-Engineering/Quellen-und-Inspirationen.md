# Quellen und Inspirationen – Requirements und Spezifikations-Engineering

Dieser Bereich kombiniert etablierte Requirements-Engineering-Quellen mit ausgewählten aktuellen Agent-Skills. Keine einzelne Quelle wird als universelle Prozess- oder Dokumentpflicht übernommen.

## Fachliche Referenzen

### IREB / CPRE

- Foundation Level: https://cpre.ireb.org/en/concept/foundationlevel
- Requirements Elicitation: https://cpre.ireb.org/en/concept/requirements-elicitation
- Nutzung: Requirements Sources, Elicitation, Work Products, Validation, Konfliktklärung und Management als Kernaktivitäten.
- Übernommen: situationsangepasste Auswahl von Techniken, sichtbare Quellen und Konflikte, Validation und Lifecycle-Denken.
- Nicht übernommen: Zertifizierungsstruktur als Prozesspflicht oder eine starre Dokumentform.

### ISO/IEC/IEEE 29148

- veröffentlichter Stand 2018: https://www.iso.org/standard/72089.html
- laufender Draft Edition 3 (2026): https://www.iso.org/standard/94091.html
- Nutzung: Requirements-Prozesse über den Lifecycle, Requirement-Qualität, Information Items und Traceability.
- Wichtig: Der 2026er Stand ist ein Draft und wird deshalb als lebender Review-Upstream behandelt, nicht als bereits veröffentlichter Ersatz für 2018.
- Nicht übernommen: vollständige Normkonformität oder bestimmte Information Items als Pflicht für jedes Projekt.

### NASA Systems Engineering Handbook

- System Design Processes / Requirements: https://www.nasa.gov/reference/4-0-system-design-processes/
- Appendix mit Good-Requirement- und V&V-Hinweisen: https://www.nasa.gov/reference/system-engineering-handbook-appendix/
- Nutzung: Trennung von Stakeholder Expectations und Requirements, Requirements Validation, Verifizierbarkeit und Verification Intent.
- Nicht übernommen: NASA-spezifische Projekt-/Review-Governance als allgemeiner Softwareprozess.

## Öffentliche Agent-Skills

### Modular Earth – requirements

- Repository: `Modular-Earth-LLC/solutions-architecture-agent`
- Pfad: `skills/requirements/SKILL.md`
- beobachteter Blob-SHA: `06ab931a6898d5f9f455d0b2d00ee7fabad9f15c`
- Nutzung: progressive Discovery, explizite Sources/Assumptions, Scope Boundaries, Requirements-Kategorien, Human Checkpoint und klare Grenze zur Architektur.
- Nicht übernommen: BANT/Pre-Sales-Fokus, AI-Suitability-Scoring, AWS-/GenAI-spezifische Felder oder feste Complexity Scores.

### Microsoft HVE Core – requirements-author

- Repository: `microsoft/hve-core`
- Pfad: `.github/skills/project-planning/requirements-author/SKILL.md`
- beobachteter Blob-SHA: `ebeca3bfba19ee3cba90648df16cb4fddac5c319`
- Lizenz laut Upstream: CC-BY-4.0.
- Nutzung: Discover/Define/Govern-Denken, Traceability, Handoffs, Supersession und getrennte Validation-/Governance-Schritte.
- Nicht übernommen: BRD-/PRD-Pflicht, feste Coverage-Thresholds, kanonische Template-/ID-Schemata oder host-/repo-spezifische Handoff-Payloads.

### Spacey6849 AgentSkills – requirements-analysis

- Repository: `Spacey6849/AgentSkills`
- Pfad: `.claude/skills/requirements-analysis/SKILL.md`
- beobachteter Blob-SHA: `4a9193522eb25f9029e09dbab5579224420dc0bb`
- Nutzung: frühes Finden von Ambiguität, fehlenden Acceptance Criteria, Dependencies und versteckter Komplexität.
- Nicht übernommen: pauschale Complexity-Schätzung als Requirements-Qualität oder die Annahme, dass jede Anforderung direkt einen automatisierten Test ergeben muss.

## Bewusste Nicht-Dogmen

Nicht aus Quellen oder Agent-Skills übernommen:

- `Clarity Score >= 90` oder andere numerische Readiness-Schwellen ohne lokale Grundlage;
- User Stories als universelles Requirement-Format;
- PRD, BRD oder SRS als Pflichtdokumente;
- EARS oder Given/When/Then als Pflichtsyntax;
- MoSCoW/RICE/P0-Priorisierung als zentrale Policy;
- vollständige NFR-Taxonomien als Checklistenbeweis;
- automatisch erzeugte Architektur oder Implementierungsphasen aus einem Requirements-Dokument;
- erfundene Benchmarks, Compliance-Regeln oder Zielwerte.

## Leitgedanke

> Quellen liefern Methoden und Prüffragen; verbindliche Anforderungen entstehen nur aus dem lokalen Bedarf und seinen autoritativen Quellen.