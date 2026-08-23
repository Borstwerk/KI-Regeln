# Skill-Handbuch

## Zweck

Dieses Dokument erklärt die Skills dieses Repositories in verständlicher Sprache.

Eine `SKILL.md` ist primär als kompakte Arbeitsanweisung für einen KI-Agenten gedacht. Dieses Handbuch erklärt für Menschen:

- was der Skill bedeutet;
- wann er sinnvoll ist;
- wann er eher nicht passt;
- wie er typischerweise eingesetzt wird;
- welche verwandten Skills dazugehören.

## Was ist ein Skill?

Ein Skill ist eine begrenzte Arbeitsdisziplin.

Er beschreibt **wie** gearbeitet wird. Er definiert nicht automatisch:

- das konkrete Projektziel;
- lokale Fachlogik;
- Architektur oder Kanon;
- persönliche Werte;
- eine Freigabe.

> Ein Skill ist ein Werkzeug. Gute Arbeit entsteht, wenn das richtige Werkzeug im richtigen Kontext eingesetzt wird.

## Schnellauswahl

| Ich möchte ... | Passender Skill |
|---|---|
| eine Erfahrung oder Situation sortieren | `reflektierender-dialog` |
| eine Entscheidung besser durchdenken | `entscheidungsunterstuetzung` |
| aus einem Ziel einen kleinen Lern- und Handlungsloop machen | `ziel-reflexions-loop` |
| für einen Agenten den nötigen Kontext auswählen | `context-engineering` |
| eine komplexe Aufgabe in abhängige Teile zerlegen | `task-graph` |
| innerhalb eines freigegebenen Scopes iterativ prüfen und reparieren | `verification-loop` |
| einen Agentenauftrag sauber begrenzen | `delegation-contract` |
| prüfen, ob ein Agent zuverlässig nach Regeln arbeitet | `agent-eval` |
| einen aktuellen Fakt schnell im Web prüfen | `web-search` |
| eine größere Recherche strukturieren | `research-plan` |
| ein Thema iterativ aus mehreren Perspektiven untersuchen | `deep-research` |
| die Eignung einer Quelle für einen Claim bewerten | `source-evaluation` |
| einen konkreten Claim verifizieren | `claim-verification` |
| Research-Funde zu einem Wissensbild zusammenführen | `research-synthesis` |
| prüfen, ob Zitate tatsächlich die Claims tragen | `citation-audit` |
| einen natürlichen Sach- oder Gebrauchstext schreiben | `natuerliches-schreiben` |
| kreative Prosa oder Szenen schreiben | `kreatives-schreiben` |
| einen Text auf künstliche oder mechanische Muster prüfen | `stilreview` |
| ein Bild vor der Generierung planen | `bild-prebrief` |
| eine wiederkehrende Figur, ein Objekt oder einen Ort definieren | `entitaetsbibel` |
| eine Bildserie auf Drift prüfen | `serien-kontinuitaetscheck` |
| entscheiden, ob ein Bild bleibt, korrigiert oder neu gebaut wird | `bildreview` |
| eine eigenständige Webdesign-Richtung entwickeln | `frontend-design` |
| Webtypografie, Farben, Abstände und UI-Grundsätze systematisieren | `design-system` |
| Seitenstruktur vor visueller Politur klären | `greybox` |
| konkreten Webcontent statt KI-Fülltext entwickeln | `web-content` |
| eine gerenderte Website kritisch auf Designqualität und AI-Slop prüfen | `web-design-review` |
| eine Weboberfläche auf Accessibility prüfen | `accessibility-review` |
| Frontend-Performance messen und gezielt verbessern | `frontend-performance` |
| eine implementierte Oberfläche tatsächlich im Browser prüfen | `visual-verification` |
| Fachbegriffe und Domänengrenzen modellieren | `domain-modeling` |
| mit kleinen Red/Green-Zyklen implementieren | `tdd` |
| einen Fehler systematisch bis zur Ursache untersuchen | `diagnose` |
| einen tatsächlichen Code-Diff kritisch prüfen | `code-review` |

---

# Arbeitsweisen

## `reflektierender-dialog`

**Was ist das?**  
Ein Skill, um Erfahrungen, Gedanken oder Situationen gemeinsam zu ordnen, ohne vorschnell zu diagnostizieren oder Lösungen aufzudrängen.

**Wann sinnvoll?**

