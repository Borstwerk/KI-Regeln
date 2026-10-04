# Workflow: Codebasierte Motion Graphics und Video

## Zweck

Dieser Workflow führt von einem Video-/Motion-Brief zu einer überprüfbaren codebasierten Komposition und einem kontrollierten Render.

Er ist frameworkneutral. HyperFrames, Remotion oder eine projektspezifische Browser-/Rendering-Pipeline können konkrete Laufzeiten sein, wenn deren Fähigkeiten und Dependencies im Projekt belegt sind.

## Verwenden wenn

- ein Motion-Graphic-, Social-, Produkt-, Software- oder Erklärvideo als codebasierte Komposition entstehen soll;
- bestehendes Footage mit programmatisch erzeugten Grafiken, Captions oder Layouts kombiniert werden soll;
- gezielte spätere Änderungen und reproduzierbare Varianten wichtig sind.

Nicht automatisch verwenden, wenn der Nutzer ausdrücklich nur ein generatives Videomodell oder klassischen manuellen Schnitt möchte.

## Ablauf

```text
Brief + Quellen
→ Asset-/Rechteplan
→ Canonical-Media-Contract
→ Script / Storyboard / Beats + Blocking
→ visuelle Richtung + Motion-Logik
→ Performance-/Derived-Media bei Bedarf erzeugen
→ Composition implementieren
→ statische Proof-Frames prüfen
→ Identity / Voice / Lip-Sync / Playback / Audio getrennt prüfen
→ korrigieren
→ finalen Render freigeben
→ Artefakt + Provenienz + offene Risiken übergeben
```

## 1. Brief und lokale Wahrheit

Festhalten:

- Zweck und Audience;
- Format, Seitenverhältnis, Dauer;
- Narration / Captions / On-Screen-Text;
- Brand-/Designquellen;
- Fakten-/Produktquellen;
- vorhandene Medien;
- gewünschte Runtime, wenn vorgegeben;
- Render-/Publikationsziel.

Keine unbekannten Produktfeatures, Preise, Kennzahlen, Testimonials oder Sicherheits-/Fachclaims erfinden.

## 2. Research und Assets

Bei faktischen Claims nach Bedarf mit `web-search`, `source-evaluation`, `claim-verification` oder `deep-research` komponieren.

Bei Marken-/Produktmaterial:

- offizielle oder vom Nutzer freigegebene Quellen priorisieren;
- Asset-Herkunft und Rechte sichtbar halten;
- keine offiziellen Screenshots/Logos plausibel erfinden.

Bei relevanter Provenienzprüfung `inhaltsprovenienz-review` ergänzen.

## 3. Canonical-Media-Contract

Vor generativen Zwischenstufen definieren, welche Quellen für welche Eigenschaften kanonisch bleiben.

Mögliche Rollen:

- `character-identity`;
- `voice-master`;
- `approved-script`;
- `brand-asset`;
- `product-ui`;
- `factual-claim-source`.

Für jede relevante Rolle dokumentieren:

- konkrete Datei/Version/Referenz;
- erlaubte Transformationen;
- zu erhaltende Eigenschaften;
- spätere Rückprüfung;
- ob die kanonische Quelle im Final erneut gebunden werden muss.

Generierte Zwischenartefakte werden als **derived** markiert. Sie dürfen eine kanonische Quelle nicht allein aufgrund ihrer Position in der Pipeline ersetzen.

Beispiel:

```text
voice-master.wav
→ Performance-Generator für Lippenbewegung / Gestik
→ derived-performance.mp4
→ finaler Composite verwendet Video aus derived-performance.mp4
  + bindet voice-master.wav erneut als Final-Voice
→ Lip-Sync gegen genau diese Finalkombination prüfen
```

Nur anwenden, wenn die konkrete Runtime/Toolkette diese Trennung unterstützt.

## 4. Script, Storyboard und Blocking

Das Narrativ in Beats oder Szenen zerlegen.

Für jeden Beat festhalten:

- Claim / Aussage;
- gesprochen oder eingeblendet;
- sichtbare Belege / UI / Grafik;
- gewünschte Bewegung;
- benötigte Assets;
- ungefährer Zeitbereich.

Bei Avatar-/Character-Performance zusätzlich:

- Blickrichtung;
- Zeige-/Greifrichtung;
- reservierte Overlay-/Grafikflächen;
- Schutzbereiche für Gesicht, Hände und wichtige Produktelemente;
- gewünschte Interaktion mit späteren Einblendungen.

