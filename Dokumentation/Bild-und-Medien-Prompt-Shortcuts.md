# Bild- und Medien-Prompt-Shortcuts

Stand: 2026-10-05

## Zweck

Diese Seite sammelt **220 kompakte Prompt-Shortcuts** für Bildgenerierung, Bildbearbeitung, Marken-/Social-Visuals und toolabhängige Videoideen.

Alle Einträge sind:

```text
PROMPT-SHORTCUT
```

und **keine behaupteten eingebauten ChatGPT-Produktbefehle**.

Die Kürzel beschreiben eine gewünschte Bild-/Medienoperation. Ob sie direkt ausgeführt werden kann, hängt von der jeweils verfügbaren Bild-, Video-, Plugin- oder Connector-Runtime ab.

## Herkunft und Übernahmegrenze

Methodische Ausgangsreferenz war die vom Nutzer bereitgestellte statische PDF:

> Christian · @KI.GLATZE · „220 Bild-Codes für ChatGPT“ · Ausgabe 2026

Die PDF selbst wird **nicht** in diesem Repository redistribuiert.

Für KI-Regeln wurden:

- die funktionalen Kurzlabels als Prompt-Sprache ausgewertet;
- Beschreibungen, Gruppierung, Qualitätsregeln und Schutzplanken eigenständig formuliert;
- keine längeren Originaltexte, Seitengestaltung oder PDF-Abbildungen übernommen;
- keine freie Lizenz der Ausgangs-PDF unterstellt.

Die Quelle selbst weist darauf hin, dass die Codes keine offiziellen OpenAI-Befehle sind. Diese Grenze wird hier beibehalten.

## Inhalt

- Erklären, zerlegen und transformieren
- Porträts und Personen
- Produktfotografie und Produktdarstellung
- Werbung und Anzeigen
- Logo, Marke und visuelles System
- Mockups, Verpackung und Präsentation
- Social Media und Content-Visuals
- Bildbearbeitung und technische Varianten
- Stil und Look
- Video und Bewegung – toolabhängig

## Verwendung

Grundform:

```text
/<shortcut> + Motiv/Referenz + gewünschter Zweck + wichtige Grenzen
```

Beispiel:

```text
/productshot
diese bereitgestellte Kaffeepackung,
ruhiges Studio-Keyvisual,
Markenfarben und Etikett exakt erhalten
```

Ein einzelnes Kürzel ersetzt keinen guten Brief. Je wichtiger Identität, Text, Maße, Claims, Branding oder Kontinuität sind, desto mehr Kontext muss mitgegeben werden.

## Shortcuts stapeln

Mehrere Kürzel können als **Arbeitskette** verstanden werden, nicht als magische Ein-Wort-Pipeline.

Beispiel:

```text
/productshot
→ /colorways
→ /staticad
→ /productreel
```

Zwischen den Schritten gilt jeweils:

- Keeper/Source of Truth festhalten;
- ungewollte Änderungen erkennen;
- Text, Marke, Produktform und Claims erneut prüfen;
- nur den nächsten notwendigen Layer verändern.

## Harte Qualitäts- und Rechtegates

### Reale Personen

Bei Bearbeitung realer Personen nur bereitgestellte beziehungsweise autorisierte Bilder verwenden. Identität, Alterseindruck, Kleidung und Umgebung nicht unnötig verändern.

### Marken, Logos und Produkte

Offizielle Logos, Verpackungen oder UI nicht plausibel erfinden, wenn eine echte Quelle benötigt wird. Ein Mockup oder Rebrand darf keine offizielle Freigabe oder Markeninhaberschaft suggerieren.

### Anzeigen und Claims

Für Anzeigen gelten echte Quelldaten:

- keine erfundenen Testimonials;
- keine erfundenen Preise, Rabatte, Öffnungszeiten oder Fristen;
- Vergleichsaussagen nur mit belastbarer Grundlage;
- Vorher/Nachher nicht irreführend verstärken;
- Native-Style-Werbung darf erforderliche Kennzeichnung nicht umgehen.

### Text im Bild

Generierter Bildtext ist fehleranfällig. Namen, Preise, Daten, Maße, Adressen und rechtlich relevante Texte nach dem Render separat prüfen.

