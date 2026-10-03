# Quellen und Inspirationen – Webentwicklung

## Inhalt

- Zweck
- Anthropic – `frontend-design`
- Impeccable
- Firzus Agent Skills – Frontend Design Pipeline
- Vercel Labs – Agent Skills
- PracticalSwan – Frontend Design
- Ilm-Alan – Frontend Design
- Design-to-Code Skill-Sammlungen
- Motion und Mikrointeraktionen – methodische Referenzen
- HyperFrames – codebasierte Motion Graphics und Video
- Motion und Mikrointeraktionen – technische Primärquellen
- skills.sh
- Übernommene allgemeine Prinzipien
- Lizenz- und Übernahmehinweis

## Zweck

Dieses Dokument nennt externe Quellen und Skill-Sammlungen, die bei der Entwicklung der allgemeinen Webdesign- und Frontend-Regeln berücksichtigt wurden.

Die Quellen sind **Inspiration, Vergleichsmaterial und Praxisbeobachtung**. Sie sind keine projektspezifische Wahrheit und werden nicht ungeprüft übernommen.

> Konzepte werden übernommen, wenn sie Arbeit besser machen – nicht weil sie populär sind oder ein gutes Buzzword ergeben.

## Anthropic – `frontend-design`

Quelle:

https://github.com/anthropics/skills/tree/main/skills/frontend-design

Relevante Ideen:

- konkrete gestalterische Richtung vor Umsetzung;
- Design aus Produkt, Publikum und Zweck ableiten;
- eigenständige visuelle Identität statt templatisierter Defaults;
- typografische und kompositorische Entscheidungen bewusst treffen;
- typische generische AI-Frontend-Muster kritisch prüfen.

Einordnung:

Diente als starke Bestätigung für die Trennung von Designrichtung und Umsetzung sowie für den Anti-Template-Grundsatz.

## Impeccable

Quelle:

https://github.com/pbakaus/impeccable

Relevante Ideen:

- explizite Anti-Pattern-Regeln gegen wiederkehrende generische AI-Webästhetik;
- lokale Produkt-/Designidentität dokumentieren;
- spezialisierte Designaktionen wie Kritik, Politur, Typografie oder Reduktion;
- Design als wiederholbarer Review- und Verbesserungsprozess.

Einordnung:

Besonders wertvoll für den Gedanken, dass AI-Slop nicht nur durch bessere Prompts, sondern auch durch klare Designregeln und Reviewmechanismen reduziert wird.

## Firzus Agent Skills – Frontend Design Pipeline

Quelle:

https://github.com/Firzus/agent-skills

Relevante Ideen:

- Designsystem vor High-Fidelity;
- Greyboxing als eigene Phase;
- reale Inhalte nach Strukturfreigabe;
- Design- und Seitenentscheidungen explizit dokumentieren.

Einordnung:

Hat die allgemeine Pipeline `Designrichtung → Designsystem → Greybox → echter Content → Umsetzung` beeinflusst.

## Vercel Labs – Agent Skills

Quelle:

https://github.com/vercel-labs/agent-skills

Besonders relevante Skills:

- `web-design-guidelines`;
- `react-best-practices`;
- `composition-patterns`.

Relevante Ideen:

- Weboberflächen systematisch auf Accessibility und UX prüfen;
- Performanceprobleme nach Wirkung priorisieren;
- Netzwerk-Waterfalls und unnötige Bundlekosten vermeiden;
- Komponenten durch Komposition statt Konfigurations-Explosion strukturieren;
- spezialisierte Regeln progressiv laden statt riesige Kontextblöcke immer vollständig einzuspeisen.

Einordnung:

Besonders relevant für unabhängigen Webreview, Frontend-Performance und Komponentenarchitektur.

## PracticalSwan – Frontend Design

Quelle:

https://github.com/PracticalSwan/agent-skills

Relevante Ideen:

- Accessibility und Responsive-Verhalten als harte Qualitätsdimensionen;
- gerenderte Oberfläche statt nur Code bewerten;
- funktionale Korrektheit und visuelle Qualität zusammen denken.

## Ilm-Alan – Frontend Design

Quelle:

https://github.com/Ilm-Alan/frontend-design

Relevante Ideen:

