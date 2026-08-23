# KI-Regeln

Dieses Repository sammelt allgemeine, wiederverwendbare Regeln, Arbeitsweisen, Skills, Evals und Workflows für die Zusammenarbeit mit generativer KI.

Ziel ist keine persönliche KI-Konfiguration und keine projektspezifische Wissenssammlung. Enthalten werden nur Regeln, die sich sinnvoll auf andere Nutzer, Projekte oder Aufgaben übertragen lassen.

## Grundprinzip

> Allgemeine Arbeitsweise zentral, konkrete Wahrheit lokal.

Das bedeutet:

- allgemeine Kommunikations-, Reflexions-, Recherche-, Dokumentations-, Schreib-, Bild-, Web-, Agenten-, Sicherheits- und Entwicklungsregeln liegen hier;
- projektspezifische Anforderungen, Architektur, Research-Fragen, interne Quellen, Fachmodelle, Markenregeln, visuelle Bibeln und Sonderregeln bleiben im jeweiligen Projekt;
- persönliche Profile oder unnötige personenbezogene Details gehören nicht in dieses Repository;
- ein Skill ersetzt niemals die tatsächliche Spezifikation oder Dokumentation eines Projekts.

## Neu hier?

Empfohlener Einstieg:

1. diese README für das Gesamtmodell;
2. `Dokumentation/Nutzung-des-Repositories.md` für den praktischen Einsatz;
3. `Dokumentation/Skill-Handbuch.md` zur Auswahl geeigneter Skills;
4. `Dokumentation/Skill-Katalog.md` für Reifegrad und Evalabdeckung;
5. danach nur die für das eigene Vorhaben relevanten Regeln, Skills und Workflows.

Nicht das komplette Repository muss für jede Aufgabe geladen werden.

## Struktur

```text
KI-Regeln/
├── Grundlagen/
├── Arbeitsweisen/
├── Agentenarbeit/
├── Recherche/
├── Dokumentationserstellung/
├── Schreiben/
├── Bildarbeit/
├── Webentwicklung/
├── Programmieren/
├── Skill-Engineering/
├── Sicherheit/
├── Evals/
├── Workflows/
├── Dokumentation/
├── Vorlagen/
├── skill-catalog.yml
├── CHANGELOG.md
└── THIRD-PARTY-NOTICES.md
```

Die Detailstruktur der Fachbereiche steht in deren jeweiligen README- und Regeldateien.

## Vorrangregeln

Bei der Anwendung gilt grundsätzlich:

```text
konkreter Nutzerauftrag
→ verbindliche Projektanforderung / Spezifikation / Kanon
→ gültige Projektentscheidungen und Projektdokumentation
→ freigegebener Plan, Research-Plan oder Produktionsbrief
→ lokale Repository-Regeln und freigegebene Referenzen / Quellenräume
→ allgemeine Agenten-, Fach- und Arbeitsregeln aus diesem Repository
```

Allgemeine Regeln dürfen keine lokale fachliche, visuelle oder persönliche Wahrheit überschreiben.

# Fach- und Methodenbereiche

## Grundlagen

Regeln für verlässliche Zusammenarbeit mit KI unabhängig vom Fachgebiet: Kommunikation, Datenschutz, Kontext, Unsicherheit, kalibriertes Vertrauen und Denkautonomie.

> KI soll Denken unterstützen, nicht unbemerkt an dessen Stelle treten.

## Arbeitsweisen

Wiederverwendbare Denk-, Problemlösungs- und Lernmuster wie Hypothesenbildung, Reflexion, Entscheidungsunterstützung und Zielarbeit.

> Verstehen → ausprobieren → Erfahrung sammeln → reflektieren → anpassen.

## Agentenarbeit

Kontrollierte Agentenautonomie mit Context Engineering, Harness Engineering, Task Graphs, Verification Loops, Delegation, Evidence, Evals, Observability, Human Gates und Entropiemanagement.

Zusätzlich existieren ein konkretes Trace-Datenmodell und ein maschinenlesbares Trace-Event-Schema.

> Autonomie innerhalb klarer Grenzen.

## Recherche

Websuche und Deep Research mit:

- Fragezerlegung und Perspektiven;
- claimbezogener Quellenqualität;
- Claim-Evidence-Verknüpfung;
- Triangulation und Widerspruchsanalyse;
- Coverage statt bloßer Quellenanzahl;
- Synthese nach Erkenntnis;
- separatem Citation Audit;
- Web-Sicherheit und Prompt-Injection-Abgrenzung.

