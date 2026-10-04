# ChatGPT-Befehle, Lernwerkzeuge und interaktive Funktionen

Stand: 2026-10-04

## Zweck

Diese Seite ist eine **praktische Referenz für Befehle, Shortcuts, Skills und interaktive Werkzeuge in ChatGPT**.

Sie beantwortet vier Fragen:

1. Was gibt es?
2. Was macht es?
3. Wann ist es nützlich?
4. Wie rufe ich es auf?

Die hier beschriebenen Produktfunktionen sind **keine KI-Regeln-Skills**. KI-Regeln beschreibt wiederverwendbare Arbeitsdisziplinen; diese Seite dokumentiert Werkzeuge, die ChatGPT selbst oder installierte/aktivierte Skills und Plugins bereitstellen.

## Wichtig: Nicht jeder Slash-Befehl ist gleich

Das ChatGPT-Eingabefeld kann mehrere Arten von Einträgen zusammen anzeigen:

- offizielle App-/Desktop-Slash-Commands;
- account- oder rolloutabhängige Lernshortcuts;
- aktivierte Skills;
- benutzerdefinierte Prompts;
- Plugins, die über `@` aufgerufen werden;
- reine Prompt-Kürzel, die nur wie Slash-Befehle aussehen.

OpenAI dokumentiert ausdrücklich:

- `/` öffnet beziehungsweise filtert die aktuell verfügbare Command-Liste;
- verfügbare Slash Commands können von Umgebung und Zugriff abhängen;
- aktivierte Skills können ebenfalls in der Slash-Command-Liste erscheinen;
- benutzerdefinierte Prompts können als `/prompts:<name>` auftauchen;
- auf ChatGPT Web gilt die dort tatsächlich angezeigte Composer-Liste; Desktop-/Codex-Befehle sind nicht automatisch identisch mit Web.

Deshalb ist die eigene Oberfläche immer die beste Antwort auf:

> Welche Befehle kann **ich hier gerade** wirklich benutzen?

## Statusklassen

| Status | Bedeutung |
|---|---|
| `DOCUMENTED` | durch eine aktuelle OpenAI-Primärquelle dokumentiert |
| `UI-OBSERVED` | in einer aktuellen ChatGPT-Oberfläche beobachtet, aber nicht als universell verfügbar dokumentiert |
| `CONDITIONAL` | offiziell beschrieben, aber nur in bestimmten Clients, Accounts oder Rollouts verfügbar |
| `PLUGIN` | installierbares/aktivierbares Werkzeug, meist über `@` |
| `PROMPT-SHORTCUT` | nützliche Kurzschreibweise, aber kein belegter Produktbefehl |
| `UNVERIFIED` | aktueller Produktstatus nicht ausreichend belegt |

---

# 1. Lernen und visuelles Verstehen

Diese Werkzeuge sind besonders interessant für Schule, Studium, Weiterbildung und Prüfungsvorbereitung.

## Übersicht

| Aufruf | Werkzeug | Wofür? | Status |
|---|---|---|---|
| `/flashcards` | Lernkarten | Fakten, Begriffe, Definitionen, Vokabeln | `UI-OBSERVED` · Funktion `DOCUMENTED` |
| `/quiz` / Quizfragen | Quiz | aktives Abrufen, Wissenslücken finden | `CONDITIONAL` |
| `/sketchnodes` | Sketchnotes | Thema als visuelle Notizen mit Struktur | `UI-OBSERVED` |
| `/mindmaps` | Mindmap | Beziehungen und Hierarchien verstehen | `UI-OBSERVED` |
| `/comicnodes` | Lerncomic | Ablauf oder Konzept bildhaft erzählen | `UI-OBSERVED` |
| `@study` | Lernmodus | schrittweise lernen statt Antwort bekommen | `DOCUMENTED` |
| `@Visualize` | interaktive Visualisierung | Diagramme, Maps, Rechner, Simulationen | `CONDITIONAL` |
| `@MindMap` | MindMap-Plugin | interaktive, zoombare Mindmaps | `PLUGIN` |

Die `UI-OBSERVED`-Einträge sind bewusst nicht als universelle ChatGPT-API dokumentiert. Sie wurden in aktuellen ChatGPT-Oberflächen beobachtet beziehungsweise können durch aktivierte Skills/Experimente in der Slash-Liste auftauchen.

