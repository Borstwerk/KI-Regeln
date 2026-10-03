# Codebasierte Motion Graphics und Video

## Zweck

Codebasierte Motion Graphics behandeln Video nicht primär als einmalig generierten Clip, sondern als **programmatisch beschriebene Komposition**, die aus Layout, Text, Medien, Animation, Timing und Audio reproduzierbar gerendert werden kann.

Das ist besonders interessant, wenn ein Ergebnis iterativ und gezielt veränderbar bleiben soll:

- einzelne Farben, Texte, Layouts oder Timings korrigieren;
- Branding konsistent halten;
- Daten, Screenshots oder UI-Zustände gezielt einbauen;
- Varianten aus demselben Aufbau erzeugen;
- definierte Zwischenzustände und Frames prüfen;
- einen Render aus versionierbarem Quellzustand reproduzieren.

Der Ansatz ersetzt weder generative Videomodelle noch klassische Schnittsoftware. Er ist eine eigene Delivery-Lane mit anderen Stärken und Fehlerklassen.

## Inhalt

- Scope und Abgrenzung
- 1. Brief und Source of Truth
- 2. Runtime und Reproduzierbarkeit
- 3. Assets, Provenienz und Rechte
- 4. Storyboard, Narration und visuelle Semantik
- 5. Composition statt Prompt-Lotterie
- 6. Verifikation: Standbild und Zeit getrennt
- 7. Audio ist eine eigene Qualitätsschicht
- 8. Typische Produktionsmodi
- 9. Human Gates und Außenwirkung
- 10. Frameworkneutralität
- Leitgedanke

## Scope und Abgrenzung

Diese Regeln betreffen **gerenderte Medienartefakte** wie:

- kurze Motion Graphics;
- Social-/Talking-Head-Clips mit grafischen Overlays;
- Produkt-/Software-Promos;
- Erklär- und Schulungsvideos;
- animierte Datenvisualisierungen;
- wiederverwendbare Video-Overlays oder Titelkarten.

Interaktive UI-Motion bleibt weiterhin primär Gegenstand von `Motion-und-Mikrointeraktionen.md` sowie den Skills `motion-design`, `motion-implementation` und `motion-review`.

Codebasierte Videoproduktion kann deren Motion-Wissen nutzen, besitzt aber zusätzliche Ebenen: Storyboard, Quellen, Medienassets, Audio, Timeline, Rendering und Export.

## 1. Brief und Source of Truth

Vor Implementierung mindestens klären:

- Ziel und Zielgruppe;
- gewünschtes Format, Seitenverhältnis und ungefähre Dauer;
- zentrale Aussage oder Handlung;
- Narration / On-Screen-Text / Captions;
- Brand-/Designquellen;
- Fakten- und Produktquellen;
- vorhandene Footage-, Bild-, Logo- und Audioassets;
- gewünschter Output und geplante Veröffentlichung.

Bei Produkt- oder Softwarevideos ist die reale Produktquelle wichtiger als eine plausible Modellvorstellung. Bei Erklär-/Schulungsvideos werden fachliche Claims gegen geeignete Primär- oder belastbare Fachquellen geprüft.

## 2. Runtime und Reproduzierbarkeit

Ein browser- oder codebasierter Renderpfad **kann** deterministisches beziehungsweise seekbares Rendering ermöglichen, wenn die gewählte Runtime das technisch garantiert.

Diese Eigenschaft nicht aus dem allgemeinen Begriff „Code“ ableiten.

Vor entsprechenden Claims prüfen:

- Timingmodell der Runtime;
- Umgang mit Zufall, Zeit und Netzwerk;
- seekbare Animationen;
- Medienstart und -synchronisation;
- Fonts und externe Assets;
- Renderer-/Browser-/Codec-Versionen;
- konkrete Dokumentation der gewählten Runtime.

Reproduzierbarkeit bedeutet außerdem nicht automatisch visuelle Qualität. Derselbe Fehler kann sehr zuverlässig immer wieder gerendert werden.

## 3. Assets, Provenienz und Rechte

Assets zuerst gegen reale Quellen planen.

Bevorzugte Reihenfolge:

1. vom Nutzer bereitgestellte oder projektoffizielle Assets;
2. offizielle Brand-/Produktquellen;
3. lizenzierte beziehungsweise nachweisbar nutzbare Medien;
4. bewusst generierte Ersatzassets, wenn der Auftrag das erlaubt.

Für jedes relevante Fremdasset sollte nachvollziehbar sein:

- Herkunft;
- Nutzungsrecht/Lizenz soweit erforderlich;
- lokale eingefrorene Fassung oder stabile Referenz;
- Bearbeitungsstatus;
- Einsatz im finalen Artefakt.

Logos, UI-Screenshots oder Produktdarstellungen nicht plausibel nachzeichnen, wenn eine offizielle Quelle erforderlich ist.

„Lizenzfrei“ oder „royalty-free“ nicht als allgemeines Synonym für uneingeschränkt frei verwendbar behandeln.

## 4. Storyboard, Narration und visuelle Semantik

Vor dem Feinschliff die zeitliche Aussage strukturieren.

Ein Storyboard oder Beat-Plan soll mindestens beantworten:

- Was wird in diesem Abschnitt gesagt oder vermittelt?
- Was sieht der Zuschauer genau dann?
- Welche Information trägt Text, Bild, UI, Diagramm oder Bewegung?
- Welche Elemente sind lediglich dekorativ?
- Wo braucht es Ruhe, Übergang oder bewussten Schnitt?

