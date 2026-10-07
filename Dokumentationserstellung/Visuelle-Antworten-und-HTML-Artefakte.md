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

## Visuelle Eskalation

Nicht jede nützliche Visualisierung braucht eine eigene HTML-Datei.

Vor dem Renderer zuerst die **kleinste ausreichende Darstellungsstufe** wählen:

| Level | Wann | Typische Ausgabe |
| --- | --- | --- |
| **0 – Direct** | einfache oder dringende Frage | kurze Textantwort |
| **1 – Compact Visual** | ein nicht-trivialer Mechanismus, Vergleich oder Flow | eine kompakte Tabelle, ASCII-/Mermaid-/Inline-Visualisierung plus wenige Callouts |
| **2 – Visual Explanation** | mehrere Akteure, Phasen, Optionen, Risiken oder zusammenhängende Konzepte | strukturierte visuelle Erklärung mit wenigen Modulen |
| **3 – Visual Artifact** | Nutzer will HTML/Artefakt, hohe Informationsdichte, Wiederverwendung oder sinnvolle Interaktion | eigenständiges HTML-/Artifact-Dokument |

Leitregel:

> So weit eskalieren wie nötig, nicht so weit wie technisch möglich.

### Whiteboard-Test

Visualisierung ist besonders plausibel, wenn ein guter Erklärer spontan etwas **zeichnen** würde, weil Struktur wichtig ist:

- Was passiert zuerst und danach?
- Was hängt womit zusammen?
- Wer wartet auf wen?
- Wie ändert sich ein Zustand?
- Welche Option passt unter welcher Bedingung?
- Welche Eingaben verändern welches Ergebnis?

Wenn eine gute Antwort natürlicherweise ein Satz wäre, ist Level 0 meist richtig.

### Urgency Override

Bei Incident, Meeting oder ausdrücklichem Zeitdruck:

1. Entscheidung / Sofortmaßnahme zuerst;
2. kein vollständiges Artefakt vor der eigentlichen Hilfe;
3. höchstens eine kleine Visualisierung, wenn sie einen Fehler verhindert;
4. ausführliche Visual-Erklärung erst danach oder auf Wunsch.

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

### 5. Visual Fidelity

Korrekte Zahlen können trotzdem irreführend dargestellt werden.

Bei Daten, KPIs und Charts zusätzlich prüfen:

- **Datenform vor Charttyp:** erst klären, was ein Datenpunkt trägt, danach die Darstellung wählen;
- fehlender Wert bleibt fehlend und wird nicht still zu `0`;
- geschätzte / modellierte Werte nicht ununterscheidbar in eine Ist-Serie mischen;
- fortgeschriebene oder veraltete Werte sichtbar kennzeichnen;
- Titel und Callouts dürfen der tatsächlichen Datenlage nicht widersprechen;
- Einheit und Bezugsgröße müssen sichtbar sein, wenn sie für Interpretation nötig sind;
- 3D-Darstellung vermeiden, wenn Perspektive Größen verzerrt;
- Dual-Axis nur mit sehr guter Begründung; sonst bevorzugt getrennte oder normalisierte Ansichten;
- bei Balken-/Säulen-/Flächendiagrammen einen abgeschnittenen Wertebereich nicht so einsetzen, dass kleine Unterschiede massiv größer wirken;
- bei Liniencharts ist ein Nullstart nicht automatisch erforderlich; die Achse muss die Aussage fair und nachvollziehbar tragen;
- Farbe unterstützt Bedeutung, ersetzt aber keine Labels.

Bei Review eines vorhandenen Charts gilt:

> Nicht aus Pixeln schätzen, was als Wert, Achsgrenze oder Einheit nicht tatsächlich belegt ist.

### 6. Progressive Detailtiefe

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

## Interaction Gate

Interaktion ist nur dann sinnvoll, wenn sie eine konkrete Leserfrage beantwortet.

Jedes Control muss diese Kette besitzen:

```text
Reader Question
→ User Action
→ sofort sichtbare neue Erkenntnis
```

Beispiele:

