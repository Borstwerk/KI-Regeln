# Sprachrichtigkeit und Typografie

## Zweck

Diese Datei trennt vier Qualitätsachsen, die bei Textarbeit häufig vermischt werden:

1. **Orthografie** – richtige Schreibung von Wörtern, Groß-/Kleinschreibung, Getrennt-/Zusammenschreibung, Bindestrichschreibung;
2. **Grammatik und Syntax** – Flexion, Kongruenz, Satzbau, Tempus, Kasus, Bezüge und vollständige Konstruktionen;
3. **Zeichensetzung** – Komma, Punkt, Doppelpunkt, Semikolon, Klammern und andere Satzzeichen nach ihrer grammatischen beziehungsweise semantischen Funktion;
4. **Typografie** – konkrete Zeichenformen und Satzkonventionen wie Anführungszeichen, Gedanken-/Bis-Strich, Auslassungszeichen, Apostroph oder Abstände.

Stil, Stimme, Argumentationsqualität und fachliche Wahrheit sind davon getrennte Prüfachsen.

## Quellenhierarchie

Für einen konkreten Text gilt zuerst die lokale Wahrheit:

```text
verbindliche Projekt-/Redaktionsregel oder freigegebener Hausstil
→ gewünschte Sprach- und Regionalvariante
→ aktuelle normative beziehungsweise fachliche Sprachquelle
→ Wörterbücher, Korpora und Prüfwerkzeuge als sekundäre Hinweise
→ Modellgedächtnis nur mit sichtbarer Unsicherheit
```

Für standardsprachliches Deutsch dienen insbesondere:

- das **Amtliche Regelwerk der deutschen Rechtschreibung** des Rats für deutsche Rechtschreibung, einschließlich Zeichensetzung und Wörterverzeichnis;
- **grammis** des Leibniz-Instituts für Deutsche Sprache (IDS) für grammatische Systematik und Zweifelsfälle.

Das derzeit amtliche Regelwerk beruht auf dem Ratsbeschluss vom 15.12.2023 und wurde 2024 von den zuständigen staatlichen Stellen beschlossen. Bei zeitkritischen oder strittigen Sprachfragen den aktuellen Stand der Quelle prüfen.

## Fehler ist nicht gleich Präferenz

Jeder Fund wird einer der folgenden Klassen zugeordnet:

- **Fehler** – nach der maßgeblichen Norm oder lokalen Regel nicht korrekt;
- **zulässige Variante** – mehrere Schreibungen oder Konstruktionen sind korrekt;
- **Projektkonvention** – eine lokale Vorgabe entscheidet zwischen mehreren grundsätzlich möglichen Formen;
- **unklar / bedeutungsabhängig** – eine Korrektur wäre ohne Kontext nicht sicher;
- **Stiloption** – grammatisch und orthografisch korrekt, aber stilistisch veränderbar.

Eine zulässige Variante oder Stiloption darf nicht als objektiver Fehler verkauft werden.

## Minimaler Eingriff

Korrekturlesen ist kein verdeckter Rewrite.

Bei reinem Korrekturauftrag:

- Bedeutung erhalten;
- Stimme und Register erhalten;
- Wortwahl nicht ohne Not veredeln oder formalisieren;
- Satzstruktur nur so weit verändern, wie es für grammatische Korrektheit oder eindeutige Lesbarkeit nötig ist;
- bewusst fragmentarische, mündliche oder figurenspezifische Sprache nicht automatisch standardisieren;
- Fachbegriffe und etablierte Projektterminologie schützen.

Für einen stilistischen Rewrite ist `natuerliches-schreiben` zuständig. Für Stilbefunde ist `stilreview` zuständig.

## Geschützte Textbestandteile

Nicht mechanisch normalisieren:

- Eigennamen, Marken- und Produktnamen;
- URLs, E-Mail-Adressen und Pfade;
- Code, Befehle, Konfiguration, reguläre Ausdrücke und Datenbankbezeichner;
- Markdown-/HTML-/JSX-Syntax und Frontmatter;
- wörtliche Zitate, wenn nicht ausdrücklich auch das Zitat redigiert werden soll;
- historische, dialektale oder absichtlich nichtstandardsprachliche Formen;
- vom Projekt verbindlich definierte Schreibweisen.

Ein Prüfwerkzeug darf diese Schutzgrenzen nicht überstimmen.

## Sprach- und Regionalvariante

Vor normativer Korrektur nach Möglichkeit klären oder aus dem Projekt ableiten, welche Variante gilt, zum Beispiel:

- Deutsch (Deutschland);
- Deutsch (Österreich);
- Deutsch (Schweiz);
- eine andere Sprache beziehungsweise Sprachvariante.

