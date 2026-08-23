# KI-Regeln

Dieses Repository sammelt allgemeine, wiederverwendbare Regeln, Arbeitsweisen und Skills für die Zusammenarbeit mit generativer KI.

Ziel ist keine persönliche KI-Konfiguration und keine projektspezifische Wissenssammlung. Enthalten werden nur Regeln, die sich sinnvoll auf andere Nutzer, Projekte oder Aufgaben übertragen lassen.

## Grundprinzip

> Allgemeine Arbeitsweise zentral, konkrete Wahrheit lokal.

Das bedeutet:

- allgemeine Kommunikations-, Schreib-, Analyse- und Entwicklungsregeln liegen hier;
- projektspezifische Anforderungen, Architektur, Figuren, Fachbegriffe und Sonderregeln bleiben im jeweiligen Projekt;
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
├── Schreiben/
│   ├── Agent-Anweisungen.md
│   ├── Schreibstil.md
│   ├── Kreatives-Schreiben.md
│   ├── Stilreview.md
│   └── Skills/
│       ├── natuerliches-schreiben/SKILL.md
│       ├── kreatives-schreiben/SKILL.md
│       └── stilreview/SKILL.md
├── Programmieren/
│   ├── Entwicklungsprozess.md
│   ├── Agent-Anweisungen.md
│   └── Skills/
│       ├── code-review/SKILL.md
│       ├── diagnose/SKILL.md
│       ├── domain-modeling/SKILL.md
│       └── tdd/SKILL.md
└── Vorlagen/
    └── AGENTS.template.md
```

## Ebenen

### 1. Grundlagen

Regeln für verlässliche Zusammenarbeit mit KI unabhängig vom Fachgebiet: Quellen, Unsicherheit, Kommunikation, Kontext und Datenschutz.

### 2. Arbeitsweisen

Wiederverwendbare Denk- und Problemlösungsmuster wie Hypothesenbildung, iterative Bearbeitung und überprüfbare Entscheidungen.

### 3. Schreiben

Allgemeine Regeln für natürliche Texte, kreative Prosa und strukturelle Stilreviews.

Enthaltene Skills:

- `natuerliches-schreiben` – klare, glaubwürdige Texte ohne unnötige KI-, Werbe- oder Managementsprache;
- `kreatives-schreiben` – Szene, Figurenstimme, räumliche Klarheit und kanontreue Wirkung;
- `stilreview` – Muster erkennen, aber nur nach Kontextprüfung ändern.

### 4. Programmieren

Allgemeiner Fünf-Gate-Prozess und wiederverwendbare Agent-Skills für Softwarearbeit.

Enthaltene Skills:

- `domain-modeling` – Begriffe, Fachobjekte und Grenzen schärfen;
- `tdd` – kleine Red/Green-Umsetzungsschnitte;
- `diagnose` – reproduzierbare Root-Cause-Diagnose;
- `code-review` – tatsächlichen Diff gegen Anforderung und Repository-Standards prüfen.

### 5. Projektregeln

Projektregeln gehören nicht hierher. Beispiele sind konkrete Produktanforderungen, Serienkanon, Fachmodelle, Releasewege oder technische Sonderfälle eines einzelnen Repositories.

## Was ist ein Skill?

Ein Skill beschreibt eine begrenzte Arbeitsdisziplin für einen KI-Agenten.

Er beschreibt **wie** gearbeitet wird. Er definiert nicht eigenmächtig, **was** ein Projekt fachlich tun soll.

Die ausführlicheren Regeldateien erklären Hintergründe und Leitplanken. `SKILL.md`-Dateien verdichten diese Regeln für einen konkreten Agenteneinsatz.

## Vorrangregeln

Bei der Anwendung gilt grundsätzlich:

```text
konkreter Nutzerauftrag
→ verbindliche Projektanforderung / Spezifikation
→ gültige Projektentscheidungen und Projektdokumentation
→ freigegebener Plan
→ allgemeine Regeln und Skills aus diesem Repository
```

Allgemeine Regeln dürfen keine lokale fachliche Wahrheit überschreiben.

## Verteilung in Projekte

KI-Agenten arbeiten normalerweise innerhalb eines konkreten Projektrepositories und lesen dieses zentrale Repository nicht automatisch.

Darum können benötigte Skills bewusst repo-lokal übernommen oder durch eine projektspezifische Agent-Datei referenziert werden.

Dabei gilt:

- zentrale Fassung = allgemeine kanonische Arbeitsweise;
- lokale Fassung = für den Agenten verfügbare Kopie oder projektspezifischer Adapter;
- projektspezifische Ergänzungen bleiben lokal;
- Änderungen an zentralen Skills werden bewusst in betroffene Projekte übernommen.

## Pflege

Neue Regeln sollen nur aufgenommen werden, wenn sie:

1. wiederverwendbar sind;
2. einen erkennbaren Qualitäts- oder Sicherheitsgewinn bringen;
3. nicht bloß eine persönliche Vorliebe als allgemeine Wahrheit darstellen;
4. keine unnötigen personenbezogenen Daten enthalten;
5. möglichst konkret beschreiben, wann und wie sie anzuwenden sind.

Eine Regel, die nur für ein einzelnes Projekt gilt, bleibt dort.