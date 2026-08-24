# Pflege und Aktualisierung

## Zweck

Dieses Dokument beschreibt, wie das Repository aktuell, konsistent und nützlich gehalten wird.

Neue Ideen werden nicht automatisch übernommen. Das Repository wird bewusst gepflegt.

## Grundsatz

> Neue Quellen erzeugen Kandidaten, keine automatische Wahrheit.

## Pflege-Rhythmus

### 1. Monatlicher Radar- und Upstream-Check

Ziel:

- neue Entwicklungen früh sehen;
- interessante Kandidaten sammeln;
- Quellen sichten;
- mögliche Lücken erkennen;
- fällige mutable Upstreams prüfen.

Typische Themenfelder:

- Human-AI-Interaction;
- Agentic Engineering;
- generative Bildarbeit;
- KI-gestütztes Schreiben;
- technische Dokumentation;
- Webentwicklung und Webdesign;
- Recherche und Deep Research;
- KI-gestützte Softwareentwicklung;
- Reliability, SRE und System-Observability;
- SLI/SLO, Alerting und Incident Management;
- Capacity, Resilience, Recovery und Chaos Engineering;
- Data Engineering, ETL/ELT und Datenpipelines;
- Batch-/Streaming-Semantik, CDC, Orchestrierung und Reprocessing;
- Data Quality, Data Contracts, Lineage und analytische Datenmodellierung;
- Software Architecture und System Design;
- Architecture Drivers, Quality Attributes und Trade-off-Analyse;
- Systemgrenzen, Dekomposition, Architektur-Evolution und Conformance;
- Reflexion, Lernen und Selbstverbesserung mit KI;
- neue Sicherheits-, Governance- oder Evaluationsansätze.

Zusätzlich wird `upstream-sources.yml` gelesen.

Für Einträge mit `cadence: monthly`:

- `monitor_mode: exact-sha` → aktuellen GitHub-Blob-SHA vergleichen;
- `monitor_mode: semantic-review` → aktuelle Produkt-/Webdoku gegen die lokal übernommenen Konzepte lesen.

Ergebnis:

- kurze Kandidatenliste;
- Quelle und Einordnung;
- vermuteter Nutzen;
- relevante Upstream-Diffs oder semantische Änderungen;
- noch keine automatische Regeländerung.

### 2. Vierteljährlicher Repo-Audit

Ziel:

- Regeln gezielt überprüfen;
- Redundanzen und Widersprüche finden;
- veraltete Regeln erkennen;
- neue Kandidaten bewerten;
- reale Nutzungserfahrungen berücksichtigen;
- `cadence: quarterly`-Upstreams prüfen;
- Quellenklassifikation erneut auf Vollständigkeit prüfen.

Prüffragen:

1. Ist die Regel noch aktuell?
2. Ist sie allgemein wiederverwendbar?
3. Ist sie redundant?
4. Widerspricht sie anderen Regeln?
5. Hat sie echte Evidenz oder belastbare Praxiserfahrung?
6. Führt sie in realen Aufgaben zu besserer Arbeit?
7. Fehlt eine wichtige Leitplanke?
8. Ist sie verständlich genug formuliert?
9. Ist ein vorhandener Skill zu breit, zu eng oder missverständlich?
10. Muss Dokumentation oder Beispiel aktualisiert werden?
11. Gibt es mutable Quellen, die noch nicht im Upstream-Register stehen?
12. Wird eine registrierte Quelle inzwischen nur noch als Radarquelle benötigt?
13. Ist ein beobachteter Upstream eingestellt, ersetzt oder archiviert worden?

### 3. Anlassbezogene Prüfung

Zusätzliche Prüfung bei:

- wichtigen neuen Modellfähigkeiten;
- größeren Änderungen offizieller Plattformen;
- wiederkehrenden Problemen in der Praxis;
- neuen Projektarten;
- auffälligen Schwächen eines bestehenden Skills;
- Änderungen an Drittquellen oder Lizenzbedingungen;
- neuen Erkenntnissen, die eine bestehende Regel wesentlich infrage stellen;
- einem relevanten Upstream-Diff außerhalb des normalen Rhythmus.

## Quellenklassifikation

Neue externe Quellen werden beim Aufnehmen einer Klasse zugeordnet.

### Aktive mutable Dependency

Eine konkrete veränderliche Quelle beeinflusst lokale Regeln oder Skills direkt.

→ in `upstream-sources.yml` aufnehmen.

### Stabile Referenzquelle

Paper, datierte Research-Artikel oder langsam veränderliche Grundlagen ohne sinnvollen Sync-Trigger.

→ im Fachbereich unter `Quellen-und-Inspirationen.md` dokumentieren.

### Radar-/Discoveryquelle

Hilft neue Kandidaten zu finden, erzeugt aber keine direkte lokale Abhängigkeit.

→ als Radarquelle dokumentieren; kein künstlicher Upstream-Watch.

Details: `Quellenregister.md`.

## Gezielter Upstream-Check

Schema v2 unterstützt zwei Monitoring-Arten.

### Exact SHA

Für konkrete GitHub-Dateien:

```text
registrierter Blob-SHA
→ aktuellen Blob-SHA abrufen
→ unverändert?
   ├─ ja → last_checked aktualisieren
   └─ nein
        ↓
      Diff prüfen
        ↓
      betrifft übernommene Konzepte?
        ├─ nein → Register aktualisieren
        └─ ja  → Änderungskandidat erzeugen
                    ↓
                  normaler Reviewprozess
```

### Semantic Review

Für lebende Webseiten und Produktdokumentation:

```text
lokal übernommene Konzepte
→ aktuelle Quelle erneut lesen
→ relevante Funktion / Empfehlung / Terminologie geändert?
   ├─ nein → last_checked aktualisieren
   └─ ja
        ↓
      lokale Auswirkungen bestimmen
        ↓
      übernehmen / beobachten / verwerfen
```

