# Quellen und Inspirationen zur Agentenarbeit

Dieser Bereich fasst allgemeine Arbeitsprinzipien zusammen. Die folgenden Quellen dienten als Inspiration und Beobachtungsmaterial. Sie sind keine verbindliche Spezifikation für dieses Repository.

## Context Engineering

Anthropic beschreibt Context Engineering als die gezielte Auswahl und Pflege des für einen Agentenlauf nützlichen Kontextes. Besonders relevant ist die Idee, mit einem möglichst kleinen, signalstarken Kontext zu arbeiten und Kontext über längere Agentenläufe iterativ zu kuratieren.

Quelle:

https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

Daraus werden insbesondere übernommen:

- Context als endliches Attention-/Token-Budget;
- Just-in-time-Retrieval statt vorsorglichem Vollladen;
- Compaction, strukturierte Notizen und Subagenten als unterschiedliche Long-Horizon-Werkzeuge;
- zuerst hohe Fidelity/Recall bei Compaction, danach unnötigen Inhalt reduzieren;
- token-effiziente Tools und begrenzte Toolräume.

## Context Rot und Long-Context-Forschung

Die Arbeit „Lost in the Middle“ und weitere Long-Context-Forschung zeigen, dass bloßes Vorhandensein einer Information im Kontext nicht garantiert, dass sie zuverlässig genutzt wird. Neuere Arbeiten untersuchen zusätzlich Context Degradation und die Grenzen pauschaler Long-Context-/RAG-Methoden.

Quellen:

https://aclanthology.org/2024.tacl-1.9/

https://aclanthology.org/2026.findings-acl.2097/

Die praktische Regel lautet nicht, lange Kontexte generell zu vermeiden. Übernommen wird das allgemeinere Prinzip, Kontextqualität und Task Outcome statt bloßer Fenstergröße zu optimieren.

## Context Compaction

Anthropic beschreibt Compaction als zentrale Technik für Long-Horizon-Agenten und empfiehlt, zunächst relevante Information mit hoher Recall-Fidelity zu erhalten. Eine aktuelle empirische Arbeit untersucht Compaction zusätzlich über gepaarte geschlossene Weiterläufe vom selben Ausgangszustand und bewertet damit die tatsächliche Ausführungsstabilität nach der Verdichtung.

Quellen:

https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

https://arxiv.org/abs/2608.06503

Für dieses Repository folgt daraus:

> Compaction wird möglichst an Fortsetzungsfähigkeit und Outcome geprüft, nicht nur an Zusammenfassungslänge oder Kompressionsrate.

Weitere aktuelle Forschung zeigt für bestimmte Tool-Workflows, dass selektives Pruning plus Zusammenfassung gleichzeitig Tokenverbrauch senken und Taskerfolg verbessern kann. Das wird als empirischer Hinweis, nicht als universelle Rezeptur behandelt.

Quelle:

https://arxiv.org/abs/2606.10209

## Long-Horizon Handoffs

Anthropic beschreibt für lang laufende Agenten explizite Artefakte, die zwischen Sessions Arbeitsfortschritt und Zustand erhalten. OpenClaws öffentlicher `handoff`-Skill formuliert zusätzlich die praktische Idee eines standalone Prompts für eine frische Arbeitsinstanz.

Quellen:

https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents

https://github.com/openclaw/agent-skills/blob/main/skills/handoff/SKILL.md

Übernommen wird das allgemeine Prinzip einer eigenständig nutzbaren Übergabe. Clipboard-, Plattform- und Repository-Sonderlogik des OpenClaw-Skills wird nicht zentral übernommen.

## Context Audit und Token-Footprint

Der öffentliche `context-doctor`-Skill macht Kontextverbrauch als Inventar sichtbar: Workspace-Dateien, Skill-Metadaten, Toolbeschreibungen und weitere Bootstrap-Anteile. Er diente als praktischer Impuls für einen eigenen `context-audit`-Skill.

Quelle:

https://github.com/jzOcb/context-doctor

Nicht übernommen werden dessen OpenClaw-spezifische Schwellenwerte oder pauschale Zeichen-zu-Token-Schätzungen als allgemeine Wahrheit. Dieses Repository behandelt solche Werte nur als lokale beziehungsweise grobe Approximation.

## Tool Outputs und Context Offloading

Anthropic beschreibt Programmatic Tool Calling beziehungsweise token-effiziente Toolverarbeitung, bei der große Zwischenresultate außerhalb des Modellkontexts gefiltert oder aggregiert werden und nur das relevante Ergebnis zurückkehrt.

Quelle:

https://www.anthropic.com/engineering/advanced-tool-use

