# Changelog

Dieses Dokument hält relevante Änderungen am Repository fest.

Die Versionierung ist datumsbasiert. Eine Version beschreibt einen bewusst nutzbaren Stand des zentralen Regelwerks.

## Unreleased

Noch nicht als eigener Versionsstand veröffentlichte Änderungen werden zunächst hier gesammelt.

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
- Schnittstellen-/Contract-Upstreams aus OpenAPI, Google AIPs, GraphQL, Protobuf und AsyncAPI semantisch sowie drei tatsächlich verwendete API-/Event-Skills per Blob-SHA registriert;
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