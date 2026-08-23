# Entwicklungsprozess für KI-gestützte Softwarearbeit

## Zweck

Dieser Prozess hält Anforderung, Planung, Umsetzung, Nachweis und Freigabe nachvollziehbar zusammen.

Er soll bewusst klein bleiben. Ziel ist keine Prozessbürokratie, sondern die dauerhafte Verbindung zwischen gewünschtem Verhalten, technischer Entscheidung, Code und Nachweis.

## Grundprinzip

Relevante Änderungen durchlaufen fünf Gates:

```text
Anforderung
    ↓
Planung
    ↓
Umsetzung
    ↓
Review und Nachweis
    ↓
Freigabe
```

Eine größere Änderung beginnt nicht unmittelbar mit Code.

## Gate 1 – Anforderung

Vor der Umsetzung wird beschrieben:

- welches Problem besteht;
- warum eine Änderung notwendig ist;
- welches Verhalten danach gelten soll;
- welche Grenzen eingehalten werden müssen;
- woran die Umsetzung später als erfolgreich gilt.

Für größere Änderungen ist eine kurze stabile Requirement-ID sinnvoll.

Beispiel:

```text
APP-020-IMP-01
```

Die ID dient der Rückverfolgbarkeit und soll nicht zu einem komplizierten Nummernsystem werden.

### Mindestinhalt

```markdown
## APP-020-IMP-01 – Titel

### Problem / Grund
Warum existiert diese Anforderung?

### Anforderung
Welches Verhalten wird gefordert?

### Akzeptanzkriterien
Welche konkret überprüfbaren Bedingungen müssen erfüllt sein?

### Nachweis
Welche automatisierten oder manuellen Prüfungen belegen die Erfüllung?
```

Eine eigene Requirement-ID ist besonders sinnvoll bei neuen Funktionen, fachlichem Verhalten, Datenänderungen, Sicherheitsverhalten, Dateiformaten, größeren Fehlerkorrekturen oder Architekturänderungen.

Für reine Rechtschreib- oder Darstellungsänderungen ohne Verhaltensänderung ist sie normalerweise nicht nötig.

Faustregel:

> Wenn eine Änderung einen eigenen fachlichen oder technischen Regressionstest verdient, sollte geprüft werden, ob sie auch eine eigene Anforderung verdient.

## Gate 2 – Planung

Nach der Anforderung wird zunächst geplant. In dieser Phase wird noch nicht implementiert.

Der Plan sollte enthalten:

- betroffene Anforderung;
- relevante bestehende Architektur;
- voraussichtlich betroffene Dateien und Komponenten;
- geplante technische Lösung;
- bestehende Entscheidungen, die beachtet werden müssen;
- Risiken;
- geplante Tests;
- notwendige manuelle Prüfungen;
- Auswirkungen auf Dokumentation, Betrieb oder Release, soweit relevant.

Bestehende Architekturentscheidungen dürfen nicht stillschweigend ersetzt werden.

Erst nach Prüfung und Freigabe des Plans beginnt die Umsetzung, sofern das Projekt diesen Freigabeschritt vorsieht.

## Gate 3 – Umsetzung

Die Umsetzung folgt dem freigegebenen Plan.

Dabei gelten insbesondere:

- Ursache statt Symptom beheben;
- KISS vor Architekturspielerei;
- keine unnötigen neuen Abhängigkeiten;
- bestehenden stabilen Code nicht ohne konkreten Grund umbauen;
- öffentliche Schnittstellen und persistierte Daten nicht beiläufig verändern;
- Sicherheits- und Validierungsregeln nicht aufweichen, nur damit Tests grün werden;
- manuelle Benutzereingaben nicht ohne ausdrückliche Anforderung überschreiben;
- bei Fehlerkorrekturen möglichst einen Regressionstest ergänzen.

### Traceability

Bei größeren Änderungen sollten Commit, Pull Request oder Abschlussbericht die Requirement-ID enthalten.

Damit bleibt nachvollziehbar:

```text
Anforderung
→ Änderung
→ Code
→ Tests
```

## Gate 4 – Review und Nachweis

„Tests sind grün“ reicht nicht als vollständiges Review.

Für jedes Akzeptanzkriterium wird angegeben, wodurch es belegt wird.

Mögliche Nachweise:

- automatisierter Test;
- Integrationstest;
- statische Prüfung;
- manueller Test;
- externer Validator;
- reproduzierbare Messung;
- Diff- oder Konfigurationsprüfung.

Das Review umfasst mindestens:

- Vergleich mit der ursprünglichen Anforderung;
- Prüfung des tatsächlichen Diffs;
- Prüfung auf Scope Creep;
- Prüfung auf unnötige Architekturänderungen;
- Prüfung neuer Abhängigkeiten;
- Prüfung der Tests selbst;
- Fehler- und Randfälle;
- notwendige Dokumentationsänderungen.

Bei sicherheitskritischen, standardrelevanten oder datenverändernden Funktionen reicht der Abschlussbericht des Implementierers nicht aus. Der tatsächliche Code beziehungsweise Diff wird geprüft.

## Gate 5 – Freigabe

Eine Anforderung gilt erst als erfüllt, wenn:

- alle Akzeptanzkriterien erfüllt sind;
- vorgesehene automatisierte Prüfungen bestanden wurden;
- notwendige manuelle Prüfungen bestanden wurden;
- Dokumentation und tatsächliches Verhalten übereinstimmen.

Die Meldung „fertig“ durch Mensch oder KI ist allein kein Freigabenachweis.

## Release-Freigabe

Ein Release ist mehr als die Summe grüner Unit-Tests.

Je nach Projekt können dazugehören:

- erfüllte Anforderungen;
- vollständige CI;
- externe Validatoren;
- manuelle Abnahme;
- Installations- oder Upgradeprüfung;
- Release-Artefakte und Checksummen;
- Dokumentation und Release Notes.

Der konkrete Releaseprozess bleibt projektspezifisch.

## Architekturentscheidungen

Nicht offensichtliche oder langfristig wichtige Entscheidungen sollten mit ihrem Grund im Projekt erhalten bleiben.

Eine Entscheidung sollte dokumentiert werden, wenn ein späterer Entwickler berechtigterweise fragen könnte:

> Warum wurde das nicht einfacher oder anders gelöst?

Nicht jede lokale Implementierungswahl benötigt einen eigenen Decision-Eintrag.

## Rollen typischer Dokumente

| Dokument | Zweck |
|---|---|
| `BACKLOG.md` | mögliche oder offene Arbeit |
| `REQUIREMENTS-*.md` | verbindliche Anforderungen |
| `DECISIONS.md` | Gründe für wichtige Entscheidungen |
| `ARCHITECTURE.md` | aktueller technischer Aufbau |
| `TESTING.md` | Prüfstrategie und Nachweise |
| `DEVELOPMENT.md` | technische Mitarbeit am Projekt |

Dateinamen sind Beispiele. Entscheidend ist die klare Rolle, nicht die konkrete Benennung.

## Einsatz generativer KI

Generative KI kann Planung, Implementierung, Review, Tests und Dokumentation unterstützen. Sie ersetzt nicht die Verantwortung für veröffentlichte Software.

Für KI-Agenten gilt insbesondere:

- vorhandene Dokumentation zuerst lesen;
- relevante Anforderungen identifizieren;
- größere Änderungen nicht ohne Plan beginnen;
- bestehende Entscheidungen nicht stillschweigend ersetzen;
- Tests nicht abschwächen, damit Implementierung grün wird;
- Akzeptanzkriterien konkreten Nachweisen zuordnen;
- Unsicherheiten offen benennen statt Annahmen als Tatsachen darzustellen.

## Leitgedanke

Am Ende soll nicht nur bekannt sein:

> Der Code läuft.

Sondern auch:

> Warum läuft er genau so und wodurch wissen wir, dass er das Richtige tut?