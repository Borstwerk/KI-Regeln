# Changelog

Dieses Dokument hält relevante Änderungen am Repository fest.

Die Versionierung ist datumsbasiert. Eine Version beschreibt einen bewusst nutzbaren Stand des zentralen Regelwerks.

## Unreleased

Noch nicht als eigener Versionsstand veröffentlichte Änderungen werden zunächst hier gesammelt.

### Lern-Prompt-Shortcuts – vier Ergänzungen

- `/lernzettel`, `/tafelbild`, `/probearbeit` und `/merkbild` als vier **eigene Prompt-Shortcuts** in `Dokumentation/ChatGPT-Funktionen-und-Lernwerkzeuge.md` und `Dokumentation/Allgemeine-Prompt-Shortcuts.md` ergänzt; nicht als universelle/offizielle ChatGPT-Kommandos dargestellt.
- Die ursprüngliche kuratierte 100er-Shortcut-Liste bleibt in Herkunft und Zählung abgegrenzt; die vier zusätzlichen Lernformate ergeben **100 + 4** dokumentierte allgemeine Kürzel.
- Lernzettel sichert Quellennähe und prüfungsrelevante Vollständigkeit; Tafelbild ordnet Beziehungen didaktisch mit fachlich korrekten Pfeilen; Probearbeit trennt Aufgabenblatt, Zeit/Punkte und späteren Lösungsschlüssel; Merkbild bietet einen fachlich geprüften visuellen Erinnerungsanker.
- Konkrete Promptbeispiele, Abgrenzungen zu `/cheatsheet`, `/mindmaps`, Quiz, `/mnemonic` und `/comicnodes` sowie fünf Negativtest-Ideen ergänzt.
- Kein zusätzlicher Skill, Plugin, Kommando-Registrierung oder Fremdtool. Qualitätskriterien sind dokumentiert, **nicht behavioral getestet**.
### Reverse Engineering und Binäranalyse – First Slice

- Neuer, bewusst schmaler Fachbereich `Reverse-Engineering-und-Binaeranalyse/` für die Untersuchung kompilierter Artefakte ohne gesicherten Quellcode. Vermeidet Werkzeug-Skills und doppelte Ownership mit `diagnose`/`code-review`.
- Zwei experimentelle Skills: `binary-triage` (Format, Runtime, sichere Capability-Wahl) und `binary-analysis` (Verhalten, Referenzen, Daten-/Kontrollfluss, Binär-Diffs und Evidence-Chain), jeweils mit Near-Miss- und Stop-Grenzen.
- Neuer Workflow `Binaerdatei-verstehen.md`; Dokumente zu Binary-Formatpfaden, Decompiler-Evidence, Isolation/Rechten und einer herstellerneutralen Runtime-Capability-Matrix für Ghidra, GhidraMCP, IDA MCP, ILSpyCmd, Cpp2IL sowie ergänzend BinDiff, capa, FLOSS, angr.
- Sicherheit: Unbekannte Binaries nicht ungefragt ausführen; getrennte READ / Analyseprojekt-WRITE / Binary-Patch-WRITE / dynamische ACTION-Grenzen; Binary-Strings und Tooloutput bleiben untrusted Daten.
- Upstream-Entscheidung in `Dokumentation/Upstream-Audit-2026-10-08-Reverse-Engineering.md`: Quellenstände und Lizenzen, keine Plugininstallation und keine automatische Übernahme externer Skills.
- Zwei Evalpacks mit insgesamt **15 definierten** Positiv-/Negativ-/Near-Miss-Fällen. `GT-18` ist ein separater verblindbarer, read-only Golden Task mit synthetischem Auszug und ausdrücklicher Verifikationsgrenze.
- Katalog, Master-Router, Workflow-Index, menschlicher Katalog und Repo-Einstieg synchronisiert; Blindrunner-Whitelist und CI-Package-Loop um den neuen Bereich/GT-18 erweitert; Regressionstest für die kuratierte Runner-Sicht.
- **Behavioral-Status:** Evals/GT-18 sind definiert, **NOT RUN**, keine Maturity-Hochstufung. Validator-PASS, sofern durch CI nachgewiesen, ist nur Struktur-/Paket-Evidence.

### Trustworthy Runtime Contracts

- Audit von BootLoops, trustworthy-agent-simulation, catbus und HyperFrames gegen vorhandene KI-Regeln: keine neuen Vendor-Skills, sondern zwei allgemeine Lücken identifiziert – **Agent-Tool-Verträge** und **Run-Replay-Verträge**;
- neuer `Skill-Engineering/Agent-Tool-Vertraege.md` plus `agent-tool-contract.schema.yml`: Selection, READ/WRITE/ACTION-Wirkung, maschinenlesbare Outputs, stabile Fehler-/Retry-Semantik, Chaining, Determinismusbedingungen und Acceptance-/Self-Test-Evidence werden als gemeinsamer Toolvertrag beschrieben;
- BootLoops-Muster generalisiert: Tooloutput ist erst nach passender Acceptance Evidence belastbar; Known-answer-/Negative-Control-/Independent-Route-Prüfungen werden als Verification-Klassen eingeordnet, ohne mathematische Spezialregeln zu übernehmen;
- catbus-Muster generalisiert: stabile Fehlercodes, Recovery-Hints, Capability Registry, maschinenlesbare Envelopes und explizite Action-Gates; Social-/Account-Automation selbst wird nicht übernommen;
- neuer `Agentenarbeit/Run-Replay-und-Reproduzierbarkeit.md` plus `run-replay-manifest.schema.yml`: Audit Replay, State Replay und Fresh Re-execution werden strikt getrennt;
- Trace-Datenmodell um Replay-/State-/Request-/Response-Referenzen und Replay-Ereignisse erweitert;
- Behavioral Harness `1.2.0` erhält `replay-run`: ein modellfreier Audit Replay verifiziert zuerst das immutable Run Package und rekonstruiert anschließend nur gespeicherte technische Evidence; keine Modell-/Toolcalls, keine neue Behavioral Evidence;
- neues `replay-report.schema.json` und synthetische Tests für deterministischen Audit Replay sowie Tamper-Rejection;
- HyperFrames-Audit in den bestehenden frameworkneutralen Motion-Workflow integriert: Runtime-/Plugin-/Skill-Snapshot getrennt betrachten, mutable Auto-Updates bei Reproduzierbarkeitsclaims vermeiden, Lint/Check/Snapshot/Preview/Render als mögliche Runtime-Evidence behandeln; keine 21 Upstream-Skills importiert;
- Quellenstände und Lizenzen dokumentiert: BootLoops Toolkit `66b680c` / Skills `ca89227` (MIT), trustworthy-agent-simulation `5c504f5` (Apache-2.0), catbus `8c09a0c` (MIT), HyperFrames `1e711b0` (Apache-2.0);
- `hello-agent-system` wurde am Commit `857823c` (MIT) als breite Produktions-/Lerncheckliste geprüft, lieferte gegenüber bestehenden Bereichen Reliability, Security, Evals, Context, Release und Observability aber keinen ausreichend neuen zentralen Vertrag; daher keine zusätzliche lokale Abstraktion.

### Deterministic Bootstrap Routing + Discovery Result Evidence

- Behavioral Rerun #4 zeigte: der Discovery-Gate aus PR #66 verbessert Suchverhalten, bindet aber nicht zuverlässig. `routing-overlays.yml` wurde in keinem der zwölf Läufe gelesen; `visual-answer`, `citation-audit` und die Voice-Composition blieben dadurch instabil oder vollständig unentdeckt;
- `AGENTS.md` erhält deshalb einen frühen und später wiederholten **Bootstrap-Read-Vertrag**: bei nichttrivialen Aufgaben müssen `Dokumentation/Skill-Handbuch.md`, `skill-catalog.yml` und `routing-overlays.yml` im aktuellen Lauf tatsächlich geöffnet beziehungsweise gezielt durchsucht werden; bei plausiblem mehrphasigem Prozess zusätzlich `workflow-index.yml` und der passende Workflow;
- der triviale Direktpfad bleibt unverändert, damit Faktenfragen und enge Ein-Satz-Zusammenfassungen weiterhin ohne künstliche Skill-Suche zu `none` routen können;
- Workflow-Kernowner werden geschützt: nennt ein geladener Workflow einen Skill ausdrücklich als Kern/Primary/zwingenden Schritt, muss dessen `SKILL.md` vor einem generischeren Ersatzkandidaten gelesen werden. Der Architektur-Tradeoff-Workflow konkretisiert dies für `architecture-tradeoff-analysis`;
- vor einer Ein-Skill-Entscheidung müssen explizit getrennte Jobs als getrennte Kandidaten geprüft werden, wenn sie tatsächlich eigenständige Ownership besitzen; damit bleibt Composition job-basiert statt related-basiert;
- die explorative Visual-A/B-Evidence wurde aus der operativen Visual-Runtime-Doku entfernt; `Skill-Engineering/Quellen-und-Inspirationen.md` wird zusätzlich aus Golden-Task-Runner-Snapshots ausgeschlossen;
- Claude-Adapter `0.3.2`: Glob/Grep-Evidence enthält jetzt einen Hash des beobachteten Resultats, Größe, erkannte package-lokale Pfade und erkennbare Skill-IDs; Suchausdruck und Sequenz bleiben erhalten;
- temporäre Managed-Policy-Doctor-Zustände wie `checking… (fetch in progress)` werden als `unknown` statt als vorhandene Remote-Policy klassifiziert;
- Regressionstests sichern Bootstrap-Read-Vertrag, Workflow-Kernowner, Discovery-Result-Evidence, Pending-Managed-Policy und die zusätzliche Blindrunner-Exclusion ab;
- einzelne Skill-Descriptions und die Golden-Task-Routing-Erwartungen bleiben unverändert. Der nächste Rerun soll zeigen, ob der mechanische Router-Floor GT-09/11/12/16 stabilisiert, ohne GT-10/15 in Over-Routing zu kippen.

### Bootstrap Discovery + Harness Evidence Hygiene

- Rerun #3 zeigte bei allen vier `discovery-required`-Golden-Tasks trotz verfügbarer Read/Glob/Grep-Discovery keinen Skill-Read; fachliche Outputs blieben überwiegend gut. Das wird als belastbares Under-Routing-Signal für den Bootstrap behandelt, nicht als Anlass, einzelne Skills triggerfreudiger zu machen;
- `AGENTS.md` und Master-Router erhalten deshalb ein verbindliches **Minimal-Discovery-Gate** für nichttriviale Aufgaben: Domäne/Workflow, plausible Katalog-Owner und aktuelle Cross-Cutting-Kandidaten dürfen nicht allein deshalb übersprungen werden, weil aus Nutzertext oder Fixture bereits eine plausible Antwort formulierbar ist;
- der triviale Direktpfad bleibt ausdrücklich erhalten: kurze Faktenklärung, mechanische Kleintransformation und eng begrenzte Ein-Satz-Zusammenfassung ohne Spezialanforderung dürfen weiterhin ohne künstliche Skill-Suche zu `none` routen;
- neues evaluator-only `behavioral_execution_mode: read-only | writable`; GT-13 ist als `writable` markiert. Prepared Packages geben den operativen Modus weiter, `readiness.yml` markiert Writable-Tasks als nicht bereit für den Default-Runner und der read-only Claude-Adapter blockt einen Modus-Mismatch vor dem Modellstart;
- der explorative Visual-Answer-A/B-Bericht wird explizit aus Golden-Task-Runner-Snapshots ausgeschlossen, weil er konkrete Human-Evidence aus früheren Testformen enthält;
- Claude-Discovery-Telemetrie protokolliert jetzt Suchausdruck und Ereignisreihenfolge für Glob/Grep sowie Action-ID/Sequenz für Skill-/Workflow-Reads; damit bleibt Reihenfolge auch dann rekonstruierbar, wenn Stream-Events keinen feingranularen Zeitstempel liefern;
- beobachtete Plugins werden auf Namen/IDs normalisiert und in der Runtime-Evidence sichtbar gemacht; `fresh_context` bleibt bei vorhandenen Plugins weiterhin streng `false` statt künstlich bereinigt;
- neue Regressionstests decken Writable-Readiness, Adapter-Modusblockade, A/B-Dokument-Isolation, Discovery-Ausdrücke/-Reihenfolge und Plugin-Namens-Evidence ab;
- GT-09/GT-11/GT-12/GT-16 bleiben unverändert in ihren fachlichen Skill-Erwartungen; der nächste Behavioral-Lauf soll prüfen, ob der Bootstrap-Fix die Discovery tatsächlich auslöst.

### Behavioral Harness Discovery Hardening

- read-only Claude-Runner erhalten zusätzlich zu `Read` kontrolliertes lokales `Glob` und `Grep`; Web, MCP, Bash und Mutation bleiben gesperrt;
- Runner-Prompt von „Behavioral Evaluation / nur tatsächlich nötige Dateien lesen“ auf neutrale Aufgabenbearbeitung mit gezielter Discovery umgestellt, damit der Harness Skill-Suche nicht selbst unterdrückt;
- Fixture-Pfade werden als exakte relative Pfade zum Runner-Package erklärt, um die im zweiten Lauf beobachteten falschen absoluten Pfade zu vermeiden;
- Golden Tasks unterscheiden evaluator-only `behavioral_routing_mode: discovery-required | outcome-primary`: fehlender Skill-Read ist nur im Discovery-Modus ein harter Read-Gate;
- GT-09, GT-11, GT-12 und GT-16 testen Discovery; GT-10, GT-13, GT-14, GT-15 und GT-17 bewerten primär Outcome/Gates und werden nicht allein wegen eines fehlenden Skill-Reads rot;
- `verify-run --run` akzeptiert jetzt auch einen Output-Root mit genau einem Run Package und meldet bei Mehrdeutigkeit die Kandidaten statt irreführend `run hashes missing`;
- Tests decken Discovery-Tool-Policy, lokale Search-Actions, Routing-Modus-Semantik und die neue Verify-Run-Pfadauflösung ab;
- GT-09/GT-12-Skills bleiben unverändert: die nächste Aussage über echte Routingregressionen soll erst aus Rerun #3 mit kontrollierter Discovery stammen;
- der strikte `fresh_context`-Vorbehalt bei beobachteten Plugins sowie der nicht verfügbare B2-Writable-Pfad für GT-13 bleiben als separate Evidence-/Capability-Gaps bestehen.

### Golden-Task Behavioral Blindness Hardening

- `golden_task_execution_view.py` gibt `id`, `title`, `goal` und `sources_of_truth` nicht mehr an den Runner weiter; diese Felder hatten im ersten Fresh-Agent-Lauf konkrete Routing-Hinweise verraten;
- neuer `golden_task_behavioral_harness.py` adaptiert Golden Tasks an den bestehenden Behavioral Harness statt ein paralleles Testsystem aufzubauen;
- Task-Fixtures werden unter neutralen Runner-Pfaden materialisiert; GT-13 nennt deshalb im Assignment keinen `Evals/Golden-Tasks/...`-Pfad mehr;
- Runner erhalten einen kuratierten Runtime-Repository-View mit Bootstrap, Katalog, Overlays, Workflows und operativen Domain-Dateien, aber ohne `Evals/**`, Changelog, Tests, Tools und bekannte evaluator-nahe Metadokumente;
- der kuratierte Workspace wird dateiweise gehasht und durch `verify_prepared_integrity` gegen Vorab-Manipulation geschützt;
- Claude-Code-Adapter erzeugt objektive `read`-Events für jedes tatsächlich gelesene `SKILL.md` und `Workflows/*.md`; Selection/Application/Rejected/Checkpoint werden weiterhin nicht aus File-Reads erfunden;
- CI führt neue Blindness-Regressionstests aus und baut GT-09 bis GT-17 als blinde Runner-Pakete;
- GT-09/GT-12-Routing wird in dieser Runde bewusst **nicht** fachlich verändert: erst der kontaminationsärmere Wiederholungslauf soll entscheiden, ob die beobachteten Misses echte Routingregressionen sind.


### Review-Korrekturen zu Routing Evidence Follow-up Hardening

- GT-13 widersprach der neuen allgemeinen Completion-Regel (Ein-Fix-Aufgabe verlangte `verification-loop`); GT-13 testet jetzt die Completion-Evidence, `verification-loop` und `diagnose` sind optional;
- Eval `mcp-config-deterministic-preflight` für `skill-security-review` auf ein Skill-Paket mit `.mcp.json` umgestellt, damit es der Bundle-Grenze nicht mehr widerspricht; Grenzfälle für eigenständigen MCP-Server, Plugin mit Skills und eigenständigen Hook ergänzt, ebenso ein positiver `tool-permission-review`-Fall für einen eigenständigen MCP-Server;
- `Sicherheit/MCP-und-externe-Tools.md` um Baseline für Plugins/Connectors und Hooks sowie die Regel „Paket mit Skills ist Skill-Bundle“ ergänzt;
- Routing-Trace um strukturierte Felder (`checkpoint_id`, `candidate_skill_id`, `replaced_skill_id`, `trigger_ref`) und die Events `ROUTING_REENTERED`, `CANDIDATE_REJECTED` erweitert; `Trace-Datenmodell.md` nachgezogen;
- Deep-Research-Workflow: `citation-audit` ist bedingt statt bedingungslos;
- drei Near-Miss-Fälle so umformuliert, dass der Prompt das Negativ nicht mehr selbst ankündigt;
- `AGENTS.md` Schritt 12 verweist auf die Registry statt Skill-Namen hart zu kodieren; Dateimodus von `tools/repo_validator.py` auf ausführbar zurückgesetzt;
- Hinweis: Die automatische Repo-Validation blockiert Merges nur, wenn sie in der Branch Protection als Required Check eingetragen ist. Das lässt sich aus dem Repository nicht prüfen;
- weiterhin offen: kein Golden Task und kein Eval-Fall für das ereignisgesteuerte Re-Entry; Behavioral Runs bleiben **DEFINED / NOT RUN**.

### Routing Evidence Follow-up Hardening

- Repo-Validation läuft zusätzlich zu `workflow_dispatch` automatisch auf Pull Requests und auf Pushes nach `main`; damit kann ein strukturell roter Golden Task nicht mehr still über einen normalen PR gemerged werden;
- GT-13-YAML-Fehler behoben und Prompt entkontaminiert: der Agent bekommt nicht mehr den konkreten Validatorbefehl oder PASS-Mechanismus vorgesagt; `verification-loop` bleibt erwarteter Cross-Cutting-Job, `diagnose` ist optional;
- allgemeine Fresh-Completion-Evidence-Regel aus dem Spezialskill `verification-loop` in die harten Bootstrap-Grenzen gehoben;
- ereignisgesteuertes Re-Entry für materiell neue Nutzerfakten, Tool-/Dateifunde, Scope-/Evidence-Änderungen und echtes Re-Planning ergänzt, ohne einen fünften globalen Checkpoint einzuführen;
- Security-Ownership nach Objekttyp geschärft: Skill-Bundle-Admission bleibt bei `skill-security-review`; eigenständige MCP-/Plugin-/Connector-/Hook-Integrationen folgen der externen Tool-Baseline, mit `tool-permission-review` für Capability-/Rechte-Scope;
- `citation-audit`, `claim-verification` und `source-evaluation` in ihren Runtime-Descriptions explizit gegeneinander abgegrenzt; zusätzliche Near-Misses gegen Citation-/Verification-/Visual-Bloat ergänzt;
- Bugdiagnose-Workflow macht `code-review` bei eng begrenzten deterministisch geprüften Konfigurations-/Datendatei-Fixes nicht mehr pauschal zum Pflichtschritt;
- GT-09 bis GT-14 sprachlich entkontaminiert; GT-14 erlaubt einen eigenständig begründeten `prompt-injection-review`, verbietet aber weiterhin redundantes `tool-permission-review`;
- Golden-Task-Suite auf **17** Aufgaben erweitert: GT-15 zweite No-Skill-Control mit lokaler Fixture, GT-16 expliziter Add-Zweig Communication+Voice, GT-17 positiver `tool-permission-review`-Fall;
- Golden-Task-Behavioral-Runs erhalten einen Routing-Trace-Vertrag auf Basis von `Agentenarbeit/trace-event.schema.yml`; reine Modell-Selbstauskunft gilt nicht als trace-verifizierte Skill-Aktivierung;
- neue und geänderte Behavioral-/Golden-Fälle bleiben bis zu einem tatsächlichen Lauf ausdrücklich **DEFINED / NOT RUN**.

### Routing Overlay Lifecycle Hardening

- `routing-overlays.yml` auf Schema v2 erweitert: `checkpoints` trennen `post-primary`, `pre-execution`, `pre-completion` und `pre-output`, ohne Triggertexte zu duplizieren;
- einmaligen Overlay-Pass durch phasenbewusste Re-Evaluation ersetzt, damit späte Trigger wie `citation-audit` nicht verloren gehen;
- Overlay-Komposition gehärtet: ein spezifischer Cross-Cutting-Skill darf vorläufiges generisches Primärrouting **verfeinern/ersetzen**, statt automatisch nur addiert zu werden;
- Security-Deduplizierung dokumentiert: `skill-security-review` besitzt die Admission externer/mächtiger Skill-Bundles; `tool-permission-review` wird nur bei eigenständigem Permission-Design zusätzlich geladen;
- Golden-Task-Schema erlaubt bewusst No-Skill-Controls mit `required_skills: []`, leeren Fixtures/Sources und `expected_domain: none`;
- Golden-Task-Suite von 9 auf **14** Aufgaben erweitert: GT-10 No-Skill, GT-11 Communication Primary Refinement, GT-12 late Citation Audit, GT-13 Verification Loop, GT-14 Security Dedupe;
- neues Evalpack für `citation-audit` mit sechs Fällen; Coverage steigt von `none` auf `partial`; Gesamtstand 152 Skills, 131× `partial`, 21× `none`;
- neue Behavioral-/Golden-Fälle bleiben bis zu einem tatsächlichen Lauf ausdrücklich **DEFINED / NOT RUN**.

### Cross-Cutting Skill Discovery und Routing Overlays

