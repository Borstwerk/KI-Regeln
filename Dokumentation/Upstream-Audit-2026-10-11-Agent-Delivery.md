# Upstream-Audit – Agent Delivery, Review, Binary Verification – 2026-10-11

## Entscheidung

Vier HypeRadar-Funde gegen KI-Regeln geprüft. Ergebnis: **keine neuen Skills und keine Vendor-Dependencies**. Vorhandene Ownership stärken, nur neue allgemeine Verträge ergänzen.

| Quelle | Schon vorhanden | Tatsächlich ergänzter Baustein | Entscheidung |
|---|---|---|---|
| Cockroach Labs MOLT Sinai | `diagnose`, Bugdiagnose, Review-Revise, Handoffs | risikobasierter Plan-Review **vor** riskantem WRITE, Circuit Breaker, Kontext-Redundanz-Audit | adaptieren, kein Krankenhaus-Rollenspiel als globale Pflicht |
| Shooter-Decompilation | `binary-analysis`, Triage, Prüf-Evidence, Replay | unabhängiger Binary-Verification-Oracle mit Schutz von Testbaseline/Referenz | adaptieren, kein behaupteter Byte-Äquivalenzbeweis |
| BinceQu/RoboHarness | Agent-Tool-Vertrag, READ/WRITE/ACTION, Observation | strukturierte Beobachtung → begrenzte Aktion → neue Observation → Akzeptanz | abstrahieren, keine Robotik-Dependency |
| Harvard/Jellyfish, vermittelt über Ars Technica | QA/Release-Gates und Observability | Delivery-/Review-Metriken statt allein Code-/PR-Menge | Methodik adaptieren, Studienergebnisse nicht als lokale Messung ausgeben |

## Quellen und Grenzen

### Cockroach Labs – Five months treating bugs like patients and coding agents like a medical team

Quelle: https://www.cockroachlabs.com/blog/experiment-running-hospital-code/

Veröffentlicht am 09.10.2026, Erfahrungsbericht aus dem MOLT-Sinai-Team.

Relevante Beobachtungen:

- eigene Rollen für Aufnahme, Ursachenanalyse, Planprüfung, Umsetzung, Review und Discharge;
- kein Code vor belegtem Plan und überprüfter Planannahme in risikoreichen Workflows;
- bei neuer Scope-Wirkung zurück in Planreview;
- strukturierte Handoffs und Eskalation statt endloser Reparaturversuche;
- umfangreiche redundante Rolleninstruktionen verursachten unnötige Kontextkosten;
- Reviewwartezeit, Tokenkosten und Bürokratie waren reale Nachteile.

**Transfer:** Cockroach-Labs-Rollen sind Organisationsentscheidungen, keine allgemein benötigten KI-Regeln-Skills. Einfache lokale Bugfixes nicht in eine mehrstufige Orchestrierung zwingen. Eine separierte Planprüfung liefert vor allem bei hoher Wirkung mehr Wert.

### Shooter-Dekompilierung

Quelle: https://momo5502.com/posts/2026-10-09-game-decompilation/

Relevante Methodik: Referenzbinary/OBJ, kontrollierte Compilerbedingungen, Bytevergleich unter Berücksichtigung von Relocations sowie separater Vergleich referenzierter Symbole und Offsets. Das Prüfsystem muss unabhängig von der rekonstruierten Ausgabe vertrauenswürdig bleiben.

**Transfer:** Die Prüfstufe im lokalen `Binary-Verification-Oracle.md` ist eine allgemeine Methodik. Bytegleichheit gilt nur unter den dokumentierten Bedingungen; Compilerunterschiede und ungeprüfte Seiteneffekte begrenzen die Aussage. Keine echte Binary-Verifikation durch diesen PR durchgeführt.

### BinceQu RoboHarness

Quelle: https://github.com/BinceQu/RoboHarness

Relevanter Aufbau: visuell erfassbare Keypoints, Tracking, geometrische Constraints, primitive Aktionen und beobachteter Endzustand. Benchmarkangaben sind projektspezifisch und nicht auf Coding-Agenten übertragbar.

**Transfer:** `Observation → Allowed Actions → Preconditions/Authorization → Toolreceipt → Observation → Acceptance` für zustandsbehaftete Tools; keine robotische Runtime oder Trainingsdaten importiert.

### Software-Output vs. Code-Volumen

Quelle: https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/

Der Ars-Artikel vom 09.10.2026 berichtet über Untersuchungen von Fiona Chen und James Stratton anhand aggregierter Jellyfish-Arbeitsereignisse. Berichtet werden höheres Code-/PR-Volumen, längere Reviewzeiten und keine statistisch signifikante Steigerung der Issue-/Epic-Abschlüsse in der betrachteten Stichprobe. Beobachtungs-/Differenz-von-Differenzen-Design; keine universelle Garantie für künftige oder lokale Effekte.

**Transfer:** In `Agentenarbeit/Delivery-und-Review-Metriken.md` zählen akzep­tierte Ergebnisse, Reviewaufwand, Reverts und Kosten als separate Signale. **Keine lokalen Produktivitätswerte aus externen Studien übernehmen.**

## Lokale Änderungen

- `Workflows/Bugdiagnose.md`: risikobasierter Plan-Review vor riskantem WRITE und Circuit Breaker;
- `Programmieren/Skills/diagnose/SKILL.md`: gezielte Übertragung auf den Fachowner;
- `Workflows/Review-Revise-Loop.md`: Stagnation → erneute Diagnose statt improvisierte Reparatur;
- `Reverse-Engineering-und-Binaeranalyse/Binary-Verification-Oracle.md` + Anbindung;
- `Agentenarbeit/Agenten-Aktionsoberflaechen.md` und `Skill-Engineering/Agent-Tool-Vertraege.md`;
- `Agentenarbeit/Delivery-und-Review-Metriken.md`;
- `Skill-Engineering/Skill-Redundanz-und-Kontextkosten.md` mit purem report-only Analyzer `tools/skill_redundancy_audit.py`;
- ergänzende Skill-Evals und synthetische Tooltests.

## Explizit nicht übernommen

- globale Pflicht für ein separates Multi-Agent-Ärzteteam bei jedem Bug;
- neue Fachskills oder `routing-overlays.yml`-Einträge ohne eigenen Job;
- automatische Bearbeitung von Tests, Referenzbinary oder Gate-Thresholds;
- Robotik/Simulator, trainierte Modelle oder proprietäre Toolkits;
- feste Token-/LOC-/PR-Grenzen aus fremden Projekten als Repo-Policy;
- automatisches Löschen identischer Skillabsätze.

## Test- und Beweisgrenze

Repo-Validator, Unit Tests und CI bestätigen Struktur und Code-Contracts, **nicht** die Behauptung einer höheren Lieferqualität. Neue Skill-Evalcases sind zunächst **DEFINED / NOT RUN** als Behavioral Tests. Der Redundanz-Audit misst lexikalische Kandidaten, keine semantische Redundanz, keine Tokenersparnis und keine Sicherheit.

## Nächster legitimer Schritt

Unabhängige Fresh-Agent-Evals für risikoreiche und risikoarme Bugfixes sowie für Oracle-Gate-Manipulation. Erst danach Maturity-/Prozess-Claims oder automatische Gates weiter ausbauen.
