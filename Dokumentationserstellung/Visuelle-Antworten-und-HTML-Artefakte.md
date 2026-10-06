# Visuelle Antworten und HTML-Artefakte

## Zweck

Komplexe Antworten können fachlich korrekt sein und trotzdem langsam erfassbar bleiben.

Der Zweck einer visuellen Antwort ist deshalb nicht dekoratives HTML, sondern eine kürzere **Time-to-Signal**:

> Kernaussage, Prioritäten, Zusammenhänge und Handlungsbedarf sollen auf den ersten Blick erkennbar sein, ohne fachlichen Inhalt zu verlieren.

HTML ist eine mögliche Ausgaberuntime. Der fachliche Kern bleibt rendererunabhängig.

## Wann eine visuelle Antwort sinnvoll ist

Starker Trigger, wenn mindestens eine dieser Formen vorliegt:

- mehrere zusammenhängende Konzepte, deren Beziehungen wichtig sind;
- Architektur, Datenfluss, Prozess, Zustandsfolge oder Entscheidungsbaum;
- Vergleich über mehrere Kriterien;
- Hierarchie oder Timeline;
- Review mit mehreren Findings, Severity- oder Statusklassen;
- Plan mit Phasen, Abhängigkeiten oder Prioritäten;
- der Nutzer verlangt ausdrücklich eine visuelle beziehungsweise HTML-Aufbereitung.

Typische Beispiele:

```text
Architektur erklären
→ Flow + Verantwortungsbereiche

drei Optionen vergleichen
→ Vergleichsmatrix + Empfehlung

14 Review-Findings
→ Gesamturteil + Severity + Priorität + Detailkarten
```

## Wann nicht

Keine visuelle Seite nur um ihrer selbst willen.

Near-Misses:

- kurze Faktenantwort;
- ein oder zwei Sätze;
- lockere Unterhaltung;
- reine Command-/Logausgabe ohne Erklärbedarf;
- der Nutzer verlangt Plain Text;
- die visuelle Fassung würde nur denselben Text in dekorative Karten zerlegen;
- Artefakterstellung wäre deutlich aufwendiger als der Informationsgewinn.

## Informationsarchitektur vor Renderer

Zuerst die Informationsform bestimmen:

| Informationsform | Bevorzugte Darstellung |
| --- | --- |
| Kernaussage / Warnung | Callout / Summary |
| Architektur / Abhängigkeit | Flow |
| Nachrichten über Zeit | Sequence |
| Optionen über Kriterien | Vergleichstabelle |
| Hierarchie | Tree |
| Entwicklung über Zeit | Timeline |
| viele Findings | Severity-/Status-Dashboard |
| Kennzahlen gegen Grenze | Limit-/Statusdarstellung |

Danach erst Renderer oder Ausgabetool wählen.

## Qualitätsregeln

### 1. Kernaussage zuerst

Die wichtigste Aussage darf nicht am Seitenende versteckt sein.

Bevorzugte Reihenfolge:

```text
Kernaussage / Gesamturteil
→ wichtigste Evidence / Priorität
→ strukturierte Details
→ nächster Schritt / Gate
```

### 2. Eine visuelle Einheit, eine Frage

Panels oder Bereiche sollen jeweils eine erkennbare Informationsaufgabe haben.

Nicht:

- dieselbe Aussage in drei Karten wiederholen;
- jedes Detail in eine eigene Box zerschneiden;
- dekorative Panels ohne Informationsfunktion ergänzen.

### 3. Visuelle Hierarchie muss semantisch sein

Größe, Position, Gruppierung und Statusdarstellung sollen Bedeutung transportieren.

Beispiele:

- Critical vor Low;
- Empfehlung vor Nebendetail;
- zusammengehörige Komponenten räumlich gruppieren;
- Folgebeziehungen als Flow statt Absatzkette.

Farbe darf unterstützen, aber nicht die einzige Statuscodierung sein. Textlabels wie `CRITICAL`, `PASS`, `BLOCK` bleiben sichtbar.

### 4. Inhaltstreue

Die visuelle Fassung darf:

- ordnen;
- gruppieren;
- kürzen, wenn Bedeutung erhalten bleibt;
- redundante Formulierungen entfernen.

Sie darf nicht:

- neue Fakten erfinden;
- Unsicherheit verstecken;
- Zahlen oder Severity verändern;
- Gegenargumente unterschlagen, nur damit die Seite sauberer aussieht;
- eine komplexe Entscheidung durch Design scheinbar eindeutiger machen als die Evidence erlaubt.

### 5. Progressive Detailtiefe

