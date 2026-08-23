# KI-Regeln

Dieses Repository sammelt allgemeine, wiederverwendbare Regeln, Arbeitsweisen und Skills für die Zusammenarbeit mit generativer KI.

Ziel ist keine persönliche KI-Konfiguration und keine projektspezifische Wissenssammlung. Enthalten werden nur Regeln, die sich sinnvoll auf andere Nutzer, Projekte oder Aufgaben übertragen lassen.

## Grundprinzip

> Allgemeine Arbeitsweise zentral, konkrete Wahrheit lokal.

Das bedeutet:

- allgemeine Kommunikations-, Schreib-, Bild-, Analyse-, Agenten- und Entwicklungsregeln liegen hier;
- projektspezifische Anforderungen, Architektur, Figuren, Fachbegriffe, visuelle Bibeln und Sonderregeln bleiben im jeweiligen Projekt;
- persönliche Profile, Gesundheitsdaten, Familieninformationen oder andere nicht notwendige personenbezogene Details gehören nicht in dieses Repository;
- ein Skill ersetzt niemals die tatsächliche Spezifikation oder Dokumentation eines Projekts.

## Struktur

```text
KI-Regeln/
├── Grundlagen/
│   ├── Zusammenarbeit-mit-KI.md
│   └── Datenschutz-und-Kontext.md
├── Arbeitsweisen/
│   └── Problemloesung.md
├── Agentenarbeit/
│   ├── README.md
│   ├── Context-Engineering.md
│   ├── Harness-Engineering.md
│   ├── Task-Graph-und-Loops.md
│   ├── Delegation-und-Evidence.md
│   ├── Agent-Evals.md
│   ├── Observability-und-Traceability.md
│   ├── Human-Gates-und-Freigaben.md
│   ├── Entropie-und-Garbage-Collection.md
│   ├── Quellen-und-Inspirationen.md
│   └── Skills/
│       ├── context-engineering/SKILL.md
│       ├── task-graph/SKILL.md
│       ├── verification-loop/SKILL.md
│       ├── delegation-contract/SKILL.md
│       └── agent-eval/SKILL.md
├── Schreiben/
│   ├── Agent-Anweisungen.md
│   ├── Schreibstil.md
│   ├── Kreatives-Schreiben.md
│   ├── Stilreview.md
│   └── Skills/
│       ├── natuerliches-schreiben/SKILL.md
│       ├── kreatives-schreiben/SKILL.md
│       └── stilreview/SKILL.md
├── Bildarbeit/
│   ├── README.md
│   ├── Quellen-und-Prioritaeten.md
│   ├── Stil-und-Referenzsysteme.md
│   ├── Charaktere-Objekte-und-Orte.md
│   ├── Szenenplanung-und-Komposition.md
│   ├── Kontinuitaet-und-Zustandsmatrix.md
│   ├── Bildpruefung-und-Freigabe.md
│   ├── Serienproduktion-und-Abschlussaudit.md
│   ├── Quellen-und-Inspirationen.md
│   └── Skills/
│       ├── bild-prebrief/SKILL.md
│       ├── entitaetsbibel/SKILL.md
│       ├── serien-kontinuitaetscheck/SKILL.md
│       └── bildreview/SKILL.md
├── Programmieren/
│   ├── Entwicklungsprozess.md
│   ├── Agent-Anweisungen.md
│   └── Skills/
│       ├── code-review/SKILL.md
│       ├── diagnose/SKILL.md
│       ├── domain-modeling/SKILL.md
│       └── tdd/SKILL.md
├── Vorlagen/
│   └── AGENTS.template.md
└── THIRD-PARTY-NOTICES.md
```

## Ebenen

### 1. Grundlagen

Regeln für verlässliche Zusammenarbeit mit KI unabhängig vom Fachgebiet: Quellen, Unsicherheit, Kommunikation, Kontext und Datenschutz.

### 2. Arbeitsweisen

Wiederverwendbare Denk- und Problemlösungsmuster wie Hypothesenbildung, iterative Bearbeitung und überprüfbare Entscheidungen.

### 3. Agentenarbeit

Regeln für kontrollierte Agentenautonomie unabhängig vom konkreten Fachgebiet.

Der Bereich behandelt insbesondere:

