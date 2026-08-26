# Third-Party Notices

Diese Datei enthält ausschließlich Materialien, bei denen die aktuelle Provenance-Bewertung eine konkrete Übernahme, Vendoring- oder Adaptionsbeziehung mit Notice-Pflicht festhält.

Die kanonischen Provenance-Entscheidungen stehen in `Dokumentation/upstream-provenance.yml`; beobachtete Upstream-Artefakte und lokale Einflussbereiche stehen getrennt in `Dokumentation/upstream-sources.yml`.

## Matt Pocock – `mattpocock/skills`

Im Phase-3-Audit wurden vier Artefakte **jeweils separat** als `adapted` eingestuft. Für jeden Fall wurde der beobachtete Artefakt-Blob dem Repository-Commit `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76` zugeordnet. An diesem selben Commit liegt die Root-Datei `LICENSE` mit MIT-Lizenz vor; der Audit fand für diese vier Artefakte keinen widersprechenden pfadspezifischen Lizenzhinweis.

Notice-relevante Provenance-IDs:

- `mattpocock-tdd` – beobachteter Blob `8fc086710806190ee7c4baa32089cb877a75736a`;
- `mattpocock-diagnosing-bugs` – beobachteter Blob `061c25a524acaa93d4534e9e08a793c0a5fe45fd`;
- `mattpocock-code-review` – beobachteter Blob `e28d7acbf7b3bb4d7817b7eb5d9c105af03f6ec4`;
- `mattpocock-domain-modeling` – beobachteter Blob `9b97707e19ef1f590aada356f2b3f6bb881f91be`.

Die Einstufung als Adaption ist eine konservative Repository-Provenance-Klassifikation aus manuellem Strukturreview und historischer lokaler Provenance. Der automatische Textähnlichkeitscheck allein trifft keine Copyright- oder Lizenzentscheidung.

Source: `https://github.com/mattpocock/skills`

License evidence: `LICENSE` at commit `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`, blob `f1dd2c09108dde1a5f56097cee8461b3ea834499`.

### MIT License

Copyright (c) 2026 Matt Pocock

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Nicht Notice-pflichtig aus der aktuellen Bewertung

Die übrigen abschließend bewerteten GitHub-Upstreams sind als `reference/inspiration` klassifiziert und verlassen sich für die lokale Nutzung nicht auf eine Redistributionslizenz des Upstreams; deshalb wird hier für sie kein Lizenztext als Übernahme-Notice dargestellt.

`neon-postgres-best-practices` ist `review_status: assessed`, `use_class: reference/inspiration`, `material_scope: concepts/methods-only`, `redistribution_reliance: not-relied-on` und `redistribution_status: not-relied-on`. Die dokumentierte same-state Apache-2.0-Evidence ist historische Provenance-Evidence. Da keine konkrete Ausdrucksübernahme festgestellt wurde und für die lokale Nutzung keine Redistributionslizenz des Upstreams benötigt wird, entsteht für Neon kein Eintrag und keine Notice-Pflicht in `THIRD-PARTY-NOTICES.md`.

Für Hardening Phase 3.5 wurden `emil-kowalski-motion-craft`, `mblode-ui-animation` und `taste-design-parameters` nach dem finalen lokalen Textstand erneut als `reference/inspiration`, `material_scope: concepts/methods-only`, `similarity_audit: no-signal` und `redistribution_reliance: not-relied-on` bestätigt. Die lokalen Motion-Regeln sind eigenständig formuliert und übernehmen insbesondere keine konkreten Timing-/Easingtabellen, benannten Skalen, Defaultwerte oder Source-Struktur. Deshalb entsteht für diese drei methodischen Referenzen keine neue Notice-Pflicht.

Die in Phase 3.5 registrierten MDN-, Motion- und GSAP-Seiten dienen ausschließlich als technische Primärquellen für dokumentierte API-/Library-Aussagen; es werden keine Dokumentationsseiten oder längeren Textpassagen vendored oder als Drittmaterial weiterverteilt. Auch daraus entsteht durch diese Phase kein zusätzlicher Notice-Eintrag.