OpenAI beschreibt ebenfalls Context-Bloat durch Tools, Skills, Plugins und Verlauf und nutzt unter anderem deferred discovery sowie Begrenzung großer Tooloutputs.

Quelle:

https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency/

Daraus wird die allgemeine Regel abgeleitet, deterministische Verarbeitung nach Möglichkeit außerhalb des LLM-Kontexts zu erledigen, ohne Evidence oder Nachvollziehbarkeit zu verlieren.

## Prompt Caching

OpenAI beschreibt für aktuelle Modelle Präfix-Caching und die Bedeutung stabiler wiederkehrender Kontextbestandteile. Konkrete Cache-Dauer, Preise, Schlüssel oder Breakpoints sind provider- und versionsabhängig.

Quellen:

https://openai.com/de-DE/index/builders-guide-to-gpt-5-6/

https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency/

Zentral übernommen wird nur:

> Wenn eine Runtime Präfix-Caching unterstützt, stabile Kontextbestandteile möglichst stabil strukturieren – ohne Aktualität oder fachliche Korrektheit für eine höhere Hit Rate zu opfern.

## Native Compaction

OpenAI beschreibt native Compaction in der Responses API für lange Agentenläufe. Sie erzeugt eine kompaktere Repräsentation früheren Zustands, damit Arbeit über das eigentliche Kontextfenster hinaus fortgesetzt werden kann.

Quelle:

https://openai.com/index/equip-responses-api-computer-environment/

Native Compaction wird als mögliche Runtime-Capability behandelt, nicht als Ersatz für Fidelity-/Outcome-Prüfung.

## Short-Term und Long-Term Memory

LangChain unterscheidet thread-/sessionbezogene Short-Term Memory von Long-Term Memory, das über verschiedene Sessions und Threads persistiert.

Quellen:

https://docs.langchain.com/oss/python/concepts/memory

https://docs.langchain.com/oss/python/langchain/long-term-memory

Für dieses Repository wird daraus eine eigene Grenze abgeleitet:

```text
Active Context / Working State
→ Agentenarbeit

Persistent Knowledge
→ Wissensmanagement
```

Konkrete LangGraph-/Store-Implementierungen bleiben tool- beziehungsweise projektspezifisch.

## Multi-Agent als Context-Isolation

Anthropic beschreibt Subagenten als getrennte Kontextfenster, die tiefe Teilrecherche durchführen und verdichtete Ergebnisse an einen Orchestrator zurückgeben. Gleichzeitig zeigen die veröffentlichten Erfahrungen einen deutlich höheren Gesamttokenverbrauch und Koordinationsaufwand.

Quelle:

https://www.anthropic.com/engineering/multi-agent-research-system

Daraus folgt:

> Multi-Agent kann Kontext isolieren und Parallelität ermöglichen, ist aber kein universeller Token-Sparmechanismus.

## Context- und GenAI-Metriken

OpenTelemetry entwickelt providerübergreifende GenAI Semantic Conventions für unter anderem Input-/Output-Token, Cache-Read/-Write-Tokens, Modelloperationen und Latenz.

Quellen:

https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/

https://opentelemetry.io/blog/2026/genai-observability/

Diese Quellen stützen die providerneutrale Benennung von Usage-Signalen. Die Semantic Conventions befinden sich teilweise weiterhin in Entwicklung und werden deshalb als lebender Upstream behandelt.

## Harness Engineering

OpenAI beschreibt Harness Engineering als den Aufbau einer agentengerechten Arbeitsumgebung aus Repository-Wissen, Tools, Tests, Observability, Review-Schleifen und technisch durchsetzbaren Regeln.

Quelle:

https://openai.com/index/harness-engineering/

## Isolation, Sandbox und Berechtigungen

OpenAI beschreibt für Codex die Kombination aus Sandbox- und Approval-Policies, um Schreibzugriffe, Netzwerkzugriffe und risikoreiche Aktionen technisch zu begrenzen.

Quelle:

https://openai.com/index/running-codex-safely/

## Task Graphs und isolierte parallele Agenten

OpenAI beschreibt mit Symphony eine Orchestrierung, in der Aufgaben in abhängige Teilaufgaben zerlegt und unabhängige Arbeit in isolierten Workspaces parallel ausgeführt werden kann.

Quelle:

https://openai.com/index/open-source-codex-orchestration-symphony/

Die hier abgeleitete Regel lautet nicht, jeden Agentenschritt als starre State Machine vorzuschreiben. Der Graph soll Abhängigkeiten, Objectives, Grenzen und prüfbare Übergänge ausdrücken.

## Loop Engineering

IBM beschreibt Loop Engineering als die Gestaltung agentischer Workflows, in denen ein Agent Ziel, Aktion, Beobachtung und Anpassung wiederholt, bis ein messbares Ziel oder Abbruchkriterium erreicht ist.