- persönliche oder strategische Reflexion;
- schwierige Situationen sortieren;
- Gedanken und Beobachtungen auseinanderhalten;
- Ambivalenz sichtbar machen;
- aus einer Erfahrung lernen.

**Wann eher nicht?**

- wenn nur eine direkte Faktenantwort benötigt wird;
- wenn eine medizinische, psychologische, rechtliche oder andere professionelle Diagnose erforderlich wäre;
- wenn der nächste Schritt bereits klar ist und weitere Reflexion nur im Kreis laufen würde.

**Mini-Beispiel**

> „Hilf mir, diese Situation zu sortieren. Ich möchte erst verstehen, was passiert ist, bevor wir Lösungen suchen.“

**Verwandte Skills**

- `entscheidungsunterstuetzung`
- `ziel-reflexions-loop`

---

## `entscheidungsunterstuetzung`

**Was ist das?**  
Ein Skill, um Kriterien, Optionen, Unsicherheiten, Gegenargumente und Zielkonflikte strukturiert sichtbar zu machen.

**Wann sinnvoll?**

- mehrere Optionen stehen im Raum;
- Kriterien müssen gegeneinander abgewogen werden;
- eine Empfehlung soll nachvollziehbar statt autoritär sein;
- eigene Überlegungen sollen erweitert und gegengeprüft werden.

**Wann eher nicht?**

- wenn die Entscheidung längst gefallen ist;
- wenn nur eine reine Faktenauskunft benötigt wird;
- wenn persönliche Wertgewichtungen fälschlich von der KI übernommen würden.

**Mini-Beispiel**

> „Ich schwanke zwischen A und B. Hilf mir, Kriterien, Unsicherheiten und die stärksten Gegenargumente sauber aufzuschreiben.“

**Verwandte Skills**

- `reflektierender-dialog`
- `ziel-reflexions-loop`

---

## `ziel-reflexions-loop`

**Was ist das?**  
Ein Skill, der Ziel, reales Hindernis, kleinen Versuch, Erfahrung und Anpassung zu einem Lernloop verbindet.

**Wann sinnvoll?**

- Gewohnheiten;
- Selbstverbesserung;
- Lernprozesse;
- kleine Verhaltensänderungen;
- Ziele, die durch reale Erfahrung statt nur durch Analyse geschärft werden müssen.

**Wann eher nicht?**

- wenn nur Analyse ohne Handlung gewünscht ist;
- wenn das Ziel noch völlig unklar ist;
- wenn eine professionelle Intervention notwendig wäre.

**Mini-Beispiel**

> „Ich möchte in Situation X anders reagieren. Lass uns einen kleinen Versuch für die nächste passende Situation bauen und danach auswerten.“

**Verwandte Skills**

- `reflektierender-dialog`
- `entscheidungsunterstuetzung`

---

# Agentenarbeit

## `context-engineering`

**Was ist das?**  
Ein Skill, um einem Agenten den kleinsten ausreichenden, aktuellen und relevanten Kontext bereitzustellen.

**Wann sinnvoll?**

- große Repositories oder Dokumentbestände;
- komplexe Aufgaben mit mehreren Quellen;
- lange Agentenläufe;
- wenn irrelevanter Kontext die Arbeit verwässern könnte.

**Wann eher nicht?**

- bei sehr kleinen Aufgaben mit offensichtlich ausreichendem Kontext.

**Mini-Beispiel**

> „Für diesen Fix sind nur Requirement R-12, diese drei Dateien, der Regressionstest und die Architekturregel X relevant.“

**Verwandte Skills**

- `delegation-contract`
- `task-graph`

---

## `task-graph`

**Was ist das?**  
Ein Skill, der komplexe Arbeit in klar abgegrenzte, überprüfbare Knoten mit echten Abhängigkeiten zerlegt.

**Wann sinnvoll?**

- größere Features oder Umbauten;
- mehrere unabhängige Teilstränge;
- mögliche Parallelisierung;
- Aufgaben, bei denen Zwischenzustände überprüfbar sein müssen.

**Wann eher nicht?**

- kleine Aufgaben, die einfacher direkt bearbeitet werden;
- wenn künstliche Zerlegung mehr Verwaltungsaufwand als Nutzen erzeugt.

**Mini-Beispiel**

```text
Spec
├─→ Slice A → Verify A
├─→ Slice B → Verify B
└─→ Slice C → Verify C
         ↓
     Integration
```