## /flashcards — Lernkarten

**Wofür**

- Definitionen;
- Vokabeln;
- Formeln;
- Fakten;
- Frage-Antwort-Paare;
- Prüfungsvorbereitung.

**Beispiel**

```text
/flashcards

Erstelle aus diesem Kapitel 20 Lernkarten.
Eine Karte = genau eine prüfbare Information.
```

Oder ohne Shortcut:

```text
Erstelle mir Lernkarten aus diesen Notizen.
```

**Was ChatGPT aktuell kann**

Die interaktive Flashcard-Funktion ist offiziell dokumentiert:

- Karten umdrehen;
- bekannte/unbekannte Karten markieren;
- falsch beantwortete Karten erneut üben;
- Karten mischen;
- Kartensätze in der Bibliothek speichern;
- Karten nachträglich ergänzen oder bearbeiten.

**Wann besonders gut**

Wenn einzelne Informationen zuverlässig abrufbar sein müssen.

---

## Quiz / Quizfragen

**Wofür**

- aktives Abrufen;
- Prüfungssimulation;
- Wissenslücken;
- Transferfragen;
- Verständnis statt Wiedererkennen.

OpenAI dokumentiert, dass manche Accounts oder Apps eigene Lernshortcuts wie **Quizzes** anzeigen können. Die genaue Shortcut-Bezeichnung kann variieren.

**Beispiel**

```text
Quiz mich zu diesem Kapitel.
Eine Frage nach der anderen.
Warte auf meine Antwort.
Erkläre Fehler erst danach.
```

Für höheren Anspruch:

```text
Stell mir 10 Fragen.
4 Faktenfragen
3 Verständnisfragen
3 Transferfragen

Bewerte erst nach meiner Antwort.
```

---

## /sketchnodes — visuelle Sketchnotes

**Wofür**

- ein Thema schnell überblicken;
- Zusammenhänge sichtbar machen;
- Text in visuelle Lernnotizen verwandeln;
- vor dem Auswendiglernen erstmal verstehen.

**Beispiel**

```text
/sketchnodes

Erkläre den Blutkreislauf.
Zeige Hauptstationen, Pfeile und kurze Merksätze.
```

**Besonders sinnvoll**

Bei Stoff, der gleichzeitig Struktur und einzelne Begriffe enthält.

**Status**

Aktuell als UI-/Skill-Shortcut beobachtet; keine belastbare öffentliche Primärquelle garantiert den Befehl für alle Accounts.

---

## /mindmaps — Mindmap

**Wofür**

- Oberthema → Unterthemen;
- Ursache/Wirkung;
- Kapitelstruktur;
- Konzeptbeziehungen;
- Brainstorming;
- große Stoffmengen vorstrukturieren.

**Beispiel**

```text
/mindmaps

Erstelle eine Mindmap zur Photosynthese.
Hauptzweige:
- Voraussetzungen
- Ablauf
- Produkte
- Bedeutung
- typische Prüfungsfragen
```

**Lerntipp**

Mindmap zuerst für das **Verstehen**, danach Flashcards für das **Abrufen**.

```text
Mindmap
→ schwache Knoten erkennen
→ daraus Flashcards bauen
→ Quiz
```

**Status**

Als UI-/Skill-Shortcut beobachtet; kann account-, rollout- oder skillabhängig sein.

---

## /comicnodes — Lernstoff als Comic

**Wofür**

- Abläufe;
- Ursache/Wirkung;
- historische Ereignisse;
- biologische Prozesse;
- abstrakte Konzepte mit handelnden Elementen;
- Stoff, den man sich über eine Geschichte besser merkt.

**Beispiel**

```text
/comicnodes

Erkläre Mitose als kurzen Lerncomic.
Jede Phase soll ein eigenes Panel bekommen.
Unter jedem Panel: ein korrekter Merksatz.
```

Oder:

```text
/comicnodes

Erkläre Angebot und Nachfrage als Gespräch
zwischen Verkäufer, Käufer und Marktpreis.
```

**Stärke**

Narrative und Bilder erzeugen zusätzliche Erinnerungsanker.

**Grenze**

Ein Comic ist eine Erklärungsschicht, keine Primärquelle. Fachliche Vereinfachungen gegen Lernmaterial prüfen.

**Status**