Quelle:

https://www.ibm.com/think/topics/loop-engineering

## Why Loop, How Loop und menschliche Steuerung

Kief Morris beschreibt bei Martin Fowler die Trennung zwischen der Frage, **was und warum** erreicht werden soll, und der autonomen technischen Ausführung innerhalb dieses Rahmens. Daraus lässt sich für dieses Repository die Trennung zwischen äußerem Why Loop und innerem How Loop ableiten.

Quelle:

https://www.martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html

## Delegation Contracts und Evidence Bundles

Eine 2026 veröffentlichte ArXiv-Arbeit untersucht explizite Delegation Contracts und Evidence Bundles bei Agentenarbeit. Für dieses Repository ist daran besonders die Idee relevant, Agentenergebnisse leichter prüfbar und übergabefähig zu machen.

Quelle:

https://arxiv.org/abs/2606.17099

Die Studie wird hier nicht als Beweis verwendet, dass formale Contracts jede Agentenlösung automatisch besser machen. Übernommen wird das allgemeinere Prinzip der überprüfbaren Delegation.

## Agent Evals

Anthropic beschreibt den Aufbau von Evals für KI-Agenten und betont unter anderem klar spezifizierte Aufgaben, reproduzierbare Umgebungen und deterministische Grader, wo diese möglich sind.

Quelle:

https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

Für dieses Repository wird daraus insbesondere die Trennung zwischen Produktqualität und Agentenprozessqualität übernommen.

## Observability und Traceability

OpenAI beschreibt Observability als Bestandteil agentischer Harnesses. GitHub hat zusätzlich die Rückverfolgbarkeit von Coding-Agent-Commits zu den zugehörigen Session-Logs beschrieben.

Quellen:

https://openai.com/index/harness-engineering/

https://github.blog/changelog/2026-03-20-trace-any-copilot-coding-agent-commit-to-its-session-logs/

Die konkrete Telemetrie oder Session-Speicherung ist projektspezifisch. Allgemein übernommen wird nur das Prinzip, relevante Agentenarbeit nachvollziehbar mit Auftrag, Evidence, Artefakt und Freigabe verbinden zu können.

## Entropie, Drift und Repository-Pflege

OpenAI beschreibt im Harness-Engineering-Bericht, dass Agenten vorhandene inkonsistente Muster replizieren können und dass wiederkehrende Qualitätsregeln sowie gezielte Bereinigung helfen, langfristige Drift zu begrenzen.

Quelle:

https://openai.com/index/harness-engineering/

Daraus wird kein Auftrag zur automatischen Großbereinigung abgeleitet. Dieses Repository bevorzugt kleine bestätigte Repair-Slices mit normalem Review- und Freigabeprozess.

## Vibe Architecting

Eine ArXiv-Arbeit von 2026 untersucht, wie Coding Agents aus lokal formulierten Prompts unbeabsichtigt Architekturentscheidungen ableiten können. Für dieses Repository ist daran das allgemeine Risiko relevant, dass eine technisch funktionierende Implementierung stillschweigend neue Architektur erzeugt.

Quelle:

https://arxiv.org/abs/2604.04990

Die praktische Regel lautet deshalb: Neue Frameworks, Persistenzformen, zentrale Layer, öffentliche Verträge oder Sicherheitsmodelle benötigen eine bewusste Architekturentscheidung, wenn sie nicht bereits vom freigegebenen Plan gedeckt sind.

## Skills für Software-Agenten

Mehrere Software-Skills dieses Repositories wurden inhaltlich durch Matt Pococks öffentliches Skill-Repository und die dazugehörige AI-Hero-Skill-Sammlung angeregt und anschließend an die hier verwendeten allgemeinen Regeln angepasst.

Quellen:

https://github.com/mattpocock/skills

https://www.aihero.dev/skills

Lizenz- und Attributionshinweise zu übernommenen beziehungsweise adaptierten Skill-Ideen stehen zusätzlich in `../THIRD-PARTY-NOTICES.md`.

## Einordnung

Neue Begriffe oder Frameworks werden nicht allein deshalb übernommen, weil sie aktuell verbreitet sind.

Für dieses Repository zählt, ob ein Ansatz:

- wiederverwendbar ist;
- konkrete Agentenfehler reduziert;
- überprüfbare Qualität verbessert;
- sich mit klaren Scope- und Freigaberegeln verbinden lässt;
- nicht nur einen neuen Namen für bereits vorhandene Praxis liefert.

> Konzepte werden übernommen, wenn sie Arbeit besser machen – nicht weil sie ein gutes Buzzword ergeben.