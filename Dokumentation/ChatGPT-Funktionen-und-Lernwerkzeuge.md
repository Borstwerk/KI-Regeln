# ChatGPT-Funktionen und Lernwerkzeuge

Stand: 2026-10-01

## Zweck

Diese Seite sammelt **produktseitige ChatGPT-Funktionen, Shortcuts und interaktive Lernwerkzeuge**, die beim Lernen, Wiederholen, Visualisieren und Prüfen von Wissen helfen können.

Sie sind **keine KI-Regeln-Skills**.

KI-Regeln beschreibt wiederverwendbare Arbeitsdisziplinen. Diese Seite beantwortet dagegen:

> Welche interaktiven Werkzeuge stellt ChatGPT selbst aktuell bereit und wie kann ich sie sinnvoll fürs Lernen einsetzen?

## Statusklassen

| Status | Bedeutung |
|---|---|
| `DOCUMENTED` | durch eine aktuelle OpenAI-Primärquelle dokumentiert |
| `UI-OBSERVED` | in einer aktuellen ChatGPT-Oberfläche beobachtet, aber nicht als universell verfügbar dokumentiert |
| `PROMPT-SHORTCUT` | nur eine nützliche Kurzschreibweise/Community-Konvention, kein belastbar dokumentierter Produktbefehl |
| `UNVERIFIED` | aktueller Produktstatus nicht ausreichend belegt |

Wichtig:

> Slash-Befehle und aktivierte Skills können je nach Client, Account, Plan, Experiment und verfügbarer Umgebung unterschiedlich sein.

Die verlässlichste aktuelle Sicht auf die eigene Oberfläche ist deshalb:

```text
im Chat-Eingabefeld "/" tippen
→ angebotene Befehle prüfen
→ nur dort sichtbare Befehle als für diese Umgebung verfügbar behandeln
```

In unterstützten Oberflächen können aktivierte Skills ebenfalls in der Slash-Command-Liste erscheinen. Die konkrete Liste ist deshalb keine dauerhaft universelle API.

## Lernwerkzeuge

### Lernkarten / Flashcards

**Status:** `DOCUMENTED` für die Funktion · Slash-Shortcut abhängig von Oberfläche

Typischer Shortcut in unterstützten Oberflächen:

```text
/flashcards
```

Alternativ immer verständlich:

```text
Erstelle mir Lernkarten aus diesen Notizen.
```

Geeignet für:

- Begriffe und Definitionen;
- Fakten;
- Vokabeln;
- Formeln und Zuordnungen;
- prüfbare Frage-Antwort-Paare;
- Wiederholung aus hochgeladenen Lernunterlagen.

ChatGPT kann interaktive Lernkarten erzeugen, Karten umdrehen, bekannte/unbekannte Karten markieren und Kartensätze in der Bibliothek ablegen.

### Quiz

**Status:** `DOCUMENTED` für die Funktion · Slash-Shortcut nicht als universell dokumentiert

Beispiel:

```text
Quiz mich zu diesem Kapitel. Eine Frage nach der anderen. Erkläre Fehler erst nach meiner Antwort.
```

Geeignet für:

- aktives Abrufen statt bloßes Wiederlesen;
- Prüfungsvorbereitung;
- Erkennen von Wissenslücken;
- Wiederholung nach Lernkarten;
- Transferfragen statt reinem Faktenabfragen.

### Sketchnotes / visuelle Lernnotizen

**Status:** `UI-OBSERVED` für `/sketchnodes`; derzeit keine belastbare öffentliche Primärdokumentation für universelle Verfügbarkeit

In unterstützten Oberflächen kann beispielsweise erscheinen:

```text
/sketchnodes
```

Sinnvoll für:

- visuelle Zusammenfassungen;
- Beziehungen zwischen Konzepten;
- Lernstoff mit vielen Abhängigkeiten;
- Überblick vor Detaillernen;
- Kombination aus Text, Symbolen und Struktur.

Da solche UI-Shortcuts experimentell oder accountabhängig sein können, vor Nutzung im aktuellen Slash-Menü prüfen.

### Visualize

**Status:** `DOCUMENTED`

Aktueller Einstieg:

```text
@Visualize
```

Danach die gewünschte interaktive Visualisierung beschreiben.

