# Quellenregister und Upstream-Monitoring

## Zweck

Die fachbezogenen `Quellen-und-Inspirationen.md`-Dateien dokumentieren, **woher Konzepte stammen**.

Dieses Register ergänzt eine zweite Frage:

> Welche externen Quellen können sich verändern und sollten deshalb aktiv auf Updates überwacht werden?

Die maschinenlesbare Liste steht in `upstream-sources.yml`.

Der letzte vollständige Bereichsaudit ist dokumentiert in `Upstream-Audit-2026-08-23.md`.

## Drei Quellenklassen

### 1. Aktive mutable Dependency

Eine externe Quelle hat konkrete lokale Regeln oder Skills wesentlich beeinflusst und kann sich weiter verändern.

Beispiele:

- `SKILL.md` auf einem `main`-Branch;
- laufend gepflegte Agent-Skill-Sammlungen;
- aktuelle Produktdokumentation;
- lebende Style Guides oder Best-Practice-Sammlungen.

Diese Quellen gehören in `upstream-sources.yml`.

### 2. Stabile Referenzquelle

Beispiele:

- veröffentlichte Paper;
- datierte Research-Artikel;
- historische Changelog-Einträge;
- grundlegende Frameworks mit langsamem Wandel.

Sie bleiben in den jeweiligen Fachquellen dokumentiert und werden im normalen Repo-Audit erneut eingeordnet.

Sie benötigen nicht künstlich einen SHA- oder Webseiten-Watch.

### 3. Radar- oder Discoveryquelle

Beispiele:

- Skill-Kataloge;
- Community-Verzeichnisse;
- Übersichtsseiten;
- Sammlungen, aus denen aktuell keine konkrete lokale Regel abgeleitet ist.

Sie helfen beim Finden neuer Kandidaten, sind aber keine lokale Dependency.

## Monitoring-Arten

Schema v2 unterscheidet zwei aktive Monitoring-Arten.

### `exact-sha`

Für konkrete GitHub-Dateien.

Gespeichert werden insbesondere:

- Repository;
- Dateipfad;
- Branch / Ref;
- beobachteter Blob-SHA;
- optional eine vom Skill selbst ausgewiesene Version;
- lokale Auswirkungen.

Beispiel:

```yaml
- id: beispiel-skill
  area: Recherche
  kind: github-file
  repository: owner/repo
  path: skills/example/SKILL.md
  ref: main
  monitor_mode: exact-sha
  cadence: monthly
  observed_sha: abc123...
  last_checked: 2026-08-23
  local_impact:
    - Recherche/Skills/example/SKILL.md
```

### `semantic-review`

Für lebende Web- oder Produktdokumentation ohne sinnvollen Git-Blob-SHA.

Hier wird nicht versucht, jedes Textzeichen technisch zu synchronisieren. Stattdessen wird die aktuelle Quelle erneut gegen die lokal übernommenen Konzepte gelesen.

Beispiel:

```yaml
- id: beispiel-produktdoku
  area: Bildarbeit
  kind: web-page
  url: https://example.com/current-docs
  monitor_mode: semantic-review
  cadence: monthly
  last_checked: 2026-08-23
  local_impact:
    - Bildarbeit/Stil-und-Referenzsysteme.md
```

## Cadence

### `monthly`

Für Quellen mit höherer Änderungswahrscheinlichkeit:

- Skills auf aktiven `main`-Branches;
- KI-Produktdokumentation;
- APIs und Toolfunktionen;
- schnell bewegte Agenten- und Researchsysteme.

### `quarterly`

Für langsamere lebende Leitfäden:

- Style Guides;
- Human-AI-Guidelines;
- allgemeine Dokumentationsframeworks und Community-Kataloge, wenn sie lokal relevant sind.

Der monatliche Pflegejob kann quartalsweise Einträge überspringen, solange sie noch nicht fällig sind.

## Monatlicher Upstream-Check

Für `exact-sha`:

