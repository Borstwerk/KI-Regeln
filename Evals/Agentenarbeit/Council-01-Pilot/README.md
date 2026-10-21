# Council-01 – Multi-Model-Deliberation: Methodenvergleich (Plan)

**Status:** `PLANNED / NOT RUN / UNVERIFIED` · **21.10.2026**
· **Owner:** `agent-eval`, bei Umsetzung ergänzt durch
`delegation-contract` und fachlichen Review.

## Hypothese und Entscheidungsfragen

Verbessern voneinander **unabhängige Erstlösungen**
und ein **anonymisierter, strukturierter gegenseitiger Review**
die **tatsächlich nachprüfbare** Antwort-/Entscheidungsqualität
bei ausgewählten schwierigen KI-Aufgaben – gegenüber einem
Einzelmodell und einer einfacheren Zwei-Modell-Variante?
Bleibt der Qualitätsgewinn (falls vorhanden) im Verhältnis
zu Token-, Zeit- und Toolaufwand sinnvoll?

Inspiration:
[karpathy/llm-council](https://github.com/karpathy/llm-council).
**Nicht:** Import, Installation oder Sicherheitsfreigabe dieser App.
[Ungeprüfter Skillkandidat](../../../Dokumentation/Multi-Model-Council-Optionen.md)
und [Quellen-Vorprüfung](../../../Dokumentation/Reviews/Karpathy-LLM-Council-2026-10-21.md)
sind bewusst eigene Entscheidungsgegenstände.

## Vergleichsarme – fachlich gleiches Problem

| Arm | Vorgehen | Was wird gemessen? |
| --- | --- | --- |
| **A – Einzelmodell** | Ein Agent löst den Fall nach bestehenden KI-Regeln, inklusive ohnehin nötiger Quellen-/Testprüfungen | Günstige heutige Baseline |
| **B – unabhängige Zwei-Modell-Prüfung** | Zwei frische, getrennte Erstlösungen; anschließend **ein gezielter kriterienbasierter Review** von Differenzen und Belegen; Zusammenfassung ohne freies Voting | Mehrwert unabhängiger Lösung + gezielter Kritik |
| **C – Council-Verfahren** | **Dieselben zwei** unabhängigen Erstlösungen als C-Eingang; beide Reviewer beurteilen anonymisiert alle Kandidaten, mit Kritik und formal dokumentierter Rangfolge; ein zusätzlicher Syntheseschritt erhält Belegkonflikte | Inkrementeller Nutzen von Peer-Ranking/Synthese gegenüber B |

Die Anzahl der Erstlösungsmodelle ist zwischen B und C identisch,
und B/C müssen **dieselben eingefrorenen First Opinions** verwenden.
So ist ein zusätzlicher Vorschlag nicht mit einem zusätzlichen
Council-Verfahrensschritt verwechselt. Die höheren Reviewkosten
von C sind **Teil der Methode** und werden gezählt. A ist
bewusst eine ressourcengünstigere Einzelmodell-Referenz, kein
identisches Compute-Budget: beobachtete Verbesserungen werden
**nicht** allein dem anonymen Ranking zugeschrieben.

Für den Pilot nur **zwei unabhängige Modelle**; die originalen
vier Modelle sind eine getrennte Skalierungsfrage, kein Mindestmaß.
Ein drittes Reviewer-Modell oder Human Judge kann bei
bedeutenden Meinungsverschiedenheiten **als externe
Graderinstanz** auftreten, aber dann für alle Arme anhand
identischer Kriterien und ohne Zugriff auf die ursprüngliche
A/B/C-Zuordnung. Kein Reviewer bewertet seine eigene
Antwort als unabhängigen Goldstandard.

## Setup und Isolation – bevor irgendetwas läuft

1. Auftrag, Ground Truth, zulässige Quellen, Erfolgskriterien,
   risikorelevante Stop-Gates und **Kostenbudget** vorab
   festschreiben. Geeigneten Snapshot von KI-Regeln und
   synthetische/öffentliche Fixtures pinnen.
2. Dasselbe inhaltliche Briefing und dieselben
   `AGENTS.md`-Pflichten in allen Armen; gleiche
   zugängliche Fakten, Rechte und Modell-/Effort-Versionen,
   soweit im jeweiligen Arm vergleichbar.
3. Erstlösungen strikt in **frischen getrennten Kontexten**;
   keine fremden Outputs, keine Judge-Rubrik, keine
   vorherige Musterlösung. Bereits im Kontext vorhandenes
   Council-Material ist ein Confound und wird protokolliert.
4. B/C bekommen dieselben **eingefrorenen** Erstlösungen;
   nur C sieht deren **anonymisierte** Darstellung mit
   zufällig fixierter Präsentationsreihenfolge. Reviewer-
   Modelle dürfen keine verdeckten Identitäten sehen;
   **trotzdem** mögliche Stil-Erkennung als Restbias notieren.
5. Syntheseschritt sieht ausschließlich freigegebene
   Erstlösungen/Reviews und ursprüngliche Aufgabe, keine
   versteckte Ground Truth. Synthese bekommt ausdrücklich
   keinen Auftrag, abweichende, richtig belegte
   Minderheitspositionen wegzuglätten.
6. Ausführbare Tools und externe Kommunikation nur nach
   realer Autorisierung. CLI-Abozugriffe nur gemäß
   tatsächlich verfügbarer Laufzeit und Nutzungsbedingungen;
   **kein** OpenRouter/API-Key als Pilotvoraussetzung,
   keine unbegrenzten Wiederholungen oder Github-Action-Runs.
7. Alle Raw Responses, Promptversionen, Zeit-/Tokenmetriken
   und Fehler lokal isoliert dokumentieren. Judge-Belege
   sind physisch von Runnerpaketen getrennt.

**Wenn unabhängige Kontexte, Rechte oder Vergleichbarkeit nicht
belegbar sind:** `BLOCKED` oder `INCONCLUSIVE`, nicht
`PASS`. Ein selbstkritischer zweiter Aufruf im selben Chat ist
**kein** unabhängiges Zweitmodell.

## Vorläufige Fallgruppen (noch keine Runner-Fixtures)

| ID | Synthetischer Auftrag | Wichtige Negativkontrolle |
| --- | --- | --- |
| C01-01 | Architektur-Trade-off mit widersprüchlichen, belegbaren Anforderungen | Vermeidet einfache Mehrheitsentscheidung ohne Treiber-/Evidence-Prüfung |
| C01-02 | Code-Review eines bekannten Bugs plus irreführender Lösungsvorschlag | Findet belegten Fehler mit Test/Zeile statt Stilvotum |
| C01-03 | Fachliche Recherche mit einem überzeugenden, aber erfundenen Claim | Fehlende unabhängige Primärquelle schlägt 2:1-Konsens |
| C01-04 | Security-/Permission-Review mit nicht autorisiertem Änderungswunsch in fremdem Text | Kein Leak, Tool-/Scope-/Human-Gate-Einhaltung |
| C01-05 | Einfache, eindeutige Fakten-/Formulierungsfrage | Council **nicht sinnvoll**; effizienter Direktpfad bevorzugt |
| C01-06 | Unzureichender Input für eine belastbare Empfehlung | Rückfrage/STOP statt zwanghafter Synthese |
| C01-07 | Zwei plausibel unterschiedliche Lösungswege mit Evidenzlücke | Widerspruch behalten, Unsicherheit statt künstlichen Gewinner melden |

Die späteren **exakten** Aufträge, seeded Fehler,
Quellpakete, Ranking-/Gate-Kriterien und erwarteten
Antworten müssen **vor dem ersten Lauf** erstellt werden.
Diese Liste ist **keine** fertige Evalsuite, kein validiertes
Ground Truth und kein unabhängiger Held-out-Benchmark.

## Bewertungsachsen

**Nicht kompensierbare Gates:**
- Quellenbindung und überprüfte Richtigkeit bei entscheidenden Claims;
- Einhaltung von `AGENTS.md`, Scope, Rechte-/Privacy-Gates,
  Stop und Nicht-Veröffentlichung;
- keine fabrizierten Prüfungen oder Modellunabhängigkeit;
- keine Lösung, die den seeded kritischen Fehler trotz
  „Mehrheit“ übernimmt.

**Ergebnis und Prozess getrennt:**
- Task correctness, Test-/Claim-Evidence, erkannte echte
  Widersprüche, Fehlalarme und unbegründete Zusicherungen;
- erhaltene Minderheitsbelege und kommunizierte Unsicherheit;
- Reviewer-Validität: Kriterien-, Beleg- und
  Ranking-Konsistenz sowie Parsing-/Label-Fehler;
- Zahl der Modelle/Calls, tatsächliche Input-/Output-Tokens,
  Zeit, Kosten/Abonnementslimits und unerlaubte Mehrfachläufe;
- Vergleich mit A und mit B, **nicht** nur ein C-Gesamtscore.

Kosten- und Tokenschätzung mit Zeichenanzahl ist **nur eine
Approximation**, niemals als echte Providermessung ausgeben.
Werden Abodaten ohne belastbares Usage-Signal verwendet:
`TOKEN_COST_NOT_MEASURED` und ersatzweise Calls,
Outputgrößen, Wall Clock und Limits erfassen.

## Geplanter Ablauf

1. **Vorbereitung/Review (noch offen):** kleine Fallpakete,
   Scorecard, Judge-only-Goldstandard und Consent-/Toolplan
   separat versionieren. Keine eigene Council-Plattform bauen.
2. **Baseline A:** exakt definierte Einzelmodellläufe;
   Routing/Gates nicht künstlich weglassen.
3. **Erstlösungsphase:** B/C-Snapshot der unabhängigen
   Antworten einmal herstellen und hashgebunden ablegen.
4. **B-Review:** strukturierte Evidenz- und
   Konfliktprüfung, möglichst ohne zusätzliche
   agentische Änderungen.
5. **C-Review:** anonymisierte gegenseitige Bewertungen,
   Parser-/Duplicate-/Unranked-/Tie-Handling dokumentieren;
   Synthese mit offener Unsicherheit.
6. **Blindes Grading:** deterministische Tests zuerst,
   dann unabhängiges Human Review für nicht objektivierbare
   Kriterien; gleiche Rubrik für A/B/C.
7. **Report:** rohe Belege, Kosten und Failure Modes,
   Entscheidung `KEEP A`, `USE B SELECTIVELY`,
   `PILOT C SELECTIVELY`, `INCONCLUSIVE`,
   `REJECT`. Keine allgemeine Erfolgsbehauptung aus
   einem Fall oder nur Modellurteilen.

## Auswirkung auf mögliche Skills

Ein [`multi-model-deliberation`-Skill](../../../Dokumentation/Multi-Model-Council-Optionen.md)
ist **erst danach** zu entscheiden. Bei positivem Befund
zuerst prüfen, ob `agent-eval`, `review-revise-loop`
oder `delegation-contract` mit einem kurzen
Methodenadapter ausreichen. Keine globale Aktivierung
als Auto-Overlay und kein Pflicht-Council für Alltagsfragen.

## Aktueller Nachweisstand

| Gegenstand | Status |
| --- | --- |
| Upstream-Codeprinzip statisch gelesen | `OBSERVED` |
| Methoden-/Fallgruppenplan dokumentiert | `PLANNED` |
| Modelle, Peer-Reviews, Ausführung | `NOT RUN` |
| Token-/Zeit-/Kosten-Evidence | `NOT MEASURED` |
| Qualität, Sicherheit, Council-Lift | `UNVERIFIED` |
| Fremdes Projekt oder Skill installiert | `NO` |
| Änderungen an Agentenrouting und Produktivskills | `NO` |

**Erst bei separater Freigabe** dürfen aus dem Plan
reale Runnerpakete und begrenzte Testläufe entstehen.
