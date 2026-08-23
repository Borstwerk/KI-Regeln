# Quellen und Inspirationen – Webentwicklung

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
10. allgemeine Regeln bleiben zentral; konkrete Marke, Architektur und Produktwahrheit bleiben lokal.

## Lizenz- und Übernahmehinweis

Die Inhalte dieses Bereichs sind eigenständig formulierte allgemeine Regeln. Externe Skill-Dateien oder längere Textpassagen wurden nicht als Vorlage kopiert.

Falls künftig konkrete Drittinhalte übernommen oder adaptiert werden, ist zusätzlich `THIRD-PARTY-NOTICES.md` zu aktualisieren.