Als UI-/Skill-Shortcut beobachtet; derzeit keine öffentliche OpenAI-Dokumentation gefunden, die universelle Verfügbarkeit garantiert.

---

## @study — Lernmodus

**Status:** `DOCUMENTED`

Auf ChatGPT Web:

```text
@study
```

eingeben und **Study / Lernen** aus den Vorschlägen wählen.

Alternativ:

```text
chatgpt.com/studymode
```

Der Lernmodus ist dafür gedacht, nicht sofort nur die Endantwort auszugeben.

Er kann:

- Fragen stellen;
- schrittweise Hinweise geben;
- Vorwissen berücksichtigen;
- Verständnis überprüfen;
- hochgeladene Notizen/PDFs einbeziehen;
- Quizfragen erstellen;
- Karteikarten-artige Wiederholung durchführen.

**Beispiel**

```text
@study

Ich lerne SQL-Joins.
Frag zuerst mein Vorwissen ab.
Erkläre dann nur die Lücken.
Gib mir anschließend 5 Aufgaben.
```

---

## @Visualize — interaktive Visualisierung

**Status:** `CONDITIONAL`

OpenAI beschreibt Visualizations als Preview. Je nach Plan, Plattform, Account und Workspace kann es fehlen.

Aufruf:

```text
@Visualize
```

**Kann geeignet sein für**

- Diagramme;
- Maps;
- Rechner;
- Simulationen;
- interaktive Erklärungen;
- veränderbare Parameter.

**Beispiel**

```text
@Visualize

Zeige mir interaktiv,
wie sich Zins, Laufzeit und Sparrate
auf das Endkapital auswirken.
```

Oder:

```text
@Visualize

Visualisiere den Wasserkreislauf
mit klickbaren Stationen.
```

---

## @MindMap — optionales MindMap-Plugin

Im ChatGPT-Plugin-Verzeichnis ist aktuell ein Plugin **MindMap** verfügbar.

Aufruf nach Installation:

```text
@MindMap
```

Beispiel:

```text
@MindMap Visualise deep learning topics
```

Es erzeugt interaktive, ein-/ausklappbare Mindmaps mit Pan/Zoom und erklärbaren Knoten.

Das ist von einem eingebauten Slash-Shortcut wie `/mindmaps` zu unterscheiden:

```text
/mindmaps
→ account-/skillabhängiger Shortcut

@MindMap
→ konkret installiertes Plugin
```

---

# 2. Offizielle ChatGPT-/Desktop-Slash-Commands

OpenAI dokumentiert für die Desktop-/Developer-Oberflächen eine Reihe echter Slash Commands.

Wichtig:

> ChatGPT Web besitzt eine eigene Composer-Command-Liste. Nicht jeder Desktop-/Codex-Befehl muss dort erscheinen.

## Planung und längere Aufgaben

### /plan

Planmodus für mehrschrittige Aufgaben.

```text
/plan
```

Sinnvoll vor:

- größeren Codingaufgaben;
- Migrationen;
- Rechercheprojekten;
- komplexen Dokumenten;
- Aufgaben mit mehreren Abhängigkeiten.

### /goal

Setzt ein persistentes Ziel, auf das ChatGPT hinarbeitet.

OpenAI empfiehlt, das Ziel bei Bedarf zuerst mit `/plan` zu formen.

```text
/plan
→ Plan klären
/goal
→ Ziel als laufende Aufgabe setzen
```

### /side

Öffnet einen temporären Nebenchat, ohne den Hauptfaden zu unterbrechen.

Praktisch für:

- Zwischenfrage;
- Begriff klären;
- Alternative prüfen;
- kleinen Seitentest durchführen.

### /compact

Komprimiert den Kontext eines langen Chats.

Nützlich, wenn:

- ein Chat sehr lang geworden ist;
- viel alter Arbeitskontext vorhanden ist;
- der Hauptstand erhalten, aber Ballast reduziert werden soll.

---

## Modell und Verhalten

### /model

Modell für den aktuellen Chat auswählen.

### /reasoning

Reasoning-/Thinking-Aufwand wählen, wenn verfügbar.

### /personality

Antwortstil/Personality auswählen, wenn Modell und Oberfläche es unterstützen.

### /fast

Verfügbaren Fast-Service-Tier ein-/ausschalten.

---

## Projekte, Chats und Arbeitskontext

### /project

