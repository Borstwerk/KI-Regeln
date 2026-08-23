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
│   ├── Schreibstil.md
│   ├── Kreatives-Schreiben.md
│   └── Stilreview.md
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

### 3. Fachliche Einsatzgebiete

Regeln für wiederkehrende Aufgabenarten, derzeit insbesondere Schreiben und Programmieren.

### 4. Skills

Kleine, klar begrenzte Arbeitsdisziplinen für Agenten. Ein Skill beschreibt **wie** gearbeitet wird. Er definiert nicht eigenmächtig, **was** ein Projekt fachlich tun soll.

### 5. Projektregeln

Projektregeln gehören nicht hierher. Beispiele sind konkrete Produktanforderungen, Serienkanon, Fachmodelle, Releasewege oder technische Sonderfälle eines einzelnen Repositories.

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

## Pflege

Neue Regeln sollen nur aufgenommen werden, wenn sie:

1. wiederverwendbar sind;
2. einen erkennbaren Qualitäts- oder Sicherheitsgewinn bringen;
3. nicht bloß eine persönliche Vorliebe als allgemeine Wahrheit darstellen;
4. keine unnötigen personenbezogenen Daten enthalten;
5. möglichst konkret beschreiben, wann und wie sie anzuwenden sind.

Eine Regel, die nur für ein einzelnes Projekt gilt, bleibt dort.