- `Context Engineering` – den kleinsten ausreichenden, aktuellen Kontext bereitstellen;
- `Harness Engineering` – Regeln durch Tests, Linter, Schemas, Rechte, Isolation und andere technische Grenzen unterstützen;
- `Task Graphs` – komplexe Arbeit in abhängige und überprüfbare Knoten zerlegen, ohne jeden Arbeitsschritt zu mikromanagen;
- `Verification Loops` – innerhalb eines freigegebenen Scopes arbeiten, prüfen, diagnostizieren und korrigieren;
- `Delegation Contracts` – Ziel, Scope, Befugnisse, Akzeptanzbedingungen und erwartete Evidence vorab klären;
- `Evidence Bundles` – Ergebnisse mit tatsächlichen Nachweisen statt bloßem Fertig-Status übergeben;
- `Agent Evals` – Produktqualität und Agentenprozessqualität getrennt und reproduzierbar prüfen;
- `Observability und Traceability` – Auftrag, Agentenlauf, Evidence, Artefakt und Freigabe nachvollziehbar verbinden;
- `Human Gates` – Why Loop und How Loop trennen und klar definieren, welche Entscheidungen nicht autonom erfolgen dürfen;
- `Entropiemanagement` – Drift und schlechte Repository-Muster erkennen, bevor Agenten sie weiter vervielfältigen.

Leitgedanke:

> Autonomie innerhalb klarer Grenzen.

Enthaltene Skills:

- `context-engineering` – relevanten Agentenkontext auswählen und Quellen der Wahrheit erhalten;
- `task-graph` – komplexe Arbeit in abhängige, überprüfbare Knoten zerlegen;
- `verification-loop` – kontrolliert iterieren, bis Nachweis oder Stop-Kriterium erreicht ist;
- `delegation-contract` – Auftrag, Grenzen, Rechte, Stop-Bedingungen und Evidence definieren;
- `agent-eval` – reproduzierbar prüfen, ob ein Agent Ergebnis- und Prozessanforderungen einhält.

### 4. Schreiben

Allgemeine Regeln für natürliche Texte, kreative Prosa und strukturelle Stilreviews.

Enthaltene Skills:

- `natuerliches-schreiben` – klare, glaubwürdige Texte ohne unnötige KI-, Werbe- oder Managementsprache;
- `kreatives-schreiben` – Szene, Figurenstimme, räumliche Klarheit und kanontreue Wirkung;
- `stilreview` – Muster erkennen, aber nur nach Kontextprüfung ändern.

### 5. Bildarbeit

Allgemeine Regeln für konsistente Einzelbilder und Bildserien mit generativer KI.

Der Bereich trennt insbesondere:

- **Identitätskonsistenz** – dieselbe Figur, dasselbe Objekt oder derselbe Ort bleibt wiedererkennbar;
- **Stilkonsistenz** – Bilder gehören sichtbar zur selben visuellen Welt;
- **Struktur- und Kompositionskonsistenz** – Perspektive und Bildorganisation werden bewusst gesteuert;
- **Kontinuitätskonsistenz** – sichtbare Zustände stimmen zum richtigen Zeitpunkt innerhalb einer Serie.

Weitere Schwerpunkte sind Quellenpriorität, Referenzsysteme, Entitätsbibeln, Szenen-Pre-Briefs, Zustandsmatrizen, Review-Stufen, Schutz vor Endlosschleifen und Abschlussaudits für komplette Bildserien.

Leitgedanke:

> Konsistenz vor Zufall. Aussage vor Effekt. Referenz vor Neuerfindung.

Enthaltene Skills:

- `bild-prebrief` – Moment, Aussage, Komposition, Entitäten, Zustand und Ausschlüsse vor einer Generierung klären;
- `entitaetsbibel` – wiederkehrende Figuren, Objekte, Fahrzeuge, Kreaturen oder Orte stabil definieren;
- `serien-kontinuitaetscheck` – Bildfolgen auf Identitäts-, Stil-, Struktur- und Zustandsdrift prüfen;
- `bildreview` – zwischen Keeper, lokalem Feinschliff und Neubau unterscheiden.

Projektkonkrete Charakterdesigns, Bildkanon und visuelle Sonderregeln bleiben im jeweiligen Projekt.

### 6. Programmieren

Allgemeiner Fünf-Gate-Prozess und wiederverwendbare Agent-Skills für Softwarearbeit.

Enthaltene Skills:

- `domain-modeling` – Begriffe, Fachobjekte und Grenzen schärfen;
- `tdd` – kleine Red/Green-Umsetzungsschnitte;
- `diagnose` – reproduzierbare Root-Cause-Diagnose;
- `code-review` – tatsächlichen Diff gegen Anforderung und Repository-Standards prüfen.

Die Regeln aus `Agentenarbeit/` ergänzen diesen Prozess. Ein innerer Agentenloop darf insbesondere keine Planungs-, Review- oder Freigabegates überspringen.

