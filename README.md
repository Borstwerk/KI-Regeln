# KI-Regeln

Dieses Repository sammelt allgemeine, wiederverwendbare Regeln, Arbeitsweisen und Skills für die Zusammenarbeit mit generativer KI.

Ziel ist keine persönliche KI-Konfiguration und keine projektspezifische Wissenssammlung. Enthalten werden nur Regeln, die sich sinnvoll auf andere Nutzer, Projekte oder Aufgaben übertragen lassen.

## Grundprinzip

> Allgemeine Arbeitsweise zentral, konkrete Wahrheit lokal.

Das bedeutet:

- allgemeine Kommunikations-, Reflexions-, Schreib-, Bild-, Analyse-, Agenten- und Entwicklungsregeln liegen hier;
- projektspezifische Anforderungen, Architektur, Figuren, Fachbegriffe, visuelle Bibeln und Sonderregeln bleiben im jeweiligen Projekt;
- persönliche Profile, Gesundheitsdaten, Familieninformationen oder andere nicht notwendige personenbezogene Details gehören nicht in dieses Repository;
- ein Skill ersetzt niemals die tatsächliche Spezifikation oder Dokumentation eines Projekts.

## Struktur

```text
KI-Regeln/
├── Grundlagen/
│   ├── Zusammenarbeit-mit-KI.md
│   ├── Mensch-KI-Interaktion.md
│   ├── Vertrauen-und-Denkautonomie.md
│   ├── Datenschutz-und-Kontext.md
│   └── Quellen-und-Inspirationen.md
├── Arbeitsweisen/
│   ├── Problemloesung.md
│   ├── Reflexion-und-Selbstverbesserung.md
│   ├── Zielarbeit-und-Umsetzung.md
│   └── Skills/
│       ├── reflektierender-dialog/SKILL.md
│       ├── entscheidungsunterstuetzung/SKILL.md
│       └── ziel-reflexions-loop/SKILL.md
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

Regeln für verlässliche Zusammenarbeit mit KI unabhängig vom Fachgebiet: Quellen, Unsicherheit, Kommunikation, Kontext, Datenschutz, kalibriertes Vertrauen und Denkautonomie.

Der Bereich behandelt insbesondere:

- `Zusammenarbeit mit KI` – Auftrag, Quellen, Unsicherheit, direkte Kommunikation, Rollen und menschliche Entscheidungshoheit;
- `Mensch-KI-Interaktion` – KI als Werkzeug, Sparringspartner und Denkunterstützung statt als Orakel;
- `Vertrauen und Denkautonomie` – richtige Ausgaben annehmen, falsche zurückweisen und eigene Urteilsfähigkeit erhalten;
- `Datenschutz und Kontext` – persönliche und projektspezifische Informationen nur so weit verwenden und zentralisieren, wie es tatsächlich nötig ist.

Leitgedanke:

> KI soll Denken unterstützen, nicht unbemerkt an dessen Stelle treten.

`Grundlagen/Quellen-und-Inspirationen.md` dokumentiert unter anderem Human-AI-Interaction-Forschung, Appropriate Reliance, Self-Determination Theory und Motivational Interviewing als Inspirations- und Evidenzquellen.

### 2. Arbeitsweisen

Wiederverwendbare Denk-, Problemlösungs- und Lernmuster.

Enthalten sind:

- `Problemloesung` – Beobachtung, falsifizierbare Hypothesen, kleine Versuche und belastbare Nachweise;
- `Reflexion-und-Selbstverbesserung` – Erfahrungen auswerten, Interpretationen als Hypothesen behandeln und kleine Lernschritte ableiten;
- `Zielarbeit-und-Umsetzung` – Ziele, reale Hindernisse, kleine Handlungen und Wenn-Dann-Pläne verbinden.

Enthaltene Skills:

- `reflektierender-dialog` – persönliche oder strategische Erfahrungen ordnen, ohne vorschnell zu diagnostizieren oder Lösungen aufzudrängen;
- `entscheidungsunterstuetzung` – Kriterien, Alternativen, Unsicherheiten und Gegenargumente strukturieren, während persönliche Wertentscheidungen beim Menschen bleiben;
- `ziel-reflexions-loop` – Ziel, Hindernis, kleinen Versuch, reale Erfahrung und Anpassung zu einem Lernloop verbinden.

Leitgedanke:

> Verstehen → ausprobieren → Erfahrung sammeln → reflektieren → anpassen.

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

Er beschreibt **wie** gearbeitet wird. Er definiert nicht eigenmächtig, **was** ein Projekt fachlich, visuell oder persönlich tun soll.

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

Allgemeine Regeln dürfen keine lokale fachliche, visuelle oder persönliche Wahrheit überschreiben.

## Menschliche Denk- und Entscheidungshoheit

Bei Reflexion, Lernen und Entscheidungen gelten zusätzlich:

- KI-Unterstützung soll vorhandenes Denken möglichst erweitern statt unnötig ersetzen;
- Vertrauen wird an Aufgabe, Quellen, Nachweise und Fehlerrisiko angepasst;
- persönliche Wertgewichtungen bleiben beim Menschen;
- psychologische Interpretationen werden nicht ohne Grundlage als Diagnose oder verborgene Wahrheit dargestellt;
- reale Beobachtungen und externe Evidenz haben Vorrang vor bloßer Gesprächskohärenz;
- wiederkehrende Unterstützung soll möglichst Kompetenz aufbauen;
- Selbstverbesserung wird als Lernloop behandelt, nicht als Urteil über die Person.

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

Persönliche Reflexionsnotizen oder individuelle Entwicklungsverläufe gehören ebenfalls nicht als allgemeine Wahrheit in dieses Repository. Zentral liegen nur die wiederverwendbaren Methoden.

## Attribution

Übernommene oder adaptierte Drittinhalte werden in `THIRD-PARTY-NOTICES.md` dokumentiert. Externe Inspirationsquellen ohne übernommene Drittinhalte werden in den jeweiligen `Quellen-und-Inspirationen.md`-Dateien eingeordnet.

## Pflege

Neue Regeln sollen nur aufgenommen werden, wenn sie:

1. wiederverwendbar sind;
2. einen erkennbaren Qualitäts- oder Sicherheitsgewinn bringen;
3. nicht bloß eine persönliche Vorliebe als allgemeine Wahrheit darstellen;
4. keine unnötigen personenbezogenen Daten enthalten;
5. möglichst konkret beschreiben, wann und wie sie anzuwenden sind.

Eine Regel, die nur für ein einzelnes Projekt oder eine einzelne Person gilt, bleibt dort.