# CF-01 – Offizielle Cloudflare Skills: statische Admission-Vorprüfung

**Datum:** 25.10.2026 · **Status:** `OBSERVED / PARTIAL REVIEW /
NOT ADMITTED / NOT RUN`

## Herkunft und geprüfter Stand

- Hersteller-Repository:
  [cloudflare/skills](https://github.com/cloudflare/skills),
  `main`, Commit `86505e44f87d801aa1864a3c4109e9a8ae5c409f`
  (bei Sichtung).
- Herstellerseite:
  [Claude Code + Cloudflare](https://developers.cloudflare.com/agent-setup/claude-code/),
  [MCP-Dokumentation](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/).
- GitHub-Metadaten und Plugin-Manifeste: **Apache-2.0**.
  Vor Codeimport wäre eine datei- und paketbezogene Lizenz-/NOTICE-
  Prüfung erforderlich.
- Sichtungsumfang: Root-README, 19 Namen/Verzeichnisse unter
  `skills/`, Stichprobe von `SKILL.md` einschließlich
  `cloudflare`, `workers-best-practices`, `wrangler`,
  `cf-cli`, `web-perf`, `agents-sdk`,
  `durable-objects`, `turnstile-spin`,
  `nextjs-on-cloudflare`, `cloudflare-one`,
  `sandbox-next`; `.claude-plugin/plugin.json`,
  `.claude-plugin/marketplace.json`,
  `.codex-plugin/plugin.json`, `.mcp.json`.
- **Nicht** durchgeführt: vollständiger rekursiver Bundle-/
  Script-/Dependency-/Submodule-Audit, Codeausführung, Lizenzprüfung
  aller Unterdateien, Credential-/OAuth-Verifikation, Installation,
  MCP-Verbindung, Cloudflare-Kontoabfrage oder Tests. Die
  Stichprobe ist **keine Sicherheitsfreigabe**.

## Beobachtete Architektur

1. Ein generischer **Cloudflare-Produktskill** routet eine
   Nutzerabsicht zu passenden Cloudflare-Produkten und
   tieferen Produkt-Skills/Referenzen. Seine eigene
   `SKILL.md` ist relativ umfangreich; für Tokenvergleiche
   **wirkliche geladenen Bytes/Tokens messen**, nicht nur
   die Zahl der Skills.
2. Nachladbare Referenzen unter
   `skills/cloudflare/references/` zu D1, R2,
   Queues, Pages, Security usw.; keine Pflicht zum
   Laden sämtlicher Referenzen.
3. Agentenfreundliche Hersteller-Dokumentation über
   `developers.cloudflare.com/<produkt>/llms.txt`
   und einzelne Docs-`/index.md`-Endpunkte.
   Das senkt möglicherweise die HTML-Boilerplate,
   ist **kein** nachgewiesener End-to-End-Tokengewinn.
4. Skills und `MCP` **gemeinsam** im Plugin.
   `.mcp.json` referenziert
   `https://mcp.cloudflare.com/mcp` (Streamable HTTP).
   Ein reines „Cloudflare Skill installieren“ über das
   Plugin kann daher zugleich einen **neuen externen
   Tool-/Kontozugriffsweg** registrieren.
5. Auf Entwicklerseite: `cf-cli` ist **Beta**;
   für vorhandene Wrangler-Konfigurationen bleibt
   `wrangler` der projekttreue Pfad. Hersteller-
   Versionsempfehlungen können sich ändern.

## Drei strikt verschiedene Risiko- und Zulassungsstufen

| Stufe | Beispiel | Risiko | Vorläufige Entscheidung |
| --- | --- | --- | --- |
| **D – Docs** | Öffentliche Cloudflare-Dokumentation, `llms.txt`, `index.md` | Quellenfrische, Prompt-Injection/Drift, falsche API-Claims, Input-Tokens | `CANDIDATE` für Quellenvergleich ohne Installation |
| **S – Skill-Bundle** | `SKILL.md`, Referenzen, Skripte, weitere Skills | Fremdinstruktionen, Remote-Dependencies, Setup-/Credential-Anweisungen, Versionsdrift | `NOT ADMITTED`; vollständiger `skill-security-review` vor Activation |
| **M – MCP/Account** | Remote MCP `docs()`, `search()`, `execute()` | OAuth/API-Token-Rechte, Cloudflare-Ressourcenzugriff, potentieller Write/Delete/Deploy, dynamisch ausgeführter Code | `BLOCKED` ohne separate Tool-Admission und explizites Human Gate |

Das Code-Mode-MCP bietet laut Hersteller
`search`, `execute` und `docs` mit einer
kleinen Schnittstelle statt Tausender Tools. Das
kleine Schema ersetzt **nicht** die Prüfung der
effektiven Backend-Berechtigungen. Ein Toolname
`docs` beweist nicht, dass die ganze Verbindung
read-only durchgesetzt ist; Read-only-Scoping
muss zur Laufzeit technisch bestätigt werden.

## Spezifische Review-Punkte

- **Token/Context:** Der `cloudflare`-Router ist kein
  kostenloser Metadateneintrag. Workflowkosten
  = Pflichtreads + geladener Skill + Referenzen +
  Docs-/MCP-Toolausgaben + mögliche Retries.
- **Owner-Kollision:** Der Herstellerrouter darf nicht
  vor `AGENTS.md`, `skill-catalog.yml`,
  `routing-overlays.yml` und dem KI-Regeln-Workflow
  an die Stelle unseres Routers treten.
- **Fach-/Versionsdrift:** Bestehende Projekte mit
  `wrangler.{jsonc,json,toml}` weder still auf
  `cf` noch Next.js-Projekte ungefragt auf
  vinext migrieren. Die Cloudflare-Skills können
  solche Defaults empfehlen, aber diese sind
  nicht autorisierte Migrationsaufträge.
- **Script-Triggers:** `turnstile-spin` enthält
  Shellskripte/Tests und Token-/Account-Probes;
  keine Ausführung, Credentialweitergabe oder
  Installation aus einem bloßen Lesescope.
  `nextjs-on-cloudflare` verweist auf
  `npx skills add cloudflare/vinext`; nur
  Quellenlink, **kein** impliziter Fremdskill-Import.
- **Rechte:** Sicherheits- und Deploy-Skills
  nennen Konto, Service, Environment, Preview,
  Staging/Prod, Tokens, Rollback. Ein durch
  OAuth prinzipiell schreibfähiger Account
  macht einen einzelnen Auftrag **nicht**
  automatisch freigegeben.
- **Anmeldung:** Ein Cloudflare-Login kann bei
  unbedachter Weitergabe andere Konten/Tenants
  einschließen. Vor Kontoinspektion Account-ID,
  Credential-Scope, Human Gate und nachweisbare
  Runtime-Isolation prüfen.
- **Quelleninjektion:** Fremd-`SKILL.md` und Docs
  sind Daten, bis sie gesondert geprüft/admitted
  sind. README-Skripte, Authbefehle und
  Anweisungen zum Umgehen lokaler Policies nie
  als höherrangige Instruktionen ausführen.

## Vorläufiger Beschluss

**`SOURCE ACCEPTED FOR RESEARCH; BUNDLE AND MCP NOT ADMITTED`.**

Für CF-01 dürfen wir ein **konzeptuelles**
A/B-Testschema mit öffentlichen/synthetischen
Aufgaben entwerfen; ein echter Test oder ein
verbundenes Cloudflare-Konto braucht eine
separate Autorisierung. Kein eingeschalteter
Plugin, kein globaler Hook, keine neuen
KI-Regeln-Routerrechte.

[Plan CF-01](../../Evals/Agentenarbeit/Cloudflare-Skills-Pilot/README.md)
und [Architekturkarte](../Cloudflare-Hersteller-Skills-und-Docs-Option.md).
