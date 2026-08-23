# Dokumentationserstellung

Dieser Bereich sammelt allgemeine Regeln und Skills für technische und projektbezogene Dokumentation.

Ziel ist nicht möglichst viel Dokumentation, sondern **die richtige Dokumentation für die richtige Zielgruppe, mit klarer Quelle der Wahrheit und überprüfbarer Aktualität**.

## Grundprinzipien

> Dokumentation beginnt mit Leser, Zweck und Quelle der Wahrheit – nicht mit einer leeren Markdown-Datei.

> Dokumenttyp und Dokumentationsmodus sind unterschiedliche Entscheidungen.

> Eine gut geschriebene falsche Anleitung ist schlechter als eine knappe korrekte.

## Zwei Achsen

### 1. Dokumentationsmodus

Nach dem Diátaxis-Modell werden vier grundlegende Leserbedürfnisse unterschieden:

- **Tutorial** – Lernen durch angeleitetes Tun;
- **How-to** – eine konkrete Aufgabe erledigen;
- **Reference** – Fakten schnell nachschlagen;
- **Explanation** – Zusammenhänge und Gründe verstehen.

### 2. Artefakttyp

Ein reales Dokument kann beispielsweise sein:

- README;
- ADR;
- Runbook;
- API-Dokumentation;
- Onboarding Guide;
- Changelog;
- Knowledge-Base-Artikel;
- Installationsanleitung.

Ein Artefakt kann mehrere klar getrennte Dokumentationsmodi enthalten. Ein README kann etwa Erklärung, Quickstart/How-to und Reference verknüpfen, ohne sie innerhalb eines Abschnitts zu vermischen.

## Empfohlener Ablauf

```text
Auftrag / Änderungsgrund
        ↓
Zielgruppe + Dokumentzweck
        ↓
Artefakttyp + Dokumentationsmodus
        ↓
Quellen der Wahrheit bestimmen
        ↓
Informationsarchitektur planen
        ↓
Dokument erstellen
        ↓
Beispiele / Links / Fakten verifizieren
        ↓
Docs Review
        ↓
Wartungs- und Driftregeln festlegen
```

## Inhalte

- `Zielgruppe-und-Dokumentzweck.md` – Leser, Aufgabe, Vorwissen und Erfolgskriterium;
- `Dokumenttypen-und-Diataxis.md` – Dokumentationsmodi und Artefakttypen sauber trennen;
- `Source-of-Truth-und-Fachkorrektheit.md` – Dokumentation an reale Quellen binden;
- `Technischer-Schreibstil.md` – Klarheit, Terminologie, Ton und Scanbarkeit;
- `Beispiele-Code-und-Verifikation.md` – Beispiele, Befehle, Links und Parameter prüfen;
- `Navigation-und-Informationsarchitektur.md` – Inhalte auffindbar und logisch strukturieren;
- `Docs-as-Code-und-Wartbarkeit.md` – Git, Review, Tests, Ownership und Aktualisierung;
- `Dokumentationsreview-und-Drift.md` – unabhängiger Audit auf Fehler, Veraltung und Lücken;
- `Quellen-und-Inspirationen.md` – externe Grundlagen und mutable Upstream-Skills;
- `Vorlagen/` – kleine Ausgangspunkte für häufige Artefakttypen;
- `Skills/` – operative Agenten-Skills.

## Skills

- `docs-plan` – Zielgruppe, Dokumentzweck, Modus, Artefakt und Quellen planen;
- `technical-writing` – technische Dokumentation klar und quellennah schreiben;
- `readme` – README als Projekt-Einstiegspunkt erstellen oder überarbeiten;
- `tutorial` – lernorientierte Schrittfolge mit überprüfbaren Ergebnissen;
- `how-to` – konkrete Aufgabe ohne unnötige Konzeptabschweifung lösen;
- `reference-docs` – scanbare, konsistente Nachschlagedokumentation;
- `explanation-docs` – Hintergründe, Zusammenhänge und Trade-offs erklären;
- `adr` – Architekturentscheidungen mit Kontext und Alternativen dokumentieren;
- `runbook` – operative Abläufe unter realen Störungsbedingungen dokumentieren;
- `docs-review` – Korrektheit, Struktur, Beispiele, Links und Drift unabhängig prüfen.

## Abgrenzung

Dieser Bereich beschreibt **wie Dokumentation erstellt und gepflegt wird**.

Er ersetzt nicht:

- die fachliche Spezifikation;
- den realen Code oder die reale API;
- gültige Architekturentscheidungen;
- Betriebsfreigaben;
- projektspezifische Terminologie;
- rechtlich verbindliche Texte.

Konkrete Dokumentationsstruktur, Produktbegriffe, Zielgruppen und Sources of Truth bleiben im jeweiligen Projekt.