**Verwandte Skills**

- `delegation-contract`
- `verification-loop`
- `context-engineering`

---

## `verification-loop`

**Was ist das?**  
Ein kontrollierter Arbeitsloop: arbeiten → prüfen → diagnostizieren → korrigieren → erneut prüfen.

**Wann sinnvoll?**

- Bugs und Fixes;
- kleine Implementierungsslices;
- Aufgaben mit klaren automatischen oder reproduzierbaren Nachweisen.

**Wann eher nicht?**

- wenn eine neue Produkt-, Architektur- oder Scope-Entscheidung nötig ist;
- wenn keine zuverlässige Prüfung möglich ist;
- wenn der Loop den freigegebenen Bereich verlassen müsste.

**Mini-Beispiel**

> „Behebe den Fehler innerhalb dieses Moduls. Führe nach jeder Änderung den Regressionstest aus. Stoppe, wenn dafür eine API-Änderung nötig wird.“

**Verwandte Skills**

- `diagnose`
- `tdd`
- `code-review`

---

## `delegation-contract`

**Was ist das?**  
Ein Skill zum Definieren eines klaren Agentenauftrags aus Ziel, Scope, Quellen, Befugnissen, Akzeptanzbedingungen, Stop-Regeln und erwarteter Evidence.

**Wann sinnvoll?**

- eigenständige Agentenarbeit;
- delegierte Teilaufgaben;
- längere oder risikoreichere Läufe;
- wenn das Ergebnis später sauber reviewed werden soll.

**Wann eher nicht?**

- bei trivialen Ein-Schritt-Aufgaben, bei denen der Vertrag mehr Text als die Aufgabe erzeugt.

**Mini-Beispiel**

> „Du darfst Dateien A–C ändern, aber weder Tests abschwächen noch pushen. Fertig ist der Auftrag erst mit grünem Test X, Diff-Liste und offenen Risiken.“

**Verwandte Skills**

- `context-engineering`
- `task-graph`
- `verification-loop`

---

## `agent-eval`

**Was ist das?**  
Ein Skill zur reproduzierbaren Prüfung, ob ein Agent nicht nur ein Ergebnis erzeugt, sondern auch die gewünschte Arbeitsweise einhält.

**Wann sinnvoll?**

- Skills oder Agentenprompts vergleichen;
- wiederkehrende Agentenworkflows verbessern;
- Regressionen im Agentenverhalten erkennen;
- Golden Tasks aufbauen.

**Wann eher nicht?**

- für einmalige kleine Aufgaben ohne wiederkehrenden Workflow.

**Mini-Beispiel**

> „Prüfe mit denselben fünf Testaufgaben, ob `tdd` v2 Scope, Testqualität und Stop-Gates zuverlässiger einhält als v1.“

**Verwandte Skills**

- `delegation-contract`
- `code-review`

---

# Recherche

## `web-search`

**Was ist das?**  
Ein Skill für schnelle aktuelle Webrecherche bei klar begrenzten Fragen.

**Wann sinnvoll?**

- einzelne aktuelle Fakten;
- Produktversionen, Termine oder konkrete Zustände;
- kleine Nachschlagefragen;
- ein Thema braucht aktuelle Quellen, aber keine umfassende Analyse.

**Wann eher nicht?**

- bei komplexen Entscheidungen mit mehreren Perspektiven;
- wenn Widersprüche, Marktvergleich oder umfangreiche Evidence nötig sind.

**Mini-Beispiel**

> „Prüfe die aktuelle Version in einer geeigneten Primärquelle. Suchsnippets sind nur Leads; öffne die eigentliche Quelle.“

**Verwandte Skills**

- `claim-verification`
- `source-evaluation`

---

## `research-plan`

**Was ist das?**  
Ein Skill, der eine größere Research-Frage in Teilfragen, Perspektiven, Quellenarten und Coverage-Kriterien zerlegt.

**Wann sinnvoll?**

- Deep Research;
- komplexe Vergleiche;
- strategische Entscheidungen;
- Themen mit mehreren relevanten Perspektiven.

**Wann eher nicht?**

- bei einfachen Lookup-Fragen;
- wenn die Planung mehr Aufwand erzeugt als die gesamte Recherche.

**Mini-Beispiel**

> „Zerlege die Hauptfrage in technische, wirtschaftliche und Nutzer-Teilfragen und definiere, welche Quellenarten jede Teilfrage am besten tragen.“