Projekt für neue Chats wählen.

### /task

Chat ohne Projekt starten.

### /fork

Aktuellen Chat in einen neuen Chat beziehungsweise Worktree verzweigen.

Praktisch, wenn zwei Lösungswege unabhängig weiterverfolgt werden sollen.

### /worktree

Arbeit in einem neuen Git-Worktree starten, wenn diese Developer-Funktion verfügbar ist.

### /local

Chat im ausgewählten lokalen Projekt ausführen.

### /cloud

Chat in der Cloud ausführen, wenn verfügbar.

### /cloud-environment

Cloud-Umgebung auswählen.

### /ide-context

Geteilten IDE-Kontext an-/ausschalten.

---

## Review und Entwicklung

### /review

Startet Code-Review-Modus.

Geeignet für:

- uncommittete Änderungen;
- Vergleich mit einem Base-Branch;
- gezieltes Diff-Review.

### /init

Erzeugt ein `AGENTS.md`-Grundgerüst für das aktuelle Projekt.

### /mcp

Zeigt MCP-Status und verbundene Server.

---

## Status und Steuerung

### /status

Zeigt unter anderem:

- Chat-ID;
- Kontextnutzung;
- Rate Limits.

### /memories

Steuert, ob der Chat Erinnerungen verwenden oder erzeugen darf, wenn Memories verfügbar ist.

### /feedback

Öffnet den Feedbackdialog.

### /pet

Weckt oder versteckt das Desktop-Pet.

```text
/pet
```

Rein funktional ist es für Lernen eher überschaubar. Für die wissenschaftlich hochrelevante Frage „Kann meine Entwicklungsumgebung ein Haustier haben?“ dagegen hervorragend.

**Scope:** ChatGPT Desktop, wenn die Funktion verfügbar ist.

### /approve

Erlaubt einen Retry nach einer automatischen Review-Ablehnung, wenn dieser Mechanismus aktiv ist.

---

# 3. Codex-/CLI-only Extras

Die Developer-/CLI-Oberflächen besitzen zusätzliche Commands. Diese **nicht mit der normalen ChatGPT-Weboberfläche verwechseln**.

| Command | Zweck |
|---|---|
| `/permissions` | Berechtigungs-/Approval-Profil wechseln |
| `/ide` | offenen IDE-Kontext einbeziehen |
| `/btw` | Alias/Variante für einen kurzen Side-Chat |
| `/stop` | laufende Background-Terminals stoppen |
| `/raw` | Raw-Scrollback ein-/ausschalten |
| `/resume` | gespeicherten Chat fortsetzen |
| `/new` | neuen Chat in derselben CLI-Sitzung starten |
| `/archive` | aktuelle Session archivieren |
| `/delete` | aktuelle Session löschen |
| `/app` | Session in der ChatGPT-Desktop-App fortsetzen |
| `/keymap` | CLI-Tastenbelegung konfigurieren |
| `/vim` | Vim-Modus für den Composer ein-/ausschalten |
| `/quit` | CLI beenden |

Diese Commands sind für Entwickler interessant, aber für einen normalen Lernchat im Web meist irrelevant.

---

# 4. Skills, Plugins und eigene Commands

## $ — Skills direkt aufrufen

OpenAI dokumentiert:

```text
$
```

öffnet beziehungsweise adressiert Skills.

Aktivierte Skills können zusätzlich in der Slash-Command-Liste erscheinen.

Das erklärt, warum Nutzer in ihrem `/`-Menü Befehle sehen können, die in der allgemeinen Slash-Command-Dokumentation nicht auftauchen.

Beispielprinzip:

```text
$<skill>
```

Die konkret verfügbaren Skills hängen von Account, Workspace und aktivierten Funktionen ab.

## @ — Plugins und Werkzeuge

Beispiele:

```text
@study
@Visualize
@MindMap
@Canva
@Miro
```

`@` adressiert ein konkretes verfügbares Werkzeug beziehungsweise Plugin.

## /prompts:<name>

Benutzerdefinierte Prompts können laut OpenAI als

```text
/prompts:<name>
```

in der Command-Liste auftauchen.

Damit lassen sich eigene wiederkehrende Arbeitsweisen als Kurzaufruf verfügbar machen.

---

# 5. Prompt-Shortcuts: nützlich, aber keine Produktbefehle