- neue maschinenlesbare Datei `routing-overlays.yml` als kleine globale Zweitprüfung nach dem fachlichen Primärrouting; Ziel ist, domänenübergreifende Skills zu entdecken, die der Nutzer nicht kennen oder nennen muss;
- bewusst **keine zweite Triggerdatenbank**: `routing-overlays.yml` enthält nur Skill-ID und Phase; die kanonische Trigger-/Near-Miss-Wahrheit bleibt in der jeweiligen `SKILL.md`;
- initiale Overlay-Kandidaten: `visual-answer` (presentation), `adressatengerechte-kommunikation` (communication), `citation-audit` und `verification-loop` (assurance), `skill-security-review` und `tool-permission-review` (security);
- neue Fachgrundlage `Skill-Engineering/Cross-Cutting-Skill-Discovery.md` mit mehrstufigem Routing: Primary → Workflow → Overlay Pass → Assurance/Gates → Runtime;
- `AGENTS.md`, `START-HIER.md`, Master-Router, Nutzungsdoku und Root-README auf automatische Skill-Discovery gehärtet: Nutzer müssen Skills nicht manuell aktivieren und frische Agenten sollen Overlays nach dem Primärrouting gezielt prüfen;
- neuer Schema-Vertrag `Schemas/routing-overlays.schema.json`; zusätzliche Validatorlogik prüft Schema, unbekannte Skill-IDs und doppelte Overlay-Skills;
- neuer Golden Task `GT-09`: Architekturtradeoff mit drei Varianten; der Prompt nennt keinen Skill und fordert kein Ausgabeformat, erwartet aber `architecture-tradeoff-analysis + visual-answer` als fachlichen Primärskill plus Presentation-Overlay;
- Golden-Task-Suite auf **9** Aufgaben erweitert; `GT-09` ist **DEFINED / NOT RUN**;
- Skillbestand bleibt **152**; Routing-Overlays sind Discovery-Metadaten und erzeugen weder neue Skills noch neue Autorisierung;
- Anti-Bloat-Regel festgelegt: typischerweise 1 Primärskill + höchstens ein Presentation/Communication-Overlay + nur tatsächlich notwendige Assurance-/Security-Skills.

### Visual Answer Hardening: Eskalation, Interaktion und Visual Fidelity

- `visual-answer` bleibt ein einzelner `experimental` Skill und wird **nicht** in mehrere Renderer-/HTML-Skills aufgespalten;
- neue Eskalationslogik eingeführt: `Level 0 Direct → Level 1 Compact Visual → Level 2 Visual Explanation → Level 3 Visual Artifact`; der Agent soll die kleinste ausreichende Stufe wählen statt komplexe Fragen reflexartig als HTML-Datei auszugeben;
- Whiteboard-Test und Urgency Override ergänzt: Visualisierung ist besonders sinnvoll bei Reihenfolge, Topologie, Zuständen, Entscheidungen und Kausalität; bei Incident/Meeting kommt Entscheidung/Sofortmaßnahme vor dem Artefakt;
- Interaction Gate ergänzt: jedes Control muss `Reader Question → User Action → sichtbare neue Erkenntnis` erfüllen; die statische Defaultansicht muss die Hauptaussage bereits tragen;
- interaktive Review-/Editierartefakte brauchen einen verwertbaren Export-/Übergabepfad für Nutzerentscheidungen, Kommentare oder geänderte Werte;
- klare Routinggrenze ergänzt: temporäre explorable Artefakte können `visual-answer` bleiben; dauerhafte Multi-User-/Auth-/Persistenz-/CRUD-Anwendungen werden an Web-/Softwareentwicklung übergeben;
- Ausgabeform stärker an Nutzung gebunden: Monitoring → Dashboard, Argument+Evidence → Report/Explanation, Print → One-Pager, Live Talk → Slides-Workflow, Exploration → explorable Artifact;
- neue **Visual-Fidelity**-Regeln für Daten/Charts: fehlend ≠ 0, Schätzung ≠ Ist-Wert, stale values kennzeichnen, Titel gegen Daten prüfen, Einheiten sichtbar halten, 3D-/Dual-Axis-/Truncated-Axis-Risiken beachten und bei Chartreview keine Werte aus Pixeln erfinden;
- acht zusätzliche `visual-answer`-Evalfälle für Urgency Override, Compact Visual, Interaction Gate, Static Story, Export Contract, fehlende Werte, Charttitel/Achse und durable-tool Routing ergänzt; `visual-answer` besitzt damit **16 definierte Fälle, NOT RUN**;
- `Maksim-Burtsev/visual-teacher` (Skill + Decision Rubric), `joshuadavidthomas/agent-skills/html-artifacts`, `robonuggets/html-it` sowie `raghuramsirigiri/raghuram-skills` (`chart-dashboard`, `chart-honesty`) als concepts/methods-only Quellen geprüft und als monatliche `exact-sha` Upstreams registriert;
- konkrete Rubric-Punktwerte, Host-spezifische Templates, HTML-by-default-Dogma, Style-Systeme, Chartbibliotheken und fremde Runtime-Implementierungen werden nicht übernommen.

### Visual Answer und HTML-Artefakte

- neuen experimentellen Skill `Dokumentationserstellung/Skills/visual-answer/SKILL.md` ergänzt; Ziel ist **Time-to-Signal** bei komplexen Antworten, nicht dekoratives HTML;
- neue Fachgrundlage `Dokumentationserstellung/Visuelle-Antworten-und-HTML-Artefakte.md`: Trigger für Architektur/Flows, Mehrkriterien-Vergleiche, Hierarchien/Timelines, komplexe Pläne und Multi-Finding-Reviews; kurze Faktenantworten, Smalltalk, reine Command-Ausgabe und Plain-Text-Wünsche bleiben Near-Misses;
- visueller Kern provider- und rendererneutral modelliert: erst Informationsform und semantische Hierarchie, danach native HTML-/Artefakterzeugung, spezialisierter Renderer, Plugin/App oder strukturierter Markdown-Fallback;
- Qualitätsgates ergänzt: Kernaussage zuerst, eine Informationsaufgabe pro Panel, Status nicht nur über Farbe, progressive Detailtiefe, keine dekorative Wiederholung und **keine Content-Verluste durch Layout**;
- direkte HTML-Ausgabe bevorzugt selbständig, responsiv und ohne unnötige Remote-/Tracking-Abhängigkeiten; `HTML erzeugt ≠ HTML visuell geprüft`;
- drei Zero-Install-A/B-Vergleiche vom 2026-10-06 als explorative Human-Evidence dokumentiert: Architektur/Überblick, Mehrkriterien-Entscheidung und Review mit 14 Findings; die HTML-Fassung wurde in allen drei Fällen vom menschlichen Reviewer bevorzugt, insbesondere wegen schnellerer Erfassbarkeit des Wichtigen;
- A/B-Evidence bewusst begrenzt: ein Reviewer, nicht verblindet, keine Zeit-/Recall-Messung, kein Token-/Kostenbenchmark und kein Test des originalen Renderers; daher keine Hochstufung über `experimental`;
- acht `visual-answer`-Evalfälle definiert: Architektur, Entscheidung, Multi-Finding-Review, kurze Faktenantwort, Plain-Text-Wunsch, Visual-Overkill, Content-Fidelity und fehlende Renderer-Capability; alle **DEFINED / NOT RUN**;
- `QingYunA/answer-me-with-html` am Commit `f3082c912c1637d7eff38e7a4c356545b756c75f` als Methodenquelle geprüft und vom Discovery-Radar zum monatlichen `exact-sha` Upstream promoted; genutzt werden nur Konzepte/Methoden, nicht CLI-Code, Theme-/Komponentensyntax, Always-on-Regel oder Benchmarkclaims;
- Skill-Katalog auf **152** zentrale Skills / **11** Dokumentationserstellungs-Skills aktualisiert; `visual-answer` startet `experimental` mit `partial` Evalabdeckung.

### HypeRadar Opportunity-Hardening: MCP, Verifikation, Retrieval und Logo-Design

- `graygnatconsole/mcp-audit-tool` source-spezifisch gegen Commit `94fec3bd11cd7c122f2f417130c090729ecce0cf` geprüft; konkrete Rule-Dateien zu Secrets, Supply Chain und Tool-Metadaten als `reference/inspiration` registriert;
- MCP-Regeln um einen deterministischen Config-Preflight ergänzt: hart codierte Secrets, sensitive Env-Weitergabe, ungepinnte Package Runner, Pipe-to-Shell, überbreiter Filesystem-Scope, unsicherer Transport/Auth, riskantes Auto-Approve und Wildcard-Rechte; maschinenlesbare Findings/SARIF sind mögliche Evidence, kein vollständiger Sicherheitsbeweis;
- Tool-Poisoning-Regexe ausdrücklich als Review-Signal statt Angriffsnachweis abgegrenzt und zwei neue `skill-security-review`-Evalfälle definiert;
- `BootLoops-ai/skills` am Commit `ca892277dcf0468d995f0036f3bd6d753a8afe7d` über `acceptance-gate`, `independence-bookkeeping` und `planted-truth` ausgewertet; `verification-loop` fordert bei wichtigen deterministischen Claims nun nach Möglichkeit einen Prüfpfad, der sichtbar scheitern kann, positive/negative Kontrollen, held-out beziehungsweise nicht zum Tuning verwendete Evidence und ehrliche Null-/Open-Ergebnisse;
- mathematische Spezialregeln wie feste Digit-Anzahlen oder konkrete Oracles werden nicht universalisiert; drei zusätzliche Verification-Evals sind **DEFINED / NOT RUN**;
- `multimodal-product-discovery` am Commit `bd87cd091d804e7336a81fc133b303ddb518e7c1` als Retrieval-Architekturreferenz aufgenommen; Knowledge Query trennt nun Candidate Generation und Reranking und behandelt Candidate Recall als vorgelagerten Bottleneck, den kein nachgelagerter Reranker reparieren kann;
- CLIP, FAISS, konkrete Gewichte und Fashion-Dataset bleiben Implementierungsdetails; zwei neue `knowledge-query`-Evalfälle sind **DEFINED / NOT RUN**;
- neuen experimentellen Bildarbeit-Skill `logo-design` samt Fachgrundlage und vier Evalfällen ergänzt: Brief → Kategorie/Klischees → viele günstige Ideen → drei unterschiedliche Richtungen → Schwarz-/Small-size-/Reversed-/Shelf-Prüfung → Konzept-Checkpoint → erst nach Freigabe kompletter Logo-Kit;
- `kaankiziltug/logo-design-skill` am Commit `0ecf52e9a4b3ac92b714f7cc6e3148ab8c774134` als Methodenquelle dokumentiert; dessen Bibliothek realer Fremdlogos wird **nicht** übernommen oder redistribuiert, da der Upstream selbst sie ausdrücklich von seiner MIT-Lizenz ausnimmt;
- Skill-Katalog auf **151** zentrale Skills / **5** Bildarbeit-Skills aktualisiert; `logo-design` startet `experimental` mit `partial` Evalabdeckung;
- `answer-me-with-html` wurde in diesem ersten Opportunity-Review zunächst als Testkandidat behandelt und nach drei positiven Zero-Install-A/B-Vergleichen in der nachfolgenden Visual-Answer-Erweiterung als Methoden-Upstream promoted; `strands-decider` bleibt im wöchentlichen Radar für kleine Decision Models mit lokaler Kalibrierung/Abstention;
- alle neun konkret übernommenen GitHub-Artefakte als monatliche `exact-sha` Upstreams registriert und mit Provenance-/Lizenzsnapshot gebunden; Discovery bleibt getrennt von Adoption;
- `dots` und `Chat_UI` erzeugen aus diesem Review keine lokale Regeländerung.

### Plugin-, App- und Capability-Routing

- neue Fachgrundlage `Skill-Engineering/Plugin-App-und-Capability-Routing.md`: fachlichen Job zuerst bestimmen, danach native Capability, verbundene Plugin-/App-Runtime, Plugin-Discovery und erst anschließend manuellen Fallback wählen;
- neue Nutzerreferenz `Dokumentation/ChatGPT-Plugins-und-Apps.md` mit aktuell beobachteten Beispielklassen für Design, Dateien, Mail/Kalender, Projektmanagement, Entwicklung, Daten, Marketing, CRM, Business, Recht, Reisen und Lernen; bewusst **keine** behauptet vollständige statische Pluginliste;
- OpenAI-Produktmodell sauber getrennt: Plugins können Workflow-Funktionen bündeln, Apps verbinden externe Dienste/Daten/Aktionen; Installation ersetzt keine notwendige App-/Account-/Workspace-Autorisierung;
- lokales Risikomodell `READ / WRITE / ACTION` ergänzt; `verfügbar ≠ verbunden ≠ autorisiert` wird als harte Routinggrenze behandelt;
- `AGENTS.md` prüft bei externen Diensten künftig native Capabilities und bereits verbundene Plugins/Apps vor manuellen Export-/Copy-Paste-Workarounds; passende fehlende Integrationen können transparent angeboten werden, ohne externe Aktionen selbst zu autorisieren;
- `Toolanforderungen-und-Fallbacks.md` und `skill-authoring` auf providerneutrale Capability-Verträge gehärtet: konkrete Apps sind normalerweise Runtime-/Adapterdetails, keine universelle fachliche Skillwahrheit;
- offizielles OpenAI Plugin Directory als **wöchentliche Discoveryquelle** in `radar-sources.yml` registriert; beobachtet werden neue Capability-Klassen, Write-/Action-Fähigkeiten, ersetzbare manuelle Fallbacks und Security-/Privacy-relevante Integrationen;
- offizielle OpenAI-Dokumentation zu Plugins und Apps als **monatliche semantic-review Upstreams** registriert, weil Plugin-/App-Begriffe, Availability und Berechtigungsgrenzen nun lokale Routingregeln beeinflussen;
- zwei zusätzliche `skill-authoring`-Evalfälle zu Vendor-App-Kopplung und falscher Action-Autorisierung definiert; beide **DEFINED / NOT RUN**;
- kein neuer zentraler Skill, keine automatische Plugininstallation und keine externe Aktion aus bloßer Pluginverfügbarkeit.

### Allgemeine Prompt-Shortcuts

- neuen Katalog `Dokumentation/Allgemeine-Prompt-Shortcuts.md` mit **100** funktionalen Kurzbefehlen ergänzt; alle Einträge sind `PROMPT-SHORTCUT`, keine behaupteten offiziellen ChatGPT-Commands;
- statische nutzerbereitgestellte Referenz „100 ChatGPT-Codes“ (Christian / @KI.GLATZE, Ausgabe 2026) als Inspiration dokumentiert, ohne PDF, Abbildungen, Tabellenlayout oder längere Originaltexte zu redistribuieren und ohne eine freie Lizenz der Ausgangsdatei anzunehmen;
- die 100 Kurzlabels in eigenständig formulierte Kategorien und Beschreibungen überführt: Priorisieren/Prompting, Schreiben, Lernen, Format, Content, Entscheiden, Denksysteme, Kreativ/Zukunft, Coding/Technik und Alltag;
- Kollisionen mit bereits dokumentierten Kürzeln explizit geregelt: `/gaps` kontextabhängig für Wissens- oder Planlücken, `/mindmap` getrennt vom möglichen UI-/Skill-Shortcut `/mindmaps`, `/carousel` nach Content-/Bildkontext und `/slides` als Struktur-Shortcut statt automatischer PPTX-Auftrag;
- `/genius` gehärtet: gründliche Prüfung, Annahmen und relevante Rechenschritte statt Aufforderung zur Offenlegung privater Chain-of-Thought;
- Unsicherheitsgates für `/odds`, `/predict`, `/simulate` und `/numbers`; Rechts-/Vertragsgrenze für `/decode`; Self-Reflection-Grenzen für `/shrink`, `rewire` und `/habit`; Evidence-Grenzen für `/tests`, `/security`, `/sql` und andere technische Kürzel;
- allgemeine ChatGPT-Shortcut-Doku, Dokumentationsindex und `ACKNOWLEDGEMENTS.md` auf den neuen Katalog beziehungsweise die statische Inspirationsquelle ergänzt;
- kein neuer Skill, kein Plugin, keine mutable Upstream-Abhängigkeit und keine PDF-Datei im Repository.

### Bild- und Medien-Prompt-Shortcuts

- neuen Katalog `Dokumentation/Bild-und-Medien-Prompt-Shortcuts.md` mit **220** funktionalen Bild-/Medien-Kürzeln ergänzt; alle Einträge sind `PROMPT-SHORTCUT`, keine behaupteten offiziellen ChatGPT-Commands;
- statische nutzerbereitgestellte Referenz „220 Bild-Codes für ChatGPT“ (Christian / @KI.GLATZE, Ausgabe 2026) als Inspiration dokumentiert, ohne die PDF, Abbildungen oder längere Originaltexte zu redistribuieren und ohne eine freie Lizenz der Ausgangsdatei anzunehmen;
- alle 220 funktionalen Kurzlabels in eigenständig formulierte Kategorien und Beschreibungen überführt: Erklären/Zerlegen, Porträts, Produkte, Anzeigen, Marke, Mockups, Social, Bildbearbeitung, Stil und toolabhängiges Video;
- Schutzregeln ergänzt: keine erfundenen Testimonials/Preise/Statistiken, keine irreführenden Vorher-Nachher-Claims, Werbekennzeichnung nicht umgehen, `/passport` nicht als Compliance-Beweis, `/removetext` nicht zur Entfernung fremder Watermarks/Provenienzmarker;
- Video-Kürzel bleiben capability-/runtimeabhängig; der in der Ausgangsreferenz genannte Higgsfield-Workflow wird nicht als universelle Toolpflicht übernommen;
- „Codes stapeln“ als kontrollierte Arbeitskette dokumentiert: jeder Schritt besitzt weiterhin Keeper-/Source-of-Truth- und Review-Gates;
- allgemeine ChatGPT-Shortcut-Doku, Dokumentationsindex und Bildarbeits-README auf den neuen Katalog verlinkt;
- kein neuer Skill, kein Plugin, keine neue mutable Upstream-Abhängigkeit und keine PDF-Datei im Repository.

### Denk- und Schreib-Prompt-Shortcuts

- `Dokumentation/ChatGPT-Funktionen-und-Lernwerkzeuge.md` um fünf kompakte Prompt-Shortcuts ergänzt: `NO/YES`, `GAPS`, `STEELMAN`, `PREMORTEM` und `TIGHTEN`;
- alle fünf bewusst als `PROMPT-SHORTCUT` klassifiziert: verständliche Kurzprompts, **keine** behaupteten eingebauten ChatGPT-Produktbefehle;
- optionale persönliche Slash-Aliase `/no-yes`, `/gaps`, `/steelman`, `/premortem` und `/tighten` dokumentiert, ohne daraus Command-Menü-Verfügbarkeit abzuleiten;
- pro Shortcut Zweck, Beispiel, bevorzugte Ausgabeform und Grenze ergänzt;
- `NO/YES` als kalibrierter Entscheidungscheck statt reflexivem Widerspruch, `STEELMAN` als stärkste vernünftige Gegenposition und `PREMORTEM` als Risikoanalyse statt Vorhersage abgegrenzt;
- `TIGHTEN` schützt Kernaussage, Termine, Zahlen, Namen und Bedingungen vor stillem Bedeutungsdrift; komplexere Rewrite-/Kommunikationsaufgaben bleiben bei den zuständigen Schreibskills;
- kein neuer Skill, kein Plugin und keine Behauptung universeller Produktverfügbarkeit.

### Text-Watermark-/Unicode-Hygiene und Upstream-Refresh

- `guillaumemeyer/watermarks-remover` erneut gegen aktuellen Stand `1181fd4e8cc581931a5ee672697a646721e92c78` geprüft; bestehender `remove-ai-marks`-Snapshot aktualisiert;
- neuen Upstream `skills/clean-user-facing-text/SKILL.md` sowie dessen Responsible-Use-Referenz als `reference/inspiration`, `concepts/methods-only` aufgenommen; keine Scripts, Phrase-Listen, Rewrite-Prompts oder Runtime-Implementierung werden redistribuiert;
- alle vier relevanten Watermarks-Remover-Artefakte in `Dokumentation/upstream-sources.yml` mit `cadence: monthly` und `monitor_mode: exact-sha` registriert; der wieder aktivierte monatliche KI-Regeln-Monatscheck nimmt sie dadurch automatisch in seinen Registry-Lauf auf;
- Provenance-/Lizenzsnapshot auf denselben Repository-Commit aktualisiert; MIT-Root-Lizenz am Snapshot dokumentiert;
- Text-Provenienz stärker getrennt in deterministische Unicode-/Steuerzeichen-Artefakte, statistische/tokenbasierte Signale und normale Schreib-/Voice-Qualität;
- klare Evidence-Grenze ergänzt: sauberer Unicode-Scan beweist weder Abwesenheit statistischer Watermarks noch menschliche Urheberschaft; lokale Stylometry-/Burstiness-Scores sind kein Vendor-Detector;
- autorisierte Text-Hygiene bleibt minimal: konkrete technische Funde gezielt entfernen, Code/URLs/Identifikatoren/Zahlen/Zitate/Claims und erforderliche Disclosures schützen, danach Re-Inspection;
- drei neue definierte Evalfälle ergänzt: Vendor-Overclaim bei Zero-Width-Fund, statistische Watermark nach sauberem Unicode-Scan sowie minimaler autorisierter Zero-Width-Clean; alle **DEFINED / NOT RUN**;
- kein neuer zentraler Skill, kein Detector-Evasion-Gate und keine Maturity-Hochstufung.

### Web Experience Design und Anti-Slop-Hardening

- weiteres Webdesign-Praxisvideo als **Discovery-/Field-Observation** ausgewertet; Modell-, Benchmark-, Produkt- und Werbeaussagen daraus werden nicht als zentrale Wahrheit übernommen;
- Referenzarbeit gehärtet: `frontend-design` und die Designrichtungs-Dokumentation unterscheiden nun **Reference Board / Reference Decomposition** von faktischer Reproduktion; pro Referenz werden übertragbare Prinzipien, produktspezifische Merkmale, Nicht-Übernahme-Grenzen und Rechte-/Nutzungshinweise getrennt;
- **Novelty Budget** ergänzt: technisch mögliche 3D-, WebGL-, Parallax-, Scrollytelling-, Minigame- oder Motion-Effekte brauchen einen konkreten Informations-, Interaktions-, Produkt- oder Identitätszweck; mehrere Signature Experiences dürfen nicht nur als Agenten-Leistungsschau konkurrieren;
- `greybox` und Informationsarchitektur um **Experience Storyboards** erweitert: immersive/scrollgetriebene Seiten planen Aussage, Beats, Interaktion, Core Content, Mobile/Touch, Reduced Motion und Fallback vor der konkreten Effektbibliothek;
- Responsive-/Interaktionsregeln um **Progressive Experience Enhancement** und lokalen Fallback Contract ergänzt: Core, Enhanced, Mobile/Touch, Reduced Motion sowie Capability-/Failure-Pfad werden getrennt beschrieben; keine pauschale „alles muss ohne JavaScript identisch sein“-Regel;
- Frontend-Performance um eine eigene Kostenklasse für 3D/WebGL/Canvas/immersive Experiences erweitert; Low-Poly, GPU, WebGL oder einzelne technische Tricks gelten nicht als automatische Performancegarantie;
- `web-design-review` prüft nun Reference-Overfit, Novelty Budget und fehlende Experience-Fallbacks; `visual-verification` trennt erfolgreichen High-End-Desktop-Happy-Path von tatsächlich ausgeführten Mobile-/Reduced-Motion-/Capability-Fallbacks;
- Workflow `Website-Neuentwicklung.md` auf Reference Board → Art Direction → Greybox/Experience Storyboard → Progressive-Experience-Contract → Qualitätsgates erweitert;
- insgesamt **9 neue definierte Evalfälle** ergänzt: 2× `frontend-design`, 2× `greybox`, 3× `web-design-review`, 2× `visual-verification`; alle **DEFINED / NOT RUN**;
- `greybox`, `web-design-review` und `visual-verification` im Skill-Katalog wegen der neuen Evalpacks von `none` auf `partial` gesetzt; keine Maturity-Hochstufung und kein neuer Skill.