Dabei gilt:

> Upstream-Änderung = Review-Signal, nicht automatischer Sync.

Details und Schema stehen in `Quellenregister.md` und `upstream-sources.yml`.

## Aufnahme neuer Regeln

Eine neue Regel wird nur übernommen, wenn sie:

1. wiederverwendbar ist;
2. nicht nur persönliche Vorliebe abbildet;
3. gegenüber bestehenden Regeln einen erkennbaren Mehrwert bringt;
4. in den bestehenden Systemgedanken passt;
5. echten Qualitäts-, Sicherheits- oder Verständlichkeitsgewinn bringt;
6. keine gefährliche oder unnötig starre Fehlanwendung fördert;
7. möglichst konkret formuliert werden kann.

## Entscheidungslogik

```text
Quelle / neue Idee
        ↓
Kandidat erfassen
        ↓
Quelle klassifizieren
        ↓
allgemein genug?
        ↓
nützlich genug?
        ↓
Evidenz / Praxistauglichkeit?
        ↓
bestehende Regeln vergleichen
        ↓
Nebenwirkungen prüfen
        ↓
übernehmen / anpassen / verwerfen
        ↓
Changelog + Quellenregister aktualisieren
```

## Quellenarten

Bevorzugt:

- offizielle Dokumentationen;
- Primärquellen;
- wissenschaftliche Originalarbeiten und Meta-Analysen;
- Research von belastbaren Institutionen;
- reale Praxiserfahrungen mit klarer Einordnung;
- gepflegte Open-Source-Projekte mit nachvollziehbarer Methodik.

Mit Vorsicht:

- Social-Media-Hypes;
- reine Buzzwords;
- ungeprüfte „Best Practices“;
- stark toolgebundene Einzellösungen;
- Aussagen ohne nachvollziehbare Quelle;
- scheinbar allgemeine Regeln, die nur in einem einzelnen Setup funktioniert haben.

## Externe Quelle ist nicht gleich zentrale Regel

Bei jeder Quelle unterscheiden:

- **Beobachtung:** Was beschreibt die Quelle tatsächlich?
- **Interpretation:** Was lässt sich daraus plausibel ableiten?
- **Übernahme:** Welcher Teil ist für dieses Repository wirklich allgemein nützlich?

Nicht eine externe Terminologie komplett übernehmen, wenn ein kleiner allgemeiner Grundsatz genügt.

## Verwerfungen dokumentieren

Auch nicht übernommene Kandidaten können dokumentiert werden, wenn sie voraussichtlich wieder auftauchen oder die Entscheidung besonders lehrreich ist.

Empfohlene Form:

```text
Kandidat:
"Jede Interaktion soll grundsätzlich sokratisch geführt werden."

Entscheidung:
Nicht übernommen.

Grund:
Nicht jede Situation profitiert von Rückfragen. In vielen Fällen ist eine klare direkte Antwort hilfreicher.
```

So werden bereits geprüfte Ideen nicht regelmäßig neu entdeckt und erneut diskutiert.

## Versionierung

Empfohlen wird eine datumsbasierte Versionierung:

- `v2026.08`
- `v2026.11`
- `v2027.02`

Eine neue Version ist sinnvoll, wenn sich der nutzbare Regelsatz merklich verändert.

Kleine Tippfehler oder rein redaktionelle Korrekturen benötigen nicht zwingend eine neue veröffentlichte Version.

## Changelog

Relevante Änderungen werden in `../CHANGELOG.md` festgehalten.

Dabei unterscheiden:

- hinzugefügt;
- geändert;
- entfernt;
- veraltet / ersetzt;
- wichtige Begründungen oder Migrationshinweise.

## Auswirkungen auf Projekte

Eine zentrale Änderung aktualisiert lokale Projekte nicht automatisch.

Empfohlener Ablauf:

```text
neue Version
→ Changelog prüfen
→ betroffene lokale Skills identifizieren
→ Diff bewerten
→ lokale Anpassungen bewusst übernehmen
→ Projektmanifest aktualisieren
```

## Skills mit Evals prüfen

Für häufig genutzte Agenten-Skills kann es sinnvoll sein, wiederholbare Beispielaufgaben oder Golden Tasks zu pflegen.

Damit lässt sich prüfen, ob eine Änderung:

- Scope-Treue verbessert oder verschlechtert;
- bessere Evidence erzeugt;
- Stop-Gates korrekt erkennt;
- weniger unnötige Änderungen verursacht;
- robuste Ergebnisse liefert.

Nicht jeder textliche Skill braucht sofort einen automatischen Eval-Harness. Aufwand und Nutzen müssen zusammenpassen.

## Praktische Pflegefragen

Bei jedem Audit prüfen:

- Welche Regeln werden real genutzt?
- Welche Skills verwirren?
- Welche Skills fehlen?
- Welche Regeln werden im Alltag regelmäßig ignoriert?
- Wo ist eine Regel zu abstrakt?
- Wo fehlt ein Beispiel?
- Wo widersprechen Handbuch und `SKILL.md` einander?
- Welche Quellen sind inzwischen veraltet?
- Welche registrierten Upstreams haben sich geändert?
- Welche mutable Quelle fehlt noch im Register?
- Welche Projektprobleme deuten auf eine allgemeine Lücke hin?

## Verantwortungsregel

Ein Research-Hinweis oder Upstream-Diff ist kein automatisches Commit.

Eine gute Quelle ersetzt nicht die bewusste Entscheidung.

> Aktualität bedeutet nicht, jedem Trend hinterherzulaufen. Aktualität bedeutet, relevante Veränderungen regelmäßig zu prüfen.