**Verwandte Skills**

- `deep-research`
- `task-graph`
- `context-engineering`

---

## `deep-research`

**Was ist das?**  
Ein Orchestrierungs-Skill für iterative Recherche über mehrere Teilfragen, Suchwinkel und Evidence-Pfade.

**Wann sinnvoll?**

- umfangreiche Markt- oder Technologieanalyse;
- komplexe politische oder wissenschaftliche Fragestellungen;
- Entscheidungen mit hohem Informationsbedarf;
- wenn ein einzelner Suchpfad blinde Flecken erzeugen würde.

**Wann eher nicht?**

- bei einer kleinen eindeutig beantwortbaren Frage;
- wenn nur ein vorhandener Claim geprüft werden soll.

**Mini-Beispiel**

```text
research-plan
→ getrennte Research-Threads
→ Claim/Evidence
→ Coverage Check
→ gezielte Nachrecherche
→ research-synthesis
→ citation-audit
```

**Verwandte Skills**

- `research-plan`
- `source-evaluation`
- `research-synthesis`
- `claim-verification`
- `citation-audit`

---

## `source-evaluation`

**Was ist das?**  
Ein Skill zur claimbezogenen Bewertung einer Quelle nach Direktheit, Aktualität, Primärnähe, Fachnähe, Unabhängigkeit und Methodentransparenz.

**Wann sinnvoll?**

- zentrale oder kontroverse Claims;
- mehrere Quellen widersprechen;
- Community- und Primärquellen müssen unterschiedlich eingeordnet werden;
- Quellenzahl ist hoch, aber Unabhängigkeit unklar.

**Wann eher nicht?**

- bei einer eindeutigen simplen Primärquelle für einen trivialen Fakt.

**Mini-Beispiel**

> „Bewerte nicht die Website allgemein, sondern ob genau diese Quelle den Claim über Feature X aktuell und direkt trägt.“

**Verwandte Skills**

- `claim-verification`
- `deep-research`

---

## `claim-verification`

**Was ist das?**  
Ein Skill, der einen konkreten Claim in prüfbare Teilclaims zerlegt und gegen Primärquelle, Gegenbelege und Kontext prüft.

**Wann sinnvoll?**

- Fact Check;
- strittige Aussagen;
- aktuelle Produkt- oder Unternehmensclaims;
- wichtige Zahlen, Studien- oder Rechtsbehauptungen.

**Wann eher nicht?**

- wenn erst eine offene Research-Frage exploriert werden muss.

**Mini-Beispiel**

> „Prüfe, ob der Claim wirklich für Version Y gilt und ob die Originalquelle dieselbe Aussage macht wie die Zusammenfassung.“

**Verwandte Skills**

- `source-evaluation`
- `citation-audit`
- `web-search`

---

## `research-synthesis`

**Was ist das?**  
Ein Skill, der Research-Funde nach Erkenntnissen statt nach Quellen ordnet und Fakten, Interpretation, Konflikte und Unsicherheiten trennt.

**Wann sinnvoll?**

- nach Multi-Source- oder Deep Research;
- für Vergleichsberichte, Decision Briefs oder ausführliche Analysen;
- wenn viele Funde zu einem klaren Wissensbild verdichtet werden müssen.

**Wann eher nicht?**

- wenn nur ein einzelner Fakt beantwortet wird.

**Mini-Beispiel**

> „Strukturiere nach: Was wissen wir? Wo besteht Konsens? Wo widersprechen sich Quellen? Welche Unsicherheit bleibt?“

**Verwandte Skills**

- `deep-research`
- `citation-audit`
- `claim-verification`

---

## `citation-audit`

**Was ist das?**  
Ein unabhängiger Review einer fertigen Research-Synthese darauf, ob wesentliche Claims von den tatsächlich zitierten Quellen getragen werden.

**Wann sinnvoll?**

- Deep-Research-Berichte;
- faktenreiche Entscheidungsvorlagen;
- Veröffentlichungen;
- Antworten mit vielen aktuellen oder strittigen Behauptungen.

**Wann eher nicht?**

- bei reiner Kreativarbeit ohne externe Faktenclaims.

**Mini-Beispiel**

> „Extrahiere die zentralen Faktenclaims und prüfe für jeden, ob die Quelle genau diesen Claim, Zeitraum und Geltungsbereich trägt.“

