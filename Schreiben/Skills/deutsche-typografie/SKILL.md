---
name: deutsche-typografie
description: "Deutsche Typografie in fertigen oder weit fortgeschrittenen Texten prüfen oder anwenden: Anführungszeichen, Apostroph, Gedanken-/Bis-Strich, Auslassungszeichen, Abstände bei Zahlen/Einheiten, geschützte Leerzeichen und regionale DE-/AT-/CH-Konventionen, ohne Grammatik, Stil oder Inhalt umzuschreiben. Verwenden bei Typografieprüfung, deutschen Anführungszeichen, Gedankenstrichen, Zeichenformen oder typografischer Endpolitur. Nicht für Kommaregeln, allgemeine Rechtschreibung, Stilreview oder Layoutdesign."
---

# Deutsche Typografie

Dieser Skill nutzt `../../Sprachrichtigkeit-und-Typografie.md`.

Leitgedanke:

> Typografie formt Zeichen. Sie soll nicht heimlich den Text umschreiben.

## Trigger

Typische Aufträge:

- „Prüfe die deutsche Typografie.“
- „Mach die Anführungszeichen und Gedankenstriche sauber.“
- „Sind die Abstände bei Zahlen und Einheiten korrekt?“
- „Passe den Text an deutsche beziehungsweise schweizerische typografische Konventionen an.“
- „Mach einen typografischen Endpass für diesen deutschen Text.“

## Nicht verwenden

Nicht primär verwenden für:

- Rechtschreibung, Grammatik oder Kommasetzung → `korrekturlektorat`;
- Stil, Rhythmus oder KI-typische Muster → `stilreview`;
- vollständigen Rewrite → `natuerliches-schreiben`;
- Schriftwahl, Satzspiegel, CSS-Typografie oder visuelles Layoutdesign → zuständiger Design-/Dokument-Skill;
- DIN-, Verlags- oder Corporate-Regeln ohne die konkrete lokale Vorgabe als Source of Truth.

## Ablauf

1. **Zielmedium bestimmen.** Plaintext, Markdown, HTML/JSX, Office-Dokument, Print/PDF oder anderes Medium können unterschiedliche technische Möglichkeiten haben.
2. **Variante und Hausstil bestimmen.** Deutschland, Österreich, Schweiz oder lokale Redaktionsregel nur soweit für den konkreten Fund relevant.
3. **Schutzbereiche markieren.** Code, URLs, Pfade, Frontmatter, Markup, technische Tokens und wörtliche Zitate nicht unbesehen verändern.
4. **Typografischen Pass durchführen.** Zeichenform, Leerraum und Verschachtelung prüfen.
5. **Funktion vor Zeichen wählen.** Erst klären, ob ein Zeichen Bindestrich, Gedankenstrich, Bis-Strich, Minus, Apostroph oder Anführungszeichen sein soll; dann die passende Darstellung wählen.
6. **Formatverträglichkeit prüfen.** Keine typografische Verbesserung einführen, die Markdown, HTML, JSX, Code, Suche, Copy/Paste oder das Zielsystem beschädigt.
7. **Nachkontrolle.** Geänderte Stellen im Satzzusammenhang und im Zielmedium soweit verfügbar erneut prüfen.

## Prüffelder

### Anführungszeichen

- öffnende und schließende Zeichen konsistent und korrekt;
- Verschachtelung von Zitaten;
- regionale oder lokale Variante beachten;
- gerade ASCII-Zeichen nicht automatisch ersetzen, wenn sie technische Syntax darstellen;
- wörtliche Zitate nicht inhaltlich redigieren, sofern dies nicht Teil des Auftrags ist.

Keine einzelne Form als universell erzwingen. In Deutschland und Österreich sind andere Konventionen üblich als in der Schweiz; ein Verlag oder Projekt kann wiederum eigene Vorgaben haben.

### Striche und Minus

Funktion unterscheiden:

- **Bindestrich** innerhalb von Wortbildungen oder Kopplungen;
- **Gedankenstrich** für Einschübe oder Abbrüche;
- **Bis-Strich** für Bereiche, sofern das Medium beziehungsweise der Hausstil dies vorsieht;
- **Minuszeichen** in mathematischen Kontexten.

Nicht pauschal jedes `-` durch denselben längeren Strich ersetzen.

### Apostroph

- typografischen Apostroph von Akut, Gravis und geradem ASCII-Zeichen unterscheiden;
- nur dort einsetzen, wo sprachlich beziehungsweise projektbezogen ein Apostroph vorgesehen ist;
- Apostrophfragen, die eigentlich Rechtschreibung betreffen, an `korrekturlektorat` übergeben.

### Auslassung

- Auslassungspunkte beziehungsweise Auslassungszeichen im Kontext prüfen;
- Abstände und angrenzende Satzzeichen nicht mechanisch normalisieren, wenn die syntaktische Funktion unklar ist;
- technische Dreipunktfolgen in Code oder Platzhaltern nicht verändern.

### Zahlen, Einheiten und Abstände

- Zahlen und Einheiten nach maßgeblicher Konvention trennen;
- Prozent-, Währungs- und Abkürzungsabstände kontextbezogen behandeln;
- geschützte oder schmale Leerzeichen nur verwenden, wenn Zielmedium, Rendering und Copy/Paste-Anforderungen sie tragen;
- keine unsichtbaren Sonderleerzeichen in technische Identifikatoren, Daten, Code oder URLs einfügen.

## Regionalität und Hausstil

Typografie ist nicht vollständig sprachraum-unabhängig.

Bei DE/AT/CH oder lokalen Redaktionsregeln:

- vorhandene Projektkonvention priorisieren;
- keine schweizerische Anführungszeichen- oder `ss`-Praxis ungefragt germanisieren;
- `ß/ss` selbst ist primär Rechtschreibung und gehört bei Korrekturfragen zu `korrekturlektorat`;
- eine konkrete DIN-, Verlags-, Behörden- oder Corporate-Vorgabe nur anwenden, wenn der aktuelle maßgebliche Stand tatsächlich vorliegt.

## Markup- und Dateisicherheit

Vor einer Ersetzung prüfen, ob das Zeichen Teil einer Syntax ist.

Besonders schützen:

- Markdown-Codefences und Inline-Code;
- YAML/JSON/Frontmatter;
- HTML-/XML-/JSX-Tags und Attribute;
- URLs, E-Mail-Adressen und Dateipfade;
- Shell-, SQL-, Programmiersprachen- und Konfigurationssyntax;
- Template-Platzhalter.

Typografische Schönheit rechtfertigt keinen kaputten Parser.

## Review versus Änderung

Ein Prüfauftrag bleibt ein Prüfauftrag. Wenn nur „prüfen“ oder „dein Urteil?“ verlangt ist, Funde markieren und nicht ungefragt den gesamten Text normalisieren.

Bei autorisierter Korrektur nur typografische Änderungen im vereinbarten Scope durchführen. Grammatik-, Stil- oder Inhaltsänderungen separat behandeln.

## Ausgabe

Funde unterscheiden als:

- **Typografiefehler** – nach gewählter Variante/Hausregel zu korrigieren;
- **Konventionsentscheidung** – mehrere Formen möglich, Projektentscheidung erforderlich oder bereits vorhanden;
- **Formatrisiko** – korrekte Zeichenform könnte Zielsystem/Markup beeinträchtigen;
- **außerhalb Scope** – Rechtschreibung, Grammatik, Stil, Layout oder Inhalt.

Bei Änderung nach Möglichkeit kompakt dokumentieren, welche Zeichenklasse normalisiert wurde.

## Qualitätsgrenze

Ein typografisch sauberer Text ist nicht automatisch grammatisch korrekt. Ein grammatisch korrekter Text ist nicht automatisch typografisch sauber. Beide Achsen getrennt prüfen.