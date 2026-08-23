# Upstream-Audit – 2026-08-23

## Zweck

Dieser Audit prüft einmal vollständig, welche externen Quellen des Repositories:

- **mutable Upstreams** sind und aktiv beobachtet werden sollten;
- **stabile oder veröffentlichte Referenzen** sind und keine laufende Dependency darstellen;
- nur **Radar-/Inspirationsquellen** sind, ohne aktuelle lokale Verhaltensabhängigkeit.

Die aktiv beobachteten Quellen stehen in `upstream-sources.yml`.

## Ergebnis

Der Audit ist für alle bestehenden Fachbereiche durchgeführt.

Es wurden zwei Monitoring-Arten festgelegt:

```text
exact-sha
→ konkrete GitHub-Datei
→ Blob-SHA vergleichen

semantic-review
→ lebende Web-/Produktdokumentation
→ relevante Konzepte erneut lesen und gegen lokale Regeln prüfen
```

Eine veränderte Quelle erzeugt immer nur einen Review-Kandidaten.

## Grundlagen / Arbeitsweisen

### Aktiv beobachtet

- Microsoft HAX Guidelines – semantischer Review, quartalsweise.

### Nicht als mutable Dependency registriert

- Microsoft-Research-Artikel zu Appropriate Reliance, ExtendAI und Critical Thinking;
- Self-Determination Theory als grundlegender Theoriebezug;
- Motivational Interviewing Network of Trainers;
- Meta-Analysen zu Implementation Intentions und MCII.

Begründung:

Diese Quellen dienen als Evidenz- oder Grundlagenbasis. Neue Forschung wird über den allgemeinen Radar-Check entdeckt; Änderungen an einzelnen historischen Artikeln sind kein sinnvoller Sync-Trigger.

`Arbeitsweisen/` nutzt diese Grundlagen mit, besitzt aber derzeit keine zusätzliche externe Skill-Dependency.

## Agentenarbeit

### Ergebnis

Die zentralen Quellen sind überwiegend veröffentlichte Engineering-Artikel, Changelog-Einträge oder Papers:

- Anthropic Context Engineering;
- OpenAI Harness Engineering;
- OpenAI Running Codex Safely;
- OpenAI Symphony;
- IBM Loop Engineering;
- Martin Fowler / Kief Morris;
- ArXiv Delegation Contracts;
- Anthropic Agent Evals;
- GitHub Traceability;
- ArXiv Vibe Architecting.

Diese werden nicht als exakte mutable Dependencies geführt. Neue Entwicklungen in diesem Feld gehören in den monatlichen Radar-Check.

Die bisher im Agentenquellen-Dokument genannten Matt-Pocock-Skills wirken konkret auf `Programmieren/` und werden dort jetzt dateigenau überwacht.

AI Hero bleibt eine Radarquelle, keine Sync-Dependency.

## Programmieren

### Neu als exact-sha registriert

- `mattpocock/skills` – `tdd/SKILL.md`;
- `mattpocock/skills` – `diagnosing-bugs/SKILL.md`;
- `mattpocock/skills` – `code-review/SKILL.md`;
- `mattpocock/skills` – `domain-modeling/SKILL.md`.

Für diesen Bereich wurde zusätzlich `Programmieren/Quellen-und-Inspirationen.md` angelegt.

## Schreiben

### Neu als semantic-review registriert

- Wikipedia `Signs of AI writing`.

Begründung:

Die Seite ist ein lebender Beobachtungskatalog. Änderungen können neue Prüfmuster liefern, dürfen aber niemals automatisch zu Wort-Blacklists oder KI-Autorenschaftsbehauptungen werden.

Für diesen Bereich wurde zusätzlich `Schreiben/Quellen-und-Inspirationen.md` angelegt.

## Bildarbeit

### Neu als semantic-review registriert

- Adobe Firefly Style Reference;
- Adobe Firefly Structure Reference;
- Midjourney Character Reference;
- Midjourney Omni Reference;
- Midjourney Style Creator.