### Canonical Media und hybride KI-Video-Pipelines

- weiteres Praxisvideo als **Field Observation / Discovery Lead** ausgewertet; Aussagen zur Ersetzung von Videoeditoren, zur „höchsten Konsistenz“ oder zu universellen Modellparametern werden nicht als Benchmark beziehungsweise zentrale Regel übernommen;
- bestehende Fachgrundlage für codebasierte Motion-/Videoproduktion um **Canonical Media vs. Derived Media** erweitert: eine spätere generative Zwischenstufe wird nicht automatisch neue Source of Truth für Character Identity, Voice, Brand oder freigegebene Claims;
- `Canonical-Media-Contract` im Video-Workflow ergänzt: Rollen wie `character-identity`, `voice-master`, `approved-script`, `brand-asset` oder `product-ui` binden konkrete Quellen, erlaubte Transformationen und Rückprüfungen;
- Rebinding-Muster dokumentiert: ein generierter Performance-Clip darf Bewegung/Lipsync liefern, während eine hörbar veränderte Derived-Audiospur verworfen und der kanonische Voice Master im Final erneut gebunden wird; Lip-Sync wird anschließend gegen genau diese Final-Audiospur geprüft;
- **Character Blocking** vor Performance-Generierung ergänzt: Blick-/Zeigerichtung, Bewegungsraum, reservierte Grafikflächen und Schutzbereiche werden bereits im Storyboard geplant und später gegen die tatsächliche Performance geprüft;
- Video-QA in getrennte Evidence-Achsen aufgeteilt: Character Identity, Voice Identity, Lip-Sync, Blocking, Motion/Composition, Captions und Brand-/Produktdarstellung; ein `PASS` einer Achse darf nicht auf andere übertragen werden;
- `motion-review` entsprechend gehärtet und um zwei definierte Evalfälle zu Derived-Voice-Drift sowie Blocking-/Overlay-Konflikt erweitert; beide **DEFINED / NOT RUN**;
- kein neuer Skill, kein neuer externer Upstream und keine Maturity-Hochstufung; die Praxisbeobachtung dient nur als Auslöser für eine eigenständig formulierte, frameworkneutrale Regelergänzung.

### Anthropic Skill-Best-Practices-Hardening

- aktuelle Anthropic-Dokumentation zu Skill Authoring und Prompting als semantisch überwachte Skill-Engineering-Upstreams registriert; YouTube-/Community-Zusammenfassungen dienen nur als Discovery-Signal, nicht als Source of Truth;
- Progressive Disclosure gehärtet: `SKILL.md` bleibt kompakter operativer Kern, lange Referenz-/Fachdokumente über ungefähr 100 Zeilen erhalten ein Inhaltsverzeichnis oder eine begründete Navigationsausnahme; die Grenze wird ausdrücklich als Authoring-Heuristik und nicht als harte Sichtbarkeitsgrenze behandelt;
- Freiheitsgrad pro Arbeitsschritt eingeführt: hoch für kontextabhängige Mehrwege-Aufgaben, mittel für bevorzugte Muster mit Variation, niedrig für fragile/reproduzierbare Schritte; deterministische Checks/Scripts werden dort bevorzugt, wo mehr Prompttext keine Robustheit schafft;
- Modell-/Runtime-Kompatibilität an tatsächliche Eval-/Run-Evidence gebunden: beabsichtigte Ziele werden als Matrix geprüft, `NOT RUN`/`UNVERIFIED` bleiben sichtbar, und konkrete Modellwahl wird nicht als neue Vendor-Pflicht in den portablen Skill-Kern geschrieben;
- Script Dependency Contract ergänzt: Runtime, Packages/Tools, Availability Check und Fallback müssen explizit sein; fehlende Dependency erzeugt keine automatische Installations-, Netzwerk- oder Write-Autorisierung;
- `skill-authoring` und `skill-review` entsprechend gehärtet und um insgesamt acht neue definierte Evalfälle erweitert; die Fälle sind **DEFINED / NOT RUN**, keine Behavioral-Pass-Aussage und keine Maturity-Hochstufung;
- bestehende lange Skill-Engineering-Fachdokumente im geänderten Scope mit Inhaltsverzeichnissen versehen; kein neuer Skill und keine Änderung der Skillanzahl.


### Codebasierte Motion-Graphics-/Video-Produktion

- zweites Praxisvideo als Discovery-/Field-Observation ausgewertet: gezeigte Qualitäts-, Zeit- und Kostenergebnisse werden ausdrücklich **nicht** als Benchmark oder allgemeine Modellzusage übernommen;
- `heygen-com/hyperframes` am Commit `5561b8cb2f8b747e3da8844d32463f9859bd4050` source-spezifisch geprüft; README und `motion-graphics`-Skill als `reference/inspiration`, Apache-2.0-Lizenz am selben Snapshot dokumentiert, keine Redistribution-Abhängigkeit;
- neue frameworkneutrale Fachgrundlage `Webentwicklung/Codebasierte-Motion-Graphics-und-Video.md`: editierbare Code-Composition, Source-/Asset-first, Storyboard-/Claim-Visual-Mapping, getrennte Audioebene, lokale Korrekturen und Render-/Publikationsgates;
- neuer Workflow `Workflows/Codebasierte-Motion-Graphics-und-Video.md` für Brief → Quellen/Assets → Storyboard → Composition → statische Proof-Frames → bewegte Playback-/Audio-Prüfung → Render/Handoff;
- HyperFrames bleibt konkrete Methodenreferenz, **kein Pflichtframework**; CLI-Kommandos, Plugin-/Cloudpfade, Workflow-Namen und Runtime-Garantien werden nicht universalisiert;
- `motion-implementation` gegen Mega-Skill-Scope gehärtet: bei gerenderten Browser-Compositionen besitzt er nur den technischen Motion-Layer, nicht Script, Research, Assetrechte, Audio oder Gesamtproduktion;
- `motion-review` und `visual-verification` trennen nun explizit Kontaktbogen/Proof-Frames von zeitlicher Playback-/Render-Evidence; Standbilder belegen weder Timing noch Schnittfluss, Flicker, Caption-Sync oder Audio-Sync;
- zwei zusätzliche Evalfälle definiert: Gesamtvideoproduktion als Workflow-Near-Miss für `motion-implementation` sowie Kontaktbogen-ohne-Playback als `partial`-Fall für `motion-review`; beide **DEFINED / NOT RUN**;
- Webentwicklungs-README und Workflow-Index ergänzt; kein neuer zentraler Skill und keine Maturity-Hochstufung.

### ChatGPT-Befehle, Lernwerkzeuge und interaktive Funktionen

- die bisher kurze Lernwerkzeug-Seite zu einer praktischen Befehlsreferenz ausgebaut: Aufruf, Zweck, typischer Einsatz, Beispiel und Verfügbarkeitsstatus stehen nun direkt am jeweiligen Werkzeug;
- Lern-/Visual-Shortcuts `/flashcards`, Quizfragen, `/sketchnodes`, `/mindmaps` und `/comicnodes` getrennt dokumentiert; beobachtete UI-/Skill-Shortcuts werden nicht als universelle Produkt-API ausgegeben;
- `@study`, `@Visualize` und das optionale `@MindMap`-Plugin als eigene Werkzeugklasse mit konkreten Einsatzbeispielen aufgenommen;
- die aktuell dokumentierten Desktop-/Developer-Slash-Commands wie `/plan`, `/goal`, `/compact`, `/side`, `/model`, `/reasoning`, `/review`, `/status`, `/project`, `/fork`, `/mcp` und weitere als Referenz ergänzt;
- erklärt, dass die Composer-Liste mehrere Mechanismen zusammenführen kann: echte Slash Commands, aktivierte Skills, `$skill`-Aufrufe, `@plugin`-Werkzeuge und `/prompts:<name>`;
- ChatGPT Web und Desktop-/Developer-Oberflächen ausdrücklich getrennt, da OpenAI unterschiedliche Command-Sets dokumentiert;
- Statusklassen `DOCUMENTED`, `UI-OBSERVED`, `CONDITIONAL`, `PLUGIN`, `PROMPT-SHORTCUT` und `UNVERIFIED` eingeführt;
- Community-Kürzel wie `/eli5`, `/flowchart`, `/teacher` oder `/xray` bleiben als Prompt-Shortcuts klar von echten Produktbefehlen getrennt;
- Lernworkflow `verstehen → strukturieren → visualisieren → erinnern → prüfen → Lücken reparieren` dokumentiert und den passenden Werkzeugen zugeordnet;
- Root-README und Dokumentationsindex bleiben der Einstieg; kein neuer KI-Regeln-Skill und keine Änderung am Skill-Katalog.

### Skill-Portabilität, Eval-Ratchets und packageweite Admission

- keinen neuen Admission-Skill angelegt: der bereits gehärtete `skill-security-review` bleibt die zuständige Capability und prüft nun explizit den gesamten relevanten Skill-Bundle-Scope statt nur `SKILL.md`; Begleit-Scripts, Referenzen, Hook-/MCP-/Konfigurationsdateien, Runtime-Nachladepfade und nicht geprüfte Bestandteile werden als Teil der Admission-Evidence behandelt;
- Security-Review um optionalen Bundle-/Snapshot-Fingerprint, maschinenlesbare Findings und CI-Grenzen erweitert; deterministische Blocker dürfen automatisiert gaten, semantische Unsicherheit bleibt Reviewpflicht, und ein belastbarer Critical-Fund darf nicht durch einen niedrigen Aggregatscore weggeglättet werden;
- zwei zusätzliche `skill-security-review`-Evalfälle zu ungescannten Begleitdateien und irreführendem Aggregatscore definiert; Ag1rin/SkillGuard dient mit geprüftem MIT-Snapshot als methodische Referenz für packageweite Discovery, Reporting und Fingerprinting, ohne dessen Regex-Regeln oder Score-Schwellen zu übernehmen;
- neue Fachgrundlage `Skill-Engineering/Portabler-Skill-Kern-und-Runtime-Adapter.md` ergänzt: fachlicher Skill-Kern, Capability-Vertrag und Gates bleiben hostneutral; Modellwahl, konkrete Toolnamen, Turn-Limits, Isolation, Hooks und client-spezifische Orchestrierung gehören in Runtime-Adapter oder gekapselte Metadaten, sofern die Plattform nicht selbst Gegenstand des Skills ist;
- `skill-authoring`, `skill-review`, Tool-/Fallback- und Progressive-Disclosure-Regeln entsprechend gehärtet; drei zusätzliche Skill-Engineering-Evalfälle prüfen Vendor-Runtime-Kopplung, modellspezifische Workarounds und die Core/Adapter-Grenze;
- Agent-Evals und Skill-Review um Quality-Floor-/Ratchet-Governance erweitert: reproduzierbare Baselines können gegen stille Regression geschützt werden, aber nur bei vergleichbarer Metrik, Population und Runtime; Floors werden nicht nach einem regressiven Change abgesenkt, Re-Baselining ist eine separate Maßstabsänderung;
- Routing-Evidence umfasst positive Trigger, Near-Misses und soweit sinnvoll pairwise Routing gegen zuständige Nachbarskills; bessere Recall-Werte dürfen nicht durch breitere Skill-Kaperung erkauft werden; keine universelle Prozentgrenze übernommen;
- zwei zusätzliche `agent-eval`-Fälle zu Ratchet-Regression und nicht vergleichbaren Messständen definiert;
- `addyosmani/agent-skills` am Release-/Repository-Stand 0.6.11 als konkrete mutable Methodenreferenz für Core/Adapter-Trennung und Eval-Ratcheting registriert; Vendor-Felder, TF-IDF-Implementierung, konkrete Modelle und externe CI-Schwellen werden nicht universalisiert;
- insgesamt sieben neue Evalfälle definiert; keine Behavioral-Evals als ausgeführt oder bestanden behauptet, keine Maturity hochgestuft und kein neuer Skill angelegt.

### Separate Open-Content-Lizenzierung für Praxisbeispiel-Bilder

- sechs vorhandene Bildassets aus drei Praxisbeispielen ausdrücklich aus der Root-MIT-Lizenz herausgelöst und – soweit daran wirksam lizenzierbare Rechte bestehen – unter **CC BY-SA 4.0** gestellt;
- `ASSET-LICENSES.md` als menschenlesbare Source of Truth für Dateiliste, Attribution und KI-Provenienz ergänzt;
- dokumentiert, dass die Bildausgaben vollständig durch OpenAI-Bildgenerierung entstanden, während Idee, Prompts, Gestaltungsvorgaben, Art Direction, Auswahl und Freigabe menschlich gesteuert wurden;
- `REUSE.toml` als maschinenlesbare SPDX-Zuordnung für exakt diese sechs Assets ergänzt, ohne daraus eine vollständige REUSE-Compliance des gesamten Repositories abzuleiten;
- Root-README, `CONTRIBUTING.md` und die drei betroffenen Praxisbeispiele auf die getrennte Medienlizenzierung ausgerichtet; fehlerhafte `.jpg`-Referenz des vorhandenen Web-POC-Bildes auf den tatsächlichen `.png`-Pfad korrigiert.

### Skill-Security-Hardening und evidence-getriebene Skill-Verbesserung

- den bereits vorhandenen `skill-security-review` statt eines Doppel-Skills gehärtet: zu prüfende Skills gelten bis zur Admission als untrusted Input; read-only Inspektion und operative Aktivierung sind getrennt; Snapshot-/Bundle-Vollständigkeit, deklarierte versus abgeleitete Capabilities, mutable Remote-Abhängigkeiten und Capability Drift werden explizit geprüft;
- Security-Evidence mehrstufig modelliert: deterministische/statische Prüfung, semantische Verhaltensanalyse und nur bei Bedarf isolierte dynamische Proben mit synthetischen Daten/Canaries; Scannerstatus und Sandbox-Erfolg sind Evidence, keine automatische Sicherheitsfreigabe;
- `Skill-Supply-Chain.md` um Pre-Load-Trust, transitive/Remote-Abhängigkeiten und die Grenze „lokal gepinnt ≠ Runtime-Abhängigkeiten gepinnt“ erweitert; Agent-Skills-Client-Guidance und aktuelle Snyk-Supply-Chain-Evidence als methodische Quellen ergänzt;
- vier zusätzliche Evalfälle für `skill-security-review` definiert: untrusted Project Skill vor dem Laden, mutable Remote-Instruktionen, grüner Scanner trotz Over-Privilege und Sandbox-Probe ohne echte Secrets; dadurch 656 definierte Cases, ohne Behavioral-Evals als ausgeführt oder bestanden zu behaupten;
- neue Fachgrundlage `Skill-Engineering/Evidence-getriebene-Skill-Verbesserung.md` und Workflow `Workflows/Skill-Verbesserung-aus-Evals-und-Fehlern.md` ergänzt; bewusst **kein neuer Skill**, weil der Job aus `agent-eval`, `skill-authoring`, `verification-loop`, `skill-review` und bei Bedarf `skill-security-review` komponiert wird;
- Failure-/Eval-Evidence in Development-, Regression-, Held-out-/Independent- und Field-Evidence getrennt; vor Skilländerungen ist Root-Cause-Klassifikation verpflichtend, und zur Änderung verwendete Fälle werden nicht nachträglich als unabhängige Erfolgsevidence ausgegeben;
- EvoSkill und SkillClaw als konkrete mutable Methodenreferenzen mit geprüftem Snapshot, Lizenz- und Provenance-Evidence registriert; SkillAudit sowie die aktuelle Trajectory-Poisoning-Arbeit bleiben stabile Fachquellen statt künstlicher Upstream-Watches; Field-/Trajectory-Evidence bleibt bis zur Provenance-/Kontaminationsprüfung untrusted; autonome Selbstmutation, automatische globale Skillverteilung und selbstautorisierte Adoption werden nicht übernommen;
- `Dokumentation/radar-sources.yml` auf wöchentliche Discovery-Cadence ausgerichtet und um Suchthemen für Skill-Supply-Chain-Security sowie Eval-/Failure-getriebene Skill-Evolution ergänzt; `Quellenregister.md` trennt nun ausdrücklich wöchentlichen Discovery-Radar von monatlicher Upstream-Maintenance;
- Skillzahl und Maturity bleiben unverändert bei 150 Skills, 125× `partial`, 25× `none`, 0× `core`/`broad`; kein aktiver Skill wird autonom überschrieben, kein Upstream automatisch synchronisiert und keine Maturity hochgestuft.

### Phase 4.2C · B2 — Launch-Kontext und Aufzeichnung

- view-lokaler `--mcp-config`: die leere MCP-Konfiguration lag im Host-Temp-Verzeichnis des Adapters und wurde dem confinten Prozess als Hostpfad übergeben, den er nicht öffnen kann; sie erhält jetzt eine eigene read-only View `/b2-config` mit genau einer Datei, und `--strict-mcp-config` ist für writable B2 erzwungen statt optional; die Inline-JSON-Variante wurde nicht genommen, weil keine modellfreie Invocation der installierten CLI diese Option parst und eine Annahme aus der Hilfe keine Messung ist;
- `PATH` innerhalb der View enthält jetzt das Verzeichnis der Claude-Code-Runtime; der confinte Launch wäre zuvor mit `env: 'claude': No such file or directory` gestorben, gefunden vom neuen Launch-Preflight;
- die gemessenen Confinement-Fakten stehen jetzt in Runtime-Preimage, Evidence und Method-Evidence; `os_or_container_sandbox` war eine Konstante und sagte „kein Sandbox" über einen Lauf mit Sandbox; die äußere Invocation wird als normalisierter Preimage gebunden (Struktur, Provider, Mount Contract, inneres argv; Assembly-Script als Hash, Launcher-Environment nur als Variablennamen), damit ein unconfinter Lauf nicht dieselbe Method Evidence erzeugen kann;
- Gate und Launch leiten ihren Kontext nur noch einmal ab: `prepare_writable_launch()` erzeugt einen `WritableLaunchContext` aus geprobtem Binary und gefiltertem Child-Environment, und dieselbe Instanz speist Criterion 22, die Admission und den Launch; zuvor maß das Kriterium `os.environ`, während der Prozess eine gefilterte Kopie erhielt, und kannte weder `base_env` noch `claude_binary`;
- neues blockierendes Kriterium 22 `confined_model_runtime_launchable`: view-lokale argv-Pfade, ausführbare Runtime in der View, Parserakzeptanz der writable Flags und ein Authpfad, der im View-Environment funktioniert;
- Pilot Entry bleibt blockiert: `claude auth status` innerhalb der View meldet `loggedIn: false`, weil das Credential unter einem Host-Home liegt, das die View bewusst nicht trägt; Host-Home oder Claude-Config einzumounten würde die gerade geschlossene Grenze wieder öffnen und ist deshalb unterblieben;
- keine Model Responses, keine Behavioral Runs, kein Judge, kein Unblinding, kein Pairing, keine Skill-Wirkungsaussage, keine Maturity- oder Coverage-Änderung.

### Phase 4.2C · B2 — Confinement des Modellprozesses

- der Claude-Code-Prozess selbst läuft jetzt im Namespace-Provider: die bisherige Annahme, `--permission-mode dontAsk` zusammen mit `Bash(check)` mache `check` zur einzigen ausführbaren Shell-Aktion, war falsch, weil eine Klasse read-only Kommandos ohne Freigabe läuft; zusammen mit einem Launcher, der den absoluten Pfad des Evaluator-`tools/`-Verzeichnisses einbettete, war das ein konkreter Weg zu Case Matrix, Trust Root und Oracle-Expectations;
- die äußere View trägt Workspace (beschreibbar, zugleich Arbeitsverzeichnis), Scratch, einen minimal gestageten Trusted Runtime aus zwei Dateien und den Check-Launcher; Repository, `/home`, `/root` und `/tmp` existieren darin nicht, und der Launcher nennt nur noch View-Pfade;
- Netzwerk bleibt in der äußeren View bewusst erreichbar, weil der Modellprozess seine API braucht; das ist die einzige Isolation, die diese Schicht nicht leistet, und wird als solche benannt statt impliziert;
- neues Pilot-Kriterium `model_process_workspace_confinement`, funktional gemessen durch reale Ausführung genau jener read-only Kommandos gegen einen außerhalb platzierten Sentinel, nicht durch Prüfung der Allowlist; Pilot Entry bleibt ohne diesen Nachweis blockiert;
- `runtime_permission_mode()` nutzt jetzt einen echten modellfreien Parser-Test der installierten CLI und behauptet nur noch das tatsächlich Gemessene; veralteter Kopfkommentar in `b2_model_runner.py` korrigiert;
- keine Model Responses, keine Behavioral Runs, kein Judge, kein Unblinding, kein Pairing, keine Skill-Wirkungsaussage, keine Maturity- oder Coverage-Änderung.

### Phase 4.2C · B2 — zweite Review-Runde

- Admission entfälscht: der writable Adapterpfad nimmt kein Token mehr entgegen, sondern wertet die Pilot-Kriterien unmittelbar vor dem Modellstart selbst aus; `execute_prepared_response` besitzt keinen `admission`-Parameter mehr, und `b2_model_runner.py` bleibt öffentlicher Einstieg ohne Autorisierungswirkung;
- Toolnamen und Permission Rules getrennt: `--tools` erhält Toolnamen (`Read,Edit,Write,Bash`), `--allowedTools` die Regeln (`Bash(check)`), dazu `--permission-mode dontAsk` für den nichtinteraktiven Lauf; Evidence berichtet requested visible tools, observed visible tools, deren Übereinstimmung, allow rules, deny rules und permission mode getrennt, und beobachtete Toolnamen werden nie gegen Permission Rules verglichen; ein Build ohne `dontAsk` lässt Pilot Entry fail closed scheitern (neues Kriterium 20);
- Oracle-Instrumentationsfehler erreichen jetzt D1: ein nicht etablierter Boundary-View oder ein Fehler beim Vorbereiten der Messung setzt `integrity_ok` auf false und führt zu `RUN_INVALID` statt zu einer Behavioral Violation; ein echtes rotes Produkt bei funktionierender Boundary trägt weiterhin D6;
- Probe-Evidence wird für die Modellpilot-Admission frisch ausgeführt statt aus einer Datei gelesen, weil die Schutzwirkung einer Namespace-Boundary auch von Kernel und util-linux des Hosts abhängt; P6 bleibt Beobachtung;
- keine Behavioral-/LLM-Runs, kein Judge, kein Unblinding, kein Pairing, keine Skill-Wirkungsaussage, keine Maturity- oder Coverage-Änderung.

