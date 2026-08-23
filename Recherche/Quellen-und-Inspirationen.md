# Quellen und Inspirationen – Recherche

## Zweck

Diese Datei dokumentiert externe Quellen und Systeme, die als Inspiration für die allgemeinen Recherche-Regeln dieses Repositories dienten.

Die genannten Quellen sind **keine normative Wahrheit**. Konzepte werden nur übernommen, wenn sie allgemein wiederverwendbar sind und zum bestehenden Regelwerk passen.

## OpenAI – Deep Research

### Help Center / Produktbeschreibung

Quelle:

`https://help.openai.com/de-de/articles/10500283-tiefgehende-recherche`

Nützliche Konzepte:

- Deep Research als mehrstufiger Prozess statt einzelner Suche;
- Rechercheplan;
- Quellensteuerung;
- iterative Recherche;
- Nachsteuerung während des Prozesses;
- Synthese mit Quellen.

### Deep Research System Card

Quelle:

`https://openai.com/index/deep-research-system-card/`

Nützliche Konzepte:

- Webinhalte können bösartige oder irreführende Instruktionen enthalten;
- Retrieval muss gegen Prompt Injection und unerlaubte Aktionen abgesichert werden;
- Browsing und Toolnutzung benötigen klare Sicherheitsgrenzen.

## Firecrawl – Deep Research Skill

Quelle:

`https://github.com/firecrawl/web-agent/blob/main/agent-core/src/skills/definitions/deep-research/SKILL.md`

Nützliche Konzepte:

- Thema in mehrere Blickwinkel zerlegen;
- unterschiedliche Query-Varianten verwenden;
- gezielte Extraktion relevanter Passagen statt vollständiger Seitendumps;
- mehrere Quellen triangulieren.

Bewusste Abweichung:

Confidence wird hier nicht allein aus der Zahl übereinstimmender Quellen abgeleitet. Quellenabhängigkeit, Claim-Direktheit und Qualität werden zusätzlich berücksichtigt.

## PracticalSwan – Research Skill

Quelle:

`https://github.com/PracticalSwan/agent-skills/blob/main/research/SKILL.md`

Nützliche Konzepte:

- Primärquellen bevorzugen;
- technische Aussagen möglichst bis zu offizieller Dokumentation, Source oder Spezifikation verfolgen;
- belastbare Entscheidungsevidenz statt bloßer Suchtreffer sammeln.

## Nous Research / Hermes – Grounded Citations

Quelle:

`https://github.com/nousresearch/hermes-agent/blob/main/skills/research/grounded-citations/SKILL.md`

Nützliche Konzepte:

- Quellen- beziehungsweise Evidence-Ledger;
- Claims mit konkreten Retrieval-Ergebnissen verbinden;
- Zitations-Coverage prüfen;
- Quellen nicht aus Modellgedächtnis rekonstruieren.

Übernommen wurde das allgemeine Prinzip einer Claim-Evidence-Verknüpfung, nicht die konkrete Hermes-Implementierung.

## Jwynia – Fact Check Skill

Quelle:

`https://github.com/jwynia/agent-skills/blob/main/skills/general/research/verification/fact-check/SKILL.md`

Nützliche Konzepte:

- Fact Checking als separater Pass nach der Synthese;
- Behauptung und Verifikation als unterschiedliche Arbeitsmodi behandeln.

## Stanford STORM

Paper:

`https://arxiv.org/abs/2402.14207`

Nützliche Konzepte:

- unterschiedliche Perspektiven erzeugen unterschiedliche Fragen;
- Research-Breite wird durch Fragevielfalt verbessert;
- Perspektivenerweiterung vor Synthese.

Wichtige Einordnung:

STORM ist ein Research-System und kein allgemeiner Beweis, dass Multi-Agent- oder Multi-Perspektiven-Verfahren für jede Recherche besser sind. Der Ansatz wird selektiv als Inspirationsquelle genutzt.

## LangChain DeepAgents – Web Research

Quelle:

`https://github.com/langchain-ai/deepagents/blob/main/libs/cli/examples/skills/web-research/SKILL.md`

Nützliche Konzepte:

- Rechercheplan;
- nicht überlappende Subthemen;
- strukturierte Research-Artefakte;
- getrennte Research-Threads mit anschließender Synthese.

## Microsoft VS Code Team Kit – Research

Quelle:

`https://github.com/microsoft/vscode-team-kit/blob/main/research/skills/research/SKILL.md`

Nützliche Konzepte:

- mehrere Research-Threads bei unabhängigen Teilfragen;
- Quality Gates;
- erneute gezielte Recherche bei unzureichender Abdeckung.

Daraus wurde insbesondere der allgemeine Gedanke eines **Coverage Loops** übernommen.

## drader / researcher_agent – Research Skill

Quelle:

`https://github.com/drader/researcher_agent/blob/main/skills/research/SKILL.md`

Nützliche Konzepte:

- unterschiedliche Research-Modi;
- Suchtreffer als Leads statt Evidenz;
- widersprüchliche Quellen sichtbar halten;
- Source Grounding.

## Wissenschaftsspezifische Skills

Beispiel:

`https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/exa-search/SKILL.md`

Diese Sammlungen zeigen, dass wissenschaftliche Recherche zusätzliche Fachlogik benötigt, etwa:

- Paper-Suche;
- DOI und Metadaten;
- Peer Review vs. Preprint;
- Methodenqualität;
- Citation Chasing;
- systematische Reviews und Meta-Analysen.

Diese Themen werden bewusst nicht vollständig in den allgemeinen Recherchekern gezogen. Ein späterer spezialisierter Wissenschaftsbereich ist möglich.

## Toolgebundene Rechercheanbieter

Ökosysteme wie Exa, Firecrawl, Tavily, Yutori oder Browser-Agenten sind nützliche Implementierungen, aber keine zentrale Methodik dieses Repositories.

Prinzip:

```text
Recherchemethodik
→ Tooladapter
```

und nicht:

```text
Tool-API
→ allgemeine Recherchewahrheit
```

## Übernahmekriterien

Ein externes Konzept wird bevorzugt übernommen, wenn es:

1. toolunabhängig generalisierbar ist;
2. Quellen- oder Ergebnisqualität verbessert;
3. Fehler oder Halluzinationen reduziert;
4. Review und Nachvollziehbarkeit verbessert;
5. nicht bloß mehr Suchvolumen produziert;
6. mit Context Engineering, Evidence und Human Gates kompatibel ist.

## Leitgedanke

> Research-Techniken werden übernommen, wenn sie bessere Evidenz und bessere Entscheidungen ermöglichen – nicht weil sie nach „Deep Research“ klingen.