- Slider → zeigt eine nicht-triviale Auswirkung eines Parameters;
- Tabs → vergleichen zwei konkrete Zustände oder Codepfade;
- Stepper → macht eine echte Reihenfolge / einen Zustandspfad nachvollziehbar;
- Auswahlkarten → unterstützen eine Entscheidung zwischen klaren Optionen.

Nicht ausreichend:

- Button ändert nur Dekoration;
- Slider zeigt lediglich seinen eigenen Zahlenwert;
- Tabs verstecken Text ohne Vergleichsgewinn;
- Interaktion ist nötig, um überhaupt die Kernaussage zu entdecken.

### Static Story Complete

Die Defaultansicht muss die Hauptaussage bereits tragen.

Interaktion darf:

- Details vertiefen;
- Parameter erkunden;
- Alternativen vergleichen;
- Entscheidungen erfassen.

Sie darf nicht die einzige Route zur Kernaussage sein.

### Export Contract für Entscheidungs-/Editierartefakte

Wenn Interaktion Nutzerentscheidungen, Kommentare, Prioritäten oder editierte Werte erfasst, braucht das Artefakt einen klaren Rückweg:

- Copy as text / markdown / JSON;
- Download/Export, wenn die Runtime das sauber unterstützt;
- oder eine gleichwertige host-native Übergabe.

Ohne verwertbaren Output ist ein aufwendiges interaktives Review-/Editierartefakt oft nur ein Spielzeug.

## Ausgabeform nach Nutzung

Nicht jede visuelle Antwort ist dasselbe Produkt.

| Nutzung | Bevorzugte Form |
| --- | --- |
| mehrere unabhängige Kennzahlen überwachen | Dashboard |
| eine Schlussfolgerung mit Evidence erklären | Report / Visual Explanation |
| kompakt drucken oder mitnehmen | One-Pager |
| wenige Kernbefunde in Mail/Chat transportieren | Snapshot / kompakte Visualisierung |
| live präsentieren | Präsentations-/Slides-Workflow statt Visual-Answer-Kern |
| Parameter erkunden / Optionen auswählen | Explorable Artifact |

Wenn das Ergebnis dauerhafte Datenspeicherung, Authentisierung, Mehrbenutzerbetrieb, echte CRUD-Workflows oder produktive Web-App-Funktion braucht, endet `visual-answer`:

```text
Visual Explanation / temporary artifact
→ visual-answer

durable application / workflow tool
→ Webentwicklung / Software-Workflow
```

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

1. War die gewählte Eskalationsstufe wirklich nötig?
2. Sind Kernaussage und Prioritäten sofort sichtbar?
3. Sind alle wesentlichen Claims aus der Textbasis erhalten?
4. Wurden keine Zahlen, Status oder Unsicherheiten verändert?
5. Ist die visuelle Darstellung proportional und datengetreu?
6. Gibt es dekorative Elemente oder Controls ohne Informationswert?
7. Ist die Hauptaussage auch ohne Interaktion sichtbar?
8. Funktioniert die Ausgabe bei kleiner Breite grundsätzlich weiter?
9. Ist die Datei tatsächlich erzeugt?
10. Wurde sie visuell in einer echten Render-/Browseransicht geprüft?
11. Falls Nutzerzustand erfasst wird: gibt es einen verwertbaren Export-/Übergabepfad?

Wichtige Grenze:

```text
HTML erzeugt
≠
HTML visuell geprüft
```

Ohne Render-/Inspection-Evidence darf kein vollständiger Visual-Pass behauptet werden.

## Human-Evidence und Blindrunner-Grenze

Explorative Human-Evidence zu visuellen Antwortformen wird getrennt von dieser operativen Runtime-Dokumentation gepflegt und nicht in Golden-Task-Blindrunner-Snapshots übernommen.

Für die operative Regel gilt nur:

- visuelle Struktur muss einen konkreten Time-to-Signal-Nutzen haben;
- Inhaltstreue und Default-Verständlichkeit bleiben Pflicht;
- ein Human-Preference-Test ist kein Triggerbeweis und keine Maturity-Evidence.

## Leitgedanke

> Nicht mehr Oberfläche erzeugen. Weniger Zeit bis zum wichtigen Signal erzeugen.