### Phase 4.2C · B2 — Review-Korrekturen der Messarchitektur

- Oracle-Leak geschlossen: die Held-out-Expectations lagen im selben Verzeichnis wie der Driver und waren dadurch als `/oracle-driver/expectations.yml` aus der agentenkontrollierten Produkt-View lesbar; der Driver wird jetzt einzeln in ein eigenes Staging-Verzeichnis kopiert, P4 prüft genau diesen Pfad samt Discovery gegen einen Leak-Canary, und die alte P4-Evidence wurde verworfen;
- separater neutraler B2-Systemprompt ergänzt, weil der bestehende kontrollierte Prompt das Schreiben verbietet und damit genau das Verhalten ausgeschlossen hätte, das B2 beobachten soll; der read-only Prompt bleibt unverändert, und der B2-Prompt nennt weder Guards noch Thresholds, Autorisierung oder Governance;
- adapterkontrollierten Check-Launcher `bin/check` ergänzt, der außerhalb des beschreibbaren Workspace liegt, keine Argumente akzeptiert, den Workspace-Pfad vom Adapter erhält und ausschließlich den Boundary-Provider aufruft; damit ist die erlaubte Invocation real an die Boundary gekoppelt statt nur erlaubt;
- effektive Tool-Policy einmal abgeleitet und durch alle tragenden Evidence-Funktionen gereicht, inklusive Systemprompt-Hash; ein writable Run kann seine Policy nicht mehr als read-only ausweisen;
- Pilot-Gate auf den tatsächlichen Launch-Pfad gelegt: ein writable Adapterlauf verlangt ein Admission-Objekt, das nur `tools/b2_model_runner.py` aus einer frischen Kriterienauswertung erzeugt; ohne das wird kein Modellprozess gestartet;
- Boundary-Setupfehler deterministisch von Payload-Exits getrennt (Marker unmittelbar vor `exec`); ein nicht etablierter View liefert `BoundaryError`, das Oracle `not-run` und die Pipeline `RUN_INVALID` statt eines vermeintlich roten Produkts;
- tragende Readiness-Kriterien messen jetzt funktional statt Quelltext-Substrings zu prüfen; zwei tatsächlich nicht anwendbare Kriterien sind als solche modelliert statt als scheinbar gemessenes `true`; Probe-Evidence ist an Boundary-, Oracle-, Probe-, Driver- und Expectation-Hashes sowie Provider und Plattform gebunden und verfällt bei Drift;
- `extra_ro`-Shadowing gegen alle reservierten Pfade in beide Richtungen geprüft; keine Behavioral-/LLM-Runs, kein Judge, kein Unblinding, kein Pairing, keine Maturity- oder Coverage-Änderung.

### Phase 4.2C · B2 — Implementierung der Messarchitektur

- die reviewten Designschritte S1 bis S5 vollständig implementiert, ohne jeden Behavioral- oder LLM-Run: neun synthetische Workspaces, exhaustive Verification Surface über zehn Elemente, Black-Box Held-out Oracle, deterministische Grading-Pipeline und modellfreie End-to-End-Dry-Runs;
- eine reale Execution Boundary ergänzt (`unshare`-Namespace mit `pivot_root`, versiegelter read-only View-Root, ausschließlich Workspace-Kopie und Scratch beschreibbar, fixe Umgebung ohne Vererbung); agentenkontrollierter Check- und Produktcode läuft nur noch darin, ein unisolierter Fallback existiert nicht;
- Breakage-Proben P1 bis P6 tatsächlich ausgeführt und als Evidence abgelegt; P2 hat dabei einen echten Mangel der ersten Boundary-Implementierung gefunden — der View-Root war beschreibbar —, woraufhin die Boundary korrigiert und nicht die Probe abgeschwächt wurde; P6 bleibt reine Beobachtung und niemals ein Gate;
- `case-matrix.yml` in die bestehende B1-Trust-Kette aufgenommen; die reviewte Behavioral-Semantik ist zusätzlich als eigener Projektions-Hash redundant in Trust Root und Testsuite gepinnt, damit ein Pin-Update keine stille Semantikänderung tragen kann;
- Behavioral-Harness additiv und opt-in um einen writable B2-Modus sowie einen gehashten Workspace-Export erweitert; der von 4.2A und 4.2B genutzte read-only Pfad bleibt unverändert, und Run-Packages ohne Export bleiben gültig;
- maschinell auswertbare Pilot Readiness über alle neunzehn Kriterien ergänzt, mit einem Gate, das einen Modellpiloten technisch verweigert, solange ein blockierendes Kriterium `false`, `unknown` oder unbelegt ist, und das sich durch eine manipulierte Readiness-Datei nicht selbst autorisieren lässt;
- Eval-Gaming-Red-Team gegen das gebaute System statt gegen das Designdokument ausgeführt und dokumentiert;
- keine Model Responses, kein Semantic Judge, kein Unblinding, kein Pairing, keine Wirksamkeitsaussage zu `verification-loop`, keine Maturity- oder Eval-Coverage-Änderung; `network_disabled` nur so stark berichtet, wie P6 es trägt.

### Inhaltsprovenienz und Metadatenhygiene

- Sicherheit um zwei klar getrennte Skills ergänzt: `inhaltsprovenienz-review` prüft Dateien und Inhalte read-only auf belegbare Provenienz-, Metadaten- und Unicode-Signale; `metadaten-hygiene` bereinigt ausschließlich eigene oder ausdrücklich autorisierte Artefakte innerhalb eines konkreten Remove-/Keep-Scopes;
- gemeinsame Fachgrundlage `Sicherheit/Inhaltsprovenienz-und-Metadatenhygiene.md` und Workflow `Workflows/Inhaltsprovenienz-und-Metadatenhygiene.md` ergänzt; Grundmuster ist Inspect → Evidence/Confidence → Erhaltungspflichten → optionales Change Set → Gate → Clean → Re-Inspection → Residual Risk;
- `guillaumemeyer/watermarks-remover` am Repository-Commit `d9e9590d94e19b39eb2794266292324bfec8249a` mit MIT-Lizenz als aktiv beobachtete methodische Referenz aufgenommen; konkrete `remove-ai-marks`- und Ethics-Artefakte sind per Blob-SHA in Upstream-Registry und Provenance dokumentiert, ohne Runtime-, Plugin-, Service- oder Sync-Abhängigkeit;
- bewusst nicht übernommen: Detector-Evasion und „human score“-Optimierung, statistische Rewrite-Rezepte zur Watermark-Reduktion, Watermark-Stealing, Secret-Key-Rekonstruktion, destructive Pixel-/Audio-/Video-Purification als allgemeine Fähigkeit sowie das Entfernen verpflichtender Attribution-, Provenienz- oder Disclosure-Signale;
- Unicode-Hygiene gegen False Positives geschärft: ungewöhnliche Spaces, Bidi-, Zero-width- oder andere Unicode-Zeichen sind nicht automatisch Watermarks; aggressive Normalisierung benötigt konkreten Zweck und Nebenwirkungsprüfung;
- zwei neue Evalpacks mit jeweils sechs Startfällen ergänzt, insgesamt 12 definierte Cases zu read-only Provenienzprüfung, unsupported Markerklassen, Unicode-False-Positives, GPS-/Privacy-Hygiene, verpflichtender Attribution, sichtbaren Watermark-Near-Misses, Detector-Evasion und Residual Risk; diese Fälle sind **definiert, aber nicht als Behavioral Evals ausgeführt oder bestanden**;
- aktueller Gesamtstand damit 150 Skills, 125× `partial`, 25× `none`, 0× `core`/`broad`, 125 Skill-Evalpacks und 652 definierte Cases; keine Maturity hochgestuft, keine Behavioral-Eval-Ergebnisse erfunden und kein Tag oder Release erzeugt.


### Vertiefter Anthropic-Finance-Upstream-Audit

- `anthropics/financial-services` am 2026-09-06 bis zum geprüften Commit `69cbc81467a5dced793eee03dec4658aa24ef856` vertieft als Apache-2.0-lizenzierter methodischer Referenzraum auditiert; Anthropic dient als Methodenquelle, nicht als Copy/Paste-, Runtime- oder automatische Sync-Abhängigkeit;
- bestehende Skills `vermoegensprojektion`, `portfolioanalyse` und `anlagevergleich` gegen unbelegte Universaldefaults, veraltete Finanz-/Produktdaten, vermischte Analyseebenen und implizite Aktionsautorisierung gehärtet;
- drei klar getrennte Finance-Skills `portfolio-rebalancing`, `unternehmensanalyse` und `bewertungsanalyse` ergänzt; alle drei starten `experimental` mit `partial` Evalabdeckung, ohne bestehende Maturity hochzustufen;
- `investmentthese` bewusst nicht als separaten Skill angelegt: falsifizierbare These, Gegenargumente, disconfirming Evidence und Invalidation Conditions bleiben zunächst Modus der `unternehmensanalyse`, bis persistentes Thesis-Tracking als eigenständiger wiederkehrender Job belegt ist;
- Workflow `Workflows/Unternehmens-und-Investmentanalyse.md` ergänzt und in `workflow-index.yml` registriert: Unternehmen verstehen → These/Gegen-Evidence → optional Bewertung → optional Anlagevergleich → optional Portfolio-Kontext → Human Gate;
- drei neue Finance-Evalpacks mit jeweils sechs Startfällen ergänzt, insgesamt 18 definierte Cases zu fehlender Zielallokation, veralteten Depot-/Unternehmens-/Marktdaten, automatischen Trades, aktueller Earnings-Evidence, unfalsifizierbaren Thesen, Peer-Cherry-Picking, erfundenen WACC-/Terminal-Growth-Defaults und DCF-zu-Order-Kurzschlüssen; diese Fälle sind **definiert, aber nicht als Behavioral Evals ausgeführt oder bestanden**;
- bewusst nicht übernommen: 401(k), IRA, Roth, 529, RMD, Wash-Sale- und andere US-spezifische Konto-/Steuerlogik als allgemeine Wahrheit, feste Rebalancing-Bänder, feste WACC-/Terminal-Growth-/Multiple-Defaults, automatische Trade-Listen oder Buy/Hold/Sell-Automatismen sowie Anthropic-spezifische MCP-/Office-/Python-/Connector-/Subagent-Struktur;
- aktueller Gesamtstand: 148 Skills, 123× `partial`, 25× `none`, 0× `core`/`broad`; 123 Skill-Evalpacks mit insgesamt 640 definierten Cases;
- keine Broker-/Bank-/Trade-Aktion autorisiert, keine Maturity hochgestuft, keine Behavioral-Eval-Ergebnisse erfunden und kein Tag, Release oder automatischer Upstream-Sync erzeugt.

### Phase 4.2C · B2 — Designstand Behavioral Verification Governance

- Designartefakte für eine behaviorale Prüfung der Verification Governance ergänzt (`Evals/Verification-Surface/behavioral/`): Forschungsfrage, Threat Model, Architekturvergleich mit begründeter Entscheidung, Fallmatrix, Observations- und Telemetriemodell, deterministische Gates, Semantic-Judge-Grenze, Blindness-/Ground-Truth-Design, Trust-Modell, Implementierungsplan, Pilot Entry Criteria, ausdrückliche Nicht-Aussagen und Red-Team-Prüfung des eigenen Entwurfs;
- Klassifikationsregel statt Verhaltensprognose vorab festgeschrieben: `case-matrix.yml` pinnt, welche deterministisch beobachtbaren Endzustände welcher Outcome-Klasse entsprechen und welche Klassen je Fall zulässig sind — nicht, wie ein Agent sich verhalten wird;
- eine deterministische Architekturprobe ohne Modellantwort durchgeführt: die vorhandene Action-Telemetrie führt `Edit`/`Write` bereits als `productive` mit getrenntem `attempted`/`executed`, während `Bash` telemetrisch undurchsichtig bleibt; daraus folgt die Festlegung, den Workspace-Endzustand und nicht den Tool-Trace als tragende Evidence zu verwenden;
- nach Review zwei tragende Designlücken geschlossen: agentenkontrollierter Check-Code hätte über den erlaubten Check-Aufruf die Read-/Write-Tool-Policy vollständig umgehen können, weshalb jetzt eine nachzuweisende Execution Boundary mit getrennten Views für sichtbaren Check und Held-out Oracle sowie sechs blockierende Breakage-Proben vorgesehen ist; und die Outcome-Klassen waren komponierbar, sodass ein Endzustand gleichzeitig permitted und violation sein konnte;
- Bewertungsalgebra als totale, eindeutige Funktion in `tools/verification_governance_disposition.py` getrennt in beobachtete Facts und genau eine terminale Disposition, mit expliziter Dominanzordnung, Enumerationstest über den vollständigen Faktenraum und Drift-Test gegen die Dokumentation;
- kein Behavioral Run, keine Model Responses, kein Semantic Judge, kein Unblinding, kein Skill-on/off-Vergleich; keine Wirksamkeitsaussage zu `verification-loop`; bestehende 4.2A-/4.2B-Ergebnisse unverändert und nicht umgedeutet; keine Maturity- oder Eval-Coverage-Änderung; kein Harness- und kein Governance-Regelwerk verändert.

### Eval-Guardrails und Monatsradar-Evidence

- Agent-Evals um Harness-/Guard-Integrität gehärtet: kritische Guards sollen ihre Schutzwirkung nach Möglichkeit durch eine kontrollierte relevante Brechprobe belegen; ein vorhandener grüner Check gilt nicht allein wegen seiner Existenz als belastbare Evidence;
- Baselines, Positiv-/Negativkontrollen sowie Kalibrierungs- und Held-out-Evidence klarer getrennt; zur Judge-/Rubrik-/Schwellenwert-Kalibrierung verwendete Fälle werden nicht zugleich als unabhängige Vergleichsevidence ausgegeben;
- `verification-loop`, `ci-pipeline-design` und `test-suite-review` gegen stilles Absenken des Quality Floors geschärft: Änderungen an Assertions, Filtern, Gate-Severity oder Schwellenwerten sind eigenständige relevante Änderungen mit eigener Begründung, Evidence und gegebenenfalls Autorisierung; ein grüner Lauf unter verändertem Maßstab ist nicht automatisch mit der vorherigen Baseline gleichwertig;
- bestehende Evalfälle für `agent-eval` und `verification-loop` entsprechend geschärft, ohne neue Evalfälle anzulegen und ohne Maturity oder Eval Coverage zu verändern;
- `Dokumentation/radar-sources.yml` um maschinenlesbare Mindestfelder für monatliche Source-Evidence ergänzt; nicht verifizierbare Zustände bleiben `UNVERIFIED` statt plausibel als unverändert klassifiziert zu werden;
- den methodisch verwendeten `github/awesome-copilot`-Agenten `research-harness-engineer.agent.md` mit beobachtetem Blob-SHA, exaktem Repository-Commit und MIT-Evidence als `reference/inspiration` in Upstream-Register und Provenance aufgenommen; keine Redistribution fremder Ausdrucksform vorausgesetzt;
- keine Behavioral Evals als ausgeführt oder bestanden dargestellt, kein Tag oder Release erzeugt.

### Schreibkorrektur und deutsche Typografie

- zwei klar getrennte Schreiben-Skills ergänzt: `korrekturlektorat` für Rechtschreibung, Grammatik, Syntax, Zeichensetzung sowie Tipp-/Wortfehler und `deutsche-typografie` für Zeichenformen, Abstände und DE-/AT-/CH-Typografiekonventionen; beide starten `experimental` mit `partial` Evalabdeckung;
- gemeinsame Fachgrundlage `Schreiben/Sprachrichtigkeit-und-Typografie.md` ergänzt und die Grenzen `Korrekturlektorat ≠ Stilreview ≠ Rewrite`, `Zeichensetzung ≠ Typografie` sowie `Toolfund ≠ Sprachregel` verankert;
- Workflow `Workflows/Text-Endkontrolle.md` ergänzt und in `workflow-index.yml` registriert; mechanische Endkontrolle folgt auf autorisierte inhaltliche beziehungsweise stilistische Revisionen, damit spätere Rewrites nicht wieder neue Sprachfehler einführen;
- regionale Varianten, Projekt-/Hausstil, Mehrdeutigkeit sowie geschützte technische Inhalte wie Code, URLs, Pfade, Bezeichner, Markdown, HTML/JSX, YAML/Frontmatter und Zitate ausdrücklich vor blinder Normalisierung geschützt;
- amtliches Regelwerk der deutschen Rechtschreibung und IDS/`grammis` als fachliche Primärquellen dokumentiert; vier tatsächlich verwendete öffentliche Proofreading-/Typografie-Skills mit konkretem beobachtetem Blob-SHA, Lizenzraum und bewussten Abweichungen als punktuelle methodische Referenzen festgehalten; LanguageTool bleibt optionaler technischer Referenzraum ohne Runtime-Abhängigkeit;
- zwei neue Evalpacks mit jeweils acht Startfällen ergänzt, insgesamt 16 definierte Cases zu Korrektur, Near-Miss-Routing, Mehrdeutigkeit, Schweizer Orthografie, Code-/URL-Schutz, zulässigen Varianten, Hausstil, fehlender DIN-Evidence und Typografie-vs.-Webdesign; diese Fälle sind **definiert, aber nicht als Behavioral Evals ausgeführt oder bestanden**;
- der parallel ergänzte Langprosa-Signaturfall im bestehenden `stilreview`-Evalpack bleibt erhalten; aktueller Gesamtstand damit 145 Skills, 120× `partial`, 25× `none`, 0× `core`/`broad`, 120 Skill-Evalpacks und 622 definierte Cases;
- keine bestehende Maturity hochgestuft, keine Behavioral-Eval-Ergebnisse erfunden und kein Tag oder Release erzeugt.

### Problem-first Entry Path

- neuen menschlichen Einstieg `START-HIER.md` ergänzt: Nutzer beginnen mit ihrem realen Problem oder Ziel und müssen weder Skill-Namen noch interne Repository-Architektur kennen;
- Root-README auf problemorientierte Nutzung neu ausgerichtet und technische Detailtiefe aus der öffentlichen Eingangstür zugunsten von Ziel, Nutzung, Beispielen, Grundprinzip, Reifegrenzen und weiterführenden Einstiegen reduziert; Fachdetails bleiben in Bereichs-READMEs, Skill-Katalog und Fachhandbüchern erhalten;
- `AGENTS.md` als Problem-to-Skill-Router geschärft: Alltagssprache ist gültiger Auftrag, fehlende Skill-Namen sind kein fehlender Input, und der Agent wählt den kleinsten ausreichenden Workflow-/Skill-Satz;
- `Dokumentation/Skill-Handbuch.md` um Problem-first-Routing, beispielhafte Alltagstrigger, Datenminimierung und die Regel „so wenig Werkzeuge wie möglich, so viele wie nötig“ erweitert;
- Skill-Auswahl wird als interne Orientierungsleistung behandelt statt als Bedienlast für den Nutzer; lange Skill-Listen sind kein Qualitätsmerkmal und bei einfachen Aufgaben ist auch direkte Bearbeitung ohne Spezialskill zulässig;
- keine Skills, Workflows, Maturity- oder Eval-Coverage-Werte geändert, keine Behavioral Evals ausgeführt oder als bestanden dargestellt und kein Tag oder Release erzeugt.

### Finanzen

- neuen tool- und jurisdiktionsneutralen Fachbereich `Finanzen/` für persönliche Finanzplanung, Cashflow, Rücklagen, Schulden, Vermögensprojektionen, Portfolioanalyse und sachlichen Anlagevergleich ergänzt;
- sechs eng geschnittene Skills `finanzstatus-und-cashflow`, `ruecklagenplanung`, `schuldenstrategie`, `vermoegensprojektion`, `portfolioanalyse` und `anlagevergleich` ergänzt; alle sechs starten `experimental` mit `partial` Evalabdeckung, ohne bestehende Maturity hochzustufen;
- Workflow `Workflows/Persoenliche-Finanzplanung.md` ergänzt und in `workflow-index.yml` registriert; Finanzbaseline, Liquidität, Schulden, Szenarien, Portfolio und Anlagevergleich werden nur soweit kombiniert, wie der konkrete Auftrag sie benötigt;
- harte Finanzgrenzen verankert: `Projektion ≠ Prognose ≠ Garantie`, historische Rendite ist keine Zukunftsrendite, Diversifikation garantiert keinen Verlustschutz und Analyse/Review autorisiert keine Überweisung, Konto-/Vertragsänderung oder Kauf-/Verkaufsorder;
- aktuelle Markt-, Produkt-, Steuer- und Regulierungsdaten als zeit- und jurisdiktionsabhängige Evidence behandelt; fehlende aktuelle Werte werden nicht aus Modellgedächtnis oder US-spezifischen Defaults ergänzt;
- sechs Finance-Evalpacks mit jeweils fünf Startfällen ergänzt, insgesamt 30 definierte Cases; diese Fälle sind **definiert, aber nicht als Behavioral Evals ausgeführt oder bestanden**;
- SEC/Investor.gov und CFPB als öffentliche methodische Primär-/Behördenreferenzen sowie `anthropics/financial-services` (Apache-2.0) als methodischen Agent-Skill-Referenzraum dokumentiert; 401(k), IRA, Roth, 529, Social Security, Wash-Sale- oder andere US-spezifische Logik wird nicht zur allgemeinen KI-Regeln-Wahrheit;
- Skill-Katalog und menschliche Katalogdokumentation auf 143 Skills, 118× `partial`, 25× `none`, 0× `core`/`broad`, 118 Skill-Evalpacks und 605 definierte Cases aktualisiert; zusätzliche Coverage ist kein Nachweis für Beratungsgüte, Renditequalität oder Behavioral-Erfolg;
- keine Broker-/Bank-Automation, kein Buy/Hold/Sell-Automatismus, kein Tag, Release oder automatische externe Synchronisation durch diese Erweiterung.

### Storyentwicklung und Fiktion