Auf den ersten Blick:

- Urteil;
- Status;
- Priorität;
- wesentliche Beziehung.

Beim zweiten Blick:

- Begründung;
- Evidence;
- Details;
- Fix / nächste Aktion.

## Renderer- und Runtime-Vertrag

Der portable Skill definiert **wann und wie Informationen visuell strukturiert werden**.

Die Runtime entscheidet **womit**.

```text
visual-answer
        ↓
strukturierter Inhaltsplan
        ↓
Runtime
├─ native HTML-/Dateierzeugung
├─ spezialisierter Renderer
├─ Plugin / App / Artifact-System
└─ Markdown-Fallback
```

Mögliche konkrete Runtime:

- native HTML-Dateierzeugung;
- `answer-me-with-html`;
- ein anderer deterministischer Renderer;
- eine Präsentations-/Design-App;
- reine Markdown-Struktur, wenn kein visueller Artefaktpfad verfügbar ist.

Eine konkrete Runtime ist keine fachliche Voraussetzung.

## Deterministischer Renderer bevorzugt, wenn sinnvoll

Wenn Layout, Diagrammpositionierung oder wiederkehrende Styles deterministisch erzeugt werden können, soll das Modell bevorzugt:

- Inhalt;
- Beziehungen;
- Labels;
- Prioritäten

liefern und nicht unnötig hunderte Zeilen Layoutcode generieren.

Das reduziert aber nicht automatisch Kosten oder Laufzeit. Zusätzliche Turns, großer Agentenkontext oder komplexe Renderer können den Vorteil umkehren.

Deshalb:

> Rendererwahl nach lokalem Nutzen und Evidence, nicht nach universellem Tokenversprechen.

## HTML-Hygiene

Bei direkt erzeugtem HTML bevorzugt:

- eine selbständige Datei;
- semantische Überschriften und klare Lesereihenfolge;
- responsive Darstellung;
- ausreichender Kontrast;
- Status nicht nur über Farbe;
- keine externen Tracker;
- keine CDN-/Remote-Abhängigkeit ohne Bedarf;
- keine erfundenen interaktiven Funktionen;
- keine versteckten externen Requests.

Wenn externe Assets oder Scripts nötig sind, diese als Runtime-/Security-Abhängigkeit behandeln.

## Verifikation

Vor Abschluss prüfen:

1. Sind Kernaussage und Prioritäten sofort sichtbar?
2. Sind alle wesentlichen Claims aus der Textbasis erhalten?
3. Wurden keine Zahlen, Status oder Unsicherheiten verändert?
4. Gibt es dekorative Elemente ohne Informationswert?
5. Funktioniert die Ausgabe bei kleiner Breite grundsätzlich weiter?
6. Ist die Datei tatsächlich erzeugt?
7. Wurde sie visuell geprüft?

Wichtige Grenze:

```text
HTML erzeugt
≠
HTML visuell geprüft
```

Ohne Render-/Inspection-Evidence darf kein vollständiger Visual-Pass behauptet werden.

## Explorative A/B-Evidence vom 2026-10-06

Drei manuelle Zero-Install-Vergleiche wurden mit inhaltlich parallelen Markdown- und HTML-Ausgaben durchgeführt:

1. **Architektur / Überblick** – HypeRadar-Funde und KI-Regeln-Einordnung;
2. **Mehrkriterien-Entscheidung** – drei Optionen für den Umgang mit visuellen Antworten;
3. **Review / Findings** – 14 synthetische Findings mit mehreren Severity-Stufen.

Beobachtung des menschlichen Reviewers:

- HTML wurde in allen drei Fällen bevorzugt;
- besonders genannt wurde, dass wichtige Informationen **auf den ersten Blick innerhalb kurzer Zeit** erfasst werden konnten;
- der wahrgenommene Vorteil lag in visueller Struktur, Gruppierung und Priorisierung, nicht in neuem fachlichem Inhalt.

Grenzen dieser Evidence:

- ein Reviewer;
- nicht verblindet;
- keine randomisierte Reihenfolge;
- keine gemessene Lesedauer;
- keine Recall-/Fehlerquote;
- die HTML-Seiten wurden direkt erzeugt und nicht mit dem originalen `answer-me-with-html`-Renderer gerendert;
- daraus folgt keine Token-, Kosten- oder Speed-Benchmark.

Die Evidence rechtfertigt deshalb einen **experimentellen** lokalen Skill, aber keine Maturity-Hochstufung.

## Leitgedanke

> Nicht mehr Oberfläche erzeugen. Weniger Zeit bis zum wichtigen Signal erzeugen.
