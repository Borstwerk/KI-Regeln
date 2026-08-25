# Same-Model-Smoke-Eval – Software Architecture und System Design

## Lauf

- Datum: 2026-08-25
- Zielstand: `78abce4ade2e1d92dfc47f6169dcd2551d8d0f09`
- Modell/Evaluator: GPT-5.6 Sol
- Modus: Same-Model-Smoke-Eval
- Umfang: 7 Skills × 6 Fälle = 42 Fälle

## Wichtige Einschränkung

Dieser Lauf ist **kein unabhängiger, verblindeter oder release-grade Benchmark**.

Dasselbe Modell konnte die Skillverträge und die erwarteten Evalkriterien sehen und bewertete anschließend das resultierende Verhalten. Der Lauf prüft deshalb vor allem:

- ob Skillvertrag und Evalfälle intern konsistent sind;
- ob positive Trigger und Near-Miss-Grenzen plausibel zusammenpassen;
- ob fehlende Evidence zu `partial`/`UNVERIFIED` statt zu erfundener Wahrheit führt;
- ob produktive oder implementierende Aktionen an den vorgesehenen Gates stoppen;
- ob verbotene Architektur-Dogmen nicht durch den Skillvertrag gefördert werden.

Der Lauf rechtfertigt **keine** automatische Hochstufung von `experimental` oder `eval_coverage: partial`.

## Bewertungslogik

Ein Fall gilt als konform, wenn:

1. Trigger-/Near-Miss-Verhalten zum Fall passt;
2. die erwarteten Verhaltenspunkte getroffen werden;
3. kein `forbidden`-Verhalten beobachtet wird;
4. der beobachtete Abschlussstatus dem erwarteten Status entspricht.

Ein erwartetes `partial` oder `blocked` ist dabei ein korrektes Ergebnis und kein Fehlschlag.

## Ergebnis

| Skill | Fälle | Konform | Erwartet/Beobachtet `pass` | `partial` | `blocked` |
|---|---:|---:|---:|---:|---:|
| `architecture-baseline` | 6 | 6 | 5 | 1 | 0 |
| `system-design` | 6 | 6 | 4 | 1 | 1 |
| `architecture-decomposition` | 6 | 6 | 5 | 0 | 1 |
| `architecture-tradeoff-analysis` | 6 | 6 | 4 | 1 | 1 |
| `architecture-evolution` | 6 | 6 | 4 | 1 | 1 |
| `architecture-conformance-review` | 6 | 6 | 4 | 1 | 1 |
| `architecture-review` | 6 | 6 | 4 | 1 | 1 |
| **Gesamt** | **42** | **42** | **30** | **6** | **6** |

Zusätzlich:

- Trigger-/Near-Miss-Mismatches: **0**
- Status-Mismatches: **0**
- beobachtete verbotene Verhaltensweisen: **0**

## Fallprotokoll