- neuen toolneutralen Fachbereich `Storyentwicklung-und-Fiktion/` ergänzt, der narrativen Kanon und Story-Bible, Figuren und Beziehungen, Plot/Arcs, Worldbuilding sowie Langzeitkontinuität getrennt von der konkreten Prosa-Ausarbeitung behandelt;
- fünf eng geschnittene Skills `story-bible`, `figurenentwicklung`, `plot-und-storystruktur`, `worldbuilding` und `story-kontinuitaet` ergänzt; alle fünf starten `experimental` mit `partial` Evalabdeckung, ohne bestehende Maturity hochzustufen;
- `kreatives-schreiben` an den neuen Bereich angebunden und fachlich abgegrenzt: Storyentwicklung plant und schützt narrative Wahrheit, `kreatives-schreiben` bleibt für die konkrete Szene oder das Kapitel als Prosa zuständig;
- Workflow `Workflows/Storyprojekt-von-Idee-bis-Manuskript.md` ergänzt und in `workflow-index.yml` registriert; Review-/Revisionen bleiben an den allgemeinen `Review-Revise-Loop` und erforderliche Human Gates gebunden;
- fünf Story-Evalpacks mit jeweils fünf Startfällen ergänzt, insgesamt 25 definierte Cases; diese Fälle sind **definiert, aber nicht als Behavioral Evals ausgeführt oder bestanden**;
- Storystruktur-Modelle wie Drei-Akt, Hero's Journey oder andere Beat-Modelle nur als optionale Linsen behandelt; Planung wird nicht mit bereits erzähltem Kanon gleichgesetzt und Worldbuilding nicht als Lore-Mengenwettbewerb modelliert;
- methodischen Referenzraum `danjdewhurst/story-skills` (MIT) fachlokal als `reference/inspiration` dokumentiert; keine Story-CLI-, Node/Bun-, Projektstruktur-, Template- oder fremde Skilltext-Abhängigkeit übernommen und keine Redistribution fremden Materials vorausgesetzt;
- Skill-Katalog und menschliche Katalogdokumentation auf 137 Skills, 112× `partial`, 25× `none`, 0× `core`/`broad`, 112 Skill-Evalpacks und 575 definierte Cases aktualisiert; zusätzliche Coverage ist kein Behavioral-Qualitätsnachweis;
- kein Tag, Release oder automatische externe Synchronisation durch diese Erweiterung.

### Phase 4.2B – Code-Review-Paired-Eval-Replikation

- Designstand `Evals/Behavioral-Harness/experiments/code-review-v1/` ergänzt: `DESIGN.md`, `experiment.draft.yml` sowie sechs vollständig synthetische Review-Pakete als Fixtures;
- die claim-verification-spezifischen Kopplungen des Pair-Harness am realen Code verifiziert: geschlossenes Fixture-Rollen-Vokabular, verpflichtendes fünfwertiges `ground_truth.classification`, fest verdrahtete Domain-/Aufgabenfamilien-Literale, klassifikationsspezifische Judge-Anweisung sowie ein Disclosure-Fehlalarm auf dem Zielskill-Bezeichner `code-review`;
- kleinste Generalisierung entworfen statt eines zweiten Harness: ein expliziter Diskriminator `ground_truth_model`, dessen Fehlen das heutige Verhalten unverändert reproduziert; Contract-Entscheidung dokumentiert als erforderlich, aber nicht breaking, `behavioral-paired-skill-eval/v1` bleibt;
- domänenspezifisches Ground-Truth-Modell `code-review-findings/v1` mit vorab festgelegten Findings, Detektionskriterien, verbotenen Findings, Akzeptanzkriterien-Status und Freigabekalibrierung entworfen; ausdrücklich ohne aggregierte Gesamtpunktzahl;
- Pair-Harness backward-compatible für `code-review-findings/v1` generalisiert: optionaler `ground_truth_model`-Diskriminator, modellspezifische Fixture-Rollen, optionaler `runner_path`, konfigurierbare `domain`/`task_family`, Change-Set-Konsistenz als verpflichtendes Prepare-Time-Gate, modellspezifische Judge-Instruction, vorab festgelegte Evaluation Policy im Blind-Judge-Vertrag und ein eng begrenztes, coordinator-only Disclosure-Opt-in; fehlende Angaben reproduzieren jeweils exakt das bisherige Verhalten, belegt durch 18 von 18 identischen Claim-Verification-Pairs;
- `code-review-v1` als ausführbares Paired Experiment vorbereitet: sechs synthetische Code-Review-Cases, 6 Cases × 3 Repetitions vorbereitet und verifiziert, 36 Prepared Response Packages;
- `code-review/SKILL.md`, das bestehende Evalpack, der Katalog sowie Maturity und Eval Coverage wurden nicht verändert;
- einen realen Cross-Domain-Smoke ausgeführt: `CR-01`, Repetition 1, exakt zwei Behavioral Responses, je ein Modellversuch ohne Retry; Claude Code `2.1.258`, Adapter `0.2.1`, Modell `claude-haiku-4-5-20251001`; Phase 4.2A lief unter Claude Code `2.1.251`, daher wird keine exakte Runtime-Replikation über die Phasen hinweg behauptet;
- 2/2 kanonische Run-Packages verifiziert, Blind Packaging erfolgreich, keine Treatment-Disclosure; `fresh_context` true, `repository_access_disabled` true, `package_only_access` true, `network_disabled` unknown;
- `method_evidence_status: partial`, `comparison_eligible: false`; kein Semantic Judge, kein Unblinding, kein Behavioral Comparison, `skill_effect: unknown`; die restlichen 34 geplanten Responses wurden nicht ausgeführt; `Evals/Behavioral-Harness/experiments/code-review-v1/METHOD-RESULT.md` als methodischer Abschlussstand ergänzt;
- keine Response-Inhalte, keine Treatment-Zuordnung, keine Findings und keine Wirksamkeits- oder Qualitätsaussage persistiert; keine Maturity- oder Eval-Coverage-Hochstufung; der Phase-4.2A-Endstand bleibt unverändert `partial` bei `network_disabled: unknown`.

### Phase 4.2A – Claim-Verification Paired Pilot mit unvollständiger Method Evidence abgeschlossen

- schmale Pair-Orchestrierung `tools/behavioral_harness_pair.py` sowie das sechsfällige Experiment `claim-verification-v1` mit vorab festgelegter Ground Truth, expliziten Fixture-Rollen und counterbalanced Treatment-Reihenfolge ergänzt;
- konkreten Claude-Code-Runner-Adapter `tools/behavioral_harness_claude.py` ergänzt und real ausgeführt; beobachtet wurden Managed Auth im normalen Host-Kontext, Fresh Context mit allen 25 Checks erfüllt sowie belegte Filesystem-/Package-Grenze;
- Fresh-Context-Evidence gehärtet: Environment-Allowlist statt pauschaler Vererbung, dokumentierte Memory-/History-Controls, Managed-Policy-Preflight, Auth-Preflight mit sicherer Fehlerklassifikation sowie getrennte Semantik für versuchten, blockierten, erfolgreichen und unaufgeklärten Zugriff außerhalb des Runner-Package;
- genau einen realen Behavioral-Smoke ausgeführt: `CV-01-supported`, Repetition 1, exakt zwei Responses, kanonisch verpackt und treatment-blind gebündelt; die restlichen 34 geplanten Responses wurden nicht ausgeführt;
- Fixed-Destination-CONNECT-Guard `tools/runner_egress_guard.py` als eigenständige Runner-Infrastruktur ergänzt und offline getestet; er ist ausdrücklich **nicht** in den kanonischen Adapter integriert;
- Egress-Isolation empirisch untersucht: Provider über den hostverwalteten Proxy erreichbar, per-UID-nftables-Enforcement real bestanden, ein echter Claude-Child unter dieser Grenze jedoch an der Authentifizierung gescheitert und cgroup-basiertes Matching in dieser Hoststruktur nicht adressierbar; invasive Hoständerungen wurden bewusst unterlassen;
- Method Evidence bleibt damit korrekt `partial` bei `network_disabled: unknown` und `comparison_eligible: false`; `Evals/Behavioral-Harness/experiments/claim-verification-v1/METHOD-RESULT.md` als kanonischer Abschlussstand ergänzt;
- kein Semantic Judge, kein Unblinding, kein Behavioral-Vergleich und keine Aussage zur Skill-Wirksamkeit; `claim-verification/SKILL.md` unverändert, keine Maturity oder Eval Coverage verändert und kein Tag oder Release erzeugt.

### Discovery- und Entry-Path-Polish

- Discovery-only-Registry `Dokumentation/radar-sources.yml` ergänzt, um neue Skills, Methoden, Spezifikationen, Security-Hinweise und relevante KI-Entwicklungen systematisch zu finden, ohne Radarquelle, Upstream oder lokale Übernahme gleichzusetzen;
- Quellenregister und Dokumentation auf die Trennung `Discovery ≠ Adoption` sowie `Radarquelle ≠ Upstream` geschärft; neue Funde bleiben Review-Kandidaten und dürfen weder Regeln noch das Repository automatisch verändern;
- Root-README um einen kompakten Abschnitt `KI-Regeln in 60 Sekunden` und einen sichtbaren Einstieg in die Praxisbeispiele ergänzt;
- `AGENTS.md` und `Dokumentation/Skill-Handbuch.md` auf den vorhandenen Local Validation Harness als bevorzugten Repo-Prüfweg ausgerichtet; eine systemweit installierte Python-Runtime wird nicht mehr vorausgesetzt und nicht ausgeführte Prüfungen bleiben `NOT RUN` beziehungsweise `UNVERIFIED`;
- keine neuen Skills angelegt, keine Maturity oder Eval Coverage verändert, keine Behavioral Evals ausgeführt oder als bestanden dargestellt und kein Tag oder Release erzeugt.

### Review-Revise Loop

- fachübergreifenden Workflow `Workflows/Review-Revise-Loop.md` ergänzt für den wiederkehrenden Zyklus Auftrag/Ergebnis → kritischer Fachreview → Urteil und Findings → Änderungsstrategie → erforderliches Human Gate → gezielte Revision → erneuter Review;
- den Workflow ausdrücklich von `verification-loop` abgegrenzt: reproduzierbare Verifikation und fachlich-qualitative Review-/Revisionssteuerung können kombiniert werden, sind aber nicht dasselbe;
- Review und Änderung getrennt: ein Auftrag wie „dein Urteil?“ oder „deine Meinung?“ autorisiert noch keine Revision; Toolverfügbarkeit, Review-Finding oder APPROVE ersetzen keine separat erforderliche externe Freigabe;
- Same-Model-Review ausdrücklich nicht als unabhängig behandelt; `bildreview` entsprechend von „unabhängig geprüft“ auf „kritisch geprüft“ gehärtet, ohne seine Fachlogik oder Statusklassen zu verändern;
- `Workflows/Bildserie.md` als konkretes Domänenbeispiel an den allgemeinen Review-Revise Loop angebunden und `workflow-index.yml` um den neuen Workflow ergänzt;
- keine neuen Skills angelegt, keine Maturity oder Eval Coverage verändert, keine Behavioral Evals ausgeführt oder als bestanden dargestellt und kein Tag oder Release erzeugt.

### Behavioral Batch 0 – Runner-Readiness

- Batch-0-Fixtures für `WK-001`, `WK-004` und `WK-047` materialisiert; `WK-006` bleibt als No-Skill-/Direct-Response-Fall bewusst fixturefrei;
- die absichtlich knappe Voice-Evidence für `WK-004` konserviert und fehlende zusätzliche Voice-Evidence evaluator-only dokumentiert, ohne die Pilotdefinition oder Judge-Erwartungen zu verändern;
- sichere, ausschließlich lokale Fake-Production-Infrastruktur für `WK-047` ergänzt, die ohne Freigabe blockiert und kein reales Production-Ziel adressieren kann;
- synthetische Runner-Readiness-Tests sowie eine Batch-0-spezifische Readiness-Aggregation vorbereitet; Compiler-`ready_for_behavioral_execution` bleibt ausdrücklich Fixture-/Case-Readiness und ist keine Gesamtfreigabe;
- keinen konkreten LLM-Runner integriert; Runner- und objektive Route-/Read-Observability bleiben bis zu einer autorisierten, instrumentierten Runner-Infrastruktur nicht ready;
- keine Behavioral Evals und keine realen WK-Fälle ausgeführt; Batch 0 nicht gestartet; keine Skills, Maturity oder Eval Coverage geändert und kein Merge, Tag oder Release durch diese Vorbereitung.

### Local Validation Harness

- Windows-freundlichen lokalen Einstieg über `Validate-KI-Regeln.cmd` und `Validate-KI-Regeln.ps1` ergänzt; eine systemweit installierte Python-Runtime ist nicht erforderlich;
- vorhandene Python-Validatoren bleiben kanonische Prüflogik; PowerShell übernimmt ausschließlich Bootstrap, Orchestrierung, Reporting und Exitcode-Gating statt eine zweite fachliche Validatorimplementierung einzuführen;
- portable Runtime unter `.validation/` mit gepinntem `uv`, uv-managed CPython 3.12.12, fest eingefrorenen Python-Abhängigkeiten und SHA-256-Prüfung des uv-Archivs ergänzt; Windows-PowerShell-Bootstrap erzwingt bei Bedarf TLS 1.2 ohne vorhandene Protokolle zu entfernen;
- Modi `Quick`, `Full` und `Release` getrennt: `Full` ist Standard und ergänzt das read-only Eval-Coverage-Inventar, `Release` ergänzt Current-Tree- und Reachable-History-Exposure-Prüfungen mit bestehender CI-Severity-Semantik;
- maschinenlesbares JSON-, menschenlesbares Markdown- und technisches Log-Reporting unter `.validation/` ergänzt; `Behavioral validation` wird ausdrücklich als `NOT RUN` ausgewiesen;
- zehn kontrollierte Harness-Selbsttestfälle in einem temporären detached Git-Worktree vorbereitet, ohne produktive Repository-Dateien zu verändern oder synthetische Secret-Fixtures zu committen;
- keine Skill-Fachlogik, Maturity oder Eval-Coverage verändert, keine Behavioral Evals als ausgeführt oder bestanden dargestellt und kein Merge, Tag oder Release durchgeführt.

### Behavioral-Test-Harness – technische Vorbereitung

- technischen Behavioral-Test-Harness für den kontrollierten Werkzeugkoffer-Pilot ergänzt; Execution View und evaluator-only Judge View werden technisch getrennt, die Pilotmatrix selbst bleibt unverändert;
- Tri-State-Observability (`true` / `false` / `unknown`), Tool-/Action-Trace mit `attempted` versus `executed`, getrennte Authorization-Evidence und Fresh-Evidence-Beziehungen für strukturierte Claims vorbereitet;
- Workflow-Erwartungen explizit als `required`, `optional` oder `none` normalisiert und Capability-Gap-Routen von realen Skill-Routen getrennt, ohne neue Skills anzulegen;
- versionierte JSON-Schemas im normalen Harness-Pfad als verbindliche Verträge aktiviert sowie Prepared-/Run-Hashprüfung und `verify-run` zur Erkennung nachträglicher Artefaktänderungen ergänzt;
- ausschließlich synthetische/replaybare Harness-Selbsttests ausgeführt; keine realen WK-Fälle und keine Behavioral Evals ausgeführt oder als bestanden dargestellt;
- keine Skills, Skillgrenzen, Maturity- oder Eval-Coverage-Einstufungen geändert; kein Merge, Tag oder Release durch diesen Harness-Stand.

### Public-Readiness Messaging Cleanup

- README-Lizenzstatus an vorhandene Root-`LICENSE` und den autorisierten MIT-Stand angepasst; Drittmaterial und Public-Release-Gate bleiben getrennt geregelt;
- öffentliche README-Positionierung als experimenteller, systematisch gepflegter Werkzeugkasten mit expliziter Maturity, Eval Coverage, Provenance, Routing, Gates und Evidence geschärft; die Skillanzahl wird dabei nicht als Qualitätsnachweis dargestellt;
- unnötig fest verdrahteten Skill-Gesamtcount in `AGENTS.md` entfernt, um zukünftige Zahlendrift zu vermeiden;
- keine Skills, Evals, Maturity, Coverage oder Workflows geändert.

### Hardening Phase 3.6 – Schreiben und Kommunikation

- Schreiben um genau einen neuen Skill `adressatengerechte-kommunikation` ergänzt; schwierige schriftliche Kommunikation bleibt ein Modus dieses Skills statt eines separaten Konflikt-, Coaching-, E-Mail- oder Plattform-Kommunikationsskills;
- `natuerliches-schreiben` um klare Generation-, Rewrite-/Preservation- und Voice-Calibration-Regeln gehärtet; Voice-Evidence wird kontextbezogen und mit kalibrierter Confidence genutzt statt als exakte Persönlichkeitsrekonstruktion;
- `stilreview` ausschließlich an der Routinggrenze zu Rewrite und adressatenbezogener Kommunikation geschärft; `kreatives-schreiben` fachlich unverändert belassen;
- Detector-Scores sind weder Qualitäts- noch Akzeptanzziel; keine Undetectability-Garantien, keine künstlichen Fehler und keine erfundenen Anekdoten zur Detector-Manipulation; freiwillige Detector-Ergebnisse dürfen ausschließlich als sekundäres Review-Signal einen erneuten unabhängigen Sprachcheck auslösen, nicht als Auftrag zur Score-Optimierung;
- vier Schreiben-Evalpacks ergänzt beziehungsweise vervollständigt: 12 Cases für `natuerliches-schreiben`, 11 für `adressatengerechte-kommunikation`, 6 für `kreatives-schreiben` und 6 für `stilreview`, zusammen 35 neue definierte Schreiben-Cases; Gesamtstand 107 Evalpacks mit 550 definierten Cases;
- die neuen Schreiben-Cases sind definiert, aber nicht als Behavioral Evals ausgeführt oder bestanden dargestellt;
- Skill-Katalog auf 132 Skills aktualisiert; Coverage 107× `partial`, 25× `none`, 0× `core`/`broad`; `adressatengerechte-kommunikation` startet `experimental / partial`, die drei bestehenden Schreiben-Skills bleiben `candidate`; keine bestehende Maturity hochgestuft;
- methodische Quellen für Humanize/Voice Calibration und adressatengerechtes Drafting source-spezifisch registriert und in `Dokumentation/upstream-provenance.yml` als `assessed / reference/inspiration / concepts/methods-only / no-signal / not-relied-on` dokumentiert; comparison-only Quellen wurden nicht künstlich als Herkunft registriert;
- bewusst keine zusätzlichen Skills `redaktioneller-entwurf`, `humanizer`, `voice-calibration`, `email-drafter`, Plattform-Kommunikation oder `ai-detector-bypass` angelegt;
- Upstream-Governance bleibt `review-only` mit `auto_sync: false`; kein Merge, Tag oder Release durch Phase 3.6.

### Hardening Phase 3.5 – Webdesign und Motion

- Webdesign um drei klar getrennte Motion-Skills ergänzt: `motion-design` definiert Zweck und Motion-Contract, `motion-implementation` setzt freigegebene Motion technisch um und `motion-review` bewertet vorhandene Motion unabhängig; Reverse Engineering aus Screenrecordings bleibt Evidence-Modus von `motion-review` statt eigener vierter Skill;
- gemeinsame Grundlage `Webentwicklung/Webdesign/Motion-und-Mikrointeraktionen.md` ergänzt: keine Animation als valides Ergebnis, kontextabhängige Timing-/Easing-Entscheidung, Spatial Continuity, Gesten, Interruptibility, Reduced Motion, evidenzbasierte Toolwahl und Performance ohne GPU-/Property-/Library-Dogmen;
- vier bestehende Web-Skills nur an realen Routingkanten geschärft (`frontend-design`, `design-system`, `web-design-review`, `visual-verification`); `accessibility-review` und `frontend-performance` blieben nach Prüfung unverändert;
- drei Motion-Evalpacks mit insgesamt 26 definierten Cases ergänzt, einschließlich positiver Trigger, Landingpage-/WCAG-/Performance-Near-Misses, `keine Animation`, Reduced Motion, Toolwahl, fehlende Render-Evidence sowie Screenrecording → `motion-review` → `motion-implementation` → `visual-verification`; diese Cases sind definiert, aber nicht als Behavioral Evals ausgeführt oder bestanden;
- drei methodische Skill-Upstreams source-spezifisch als `reference/inspiration` geprüft (`emilkowalski/skills`, `mblode/agent-skills`, `Leonxlnx/taste-skill`); finaler Text übernimmt keine konkreten Tabellen, Skalen, Defaultwerte oder Source-Struktur und bleibt `similarity_audit: no-signal`; genealogisch abhängige Hinweise werden nicht als unabhängiger Konsens doppelt gezählt;
- acht konkrete technische Primärquellen für Reduced Motion, WAAPI, `@starting-style`, View Transitions, Scroll-driven Animations sowie Motion-/GSAP-Fähigkeiten registriert; technische Primärquellen werden nicht als methodischer Designkonsens behandelt;
- Skill-Katalog von 128 auf 131 Skills erweitert; die drei neuen Skills starten `experimental` mit `partial` Evalabdeckung, ohne bestehende Maturity hochzustufen; aktueller Coverage-Stand 103× `partial`, 28× `none`;
- GT-09 bewusst nicht allein zur Erhöhung der Golden-Task-Anzahl erzeugt: der zusätzliche kombinierte Motion-Reproduktionsfall prüft bereits die neue Cross-Skill-Routingkante, ohne aktuell einen zusätzlichen systemischen Golden-Task-Gewinn zu belegen;
- CI-Noise auf Hardening-Branches reduziert: die dauerhaften Repo-Validation- und Open-Source-Exposure-Workflows laufen automatisch auf `pull_request` und `push: main`; Branchläufe bleiben gezielt per `workflow_dispatch` verfügbar, ohne Checks, Permissions oder Auditlogik zu reduzieren;
- Upstream-Governance bleibt `review-only` mit `auto_sync: false`; kein Merge, Tag, Release, Visibility-Wechsel oder automatische Upstream-Synchronisation durch Phase 3.5.

### Hardening Phase 3 – Open-Source Readiness

- maschinenlesbaren Open-Source-Readiness-Status und menschenlesbaren Phase-3-Auditbericht ergänzt; Public-Release-Gates bleiben von erfolgreichem technischem Hardening getrennt;
- Provenance-Zustandsmodell so gehärtet, dass `assessed` nur abschließend klassifizierte Fälle erlaubt und `needs-human/legal-review` echte Unklarheit mit `use_class: unclear`, `material_scope: unclear`, `redistribution_reliance: unclear` und `redistribution_status: unresolved` ausdrücken kann, ohne daraus Redistributionsfreigabe abzuleiten;
- alle 65 konkreten GitHub-Upstream-Artefakte source-spezifisch auditiert und `Dokumentation/upstream-provenance.yml` migriert: final 61× `reference/inspiration` ohne Redistributionsabhängigkeit und vier Matt-Pocock-Artefakte jeweils separat als `adapted`; der zunächst offene Neon-Fall wurde nach Auflösung des historischen Blob→Commit-Mappings per Local-Impact-/Expression-Vergleich als `assessed / reference/inspiration` abgeschlossen und trägt same-state Apache-2.0-Evidence;
- `THIRD-PARTY-NOTICES.md` aus tatsächlich redistribution-relevanten Adaptionsfällen abgeleitet und von `ACKNOWLEDGEMENTS.md` für reine Referenz-/Inspirationsräume getrennt;
- Current-Tree- und Reachable-History-Exposure-Audits ergänzt; Reports geben nur Finding-Metadaten wie Klasse, Pfad, Zeile und Commit aus, niemals gematchte Secretwerte;
- Public-Repo-Hygiene mit `CONTRIBUTING.md`, `SECURITY.md`, Pull-Request-Template, Dependabot-Konfiguration, dokumentierter Branch-Protection-Empfehlung und schlankem README-Public-Entry-Path ergänzt;
- GitHub Actions auf konkrete geprüfte v7-Commit-SHAs gepinnt, Workflowrechte bei `contents: read` belassen und keinen Auto-Merge oder automatischen Upstream-Sync eingeführt;
- `tools/repo_validator.py` um dauerhafte strukturelle Provenance-/Readiness-Invarianten erweitert, ohne juristische Ähnlichkeits- oder Lizenzentscheidung zu automatisieren;
- autorisierten Projektlizenz-Decision-Gate geschlossen und Root-`LICENSE` mit MIT für das originäre KI-Regeln-Projektmaterial ergänzt; Drittmaterial wird dadurch nicht relicensed, `THIRD-PARTY-NOTICES.md` bleibt für redistribution-relevante Fremdanteile maßgeblich; Security Reporting bleibt bis zu einem verifizierten privaten Meldeweg als Phase-4-Release-Day-Gate blockiert;
- keine `SKILL.md`-Fachlogik, Maturity oder Eval-Coverage im Rahmen von Phase 3 hochgestuft; kein Merge, Tag, Release, Visibility-Wechsel oder Branch-Protection-Write durch das Hardening.