### Audit-Fund

Die aktuelle Midjourney-Dokumentation weist darauf hin, dass für V7 Omni Reference an die Stelle von Character Reference tritt.

Die lokale Regel war bereits kompatibel, da sie Character Reference und neuere Omni Reference toolneutral als Varianten einer Identitätsreferenz einordnet. Deshalb war keine Verhaltensänderung nötig.

Der zeitbezogene Midjourney-V7-Updateartikel bleibt Referenzquelle, wird aber nicht separat als mutable Dependency geführt.

## Webentwicklung

### Bereits registriert

- Anthropic `frontend-design`;
- Vercel `web-design-guidelines`;
- Vercel `react-best-practices`;
- Vercel `composition-patterns`.

### Neu ergänzt

- Impeccable README / aktuelles Systemmodell;
- Firzus `frontend-design`;
- PracticalSwan `frontend-design`;
- Ilm-Alan `frontend-design`;
- JPeetz `design-to-code`.

Alle konkreten GitHub-Dateien werden per Blob-SHA überwacht.

`skills.sh` bleibt Radar-/Discoveryquelle. Popularität oder ein neuer Katalogeintrag ist kein lokaler Updategrund.

## Recherche

### Bereits registriert

- Firecrawl `deep-research`;
- PracticalSwan `research`;
- Hermes `grounded-citations`.

### Neu ergänzt

- OpenAI Deep Research Help – semantischer Produktreview;
- Jwynia `fact-check`;
- LangChain DeepAgents `web-research`;
- Microsoft VS Code Team Kit `research`;
- drader `research`.

### Nicht als aktive Dependency registriert

- Stanford STORM – Paper / Forschungsreferenz;
- K-Dense wissenschaftliche Skills – Inspirationsquelle für einen möglichen späteren Wissenschaftsbereich, derzeit ohne direkte lokale Verhaltensabhängigkeit.

## Dokumentationserstellung

### Bereits registriert

- mcollina `documentation`;
- mblode `docs-writing`;
- JPeetz `technical-documentation`.

### Neu ergänzt

- Google Developer Documentation Style Guide – semantisch, quartalsweise;
- Write the Docs `Docs as Code` – semantisch, quartalsweise;
- The Good Docs Project Templates – semantisch, quartalsweise;
- Vale Agent Skills – semantisch, monatlich.

Diátaxis bleibt eine grundlegende Framework-Referenz. Das Modell wird im normalen vierteljährlichen Repo-Audit erneut eingeordnet, aber nicht wie eine konkrete `SKILL.md` als Sync-Dependency behandelt.

## Monitoring-Entscheidung

### Monatlich

Besonders volatile Quellen:

- konkrete GitHub-Skills auf `main`;
- aktuelle KI-Produktdokumentation;
- Bildgenerator-Funktionen;
- Vale-Agent-Skills;
- Deep-Research-Produktoberflächen und -Skills.

### Quartalsweise

Langsamer veränderliche lebende Leitfäden:

- HAX Guidelines;
- Google Developer Documentation Style Guide;
- Write the Docs;
- Good Docs Project;
- Wikipedia-Patternkatalog.

### Nur Radar / Referenz

- Papers;
- datierte Research-Artikel;
- historische Changelog-Posts;
- allgemeine Skill-Kataloge ohne direkte lokale Abhängigkeit.

## Abschlussurteil

Der Quellenbestand ist nach diesem Audit vollständig nach Wartungsart klassifiziert.

Neue externe Quellen müssen künftig bei Aufnahme explizit einer der drei Klassen zugeordnet werden:

```text
aktive Dependency
→ upstream-sources.yml

stabile Referenz
→ Fachbereich/Quellen-und-Inspirationen.md

Radar-/Discoveryquelle
→ Fachquellen oder Pflegeprozess, aber kein künstlicher Sync-Trigger
```

> Nicht jede Quelle muss überwacht werden. Aber jede relevante mutable Abhängigkeit muss als solche erkennbar sein.