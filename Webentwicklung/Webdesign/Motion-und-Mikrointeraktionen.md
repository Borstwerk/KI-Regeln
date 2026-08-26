# Motion und Mikrointeraktionen

## Zweck

Motion ist eine Interaktions- und Orientierungsebene einer Weboberfläche. Bewegung soll Zustandsänderungen verständlicher machen, räumliche Beziehungen erklären, Feedback geben oder bewusst Aufmerksamkeit führen. Sie ist kein Selbstzweck und kein Pflichtmerkmal eines hochwertigen Designs.

Eine gute Entscheidung kann deshalb auch **keine Animation** sein.

## 1. Produktkontext vor Bewegung

Bevor Motion gestaltet wird, kläre:

- Welche Aufgabe erledigt der Nutzer?
- Wie häufig tritt die Interaktion auf?
- Muss eine Zustandsänderung erklärt oder nur bestätigt werden?
- Welche Marken-, Produkt- oder Plattformregeln gelten?
- Welche Eingaben sind relevant: Maus, Touch, Tastatur, Scroll, Sensorik?
- Welche Accessibility- und Performancegrenzen existieren?

Eine seltene, erklärungsbedürftige Zustandsänderung darf anders behandelt werden als ein hochfrequenter Bedienvorgang. Je häufiger eine Interaktion wiederholt wird, desto kritischer ist unnötige Verzögerung oder visuelle Dominanz.

## 2. Designparameter statt Vibe-Wörter

Unscharfe Anforderungen wie „ruhig, hochwertig, aber nicht steril“ können durch wenige explizite Parameter operationalisiert werden. Nützliche lokale Achsen sind beispielsweise:

- **visuelle Varianz** – wie stark sich Formen, Rhythmus und Komposition voneinander unterscheiden;
- **Bewegungsintensität** – wie präsent, großräumig oder häufig Motion auftreten darf;
- **Informationsdichte** – wie kompakt oder luftig Inhalte und Interaktionen organisiert sind.

Diese Parameter ersetzen kein Designsystem und keine Art Direction. Es gibt keine verpflichtende Zahlenskala oder universelle Defaultwerte. Projekt-, Brand- und Produktvorgaben haben Vorrang.

## 3. Zweck und Frequenz

Für jede relevante Animation sollte ein Zweck benennbar sein, zum Beispiel:

- Ursache und Wirkung einer Aktion sichtbar machen;
- Ursprung und Ziel eines Elements räumlich verbinden;
- Status oder Abschluss bestätigen;
- Hierarchie oder Fokuswechsel erklären;
- kontinuierliche Eingabe wie Drag oder Scroll nachvollziehbar abbilden.

Wenn der Zweck nicht benennbar ist, ist Weglassen eine ernsthafte Option.

Häufig wiederholte Interaktionen benötigen besonders zurückhaltende Motion. Eine Animation, die beim ersten Mal charmant ist, kann beim fünfzigsten Mal Reibung erzeugen.

## 4. Timing und Easing

Timing und Easing werden aus Interaktionsart, Distanz, Größe, Frequenz, Unterbrechbarkeit und Produktcharakter abgeleitet. Es gibt keine universelle Millisekundenzahl und keine eine richtige Easing-Kurve für alle Interfaces.

Prüffragen:

- Reagiert das Interface unmittelbar genug auf die Eingabe?
- Wird das Ende der Bewegung verständlich und kontrolliert erreicht?
- Wirkt eine häufige Interaktion durch Motion langsamer als nötig?
- Passt die Beschleunigung zur räumlichen und semantischen Veränderung?
- Ist ein Spring tatsächlich hilfreich oder nur dekorativ?

Konkrete Werte sind Hypothesen und werden im realen Kontext geprüft.

## 5. Spatial Continuity und Choreographie

Motion kann Beziehungen zwischen Zuständen erklären. Dafür sollten Quelle, Ziel, Richtung und Reihenfolge plausibel bleiben.

- Ein Element, das aus einem konkreten Trigger hervorgeht, sollte seinen Ursprung nicht willkürlich verleugnen.
- Gleichzeitige Veränderungen brauchen eine erkennbare Priorität.
- Staggering ist nur sinnvoll, wenn Reihenfolge oder Gruppierung dadurch verständlicher werden.
- Große Seitenbewegungen benötigen einen stärkeren Zweck als kleine lokale Rückmeldungen.
- Shared-Element- oder View-Transitions sind Mittel für Kontinuität, nicht automatisch ein Qualitätsmerkmal.

## 6. Interruptibility

Interaktive Motion muss mit realem Nutzerverhalten umgehen können.

Prüfe insbesondere:

- Was passiert bei erneutem Klick oder Tap während der Bewegung?
- Kann ein Drag jederzeit Richtungswechsel und Loslassen verarbeiten?
- Kann Navigation oder Zustand wechseln, ohne auf dekorative Motion warten zu müssen?
- Springt das UI bei Unterbrechung in einen unplausiblen Zwischenzustand?
- Bleiben Fokus, Eingabe und semantischer Zustand korrekt?

Eine Animation darf die Interaktion nicht zu einer ununterbrechbaren Vorführung machen.

## 7. Gesten, Touch und kontinuierliche Eingabe

Bei Drag-, Swipe-, Pinch- oder Scroll-Interaktionen folgt Motion einer kontinuierlichen Eingabe statt nur einem Start-/Endzustand.

Dabei sind mindestens zu prüfen:

- direkte Rückkopplung zwischen Eingabe und visueller Reaktion;
- Grenzen, Constraints und Rückkehrverhalten;
- Velocity nur dort, wo sie semantisch sinnvoll ist;
- Touch- und Pointer-Verhalten getrennt betrachten;
- Fokus- und Tastaturpfade nicht durch pointerzentrierte Motion beschädigen;
- Abbruch- und Unterbrechungspfade.

## 8. Reduced Motion und Accessibility

`prefers-reduced-motion` signalisiert eine Präferenz, nicht essenzielle Bewegung zu minimieren. Die passende Antwort kann Motion **entfernen, reduzieren oder ersetzen**. Eine pauschale `0ms`-Regel ist deshalb zu grob.

Ziel ist, Zweck und Informationsgehalt zu erhalten, ohne unnötige oder vestibulär problematische Bewegung zu erzwingen.

Besonders kritisch sind:

- großflächiges Panning, Zooming oder Parallax;
- starke Skalierung großer Elemente;
- dauerhaft wiederholte oder schwer stoppbare Animationen;
- Information, die ausschließlich durch Bewegung vermittelt wird;
- Motion, die Fokus, Tastaturbedienung oder Touch-Ziele beeinträchtigt.

Reduced-Motion-Zustände müssen bei relevanten Interaktionen tatsächlich geprüft werden.

Primärquelle: MDN – [`prefers-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion).

## 9. Technische Werkzeugwahl

Die technische Umsetzung folgt einer bereits begründeten Motion-Absicht. Es gibt kein starres Toolranking.

Mögliche Werkzeugklassen sind unter anderem:

- CSS Transitions und CSS Animations für deklarative Zustandswechsel;
- `@starting-style` für unterstützte Eintritts-/Initialzustände;
- Web Animations API (WAAPI), wenn JavaScript Playback, Timing oder Laufzeitsteuerung benötigt;
- View Transition API für unterstützte Zustands- oder Navigationsübergänge;
- CSS Scroll-driven Animations für unterstützte scrollgebundene Timelines;
- Motion oder ähnliche Framework-/Library-Abstraktionen für passende Layout-, Gesture- oder Orchestrierungsaufgaben;
- GSAP für Aufgaben, bei denen dessen Timeline-/Scroll-Orchestrierung oder bestehende Projektintegration einen echten Vorteil liefert;
- spezialisierte Asset-/Rendering-Runtimes nur bei entsprechendem Medien- oder Interaktionsmodell.

Die einfachste ausreichende Lösung ist ein guter Ausgangspunkt, aber kein Dogma. Projektstack, Browserziele, vorhandene Dependencies, Wartbarkeit, Accessibility und gemessene Laufzeitkosten gehören in die Entscheidung.

Primärquellen:

- MDN – [Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API)
- MDN – [`@starting-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40starting-style)
- MDN – [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
- MDN – [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
- Motion – [Layout animations](https://motion.dev/docs/react-layout-animations)
- GSAP – [Timeline](https://gsap.com/docs/v3/GSAP/Timeline/) und [ScrollTrigger](https://gsap.com/docs/v3/Plugins/ScrollTrigger/)

Browserunterstützung und API-Status sind zeitabhängig und müssen vor einer produktiven Festlegung gegen aktuelle Primärdokumentation geprüft werden.

## 10. Performance ohne Mythen

Keine der folgenden Kurzformeln ist eine universelle Wahrheit:

- GPU = schnell;
- `transform` = kostenlos;
- `filter` = billig;
- `will-change` vorsorglich überall;
- CSS = immer schneller;
- JavaScript = langsam;
- GSAP = immer besser;
- Motion = immer kleiner oder besser als GSAP.

Performance hängt unter anderem von Layout, Paint, Composite, Layer-Anzahl und -Speicher, Main-Thread-Arbeit, Scrollpfad, Anzahl animierter Elemente, DOM-Größe, Hardware und Browser ab.

Deshalb:

1. Problem und Zielzustand festhalten.
2. Auf realistischen Geräten und Viewports reproduzieren.
3. Browser-Profiler oder gleichwertige Messung verwenden.
4. Ursache von bloßer Korrelation trennen.
5. Erst dann eine technische Optimierung als wirksam bezeichnen.

Ohne Render- oder Profiler-Evidence bleibt eine Performanceaussage Hypothese.

## 11. Evidence-Gates

Für Designentscheidungen kann ein begründeter Motion-Contract ohne Browser genügen. Für Aussagen über das **reale Verhalten** gelten stärkere Gates:

- visuelle Qualität → Render, Video oder reproduzierbare Browser-Evidence;
- Interruptibility → ausgeführte Interaktion;
- Reduced Motion → ausgeführter Alternativzustand;
- Performance → Messung/Profiler;
- Browserkompatibilität → aktuelle Zielbrowser-/Primärquellenprüfung.

Fehlt notwendige Evidence, wird das Ergebnis `partial` oder der betreffende Claim bleibt offen. Fehlende Evidence darf nicht durch Modellgedächtnis ersetzt werden.

## 12. Zusammenspiel der Skills

- `frontend-design` definiert die allgemeine visuelle Richtung.
- `motion-design` definiert Zweck und Verhalten der Motion.
- `motion-implementation` setzt eine definierte Motion technisch um.
- `motion-review` prüft vorhandene Motion unabhängig.
- `accessibility-review` prüft die gesamte Accessibility eines Interfaces.
- `frontend-performance` diagnostiziert allgemeine Frontendperformance messungsbasiert.
- `visual-verification` liefert bei Bedarf Render-/Viewport-Evidence.

Motion-Kompetenz ergänzt diese Skills; sie ersetzt sie nicht.