### 7. Projektregeln

Projektregeln gehören nicht hierher. Beispiele sind konkrete Produktanforderungen, Serienkanon, Charaktermerkmale, visuelle Referenzen, Fachmodelle, Releasewege oder technische Sonderfälle eines einzelnen Repositories.

## Was ist ein Skill?

Ein Skill beschreibt eine begrenzte Arbeitsdisziplin für einen KI-Agenten.

Er beschreibt **wie** gearbeitet wird. Er definiert nicht eigenmächtig, **was** ein Projekt fachlich oder visuell tun soll.

Die ausführlicheren Regeldateien erklären Hintergründe und Leitplanken. `SKILL.md`-Dateien verdichten diese Regeln für einen konkreten Agenteneinsatz.

## Vorrangregeln

Bei der Anwendung gilt grundsätzlich:

```text
konkreter Nutzerauftrag
→ verbindliche Projektanforderung / Spezifikation / Kanon
→ gültige Projektentscheidungen und Projektdokumentation
→ freigegebener Plan oder Produktionsbrief
→ lokale Repository-Regeln und freigegebene Referenzen
→ allgemeine Agenten-, Fach- und Arbeitsregeln aus diesem Repository
```

Allgemeine Regeln dürfen keine lokale fachliche oder visuelle Wahrheit überschreiben.

## Agentenautonomie

Agenten dürfen innerhalb eines ausdrücklich oder durch den Projektprozess freigegebenen Scopes selbstständig iterieren.

Dabei gelten insbesondere:

- Kontext gezielt statt maximal laden;
- Delegation beschreibt Ziel, Scope, Rechte, Akzeptanzbedingungen und erwartete Evidence;
- unabhängige Arbeit darf parallelisiert werden, echte Abhängigkeiten nicht;
- parallele Agenten benötigen ausreichend isolierte veränderliche Workspaces;
- jeder wichtige Arbeitsschritt braucht einen überprüfbaren Ausgangszustand;
- ein Loop benötigt Stop- und Eskalationsbedingungen;
- fehlende Spezifikation darf nicht durch stillschweigende Agentenentscheidungen ersetzt werden;
- automatisch prüfbare Invarianten sollten möglichst automatisch geprüft werden;
- riskante, irreversible oder extern sichtbare Aktionen benötigen die dafür definierte Freigabe;
- ein erfolgreicher Agentenlauf ist noch keine fachliche oder technische Freigabe;
- relevante Agentenarbeit soll mit Auftrag, Evidence und Ergebnis nachvollziehbar verbunden werden;
- wiederkehrende Agentenfähigkeiten können mit Evals statt nur durch subjektiven Eindruck geprüft werden;
- Repository-Drift wird nicht automatisch großflächig refactort, sondern in bestätigten kleinen Repair-Slices behandelt.

## Verteilung in Projekte

KI-Agenten arbeiten normalerweise innerhalb eines konkreten Projektrepositories und lesen dieses zentrale Repository nicht automatisch.

Darum können benötigte Skills bewusst repo-lokal übernommen oder durch eine projektspezifische Agent-Datei referenziert werden.

Dabei gilt:

- zentrale Fassung = allgemeine kanonische Arbeitsweise;
- lokale Fassung = für den Agenten verfügbare Kopie oder projektspezifischer Adapter;
- projektspezifische Ergänzungen bleiben lokal;
- Änderungen an zentralen Skills werden bewusst in betroffene Projekte übernommen.

Dasselbe gilt für Bildarbeit: zentrale Bildregeln beschreiben die Arbeitsweise, während Charakterbibeln, konkrete Referenzbilder, Szenenlisten und visuelle Projektregeln lokal bleiben.

## Attribution

Übernommene oder adaptierte Drittinhalte werden in `THIRD-PARTY-NOTICES.md` dokumentiert. Externe Inspirationsquellen ohne übernommene Drittinhalte werden in den jeweiligen `Quellen-und-Inspirationen.md`-Dateien eingeordnet.

## Pflege

Neue Regeln sollen nur aufgenommen werden, wenn sie:

1. wiederverwendbar sind;
2. einen erkennbaren Qualitäts- oder Sicherheitsgewinn bringen;
3. nicht bloß eine persönliche Vorliebe als allgemeine Wahrheit darstellen;
4. keine unnötigen personenbezogenen Daten enthalten;
5. möglichst konkret beschreiben, wann und wie sie anzuwenden sind.

Eine Regel, die nur für ein einzelnes Projekt gilt, bleibt dort.