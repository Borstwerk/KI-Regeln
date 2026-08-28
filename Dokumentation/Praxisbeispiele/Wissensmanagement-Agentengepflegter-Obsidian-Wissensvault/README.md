# Praxisbeispiel: Agentengepflegter Obsidian-Wissensvault

Dieses Beispiel dokumentiert einen realen Arbeitsmodus: Eine über viele Sitzungen gewachsene Obsidian-Wissensbasis wird mit wiederkehrenden Dokumenten und Protokollen aktualisiert, verdichtet, verknüpft und auf Drift geprüft.

Es ist **kein vollständiger Export eines realen Vaults**. Alle Bezeichnungen, Pfade, Zeitangaben und Korrekturfälle sind verallgemeinert. Personenbezogene Inhalte, Rohdaten, Messwerte, Vertragsdetails, Screenshots und Chatverläufe wurden nicht übernommen.

Das Beispiel ist kein Benchmark, keine Erfolgsgarantie und keine Aussage über die allgemeine Zuverlässigkeit der beteiligten Skills.

## 1. Konkreter Auftrag

Der Agent sollte nicht nur neue Dateien ablegen, sondern eine dauerhaft nutzbare Wissensbasis pflegen:

- wiederkehrende Tagesprotokolle und Dokumentstände aufnehmen;
- unveränderte Quellen von abgeleitetem Wissen trennen;
- bestehende Seiten aktualisieren, statt Dubletten anzulegen;
- Zusammenhänge nur bei ausreichender Evidenz formulieren;
- Korrekturen und ersetzte Quellen nachvollziehbar verarbeiten;
- Übersichten, interne Links und Metadaten aktuell halten;
- spätere Fragen ausschließlich auf Basis des Vault-Inhalts beantworten;
- einen neuen Task ohne vollständiges erneutes Einlesen fortsetzungsfähig machen.

Der zusätzliche Schwierigkeitsgrad lag in der Dauer: Der Vault wurde nicht in einem einzelnen Lauf erzeugt, sondern über viele kleine und einige größere Datenpakete hinweg weiterentwickelt.

## 2. Lokale Projektwahrheit

Die zentrale Regel lautete:

> Allgemeine Arbeitsweise bleibt zentral; konkrete Wahrheit bleibt lokal.

Eine lokale Projektdatei definierte deshalb Schema, Ablageorte, Benennung, Schreibgrenzen und Abschlussprüfungen. Sie hatte Vorrang vor allgemeinen Konventionen.

Die Wissensbasis unterschied vier Ebenen:

| Ebene | Zweck | Schreibregel |
|---|---|---|
| Raw Sources | unveränderte Originaldateien und Uploads | nach korrekter Ablage nicht inhaltlich verändern |
| Sources | lesbare, quellennahe Zusammenfassungen | Fakten mit klarer Herkunft und Dokumentstatus |
| Concepts und Entities | wiederverwendbare Begriffe, Personenrollen, Objekte und Beziehungen | Search before Create; Unsicherheit sichtbar halten |
| Synthesen und Hauptseiten | verdichtete Navigation, Zeitverläufe und bereichsübergreifende Erkenntnisse | nur aus belegten Wissenseinheiten ableiten |

Zusätzlich gab es kleine operative Dateien für Navigation, Arbeitsstand und Änderungsprotokoll. Sie waren kein Ersatz für die eigentlichen Quellen.

## 3. Verwendeter Wissensmanagement-Workflow

Der zentrale Workflow wurde lokal auf Obsidian Markdown abgebildet:

```text
neue Quelle oder Nutzerangabe
→ knowledge-ingest
→ vorhandene Identität und passende Seiten suchen
→ Raw Source erhalten und Source-Notiz aktualisieren
→ knowledge-distill
→ bei tragfähiger Mehrquellenlage optional knowledge-synthesis
→ Navigation und Änderungsstand aktualisieren
→ gezielte Prüfung mit knowledge-maintenance
→ Nutzung über knowledge-query
→ bei größeren Meilensteinen knowledge-base-review
```

Nicht jeder Ingest erzeugte eine neue Seite oder Synthese. Ein kleiner Tagesstand konnte nur bestehende Source- und Hauptseiten aktualisieren. Ein größeres Dokumentpaket erforderte dagegen mehrere Wissenseinheiten, Konfliktprüfung und einen abschließenden Review.

## 4. Relevante Skills

| Skill | Rolle im Fall |
|---|---|
| `knowledge-base-design` | lieferte das Modell für Wissensobjekte, Provenance, Retrieval und Datenschutz |
| `knowledge-ingest` | entschied zwischen Update, Create, Raw-only und Konfliktstatus |
| `knowledge-distill` | trennte belastbare Claims von quellennahem Fließtext |
| `knowledge-synthesis` | verband mehrere Quellen, ohne Korrelation als Kausalität auszugeben |
| `knowledge-query` | beantwortete spätere Fragen grounded aus dem Vault |
| `knowledge-maintenance` | suchte Staleness, Dubletten, Orphans, kaputte Links und Schema-Drift |
| `knowledge-base-review` | prüfte den Gesamtzustand bei größeren Meilensteinen |
| `session-handoff` | hielt Arbeitsstand und Fortsetzung zwischen getrennten Tasks knapp fest |

