# KI-Regeln

> **Start with a real problem. Find the smallest useful way for AI to work on it.**

**Language:** English · [Deutsch / Einstieg auf Deutsch](START-HIER.md)

KI-Regeln ("AI Rules") is an **open-source, provider-agnostic toolkit** of reusable rules, agent skills, workflows and evaluation methods for working with generative AI. It is designed for people who have a task to solve—not for people who already know which skill to invoke.

Rather than offering one giant prompt, the repository helps an AI assistant **discover and combine relevant methods**, work within the real project's constraints, and make verification and human decisions visible.

## Choose your starting point

| I want to… | Start here |
| --- | --- |
| Use AI for a real task, without learning the internal architecture | **[Start here — English](START-HERE.md)** · [Deutsch](START-HIER.md) |
| See how the toolkit is used in practice | [Real-world examples (German)](PRAXISBEISPIELE.md) |
| Understand its scope, routing and limitations | [Usage guide (German)](Dokumentation/Nutzung-des-Repositories.md) |
| Integrate it into an AI agent's work | **[AGENTS.md — canonical agent bootstrap (German)](AGENTS.md)** |
| Discover available skills or workflows | [Skill catalog](skill-catalog.yml) · [Workflow index](workflow-index.yml) |
| Contribute or review the project | [Contributing (German)](CONTRIBUTING.md) · [Security policy](SECURITY.md) |

**Important:** These files do not automatically install or enforce anything in ChatGPT, Codex or another AI tool. The assistant needs access to the relevant repository files and an appropriate runtime; actual execution, permissions and evidence depend on the user's environment.

## What you can do with KI-Regeln

Describe the problem in your own words. Typical areas include research, software development, testing, documentation, creative writing, image work, financial reasoning, data and infrastructure workflows. See the [domain overview (German)](Dokumentation/Skill-Handbuch.md) for the maintained routing guide.

```text
Your goal and project context
  → identify the local source of truth
  → discover the smallest suitable skill / workflow set
  → perform the task with appropriate tools and boundaries
  → verify what actually ran and what remains uncertain
  → request human approval where required
```

**Project-specific facts stay with the project.** KI-Regeln describes general ways of working, but it cannot know your files, requirements, credentials, environment or authorization from a prompt alone.

## What makes this different?

- **Problem-first discovery:** Users do not need to memorize skill names. Agents consult [AGENTS.md](AGENTS.md) and the catalog to select what is relevant.
- **Provider-independent design:** Methods are not tied to one model or vendor; platform capabilities and limitations are checked locally.
- **Evidence before claims:** Skills, [evaluations](Evals/README.md), review gates and the [verification/reporting contract](Testing-und-QA/Umgebungsabhaengige-Verifikation-und-Reports.md) distinguish executed checks from defined or unavailable checks.
- **Human control:** Tool availability is not permission to publish, deploy, purchase, alter production data or take other external actions.
- **Traceable reuse:** External influences and licensing are documented rather than silently copied into the toolkit.

## Maturity and verification

KI-Regeln is an **experimental, actively maintained project**. Skill count is an inventory metric, **not** proof of quality. Defined evaluations are not automatically executed or independently validated. A successful structural check is not evidence that a real-world model always follows the rules.

See the [skill maturity and evaluation catalog (German)](Dokumentation/Skill-Katalog.md) and [evaluation documentation](Evals/README.md) for actual status and limitations.

## Contributing, licensing and reuse

We welcome careful reviews, bug reports and contributions. Read [CONTRIBUTING.md](CONTRIBUTING.md), the [security policy](SECURITY.md) and the [documentation index](Dokumentation/README.md). The canonical agent instructions remain in [AGENTS.md](AGENTS.md); translations of the human introduction never override them.

The root [MIT license](LICENSE) covers KI-Regeln-owned material unless a file states otherwise; **it does not relicense third-party material**. Six explicitly listed generated media assets are **excluded from MIT** and documented separately under **CC BY-SA 4.0** to the extent licensable rights exist. Before reusing any media or adapted material, consult [ASSET-LICENSES.md](ASSET-LICENSES.md), [REUSE.toml](REUSE.toml) and [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md). A root license is not itself a publication authorization; current public-release gates are recorded in [open-source-readiness.yml](Dokumentation/open-source-readiness.yml).

## About BorstWerk

KI-Regeln is part of [BorstWerk](https://github.com/Borstwerk), a non-commercial, problem-driven collection of tools that grew from practical needs among friends and family.

> **You don't have to know the toolbox before you can use it. Start with your task.**
