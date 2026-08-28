# Skill-Handbuch – Master-Router

Dieses Dokument ist kein zweites Skill-Katalogbuch. Es routet von einem Auftrag zum kleinsten ausreichenden Skill-Satz und verweist für Details auf Katalog, Fachhandbücher und lokale Sources of Truth.

## Startpfad

```text
Nutzerauftrag
→ lokale Sources of Truth
→ passende Domäne / Workflow
→ kleinster ausreichender Skill-Satz
→ Capabilities / Maturity / Evals prüfen
→ Ausführung
→ Verification / Review / Gate
```

Für einen frischen Agenten beginnt der Einstieg in `../AGENTS.md`. Die maschinenlesbare Skill-Wahrheit liegt in `../skill-catalog.yml`; Workflows stehen in `../workflow-index.yml`.

## Routing-Regeln

- Allgemeine Arbeitsweise zentral, konkrete Wahrheit lokal.
- Nicht alle Skills laden. Im Katalog nach `purpose`, `area`, `capabilities` und `related` routen und nur die benötigten `SKILL.md`-Dateien öffnen.
- `maturity` ist Reifeinformation, keine Autorisierung.
- `eval_coverage` beschreibt vorhandene Abdeckung, keinen bestandenen Lauf.
- Toolverfügbarkeit ist keine Autorisierung.
- Ein Workflow erweitert keine Rechte und ersetzt keine Human Gates.
- Bei Near-Misses den enger passenden Skill bevorzugen oder ohne Skill arbeiten, statt einen breiten Skill zu erzwingen.

## Fachhandbücher

Ausführliche Fachbeschreibung wird hier nicht dupliziert. Vorhandene Spezialhandbücher:

| Bereich | Detailrouter |
|---|---|
| Agentenarbeit / Context / Long Horizon | `Skill-Handbuch-Context-und-Long-Horizon.md` |
| Data Engineering | `Skill-Handbuch-Data-Engineering.md` |
| Datenbanken | `Skill-Handbuch-Datenbanken.md` |
| Dokumentationserstellung | `Skill-Handbuch-Dokumentationserstellung.md` |
| Infrastruktur und DevOps | `Skill-Handbuch-Infrastruktur-und-DevOps.md` |
| Reliability und System-Observability | `Skill-Handbuch-Reliability-und-System-Observability.md` |
| Requirements und Spezifikations-Engineering | `Skill-Handbuch-Requirements-und-Spezifikations-Engineering.md` |
| Schnittstellen und Verträge | `Skill-Handbuch-Schnittstellen-und-Vertraege.md` |
| Social Media und Content-Präsenz | `Skill-Handbuch-Social-Media-und-Content-Praesenz.md` |
| Software Architecture und System Design | `Skill-Handbuch-Software-Architecture-und-System-Design.md` |
| Testing und QA | `Skill-Handbuch-Testing-und-QA.md` |
| Wissensmanagement | `Skill-Handbuch-Wissensmanagement.md` |
| Skill Engineering / Sicherheit | `Skill-Handbuch-Meta-und-Sicherheit.md` |

Für Bereiche ohne eigenes Spezialhandbuch ist `Skill-Katalog.md` der menschliche Überblick und `../skill-catalog.yml` die maschinenlesbare Wahrheit. Bereichs-READMEs und lokale Fachdateien liefern anschließend die konkrete Domänenbasis.

## Workflow oder Skill?

- **Workflow** wählen, wenn der Auftrag mehrere klar aufeinanderfolgende Arbeitsphasen verbindet. Vorhandene Workflows ausschließlich aus `../workflow-index.yml` beziehen.
- **Skill** wählen, wenn eine klar begrenzte Fähigkeit genügt.
- **Mehrere Skills** nur dann kombinieren, wenn jeder Skill einen notwendigen Teil des Auftrags abdeckt. `related` ist ein Hinweis, kein Ladebefehl.

## Vor der Ausführung

Für jeden ausgewählten Skill prüfen:

1. Katalog-ID und Pfad;
2. `maturity` und `eval_coverage`;
3. benötigte `capabilities` und lokale Toolrealität;
4. Frontmatter-`description` einschließlich Trigger/Abgrenzung;
5. lokale Regeln, Daten, Versionen und Autorisierung;
6. relevante Evals nur als Evidence verwenden, wenn sie tatsächlich ausgeführt wurden.

## Abschluss

Vor Abschluss mindestens Auftragserfüllung, Quellen-/Evidence-Treue, offene Annahmen, nicht ausgeführte Prüfungen und notwendige Gates nennen.

Bei Änderungen am Repository bevorzugt den lokalen Validation Harness verwenden; keine globale Python-Installation voraussetzen:

```powershell
.\Validate-KI-Regeln.ps1 -Quick
```

Je nach Änderungsumfang `-Full` oder `-Release` verwenden. Kann der vorgesehene Prüfstand in der aktuellen Laufzeit nicht ausgeführt werden, `NOT RUN` beziehungsweise `UNVERIFIED` melden statt einen erfolgreichen Lauf abzuleiten. Details: `Local-Validation-Harness.md`.