**Verwandte Skills**

- `claim-verification`
- `research-synthesis`
- `source-evaluation`

---

# Schreiben

## `natuerliches-schreiben`

**Was ist das?**  
Ein Skill für klare, glaubwürdige Texte ohne unnötige KI-, Werbe-, Management- oder Bedeutungsrhetorik.

**Wann sinnvoll?**

- Sachtexte;
- Dokumentation;
- Erklärtexte;
- E-Mails oder Gebrauchstexte;
- Überarbeitung künstlich wirkender Texte.

**Wann eher nicht?**

- wenn bewusst eine stark stilisierte literarische Stimme gefragt ist.

**Mini-Beispiel**

> „Formuliere das klar und natürlich. Einfache Verben sind ausdrücklich erlaubt; keine künstliche Aufwertung.“

**Verwandte Skills**

- `stilreview`

---

## `kreatives-schreiben`

**Was ist das?**  
Ein Skill für kreative Prosa mit Szene, Figurenstimme, räumlicher Klarheit, natürlichem Dialog und verdienter Wirkung.

**Wann sinnvoll?**

- Roman- und Kurzgeschichtenszenen;
- Kinder- und Jugendprosa;
- fiktionale Dialoge;
- erzählerische Überarbeitungen.

**Wann eher nicht?**

- für technische oder rein sachliche Texte.

**Mini-Beispiel**

> „Schreibe die Szene aus dem konkreten Moment heraus. Erkläre die Bedeutung nicht vorab; lass sie aus Handlung und Reaktion entstehen.“

**Verwandte Skills**

- `stilreview`
- `natuerliches-schreiben`

---

## `stilreview`

**Was ist das?**  
Ein Skill, der auffällige Muster in einem Text erkennt und erst nach Kontextprüfung entscheidet, ob daraus ein echter Änderungsfall wird.

**Wann sinnvoll?**

- Schlussredaktion;
- Prüfung auf mechanische KI-Muster;
- Rhythmus- und Strukturprüfung;
- Vergleich mit einer vorhandenen Stilreferenz.

**Wann eher nicht?**

- wenn bloß Wörter nach einer Blacklist gesucht und automatisch ersetzt werden sollen.

**Mini-Beispiel**

> „Markiere Muster, aber ändere nur Stellen, an denen Präzision, Stimme, Rhythmus oder Glaubwürdigkeit tatsächlich leiden.“

**Verwandte Skills**

- `natuerliches-schreiben`
- `kreatives-schreiben`

---

# Bildarbeit

## `bild-prebrief`

**Was ist das?**  
Ein Skill, der vor einer Bildgenerierung Moment, Aussage, Komposition, sichtbare Entitäten, Kontinuitätszustand und Ausschlüsse klärt.

**Wann sinnvoll?**

- Illustrationen;
- Storyboards;
- Serienbilder;
- komplexe Szenen mit wiederkehrenden Figuren oder Objekten.

**Wann eher nicht?**

- bei freien Einzelbildern, bei denen Überraschung ausdrücklich wichtiger als Kontinuität ist.

**Mini-Beispiel**

> „Vor der Generierung: Was ist der exakte Moment, was soll sofort lesbar sein, wer ist sichtbar und was darf keinesfalls im Bild erscheinen?“

**Verwandte Skills**

- `entitaetsbibel`
- `serien-kontinuitaetscheck`
- `bildreview`

---

## `entitaetsbibel`

**Was ist das?**  
Ein Skill zum stabilen Definieren wiederkehrender Figuren, Kreaturen, Objekte, Fahrzeuge oder Orte.

**Wann sinnvoll?**

- Bildserien mit wiederkehrenden Motiven;
- Storybooks und Comics;
- Marken- oder Produktwelten;
- konsistente Orte und Requisiten.

**Wann eher nicht?**

- bei bewusst einmaligen, nicht wiederkehrenden Elementen.

**Mini-Beispiel**

> „Definiere Form, Proportionen, unveränderliche Erkennungsmerkmale, erlaubte Variation und bekannte No-Gos dieser Figur.“

**Verwandte Skills**

- `bild-prebrief`
- `serien-kontinuitaetscheck`

---

## `serien-kontinuitaetscheck`

**Was ist das?**  
Ein Skill zur Prüfung mehrerer Bilder auf Drift bei Identität, Stil, Struktur und zeitabhängigem Zustand.

**Wann sinnvoll?**