Im Internet kursieren hunderte Einträge wie:

```text
/eli5
/mindmap
/flowchart
/timeline
/cheatsheet
/teacher
/tutor
/roadmap
/diagram
/anatomy
/xray
```

Viele davon sind **keine offiziellen ChatGPT-Befehle**.

Sie funktionieren häufig trotzdem, weil das Modell versteht:

```text
/mindmap Thema
≈
"Stelle das Thema als Mindmap dar."
```

Solche Kürzel sind als persönliche Prompt-Sprache völlig legitim.

Aber:

```text
funktioniert als Prompt
≠
eingebaute Produktfunktion
```

Für KI-Regeln werden solche Einträge nur als `PROMPT-SHORTCUT` geführt, solange keine belastbare Produkt- oder UI-Evidence vorliegt.

## Kurze Denk- und Schreibcodes

Die folgenden Kürzel sind **keine belegten eingebauten ChatGPT-Befehle**. Sie sind kompakte Prompt-Shortcuts für wiederkehrende Denk- oder Schreibaufgaben.

Sie können als beobachtetes Schlüsselwort geschrieben werden:

```text
STEELMAN
PREMORTEM
TIGHTEN
```

oder als persönliche Slash-Schreibweise:

```text
/steelman
/premortem
/tighten
```

Die Slash-Variante ist dabei nur eigene Prompt-Sprache. Sie garantiert keinen Eintrag im ChatGPT-Command-Menü.

| Kürzel | Zweck | Typische Ausgabe | Status |
|---|---|---|---|
| `NO/YES` · `/no-yes` | Entscheidung oder Plan kritisch gegenprüfen | mögliche Fehlannahme, stärkstes Gegenargument, Bedingung für ein belastbareres Ja/Nein | `PROMPT-SHORTCUT` |
| `GAPS` · `/gaps` | übersehene Lücken in einem Plan finden | fehlende Aufgaben, Zuständigkeiten, Risiken oder Voraussetzungen | `PROMPT-SHORTCUT` |
| `STEELMAN` · `/steelman` | stärkste vernünftige Gegenposition formulieren | bestes Gegenargument ohne Strohmann | `PROMPT-SHORTCUT` |
| `PREMORTEM` · `/premortem` | Scheitern gedanklich vorwegnehmen | wahrscheinlichste Fehlerursachen, frühe Warnsignale, mögliche Gegenmaßnahmen | `PROMPT-SHORTCUT` |
| `TIGHTEN` · `/tighten` | Text straffen | kürzere Fassung ohne unnötige Füllsätze und ohne stillen Bedeutungsverlust | `PROMPT-SHORTCUT` |

### NO/YES — Entscheidung gegenprüfen

**Wofür**

- Kündigung oder Selbstständigkeit;
- größere Anschaffung;
- Projektstart;
- Priorisierungsentscheidung;
- Plan, bei dem man möglicherweise zu schnell auf ein gewünschtes Ergebnis zuläuft.

**Beispiel**

```text
Ich will meinen Job kündigen
und mich nächstes Jahr selbstständig machen.

NO/YES
```

Sinnvolle Antwortstruktur:

```text
WO DU FALSCH LIEGEN KÖNNTEST
- zentrale Annahme, die möglicherweise nicht trägt

STÄRKSTES GEGENARGUMENT
- die belastbarste Gegenposition

JA / NEIN / JA-WENN
- nur soweit die vorhandenen Fakten das tragen

WAS DIE ENTSCHEIDUNG ÄNDERN WÜRDE
- fehlende Evidence oder konkrete Bedingung
```

**Grenze**

Nicht künstlich widersprechen. Ein kritischer Shortcut ist kein Auftrag, zwanghaft `NO` zu sagen. Ziel ist Kalibrierung statt Yes-Man oder No-Man.

---

### GAPS — Was fehlt noch?

**Wofür**

- Launchpläne;
- Projektpläne;
- Veranstaltungen;
- Reisen;
- Prozesse;
- Produkte;
- organisatorische Vorhaben.

**Beispiel**

```text
Plan:
Wir launchen unseren Online-Kurs Mitte November.

GAPS
```

Mögliche Kategorien:

- Recht / Compliance;
- Zahlung / Abrechnung;
- Rollen und Zuständigkeiten;
- Support;
- technische Voraussetzungen;
- Kommunikation;
- Abhängigkeiten;
- Erfolgsmessung;
- Fallbacks.

