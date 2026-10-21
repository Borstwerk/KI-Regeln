# Ideenkarte: Multi-Model Council und möglicher KI-Regeln-Skill

**Status:** `UNVERIFIED / PLANNED / NOT ADMITTED` · **Datum:** 21.10.2026

**Ausgangspunkt:** [karpathy/llm-council](https://github.com/karpathy/llm-council)
ist ein **externes Anwendungsprojekt**, **kein fertiger Agenten-Skill für
KI-Regeln**. Sein Prinzip – unabhängige Antworten, anonymer gegenseitiger
Review, abschließende Synthese – dient uns als **methodische Inspiration**,
nicht als installierbare Abhängigkeit. Der Projektstand und Risiken sind in
[der Quellen-Vorprüfung](Reviews/Karpathy-LLM-Council-2026-10-21.md) festgehalten.

Die [Council-01-Methodenplanung](../Evals/Agentenarbeit/Council-01-Pilot/README.md)
prüft zunächst, ob mehrmodelliger Review tatsächlich mehr leistet
als unsere bestehenden Methoden. Ein positiver Effekt ist **nicht belegt**.

## Option S – Eigener Skill-Kandidat `multi-model-deliberation`

**Nur vorgemerkt, nicht implementiert oder registriert.** Kein
`SKILL.md`, kein `skill-catalog.yml`-Eintrag, kein Routing-Overlay,
keine neue generelle Ausführungs- oder API-Capability.

### Mögliche eigenständige Verantwortung

Für eine ausdrücklich gewünschte, **schwierige oder strittige** Frage einen
**kontrollierten, nachvollziehbaren Multi-Model-Review** veranlassen:

1. Gemeinsame Frage, Sources of Truth, Rechte, Kriterien und Stop-Gates fixieren.
2. Unabhängige Erstlösungen in getrennten Kontexten erstellen; kein
   vorzeitiger Zugriff auf die Lösung anderer Reviewer.
3. Antworten vor dem Peer-Review wo praktikabel anonymisieren und in
   zufälliger Reihenfolge präsentieren.
4. **Claims und Belege** prüfen; Ranking und Zustimmung sind Signale,
   **keine Wahrheitsbeweise**. Uneinigkeit samt möglicher
   Mehrheits-/Common-Mode-Fehler sichtbar erhalten.
5. Eine Synthese liefern, die Konsens, Konflikt, Unsicherheit,
   überprüfte Gegenbelege und erforderliche Human-Gates trennt.

Ein späterer Skill wäre **toolneutral**: verschiedene tatsächlich
verfügbare KI-Modelle, zulässige getrennte CLI-Abos oder manuelle
Übergabe – **kein** universell behaupteter API-Zugriff. Eine
Runtime-/Provider-Integration wäre ein **separater Adapter**.

### Mögliche Trigger

- „Lass Claude und Codex unabhängig entscheiden und ihre Ansätze
  kriterienbasiert gegeneinander prüfen.“
- „Ich möchte bei dieser schwierigen Architekturentscheidung bewusst
  zwei gegensätzliche KI-Perspektiven und eine neutrale Synthese.“
- „Führe für diese risikoreiche, unbelegte Empfehlung einen
  mehrmodelligen Review mit Quellenkontrolle durch.“

### Near-Misses / kein Trigger

- Kurze Faktenfrage, triviale Formulierung oder normales Coding.
- „Prüfe den bestehenden PR“ → zuerst fachlicher `code-review`.
- „Entwirf Evalfälle für ein Agentensystem“ → `agent-eval`.
- „Vergleiche Architekturvarianten“ → zunächst `architecture-tradeoff-analysis`;
  ein Council ist höchstens ein **separat begründetes Reviewverfahren**.
- „Recherchiere Quellen“ → `deep-research`/`claim-verification`;
  zusätzliche LLM-Stimmen ersetzen keine unabhängigen Quellen.
- Fehlende zusätzliche Modelle, ungeklärte Datengrenzen oder
  keine ausdrückliche Erlaubnis für externe Übertragung:
  **kein vorgetäuschter Multi-Model-Lauf**, sondern `NOT RUN`
  und gegebenenfalls manueller oder Single-Model-Fallback.

### Potenzieller Outputvertrag

`COUNCIL-REPORT` mit Task/Snapshot/Tools/Modellen,
anonymisierten Erstlösungen, getrennten Bewertungen, belegten
Konflikten, finalem begrenztem Vorschlag, Token-/Zeit-/Kostenaufwand,
fehlenden Prüfschritten und ausdrücklichen `NOT_RUN`/
`UNVERIFIED`-Feldern. Identität des Reviewers und Anonymisierung
dokumentieren; ein anonymer Anzeigename beweist keine echte
Unabhängigkeit.

### Vor einem möglichen Skill-Bau prüfen

- **Owner-Duplikat:** `agent-eval` besitzt Methoden-/Evals,
  `delegation-contract` besitzt Rechte/Gates,
  `review-revise-loop` besitzt Review und Revision,
  Fachreviews beurteilen das jeweilige Artefakt,
  `claim-verification` prüft Fakten, `context-engineering`
  minimiert Kontext.
- **Mehrwert:** Council-01 muss eine eigene wiederkehrende
  Arbeitsdisziplin nachweisen, nicht nur mehrere vorhandene
  Skills nacheinander erneut beschreiben.
- **Aktivierung:** Nur bei explizitem Bedarf und verfügbarer,
  genehmigter Capability, **nie als globale Zweitmeinung**.
- **Kosten-/Privacy-Gate:** zusätzliche Modellaufrufe sind
  zunächst Mehrkosten; keine Prompt-/Repo-/Kundendaten ohne
  passende Autorisierung an fremde Provider.
- **Lizenz/Trust:** Keine Code-/Prompttexte aus Upstream
  importieren, bevor Lizenz- und Rechteumfang geklärt sind.

**Aufnahmeentscheidung erst nach Council-01:** eigener Skill,
kleine Ergänzung des Review-Workflows, dokumentierte Methode ohne
Skill oder `REJECT`. Kein vorgezogener Architekturentscheid.

## Option P – Externes LLM Council als Projekt/Referenz

Das [originale Projekt](https://github.com/karpathy/llm-council)
hat Python/FastAPI, ein lokales React-Frontend und sendet
Modellprompts über OpenRouter an externe Anbieter.

**In der Planung behalten:** Anonymisierte Peer-Reviews,
getrennte Originalantworten, Transparenz von Rankings und Synthese.

**Nicht unbesehen übernehmen:** Externe API-Aufrufe,
festcodierte Modellkonfiguration, Ranking per Freitextparser,
öffentliche HTTP-Server-Konfiguration, API-Schlüssel und
lokales Speichern von Gesprächen. Die Codebasis ist kein
geprüfter Sicherheits- oder Qualitätsstandard; Lizenzstatus
nicht aus GitHub-Stars oder einem README ableiten.

Bei Council-01 ist **kein** laufender Council-Service erforderlich.
Kein `pip install`, `uv sync`, `npm install`,
`OPENROUTER_API_KEY` oder fremder Agenten-Skill-Aufruf.

## Schnittstellen, Prioritäten und Entscheidung

- [Council-01](../Evals/Agentenarbeit/Council-01-Pilot/README.md):
  A Einzelmodell, B zwei unabhängig + gezielter Gegenreview,
  C vollständiger Council. Keine Ergebnisbehauptung vor Modelltests.
- [Agent Eval](../Agentenarbeit/Skills/agent-eval/SKILL.md):
  Qualität **und** Prozess, Negative, Baseline, blindes Review.
- [Delegation Contract](../Agentenarbeit/Skills/delegation-contract/SKILL.md):
  identischer Scope, Capabilities und menschliche Freigaben.
- [Review-Revise Loop](../Workflows/Review-Revise-Loop.md):
  Review allein autorisiert keine Revision.
- [Claim Verification](../Recherche/Skills/claim-verification/SKILL.md):
  Quellenbelege wichtiger als Stimmenzahl.

**Keine Live-Council-Funktion, keine Kosten- oder Qualitätsgarantie,
kein Skill in Produktion.** Idee und Bedingungen sind hier
dauerhaft auffindbar.