Geeignet für:

- Systeme und Zusammenhänge;
- Prozesse;
- räumliche oder zeitliche Beziehungen;
- interaktive Erklärungen;
- komplexe Konzepte, die sich schlecht nur als Fließtext lernen lassen.

## Sinnvoller Lernworkflow

Die Werkzeuge ergänzen sich besser, als wenn man nur eines davon benutzt.

### 1. Verstehen

```text
Sketchnotes / Visualize
→ Struktur und Zusammenhänge sichtbar machen
```

### 2. Verdichten

```text
Zusammenfassung
→ Kernbegriffe und Regeln identifizieren
```

### 3. Enkodieren

```text
Flashcards
→ atomare, prüfbare Wissenseinheiten erzeugen
```

### 4. Abrufen

```text
Quiz
→ Wissen ohne Vorlage reproduzieren
```

### 5. Lücken reparieren

```text
falsch beantwortete Fragen
→ gezielte Erklärung
→ neue oder überarbeitete Lernkarten
→ erneutes Quiz
```

Kurz:

```text
verstehen
→ verdichten
→ erinnern
→ prüfen
→ Lücken schließen
```

## Gute Lernkarten statt Kartenfriedhof

Eine Lernkarte sollte möglichst **eine prüfbare Information** enthalten.

Bevorzugen:

```text
Frage: Was ist der Primärschlüssel einer relationalen Tabelle?
Antwort: Ein Attribut oder Attributsatz, der jeden Datensatz eindeutig identifiziert.
```

Vermeiden:

```text
Erkläre Primärschlüssel, Fremdschlüssel, Normalisierung,
Transaktionen und ACID vollständig.
```

Das ist eher eine kleine Klausur als eine Karte.

Bei prüfungsrelevanten oder fachlich kritischen Inhalten sollten Karten gegen die ursprünglichen Lernunterlagen oder andere verbindliche Quellen geprüft werden.

## Produktbefehle sind keine Prompt-Magie

Im Internet kursieren viele Listen mit Einträgen wie:

```text
/eli5
/mindmap
/teacher
/study
/rootcause
/cheatsheet
```

Solche Kürzel können als **Prompt-Shortcuts** praktisch sein, sind aber nicht automatisch echte ChatGPT-Produktbefehle.

Deshalb gilt:

```text
im Slash-Menü vorhanden
→ produktseitig verfügbar in dieser Umgebung

nur irgendwo im Internet aufgelistet
→ höchstens Prompt-Shortcut, bis primär belegt
```

KI-Regeln sollte diese beiden Klassen nicht vermischen.

## Quellen

### OpenAI – Slash Commands

https://learn.chatgpt.com/docs/reference/slash-commands

Relevante Aussagen am geprüften Stand:

- verfügbare Slash Commands hängen von Umgebung und Zugriff ab;
- `/` öffnet beziehungsweise filtert die aktuelle Command-Liste;
- aktivierte Skills können in der Slash-Command-Liste erscheinen.

### OpenAI – Flashcards in ChatGPT

https://help.openai.com/en/articles/20001533-flashcards-in-chatgpt

Bestätigt die interaktive Lernkartenfunktion, Nutzung aus eigenen Notizen und Speicherung in der ChatGPT-Bibliothek.

### OpenAI Education – Flashcards, quizzes and Visualize

https://edunewsletter.openai.com/p/the-edu-prompt-issue-6

Bestätigt aktuelle interaktive Flashcards und Quizzes sowie `@Visualize` als Lernwerkzeug.

## Pflege

Diese Seite beschreibt **Produktoberfläche**, keine stabile Protokollspezifikation.

Deshalb bei Änderungen:

1. aktuelle OpenAI-Primärquelle prüfen;
2. tatsächliche Verfügbarkeit im Client gegenprüfen;
3. Slash-Shortcut und zugrunde liegende Fähigkeit getrennt bewerten;
4. nicht mehr belegte Einträge auf `UNVERIFIED` setzen statt still weiterzuführen;
5. Community-Promptkürzel nicht als offizielle Befehle ausgeben.

## Leitgedanke

> KI-Regeln erklärt die Methode. ChatGPT-Funktionen können dafür das passende interaktive Werkzeug liefern.