### Technische Dokumentdarstellungen

`/passport`, `/sizechart`, `/blueprint` oder ähnliche Kürzel erzeugen eine visuelle Darstellung. Sie beweisen keine amtliche, technische oder normative Konformität.

### Entfernen von Text oder Watermarks

`/removetext` ist für eigene beziehungsweise autorisierte Bildbearbeitung gedacht. Fremde Watermarks, Herkunftsmarker oder Kennzeichnungen nicht zur Rechte-, Attribution- oder Provenienzumgehung entfernen.

### Video

Die Video-Shortcuts sind **runtimeabhängig**. Die Ausgangsreferenz nennt Higgsfield als konkrete Option; KI-Regeln macht daraus **keine universelle Toolpflicht**. Ohne passende Video-Capability bleibt der Shortcut ein Briefing beziehungsweise `UNVERIFIED`.

Bei Avatar-/Voice-/Motion-Pipelines zusätzlich die Regeln zu Canonical Media, Lip-Sync, Playback-Evidence und Veröffentlichungsgates beachten.

## Erklären, zerlegen und transformieren

| Shortcut | Zweck / KI-Regeln-Lesart |
|---|---|
| `/explodedview` | Objekt als auseinandergezogene Komponentenansicht mit klarer Teileordnung. |
| `/cutaway` | Schnittdarstellung, die relevante Innenbereiche oder Schichten sichtbar macht. |
| `/lego` | Quelle-Alias für eine Klemmbaustein-Interpretation; in Prompts möglichst neutral als Baustein-Set beschreiben. |
| `/timemachine` | Motiv glaubwürdig in eine gewählte historische Fotoepoche übertragen. |
| `/hologram` | Motiv als leuchtende futuristische Projektionsdarstellung inszenieren. |
| `/headshot` | Aus einem geeigneten Porträt eine professionelle Headshot-Komposition ableiten. |
| `/productexplosion` | Produktteile als räumlich getrennte Komponentenvisualisierung darstellen. |
| `/adcreative` | Produkt oder Angebot als vollständiges Werbemotiv mit klarer visueller Hierarchie gestalten. |
| `/ugc` | UGC-artige Videodarstellung eines Produkts; synthetische Darstellung nicht als echte Kundenstimme ausgeben. |
| `/productspin` | Produkt als 360-Grad-orientierte Videosequenz beziehungsweise Drehdarstellung planen. |
| `/animated` | Vorhandenes Produktmotiv in eine kurze bewegte Werbeinszenierung überführen. |

## Porträts und Personen

| Shortcut | Zweck / KI-Regeln-Lesart |
|---|---|
| `/portrait` | Klassisches Porträt mit kontrollierter Licht- und Hintergrundgestaltung. |
| `/corporate` | Sachliches Unternehmensporträt mit professioneller, zurückhaltender Wirkung. |
| `/linkedin` | Profilbild-Komposition für berufliche Netzwerke mit engem, klar lesbarem Zuschnitt. |
| `/teamphoto` | Mehrere Personen in einer visuell konsistenten Teamdarstellung zusammenführen. |
| `/outdoorportrait` | Porträt im Außenraum mit natürlicher Lichtstimmung. |
| `/blackwhite` | Porträt in bewusst gestalteter Schwarzweiß-Tonalität. |
| `/glasses` | Brille ergänzen oder erhalten und störende Spiegelungen kontrollieren. |
| `/suit` | Kleidung in Richtung formeller Business-Look verändern, ohne Identität unnötig umzubauen. |
| `/smilefix` | Gesichtsausdruck dezent natürlicher gestalten, Identitätsmerkmale erhalten. |
| `/retouch` | Zurückhaltende Retusche ohne plastikartige Haut oder Identitätsdrift. |
| `/oldphoto` | Gealtertes Foto restaurieren: Schäden, Flecken und Kontrastverluste behutsam korrigieren. |
| `/colorize` | Schwarzweißaufnahme plausibel kolorieren; historische Farbtreue nur mit belastbarer Referenz behaupten. |
| `/passport` | Passbildartige, frontale Aufnahme erzeugen; keine behördliche oder biometrische Konformität garantieren. |
| `/cutout` | Person sauber vom Hintergrund trennen. |
| `/newbackground` | Hintergrund ersetzen und Licht, Perspektive sowie Farbstimmung anpassen. |
| `/twopeople` | Zwei bereitgestellte Personenreferenzen in einer gemeinsamen Szene komponieren. |
| `/agefix` | Alterseindruck vorsichtig verändern, ohne Identität oder Proportionen unnötig zu verfälschen. |
| `/actionshot` | Person in einer dynamischen Bewegungsszene inszenieren. |
| `/speaker` | Person als Vortragende auf einer Bühne oder in einer Präsentationssituation zeigen. |
| `/officescene` | Person glaubwürdig in einer Büroumgebung bei einer Arbeitssituation darstellen. |
| `/avatarset` | Mehrere Profilvarianten derselben Person mit kontrollierter Identitätskonsistenz erzeugen. |
| `/founder` | Gründer- oder Presseporträt mit seriöser, markengerechter Wirkung gestalten. |
| `/podcastshot` | Person in einer Podcast-/Studio-Situation mit Mikrofon und passender Lichtstimmung zeigen. |
| `/casual` | Porträt bewusst informeller, nahbarer und alltagsnäher gestalten. |
| `/thumbnailface` | Gesicht beziehungsweise Person für ein Thumbnail klar freistellen und plakativ komponieren. |

