# CF-01 – Offizielle Cloudflare-Skills als optionale Herstellerquelle

**Status:** `CANDIDATE / PLANNED / NOT ADMITTED / NOT RUN` · **25.10.2026**

## Entscheidungsidee

[Cloudflare Skills](https://github.com/cloudflare/skills) ist eine
offiziell gepflegte Sammlung von **19 Agent Skills**. Daneben bietet
Cloudflare agentenfreundliche, aktuelle Markdown-Dokumentation
(`llms.txt`, einzelnes `index.md`) und den Cloudflare Code Mode
MCP-Server. Dieser **Hersteller-Stack ist nicht dasselbe wie ein
neuer KI-Regeln-Skill**.

Wir prüfen eine **optionale, bedarfsabhängige Herstellerwissensschicht**:

```text
Alltagssprachlicher Auftrag
  → KI-Regeln: AGENTS.md + Pflicht-Router + Domänenowner / Workflow
  → Ist Cloudflare-Produktewissen tatsächlich notwendig?
       nein → bestehender Pfad, kein Cloudflare-Overtrigger
       ja   → offizielle Cloudflare-Skill-Description prüfen
              → nur benötigten Skill + Referenzen laden
              → aktuelle Produktdokumentation aus Cloudflare llms.txt /
                produktbezogener /index.md nachladen
  → KI-Regeln: Rechte, Source-/Versionsprüfung, Tests, Evidence, Human Gate
```

**KI-Regeln bleibt der fachliche Arbeits- und Freigaberahmen.** Ein
externes Skill ist ein **untrusted, versionsgebundener Referenzkandidat**
und kann kein `AGENTS.md`, keinen Primärowner und keine Freigabe
ersetzen. `related`-Kanten im externen Katalog sind keine
automatischen Pflichtaktivierungen.

## Offizieller Skillbestand – Stand des geprüften Snapshots

- **Produktsuche / Routing:** `cloudflare`.
- **Workers, CLI, Qualität:** `workers-best-practices`,
  `wrangler`, `cf-cli`, `workers-profiling`, `web-perf`.
- **Agenten und Zustandsverwaltung:** `agents-sdk`,
  `durable-objects`, `sandbox-stable`, `sandbox-next`,
  `sandbox-migrate-to-next`.
- **Web, Security und Plattformbetrieb:**
  `nextjs-on-cloudflare`, `turnstile-spin`,
  `cloudflare-one`, `cloudflare-one-migrations`,
  `gateway-workers`.
- **Daten und Kommunikation:** `basin`, `k2`,
  `cloudflare-email-service`.

Die Produkt-Descriptions sind **Routinghinweise, keine
funktionsgleiche Kopie** unserer Skills. Die Priorisierung dient
nur der späteren Review-Reihenfolge:

| Erste Kandidaten | Warum | KI-Regeln-Kollision / Owner |
| --- | --- | --- |
| `cloudflare` | Router vom Nutzerproblem zu Cloudflare-Produkt und Referenz | Nur ergänzender Herstellerrouter nach `Skill-Handbuch.md`, nie neuer globaler Router |
| `workers-best-practices` | Aktuelle Runtime-Patterns, Security und Worker-Konfiguration | `code-review`, `verification-loop`, Security; Herstellerdetails ergänzen nur |
| `wrangler` / `cf-cli` | Toolversionen, richtige CLI pro **vorhandenem** Projekt, Preflight | `deployment-strategy`, `infrastructure-change-review`, Tool-/Permission-Gates |
| `web-perf` | Browser-/Trace- und Core-Web-Vitals-Methoden | `frontend-performance` bleibt fachlicher Owner |
| `agents-sdk` / `durable-objects` | Cloudflare-spezifische Zustands-/Agentenarchitektur | Architektur-/Systemdesign bleibt Owner |
| `turnstile-spin` | Sicherheitssensitive Bot-Abwehr und Siteverify mit Scripts | `skill-security-review`; Account-/API-Writes separat zu autorisieren |

Die weiteren Skills bleiben zunächst **WATCH**. Ein konkreter
Cloudflare-Einsatz (z. B. R2, Workers, Zero Trust) darf die Reihenfolge
ändern, nicht jedoch das Admission-Gate.

## Entscheidende Prinzipien

1. **Statt eines Imports** einen zukünftigen *Vendor Skill Reference
   Adapter* als **Idee** prüfen: Quell-URL, gepinnter Commit,
   konkrete `SKILL.md`, geprüfte Referenzen/Scripts, aktuelle
   Dokumentationslinks, Trigger/Near-Misses und benötigte Capability.
   Kein implizites „Hersteller = darf alles“.
2. **Docs first / just in time**: Cloudflare-Dokumentationen über
   produktbezogene `llms.txt`-Indizes gezielt auffinden, einzelne
   `/index.md`-Seiten lesen. Verfügbarkeit/Format/Version und
   Belege bei einer konkreten Aufgabe prüfen; kein
   unkontrollierter `llms-full.txt`-Dump.
3. **Versions-/Projekttreue**: bestehendes `wrangler.jsonc`,
   `wrangler.json` oder `wrangler.toml` nicht still nach
   `cloudflare.config.ts` migrieren. Aktuelle Cloudflare-Docs
   und lokal tatsächlich installierte CLI-/SDK-Versionen
   haben Vorrang vor Modellwissen. `cf` ist Beta, keine
   ungefragte Neuinstallation.
4. **Getrennte Trust-Domänen**: (a) reine Skill-/Docs-Referenz,
   (b) CLI-/Script-Ausführung, (c) remote MCP mit Cloudflare
   Kontozugriff; jede hat **eigene** Aufnahme-/Berechtigungsgates.
5. **Kein Autonachladen von Fremdcode**: Ein Skill kann zusätzliche
   `npx skills add`-/Setup-/Auth-Befehle empfehlen (z. B.
   `nextjs-on-cloudflare` → vinext). Solche Texte begründen
   weder installierbare Abhängigkeit noch Schreibrechte.
6. **Fachliche Bewertung statt Token-Rhetorik**: Ein kurzer
   MCP-Tool-Descriptor ist nicht gleichbedeutend mit
   niedrigerem Gesamtverbrauch inklusive Suchen, Executes,
   Reruns, Kontext und Ergebnisverifikation.

## Mögliches Langfristbild – KEINE aktuelle Implementierung

- Optionaler herstellerneutraler **`vendor-skill-reference`-Adapter**
  *nur* bei wiederholter, nachgewiesener Routing-/Dokslücke.
- Katalog und Source-Versionierung für offiziell gepflegte
  Fremdreferenzen, **keine** Kopie von 19 Skill-Bundles.
- `Cloudflare` als erster begrenzter Referenzfall;
  Erweiterung auf weitere Anbieter **nur nach eigenem Review**.
- Das könnte KG-01 (Graph-Retrieval) und TE-01
  (Tooloutput-/Token-Fidelity) langfristig ergänzen; die
  gemessenen Effekte getrennt halten.

## Pilot- und Review-Quellen

- [CF-01 Pilotplan](../Evals/Agentenarbeit/Cloudflare-Skills-Pilot/README.md)
  – A/B Routing und Dokumentationsqualität, optionale separat
  gegatete MCP-Stufe; **NOT RUN**.
- [Cloudflare Bundle-Vorprüfung](Reviews/Cloudflare-Skills-2026-10-25.md)
  – Herkunft, Plugin-/MCP-/Script-/Auth-Grenzen,
  **NOT ADMITTED**.
- Hersteller: [Cloudflare Agent Setup für Claude Code](https://developers.cloudflare.com/agent-setup/claude-code/)
  und [offizielle Skills](https://github.com/cloudflare/skills).
- Bereits vorhanden: `Agentenarbeit/Skills/context-engineering`,
  `Recherche/Skills/source-evaluation`,
  `Sicherheit/Skills/skill-security-review`,
  `Sicherheit/Skills/tool-permission-review`,
  `Infrastruktur-und-DevOps/Skills/deployment-strategy`.

**Nicht vorgenommen:** neue `SKILL.md`, Eintrag in
`skill-catalog.yml`, `routing-overlays.yml`,
`AGENTS.md`-Änderung, Installation, Connect, Accountzugriff,
Cloudflare-Deployment oder CLI-Aufruf. Bei einem
späteren Pilot entscheiden wir erst über einen Adapter;
der Herstellerkatalog ersetzt nie unser Routing.