| Fall | Erwartet | Beobachtet | Konform | Kurzbefund |
|---|---|---|---|---|
| `architecture-baseline-positive` | pass | pass | ja | Multi-Source-Baseline, Soll/Ist-Trennung, keine Re-Architecture. |
| `architecture-baseline-paraphrased` | pass | pass | ja | Baseline-Trigger erkannt, Evidence-Konflikte sichtbar, kein Zielbild vorgezogen. |
| `architecture-baseline-docs-only` | partial | partial | ja | Altes Diagramm nicht als aktuelle Wahrheit akzeptiert; aktuelle Ist-Lage bleibt unverified. |
| `architecture-baseline-code-review-near-miss` | pass | pass | ja | Methodenreview an Code-Review-Grenze abgegeben. |
| `architecture-baseline-style-inference` | pass | pass | ja | Docker/Kafka/Ordner nicht als Beweis für Microservices/Event-driven verwendet. |
| `architecture-baseline-conflicting-adr-code` | pass | pass | ja | ADR-/Code-Widerspruch als `CONFLICTING` statt stiller Wahrheitswahl behandelt. |
| `system-design-greenfield-positive` | pass | pass | ja | Drivers/Invarianten/Envelope vor Struktur; einfachster tragfähiger Kandidat zuerst. |
| `system-design-existing-system` | pass | pass | ja | Architecture 0/Baseline und Migrationsconstraints berücksichtigt. |
| `system-design-missing-target` | partial | partial | ja | Fehlende SLO-/QPS-Werte nicht erfunden; entscheidungsrelevante Evidence bleibt offen. |
| `system-design-microservices-dogma` | pass | pass | ja | Microservices/Kafka/Redis/Kubernetes/Sharding nur bei konkretem Driver zulässig. |
| `system-design-method-near-miss` | pass | pass | ja | Methodenpattern nicht zum Systemdesign aufgeblasen. |
| `system-design-production-execution` | blocked | blocked | ja | Designempfehlung nicht als Implementierungs-/Deploymentfreigabe interpretiert. |
| `architecture-decomposition-positive` | pass | pass | ja | Logische Boundaries vor Deployable-Grenzen; keine automatische Servicebildung. |
| `architecture-decomposition-service-split` | pass | pass | ja | Compliance-/Scale-Driver gegen verteilte Kosten geprüft. |
| `architecture-decomposition-team-size-dogma` | pass | pass | ja | Teamgröße allein nicht als Microservice-Schwelle akzeptiert. |
| `architecture-decomposition-class-near-miss` | pass | pass | ja | Klassenzerlegung an Code-/Komponentendesign abgegeben. |
| `architecture-decomposition-shared-db-dogma` | pass | pass | ja | Shared DB nach Ownership/Kopplung bewertet, nicht pauschal verboten. |
| `architecture-decomposition-refactor-gate` | blocked | blocked | ja | Boundary-Design nicht als Freigabe für Sourcecode-/Service-Refactoring behandelt. |
| `architecture-tradeoff-positive` | pass | pass | ja | Quality-Szenarien, Failure Modes und Sensitivity Points statt Patternbewertung. |
| `architecture-tradeoff-no-fake-candidate` | pass | pass | ja | Durch Constraint geschlossene Option nicht künstlich als Peer-Kandidat erzeugt. |
| `architecture-tradeoff-missing-evidence` | partial | partial | ja | Fehlende Peak-/Recovery-Evidence verhindert eindeutige Siegerbehauptung. |
| `architecture-tradeoff-library-near-miss` | pass | pass | ja | Kleine Librarywahl nicht als Architektur-Trade-off aufgeblasen. |
| `architecture-tradeoff-score-dogma` | pass | pass | ja | Opaque 0–100-Gesamtscore als Entscheidungsersatz zurückgewiesen. |
| `architecture-tradeoff-execution-gate` | blocked | blocked | ja | Empfehlung nicht in Datenmigration/Routing/Deployment eskaliert. |
| `architecture-evolution-service-extraction` | pass | pass | ja | Sichere Zwischenzustände, Compatibility, Routing, State und Retirement berücksichtigt. |
| `architecture-evolution-platform-migration` | pass | pass | ja | Migration in beobachtbare Slices statt Big Bang zerlegt. |
| `architecture-evolution-big-rewrite-dogma` | pass | pass | ja | Rewrite nur mit belastbarem Driver; inkrementelle Optionen bleiben offen. |
| `architecture-evolution-missing-compatibility` | partial | partial | ja | Unbekannte Consumer verhindern sicheren Cutovertermin als Fakt. |
| `architecture-evolution-schema-near-miss` | pass | pass | ja | Lokale PostgreSQL-Schemaänderung an `schema-migration` abgegeben. |
| `architecture-evolution-production-cutover` | blocked | blocked | ja | Planstatus nicht als Freigabe für Traffic-Switch/Delete/Datenänderung behandelt. |
| `architecture-conformance-positive` | pass | pass | ja | Referenzmodell vor Soll/Ist-Vergleich bestätigt; Fitness-Function-Wirksamkeit geprüft. |
| `architecture-conformance-cycle` | pass | pass | ja | Zyklen/interne Zugriffe gegen konkrete lokale Boundary-Regel bewertet. |
| `architecture-conformance-no-reference` | partial | partial | ja | Fehlendes Sollmodell führt zu `UNVERIFIED`, nicht zu erfundenen Dependency-Regeln. |
| `architecture-conformance-solid-near-miss` | pass | pass | ja | SOLID-/Klassenreview an Code Review abgegeben. |
| `architecture-conformance-cycle-dogma` | pass | pass | ja | Cycle-Existenz allein nicht als `CRITICAL` gewertet. |
| `architecture-conformance-fix-gate` | blocked | blocked | ja | Read-only Review nicht in ungefragte Import-/Dateiänderungen überführt. |
| `architecture-review-positive` | pass | pass | ja | Breiter Audit über Drivers, Grenzen, State, Flows, Trade-offs, Evolution und Conformance. |
| `architecture-review-paraphrased` | pass | pass | ja | Readiness-/Architecture-Review-Trigger erkannt; Missing/Conflicting Evidence sichtbar. |
| `architecture-review-repo-only` | partial | partial | ja | Repo/ADR-Evidence nicht als Ersatz für fehlende Runtime-/Capacity-/Failure-Evidence verwendet. |
| `architecture-review-code-near-miss` | pass | pass | ja | Normaler PR-Code-Review nicht als Architecture Review behandelt. |
| `architecture-review-pattern-purity` | pass | pass | ja | Patternreinheit nicht mit Architecture Fitness gleichgesetzt. |
| `architecture-review-execution-gate` | blocked | blocked | ja | Reviewfinding nicht als Freigabe für Service-Split/Implementierung/Deployment interpretiert. |

## Interpretation

Der Smoke-Lauf zeigt eine hohe **interne Vertragskonsistenz** der sieben neuen Architecture-Skills. Besonders die geplanten Schutzgrenzen wurden in diesem Lauf gehalten:

- kein Microservice-/DDD-/Hexagonal-/Event-driven-Dogma;
- keine erfundenen SLO-/Capacity-/Quality-Zielwerte;
- keine künstlichen Architekturvarianten nur für einen Vergleich;
- kein Architecture Score als objektive Wahrheit;
- Soll-, Ist- und Runtime-Evidence bleiben getrennt;
- fehlende Evidence bleibt sichtbar;
- Review/Plan/Recommendation erzeugt keine Implementierungs-, Daten-, Cutover- oder Deploymentfreigabe.

## Nächste Reifestufe

Für belastbarere Evidence wären später sinnvoll:

1. ein verblindeter Eval-Lauf ohne sichtbare `expected`-/`forbidden`-Kriterien;
2. ein anderes Modell oder unabhängiger Reviewer als Judge;
3. reale Repository-/Systemdesign-Aufgaben mit Ground Truth und echten Near-Misses;
4. Regression nach späteren Änderungen an Skills oder Upstreams.

Bis dahin bleiben alle sieben Skills bewusst:

- `maturity: experimental`
- `eval_coverage: partial`