## Produktfotografie und Produktdarstellung

| Shortcut | Zweck / KI-Regeln-Lesart |
|---|---|
| `/productshot` | Sauberes, kontrolliertes Produktmotiv mit neutraler oder definierter Studioanmutung. |
| `/lifestyle` | Produkt in einer glaubwürdigen Nutzungssituation zeigen. |
| `/flatlay` | Produkt und Zubehör als geordnete Draufsicht arrangieren. |
| `/closeup` | Material, Oberfläche oder relevantes Detail als Nahaufnahme hervorheben. |
| `/colorways` | Dasselbe Produkt in mehreren kontrollierten Farbvarianten zeigen. |
| `/scale` | Größe des Produkts durch nachvollziehbaren Referenzvergleich vermitteln. |
| `/hero` | Hochwertiges zentrales Produkt-Keyvisual für Hero- oder Titelbereich entwickeln. |
| `/bundle` | Mehrere Produkte als zusammengehöriges Set inszenieren. |
| `/packshot` | Produkt und zugehörige Verpackung konsistent nebeneinander darstellen. |
| `/ingredients` | Produkt mit realen, belegten Zutaten oder Bestandteilen visuell kontextualisieren. |
| `/beforeafter` | Vorher-/Nachher-Darstellung; Unterschiede nicht erfinden oder irreführend übertreiben. |
| `/onwhite` | Produkt sauber vor hellem neutralem Hintergrund für Katalog-/Shopkontext darstellen. |
| `/shadowplay` | Produkt über gerichtete Schatten und Lichtmuster inszenieren. |
| `/waterdrops` | Feuchtigkeit, Kondenswasser oder Tropfen als Frische-/Kältewirkung einsetzen. |
| `/floating` | Produkt scheinbar schwebend mit plausibler Licht- und Schattenlogik darstellen. |
| `/inhand` | Produkt in einer Hand zeigen und dabei Maßstab sowie Griff glaubwürdig halten. |
| `/tabletop` | Produkt auf einer Tischfläche mit wenigen passenden Requisiten inszenieren. |
| `/marble` | Produkt auf heller stein-/marmorartiger Oberfläche präsentieren. |
| `/wood` | Produkt auf Holz oder in warmer natürlicher Materialumgebung zeigen. |
| `/studio` | Kontrolliertes Studiomotiv mit nachvollziehbarer Lichtsetzung erzeugen. |
| `/outdoorproduct` | Produkt im Außenraum passend zu Nutzung, Wetter und Umgebung inszenieren. |
| `/nightshot` | Produkt als Nachtmotiv mit kontrollierten künstlichen Lichtquellen zeigen. |
| `/exploded` | Technische Produktteile geordnet getrennt beziehungsweise gestapelt visualisieren. |
| `/threeviews` | Produkt aus Vorder-, Seiten- und Rückansicht konsistent in einer Tafel zeigen. |
| `/sizechart` | Maß- oder Größenangaben nur aus bereitgestellten Daten sauber visualisieren. |
| `/matchset` | Mehrere Produktbilder auf gemeinsame Licht-, Farb- und Hintergrundlogik angleichen. |
| `/removebg` | Produkt sauber vom Hintergrund trennen. |
| `/reflection` | Kontrollierte Spiegelung auf geeigneter Oberfläche ergänzen. |
| `/seasonal` | Produkt saisonal kontextualisieren, ohne Marke oder Produktform unnötig zu verändern. |