```text
gespeicherter SHA
        ↓
aktuellen Blob-SHA lesen
        ↓
unverändert?
   ├─ ja → last_checked aktualisieren
   └─ nein
        ↓
      Diff prüfen
        ↓
      betrifft übernommene Konzepte?
        ├─ nein → Registry aktualisieren
        └─ ja  → Änderungskandidat
                    ↓
                  Review + Changelog
```

Für `semantic-review`:

```text
lokale übernommene Konzepte
        ↓
aktuelle Produkt-/Webdoku lesen
        ↓
relevante Funktion / Terminologie / Empfehlung geändert?
   ├─ nein → last_checked aktualisieren
   └─ ja
        ↓
      lokale Auswirkungen bestimmen
        ↓
      übernehmen / beobachten / verwerfen
```

## Keine automatische Synchronisierung

Ein Upstream-Update führt **niemals automatisch** zu einer Änderung unserer Skills.

Gründe:

- Upstream kann tool- oder projektspezifischer geworden sein;
- eine neue Regel kann unseren Grundsätzen widersprechen;
- der lokale Skill kann bewusst anders abstrahiert sein;
- ein Update kann Regressionen oder unnötige Komplexität einführen;
- eine Produktfunktion kann umbenannt worden sein, ohne dass sich das allgemeine Prinzip ändert.

Deshalb gilt:

> Upstream-Änderung = Review-Signal, nicht Sync-Befehl.

## Änderungen bewerten

Bei einem geänderten Upstream prüfen:

1. Was hat sich tatsächlich geändert?
2. Betrifft es ein Konzept, das wir übernommen haben?
3. Ist der neue Ansatz allgemeiner, belastbarer oder sicherer?
4. Widerspricht er unseren bestehenden Regeln?
5. Ist eine lokale Änderung nötig oder nur die Quellenbasis zu aktualisieren?
6. Müssen Skill-Handbuch, Changelog, Evals oder Vorlagen angepasst werden?
7. Hat sich nur Toolterminologie geändert, während das allgemeine Prinzip stabil bleibt?

## Neue Quellen aufnehmen

Bei jeder neuen externen Quelle zuerst klassifizieren:

```text
konkrete mutable Abhängigkeit?
→ upstream-sources.yml

stabile Evidenz / Grundlagenquelle?
→ Fachbereich/Quellen-und-Inspirationen.md

nur Discovery / Radar?
→ als Radarquelle dokumentieren, kein künstlicher Sync-Trigger
```

Ein aktiver Upstream-Eintrag lohnt sich insbesondere, wenn:

- eine konkrete externe `SKILL.md` lokale Arbeitsweise deutlich beeinflusst hat;
- eine Produktdokumentation Funktionen beschreibt, auf deren Modell lokale Regeln beruhen;
- die Quelle regelmäßig gepflegt wird;
- Änderungen wahrscheinlich relevant sein können;
- ein gezielter Review günstiger ist als regelmäßige komplette Neurecherche.

## Entfernte oder aufgegebene Quellen

Wenn eine Quelle verschwindet oder nicht mehr gepflegt wird:

- nicht automatisch unsere abgeleiteten Regeln löschen;
- lokale Regeln weiterhin nach eigenem Nutzen und Evidenz bewerten;
- Quelle im Register als `inactive` oder `archived` markieren;
- bei kritischer Abhängigkeit nach einer aktuelleren Primärquelle suchen.

## Verhältnis zu den Fachquellen

```text
Fachbereich/Quellen-und-Inspirationen.md
→ Was hat uns fachlich beeinflusst?

Dokumentation/upstream-sources.yml
→ Welche veränderlichen Quellen beobachten wir aktiv?

Dokumentation/Upstream-Audit-*.md
→ Warum wurde eine Quelle so klassifiziert?

CHANGELOG.md
→ Welche lokalen Regeln haben wir tatsächlich geändert?
```

## Leitgedanke

> Quellen sollen nicht nur zitierbar, sondern bei veränderlichen Upstreams auch wartbar sein.