Zum dokumentierten Stand waren diese Skills experimentell; ihre Eval-Abdeckung war nur teilweise. Das Praxisbeispiel ändert weder Maturity noch Eval Coverage.

## 5. Rollen und Human Gates

### Menschliche Verantwortung

Der Mensch:

- stellte Quellen bereit und erklärte den beabsichtigten Kontext;
- bestätigte mehrdeutige oder korrigierte Angaben;
- entschied, welche Bereiche dauerhaft gespeichert werden durften;
- gab Löschungen, Massenverschiebungen und größere Strukturänderungen frei;
- entschied bei sensiblen Themen über Veröffentlichung und Detailtiefe;
- bewertete, ob eine abgeleitete Erkenntnis praktisch plausibel war.

### Verantwortung des Agenten

Der Agent:

- las vor dem Schreiben die lokale Projektwahrheit;
- suchte vor jeder Neuanlage nach bestehenden Seiten und Aliasen;
- erhielt Quellen und dokumentierte Ableitungen getrennt;
- kennzeichnete Evidenz, Interpretation, Hypothese und offene Lücke;
- aktualisierte Links, Frontmatter, Übersichten und Änderungsstand;
- rechnete Aggregationen nach, statt alte Zusammenfassungen fortzuschreiben;
- meldete fehlende oder widersprüchliche Quellen, statt Werte zu erfinden;
- führte keine gatepflichtigen Bulk- oder Löschaktionen stillschweigend aus.

## 6. Typischer Arbeitslauf

### Phase A – Intake und Provenance

1. Neue Dateien und Angaben wurden vollständig inventarisiert.
2. Dateityp, Zeitraum, Dokumentstatus und mögliche Zielseiten wurden bestimmt.
3. Vorhandene Identitäten, Aliase und ähnliche Seiten wurden gesucht.
4. Originale wurden in der Raw-Ebene eingeordnet; Ableitungen erhielten Links zur Quelle.
5. Korrigierte oder ersetzte Dokumente wurden als solche markiert, ohne die Historie unsichtbar zu machen.

### Phase B – Verdichtung

1. Fakten wurden aus der Quelle extrahiert.
2. Explizite Aussagen wurden von Berechnungen und Interpretationen getrennt.
3. Wiederverwendbare Claims wurden bestehenden Concepts oder Entities zugeordnet.
4. Neue Seiten entstanden nur, wenn keine passende kanonische Einheit existierte.
5. Unsichere Beziehungen blieben als Hypothese sichtbar.

### Phase C – Synthese

1. Mehrere Zeitpunkte oder Quellen wurden gemeinsam betrachtet.
2. Gegenbeispiele und alternative Erklärungen wurden mitgeführt.
3. Zeitverläufe erhielten einen klaren Datenstand.
4. Zusammenhänge wurden als Beobachtung formuliert, nicht als unbewiesene Ursache.
5. Redundante Übersichten wurden zugunsten einer kanonischen Seite zurückgebaut.

### Phase D – Verifikation

1. Raw-, Source- und Hauptseiten wurden gegeneinander geprüft.
2. Tabellen und abgeleitete Werte wurden neu berechnet.
3. Wikilinks, Frontmatter, Datumsstände und Dateiverweise wurden geprüft.
4. Veraltete Formulierungen wurden über gezielte Suche gefunden.
5. Offene Lücken und nicht ausgeführte gatepflichtige Aktionen wurden berichtet.

## 7. Fehler, Near Misses und Korrekturen

### Falsch eingeordnete Originaldateien

Einige hochgeladene Originale lagen zunächst in einem abgeleiteten Bereich. Eine Wartungsrunde erkannte die vermischte Provenance.

Korrektur:

```text
Originaldatei identifizieren
→ in Raw Sources einordnen
→ kanonische Source-Notiz erstellen oder aktualisieren
→ alte Verweise auf die Source-Notiz umstellen
→ Original anschließend unverändert lassen
```

**Lerneffekt:** Eine saubere Ordnerstruktur ist nicht nur Kosmetik. Sie schützt die Grenze zwischen Quelle und Interpretation.

### Korrigierte Quelle änderte nur einen Teil der Aussage

Eine spätere, korrigierte Aufzeichnung widerlegte eine pauschale Annahme über wiederholte Einträge. Andere Angaben derselben Quelle blieben gültig.

Korrektur:

- die betroffene Volumeninterpretation wurde zurückgenommen;
- weiterhin belegte Werte blieben erhalten;
- abhängige Übersichten wurden gezielt neu berechnet;
- die Korrektur wurde als Supersession dokumentiert.

**Lerneffekt:** Eine korrigierte Quelle macht nicht automatisch alle früheren Daten wertlos. Korrekturen müssen claimbezogen propagiert werden.

### Datei beim ersten Suchlauf nicht gefunden

Eine erwartete Quelle schien zunächst zu fehlen, weil Benennung und Ablage vom üblichen Muster abwichen. Eine breitere Suche fand sie später.

