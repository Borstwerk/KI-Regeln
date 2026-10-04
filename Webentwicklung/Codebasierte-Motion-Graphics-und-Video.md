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
- 4. Canonical Media und Derived Media
- 5. Storyboard, Narration und visuelle Semantik
- 6. Composition statt Prompt-Lotterie
- 7. Verifikation: Standbild, Zeit und Identität getrennt
- 8. Audio ist eine eigene Qualitätsschicht
- 9. Typische Produktionsmodi
- 10. Human Gates und Außenwirkung
- 11. Frameworkneutralität
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

## 4. Canonical Media und Derived Media

In hybriden KI-Video-Pipelines entstehen häufig mehrere Fassungen desselben inhaltlichen Elements. Deshalb muss sichtbar bleiben, **welches Artefakt für welche Eigenschaft die Source of Truth ist**.

Beispiele:

- ein freigegebenes Charakterbild kann kanonische Identitätsreferenz sein;
- eine freigegebene Voice-/Narrationsspur kann kanonische Audioquelle sein;
- ein generierter Performance-Clip kann daraus Bewegung und Lippenbewegung ableiten;
- eine codebasierte Composition kann Performance, Voice, Captions, Motion Graphics, Musik und SFX zusammenführen.

Ein generiertes Zwischenartefakt darf eine kanonische Quelle **nicht stillschweigend ersetzen**, nur weil es technisch später in der Pipeline entstanden ist.

```text
Canonical Character / Voice / Brand / Claim
        ↓
Derived Performance / Animation / Composite
        ↓
gezielte Weiterverarbeitung
        ↓
Final Composite

Derived Artifact ≠ automatisch neue Source of Truth
```

Für relevante kanonische Medien mindestens festhalten:

- Rolle der Quelle, zum Beispiel `character-identity`, `voice-master`, `brand-asset`, `approved-script`;
- konkrete Datei/Version beziehungsweise stabile Referenz;
- welche Transformationen erlaubt sind;
- welche Eigenschaften unverändert bleiben müssen;
- wann ein Derived Artifact gegen die kanonische Quelle zurückgeprüft wird.

Wenn ein Zwischenmodell Audio, Gesicht, Text, Branding oder Timing neu interpretiert, ist das ein **Derived State**. Für das Final kann die kanonische Quelle erneut gebunden werden, wenn genau diese Eigenschaft erhalten bleiben soll.

Beispiel:

```text
Voice Master
→ Performance-Modell nutzt Audio für Lipsync/Bewegung
→ Performance-Modell verändert hörbar Stimme oder Pausen
→ Videoanteil bleibt nutzbar
→ Final Composite bindet wieder den Voice Master
→ Lip-Sync und Timing erneut prüfen
```

Damit wird nicht vorausgesetzt, dass jede Pipeline denselben technischen Weg unterstützt. Entscheidend ist die explizite Quellenrolle.

## 5. Storyboard, Narration und visuelle Semantik

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

### Character Blocking und reservierte Grafikräume

Wenn generierte Figuren oder Avatare später mit Motion Graphics zusammenspielen sollen, diese Beziehung **vor** der Performance-Generierung planen.

Für relevante Beats festhalten:

- Blickrichtung;
- Zeige-/Greifrichtung;
- Körperposition und Bewegungsraum;
- reservierte Flächen für Text, Diagramme, UI oder andere Overlays;
- Bereiche, die Gesicht, Hände oder wichtige Produktelemente nicht verdecken dürfen;
- geplante Übergabe zwischen Performance und späterer Grafik.

Blocking ist keine Garantie, dass ein generatives Videomodell die Regieanweisung exakt umsetzt. Es reduziert aber vermeidbare Kollisionen und schafft überprüfbare Erwartungen für die spätere Composition.

## 6. Composition statt Prompt-Lotterie

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

## 7. Verifikation: Standbild, Zeit und Identität getrennt

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

Bei hybriden Avatar-/Performance-Pipelines reicht außerdem ein einziger Gesamt-`PASS` nicht. Relevante Eigenschaften separat prüfen:

| Prüfachse | Vergleich / Evidence |
| --- | --- |
| Character Identity | gegen kanonische Character-/Referenzquelle |
| Voice Identity | gegen kanonischen Voice Master |
| Lip-Sync | bewegte Performance gegen tatsächlich verwendete Final-Audiospur |
| Blocking | Blick, Gesten und freie Grafikräume gegen Storyboard/Beat-Plan |
| Motion / Composition | Playback-/Render-Evidence |
| Captions | Textinhalt und zeitliche Synchronität |
| Brand / Produktdarstellung | gegen freigegebene Brand-/Produktquelle |

Ein guter Character-Frame beweist weder Voice-Treue noch Lip-Sync. Eine korrekte Stimme beweist weder Blocking noch Composition.

```text
Identity PASS
Voice FAIL
Lip-Sync PASS
Composition PASS

≠ Gesamt-PASS
```

Der Gesamtstatus bleibt eingeschränkt, solange eine für den Auftrag relevante Achse nicht bestanden oder nicht geprüft wurde.

## 8. Audio ist eine eigene Qualitätsschicht

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

## 9. Typische Produktionsmodi

Die folgenden Modi sind Routinghilfen, keine verpflichtenden Produktkategorien:

### Kurze Motion Graphic

Motion selbst trägt die Aussage: kinetische Typografie, Stat-/Chart-Hit, Logo-Sting, Callout oder kurzer Social-Overlay-Baustein.

### Talking-Head-/Footage-Repackage

Bestehendes Footage bleibt zentrale Quelle; Schnitt, Captions, Layoutwechsel, Overlays und unterstützende Grafiken erhöhen Verständlichkeit oder Aufmerksamkeit.

### Produkt-/Software-Promo

Produktwirkung wird über reale UI-/Brand-/Produktquellen sichtbar gemacht. Besonders bei immateriellen Produkten kann Motion die Nutzung oder Wirkung zeigen statt ein erfundenes physisches Objekt zu inszenieren.

### Explainer / Schulung

Fachliche Aussage und visuelle Erklärung werden gemeinsam geplant. Quellenqualität, Verständlichkeit und Claim-Visual-Mapping sind wichtiger als Effektmenge.

## 10. Human Gates und Außenwirkung

Mindestens getrennt behandeln:

- Draft/Preview erzeugen;
- finalen aufwendigen Render erzeugen, wenn Kosten oder Laufzeit relevant sind;
- veröffentlichen oder extern versenden.

Ein technisch bestandener Render ist keine Veröffentlichungsfreigabe.

Bei Werbe-, Schulungs- oder öffentlich sichtbaren Inhalten zusätzlich Claims, Rechte, Branding und sensible Informationen vor Veröffentlichung prüfen.

## 11. Frameworkneutralität

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