- Buchillustrationen;
- Storyboards;
- Kampagnen;
- wiederkehrende Charaktere oder Orte;
- längere Bildserien.

**Wann eher nicht?**

- bei voneinander unabhängigen Einzelbildern.

**Mini-Beispiel**

> „Prüfe alle Bilder chronologisch: Bleiben Figur, Größenrelation, Ausrüstung, Stil und zeitabhängige Veränderungen konsistent?“

**Verwandte Skills**

- `entitaetsbibel`
- `bildreview`

---

## `bildreview`

**Was ist das?**  
Ein Skill, der ein generiertes Bild gegen Brief, Referenzen und Kontinuität prüft und zwischen Keeper, lokalem Feinschliff, kontrolliertem Neubau und komplettem Neubau unterscheidet.

**Wann sinnvoll?**

- nach jeder wichtigen Bildgenerierung;
- bei Serien mit hohen Konsistenzanforderungen;
- wenn gute Kompositionen vor unnötigem Neugenerieren geschützt werden sollen.

**Wann eher nicht?**

- wenn nur freie visuelle Exploration gewünscht ist.

**Mini-Beispiel**

> „Die Szene und Komposition stimmen, aber ein Accessoire ist falsch: enger Feinschliff statt kompletter Neubau.“

**Verwandte Skills**

- `bild-prebrief`
- `serien-kontinuitaetscheck`

---

# Webentwicklung

## `frontend-design`

**Was ist das?**  
Ein Skill, der aus Produkt, Zielgruppe und Aufgabe eine konkrete visuelle Richtung ableitet, bevor das eigentliche UI gebaut wird.

**Wann sinnvoll?**

- neue Website oder neue Produktoberfläche;
- bestehendes UI wirkt austauschbar;
- eine klare Art Direction fehlt;
- typische KI-Template-Ästhetik soll bewusst vermieden werden.

**Wann eher nicht?**

- wenn eine freigegebene Designrichtung bereits vollständig existiert und nur umgesetzt werden soll;
- als Ersatz für lokale Markenentscheidungen.

**Mini-Beispiel**

> „Entwickle erst eine konkrete Designrichtung für diese Fachanwendung. Benenne auch, welche typischen SaaS-Muster hier bewusst nicht passen.“

**Verwandte Skills**

- `design-system`
- `greybox`
- `web-design-review`

---

## `design-system`

**Was ist das?**  
Ein Skill, der eine freigegebene Designrichtung in konsistente Typorollen, Farben, Spacing, Surfaces, Motion-Grundsätze und wiederverwendbare Komponentenprinzipien überführt.

**Wann sinnvoll?**

- mehrere Seiten oder Screens;
- wiederkehrende UI-Muster;
- Aufbau oder Pflege einer lokalen `DESIGN.md`;
- Designentscheidungen sollen stabil und agentenlesbar werden.

**Wann eher nicht?**

- wenn die Designrichtung selbst noch ungeklärt ist;
- wenn ein riesiges Designsystem für eine triviale Einzelseite gebaut würde.

**Mini-Beispiel**

> „Leite aus der freigegebenen Art Direction semantische Farbrollen, Typorollen, Spacing und begrenzte Surface-Varianten ab.“

**Verwandte Skills**

- `frontend-design`
- `greybox`
- `accessibility-review`

---

## `greybox`

**Was ist das?**  
Ein Skill für Seitenstruktur, Informationshierarchie, Navigation und Nutzerfluss vor visueller Politur.

**Wann sinnvoll?**

- neue Seiten oder Flows;
- unklare Informationsarchitektur;
- High-Fidelity wurde zu früh begonnen;
- Desktop und Mobile sollen strukturell gemeinsam geplant werden.

**Wann eher nicht?**

- wenn nur ein kleiner lokaler Stylefix an einer stabilen Seite nötig ist.

**Mini-Beispiel**

> „Baue zuerst eine reduzierte Greybox mit realistischen Textlängen. Noch keine Gradients, Schatten oder Motion.“

**Verwandte Skills**

- `frontend-design`
- `design-system`
- `web-content`

---

## `web-content`

**Was ist das?**  
Ein Skill für konkreten, glaubwürdigen Webcontent mit Informations- oder Handlungswert statt generischer Marketing- und Fülltexte.

**Wann sinnvoll?**