**Lerneffekt:** Kein erster Treffer ist noch kein Beleg für eine fehlende Quelle. Vor einer Lückenmeldung sind Pfad-, Namens- und Inhaltsvarianten zu prüfen.

### Veraltete Doppelübersicht

Eine ältere Hauptseite führte Werte weiter, die inzwischen auf einer kanonischen Verlaufsseite gepflegt wurden. Beide Seiten drifteten auseinander.

Korrektur:

- die kanonische Seite wurde festgelegt;
- die alte Seite wurde auf Navigation und Erklärung reduziert;
- doppelte Tabellen wurden entfernt;
- eingehende Links wurden auf das neue Ziel geprüft.

**Lerneffekt:** Wartbarkeit kann durch kontrolliertes Entfernen redundanter Inhalte steigen. Mehr Seiten bedeuten nicht automatisch mehr Wissen.

## 8. Verwendete Evidence

Die Verifikation stützte sich nicht auf die Sicherheit der Formulierung, sondern auf prüfbare Artefakte:

- Existenz und Ablage der Raw Sources;
- direkte Links von abgeleiteten Aussagen zur passenden Source-Notiz;
- Vergleich ersetzter und korrigierter Dokumentstände;
- neu berechnete Tabellen und Zeitverläufe;
- auflösbare Wikilinks und konsistentes Frontmatter;
- Suchläufe nach veralteten Begriffen, Pfaden und Datenständen;
- Zählungen von Quellen, Seiten und offenen Konflikten;
- dokumentierte Human Gates und bewusst nicht ausgeführte Aktionen.

Wo keine belastbare Quelle vorlag, blieb das Ergebnis `UNVERIFIED`, `UNKNOWN` oder als offene Frage markiert.

## 9. Datenschutz und Veröffentlichungsgrenze

Für dieses Praxisbeispiel wurden bewusst nicht übernommen:

- Namen, Geburtsdaten, Adressen oder Nutzerkennungen;
- konkrete Gesundheitsangaben oder persönliche Messwerte;
- Familien-, Finanz-, Versicherungs- oder Vertragsdaten;
- reale Tagesdaten und eindeutige Chronologien;
- private Dateipfade, Screenshots, Rohdokumente oder Chatverläufe;
- Inhalte, aus denen sich eine reale Person oder ihr Alltag rekonstruieren ließe.

Die beschriebenen Fehlerklassen und Arbeitsabläufe sind echt, ihre Darstellung ist jedoch abstrahiert. Damit bleibt der technische Lerneffekt erhalten, ohne den zugrunde liegenden Vault offenzulegen.

## 10. Ergebnis

Der Arbeitsmodus führte zu einer Wissensbasis, in der neue Quellen vorhandenes Wissen verbesserten, statt nur die Dateimenge zu erhöhen.

Besonders sichtbar wurden:

- lokale Projektregeln als wirksame Source of Truth;
- die Trennung von Rohquelle, quellennahem Wissen und Synthese;
- Search before Create als Schutz gegen Dubletten;
- claimbezogene Korrekturen statt pauschaler Überschreibung;
- getrennte Modi für Ingest, Query, Wartung und Gesamtprüfung;
- kleine Active Contexts statt vollständigem Laden des Vaults;
- Human Gates bei sensiblen oder strukturell weitreichenden Aktionen.

## 11. Was dieses Beispiel nicht zeigt

Dieses Beispiel beweist ausdrücklich nicht:

- dass Obsidian für jede Wissensbasis das richtige Werkzeug ist;
- dass ein Agent sensible Daten ohne lokale Datenschutzregeln verwalten sollte;
- dass Zusammenfassungen oder Synthesen automatisch korrekt sind;
- dass jeder Ingest alle Skills oder eine vollständige Review-Kette benötigt;
- dass ein einzelner Prompt einen langfristig gepflegten Vault erzeugt;
- dass das dokumentierte Ergebnis eine professionelle medizinische, rechtliche oder finanzielle Bewertung ersetzt;
- dass die beteiligten Skills bereits produktionsreif sind.

## 12. Übertragbares Muster

Der übertragbare Teil ist nicht die konkrete Ordnerstruktur, sondern der Vertrag zwischen Quelle, Wissen und Nutzung:

```text
Quelle erhalten
→ Herkunft sichtbar machen
→ vorhandene Identität suchen
→ Fakten claimbezogen verdichten
→ Unsicherheit und Konflikte markieren
→ nur bei ausreichender Basis synthetisieren
→ Änderungen verifizieren
→ Active Context für die konkrete Frage auswählen
→ sensible und weitreichende Aktionen menschlich freigeben
```

Damit zeigt der Fall einen anderen Arbeitsmodus als ein einmaliges Erzeugungsprojekt: kontinuierliche, provenance-bewusste Wissenspflege über viele Sitzungen hinweg.

## 13. Zentrale Referenzen

- [Workflow „Wissensbasis aufbauen und pflegen“](../../../Workflows/Wissensbasis-Aufbauen-und-Pflegen.md)
- [Skill-Katalog mit Maturity und Eval Coverage](../../../skill-catalog.yml)