## Werbung und Anzeigen

| Shortcut | Zweck / KI-Regeln-Lesart |
|---|---|
| `/staticad` | Statisches Werbemotiv mit klarer Botschaft, Produktfokus und CTA-Struktur erstellen. |
| `/carousel` | Mehrteilige Anzeigen- oder Erklärsequenz als zusammenhängendes Karussell planen. |
| `/storyad` | Vertikales Anzeigenmotiv mit ausreichend Raum für UI-Overlays und sichere Textzonen gestalten. |
| `/salepost` | Rabatt- oder Angebotsmotiv nur mit tatsächlich vorgegebenen Preisen, Fristen und Bedingungen erstellen. |
| `/newsletterbild` | Breites E-Mail-/Newsletter-Keyvisual mit lesbarer Komposition für schmale Layouts gestalten. |
| `/comparisonad` | Vergleichsanzeige nur mit belegbaren, fair formulierten Vergleichsaussagen erzeugen. |
| `/testimonialad` | Kundenstimme nur aus echter, freigegebener Aussage verwenden; keine Testimonials erfinden. |
| `/problemsolution` | Problem und Lösung visuell gegenüberstellen, ohne unbelegte Wirkversprechen. |
| `/billboard` | Plakatmotiv mit sehr klarer Fernwirkung und geringer Informationsdichte gestalten. |
| `/menuboard` | Angebots- oder Menütafel aus bereitgestellten Preisen und Bezeichnungen setzen. |
| `/flyer` | Ein- oder zweiseitiges Flyerlayout aus vorhandenen Inhalten strukturieren. |
| `/coupon` | Gutscheinmotiv aus echtem Code, Frist und Bedingungen gestalten. |
| `/eventposter` | Veranstaltungsplakat aus bestätigtem Datum, Ort und Titel erstellen. |
| `/jobad` | Stellenanzeige als Social-/Visual-Motiv mit korrekten Rollen- und Arbeitgeberdaten gestalten. |
| `/pricetable` | Preis- oder Tarifstufen ausschließlich aus verifizierten Daten visualisieren. |
| `/featuregrid` | Mehrere Produktmerkmale als einheitliches Raster mit verständlicher Hierarchie darstellen. |
| `/quotecard` | Echtes Zitat mit sauberer Attribution als typografisches Visual setzen. |
| `/countdown` | Countdown-Motiv auf Basis eines realen Termins oder einer realen Frist gestalten. |
| `/giveaway` | Gewinnspielmotiv mit klar sichtbaren tatsächlichen Teilnahmebedingungen planen. |
| `/openinghours` | Öffnungszeiten nur aus bestätigten Angaben als gut lesbares Visual darstellen. |
| `/mapcard` | Standort- oder Adresskarte aus einer realen, bestätigten Ortsangabe gestalten. |
| `/brandposter` | Markenmotiv ohne Angebotszwang, fokussiert auf Haltung und visuelle Identität. |
| `/nativead` | Native-artige Werbegestaltung; erforderliche Werbekennzeichnung niemals verdecken oder umgehen. |
| `/retargeting` | Folgemotiv für bekannte Zielgruppe mit klarer, nicht irreführender Anschlussbotschaft. |
| `/labelad` | Produktetikett oder Verpackungsdetail als zentrales Werbeelement inszenieren. |

## Logo, Marke und visuelles System