Keine Variante stillschweigend in eine andere umschreiben. Besonders bei `ß/ss`, Anführungszeichen, einzelnen Wortvarianten und typografischen Konventionen kann der Zielraum relevant sein.

Wenn die Variante für den konkreten Fund keine Rolle spielt, ist keine unnötige Rückfrage erforderlich.

## Zweipass-Prinzip

### Pass 1 – mechanische Prüfung

Den gesamten relevanten Text lesen und systematisch prüfen:

- Rechtschreibung und Tippfehler;
- Groß-/Kleinschreibung;
- Getrennt-/Zusammenschreibung und Bindestriche;
- Flexion, Kongruenz, Kasus und Numerus;
- Tempus- und Personenbezüge;
- Pronomen- und Referenzklarheit, soweit grammatisch relevant;
- fehlende oder doppelte Wörter;
- Satzgrenzen und Satzbau;
- Kommas und übrige Zeichensetzung;
- unbeabsichtigte Wortdopplungen;
- offensichtliche Leerraum-/Zeichenfehler.

### Pass 2 – erneute Lektüre nach Änderungen

Nach einer Korrektur den **geänderten Gesamttext erneut als Text lesen**, nicht nur den Diff.

Prüfen:

- Wurde durch die Korrektur ein neuer Grammatik- oder Anschlussfehler erzeugt?
- Hat sich Bedeutung, Unsicherheit oder Stimme verändert?
- Sind Satzzeichen nach dem Umbau noch korrekt?
- Sind geschützte Tokens und Formatierung intakt?
- Bleiben Zweifelsfälle sichtbar statt weggeraten?

Ein einzelner Toollauf oder der erste gefundene Fehler beendet den Korrekturpass nicht.

## Zeichensetzung

Zeichensetzung ist nicht bloß optische Formatierung. Sie kann Syntax und Bedeutung abbilden.

Daher:

- Kommas nicht allein nach Sprechpause setzen oder entfernen;
- optionale Kommas beziehungsweise alternative zulässige Konstruktionen nicht als zwingenden Fehler darstellen;
- bei mehrdeutiger Struktur zuerst die gemeinte Syntax klären;
- Anführungszeichen sowohl grammatisch als auch typografisch im Kontext prüfen;
- Gedankenstrich, Bindestrich und Bis-Strich nicht als austauschbare Zeichen behandeln.

## Deutsche Typografie

Typografische Korrektur betrifft die **Darstellungsform**, nicht automatisch Grammatik oder Stil.

Typische Prüffelder:

- öffnende und schließende Anführungszeichen sowie Verschachtelung;
- Apostroph versus Akzent-/ASCII-Ersatzzeichen;
- Bindestrich, Gedankenstrich, Bis-Strich und mathematisches Minus nach Funktion;
- Auslassungszeichen und seine Abstände;
- Abstände bei Zahlen, Einheiten, Prozentangaben und Abkürzungen;
- geschützte Leerzeichen, wenn das Zielmedium sie sinnvoll unterstützt;
- typografische Sonderzeichen nur dort, wo Dateiformat, Rendering und Projektkonvention sie tragen;
- DE-/AT-/CH-spezifische oder redaktionelle Varianten.

Keine einzelne typografische Konvention als universell erzwingen, wenn Zielmedium oder Projekt etwas anderes verlangt. Für DIN-, Verlags-, Corporate- oder wissenschaftliche Hausregeln ist die konkrete aktuelle lokale Vorgabe Source of Truth.

## Toolunterstützung

Rechtschreib-, Grammatik- oder Stilprüfer wie LanguageTool können zusätzliche Fundstellen liefern. Ihre Vorschläge sind **Hinweise, keine Autorität**.

Vor Übernahme eines Toolfunds prüfen:

1. passt die Sprache und Regionalvariante?
2. ist der betroffene Text geschützt?
3. ist es tatsächlich ein Fehler oder nur eine Präferenz?
4. verändert der Vorschlag Bedeutung, Register oder Fachterminologie?
5. deckt die aktuelle normative beziehungsweise lokale Quelle den Fall?

Kein externes Prüfwerkzeug ist Voraussetzung für die Skills dieses Repositories.

## Review versus Änderung

Ein Auftrag wie „Prüfe die Rechtschreibung“ oder „Dein Urteil?“ ist zunächst ein Prüfauftrag. Er autorisiert nicht automatisch eine vollständige Textänderung oder Dateiüberschreibung.

Wenn eine Korrekturfassung ausdrücklich gewünscht oder innerhalb des vereinbarten Scopes autorisiert ist, dürfen objektive Korrekturen angewendet werden. Bedeutungsrelevante Zweifelsfälle, Stiländerungen und größere Satzumbauten bleiben sichtbar beziehungsweise separat freizugeben.

## Leitgedanke

> Korrekturlesen soll Fehler entfernen, nicht den Autor entfernen.