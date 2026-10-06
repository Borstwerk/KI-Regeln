# Skill-Handbuch – Master-Router

Dieses Dokument ist kein zweites Skill-Katalogbuch. Es routet von einem **konkreten Problem oder Auftrag** zum kleinsten ausreichenden Skill-Satz und verweist für Details auf Katalog, Fachhandbücher und lokale Sources of Truth.

Der Nutzer muss dafür weder die richtige Domäne noch einen Skill-Namen kennen.

## Startpfad

```text
Problem / Nutzerauftrag
→ lokale Sources of Truth und verfügbare Evidence
→ Aufgabe fachlich einordnen
→ passende Domäne / vorhandenen Workflow prüfen
→ kleinsten fachlich ausreichenden Skill-Satz wählen
→ Cross-Cutting-Checkpoints nach Bedarf
→ Capabilities / Maturity / Evals prüfen
→ Ausführung
→ Pre-Completion / Pre-Output Checkpoints
→ Verification / Review / Gate
```

Für Menschen ohne Repository-Vorkenntnisse beginnt der Einstieg in `../START-HIER.md`. Für einen frischen Agenten beginnt er in `../AGENTS.md`. Die maschinenlesbare Skill-Wahrheit liegt in `../skill-catalog.yml`; Workflows stehen in `../workflow-index.yml`. Die kleine globale Zweitprüfung für domänenübergreifende Skills steht in `../routing-overlays.yml`.

## Problem-first Routing

Nicht vom Werkzeugnamen ausgehen, sondern von der zu erledigenden Arbeit.

| Beispielhafter Auftrag | Typischer erster Routingraum |
|---|---|
| „Prüfe, ob diese Behauptung stimmt.“ | Recherche |
| „Schreib oder überarbeite diesen Text.“ | Schreiben |
| „Hilf mir, Figuren, Plot oder Welt für eine Geschichte zu entwickeln.“ | Storyentwicklung und Fiktion |
| „Ordne meine Rücklagen, Schulden oder Anlageoptionen ein.“ | Finanzen |
| „Prüfe mein Depot oder bringe es kontrolliert zurück zu meiner Zielallokation.“ | Finanzen |
| „Analysiere dieses Unternehmen fundamental oder ordne die neuesten Quartalszahlen ein.“ | Finanzen + Recherche für aktuelle Evidence |
| „Bewerte dieses Unternehmen mit DCF oder vergleichbaren Unternehmen.“ | Finanzen + Recherche für aktuelle Evidence |
| „Erstelle oder prüfe eine Bildserie.“ | Bildarbeit |
| „Entwickle, kritisiere oder überarbeite ein Logo / Brand Mark.“ | Bildarbeit → `logo-design` |
| „Baue oder prüfe diese Website.“ | Webentwicklung |
| „Finde die Ursache dieses Fehlers.“ | Programmieren / Diagnose, je nach System weitere Fachdomänen |
| „Dokumentiere diese Datenbanktabelle.“ | Dokumentationserstellung + Datenbanken |
| „Mach diese komplexe Erklärung, Entscheidung oder Review auf einen Blick erfassbar.“ | Dokumentationserstellung → `visual-answer` |
| „Kläre, was dieses Feature eigentlich können soll.“ | Requirements und Spezifikations-Engineering |
| „Baue eine langfristig nutzbare Wissensbasis.“ | Wissensmanagement |
| „Welche Provenienz-, Geräte- oder Bearbeitungshinweise stecken in dieser Datei?“ | Sicherheit → `inhaltsprovenienz-review` |
| „Erstelle aus meiner Datei eine Sharing-Kopie ohne GPS- oder unnötige Autor-Metadaten.“ | Sicherheit → `metadaten-hygiene`, bei Bedarf vorher `inhaltsprovenienz-review` |

Die Tabelle ist keine vollständige Routingmatrix. Ein Auftrag kann mehrere Domänen berühren; trotzdem gilt: **so wenig Werkzeuge wie möglich, so viele wie nötig**.

## Cross-Cutting-Checkpoints

Nach dem primären fachlichen Routing wird **nicht** der gesamte Katalog ein zweites Mal durchsucht und auch nicht nur einmal pauschal ein Overlay-Pass ausgeführt.

Stattdessen nennt `../routing-overlays.yml` für wenige domänenübergreifende Kandidaten Checkpoints, an denen ihre **kanonische Skill-Description** gegen den dann tatsächlich vorhandenen Arbeitszustand geprüft wird.

| Checkpoint | Zweck |
|---|---|
| `post-primary` | direkt nach dem vorläufigen Primärrouting; kann einen spezifischeren Owner entdecken oder Darstellung früh planen |
| `pre-execution` | vor Toolnutzung, Änderungen oder iterativer Arbeit; vor allem Verification- und Security-Fragen |
| `pre-completion` | wenn ein Ergebnis weitgehend vorliegt, aber noch kein Completion Claim abgegeben wurde |
| `pre-output` | unmittelbar vor der Darstellung; tatsächliche Informationsdichte kann Presentation-Skills erst jetzt rechtfertigen |

Die vorhandenen `phase`-Werte beschreiben weiterhin die Rolle eines Overlays. `checkpoints` beschreiben nur, **wann** der Kandidat geprüft wird. Beides enthält keine Triggerlogik.

Wichtig:

- `routing-overlays.yml` ist keine zweite Triggerdatenbank;
- Overlay-Eintrag ≠ Aktivierung;
- ein später Trigger darf nicht dadurch verloren gehen, dass er beim Start noch nicht erfüllt war;
- ein Overlay muss nicht immer addiert werden: Ist es der spezifischere Primärowner, kann es einen redundanten generischen Skill ersetzen;
- mehrere aktive Overlays brauchen jeweils einen eigenen notwendigen Job;
- Security-Reviews werden nach Objekt und Job dedupliziert: `skill-security-review` besitzt die Admission eines externen/mächtigen Skill-Bundles; `tool-permission-review` kommt dort nur zusätzlich hinzu, wenn Berechtigungsdesign selbst Gegenstand der Aufgabe ist. Eigenständige MCP-Server, Plugins, Connectors oder Hooks folgen der Baseline aus `../Sicherheit/MCP-und-externe-Tools.md` und werden nicht automatisch als Skill-Bundle behandelt.
- Nach Rückfragen oder neuen Tool-/Dateifunden darf ein bereits geprüfter Kandidat ereignisgesteuert erneut bewertet werden, aber nur wenn der neue Fakt einen Description-relevanten Sachverhalt materiell ändert; kein kompletter Katalogscan.

Details: `../Skill-Engineering/Cross-Cutting-Skill-Discovery.md`.

## Routing-Regeln

- Allgemeine Arbeitsweise zentral, konkrete Wahrheit lokal.
- Der Nutzer muss keine Skill-Namen kennen. Fehlende Skill-Auswahl ist Aufgabe des Routers, nicht automatisch eine Rückfrage an den Nutzer.
- Nicht alle Skills laden. Im Katalog nach `purpose`, `area`, `capabilities` und `related` primär routen und nur die benötigten `SKILL.md`-Dateien öffnen.
- `routing-overlays.yml` an den angegebenen Checkpoints prüfen; die dort gelisteten Skills nur bei passender eigener Skill-Description aktivieren und redundante generische Skills bei spezifischerem Ownership-Signal entfernen.
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