| Shortcut | Zweck / KI-Regeln-Lesart |
|---|---|
| `/logoconcepts` | Mehrere eigenständige Logoideen aus Name, Kontext und gewünschten Eigenschaften entwickeln. |
| `/wordmark` | Reine Wortmarken-Richtung über Typografie und Buchstabenform erkunden. |
| `/monogram` | Initialen oder Kürzel als kompaktes Markenzeichen untersuchen. |
| `/favicon` | Kleines, reduziertes Symbol für sehr geringe Darstellungsgrößen entwickeln. |
| `/logovariants` | Logo in hell, dunkel, monochrom und kleinformatig auf Robustheit prüfen. |
| `/colorpalette` | Kleine, benannte Markenpalette mit nachvollziehbaren Farbwerten ableiten. |
| `/fontpair` | Passendes Schriftpaar nach Funktion, Lesbarkeit und Markenwirkung vorschlagen. |
| `/brandboard` | Logo, Farbe, Typografie und Bildsprache auf einer kompakten Markentafel zusammenführen. |
| `/patternfill` | Wiederholbares Muster aus freigegebenen Markenelementen entwickeln. |
| `/iconset` | Kleine zusammengehörige Symbolfamilie mit konsistenter Strich-/Flächenlogik entwickeln. |
| `/businesscard` | Visitenkartenentwurf mit klarer Informationshierarchie erstellen. |
| `/letterhead` | Briefkopf oder Geschäftspapier aus vorhandener Markenidentität ableiten. |
| `/signage` | Beschilderung für Raum, Laden oder Messe unter realistischen Größen-/Abstandsbedingungen visualisieren. |
| `/vehiclewrap` | Fahrzeugbeschriftung als Mockup planen; reale Fahrzeugform und markenrechtliche Vorgaben berücksichtigen. |
| `/merch` | Freigegebenes Motiv auf typische Merchandise-Flächen übertragen. |
| `/stamp` | Markenzeichen als reduzierte stempelartige Variante testen. |
| `/badge` | Siegel-/Badge-Variante nur mit realen Jahreszahlen, Claims oder Zertifizierungen gestalten. |
| `/emblem` | Emblemartige, kompakte Markenform für traditionelle oder handwerkliche Wirkung entwickeln. |
| `/socialkit` | Profil-, Header- und Social-Basisvisuals aus einem bestehenden Markensystem ableiten. |
| `/rebrand` | Bestehende Marke behutsam modernisieren; wiedererkennbare Kernmerkmale bewusst behandeln. |

## Mockups, Verpackung und Präsentation

| Shortcut | Zweck / KI-Regeln-Lesart |
|---|---|
| `/mockup` | Design oder Produkt in einem realistischen Anwendungskontext präsentieren. |
| `/phonemockup` | UI oder Website auf einem Smartphone-Rahmen beziehungsweise Gerät zeigen. |
| `/laptopmockup` | UI oder Website in einer realistischen Laptop-Szene präsentieren. |
| `/tshirtmockup` | Motiv auf einem getragenen oder ausgelegten Shirt plausibel platzieren. |
| `/mugmockup` | Motiv auf einer Tasse mit korrekter Perspektivverzerrung zeigen. |
| `/bookcover` | Buch-/E-Book-Cover als flache Gestaltung oder Präsentationsmockup entwickeln. |
| `/packagingbox` | Verpackungsdesign auf einer Faltschachtel beziehungsweise Box visualisieren. |
| `/bottlelabel` | Etikett auf Flasche, Dose oder ähnlicher Verpackung perspektivisch korrekt zeigen. |
| `/pouch` | Design auf einem Standbeutel oder flexibler Verpackung präsentieren. |
| `/jar` | Etikett und Gestaltung auf einem Glas-/Dosenbehälter zeigen. |
| `/sticker` | Mehrere Aufklebermotive als Bogen oder Set präsentieren. |
| `/postermockup` | Poster in einer realistischen Wand-/Rahmensituation zeigen. |
| `/billboardmockup` | Plakatgestaltung in einer realistischen Außenwerbefläche visualisieren. |
| `/shelf` | Produkt in einer Regalsituation mit plausibler Konkurrenz-/Umgebungsdichte zeigen. |
| `/unboxing` | Geöffnete Verpackung, Produkt und Zubehör als Unboxing-Szene arrangieren. |
| `/appicon` | App-Symbol in einem Startbildschirm-/UI-Kontext präsentieren. |
| `/screenshotframe` | Screenshot in einen passenden Geräte- oder Browserrahmen setzen. |
| `/businesscardmockup` | Visitenkartenentwurf als physisches Mockup präsentieren. |
| `/menu` | Speisekarten- oder Menülayout aus bereitgestellten Inhalten gestalten. |
| `/tote` | Motiv auf einem Stoffbeutel oder ähnlichem Träger mocken. |