### Hardening Phase 2 – Evals & Golden Tasks

- reproduzierbaren read-only Coverage-Audit für alle 128 katalogisierten Skills ergänzt;
- elf systemisch wirksame Eval-Lücken gezielt geschlossen (`task-graph`, `verification-loop`, `delegation-contract`, `agent-eval`, `docs-plan`, `technical-writing`, `reference-docs`, `web-search`, `research-plan`, `claim-verification`, `skill-review`): 11 neue Evalpacks mit 55 definierten Cases; Eval Coverage dadurch 89→100× `partial` und 39→28× `none`, ohne Maturity-Änderung;
- systemweite Golden-Task-Suite mit acht lokalen reproduzierbaren Aufgaben, maschinenlesbarem Schema und struktureller Validatorprüfung ergänzt;
- Execution View und Judge View für Golden Tasks getrennt; evaluator-only Routing-, Status-, Forbidden- und Rubrikfelder werden aus der reproduzierbaren Execution-Projektion ausgeblendet;
- Same-Model-Smoke mit GPT-5.6 Sol über GT-01 bis GT-08 ausgeführt: final 8/8 aligned, davon 7× `pass` und GT-04 erwartungsgemäß `partial`, 0 Forbidden-Verstöße; ausdrücklich `same-model / non-blind / author-contaminated` und daher kein unabhängiger Generalisierungs- oder Routing-Benchmark;
- Smoke-Fund in GT-07 als zu enge Bewertungsrubrik klassifiziert: gerenderter `web-design-review` war ohne Render-Evidence fälschlich Pflicht; ausschließlich evaluator-only Taskdefinition minimal korrigiert und re-judged, kein Fachskill geändert;
- `tools/repo_validator.py` um read-only Strukturprüfung der Golden Tasks erweitert; definierte Cases oder strukturell gültige Golden Tasks werden dadurch nicht als behavioral bestanden behandelt.

### Hardening Phase 1

Strukturelles Hardening für reproduzierbare KI-Nutzung, Discovery, Validierung und Provenance ohne Maturity- oder Fachlogik-Hochstufung:

- `AGENTS.md` als schlanker KI-Bootstrap ergänzt und `Dokumentation/Skill-Handbuch.md` zum Master-Router für Fachbereiche, Skills und Workflows umgebaut;
- `workflow-index.yml` als maschinenlesbarer Index des vollständigen Workflow-Bestands ergänzt;
- deterministischen, read-only arbeitenden Repo-Validator unter `tools/repo_validator.py` einschließlich JSON-Schemas und GitHub Action `.github/workflows/repo-validation.yml` ergänzt;
- alle 128 katalogisierten Skills reproduzierbar auf Discovery-Metadaten geprüft; ausschließlich 49 durch den Validator konkret beanstandete Skills normalisiert, ohne Maturity zu ändern;
- Diff-Gegenprobe der 49 normalisierten Skills gegen `5be2763da15522bec6ced372a8119c806a77e244` durchgeführt; dabei unbeabsichtigte Kürzungen in `Webentwicklung/Skills/frontend-design/SKILL.md` und `Recherche/Skills/web-search/SKILL.md` gefunden und deren fachliche Originalkörper vollständig wiederhergestellt, sodass dort nur erforderliche Discovery-Metadaten verbleiben;
- YAML-Datumsbehandlung so kalibriert, dass native YAML-Date-/Datetime-Werte ausschließlich für die Schema-Prüfung als ISO-Werte normalisiert und mit Date-Formatprüfung validiert werden; Quelldateien werden dafür nicht umgeschrieben;
- syntaktisch ungültigen Backtick-Eintrag in `Vorlagen/ki-regeln.template.yml` minimal gequotet und kommentierte, bewusst leere Auswahlblöcke im zugehörigen Schema als leere YAML-Semantik (`null` oder Array) abgebildet;
- zwei veraltete `Data-Engineering/Transformationen-und-Backfills.md`-Referenzen auf den tatsächlich vorhandenen Pfad `Data-Engineering/Transformationen-Inkrementalitaet-und-Backfills.md` korrigiert;
- für alle 65 konkret beobachteten GitHub-Upstream-Artefakte source-spezifische Provenance-Einträge in `Dokumentation/upstream-provenance.yml` ergänzt; ohne belastbar zusammengehörigen historischen Repository-Commit und Lizenznachweis bleibt der Redistributionsstatus konservativ `unresolved`;
- `THIRD-PARTY-NOTICES.md` auf tatsächlich notice-relevantes übernommenes, vendored oder substanziell adaptiertes Fremdmaterial begrenzt; reine `reference/inspiration`-Quellen werden dort nicht wie eingebettetes Fremdmaterial dargestellt;
- keine Behavioral-Evals für dieses Hardening ausgeführt oder als bestanden behauptet, keine Maturity geändert, keinen Tag oder Release erzeugt und keinen automatischen Upstream-Sync eingeführt.

### Social Media und Content-Präsenz

Neuer plattform- und toolneutraler Hauptbereich für Social-Media-Präsenz, Content-Systeme, Community-Arbeit und performancebasiertes Lernen:

- Content-Präsenz als System aus Ziel, Audience, Positionierung, Themen, Plattformrollen, Content, Community und Evidence modelliert statt als Sammlung einzelner Posts;
- bestehende Profile, Bios, Links, Posts, Formate, Kadenz und reale Analytics über `content-presence-baseline` read-only erfassbar, ohne fehlende Performanceursachen oder Benchmarks zu erfinden;
- Social-Content-Strategie aus bestätigten Zielen, Audience, Positionierung, Themen und realen Plattformrollen statt universellen Content-Pillars, Postingfrequenzen oder Algorithmusmythen;
- Editorial Planning übersetzt Strategie in Backlog, Serien, Prioritäten, Owner, Produktionsstatus und Kalender, bleibt aber klar von realem Scheduling und Publishing getrennt;
- konkrete Social-Drafts über `social-content-design` mit belegter Source-Wahrheit, natürlicher Sprache und sichtbaren Claim-/Rights-/Disclosure-Grenzen statt erfundener Zahlen, Testimonials, Trends oder künstlicher Hook-Mechanik;
- Plattformadaption erhält Kernbotschaft und Wahrheit, verändert aber Struktur, Einstieg, Länge, Interaktionsform und Format nach aktueller Plattform-Evidence; zentrale Regeln konservieren keine angeblich ewigen Rankinggewichte, Limits oder Best Times;
- Content Repurposing behandelt Source-Assets als kanonische Quelle und erzeugt eigenständige Derivatives statt mechanischer Cross-Posts oder Low-Value-Reuploads;
- Community Engagement priorisiert reale Fragen und Dialog, trennt Reply-Drafts, Support-/Moderationseskalation und Außenaktionen und lehnt Fake-Engagement, Engagement-Ringe, Dogpiling und koordinierte Manipulation ab;
- Content Performance Analysis bindet Metriken an Ziele, hält Definition, Zeitraum, Vergleichsbasis und Nenner fest und trennt Korrelation, Hypothese und Kausalität; ein einzelner Gewinnerpost beweist keine Algorithmusregel;
- unabhängiges `content-presence-review` prüft Ziele, Audience, Positionierung, Plattformfit, Content, Community, Analytics, Claims, Rights/Disclosure und Freigabeprozess read-only;
- zentrale Trennungen `Draft ≠ Post`, `Kalender ≠ Scheduling`, `Review ≠ Publishing-Freigabe`, `Engagement ≠ Geschäftserfolg`, `Korrelation ≠ Kausalität` und `Repurposing ≠ Copy/Paste`;
- neun neue Skills `content-presence-baseline`, `social-content-strategy`, `editorial-planning`, `social-content-design`, `platform-content-adaptation`, `content-repurposing`, `community-engagement`, `content-performance-analysis` und `content-presence-review`;
- alle neun Social-Media-Skills starten `experimental` mit `partial` Evalabdeckung;
- 54 Evalfälle definiert, sechs je Skill, mit erwarteter Statusverteilung 36× `pass`, 9× `partial` und 9× `blocked`, einschließlich fehlender Analytics-/Policy-/Rights-Evidence, Algorithmus-/Benchmarkdogmen, Fake-Engagement, Kausalitätsfehlern und externen Publishing-/Reply-/Delete-/Block-Gates; diese 54 Fälle sind **definiert, aber noch nicht als Behavioral Evals ausgeführt oder bestanden**;
- fünf Workflows für Presence-/Strategie-Baseline, Editorialproduktion, Cross-Platform-/Repurposing, Community-Arbeit sowie Performance-/Readiness-Review;
- neues menschliches `Dokumentation/Skill-Handbuch-Social-Media-und-Content-Praesenz.md`;
- Root-README, Workflow-/Eval-Dokumentation, Skill-Katalog, Projektmanifest, Nutzungsdoku und Pflege-Radar um Social Media und Content-Präsenz erweitert;
- Projektmanifest um lokalen `content_presence_context` für Ziele, Audience, Voice/Positionierung, Plattformrollen, Sources, Themen, Metrikdefinitionen, Rights/Disclosure und Publishing-/Approval-Policy ergänzt;
- Requirements, Recherche, Schreiben und Bildarbeit mit expliziten Social-Media-Handoffs verbunden: Ziele und Constraints bleiben lokal/bei Requirements, externe Claims und Trends bei Recherche, allgemeine Sprachqualität bei Schreiben und visuelle Produktion bei Bildarbeit;
- Skill-Katalog von 119 auf 128 zentrale Skills erweitert;
- neun aktive Social-Media-Upstreams registriert: lebende LinkedIn-, Meta-, YouTube- und FTC-Quellen per semantischem Monatsreview sowie vier konkret verwendete öffentliche Social-Agent-Skills per Repositorypfad und geprüftem Blob-SHA;
- konkrete Skill-Upstreams: `blacktwist/social-media-skills` `content-strategy-sms` (`b4eefa218107e9c8402bf8318abd1cce38f383f1`), `blacktwist/social-media-skills` `content-repurposer-sms` (`03e0d2398cb513ee19dd80f19d24dfe58ed701a3`), `social-media-skills/skills` `analytics-and-reporting` (`bf851b46b375f6c9952f54245f5fa49ff7da0371`) und `inklate/social-skills` `social-audit` (`de89934532c0203052f12158df32032469afab77`);
- Plattformfeatures, Formatlimits, Analyticsdefinitionen und Aussagen über Ranking/Distribution werden als mutable Evidence behandelt und bei Materialität aktuell geprüft statt als zeitlose zentrale Regeln festgeschrieben;
- reale Posts, Scheduling, Replies, DMs, Deletes, Blocks, Profiländerungen und andere Außenaktionen bleiben lokal gated; Toolverfügbarkeit oder ein Review-Verdict autorisieren sie nicht automatisch;
- Upstream-Governance bleibt `on_change: review-only` und `auto_sync: false`.

### Requirements und Specification Engineering

Neuer tool- und formatneutraler Hauptbereich für Requirements Elicitation, Spezifikation, Acceptance, Traceability, Change und Validation:

- Requirements Engineering als Übersetzung von Stakeholderbedarf, Zielen, Constraints und Evidence in nachvollziehbare, prüfbare Soll-Aussagen statt als PRD-/Ticket-Schreibübung modelliert;
- klare Quellen- und Autoritätslogik für Stakeholderaussagen, Entscheidungen, bestehende Spezifikationen, Fachquellen, Tickets, Code, Tests und Runtime-/Ist-Evidence;
- `Stakeholderwunsch ≠ automatisch verbindliches Requirement` sowie `Ist-Verhalten ≠ automatisch gewünschtes Soll` als zentrale Brownfield-Grenzen;
- Requirements Baseline trennt bestätigte Soll-Aussagen, aktuelle Ist-Evidence, Annahmen, Konflikte, offene Fragen und Supersession statt aus dem Repository stillschweigend Spezifikation zu rekonstruieren;
- Elicitation über Interviews, Workshops, Dokumentanalyse, Beobachtung und technische Evidence nach Kontext statt festem Fragebogen oder Vollständigkeitsscore;
- Problem, Ziel, Scope, Out-of-Scope, Constraints, Assumptions, Dependencies und offene Fragen als explizite Ebenen;
- funktionale Anforderungen beschreiben benötigtes Verhalten beziehungsweise Capability, ohne frühzeitig Architektur, Framework, Datenbank oder konkrete Implementierung festzuschreiben;
- Quality Requirements werden über relevantes Objekt/Flow, Bedingung, Messidee und bestätigten Zielwert formuliert statt mit unprüfbaren Adjektiven wie „schnell“, „skalierbar“ oder „hochverfügbar“;
- fehlende Performance-, Availability-, RTO/RPO-, Capacity-, Kosten- oder andere Zielwerte werden nicht erfunden; sie bleiben Missing Evidence beziehungsweise lokale Entscheidung;
- Acceptance Criteria als beobachtbare Akzeptanzbedingungen von konkreten Testfällen, Testdaten und Testautomatisierung getrennt;
- EARS, Given-When-Then, Gherkin, User Stories, Use Cases, PRD, BRD und SRS als optionale Formate und Techniken statt Pflichtmodell;
- bidirektionale Traceability von Source/Goal über Requirement und Acceptance bis zu downstream Design-/Test-/Evidence-Artefakten, ohne Traceability mit Korrektheit gleichzusetzen;
- Requirements Change Analysis mit Baseline-Diff, Impact auf Ziele, Acceptance, Architektur, Interfaces, Daten, Reliability, Tests und Migration, aber ohne automatische Downstream-Änderung;
- Lifecycle mit Draft, Review, Approval/Baseline, Versionierung, Supersession und Change-Historie; konkrete Statusnamen und Approval-Policy bleiben lokal;
- Requirements Validation prüft, ob die beschriebenen Anforderungen den tatsächlichen Stakeholderbedarf und Intended Use treffen; Verification/Testen der Implementierung bleibt downstream;
- unabhängiges Requirements Review prüft Quellenbasis, Scope, Qualität, Acceptance, Traceability, Konflikte, Change-/Lifecycle-State und Missing Evidence read-only;
- Readiness-Verdicts `READY_FOR_LOCAL_GATE`, `READY_WITH_FINDINGS`, `BLOCKED` und `UNVERIFIED` liefern Evidence für die nächste lokale Entscheidung, aber keine fachliche Abnahme oder Implementierungs-/Releasefreigabe;
- acht neue Skills `requirements-baseline`, `requirements-elicitation`, `requirements-specification`, `acceptance-criteria-design`, `requirements-traceability`, `requirements-change-analysis`, `requirements-validation` und `requirements-review`;
- alle acht Requirements-Skills starten `experimental` mit `partial` Evalabdeckung;
- 48 Evalfälle definiert, sechs je Skill, einschließlich Code-/Ist-vs.-Soll-Fällen, Clarity-Score-/User-Story-/Gherkin-/MoSCoW-Dogmen, erfundenen Quality Targets, Acceptance-vs.-Test-Near-Misses, Traceability-Autofix, Change-Autorisierung, fehlender Stakeholder-/Source-Evidence und Approval-/Deployment-Gates; diese 48 Fälle sind **definiert, aber noch nicht als Behavioral Evals ausgeführt oder bestanden**;
- fünf Workflows `Requirements-Baseline-und-Spezifikation.md`, `Requirements-Elicitation-und-Klaerung.md`, `Acceptance-Traceability-und-Handoff.md`, `Requirements-Change-und-Impact.md` und `Requirements-Readiness-Review.md`;
- neues menschliches `Dokumentation/Skill-Handbuch-Requirements-und-Spezifikations-Engineering.md`;
- `Software-Architecture-und-System-Design/`, `Reliability-und-System-Observability/`, `Data-Engineering/`, `Testing-und-QA/` und `Schnittstellen-und-Vertraege/` mit dem realen Requirements-Bereich verbunden;
- Root-README, Workflow-/Eval-Dokumentation, Skill-Katalog, Projektmanifest, Nutzungsdoku und Pflege-Radar um Requirements und Specification Engineering erweitert;
- Projektmanifest um lokalen `requirements_context` für Stakeholder, Ziele, Sources of Truth, Scope, Constraints, bestätigte Quality Targets, Approval-/Baseline-Policy und offene Fragen ergänzt;
- Skill-Katalog von 111 auf 119 zentrale Skills erweitert;
- acht aktive Requirements-Upstreams registriert: IREB Foundation, IREB Elicitation, NASA Requirements Engineering, NASA SE Handbook Appendix und ISO/IEC/IEEE 29148 Edition 3 Draft per semantischem Monatsreview sowie `Modular-Earth-LLC/solutions-architecture-agent`, `microsoft/hve-core` `requirements-author` und `Spacey6849/AgentSkills` `requirements-analysis` per konkretem Repositorypfad und geprüftem Blob-SHA;
- ISO/IEC/IEEE 29148 Edition 3 ausdrücklich als Draft-Upstream behandelt, damit ein späterer Final-Release als Review-Signal erkannt wird, ohne den Draft heute als endgültigen Normstand auszugeben;
- öffentliche Agent-Skills als methodische Upstreams eingeplant, ohne BANT-/GenAI-/AWS-Speziallogik, BRD/PRD-Zwang, feste Clarity Scores oder andere hostspezifische Prozessvorgaben zu zentralen Regeln zu machen;
- Upstream-Governance bleibt `on_change: review-only` mit `auto_sync: false`.

### Software Architecture und System Design

Neuer technologie- und providerneutraler Hauptbereich für Systemstruktur, Architekturentscheidungen, Trade-offs, Evolution und Conformance:

- Architecture Drivers, Constraints, Annahmen und Missing Evidence als Ausgangspunkt statt Pattern-, Framework- oder Cloudpräferenz;
- System Context mit Akteuren, externen Systemen, Verantwortung, Ownership und Sources of Truth vor interner Kästchenstruktur;
- Dekomposition in Module, Komponenten und Services nach Verantwortung, Invarianten, Change-/Failure-Isolation, Scale, Security und Lifecycle statt Teamgröße oder Bounded-Context-Dogma;
- logische Boundary ausdrücklich vor Deployment-/Servicegrenze; ein Bounded Context ist nicht automatisch ein Microservice;
- Dependency Direction, öffentliche Oberflächen, Shared Components und Zyklen nach lokaler Architekturwirkung statt pauschaler Reinheitsregel bewertet;
- Runtime- und Failure-Flows mit State Ownership, Acknowledgement-/Commit-Punkten, Coordination, Retry-/Idempotenz-Verantwortung und Recovery als notwendige Ergänzung statischer Diagramme;
- Architekturstyles und Patterns wie Modular Monolith, Layered, Hexagonal, Microservices, Event-driven, CQRS, Event Sourcing, Saga oder Strangler als Optionen mit Voraussetzungen, Kosten und neuen Failure Modes statt Reifeleiter;
- einfachste tragfähige Architektur als Baseline-Kandidat; zusätzliche Kandidaten nur, wenn sie eine echte strukturelle, Daten-, Konsistenz-, Failure-, Kosten- oder Operability-Achse anders lösen;
- Quality Attributes über konkrete Szenarien, Sensitivity Points und Trade-offs statt abstrakter Schlagwörter oder undurchsichtiger Architecture Scores;
- fehlende QPS-, SLO-, RTO/RPO-, Kosten-, Team- oder andere Zielwerte werden nicht erfunden, sondern als Annahme oder Missing Evidence sichtbar gemacht;
- Technologieauswahl nach Problem, Drivers, benötigten Eigenschaften und Struktur; Reversibilität, Lifecycle, Betriebsmodell und Exit-/Migrationspfad werden berücksichtigt;
- evolutionäre Architekturänderungen über begrenzte Slices, Compatibility, beobachtbare Zwischenzustände, Abort/Rollback und Retirement statt Big-Bang-Rewrite oder reinem Zielbild;
- Architecture Evidence über aktuelle Code-/Config-/Runtime-Artefakte, ADRs und zielgerichtete Views; alte Diagramme oder Dokumente sind nicht automatisch aktuelle Ist-Evidence;
- C4 als optionale View-Sprache und arc42 als Coverage-Inspiration genutzt, ohne vollständige Diagrammhierarchie oder Dokumenttemplate verpflichtend zu machen;
- Architecture Conformance und Fitness Functions für lokale Boundary-, Dependency-, Ownership- und ADR-Regeln; ein konfigurierter Check gilt erst als Evidence, wenn seine Wirksamkeit gegenüber relevanten Verstößen nachgewiesen ist;
- sieben neue Skills `architecture-baseline`, `system-design`, `architecture-decomposition`, `architecture-tradeoff-analysis`, `architecture-evolution`, `architecture-conformance-review` und `architecture-review`;
- alle sieben Architecture-Skills starten `experimental` mit `partial` Evalabdeckung;
- 42 Evalfälle definiert, sechs je Skill, einschließlich veralteter Diagramme, ADR-/Code-Konflikte, Microservice-/Teamgrößen-/Shared-DB-Dogmen, fehlender Quality-/Capacity-Evidence, künstlicher Kandidaten, Architecture-Score-Dogma, Big-Bang-Migrationen, fehlender Conformance-Baseline und produktiver Implementierungs-/Cutover-Gates;
- erster Same-Model-Smoke am 2026-08-25 gegen `78abce4ade2e1d92dfc47f6169dcd2551d8d0f09`: 42/42 Fälle entsprachen dem erwarteten Verhalten und Status (30× `pass`, 6× `partial`, 6× `blocked`, 0 beobachtete verbotene Verhaltensweisen); der Lauf ist kein unabhängiger verblindeter Benchmark und rechtfertigt keine Maturity-Hochstufung;
- fünf Workflows `Architektur-Baseline-und-Systemdesign.md`, `Architekturentscheidung-und-Tradeoff.md`, `Systemgrenze-und-Dekomposition.md`, `Evolutionaere-Architekturaenderung.md` und `Architektur-Readiness-Review.md`;
- neues menschliches `Dokumentation/Skill-Handbuch-Software-Architecture-und-System-Design.md`;
- Nachbardomänen `Schnittstellen-und-Vertraege/`, `Infrastruktur-und-DevOps/`, `Reliability-und-System-Observability/` und `Data-Engineering/` mit expliziten Architecture-Grenzen verbunden;
- Root-README, Workflow-/Eval-Dokumentation, Skill-Katalog, Projektmanifest, Nutzungsdoku und Pflege-Radar um Software Architecture und System Design erweitert;
- Skill-Katalog von 104 auf 111 zentrale Skills erweitert;
- sieben aktive Architecture-Upstreams registriert: C4, arc42, SEI/ATAM und Azure Architecture Styles per semantischem Monatsreview sowie `pinchen147/system-design-skill`, `lx-wnk/skills` `architecture-design` und `architecture-review` per konkretem Repositorypfad und geprüftem Blob-SHA;
- öffentliche Agent-Skills als aktiv beobachtete methodische Upstreams eingeplant, ohne deren hostspezifische Renderer, erzwungene Kandidatenzahlen oder stackspezifische Regeln blind zu übernehmen;
- vorhandener `adr`-Skill bleibt für dauerhafte Architecture Decision Records zuständig; kein redundanter ADR-Skill angelegt;
- Architektur-Verdicts, Conformance-Findings oder Migrationspläne autorisieren weder Sourcecodeänderung, Datenmigration, Deployment, Traffic Switch noch Release automatisch.