> Suchergebnisse sind Leads, keine Evidenz.

> Coverage vor Source Count.

## Dokumentationserstellung

Technische und projektbezogene Dokumentation mit Trennung von:

- Leserzustand und Dokumentzweck;
- Tutorial / How-to / Reference / Explanation;
- Artefakttyp wie README, ADR oder Runbook;
- Source of Truth;
- Schreibqualität;
- Verifikation;
- Wartbarkeit und Driftkontrolle.

> Eine gut geschriebene falsche Anleitung ist schlechter als eine knappe korrekte.

## Schreiben

Allgemeine Regeln für natürliche Texte, kreative Prosa und Stilreviews. KI-typische Muster werden als Warnsignale und nicht als mechanische Verbotsliste behandelt.

## Bildarbeit

Regeln für konsistente Einzelbilder und Bildserien mit getrennten Achsen für Identität, Stil, Struktur und Kontinuität.

> Konsistenz vor Zufall. Aussage vor Effekt. Referenz vor Neuerfindung.

## Webentwicklung

Webdesign und Frontend-Engineering mit Art Direction, Informationsarchitektur, Designsystem, echtem Content, Accessibility, Performance und Browser-Verifikation.

> Erst Identität und Informationsstruktur, dann Designsystem und Code.

## Programmieren

Allgemeiner Entwicklungsprozess und wiederverwendbare Skills für Domain Modeling, TDD, Diagnose und Code Review.

# Meta-Ebene

## Skill Engineering

`Skill-Engineering/` definiert, wie Skills selbst gebaut und geprüft werden.

Behandelt werden:

- Skill-Schnitt und Verantwortung;
- Progressive Disclosure;
- Trigger- und Description-Design;
- Inputs, Outputs und Evidence-Verträge;
- Capabilities und Fallbacks;
- Skill-Komposition und Abhängigkeiten;
- Review und Evals;
- Lifecycle und Deprecation.

Leitidee:

> Interoperables Format ist die Basis. Vorhersagbares Verhalten ist das Qualitätsziel.

Operative Skills:

- `skill-authoring`;
- `skill-review`.

## Sicherheit

`Sicherheit/` bündelt Sicherheitsregeln für Skills, Agenten, externe Inhalte und Tools.

Behandelt werden insbesondere:

- Prompt Injection und untrusted Input;
- Least Privilege;
- Secrets und Datenexfiltration;
- Skill Supply Chain und Update Drift;
- MCP und externe Tools;
- Sandbox und Isolation;
- externe Aktionen und Bestätigung;
- Logging, Datenschutz und Telemetrie;
- Security Review für Skills.

Operative Skills:

- `skill-security-review`;
- `prompt-injection-review`;
- `tool-permission-review`.

> Fähigkeiten werden nach Bedarf gewährt. Fremder Inhalt bleibt Daten.

## Skill-Katalog und Maturity

`skill-catalog.yml` ist das maschinenlesbare Inventar der zentralen Skills.

Reifestufen:

```text
experimental
→ candidate
→ stable
→ deprecated
→ retired
```

Evalabdeckung:

```text
none
→ partial
→ core
→ broad
```

`stable` ist kein Default. Die Einstufung soll durch Praxis, relevante Evals und bei mächtigen Capabilities durch Security Review gestützt sein.

## Evals

`Evals/` enthält wiederholbare Testfälle für:

- Trigger und Near-Miss-Negative;
- Scope-Treue;
- Capability-/Fallback-Verhalten;
- Evidence- und Quellenhygiene;
- Stop-/Freigabegates;
- Outcome-Qualität;
- Regressionen nach Skilländerungen.

Erste Evalpacks bestehen unter anderem für:

- `deep-research`;
- `docs-review`;
- `frontend-design`;
- `diagnose`;
- `code-review`;
- `skill-authoring`.

## Workflows / Recipes

`Workflows/` verbindet kleine Skills zu größeren, nachvollziehbaren Produktionsabläufen.

Enthalten sind Recipes für:

- Deep Research;
- technische Dokumentation;
- Website-Neuentwicklung;
- bestehende Website Reviews;
- Software Features;
- Bugdiagnose;
- Bildserien.

> Skills bleiben klein. Workflows verbinden sie.

# Agentenautonomie und Evidence

