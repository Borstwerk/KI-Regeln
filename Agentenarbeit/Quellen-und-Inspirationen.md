# Quellen und Inspirationen zur Agentenarbeit

Dieser Bereich fasst allgemeine Arbeitsprinzipien zusammen. Die folgenden Quellen dienten als Inspiration und Beobachtungsmaterial. Sie sind keine verbindliche Spezifikation für dieses Repository.

## Context Engineering

Anthropic beschreibt Context Engineering als die gezielte Auswahl und Pflege des für einen Agentenlauf nützlichen Kontextes. Besonders relevant ist die Idee, mit einem möglichst kleinen, signalstarken Kontext zu arbeiten und Kontext über längere Agentenläufe iterativ zu kuratieren.

Quelle:

https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

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