## Social Media und Content-Visuals

| Shortcut | Zweck / KI-Regeln-Lesart |
|---|---|
| `/thumbnail` | Plakatives Vorschaubild mit sehr kurzer, klar lesbarer Titelbotschaft entwickeln. |
| `/reelcover` | Vertikales Reel-/Short-Cover mit sicherer Textposition und starkem ersten Eindruck gestalten. |
| `/quotepost` | Freigegebenes Zitat als gut lesbares Social-Visual setzen. |
| `/carouselcover` | Einstiegsfolie für ein Karussell mit klarer Neugier-/Nutzenbotschaft entwickeln. |
| `/tipgraphic` | Einen einzelnen Tipp als schnell erfassbare Grafik visualisieren. |
| `/stepbystep` | Kurze Anleitung als geordnete Bildfolge beziehungsweise Schritte darstellen. |
| `/checklistcard` | Kompakte Checkliste als scanbares Visual aufbereiten. |
| `/statcard` | Kennzahl nur mit bestätigter Zahl und Quelle als Visual darstellen. |
| `/mythfact` | Mythos und belegten Fakt klar gegenüberstellen. |
| `/memeformat` | Eigenes Meme-Format aus dem Thema entwickeln, ohne fremdes geschütztes Bildmaterial vorauszusetzen. |
| `/faceless` | Social-Visual ohne erkennbare Person, fokussiert auf Grafik, Objekt oder Typografie. |
| `/podcastcover` | Podcast- oder Episoden-Cover mit konsistenter Marken- und Plattformlesbarkeit entwickeln. |
| `/profilbanner` | Breites Profil-/Headerbild für Social-Plattformen gestalten. |
| `/highlightcover` | Kleine, konsistente Cover-Symbole für Story-/Highlight-Sammlungen entwickeln. |
| `/beforeafterpost` | Vorher-/Nachher-Post nur mit realen, nicht irreführend verstärkten Unterschieden erstellen. |
| `/teamintro` | Teammitglied aus freigegebenem Foto, Name und Rolle als Vorstellungsvisual präsentieren. |
| `/eventrecap` | Mehrere reale Eventmomente als konsistente Rückblick-Collage aufbereiten. |
| `/announcement` | Ankündigungsvisual aus bestätigten Kerninformationen gestalten. |
| `/pollcard` | Einfache Umfragegrafik mit klaren Antwortoptionen entwickeln. |
| `/countdownstory` | Vertikale Countdown-Story auf Basis eines realen Termins gestalten. |
| `/threadcover` | Titelvisual für einen Thread oder längeren Post entwickeln. |
| `/infographic` | Wenige zusammengehörige Punkte als kompakte Infografik strukturieren. |
| `/timeline` | Chronologische Stationen aus bestätigten Daten als Zeitstrahl visualisieren. |
| `/mapinfographic` | Geografische Information nur aus realen Orts-/Kartendaten als Infografik aufbereiten. |
| `/recipecard` | Rezept aus bereitgestellten Zutaten und Schritten als lesbare Karte gestalten. |

## Bildbearbeitung und technische Varianten