- Landingpages;
- Produktseiten;
- Überschriften und Mikrocopy;
- Formulare und Empty States;
- Überarbeitung KI-typischer Website-Texte.

**Wann eher nicht?**

- wenn Fakten oder Produktversprechen fehlen und erfunden werden müssten.

**Mini-Beispiel**

> „Ersetze abstrakte Benefits durch konkrete Produktinformationen. Keine erfundenen Prozentwerte, Logos oder Testimonials.“

**Verwandte Skills**

- `natuerliches-schreiben`
- `greybox`
- `web-design-review`

---

## `web-design-review`

**Was ist das?**  
Ein unabhängiger Review einer gerenderten Website auf Identität, Hierarchie, Typografie, Content, Responsive-Verhalten und typische AI-Slop-Muster.

**Wann sinnvoll?**

- vor Designfreigabe;
- nach Agentenimplementierungen;
- bei bestehenden Seiten, die generisch wirken;
- zum Vergleich mehrerer Designstände.

**Wann eher nicht?**

- als Auftrag, ungefragt eine komplett neue Markenidentität zu entwerfen.

**Mini-Beispiel**

> „Prüfe die Seite gegen `DESIGN.md` und markiere Blocker, hohe Funde und Anti-Slop-Risiken. Schütze starke bestehende Entscheidungen.“

**Verwandte Skills**

- `frontend-design`
- `web-content`
- `visual-verification`

---

## `accessibility-review`

**Was ist das?**  
Ein Skill zur Prüfung von Semantik, Tastaturbedienung, Fokus, Formularen, Kontrast, Motion und assistiver Nutzbarkeit.

**Wann sinnvoll?**

- interaktive Weboberflächen;
- Formulare, Navigation, Dialoge;
- vor Release;
- bei Accessibility-Regressionsrisiken.

**Wann eher nicht?**

- als bloßer Linterlauf ohne reale Bedienprüfung.

**Mini-Beispiel**

> „Prüfe den Kernflow per Tastatur, kontrolliere Fokus und Labels und kombiniere das mit automatisierten Accessibility-Checks.“

**Verwandte Skills**

- `visual-verification`
- `design-system`
- `code-review`

---

## `frontend-performance`

**Was ist das?**  
Ein Skill für messbare Performanceanalyse mit Priorität auf Waterfalls, Bundlekosten, Client-JavaScript, Medien und teure Renderingpfade.

**Wann sinnvoll?**

- langsame Seiten;
- neue komplexe Features;
- auffällige Bundles;
- Performanceprüfung vor Release.

**Wann eher nicht?**

- wenn ohne Messung nur prophylaktisch Mikrooptimierungen eingebaut werden sollen.

**Mini-Beispiel**

> „Messe zuerst die Route. Behebe danach den größten bestätigten Engpass und vergleiche unter denselben Bedingungen erneut.“

**Verwandte Skills**

- `diagnose`
- `verification-loop`
- `visual-verification`

---

## `visual-verification`

**Was ist das?**  
Ein Skill, der eine implementierte Website tatsächlich in Browser, Viewports und relevanten UI-Zuständen prüft.

**Wann sinnvoll?**

- nach UI-Implementierung;
- vor Review oder Release;
- bei responsiven oder visuellen Änderungen;
- wenn Screenshots oder andere UI-Evidence benötigt werden.

**Wann eher nicht?**

- als Ersatz für Code-Review, Accessibility oder funktionale Tests.

**Mini-Beispiel**

> „Rendere die geänderten Seiten auf Desktop und Mobile, prüfe Loading/Error/Empty, Konsole, Fokus und sammle visuelle Evidence.“

**Verwandte Skills**

- `web-design-review`
- `accessibility-review`
- `frontend-performance`
- `code-review`

---

# Programmieren

## `domain-modeling`

**Was ist das?**  
Ein Skill, um Fachbegriffe, Objekte, Zustände, Beziehungen und Systemgrenzen sauber zu modellieren, bevor Implementierungsdetails alles vermischen.

**Wann sinnvoll?**

- neue Fachlogik;
- unklare Begriffe;
- komplexe Zustände oder Regeln;
- wenn technische Strukturen die Domäne falsch abbilden könnten.

**Wann eher nicht?**

- bei rein technischen Kleinständerungen ohne fachliche Bedeutung.

**Mini-Beispiel**

> „Bevor wir Klassen bauen: Was ist fachlich eine Rechnung, ein Beleg, ein Statuswechsel und welche Invarianten gelten?“

