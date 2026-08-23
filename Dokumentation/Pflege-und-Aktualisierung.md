# Pflege und Aktualisierung

## Zweck

Dieses Dokument beschreibt, wie das Repository aktuell, konsistent und nützlich gehalten wird.

Neue Ideen werden nicht automatisch übernommen. Das Repository wird bewusst gepflegt.

## Grundsatz

> Neue Quellen erzeugen Kandidaten, keine automatische Wahrheit.

## Pflege-Rhythmus

### 1. Monatlicher Radar-Check

Ziel:

- neue Entwicklungen früh sehen;
- interessante Kandidaten sammeln;
- Quellen sichten;
- mögliche Lücken erkennen.

Typische Themenfelder:

- Human-AI-Interaction;
- Agentic Engineering;
- generative Bildarbeit;
- KI-gestütztes Schreiben;
- KI-gestützte Softwareentwicklung;
- Reflexion, Lernen und Selbstverbesserung mit KI;
- neue Sicherheits-, Governance- oder Evaluationsansätze.

Ergebnis:

- kurze Kandidatenliste;
- Quelle und Einordnung;
- vermuteter Nutzen;
- noch keine automatische Regeländerung.

### 2. Vierteljährlicher Repo-Audit

Ziel:

- Regeln gezielt überprüfen;
- Redundanzen und Widersprüche finden;
- veraltete Regeln erkennen;
- neue Kandidaten bewerten;
- reale Nutzungserfahrungen berücksichtigen.

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

### 3. Anlassbezogene Prüfung

Zusätzliche Prüfung bei:

- wichtigen neuen Modellfähigkeiten;
- größeren Änderungen offizieller Plattformen;
- wiederkehrenden Problemen in der Praxis;
- neuen Projektarten;
- auffälligen Schwächen eines bestehenden Skills;
- Änderungen an Drittquellen oder Lizenzbedingungen;
- neuen Erkenntnissen, die eine bestehende Regel wesentlich infrage stellen.

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
Changelog aktualisieren
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
- Welche Projektprobleme deuten auf eine allgemeine Lücke hin?

## Verantwortungsregel

Ein Research-Hinweis ist kein automatisches Commit.

Eine gute Quelle ersetzt nicht die bewusste Entscheidung.

> Aktualität bedeutet nicht, jedem Trend hinterherzulaufen. Aktualität bedeutet, relevante Veränderungen regelmäßig zu prüfen.