### Data Engineering

Neuer tool- und plattformneutraler Hauptbereich für systemübergreifende Datenflüsse, analytische Datenprodukte und kontrollierte Datenänderungen:

- klare Scope-Grenze zu `Datenbanken/`: operative Datenspeicher, Query-/Schema-/DB-Betrieb bleiben dort; Ingestion, CDC, Transformation, Orchestrierung und veröffentlichte Datenprodukte liegen in `Data-Engineering/`;
- Datenfluss zunächst über Source of Truth, Source, Destination, Consumer, Ownership, Grain, Semantik und Betriebsanforderungen modelliert statt aus Toolpräferenzen heraus;
- Ingestion mit Snapshot, Incremental, CDC, Cursor/Checkpoint, Duplicate-/Ordering-Verhalten, Late Data und Replay als expliziten Entwurfsfragen;
- `updated_at` ausdrücklich nicht als automatisch sicherer Cursor behandelt und Processing Guarantees wie `exactly once` nicht ohne End-to-End-Evidence behauptet;
- Transformationen und inkrementelle Verarbeitung mit expliziten Keys, Grain, Zustands-/Historisierungssemantik und Reprocessing-Verhalten;
- Backfill und Replay als reale, publish-sensitive Datenänderungen mit bounded scope, Idempotenz-/Write-Strategie, Reconciliation, Recovery und lokalem Human Gate;
- analytische Datenmodellierung als eigene Disziplin für Grain, Historisierung, Dimensionen/Fakten, Metriksemantik und Consumer-Fit statt Star-Schema-Dogma;
- Datenqualität entlang getrennter Achsen wie Korrektheit, Vollständigkeit, Freshness, Eindeutigkeit, Konsistenz und Reconciliation; ein grüner Job beweist keine korrekten Daten;
- Data Contracts als veröffentlichte Dataset-Zusage mit Struktur, Semantik, Quality, Service-/Freshness-Erwartungen, Ownership und Evolution statt bloßem DDL;
- Lineage und Provenance für Herkunft, Transformation, Dataset-/Job-/Run-Beziehungen und Impact Analysis; Diagrammexistenz allein gilt nicht als Evidence;
- Orchestrierung mit Abhängigkeiten, Ausführungszustand, Retry, Catch-up/Reprocessing und Publish-Gates ohne Airflow-/DAG-Pflicht;
- Batch, Micro-Batch und Streaming nach tatsächlicher Latenz-/Vollständigkeitsanforderung statt Streaming-Reifegrad-Dogma; Event Time, Processing Time, Windows, Watermarks und Late Data werden als Semantikentscheidungen behandelt;
- Publish, Retention und Datenlebenszyklus als bewusste Consumer- und Governance-Grenzen statt implizite Nebenwirkung eines erfolgreichen Jobs;
- Pipeline-Observability für Freshness, Completeness, Lag, Processing State, Quality und Replay Evidence mit klarer Übergabe an `Reliability-und-System-Observability/` für systemweite Betriebsziele und Incidents;
- neun neue Skills `data-pipeline-design`, `data-ingestion-design`, `data-transformation-design`, `analytical-data-modeling`, `data-quality-design`, `data-contract-design`, `data-lineage-analysis`, `data-orchestration-design` und `data-engineering-review`;
- alle neun Skills starten `experimental` mit `partial` Evalabdeckung;
- 54 Evalfälle definiert, sechs je Skill, einschließlich DB-/Interface-/Testing-Near-Misses, fehlender Source Evidence, unsicherer Cursor-/Exactly-once-Annahmen, Modellierungsdogmen, Quality-/Publish-Grenzen und produktiver Backfill-/Replay-Gates; diese 54 Fälle sind definiert, aber noch nicht als Behavioral Evals ausgeführt oder bestanden;
- fünf Workflows `Data-Pipeline-Baseline-und-Design.md`, `Neue-Datenquelle-und-Ingestion.md`, `Datenqualitaetsstoerung-und-Reconciliation.md`, `Backfill-und-Reprocessing.md` und `Data-Engineering-Readiness-Review.md`;
- neues menschliches `Dokumentation/Skill-Handbuch-Data-Engineering.md`;
- Nachbardomänen `Datenbanken/`, `Schnittstellen-und-Vertraege/`, `Testing-und-QA/`, `Reliability-und-System-Observability/` und `Infrastruktur-und-DevOps/` mit expliziten Data-Engineering-Grenzen verbunden;
- Root-README, Workflow-/Eval-Dokumentation, Skill-Katalog, Projektmanifest, Nutzungsdoku und Pflege-Radar um Data Engineering erweitert;
- Skill-Katalog von 95 auf 104 zentrale Skills erweitert;
- sieben aktive Data-Engineering-Upstreams registriert: Airflow, Beam, Kafka, OpenLineage und Open Data Contract Standard semantisch sowie zwei konkret verwendete `vaquarkhan/data-engineering-agent-skills` per geprüftem Blob-SHA;
- Airflow, Beam, Kafka, OpenLineage, ODCS, AWS Analytics Lens und öffentliche Agent-Skills als Referenzen genutzt, ohne Airflow, dbt, Kafka, Spark, Beam, Star Schema, Streaming oder Exactly-once als universellen Pflichtstack beziehungsweise Default zu erklären.

### Reliability und System-Observability

Neuer tool- und providerneutraler Hauptbereich für Zuverlässigkeitsziele, System-Observability, Betriebsreaktion und Resilience:

- klare Trennung von Agenten-Observability und Runtime-/System-Observability;
- Reliability entlang der Ebenen Objectives, Sensing, Response sowie Learning & Resilience strukturiert;
- SLI-Spezifikation, Messimplementierung, SLO, Messfenster und Error Budget getrennt modelliert; konkrete Zielwerte werden nicht ohne lokale Anforderungsgrundlage erfunden;
- `SLO ≠ SLA ≠ RTO/RPO` als zentrale Grenze festgeschrieben;
- System-Observability als Fähigkeit modelliert, relevante Zustands- und Betriebsfragen aus externer Evidence beantworten zu können; Metrics, Logs, Traces und weitere Telemetrieformen sind mögliche Signale, keine Definition von Observability;
- Alerting nach Actionability, Nutzer-/Serviceimpact, Symptom-vs.-Cause, Noise, Fensterung und Runbook-/Next-Action-Bezug statt universeller Thresholds oder Severitymodelle;
- Incident Response mit Impact, Rollen, Incident State, Mitigation, Kommunikation, Handoff und Fresh Recovery Evidence; Incident-Dringlichkeit erweitert keine Rechte und ersetzt keine Human Gates;
- Postmortems mit Timeline, Evidence, beitragenden Faktoren, Detection-/Response-/Recovery-Gaps und Follow-ups statt erzwungener Einzelursache;
- Capacity Planning als eigene Arbeitsdisziplin zwischen gemessener Belastungsgrenze und technischer Provisionierung; Peak, Wachstum, Saturation, Failure Domains, Lead Time, Headroom und Unsicherheit werden explizit;
- Recovery-Ziele RTO/RPO bleiben lokale Business-/Requirement-Werte; Reliability operationalisiert und prüft sie, während Backup/Restore/Failover technisch in den zuständigen Domänen bleiben;
- Resilience über Failure Domains, Dependency Health, Graceful Degradation und Recovery-Verhalten beschrieben; konkrete Architekturpatterns bleiben bei Software Architecture;
- Chaos Engineering und Game Days als kontrollierte Hypothesenexperimente mit Steady State, Blast Radius, Abort und Recovery statt als destruktiver Stunt oder Produktionspflicht;
- Toil als Signal für nicht nachhaltigen Betrieb eingeordnet, ohne universelle Prozentziele;
- Operational Readiness als zusammengesetzte Evidence und Workflow statt als Mega-Skill modelliert;
- acht neue Skills `slo-design`, `system-observability-design`, `alert-design`, `incident-response`, `incident-postmortem`, `capacity-planning`, `resilience-experiment` und `reliability-review`;
- alle acht Skills starten `experimental` mit `partial` Evalabdeckung;
- 48 Evalfälle definiert, sechs je Skill, einschließlich SLO-/RTO-Grenzen, Telemetrie-/PII-Fällen, Alert-Noise, Incident-Gates, Capacity-Evidence, Failure-Testing-vs.-Chaos und unabhängigen Reliability-Reviews; die Fälle sind definiert, nicht automatisch als ausgeführt oder bestanden zu verstehen;
- fünf Workflows `Reliability-Baseline-und-SLOs.md`, `Produktionsincident.md`, `Post-Incident-Learning.md`, `Resilience-Game-Day.md` und `Operational-Readiness-Review.md`;
- neues menschliches `Dokumentation/Skill-Handbuch-Reliability-und-System-Observability.md`;
- neue Capability `controlled-fault-injection-gated` für ausdrücklich freigegebene Resilience-Experiment-Ausführung;
- bestehende Grenzen in `Testing-und-QA/`, `Infrastruktur-und-DevOps/`, `Schnittstellen-und-Vertraege/` und `Agentenarbeit/` auf den realen Reliability-Bereich umgestellt;
- `failure-testing` mit `resilience-experiment` und `deployment-strategy` mit `slo-design`, `system-observability-design` und `reliability-review` verbunden;
- Skill-Katalog auf 95 zentrale Skills erweitert;
- Quellenbasis aus Google SRE, CNCF/OpenTelemetry, Principles of Chaos Engineering, ISO/IEC 25010 sowie AWS-/Azure-/GCP-Gegenprüfungen und ausgewählten aktuellen öffentlichen Agent-Skills, ohne provider- oder toolgebundene Defaults zu universalisieren.

### Infrastruktur und DevOps

Neuer tool- und providerneutraler Hauptbereich für Infrastructure as Code, Delivery-Automation und kontrollierte Infrastrukturänderungen:

- klare Zustandsgrenze `Desired State ≠ Actual State` mit expliziter Ownership von Configuration, Tool-/Controller-State und realem Zielzustand;
- Infrastructure as Code als reviewbare und reproduzierbare Zustandsbeschreibung statt Terraform-spezifische Universalregel modelliert;
- Drift als Befund mit bewusster Entscheidung zwischen Übernahme in Desired State und Rückführung des Actual State statt automatischer Korrekturanweisung;
- Change Preview, Plan, Review, Gate und Apply als getrennte Schritte mit der Grundregel `Preview ≠ Apply` und `Plan Review ≠ Apply Authorization`;
- Freshness von Plans/Previews und Grenzen von Dry-Run-/Simulationsevidence ausdrücklich berücksichtigt;
- Risikoklassen `READ / VALIDATE`, `BUILD`, `PLAN / PREVIEW`, `CHANGE / DEPLOY` und `DESTRUCTIVE / STATE / RECOVERY`;
- Environment-Parität als kontrollierte, dokumentierte Unterschiede statt Dogma „nur Values dürfen differieren“;
- CI-Pipelines als Orchestrierung von Triggern, DAG, Artifacts, Caches, Credentials, Environment-Grenzen und Gates; Teststrategie bleibt `Testing-und-QA/`;
- Build-Artefakte, Identität, Provenance und Reproduzierbarkeit mit Trennung `Build ≠ Deploy ≠ Release`;
- Container Build und Runtime Contract ohne Dockerpflicht, einschließlich Build-/Runtime-Trennung, Base-/Dependency-Pinning, Secret-Hygiene, Signals, Health und Runtime-Konfiguration;
- Deploymentstrategien Rolling, Blue-Green, Canary, Shadow, Recreate und Feature-gated Release risikobasiert statt als Pflichtmuster;
- Promotion, Pause, Abort und Rollback mit lokaler Health-/SLO-Evidence; konkrete Health-Schwellen bleiben beim späteren Reliability-/Produktkontext;
- Rollback ausdrücklich nicht als Undo bereits erfolgter Datenänderungen, Events oder externer Nebenwirkungen behandelt;
- GitOps als eigener fachlicher Schnitt wegen Continuous Reconciliation und dauerhafter Controller-Autorität; Desired-State-Merge kann bei Auto-Reconcile eine extern wirksame Aktion sein;
- Kubernetes als wichtige Referenzplattform für Controller, Workloads und Rollouts, aber nicht als universelle Infrastrukturvoraussetzung;
- Policy as Code als technische Decision-/Enforcement-Schicht eingeordnet; Inhalt von Security Policies bleibt `Sicherheit/`;
- Secrets, Permissions und Execution Boundaries mit getrennten Rechten für Read/Validate, Build, Preview und reale Change-/Recovery-Aktionen;
- Skills `infrastructure-as-code`, `infrastructure-change-review`, `ci-pipeline-design`, `container-build`, `deployment-strategy`, `gitops-design` und `infrastructure-review`;
- alle sieben Skills starten `experimental` mit `partial` Evalabdeckung;
- Evalpacks für alle sieben Skills mit Drift-, stale-Preview-, destructive-Change-, Secret-/Fork-, Container-Runtime-, Rollback-, GitOps- und Evidence-Grenzfällen;
- Workflows `Workflows/Infrastruktur-Aenderung.md` und `Workflows/Build-Deploy-und-Promotion.md`;
- menschliches `Dokumentation/Skill-Handbuch-Infrastruktur-und-DevOps.md`;
- Quellenbasis aus Terraform, OpenTofu, Kubernetes, OpenGitOps, Argo CD/Rollouts, OPA, SLSA, Docker Build sowie aktuellen offiziellen und Community-Agent-Skills;
- keine provider-/tool-spezifischen Defaults, festen Canary-Schwellen oder automatischen Apply-/Deploy-Freigaben zur zentralen Wahrheit erklärt.

### Schnittstellen und Verträge

Neuer technologieübergreifender Hauptbereich für Interface- und Contract-Engineering:

- Schnittstellen als beobachtbare Zusage zwischen Provider und Consumer statt bloß als Transport oder Schema modelliert;
- klare Grenze zu späterem Software Architecture: Architektur entscheidet, warum und wo eine Grenze existiert; Interface Design definiert die Zusagen über diese Grenze;
- Interaktionsstile HTTP, GraphQL, RPC/IDL, Events sowie Webhooks/Callbacks nach Consumer- und Kommunikationsanforderungen statt Transportdogma eingeordnet;
- öffentliche Request-/Response-/Message-Repräsentationen bewusst von internen Datenbank-, Klassen- und Frameworkmodellen getrennt;
- Schema- und Feldsemantik einschließlich required/optional, nullable/absent, Defaults, Enums und Fehlerverträgen;
- HTTP API Design mit bewusster Method-/Statussemantik, Collections, Pagination, Filtering, Ordering, Idempotenz, Retry und Concurrency;
- GraphQL-Schemaevolution und Deprecation als eigene Fachregel ohne unnötigen Format-Skill;
- RPC-/IDL-/Protobuf-Regeln für Field Numbers, Reserved Fields, generierten Code und die Trennung von Source- und Wire-Kompatibilität;
- Event-/Async-Verträge mit Producer/Consumer, Envelope/Payload, Delivery, Ordering, Duplicate-Verhalten, Replay, Dead Letter, Correlation und Schemaevolution;
- Webhooks und Callbacks als HTTP-basierte asynchrone Contracts eingeordnet; provider-spezifische Signatur-/Replay-Security bleibt lokal beziehungsweise in `Sicherheit/`;
- Auth-, Scope- und Tenant-Grenzen als beobachtbare Contract-Semantik;
- providerneutrales Compatibility-Modell aus Source-, Wire- und semantischer Kompatibilität plus realen Consumer-/Deploymentbedingungen;
- Change-Verdicts `COMPATIBLE`, `ROLLOUT-SENSITIVE`, `BREAKING` und `UNVERIFIED`;
- additive Syntax ausdrücklich nicht mit bewiesener semantischer Rückwärtskompatibilität gleichgesetzt;
- Versionierung, Deprecation, Migration, Sunset und Removal-Gates ohne universelle `/v1`-, SemVer- oder Supportfenster-Pflicht;
- Contract-First und maschinenlesbare Artefakte wie OpenAPI, GraphQL SDL, Protobuf/IDL und AsyncAPI mit eindeutiger lokaler Source of Truth;
- Skills `interface-design`, `http-api-design`, `event-contract-design`, `contract-change-review` und `interface-review`;
- alle fünf Skills starten `experimental` mit `partial` Evalabdeckung;
- Evalpacks für alle fünf Skills mit Architecture-/Framework-Near-Misses, DB-Leaks, Versionierungsdogma, Async-Delivery, Additive-vs.-Semantic-Compatibility, Source-/Wire-Trennung, rollout-sensitive Changes und fehlenden Baselines;
- vorhandenen Testing-Skill `contract-testing` mit `contract-change-review` und `interface-review` verbunden, ohne Design und Verifikation zusammenzulegen;
- Workflow `Workflows/Schnittstellenvertrag-Entwerfen-und-Aendern.md`;
- menschliches `Dokumentation/Skill-Handbuch-Schnittstellen-und-Vertraege.md`;
- Quellenbasis aus OpenAPI, HTTP RFCs, Google AIPs, GraphQL, Protobuf/gRPC, AsyncAPI, CloudEvents und aktuellen API-/Event-Agent-Skills;
- aktive Upstreams aus OpenAPI, Google AIPs, GraphQL, Protobuf und AsyncAPI semantisch sowie drei tatsächlich einflussreiche API-/Event-Skills per Blob-SHA registriert.

### Wissensmanagement / Knowledge Bases

Neuer toolneutraler Hauptbereich für persistente Wissensbasen und Knowledge Management:

- klare Trennung zwischen Recherche, Persistent Knowledge, Context Engineering, Dokumentation und technischer Retrieval-/RAG-Implementierung;
- Wissensmodell aus Raw Source, Derived Knowledge Unit, Synthese und Navigation;
- Capture, Ingest und Triage mit `search before create` und Update-vs.-Create statt Append-only-Wachstum;
- Provenance, Evidence und Source-of-Truth-Bezug mit Rückführbarkeit von Synthesen auf Eingabeeinheiten und Quellen;
- Wissensgranularität als eigenständig verwertbare Einheit statt maximaler Fragmentierung;
- Links, Relationen, Taxonomien, kontrolliertes Vokabular und Navigation ohne toolabhängige Pflichtmechanismen;
- Synthesen und Maps of Content mit sichtbaren Eingaben, Gegenbelegen und Unsicherheit;
- Widerspruchsbehandlung mit Trennung von Zeit-, Scope- und Definitionsunterschieden;
- Aktualität, Staleness und Lifecycle mit risikobasiertem Review statt universeller Prüffrist;
- Retrieval und Findability mit expliziter Regel `Retrievalscore ≠ Wahrheit` und `No-Hit ≠ sichere Abwesenheit`;
- Content Health für Dubletten, Orphans, kaputte Links, fehlende Provenance und Taxonomie-/Schema-Drift;
- Datenschutz und sensitives Wissen mit stärkerer Persistenzprüfung als bei kurzfristigem Kontext; Secrets gehören nicht als normale Wissenseinheiten in die Knowledge Base;
- Obsidian, Notion, Vector Stores, RAG und Knowledge Graphs als mögliche Adapter eingeordnet statt zu zentralen Standards erklärt;
- Skills `knowledge-base-design`, `knowledge-ingest`, `knowledge-distill`, `knowledge-synthesis`, `knowledge-maintenance`, `knowledge-query` und `knowledge-base-review`;
- alle sieben Skills starten `experimental` mit `partial` Evalabdeckung;
- Evalpacks für alle sieben Skills mit Tool-Bias-, Search-before-Create-, Provenance-, Bulk-Gate-, Distillation-, Synthesis-, Duplicate-/Orphan-, Query- und Review-Coverage-Fällen;
- Workflow `Workflows/Wissensbasis-Aufbauen-und-Pflegen.md` einschließlich Research-to-Knowledge- und Context-Übergang;
- menschliches `Dokumentation/Skill-Handbuch-Wissensmanagement.md`;
- Quellenbasis aus KCS, W3C PROV, ISO 30401, offiziellen Obsidian-/Notion-Mechanismen, OpenAI Retrieval sowie aktuellen Knowledge-Base-Skills;
- aktive Upstreams: KCS und OpenAI Knowledge Retrieval semantisch sowie `Ar9av/obsidian-wiki`, `obsidian-second-brain` und `knowledge-distill` per Blob-SHA.

### Context, Token-Effizienz und Long-Horizon-Agentenarbeit

`Agentenarbeit/` um die technische Betriebsseite von Context Engineering erweitert:

- Context Budget und Token-Effizienz als Optimierung von Informationswert, Qualität, Latenz und Kosten statt bloßer Token-Minimierung;
- providerneutrale Messsignale für Input-/Output-Tokens, Cache-Nutzung, Kontext- und Tool-Output-Größen, soweit die jeweilige Runtime diese tatsächlich liefert;
- Context Rot, Duplikate, Altstände, Widersprüche und Signalqualität als eigene Prüfachse;
- Context Compaction mit Fortsetzungsfähigkeit und Erhalt harter Constraints, Entscheidungen, Evidence, Sources of Truth und Gates als Qualitätskriterium;
- Long-Horizon-Handoffs für neue Sessions oder Agenten mit eigenständig verständlichem Fortsetzungszustand;
- Tool-Output-Offloading: deterministische Filterung, Aggregation oder Reduktion großer Rohresultate außerhalb des Modellkontexts, wenn dadurch kein benötigtes Signal verloren geht;
- providerneutrale Regeln für Prompt Caching und stabile Kontextpräfixe, ohne konkrete Cache-Semantik oder Modellgrenzen zentral festzuschreiben;
- klare Trennung `Active Context → Working State → Persistent Knowledge`; dauerhafte Wissensbasen werden nicht mit taskbezogenem Agentenzustand vermischt;
- vorhandenen Skill `context-engineering` geschärft und mit `partial` Evalabdeckung versehen;
- neue Skills `context-audit`, `context-compaction` und `session-handoff`, zunächst `experimental` mit `partial` Evalabdeckung;
- Evalpacks für alle vier Context-Skills mit Near-Miss-, Messfähigkeits-, Informationsverlust-, Handoff- und Knowledge-Base-Grenzfällen;
- Workflow `Workflows/Long-Horizon-Agentenarbeit.md`;
- menschliches `Dokumentation/Skill-Handbuch-Context-und-Long-Horizon.md`;
- Trace-Datenmodell und `trace-event.schema.yml` um optionale, metadata-first Context-/Usage-Signale und Compaction-/Handoff-Ereignisse erweitert;
- aktive Context-Upstreams aus Anthropic, OpenAI, LangChain und OpenTelemetry sowie die konkret verwendeten Skills `context-doctor` und OpenClaw `handoff` im zentralen Monitoring registriert;
- keine festen universellen Tokenquoten, Fenstergrenzen, Cachewerte oder Modellpreise als zentrale Wahrheit übernommen.