- Content-Slop als eigener Fehlerbereich;
- keine erfundenen Kennzahlen oder scheinbar realen Produktdaten;
- normale Funktionen nicht unnötig mit futuristischer Sprache verkleiden;
- Design und Content bewusst getrennt beurteilen.

Einordnung:

Hat insbesondere `Webdesign/Content-und-Anti-Slop.md` beeinflusst.

## Design-to-Code Skill-Sammlungen

Beispiel:

https://github.com/JPeetz/agent-skills

Relevante Ideen:

- vorhandene Designs, Screenshots oder Mockups als konkrete Quelle behandeln;
- Tokens und Komponenten aus einer Referenz ableiten;
- visuelle Verifikation nach Implementierung;
- Design-to-Code nicht mit freier Art Direction vermischen.

## Motion und Mikrointeraktionen – methodische Referenzen

Für Phase 3.5 wurden drei konkrete öffentliche Skill-Artefakte source-spezifisch geprüft und ausschließlich als `reference/inspiration` verwendet:

- Emil Kowalski – `emilkowalski/skills`, `skills/animate/SKILL.md`;
- mblode – `mblode/agent-skills`, `skills/ui-animation/SKILL.md`;
- Taste – `Leonxlnx/taste-skill`, `skills/taste-skill/SKILL.md`.

Relevante abstrahierte Ideen:

- zuerst entscheiden, ob Motion überhaupt einen Produktzweck erfüllt;
- Frequenz und wiederholte Nutzung als Teil der Motion-Entscheidung behandeln;
- Spatial Continuity, Gesten und Interruptibility bewusst modellieren;
- Screenrecordings als Evidence zur Rekonstruktion beobachtbarer Bewegung nutzen, ohne daraus die ursprüngliche Technik zu erraten;
- unscharfe Designanforderungen bei Bedarf in wenige explizite lokale Parameter übersetzen.

Einordnung:

Die Quellen wurden **nicht** als Normenkatalog übernommen. Insbesondere feste Dauer-/Easingtabellen, harte Toolrankings, absolute Performancebehauptungen, benannte Skalen und Defaultwerte wurden nicht als universelle lokale Wahrheit übernommen. mblode wird bei Emil-nahen Craft-Heuristiken wegen genealogischer Nähe nicht als unabhängiger Konsens doppelt gezählt. Die konkrete Provenance-Klassifikation und die beobachteten Blob-SHAs stehen in `../Dokumentation/upstream-provenance.yml`.

Die daraus entstandene lokale Struktur trennt `motion-design`, `motion-implementation` und `motion-review`. Reverse Engineering aus Video ist ein Evidence-Modus von `motion-review`; die technische Umsetzung und die anschließende Browser-Gegenprüfung werden mit `motion-implementation` beziehungsweise `visual-verification` komponiert.

## HyperFrames – codebasierte Motion Graphics und Video

Repository:

https://github.com/heygen-com/hyperframes

Geprüfter Stand am 2026-10-03:

- Repository-Commit: `5561b8cb2f8b747e3da8844d32463f9859bd4050`
- `README.md`: Blob-SHA `973727c5af7ea2c8163a95a463f8627c3f8d8495`
- `skills/motion-graphics/SKILL.md`: Blob-SHA `59ec607875ea7a14df5f3ee7207730fd01063e0f`
- Root-Lizenz: Apache-2.0, Blob-SHA `ae06b37e1c5116ccfaa615ac25ec1aabf5658d8c`

Methodisch relevant sind:

- HTML-/CSS-/Media-basierte Komposition als editierbarer Videoquellzustand;
- seekbare Animation und frameweises Rendering als expliziter Runtime-Vertrag;
- getrennte Plan-, Source-, Design-, Build-, Verify- und Renderphasen;
- Asset-first-Planung und lokale, nachvollziehbare Medienquellen;
- Proof-Snapshots beziehungsweise Kontaktbögen als statische Evidence vor Render;
- Trennung verschiedener Produktionsmodi wie kurze Motion Graphics, Produktvideo, Explainer und Talking-Head-Repackage.

Die lokale Übernahme bleibt frameworkneutral. Insbesondere werden **nicht** als allgemeine Regeln übernommen:

