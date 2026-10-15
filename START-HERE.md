# KI-Regeln — Start here

**Language:** English · [Deutsch](START-HIER.md) · [Project overview](README.md)

> **Bring a task. Let the AI find a suitable way to work on it.**

KI-Regeln is for people who want to **get something done with generative AI** without first learning skill names or agent architecture. Start with your goal, not with the toolbox.

## 1. Describe what you want to achieve

For example: “Help me change a PowerShell script safely”, “Check this claim using reliable sources”, or “Help me revise a story while keeping the characters consistent”.

An initial request can be as simple as:

> I want to **[describe the task]**. You may read the relevant KI-Regeln repository files for this work. Find the rules, skills or workflows that actually apply, select only those needed and briefly explain your choice. Treat my project information as the local source of truth and be explicit about what you could not verify. Ask for approval before risky or external actions.

**This is an example, not a mandatory magic prompt.**

## 2. Give the assistant access to relevant information

- Provide the repository, relevant files or an available repository connection. **A link alone does not prove** the model has accessed or read the files.
- Share your task, project instructions and relevant sources. Use appropriately authorized channels for private data and credentials.
- KI-Regeln is **not an automatically installed ChatGPT or Codex feature**. Whether a skill can be read, a tool used or a test run depends on the actual environment and permissions.

### If the AI cannot access the repository

1. Ask it to **name which KI-Regeln files it actually opened**. A pasted GitHub URL or a confident summary is not evidence of file access.
2. If access is unavailable, share the necessary files through an authorized upload, local checkout or supported repository connector. Start with [`AGENTS.md`](AGENTS.md) for agent-led work; for nontrivial tasks the agent must also access the relevant router files that `AGENTS.md` names. Share only task-relevant material, **not** the entire repository by default.
3. If the required files or tools still cannot be accessed, stop that part of the workflow and mark it **NOT RUN / UNVERIFIED**. Do not claim the repository's rules or tests were applied.

**Quick check:** *“Which KI-Regeln files did you open for this task, and what could you not access or execute?”*

## 3. What the assistant should do

```text
Your task and existing project context
→ understand the local source of truth and requirements
→ discover the smallest relevant skill / workflow set
→ work with appropriate tools
→ report what was actually done, verified and still uncertain
→ request approvals when necessary
```

The assistant should not load every skill or ask you to pick skill names first. Sometimes **no special skill** is needed. To explore other options, ask: *“What additional capabilities might genuinely help with this task?”*

## 4. What stays with you and the project?

KI-Regeln offers general methods, **not automatic knowledge of your project**. Requirements, files, systems, current facts, test data, preferences and permissions must come from the real task and its environment.

A defined test is not an executed test; a green structural check is not independent proof of real-world behavior. Publishing, changing production data or deploying software still requires the appropriate human or project-specific authorization.

## 5. Where to go next

- [Practical examples (German)](PRAXISBEISPIELE.md) – real workflows with limitations and corrections.
- [Detailed usage guide (German)](Dokumentation/Nutzung-des-Repositories.md) – project integration and working model.
- [Skill handbook (German)](Dokumentation/Skill-Handbuch.md) – how the toolkit selects methods.
- [Skill maturity and evaluation catalog (German)](Dokumentation/Skill-Katalog.md) – skills, maturity and evaluation coverage.
- [AGENTS.md (German)](AGENTS.md) – canonical technical bootstrap for AI agents, not the human quickstart.
- [CONTRIBUTING.md (German)](CONTRIBUTING.md) – how to contribute and propose changes.

**Core principle:** Centralize general methods; keep project-specific truth local.
