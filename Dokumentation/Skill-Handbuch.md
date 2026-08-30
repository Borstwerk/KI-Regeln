# Skill-Handbuch – Master-Router

Dieses Dokument ist kein zweites Skill-Katalogbuch. Es routet von einem **konkreten Problem oder Auftrag** zum kleinsten ausreichenden Skill-Satz und verweist für Details auf Katalog, Fachhandbücher und lokale Sources of Truth.

Der Nutzer muss dafür weder die richtige Domäne noch einen Skill-Namen kennen.

## Startpfad

```text
Problem / Nutzerauftrag
→ lokale Sources of Truth und verfügbare Evidence
→ Aufgabe fachlich einordnen
→ passende Domäne / vorhandenen Workflow prüfen
→ kleinsten ausreichenden Skill-Satz wählen
→ Capabilities / Maturity / Evals prüfen
→ Ausführung
→ Verification / Review / Gate
```

Für Menschen ohne Repository-Vorkenntnisse beginnt der Einstieg in `../START-HIER.md`. Für einen frischen Agenten beginnt er in `../AGENTS.md`. Die maschinenlesbare Skill-Wahrheit liegt in `../skill-catalog.yml`; Workflows stehen in `../workflow-index.yml`.

## Problem-first Routing

Nicht vom Werkzeugnamen ausgehen, sondern von der zu erledigenden Arbeit.

| Beispielhafter Auftrag | Typischer erster Routingraum |
|---|---|
| „Prüfe, ob diese Behauptung stimmt.“ | Recherche |
| „Schreib oder überarbeite diesen Text.“ | Schreiben |
| „Hilf mir, Figuren, Plot oder Welt für eine Geschichte zu entwickeln.“ | Storyentwicklung und Fiktion |
| „Ordne meine Rücklagen, Schulden oder Anlageoptionen ein.“ | Finanzen |
| „Erstelle oder prüfe eine Bildserie.“ | Bildarbeit |
| „Baue oder prüfe diese Website.“ | Webentwicklung |
| „Finde die Ursache dieses Fehlers.“ | Programmieren / Diagnose, je nach System weitere Fachdomänen |
| „Dokumentiere diese Datenbanktabelle.“ | Dokumentationserstellung + Datenbanken |
| „Kläre, was dieses Feature eigentlich können soll.“ | Requirements und Spezifikations-Engineering |
| „Baue eine langfristig nutzbare Wissensbasis.“ | Wissensmanagement |

Die Tabelle ist keine vollständige Routingmatrix. Ein Auftrag kann mehrere Domänen berühren; trotzdem gilt: **so wenig Werkzeuge wie möglich, so viele wie nötig**.

## Routing-Regeln

- Allgemeine Arbeitsweise zentral, konkrete Wahrheit lokal.
- Der Nutzer muss keine Skill-Namen kennen. Fehlende Skill-Auswahl ist Aufgabe des Routers, nicht automatisch eine Rückfrage an den Nutzer.
- Nicht alle Skills laden. Im Katalog nach `purpose`, `area`, `capabilities` und `related` routen und nur die benötigten `SKILL.md`-Dateien öffnen.
- Vor einer Rückfrage prüfen, ob Auftrag, lokale Quellen oder vorhandene Artefakte die Information bereits liefern.
- Nur Informationen erfragen, die für die konkrete Aufgabe materiell fehlen; keine unnötige Vollerhebung oder sensible Datensammlung.
- `maturity` ist Reifeinformation, keine Autorisierung.
- `eval_coverage` beschreibt vorhandene Abdeckung, keinen bestandenen Lauf.
- Toolverfügbarkeit ist keine Autorisierung.
- Ein Workflow erweitert keine Rechte und ersetzt keine Human Gates.
- Bei Near-Misses den enger passenden Skill bevorzugen oder ohne Skill arbeiten, statt einen breiten Skill zu erzwingen.
- Eine lange Skill-Liste ist kein Qualitätsmerkmal. Der ausgewählte Satz soll begründbar und klein bleiben.

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
- **Keinen Skill** erzwingen, wenn der Auftrag mit allgemeinen Regeln zuverlässig direkt bearbeitet werden kann.

## Vor der Ausführung

Für jeden ausgewählten Skill prüfen:

1. Katalog-ID und Pfad;
2. `maturity` und `eval_coverage`;
3. benötigte `capabilities` und lokale Toolrealität;
4. Frontmatter-`description` einschließlich Trigger/Abgrenzung;
5. lokale Regeln, Daten, Versionen und Autorisierung;
6. relevante Evals nur als Evidence verwenden, wenn sie tatsächlich ausgeführt wurden.

## Auswahl gegenüber dem Nutzer erklären

Die Routingentscheidung soll transparent, aber nicht belastend sein.

- Bei kleinen Aufgaben genügt meist ein kurzer Satz wie: „Dafür nutze ich vor allem X, weil …“.
- Bei größeren Aufgaben kann der ausgewählte Workflow mit den wichtigsten Skills genannt werden.
- Interne Katalogdetails nur erklären, wenn sie für Risiko, Grenzen oder Verständnis relevant sind.
- Erst die Aufgabe lösen, nicht den Nutzer mit Repository-Inventar prüfen.

## Abschluss

Vor Abschluss mindestens Auftragserfüllung, Quellen-/Evidence-Treue, offene Annahmen, nicht ausgeführte Prüfungen und notwendige Gates nennen.

Bei Änderungen am Repository bevorzugt den lokalen Validation Harness verwenden; keine globale Python-Installation voraussetzen:

```powershell
.\Validate-KI-Regeln.ps1 -Quick
```

Je nach Änderungsumfang `-Full` oder `-Release` verwenden. Kann der vorgesehene Prüfstand in der aktuellen Laufzeit nicht ausgeführt werden, `NOT RUN` beziehungsweise `UNVERIFIED` melden statt einen erfolgreichen Lauf abzuleiten. Details: `Local-Validation-Harness.md`.