Visuals und Narration müssen semantisch zusammenpassen. Blocking-Anweisungen sind Planungs- und Prüfkriterien, keine Garantie, dass ein generatives Modell sie exakt erfüllt.

## 5. Design und Motion

Lokale Brand- und Designquellen schlagen generische Modellästhetik.

Bei Bedarf:

- `frontend-design` für visuelle Richtung;
- `motion-design` nur soweit dessen Motion-Contract für die browserbasierte Komposition fachlich passt.

Tool- oder Frameworkwahl aus Projektanforderungen ableiten, nicht aus persönlicher Vorliebe.

## 6. Implementierung

Runtime-Vertrag zuerst prüfen:

- seekbares Timing;
- Medienkontrolle;
- Renderpfad;
- benötigte Browser-/Runtime-/Codec-/Font-Abhängigkeiten;
- deterministische Bedingungen, falls Reproduzierbarkeit behauptet wird.

`motion-implementation` kann für die konkrete browserbasierte Animationsmechanik komponiert werden. Der Skill übernimmt dadurch **nicht** automatisch Script, Asset-Sourcing, Audio, Claim-Recherche oder Gesamtvideoproduktion.

Änderungen lokal halten und bereits freigegebene Bereiche nicht unnötig neu bauen.

## 7. Verifikation

Mindestens zwei Prüfschichten und bei hybriden Character-/Voice-Pipelines zusätzliche Identitätsachsen:

### A. Frame-/Snapshot-Prüfung

Geeignet für:

- Layout;
- Typografie;
- Crop;
- Brandkonsistenz;
- sichtbare Quellen/Assets;
- Schlüsselzustände.

### B. Playback-/Render-Prüfung

Erforderlich für Aussagen zu:

- Timing;
- Schnitten;
- Bewegungsfluss;
- Caption-/Voice-Sync;
- Musik/SFX;
- Flicker/temporalen Artefakten;
- tatsächlicher Gesamtdauer.

Bei Motion-Craft `motion-review` verwenden. Browser-/Renderzustände können mit `visual-verification` geprüft werden, soweit die Runtime zugänglich ist.

Ein Kontaktbogen allein darf keinen vollständigen Video-Pass begründen.

### C. Canonical-/Derived-Media-Prüfung

Wenn kanonische Quellen und generierte Zwischenartefakte beteiligt sind, relevante Achsen separat bewerten:

- Character Identity gegen `character-identity`;
- Voice Identity gegen `voice-master`;
- Lip-Sync gegen die **tatsächlich im Final verwendete** Audiospur;
- Blocking gegen Storyboard und reservierte Grafikräume;
- Brand-/Produktdarstellung gegen freigegebene Quellen.

Ein Derived Performance Clip darf als Video-`PASS` weiterverwendet werden, obwohl seine erzeugte Audiospur verworfen wird. Umgekehrt darf ein passender Voice Master keinen fehlerhaften Character- oder Lip-Sync-Zustand verdecken.

Kein zusammenfassender `PASS`, wenn eine relevante Achse `FAIL`, `NOT RUN` oder `UNVERIFIED` ist.

## 8. Korrekturschleife

```text
Fund
→ betroffenen Beat / Layer / Zeitbereich lokalisieren
→ kleinste wirksame Änderung
→ relevante Checks erneut ausführen
→ Frame + Playback erneut prüfen
```

Keine Dauer, Auflösung oder Qualitätsstufe nur deshalb reduzieren, um einen sichtbaren Fehler zu verstecken.

## 9. Render- und Veröffentlichungsgate

Wenn der finale Render erhebliche Laufzeit, Credits oder externe Kosten verursacht, Preview beziehungsweise Draft vor dem finalen Render bestätigen lassen.

Veröffentlichung, Upload, Kampagnenstart oder externe Weitergabe bleiben separate Außenaktionen und benötigen vorhandene Autorisierung.

## Handoff

Mindestens liefern:

- Quell-/Projektpfad;
- Runtime/Version soweit relevant;
- finaler Renderpfad und tatsächliche Dauer;
- verwendete Quellen/Assets und Provenienz;
- Canonical-/Derived-Media-Rollen, soweit relevant;
- ausgeführte statische und bewegte Verifikation;
- getrennte Identity-/Voice-/Lip-Sync-/Blocking-Statuswerte, soweit relevant;
- bekannte Abweichungen;
- nicht ausgeführte Checks;
- Veröffentlichungsstatus.

## Leitgedanke

> Erst eine überprüfbare Composition bauen, dann rendern – nicht einen hübschen Render mit unbekannter Herkunft nachträglich erklären.