Für erklärende Inhalte gilt:

> Die Grafik muss den aktuellen Gedanken erklären oder unterstützen – nicht nur gleichzeitig hübsch animiert sein.

Bei Voiceover oder Talking Head visuelle Overlays deshalb an die tatsächlich gesprochenen Claims koppeln.

## 5. Composition statt Prompt-Lotterie

Der Vorteil einer codebasierten Komposition liegt in kontrollierbaren Zuständen.

Änderungen möglichst lokal ausdrücken:

```text
bestehender Keeper
→ konkrete Abweichung benennen
→ betroffene Szene / Ebene / Zeitspanne bestimmen
→ nur notwendigen Code-/Assetbereich ändern
→ unveränderte Bereiche als Erhaltungsziel behandeln
→ erneut verifizieren
```

Nicht jede Korrektur rechtfertigt einen vollständigen Neubau der Komposition.

Für komplexe Produktionen Schichten bewusst trennen:

- Footage;
- Layout / Shapes / Typografie;
- Animation;
- Captions;
- Bilder / Logos / Screens;
- Voiceover;
- Musik;
- SFX;
- Render-/Exportkonfiguration.

## 6. Verifikation: Standbild und Zeit getrennt

Eine Kontaktübersicht, Snapshot-Serie oder ausgewählte Proof-Frames ist stark für:

- Layout;
- Typografie;
- Branding;
- sichtbare Assets;
- Crop;
- räumliche Zustände;
- Anfangs-/Endholds.

Sie beweist **nicht** zuverlässig:

- Timinggefühl;
- Easing über die Zeit;
- harte oder fehlerhafte Schnitte;
- Audio-/Lippensynchronität;
- Caption-Sync;
- Flicker;
- Übergangsartefakte;
- Rhythmus.

Für relevante Videoqualität deshalb mindestens zwei Evidence-Arten unterscheiden:

```text
Frame-/Snapshot-Evidence
+ bewegte Playback-/Render-Evidence
= belastbarerer Review
```

Bei Audio zusätzlich den tatsächlichen Mix beziehungsweise die gerenderte Tonspur prüfen.

## 7. Audio ist eine eigene Qualitätsschicht

Gute Visuals kompensieren keinen schlechten Ton.

Voice, Musik und SFX getrennt betrachten:

- Sprachverständlichkeit;
- Pegelverhältnis;
- Timing;
- Musikbett unter Sprache;
- harte Audio-Cuts;
- SFX als funktionales Feedback statt Dauerbeschallung;
- Rechte und Provenienz der Audioquellen.

Synthetisch erzeugtes Audio ist nicht automatisch ungeeignet, aber auch nicht automatisch produktionsreif. Es wird wie jeder andere Output geprüft.

## 8. Typische Produktionsmodi

Die folgenden Modi sind Routinghilfen, keine verpflichtenden Produktkategorien:

### Kurze Motion Graphic

Motion selbst trägt die Aussage: kinetische Typografie, Stat-/Chart-Hit, Logo-Sting, Callout oder kurzer Social-Overlay-Baustein.

### Talking-Head-/Footage-Repackage

Bestehendes Footage bleibt zentrale Quelle; Schnitt, Captions, Layoutwechsel, Overlays und unterstützende Grafiken erhöhen Verständlichkeit oder Aufmerksamkeit.

### Produkt-/Software-Promo

Produktwirkung wird über reale UI-/Brand-/Produktquellen sichtbar gemacht. Besonders bei immateriellen Produkten kann Motion die Nutzung oder Wirkung zeigen statt ein erfundenes physisches Objekt zu inszenieren.

### Explainer / Schulung

Fachliche Aussage und visuelle Erklärung werden gemeinsam geplant. Quellenqualität, Verständlichkeit und Claim-Visual-Mapping sind wichtiger als Effektmenge.

## 9. Human Gates und Außenwirkung

Mindestens getrennt behandeln:

- Draft/Preview erzeugen;
- finalen aufwendigen Render erzeugen, wenn Kosten oder Laufzeit relevant sind;
- veröffentlichen oder extern versenden.

Ein technisch bestandener Render ist keine Veröffentlichungsfreigabe.

Bei Werbe-, Schulungs- oder öffentlich sichtbaren Inhalten zusätzlich Claims, Rechte, Branding und sensible Informationen vor Veröffentlichung prüfen.

## 10. Frameworkneutralität

HyperFrames ist eine konkrete aktuelle Referenz für HTML-/CSS-/Media-basierte, seekbare und frameweise gerenderte Kompositionen. Andere Runtimes können andere Verträge besitzen.

Zentrale KI-Regeln übernehmen deshalb **nicht**:

- HyperFrames als Pflichtframework;
- dessen konkrete CLI-Kommandos;
- dessen Workflow-Namen als universelle Taxonomie;
- dessen Installations- oder Cloudpfade;
- dessen Laufzeitgarantien für andere Frameworks.

Übernommen werden nur allgemeine Methoden:

- editierbare Code-Composition;
- Source-/Asset-first;
- getrennte Plan-/Build-/Verify-Phasen;
- Frame- und Playback-Evidence;
- explizite Render-/Außenwirkungsgates.

## Leitgedanke

> Code macht Video gezielt veränderbar. Qualität entsteht trotzdem erst durch Quellen, Gestaltung, zeitliche Semantik und echte Render-Evidence.