**Verwandte Skills**

- `tdd`
- `code-review`

---

## `tdd`

**Was ist das?**  
Ein Skill für kleine Red/Green-Zyklen: erst ein aussagekräftiger fehlschlagender Test, dann die kleinste passende Implementierung, anschließend Aufräumen bei weiterhin grünen Tests.

**Wann sinnvoll?**

- neue Logik;
- Bugfixes mit reproduzierbarem Verhalten;
- Regressionen;
- kleine überprüfbare Implementierungsslices.

**Wann eher nicht?**

- wenn noch gar nicht klar ist, welches Verhalten überhaupt gewünscht ist;
- bei rein explorativen Prototypen, sofern der Prototyp ausdrücklich Wegwerfcode ist.

**Mini-Beispiel**

> „Schreibe zuerst den Regressionstest, der den Bug sichtbar macht. Implementiere danach nur so viel, dass er grün wird.“

**Verwandte Skills**

- `diagnose`
- `verification-loop`
- `code-review`

---

## `diagnose`

**Was ist das?**  
Ein Skill für reproduzierbare Root-Cause-Diagnose mit Beobachtung, Hypothesen, gezielten Tests und Gegenproben.

**Wann sinnvoll?**

- Bugs;
- Performanceprobleme;
- unerklärliche Zustände;
- sporadische Fehler;
- Probleme mit mehreren plausiblen Ursachen.

**Wann eher nicht?**

- wenn die Ursache bereits eindeutig nachgewiesen ist und nur noch umgesetzt werden muss.

**Mini-Beispiel**

> „Isoliere zuerst den kleinsten reproduzierbaren Fall und prüfe die drei plausibelsten Ursachen mit gezielten Messungen.“

**Verwandte Skills**

- `tdd`
- `verification-loop`
- `code-review`

---

## `code-review`

**Was ist das?**  
Ein Skill zur kritischen Prüfung des tatsächlichen Code-Diffs gegen Anforderung, Projektregeln, Tests, Architektur und Risiken.

**Wann sinnvoll?**

- vor Freigabe;
- nach Agentenimplementierungen;
- bei Pull Requests;
- bei sicherheits- oder migrationsrelevanten Änderungen.

**Wann eher nicht?**

- als Ersatz für Planung oder Tests;
- wenn nur ein Abschlussbericht gelesen wird, aber der tatsächliche Diff nicht verfügbar ist.

**Mini-Beispiel**

> „Prüfe nicht nur, ob Tests grün sind. Vergleiche Requirement, tatsächlichen Diff, Teständerungen und mögliche Scope-Ausweitungen.“

**Verwandte Skills**

- `diagnose`
- `tdd`
- `agent-eval`

---

# Skills kombinieren

Skills können bewusst kombiniert werden.

Beispiele:

```text
Software-Bug:
context-engineering
→ diagnose
→ tdd
→ verification-loop
→ code-review
```

```text
größeres Agentenfeature:
delegation-contract
→ context-engineering
→ task-graph
→ verification-loop pro Slice
→ code-review
```

```text
Deep Research:
research-plan
→ deep-research
→ source-evaluation bei wichtigen Quellen
→ research-synthesis
→ claim-verification für zentrale Claims
→ citation-audit
```

```text
schnelle aktuelle Websuche:
web-search
→ claim-verification, falls der gefundene Fakt besonders wichtig oder strittig ist
```

```text
Bildserie:
entitaetsbibel
→ bild-prebrief
→ Generierung
→ bildreview
→ serien-kontinuitaetscheck
```

```text
Website von Grund auf:
frontend-design
→ design-system
→ greybox
→ web-content
→ Implementierung
→ accessibility-review
→ frontend-performance
→ visual-verification
→ web-design-review
```

```text
bestehende Website verbessern:
visual-verification
→ web-design-review
→ accessibility-review
→ frontend-performance, falls relevant
→ gezielte Änderung
→ visual-verification erneut
```

```text
persönlicher Lernprozess:
reflektierender-dialog
→ entscheidungsunterstuetzung, falls nötig
→ ziel-reflexions-loop
→ reale Erfahrung
→ neuer Reflexionsdurchlauf
```

## Leitgedanke

> Nicht möglichst viele Skills gleichzeitig einsetzen. Den kleinsten Satz wählen, der die Aufgabe zuverlässig unterstützt.