- HyperFrames als Pflichtframework;
- konkrete CLI-Kommandos, Plugin-/Cloudpfade oder Installationsregeln;
- HyperFrames-spezifische Workflow-Namen als universelle Taxonomie;
- Runtime-Garantien von HyperFrames für andere Engines;
- konkrete Agenten-, Subagenten- oder Tool-Orchestrierung des Upstreams.

Das begleitende Video-/Praxisbeispiel, durch das diese Quelle entdeckt wurde, wird nur als **Field Observation / Discovery Lead** behandelt. Die gezeigten Qualitäts-, Zeit- oder Kostenergebnisse sind kein unabhängiger Benchmark und werden nicht als allgemeine Leistungszusage übernommen.

Daraus entstanden `Codebasierte-Motion-Graphics-und-Video.md` und der gleichnamige Workflow. Bestehende Motion-Skills wurden nur an den Stellen erweitert, an denen statische versus zeitliche Evidence oder die Scope-Grenze zur Gesamtvideoproduktion betroffen ist.

## Motion und Mikrointeraktionen – technische Primärquellen

Konkrete technische Aussagen werden nicht aus den Agent-Skills abgeleitet, sondern aus Primärdokumentation:

- MDN – `prefers-reduced-motion`;
- MDN – Web Animations API;
- MDN – `@starting-style`;
- MDN – View Transition API;
- MDN – CSS Scroll-driven Animations;
- Motion – offizielle Layout-Animations-Dokumentation;
- GSAP – offizielle Timeline-Dokumentation;
- GSAP – offizielle ScrollTrigger-Dokumentation.

Diese Quellen belegen technische Fähigkeiten und API-Verhalten. Sie sind **kein methodischer Designkonsens** und begründen keine pauschale Toolpräferenz. Browserunterstützung und API-Status bleiben zeitabhängige Evidence und werden bei Materialität aktuell geprüft. Die konkreten URLs und `local_impact`-Pfade stehen in `../Dokumentation/upstream-sources.yml`.

## skills.sh

Quelle:

https://skills.sh/

Einordnung:

Nützlich als Radar für neue öffentliche Agent-Skills und wiederkehrende Themen im Skill-Ökosystem.

Die Popularität eines Skills ist kein Qualitätsnachweis. Neue Kandidaten werden nach dem allgemeinen Pflegeprozess dieses Repositories bewertet.

## Übernommene allgemeine Prinzipien

Aus den Quellen wurden vor allem folgende allgemeine Konzepte bestätigt oder geschärft:

1. Designrichtung vor Code.
2. Informationsarchitektur vor visueller Politur.
3. echter Content vor Fülltext.
4. Designsysteme dokumentieren stabile Entscheidungen.
5. Anti-Slop-Regeln müssen sowohl visuelle als auch sprachliche Muster betrachten.
6. Accessibility, Performance und Responsive-Verhalten sind Qualitätsgates.
7. gerenderte Browserprüfung ist Teil der Verifikation.
8. unabhängiger Review ist stärker als Selbstbewertung des erzeugenden Agenten.
9. Komponenten sollen durch Komposition und klare Verantwortung wartbar bleiben.
10. Motion braucht einen benennbaren Produktzweck; keine Animation ist ein zulässiges Ergebnis.
11. Reduced Motion, Unterbrechbarkeit und reale Render-/Performance-Evidence gehören zur Motion-Qualität.
12. allgemeine Regeln bleiben zentral; konkrete Marke, Architektur und Produktwahrheit bleiben lokal.

## Lizenz- und Übernahmehinweis

Die Inhalte dieses Bereichs sind eigenständig formulierte allgemeine Regeln. Externe Skill-Dateien oder längere Textpassagen wurden nicht als Vorlage kopiert.

Die drei in Phase 3.5 geprüften methodischen Motion-Artefakte bleiben `reference/inspiration`, `material_scope: concepts/methods-only`, `redistribution_reliance: not-relied-on`; ihr finaler Similarity-Recheck ergab kein Signal für konkrete Ausdrucksübernahme. Deshalb entsteht aus ihnen keine neue Notice-Pflicht.

Falls künftig konkrete Drittinhalte übernommen oder adaptiert werden, ist zusätzlich `THIRD-PARTY-NOTICES.md` zu aktualisieren.
