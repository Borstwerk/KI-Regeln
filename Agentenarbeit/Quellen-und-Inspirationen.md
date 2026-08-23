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

## Loop Engineering

IBM beschreibt Loop Engineering als die Gestaltung agentischer Workflows, in denen ein Agent Ziel, Aktion, Beobachtung und Anpassung wiederholt, bis ein messbares Ziel oder Abbruchkriterium erreicht ist.

Quelle:

https://www.ibm.com/think/topics/loop-engineering

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