| Shortcut | Zweck / KI-Regeln-Lesart |
|---|---|
| `/upscale` | Bildauflösung beziehungsweise Detailwahrnehmung vergrößern, Artefakte anschließend prüfen. |
| `/sharpen` | Schärfeeindruck kontrolliert erhöhen, ohne Halos oder Rauschen unnötig zu verstärken. |
| `/denoise` | Bildrauschen reduzieren und wichtige Texturdetails erhalten. |
| `/relight` | Lichtwirkung und Richtung neu gestalten, Geometrie und Schatten konsistent halten. |
| `/colorgrade` | Farbcharakter und Kontrast auf eine gewünschte Gesamtstimmung angleichen. |
| `/whitebalance` | Ungewollten Farbstich korrigieren beziehungsweise Weißpunkt neutralisieren. |
| `/straighten` | Horizont, vertikale Linien oder Perspektivwirkung korrigieren. |
| `/expand` | Bildfläche durch Outpainting erweitern und Anschlussbereiche konsistent halten. |
| `/cleanup` | Störende kleine Elemente gezielt entfernen, ohne das übrige Bild unnötig neu zu generieren. |
| `/removeperson` | Unerwünschte Person aus dem Hintergrund entfernen und Fläche plausibel rekonstruieren. |
| `/removetext` | Text aus einem eigenen/autorisierten Bild entfernen; fremde Watermarks oder Herkunftsmarker nicht zur Rechteumgehung beseitigen. |
| `/replacesky` | Himmel ersetzen und Beleuchtung/Farbtemperatur der Szene entsprechend angleichen. |
| `/blurbg` | Hintergrund kontrolliert unscharf setzen, Motivkanten sauber halten. |
| `/bokeh` | Plausible unscharfe Lichtpunkte als Hintergrundwirkung ergänzen. |
| `/grain` | Dezente Filmkornstruktur hinzufügen, ohne Details unnötig zu zerstören. |
| `/crop45` | Auf 4:5 formatieren und Motiv/Hauptinformation sinnvoll neu ausrichten. |
| `/squarefit` | Quadratische Ausgabe ohne wichtigen Inhaltsverlust herstellen, fehlende Fläche kontrolliert ergänzen. |
| `/transparent` | Motiv mit transparentem Hintergrund ausgeben, sofern Format/Runtime dies unterstützt. |
| `/vector` | Motiv in vereinfachte flächige Grafiklogik überführen; kein echtes editierbares Vektorformat garantieren, wenn nur Rasteroutput entsteht. |
| `/linework` | Motiv auf klare Kontur-/Strichdarstellung reduzieren. |
| `/duotone` | Bild auf zwei dominierende Farbtöne beziehungsweise Markenfarben reduzieren. |
| `/hdr` | Schatten-/Lichterumfang ausgleichen, ohne unnatürliche HDR-Artefakte zu erzwingen. |
| `/mirror` | Motiv spiegeln oder bewusst symmetrisch komponieren. |
| `/collage` | Mehrere Bilder in einem klaren Raster oder einer gemeinsamen Komposition zusammenführen. |
| `/watermark` | Eigenes Logo oder freigegebenes Kennzeichen dezent als Herkunfts-/Brandingelement ergänzen. |

## Stil und Look

| Shortcut | Zweck / KI-Regeln-Lesart |
|---|---|
| `/photoreal` | Fotorealistische Material-, Licht- und Kamerawirkung anstreben. |
| `/cinematic` | Filmische Bildsprache über Licht, Kontrast, Perspektive und Farbdramaturgie entwickeln. |
| `/minimal` | Reduzierte Gestaltung mit viel Negativraum und wenigen dominanten Elementen. |
| `/luxury` | Zurückhaltende Premium-Anmutung mit kontrollierter Materialität und Farbpalette. |
| `/scandi` | Helle, ruhige, funktionale nordisch inspirierte Gestaltung mit natürlichen Materialien. |
| `/vintage` | Bewusst ältere fotografische oder grafische Anmutung mit passender Material-/Farbwirkung. |
| `/y2k` | Früh-2000er-inspirierte digitale, typografische oder glänzende Gestaltung. |
| `/neon` | Nacht-/Neonwirkung mit leuchtenden Akzentfarben und dunkler Umgebung. |
| `/pastel` | Weiche, helle Pastellpalette mit geringer visueller Härte. |
| `/monochrome` | Gestaltung überwiegend innerhalb einer Farbfamilie. |
| `/isometric` | Isometrische räumliche Darstellung mit konsistentem Winkelraster. |
| `/3drender` | Saubere 3D-Render-Anmutung mit kontrollierter Material- und Lichtwirkung. |
| `/claymation` | Knetanimationsartige Material- und Figurenwirkung; als Stilbeschreibung, nicht als Behauptung eines bestimmten Studios. |
| `/papercut` | Mehrlagige Papier-/Scherenschnittoptik mit sichtbarer Ebenenwirkung. |
| `/watercolor` | Aquarellartige Farbflächen, Übergänge und Papierwirkung. |
| `/sketch` | Skizzenhafte Bleistift-/Zeichenwirkung mit sichtbarer Linienarbeit. |
| `/blueprint` | Technische Blaupausen-/Konstruktionszeichnung mit schematischer Linienlogik. |
| `/comic` | Allgemeine Comicdarstellung mit klarer Linien-/Flächenhierarchie; keine konkrete lebende Künstlerhandschrift imitieren. |
| `/pixelart` | Rasterbasierte Pixelästhetik mit bewusst begrenzter Auflösung/Farbpalette. |
| `/analogfilm` | Analoge Fotoanmutung mit passender Tonkurve, Körnung und Farbwiedergabe. |