Agenten dürfen innerhalb eines ausdrücklich oder durch den Projektprozess freigegebenen Scopes selbstständig iterieren.

Dabei gelten insbesondere:

- Kontext gezielt statt maximal laden;
- Delegation beschreibt Ziel, Scope, Rechte, Akzeptanzbedingungen und erwartete Evidence;
- unabhängige Arbeit darf parallelisiert werden, echte Abhängigkeiten nicht;
- parallele Agenten benötigen ausreichend isolierte veränderliche Workspaces;
- ein Loop benötigt Stop- und Eskalationsbedingungen;
- fehlende Spezifikation darf nicht durch stillschweigende Agentenentscheidungen ersetzt werden;
- automatisch prüfbare Invarianten sollten möglichst automatisch geprüft werden;
- riskante, irreversible oder extern sichtbare Aktionen benötigen die dafür definierte Freigabe;
- ein erfolgreicher Agentenlauf ist noch keine fachliche oder technische Freigabe;
- relevante Agentenarbeit soll mit Auftrag, Evidence und Ergebnis nachvollziehbar verbunden werden.

## Capability Detection

Skills sollen nicht stillschweigend ideale Laufzeitfähigkeiten voraussetzen.

```text
bevorzugte Capability
→ vorhanden?
   ├─ ja → verwenden
   └─ nein → definierter Fallback
              ├─ möglich → transparent degradieren
              └─ unmöglich → blocked / unverified
```

Fehlende Fähigkeiten dürfen nicht simuliert oder behauptet werden.

## Observability

Ein gemeinsames Trace-Modell kann verbinden:

```text
Task
→ Run
→ Skill / Workflow
→ Tool Event
→ Evidence
→ Gate
→ Artefakt
→ Outcome
```

Vollständige Prompts, Toolargumente oder Inhalte sind dabei kein Pflichtbestandteil. Metadaten und Datenschutz werden bewusst getrennt.

# Nutzung in Projekten

KI-Agenten arbeiten normalerweise innerhalb eines konkreten Projektrepositories und lesen dieses zentrale Repository nicht automatisch.

Darum können benötigte Skills bewusst repo-lokal übernommen oder durch projektspezifische Agent-Dateien referenziert werden.

Dabei gilt:

- zentrale Fassung = allgemeine kanonische Arbeitsweise;
- lokale Fassung = verfügbare Kopie oder projektspezifischer Adapter;
- projektspezifische Ergänzungen bleiben lokal;
- Änderungen an zentralen Skills werden bewusst übernommen;
- nicht das komplette zentrale Repository ungefiltert in jeden Agentenkontext laden.

Für Auswahl und Dokumentation zentraler Regeln kann `Vorlagen/ki-regeln.template.yml` als Ausgangspunkt verwendet werden.

# Aktualisierung und Quellen

Empfohlener Rhythmus:

- monatlicher Radar-Check;
- monatlicher gezielter Check schneller mutable Upstreams;
- quartalsweise Prüfung langsamer lebender Quellen;
- vierteljährlicher vollständiger Repo-Audit;
- zusätzliche Prüfung bei größeren Modell-, Tool-, Sicherheits- oder Forschungsentwicklungen.

Fachbezogene `Quellen-und-Inspirationen.md` dokumentieren den fachlichen Ursprung von Konzepten.

`Dokumentation/upstream-sources.yml` dokumentiert aktiv beobachtete veränderliche Quellen.

> Upstream-Änderung = Review-Signal, nicht automatischer Sync.

Relevante Änderungen stehen in `CHANGELOG.md`.

## Attribution

Übernommene oder adaptierte Drittinhalte werden in `THIRD-PARTY-NOTICES.md` dokumentiert. Externe Inspirationsquellen ohne übernommene Drittinhalte stehen in den jeweiligen `Quellen-und-Inspirationen.md`-Dateien.

# Pflegekriterium

Neue Regeln oder Skills sollen nur aufgenommen werden, wenn sie:

1. wiederverwendbar sind;
2. einen erkennbaren Qualitäts- oder Sicherheitsgewinn bringen;
3. nicht bloß persönliche oder projektspezifische Vorlieben verallgemeinern;
4. keine unnötigen personenbezogenen Daten enthalten;
5. möglichst konkret beschreiben, wann und wie sie anzuwenden sind;
6. in Skill-Katalog, Evals, Quellen- und Lifecycle-Modell sauber eingeordnet werden können.