Der Shortcut soll **plausible Lücken finden**, nicht eine endlose Universalcheckliste erzeugen. Fehlende Fakten als Fragen oder Annahmen markieren.

---

### STEELMAN — stärkste Gegenposition

Ein Steelman ist das Gegenteil eines Strohmanns.

Statt die Gegenseite möglichst leicht angreifbar zu formulieren, wird ihre **stärkste vernünftige Version** gebaut.

**Beispiel**

```text
Homeoffice ist produktiver als das Büro.

STEELMAN
```

Mögliche Ausgabe:

```text
DIE STÄRKSTE GEGENPOSITION

- bestes sachliches Gegenargument
- Bedingungen, unter denen es besonders stark ist
- stärkster Punkt, den die Ausgangsthese beantworten müsste
```

**Grenze**

`STEELMAN` bedeutet nicht, dass die Gegenposition automatisch wahr ist. Es verbessert die Qualität der anschließenden Bewertung.

---

### PREMORTEM — Scheitern vorwegnehmen

Beim Premortem wird angenommen, dass ein Vorhaben bereits gescheitert ist.

Dann wird rückwärts gefragt:

> Was waren wahrscheinlich die Gründe?

**Beispiel**

```text
Plan:
Wir starten im Januar einen Firmen-Podcast.

PREMORTEM
```

Bevorzugte Struktur:

```text
ANGENOMMEN, ES IST GESCHEITERT

1. wahrscheinliche Ursache
   Frühestes Warnsignal
   mögliche Gegenmaßnahme

2. wahrscheinliche Ursache
   Frühestes Warnsignal
   mögliche Gegenmaßnahme

3. wahrscheinliche Ursache
   Frühestes Warnsignal
   mögliche Gegenmaßnahme
```

**Besonders sinnvoll**

Vor Launches, Migrationen, Investitionen oder Projekten mit mehreren Abhängigkeiten.

**Grenze**

Ein Premortem ist Risikoanalyse, keine Vorhersage. Wahrscheinlichkeit und Schadenshöhe getrennt betrachten.

---

### TIGHTEN — Text straffen

`TIGHTEN` ist ein Rewrite-Shortcut.

Ziel:

> denselben Inhalt mit weniger Ballast ausdrücken.

**Beispiel**

Ausgangstext:

```text
Hallo zusammen, ich wollte euch nur kurz darüber informieren,
dass wir das für Donnerstag angesetzte Meeting aus verschiedenen
organisatorischen Gründen leider nicht wie geplant durchführen
können und es stattdessen auf Montag um 10 Uhr verschieben möchten.

TIGHTEN
```

Bevorzugte Regeln:

- Kernaussage nach vorn;
- Füllformulierungen entfernen;
- Dopplungen streichen;
- Ton und notwendige Höflichkeit erhalten;
- Zahlen, Termine, Namen und Bedingungen unverändert lassen;
- keine neuen Gründe, Zusagen oder Fakten hinzufügen.

Sinngemäß:

```text
Das Meeting am Donnerstag entfällt aus organisatorischen Gründen.
Neuer Termin: Montag, 10 Uhr.
```

Für komplexere oder sensible Texte bleibt `natuerliches-schreiben` beziehungsweise `adressatengerechte-kommunikation` die eigentliche Arbeitsdisziplin. Der Shortcut ist nur eine kompakte Bedienform.

---

## Warum diese Codes nützlich sind

Sie verändern weniger das **Thema** des Prompts als die gewünschte **Denkoperation**:

```text
NO/YES
→ Entscheidung challengen

GAPS
→ fehlende Teile suchen

STEELMAN
→ Gegenposition maximieren

PREMORTEM
→ Scheitern rückwärts analysieren

TIGHTEN
→ sprachlichen Ballast entfernen
```

Das macht sie als persönliche Prompt-Sprache nützlich.

Es bleibt aber:

```text
verständlicher Kurzprompt
≠
eingebaute ChatGPT-Funktion
```

---

# 6. Welches Lernwerkzeug für welchen Zweck?