## Video und Bewegung – toolabhängig

| Shortcut | Zweck / KI-Regeln-Lesart |
|---|---|
| `/productreel` | Kurzen Produktclip aus vorhandenem Produktmaterial planen oder erzeugen. |
| `/ugcreview` | UGC-artige Produktbesprechung; synthetische Sprecher nicht als echte Kunden ausgeben. |
| `/unboxingvideo` | Öffnungs-/Auspacksequenz mit Produkt und Verpackung als Video konzipieren. |
| `/tryon` | Produkt wie Kleidung oder Brille als Anprobe-/Try-on-Szene darstellen; Identität und Produktform prüfen. |
| `/beforeafterclip` | Vorher-/Nachher-Zustand als Übergangsclip zeigen; Unterschiede müssen real beziehungsweise klar als Simulation kenntlich sein. |
| `/zoomin` | Langsame Kamerafahrt beziehungsweise Bewegung auf das Motiv zu. |
| `/orbit` | Kamera oder Ansicht kontrolliert um das Objekt führen. |
| `/flythrough` | Räumliche Kamerafahrt durch eine Szene oder Umgebung planen. |
| `/textreveal` | Text zeitlich kontrolliert ein- und ausblenden. |
| `/logosting` | Kurze Logo-/Markenanimation als Intro, Outro oder Trenner erstellen. |
| `/loopclip` | Nahtlos wiederholbaren Kurzclip mit passender End-/Startkontinuität erzeugen. |
| `/slowmotion` | Bewegung als verlangsamte Sequenz inszenieren; keine echte High-FPS-Aufnahme behaupten, wenn sie nur synthetisch erzeugt ist. |
| `/splash` | Flüssigkeits-/Eintauchbewegung als kurzer Effektclip darstellen. |
| `/ingredientdrop` | Zutaten oder Bestandteile kontrolliert in die Szene fallen beziehungsweise einfliegen lassen. |
| `/steam` | Dampf-/Rauchbewegung als atmosphärischen Effekt ergänzen. |
| `/talkinghead` | Sprechende Person als Frontal-/Kameraansprache erzeugen oder bearbeiten; Voice-/Lip-Sync separat prüfen. |
| `/cartoonclip` | Kurzen animierten Clip in allgemeiner Zeichen-/Cartoonästhetik erzeugen. |
| `/parallax` | Aus Ebenen/Tiefe eine kontrollierte Parallaxbewegung ableiten. |
| `/dayornight` | Zeit-/Lichtwechsel zwischen Tages- und Nachtwirkung als Übergang gestalten. |
| `/hookclip` | Sehr kurzer aufmerksamkeitsstarker Einstieg, dessen Inhalt trotzdem zum anschließenden Video passen muss. |

## Routing zu KI-Regeln

Diese Shortcuts sind Bedienkürzel, keine Ersatzskills.

Je nach Aufgabe:

```text
ein einzelnes Bild planen
→ Bildarbeit/Skills/bild-prebrief

bestehendes Bild bewerten
→ Bildarbeit/Skills/bildreview

Serienidentität / wiederkehrende Figur
→ entitaetsbibel + serien-kontinuitaetscheck

Social-/Anzeigenkontext
→ Social-Media-und-Content-Praesenz

codebasierte Motion-/Videoproduktion
→ Workflows/Codebasierte-Motion-Graphics-und-Video.md
```

## Leitgedanke

> Ein gutes Kürzel spart Tipparbeit. Es ersetzt weder Quelle, Briefing, Rechteprüfung noch Qualitätsreview.