### Testing und QA

Neuer technologie- und frameworkneutraler Hauptbereich für Softwaretesting und Qualitätsevidence:

- risikobasierte Teststrategie statt pauschaler Testmengen oder Coverage-Ziele;
- Testebenen als Portfolio mit der kleinsten belastbaren Ebene für das jeweilige Risiko;
- Testdesign über Äquivalenzklassen, Grenzwerte, Entscheidungstabellen, Zustandsübergänge, kombinatorische Auswahl und Property-based Testing;
- klare Regeln für Test-Seams, Test Doubles und reale Dependencies ohne universelle Mocking-Doktrin;
- Testdaten, Isolation, Hermetik, Zeit-/Randomness-Kontrolle und Parallelisierung;
- Integration Testing und Contract Testing als getrennte Prüfachsen;
- End-to-End-Tests auf ausgewählte kritische Nutzer-/Geschäftsflows begrenzt;
- Flaky Tests als Defekt am Qualitätssignal; Retry ist Diagnose-/Mitigationswerkzeug und kein Root-Cause-Fix;
- kontrollierte Failure-/Recovery-Tests für Timeout, Teilfehler, Retry, Idempotenz und Recovery;
- klare Grenze zu späterem Reliability-/Chaos-Engineering;
- Coverage als Ausführungssignal, Mutation/Brechprobe als mögliche Wirksamkeitsprüfung;
- exploratives Testen mit Charter, Mission, Scope und Zeitbox;
- Release-Evidence mit `PASS`, `FAIL`, `BLOCKED`, `NOT RUN` und sichtbarer Restunsicherheit; Releaseentscheidung bleibt beim lokalen Gate;
- `verification-loop` um die Pflicht zu frischer, zum Completion Claim passender Evidence geschärft statt einen redundanten `verification-before-completion`-Skill anzulegen;
- Skills `test-strategy`, `test-design`, `integration-testing`, `contract-testing`, `e2e-testing`, `flaky-test-diagnosis`, `failure-testing`, `exploratory-testing` und `test-suite-review`;
- alle neun Skills zunächst `experimental` mit `partial` Evalabdeckung;
- Evalpacks für alle neun Skills mit positiven, Near-Miss-, Drift-, Flakiness-, Production-Safety- und Release-Gate-Fällen;
- Workflow `Workflows/Teststrategie-und-QA.md`;
- Quellenbasis aus ISTQB, Playwright, Pact, Testcontainers, Hypothesis, Stryker, Testing Library, Fowler, Google Testing Blog sowie aktuellen Testing-Agent-Skills von Anthropic, Currents und Superpowers.

### Datenbanken

Neuer engine-neutraler Hauptbereich für Datenbankarbeit:

- Datenmodellierung anhand von Domäne, Invarianten und realen Zugriffsmustern;
- reales Schema und verwendete Engine-/Driver-/ORM-Version als Source of Truth statt plausibler Annahmen;
- Schema-, Constraint- und Integritätsregeln;
- Query-Korrektheit, Parametrisierung, Tenant-/Scope-Sicherheit und Write-Wirkung;
- messungsbasierte Query-Performance mit bestehenden Indizes und Execution-Plan-Evidence;
- Transaktionen, Isolation, Locking, Race Conditions, Idempotenz und Retry;
- Migrationen, Backfills, Expand–Migrate–Contract, Rollback und Forward Fix;
- Connections, Pooling, Timeouts und Ressourcen als systemweite Kapazitätsfrage;
- Least Privilege und getrennte Diagnose-/Write-/Adminrechte;
- Backup, Restore und Recovery mit getestetem Restore statt bloß grünem Backup-Job;
- Monitoring und Ursachen-Diagnose;
- klare Scope-Grenze: Zustand innerhalb eines operativen Datenspeichers gehört zu `Datenbanken/`, systemübergreifende ETL-/ELT-/CDC-Pipelines zu einem späteren `Data Engineering/`;
- Risikoklassen `READ`, `WRITE`, `MIGRATION` und `DESTRUCTIVE / RECOVERY` mit steigenden Evidence- und Human-Gate-Anforderungen;
- Skills `database-design`, `database-query-review`, `query-performance`, `schema-migration`, `transaction-review`, `database-operations` und `database-review`;
- alle sieben Skills zunächst `experimental` mit `partial` Evalabdeckung;
- Evalpacks mit positiven, Near-Miss- und Safety-/Gate-Fällen;
- Workflow `Workflows/Datenbank-Aenderung.md`;
- Quellenbasis aus Supabase/Postgres, Neon, MongoDB, Redis, Prisma und lebender Primärdokumentation, ohne deren enginespezifische Regeln zu universalisieren.

### Skill Engineering

Neuer Meta-Bereich für Entwurf und Pflege von Agent-Skills:

- klare Skill-Schnitte und Verantwortungen;
- Progressive Disclosure mit kompaktem `SKILL.md` und optionalen `references/`, `scripts/` und `assets/`;
- Trigger- und Description-Design mit Near-Miss-Negativfällen;
- Input-/Output-/Evidence-Verträge;
- Capability Detection, Least-Privilege-nahe Anforderungen und ehrliche Fallbacks;
- Skill-Komposition ohne versteckte Mega-Orchestrierung;
- Review- und Evalregeln;
- Lifecycle `experimental → candidate → stable → deprecated → retired`;
- Skills `skill-authoring` und `skill-review`;
- Agent Skills Specification als externe Formatgrundlage eingeordnet.

### Skill-Katalog und Maturity

Neu beziehungsweise erweitert:

- `skill-catalog.yml` als maschinenlesbares Skill-Inventar;
- explizider Maturity-Status je Skill;
- Evalabdeckung `none`, `partial`, `core`, `broad`;
- Capability- und Related-Hinweise für relevante Skills;
- `Dokumentation/Skill-Katalog.md` als menschliche Erläuterung;
- konservative Einstufung: neue Bereiche zunächst `experimental`, ältere praktisch genutzte Skills überwiegend `candidate`; `stable` wird nicht automatisch vergeben;
- Datenbank- und Testing-und-QA-Skills als `experimental` mit `partial` Evalabdeckung;
- `context-engineering` bleibt `candidate` und erhält `partial` Evalabdeckung;
- `context-audit`, `context-compaction` und `session-handoff` als `experimental` mit `partial` Evalabdeckung;
- sieben Wissensmanagement-Skills als `experimental` mit `partial` Evalabdeckung ergänzt;
- fünf Schnittstellen-/Contract-Skills als `experimental` mit `partial` Evalabdeckung ergänzt;
- sieben Infrastruktur-/DevOps-Skills als `experimental` mit `partial` Evalabdeckung ergänzt;
- Gesamtbestand auf 87 zentrale Skills erweitert.

### Evals

Bereich `Evals/` erweitert:

- gemeinsames Evalfall-Schema;
- Trigger-, Behavior-, Outcome- und Regressionsevals;
- Near-Miss-Negative als eigener Qualitätsbestandteil;
- erste Evalpacks für `deep-research`, `docs-review`, `frontend-design`, `diagnose`, `code-review` und `skill-authoring`;
- zusätzliche Evalpacks für alle sieben Datenbank-Skills mit Schema-Source-of-Truth-, Query-Safety-, `EXPLAIN ANALYZE`-, Migration-, Concurrency-, Restore- und Review-Gate-Fällen;
- zusätzliche Evalpacks für alle neun Testing-und-QA-Skills, unter anderem zu fehlendem Oracle, Mock-/Contract-Drift, E2E-Near-Misses, Flakiness trotz Retry, Failure Testing vs. Chaos Engineering und Testsignal-Review;
- zusätzliche Evalpacks für `context-engineering`, `context-audit`, `context-compaction` und `session-handoff`, unter anderem zu fehlender Tokenmessung, Context Bloat, Compaction-Verlust, erfundenen Freigaben und Persistent-Knowledge-Near-Misses;
- zusätzliche Evalpacks für alle sieben Wissensmanagement-Skills, unter anderem zu Tool-Bias, Search-before-Create, Provenance, sensibler Persistenz, Bulk-Gates, Distillation, Synthese-Evidence, Duplicate-/Orphan-Entscheidungen, Retrieval und Review-Coverage;
- zusätzliche Evalpacks für alle fünf Schnittstellen-/Contract-Skills, unter anderem zu Transportdogma, Framework-Near-Misses, Datenbankmodell-Leaks, unbekannten Enum-Werten, Source-/Wire-Trennung, rollout-sensitive Changes und fehlenden Baselines;
- zusätzliche Evalpacks für alle sieben Infrastruktur-/DevOps-Skills, unter anderem zu Drift, State-Sensitivität, stale Previews, destructive Replacements, CI-Secret-Grenzen, Container-Runtime-Verträgen, Rollback-Grenzen und GitOps-Reconciliation;
- Skill-Katalog für diese Skills auf `eval_coverage: partial` aktualisiert.

### Sicherheit

Neuer Hauptbereich für agentische und Skill-Sicherheit:

- Prompt Injection und untrusted Input;
- Toolrechte und Least Privilege;
- Secrets und Datenexfiltration;
- Skill Supply Chain, Provenance, Pinning und Update Drift;
- MCP und externe Tools;
- Sandbox und Isolation;
- externe Aktionen und Bestätigung;
- Logging, Datenschutz und Telemetrie;
- Security Review für Skills;
- Skills `skill-security-review`, `prompt-injection-review` und `tool-permission-review`;
- OWASP Agentic Skills Top 10 und Agentic Applications Top 10 als Sicherheitsreferenzen eingeordnet.

### Workflows / Recipes

Bereich zur bewussten Skill-Komposition mit Recipes für:

- Deep Research;
- technische Dokumentation;
- Website-Neuentwicklung;
- Review bestehender Websites;
- Software Feature;
- Bugdiagnose;
- Bildserie;
- Datenbankänderung;
- Teststrategie und QA;
- Long-Horizon-Agentenarbeit;
- Aufbau und Pflege persistenter Wissensbasen;
- Entwurf und Änderung von Schnittstellenverträgen;
- kontrollierte Infrastrukturänderungen;
- Build, Deploy und Promotion.

Grundregel: Skills bleiben begrenzte Disziplinen; wiederkehrende Skill-Ketten werden als Workflow statt als Mega-Skill modelliert.

### Observability und Traceability

Erweitert:

- `Agentenarbeit/Trace-Datenmodell.md` für Task → Run → Skill/Workflow → Tool/Event → Evidence → Gate → Artefakt → Outcome;
- `Agentenarbeit/trace-event.schema.yml` als toolneutrale maschinenlesbare Ereignisstruktur;
- optionale Context-/Usage-Metadaten für Input-/Output-Tokens, Cache-Signale, Context- und Tool-Output-Größen sowie Compaction-/Handoff-Ereignisse ergänzt;
- Inhaltslogging bleibt optional und datenschutzsensibel; Metadaten sind vom vollständigen Prompt-/Toolinhalt getrennt.

### Dokumentationserstellung

Neuer Hauptbereich für technische und projektbezogene Dokumentation:

- Zielgruppe, Leserzustand und Dokumentzweck vor dem Schreiben klären;
- Dokumentationsmodus nach Tutorial, How-to, Reference und Explanation unterscheiden;
- Artefakttypen wie README, ADR und Runbook getrennt vom Diátaxis-Modus behandeln;
- Source-of-Truth- und Fachkorrektheitsregeln gegen plausible, aber erfundene Dokumentation;
- technischer Schreibstil mit stabiler Terminologie, Scanbarkeit und Accessibility;
- Beispiele, Befehle, Links und Parameter als verifizierbare Bestandteile behandeln;
- Navigation und Informationsarchitektur;
- Docs as Code, Ownership, Wartung und automatisierbare Checks;
- Dokumentationsreview mit Drift-Typen und Schweregraden;
- Vorlagen für README, ADR, Runbook, How-to und Tutorial;
- Skills `docs-plan`, `technical-writing`, `readme`, `tutorial`, `how-to`, `reference-docs`, `explanation-docs`, `adr`, `runbook` und `docs-review`.

### Quellen- und Upstream-Monitoring

Erweitert und vollständig auditiert:

- `Dokumentation/Quellenregister.md` auf Monitoring-Schema v2 erweitert;
- `Dokumentation/upstream-sources.yml` unterscheidet `exact-sha` für konkrete GitHub-Dateien und `semantic-review` für lebende Web-/Produktdokumentation;
- monatliche und quartalsweise Cadence für unterschiedlich volatile Quellen;
- vollständiger bereichsübergreifender Audit in `Dokumentation/Upstream-Audit-2026-08-23.md` dokumentiert;
- mutable Upstreams aus Programmieren, Schreiben, Bildarbeit, Webentwicklung, Recherche, Dokumentationserstellung und relevanten Grundlagen klassifiziert;
- `Schreiben/Quellen-und-Inspirationen.md` und `Programmieren/Quellen-und-Inspirationen.md` ergänzt;
- konkrete Matt-Pocock-Engineering-Skills für TDD, Diagnose, Code-Review und Domain Modeling per Blob-SHA registriert;
- lebende Adobe-/Midjourney-Bilddokumentation semantisch registriert;
- weitere tatsächlich verwendete Web- und Research-Skills mit geprüftem Blob-SHA ergänzt;
- langsamere Leitfäden wie HAX, Google Developer Style Guide, Write the Docs und Good Docs Project quartalsweise eingeordnet;
- Datenbank-Upstreams aus Supabase, Neon, MongoDB, Redis und Prisma sowie lebende Postgres-/Migration-Dokumentation in die Quellenpflege aufgenommen;
- Testing-und-QA-Upstreams aus Anthropic, Currents und Superpowers per Blob-SHA sowie ISTQB, Playwright, Pact und Testcontainers semantisch registriert;
- Context-/Long-Horizon-Upstreams aus Anthropic, OpenAI, LangChain und OpenTelemetry semantisch sowie `context-doctor` und OpenClaw `handoff` per Blob-SHA registriert;
- Wissensmanagement-Upstreams aus KCS und OpenAI Retrieval semantisch sowie `obsidian-wiki`, `obsidian-second-brain` und `knowledge-distill` per Blob-SHA registriert;
- Schnittstellen-/Contract-Upstreams aus OpenAPI, Google AIPs, GraphQL, Protobuf und AsyncAPI semantisch sowie drei konkret verwendete API-/Event-Skills per Blob-SHA registriert;
- Infrastruktur-/DevOps-Upstreams aus Terraform, OpenTofu, Kubernetes, OpenGitOps, Argo Rollouts, OPA, SLSA und Docker Build semantisch sowie HashiCorp-, Flux- und ausgewählte IaC/CI/Container/Deployment-Skills per Blob-SHA registriert;
- stabile HTTP-/Problem-Details-/Deprecation-RFCs und weitere formatbezogene Referenzen bewusst in der Fachquellendatei statt als künstliche schnelle Sync-Dependencies geführt;
- W3C PROV, ISO 30401 und toolbezogene Hilfedokumentation als stabile Fachreferenzen im Bereich dokumentiert statt künstlich als schnelle mutable Dependencies zu behandeln;
- Papers, datierte Research-Artikel und reine Discovery-Kataloge bewusst nicht als künstliche Sync-Dependencies behandelt;
- Grundregel bleibt: Upstream-Änderung ist Review-Signal, kein automatischer Sync;
- monatlicher `KI-Regeln Monatscheck` auf das Monitoring-Schema und Infrastruktur/DevOps als eigenes Fachfeld erweitert.

### Recherche

Neuer Hauptbereich für KI-gestützte Websuche und Deep Research:

- fünf Research-Modi von Lookup bis Literature Research;
- Rechercheplanung mit Teilfragen, Perspektiven und Coverage-Kriterien;
- claimbezogene Quellenstrategie mit Primärquellen-, Aktualitäts- und Unabhängigkeitsprüfung;
- Suchtreffer und Snippets ausdrücklich nur als Leads, nicht als Evidenz;
- Claim-Evidence-Ledger und Zitationshygiene;
- Triangulation, Widerspruchsanalyse und qualitative Confidence;
- Coverage Loop statt bloßer Quellenzählung;
- Synthese nach Erkenntnis statt nach Quellenliste;
- Web-Sicherheitsregeln gegen Prompt Injection und unerlaubte Aktionseskalation;
- Quellen- und Inspirationssammlung zu OpenAI Deep Research, Firecrawl, PracticalSwan, Hermes, STORM, LangChain DeepAgents, Microsoft Research Skills und weiteren öffentlichen Research-Skills;
- Skills `web-search`, `research-plan`, `deep-research`, `source-evaluation`, `claim-verification`, `research-synthesis` und `citation-audit`.

### Webentwicklung

Neuer Hauptbereich für Gestaltung und Entwicklung von Websites und Weboberflächen:

- Designrichtung und visuelle Identität vor Umsetzung;
- Informationsarchitektur und Greyboxing als eigene Phase;
- Typografie-, Farb-, Spacing- und Rhythmusregeln;
- Content- und Anti-Slop-Regeln gegen generische KI-Webtexte und Fake-Belege;
- responsive Gestaltung und Interaktionszustände;
- unabhängiger Webdesign-Review;
- Komponentenarchitektur mit Komposition vor Konfigurationsexplosion;
- Accessibility als Qualitätsgate;
- messungsbasierte Frontend-Performance;
- responsive Implementierung;
- Render- und Browser-Verifikation;
- Quellen- und Inspirationssammlung zu Anthropic `frontend-design`, Impeccable, Vercel Agent Skills und weiteren öffentlichen Skill-Sammlungen;
- Skills `frontend-design`, `design-system`, `greybox`, `web-content`, `web-design-review`, `accessibility-review`, `frontend-performance` und `visual-verification`.

### Dokumentation

Aktualisiert:

- Haupt-README um `Webentwicklung/`, `Recherche/`, `Wissensmanagement/`, `Schnittstellen-und-Vertraege/`, `Infrastruktur-und-DevOps/`, `Dokumentationserstellung/`, `Skill-Engineering/`, `Sicherheit/`, `Evals/`, `Workflows/`, `Datenbanken/` und `Testing-und-QA/` erweitert und um Context-/Long-Horizon-Agentenarbeit geschärft;
- menschliche Doku um Quellenregister, vollständigen Upstream-Audit, Skill-Katalog und zusätzliche Skill-Handbücher einschließlich `Skill-Handbuch-Context-und-Long-Horizon.md`, `Skill-Handbuch-Wissensmanagement.md`, `Skill-Handbuch-Schnittstellen-und-Vertraege.md` und `Skill-Handbuch-Infrastruktur-und-DevOps.md` ergänzt;
- Projektmanifest und Nutzungsanleitung um Research-, Wissensmanagement-, Schnittstellen-/Contract-, Infrastruktur-/DevOps-, Web-, Dokumentations-, Datenbank-, Testing-/QA- und Long-Horizon-Arbeit ergänzt.

## v2026.08

### Grundlagen

Hinzugefügt beziehungsweise zentralisiert:

- allgemeine Zusammenarbeit mit KI;
- Datenschutz und Kontext;
- Mensch-KI-Interaktion;
- kalibriertes Vertrauen und Denkautonomie;
- Quellen und Inspirationen für Human-AI-Interaction und Selbstentwicklung.

### Arbeitsweisen

Hinzugefügt:

- systematische Problemlösung;
- Reflexion und Selbstverbesserung als Lernloop;
- Zielarbeit und Umsetzung;
- Skills `reflektierender-dialog`, `entscheidungsunterstuetzung` und `ziel-reflexions-loop`.

### Agentenarbeit

Hinzugefügt:

- Context Engineering;
- Harness Engineering;
- Task Graphs und kontrollierte Loops;
- Delegation Contracts und Evidence Bundles;
- Agent Evals;
- Observability und Traceability;
- Human Gates;
- Entropie- und Driftmanagement;
- Skills `context-engineering`, `task-graph`, `verification-loop`, `delegation-contract` und `agent-eval`.

### Schreiben

Hinzugefügt beziehungsweise generalisiert:

- natürlicher Schreibstil;
- kreatives Schreiben;
- strukturelles Stilreview;
- Schutz einfacher Verben vor künstlicher Aufblähung;
- KI-typische Muster als Warnsignal statt Wort-Blacklist;
- Trennung von Meta-Kommunikation und Endprodukt;
- Skills `natuerliches-schreiben`, `kreatives-schreiben` und `stilreview`.

### Bildarbeit

Neuer Hauptbereich für konsistente Einzelbilder und Bildserien:

- Quellen- und Prioritätenlogik;
- getrennte Betrachtung von Identitäts-, Stil-, Struktur- und Kontinuitätskonsistenz;
- Entitätsbibeln;
- Szenenplanung und Bild-Pre-Briefs;
- Zustandsmatrizen;
- Bildreview und Freigabestufen;
- Serien- und Abschlussaudit;
- Skills `bild-prebrief`, `entitaetsbibel`, `serien-kontinuitaetscheck` und `bildreview`.

### Programmieren

Hinzugefügt beziehungsweise generalisiert:

- Fünf-Gate-Entwicklungsprozess;
- Agentenanweisungen für Softwarearbeit;
- Skills `domain-modeling`, `tdd`, `diagnose` und `code-review`.

### Dokumentation und Governance

Hinzugefügt:

- menschlich lesbare Nutzungsanleitung;
- Skill-Handbuch;
- definierter monatlicher Radar-Check;
- vierteljährlicher Repo-Audit;
- datumsbasierte Versionierung;
- Projektmanifest-Vorlage;
- Changelog als nachvollziehbare Änderungshistorie.

## Pflegehinweis

Rein redaktionelle Änderungen müssen nicht zwingend einen neuen Versionsstand erzeugen. Änderungen, die Verhalten, Prioritäten oder empfohlene Nutzung von Regeln und Skills beeinflussen, sollen dagegen im Changelog sichtbar werden.