| Ziel | Werkzeug |
|---|---|
| Stoff erstmal begreifen | `@study` |
| Gesamtstruktur erkennen | `/mindmaps` |
| visuell und locker verstehen | `/sketchnodes` |
| Ablauf/Geschichte einprägen | `/comicnodes` |
| einzelne Fakten behalten | `/flashcards` |
| Wissenslücken finden | Quiz |
| Zusammenhänge interaktiv erkunden | `@Visualize` |
| editierbare Mindmap erzeugen | `@MindMap` |
| langen Lernchat entlasten | `/compact` |
| Lernprojekt in Schritte zerlegen | `/plan` |

---

# 7. Empfohlener Lernworkflow

## Phase 1 – Orientierung

```text
@study
oder
/mindmaps
```

Ziel: Stoffstruktur verstehen.

## Phase 2 – visuelle Verankerung

```text
/sketchnodes
oder
/comicnodes
```

Ziel: zusätzliche Bilder, Beziehungen und Geschichten im Gedächtnis erzeugen.

## Phase 3 – Abruftraining

```text
/flashcards
```

Ziel: einzelne Informationen aktiv erinnern.

## Phase 4 – Prüfung

```text
Quiz mich.
```

Ziel: echte Wissenslücken sichtbar machen.

## Phase 5 – Reparatur

```text
Erkläre nur die falsch beantworteten Themen.
Erstelle danach neue Karten nur für meine Lücken.
```

Kurz:

```text
verstehen
→ strukturieren
→ visualisieren
→ erinnern
→ prüfen
→ Lücken reparieren
```

---

# 8. Gute Lernkarten statt Kartenfriedhof

Eine Karte sollte möglichst **eine prüfbare Information** enthalten.

Gut:

```text
Frage:
Was ist ein Primärschlüssel?

Antwort:
Ein Attribut oder Attributsatz,
der jeden Datensatz eindeutig identifiziert.
```

Schlecht:

```text
Erkläre Primärschlüssel, Fremdschlüssel,
Normalisierung, Transaktionen und ACID.
```

Das ist eine kleine Klausur, keine Lernkarte.

Bei prüfungsrelevanten Inhalten Karten gegen die ursprünglichen Lernunterlagen prüfen.

---

# 9. Pflege dieser Liste

Diese Seite beschreibt **Produktoberfläche**, keine dauerhaft stabile Protokollspezifikation.

Bei neuen Einträgen:

1. im aktuellen `/`-, `$`- oder `@`-Menü prüfen;
2. nach OpenAI-Primärdokumentation suchen;
3. zugrunde liegende Funktion und konkreten Shortcut getrennt bewerten;
4. Status setzen;
5. Beispielaufruf ergänzen;
6. Verfügbarkeitsgrenzen benennen.

Wenn ein Befehl nur in einem Account beobachtet wurde:

```text
UI-OBSERVED
```

statt ihn als universell verfügbar auszugeben.

Wenn ein Eintrag nur als verständliches Promptkürzel funktioniert:

```text
PROMPT-SHORTCUT
```

---

# Quellen

## OpenAI – Slash commands

https://learn.chatgpt.com/docs/reference/slash-commands

Dokumentiert die Slash-Command-Liste der Desktop-App sowie `/`, `$`, aktivierte Skills und `/prompts:<name>`.

## OpenAI – Developer commands

https://learn.chatgpt.com/docs/developer-commands

Stellt ausdrücklich klar, dass ChatGPT Web eine eigene Composer-Command-Liste besitzt und Desktop-/CLI-/Codex-Commands nicht automatisch für Web gelten.

## OpenAI – Study mode

https://help.openai.com/en/articles/11780217-using-study-mode-in-chatgpt

Dokumentiert `@study`, Lernmodus, Quiz-/Übungsfunktionen und accountabhängige Lernshortcuts.

## OpenAI – Flashcards in ChatGPT

https://help.openai.com/en/articles/20001533-flashcards-in-chatgpt

Dokumentiert die interaktive Flashcard-Funktion.

## OpenAI – Visualizations

https://learn.chatgpt.com/docs/visualizations

Dokumentiert `@Visualize` und dessen rolloutabhängige Verfügbarkeit.

## ChatGPT Plugin Directory – MindMap

Aktuell verfügbares Plugin zum Erzeugen interaktiver Mindmaps; Aufruf nach Installation über `@MindMap`.

## Leitgedanke

> Erst unterscheiden, **was** ein Werkzeug ist; dann lernen, **wann** man es sinnvoll einsetzt.
