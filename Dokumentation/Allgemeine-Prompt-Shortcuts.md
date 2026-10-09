# Allgemeine Prompt-Shortcuts

Stand: 2026-10-09

## Zweck

Diese Seite sammelt die **100 ursprünglichen Prompt-Shortcuts** für Schreiben, Lernen, Formatierung, Content, Entscheidungen, Denksysteme, Kreativität, Coding und Alltag sowie **vier eigenständig ergänzte Lern-Shortcuts** (`/lernzettel`, `/tafelbild`, `/probearbeit`, `/merkbild`). Damit sind 104 Kürzel dokumentiert; die ursprüngliche 100er-Liste bleibt unverändert.

Alle Einträge sind:

```text
PROMPT-SHORTCUT
```

und **keine behaupteten eingebauten ChatGPT-Produktbefehle**.

Ein Shortcut ist nur eine kurze Bedienform für eine gewünschte Denk-, Schreib- oder Ausgabeoperation. Er ersetzt weder belastbare Quellen noch die zuständigen KI-Regeln-Skills.

## Herkunft und Übernahmegrenze

Methodische Ausgangsreferenz war die vom Nutzer bereitgestellte statische PDF:

> Christian · @KI.GLATZE · „100 ChatGPT-Codes“ · Ausgabe 2026

Die PDF selbst wird **nicht** in diesem Repository redistribuiert. Die vier neuen Lern-Ergänzungen stammen nicht aus dieser 100er-PDF; sie wurden anhand einer später vom Nutzer genannten Kurzbefehlsliste als eigenständige, quellenkritische Bedienformen formuliert.

Für KI-Regeln wurden:

- die funktionalen Kurzlabels als Prompt-Sprache ausgewertet;
- Beschreibungen, Grenzen, Routing und Schutzregeln eigenständig formuliert;
- keine längeren Originaltexte, Beispiele, Tabellenlayouts oder PDF-Abbildungen übernommen;
- keine freie Lizenz der Ausgangs-PDF unterstellt.

Die Quelle stellt selbst klar, dass es sich nicht um versteckte OpenAI-Befehle handelt, sondern um verständliche Kurzformen für Anweisungen. Diese Einordnung wird beibehalten.

## Verwendung

Ein Shortcut kann vor oder nach der eigentlichen Aufgabe stehen:

```text
/pareto
Priorisiere diese Projektliste.
```

oder:

```text
Hier ist mein Entwurf.
No Fluff
```

Beim ersten Gebrauch in einem unbekannten Kontext hilft ein kurzer Zusatz:

```text
/odds
Schätze nur grob und nenne Annahmen und Hebel.
```

Shortcuts können kombiniert werden, wenn sich ihre Anforderungen nicht widersprechen:

```text
/pareto + No Fluff
```

bedeutet sinngemäß:

> auf die stärksten Hebel fokussieren und knapp antworten.

## Kollisionen und bestehende Kürzel

Einige Namen überschneiden sich mit bereits dokumentierten Prompt-/UI-Shortcuts.

### `/gaps`

Bereits vorhanden. Die lokale Bedeutung wird bewusst **breiter** gefasst:

- bei Lernstoff → Wissenslücken;
- bei Plänen → fehlende Aufgaben, Rollen, Voraussetzungen oder Risiken.

### Lern-Shortcuts gegenüber bestehenden Formen

- `/lernzettel` erweitert `/cheatsheet`: lernorientierte Quellensynthese statt reine Kurzreferenz.
- `/tafelbild` ergänzt `/mindmap` und `/sketchnodes`: geführter didaktischer Zusammenhang statt Begriffsnetz.
- `/probearbeit` ergänzt Quiz: Punkte, Zeit, Aufgabenmix und separater Lösungsteil.
- `/merkbild` ergänzt `/mnemonic` und `/comicnodes`: ein präziser visueller Erinnerungsanker statt bloßer Merksatz oder Panel-Folge.

Alle vier sind `PROMPT-SHORTCUT`, keine nachgewiesenen offiziellen Slash-Befehle. Die ausführlichen Beispiele und Qualitätsgrenzen stehen in `ChatGPT-Funktionen-und-Lernwerkzeuge.md`.

### `/mindmap` vs. `/mindmaps`

- `/mindmap` hier = allgemeiner Prompt-Shortcut;
- `/mindmaps` kann als UI-/Skill-Shortcut beobachtet werden.

Nicht automatisch gleichsetzen.

### `/carousel`

- in diesem Katalog primär Content-/Slide-Struktur;
- im Bild-/Medienkatalog kann `/carousel` die visuelle Karussellproduktion meinen.

Der umgebende Auftrag entscheidet.

### `/slides`

`/slides` als Prompt-Shortcut kann eine **Folienstruktur** bedeuten.

Wenn der Nutzer tatsächlich eine PPTX/Präsentationsdatei verlangt, gilt der Artefaktworkflow für Präsentationen.

### `/counter` vs. `/steelman`

Beide verlangen eine starke Gegenposition. `/steelman` ist die explizitere Variante; `/counter` bleibt ein kurzer Alias für denselben Grundgedanken.

## Wichtige Schutzregeln

### Keine private Gedankenkette

`/genius` bedeutet hier:

- sorgfältiger prüfen;
- Annahmen nennen;
- relevante Rechenschritte zeigen;
- Ergebnis begründen.

Es bedeutet **nicht**, interne/private Chain-of-Thought offenzulegen.

### Keine Scheingenauigkeit

`/odds`, `/predict`, `/simulate`, `/numbers` und ähnliche Kürzel müssen Annahmen, Datenqualität und Unsicherheit sichtbar halten.

Eine Zahl wirkt nicht allein deshalb belastbar, weil sie Prozentzeichen oder Nachkommastellen besitzt.

### Recht, Finanzen und Verträge

`/decode`, `/budget`, `/numbers` und verwandte Kürzel können strukturieren und rechnen. Sie ersetzen keine notwendige professionelle Beratung und dürfen keine nicht belegten Rechts-/Vertragsfolgen erfinden.

### Selbstreflexion

`/shrink`, `rewire` oder `/habit` sind Werkzeuge für Reflexion und Planung, keine Diagnose- oder Therapiekommandos.

Nur relevante, vom Nutzer bereitgestellte persönliche Informationen verwenden.

### Coding und Security

`/debug`, `/tests`, `/security` oder `/sql` ändern keine Evidence-Regeln:

```text
Code geschrieben
≠
Code ausgeführt

Test geschrieben
≠
Test bestanden

Review durchgeführt
≠
vollständige Sicherheit bewiesen
```

### Aktuelle Informationen

Bei `/travel`, `/convert` für Währungen, Produkt-/Preisfragen oder anderen zeitabhängigen Aufgaben aktuelle Quellen/Tools verwenden, wenn die Antwort davon abhängt.

## Inhalt

- Priorisieren, verdichten und Prompting
- Schreiben und Ton
- Lernen und Verstehen
- Format und Ausgabe
- Ideen und Content
- Analysieren und Entscheiden
- Denksysteme und Problemlösung
- Kreativ und Zukunft
- Coding und Technik
- Alltag und Planung

## Priorisieren, verdichten und Prompting

| Shortcut | KI-Regeln-Lesart |
|---|---|
| `/pareto` | Finde die wenigen Hebel mit wahrscheinlich größtem Nutzen und benenne bewusst, was nachrangig bleiben kann. |
| `/autoprompt` | Baue aus einer groben Idee einen klaren Arbeitsauftrag mit Ziel, Kontext, Input, Ausgabeformat, Qualitätskriterien und Grenzen. |
| `No Fluff` | Antworte kürzer und direkter: keine unnötige Einleitung, Wiederholung oder Füllformulierung; notwendige Einschränkungen bleiben erhalten. |
| `/signal` | Trenne entscheidungsrelevante Informationen von Kontext, Wiederholung und Nebensachen; Unsicherheit nicht als Rauschen wegwerfen. |
| `/odds` | Gib eine begründete Wahrscheinlichkeits- oder Chancenabschätzung mit Annahmen, Bandbreite und wichtigsten Hebeln statt Scheingenauigkeit. |
| `/decode` | Lies Vertrag, AGB oder Kleingedrucktes strukturiert und markiere Kosten-, Bindungs-, Kündigungs-, Haftungs- oder Rechtepunkte; kein Ersatz für Rechtsberatung. |
| `/simulate` | Spiele mehrere Handlungswege unter expliziten Annahmen über definierte Zeithorizonte durch und zeige, wodurch das Ergebnis kippen würde. |
| `/genius` | Bearbeite die Aufgabe besonders gründlich: prüfe Annahmen, rechne relevante Zwischenschritte nach und begründe das Ergebnis kompakt; keine private Gedankenkette offenlegen. |
| `/shrink` | Hilf bei ruhiger Selbstreflexion: frage nach Auslösern, Mustern, Nutzen und Kosten eines Verhaltens, ohne Diagnose- oder Therapieanspruch. |
| `rewire` | Entwirf aus ausdrücklich bereitgestellten Zielen, Verpflichtungen und Präferenzen eine praktikable Routine; nicht ungefragt persönliche Daten oder vermeintliches Wissen ausschöpfen. |

## Schreiben und Ton

| Shortcut | KI-Regeln-Lesart |
|---|---|
| `/polish` | Verbessere Grammatik, Rhythmus und Wortwahl bei möglichst unverändertem Inhalt und unveränderten Aussagen. |
| `/voice` | Leite aus freigegebenen Beispieltexten beobachtbare Stilmerkmale ab und wende sie an; bei fremden lebenden Autoren Eigenschaften abstrahieren statt eng imitieren. |
| `/active` | Formuliere unnötiges Passiv und schwere Nominalketten klarer mit aktiven Verben, ohne Verantwortlichkeiten zu erfinden. |
| `/dejargon` | Ersetze unnötigen Fachjargon durch verständliche Sprache oder erkläre notwendige Fachbegriffe kurz. |
| `/rhythm` | Variiere Satzlänge und Satzbau für bessere Lesbarkeit und Sprechbarkeit, ohne künstliche Unruhe zu erzeugen. |
| `/opener` | Erzeuge mehrere unterschiedliche Einstiege mit klar erkennbarer Ton- und Funktionsvariation. |
| `/closer` | Formuliere einen passenden Schluss mit klarer Konsequenz oder Handlungsaufforderung, wenn der Inhalt eine solche rechtfertigt. |
| `/mail` | Forme Stichpunkte zu einer vollständigen E-Mail mit passendem Betreff, Ton und klarer Handlungsinformation. |
| `/reply` | Entwirf eine Antwort auf eine vorhandene Nachricht im gewünschten Ton; Behauptungen und Zusagen nur aus vorhandenem Kontext ableiten. |
| `/du` | Stelle Anrede und Ton konsistent zwischen Du-/Sie-Form um; Namen, Fakten und Rechts-/Vertragsinhalte nicht verändern. |

## Lernen und Verstehen

| Shortcut | KI-Regeln-Lesart |
|---|---|
| `/levels` | Erkläre dasselbe Thema auf mehreren Verständnistiefen und halte die fachliche Aussage zwischen den Ebenen konsistent. |
| `/why5` | Nutze die Five-Whys-Heuristik zur Ursachenklärung; stoppe, wenn mehrere Ursachen plausibel sind, statt eine Scheinkausalität zu erzwingen. |
| `/mnemonic` | Baue eine merkbare Eselsbrücke oder einen Merksatz, der die zugrunde liegende Information nicht verfälscht. |
| `/gaps` | Finde fehlende Wissensbausteine oder Planlücken. Bei Lernstoff gezielt Rückfragen stellen; bei Vorhaben fehlende Voraussetzungen, Rollen oder Abhängigkeiten markieren. |
| `/spaced` | Entwirf einen Wiederholungsplan mit zunehmenden Abständen; konkrete Intervalle an Lernziel, Stoffmenge und Termin anpassen statt starr zu behandeln. |
| `/cheatsheet` | Verdichte ein Thema auf eine kompakte Referenz mit Begriffen, Regeln, Beispielen und typischen Fehlern. |
| `/mistakes` | Liste häufige Anfängerfehler, warum sie passieren und wie man sie erkennt oder vermeidet. |
| `/history` | Ordne eine Entwicklung chronologisch in wenige überprüfbare Stationen; unsichere Daten oder umstrittene Deutungen kenntlich machen. |
| `/roadmap` | Baue einen Lernpfad von Grundlagen zu fortgeschrittenen Fähigkeiten mit sinnvollen Meilensteinen und Übungsnachweisen. |
| `/teachback` | Lass den Nutzer ein Konzept in eigenen Worten erklären, prüfe die Erklärung und korrigiere nur konkrete Lücken oder Fehlannahmen. |

### Vier ergänzende Lern-Shortcuts (zusätzlich zur ursprünglichen 100er-Liste)

| Shortcut | KI-Regeln-Lesart |
|---|---|
| `/lernzettel` | Fasse bereitgestellte Lernunterlagen lernorientiert zusammen: Kernbegriffe, Regeln, prüfungsrelevante Inhalte, kurze Beispiele und typische Fehler. Fehlende Quelleninhalte markieren statt still ergänzen. |
| `/tafelbild` | Baue einen Zusammenhang wie an einer Tafel schrittweise auf: Frage, Begriffe, richtige Pfeile/Beziehungen, Ergebnis und Merksatz. Standardmäßig lesbares Schema; Bild/HTML nur bei entsprechender Aufgabe. |
| `/probearbeit` | Erzeuge eine alters-/niveaugerechte Übungsprüfung mit passender Bearbeitungszeit, Aufgabenmix, konsistenter Punkteverteilung und **separatem** Lösungsschlüssel samt Erwartungshorizont. Keine offiziellen Prüfungsunterlagen vortäuschen. |
| `/merkbild` | Verankere genau eine Zielinformation in einem merkfähigen Bildmotiv. Prüfe Metapher, Pfeile und Beschriftung fachlich; einen Bildentwurf nicht mit einem tatsächlich gerenderten Bild verwechseln. |

Diese Kürzel sind **keine neue Skill-Routing-Wahrheit**. Ein verständlicher Slash-Prompt ist noch keine produktseitig verfügbare Funktion. Die vier Kriterien sind zunächst dokumentiert, nicht als eigenständige Behavioral-Tests bestanden.
## Format und Ausgabe

| Shortcut | KI-Regeln-Lesart |
|---|---|
| `/matrix` | Ordne Punkte in eine passende 2×2-Matrix und erkläre Achsen sowie Zuordnungskriterien. |
| `/mermaid` | Erzeuge Mermaid-Code für ein passendes Diagramm; Syntax und Diagrammtyp an die Zielumgebung anpassen. |
| `/csv` | Gib strukturierte Daten als konsistentes CSV mit klarer Spaltenlogik aus; Trennzeichen/Encoding bei Bedarf an Zielsystem anpassen. |
| `/markdown` | Formatiere die Antwort als sauberes Markdown mit sinnvoller Hierarchie statt dekorativer Überschrifteninflation. |
| `/slides` | Entwirf eine Folienstruktur beziehungsweise ein Storyboard. Wenn ausdrücklich eine Präsentationsdatei gewünscht ist, ist das eine Artefaktaufgabe und nicht nur Textformatierung. |
| `/tweet` | Verdichte die Botschaft auf ein sehr kurzes Social-Posting; aktuelle Plattformlimits nur behaupten, wenn sie verifiziert sind. |
| `/faq` | Forme Inhalt in tatsächlich relevante Fragen und kurze Antworten um; keine Fragen erfinden, die fachlich nicht durch den Ausgangstext gedeckt sind. |
| `/glossary` | Extrahiere zentrale Fachbegriffe und erkläre jeden knapp, konsistent und im Kontext der Quelle. |
| `/timeline` | Ordne bestätigte Ereignisse, Schritte oder Meilensteine chronologisch; fehlende Daten nicht erfinden. |
| `/mindmap` | Strukturiere ein Thema als Zentrum, Hauptäste und Unteräste. Nicht mit dem account-/skillabhängigen UI-Shortcut `/mindmaps` gleichsetzen. |

## Ideen und Content

| Shortcut | KI-Regeln-Lesart |
|---|---|
| `/hooks10` | Erzeuge mehrere unterschiedliche Hooks und variiere Mechanik, Ton und Informationsversprechen statt nur Formulierungen. |
| `/angles` | Betrachte dasselbe Thema aus mehreren echten Perspektiven, zum Beispiel Fehler, Mythos, Zahl, Geschichte, Gegenposition oder Praxisfall. |
| `/series` | Entwickle aus einer Kernidee eine kurze Serie mit eigenständigem Nutzen pro Folge und nachvollziehbarer Reihenfolge. |
| `/repurpose` | Übertrage einen vorhandenen Inhalt in mehrere Formate, ohne Claims oder Quellen beim Formatwechsel zu verändern. |
| `/carousel` | Plane ein Content-Karussell als Folgensequenz. Bei Bildarbeit kann derselbe Shortcut visuelle Slides meinen; Kontext entscheidet. |
| `/caption` | Schreibe eine plattformgerechte Caption mit Hook, Kerninhalt und passendem CTA, ohne Clickbait-Versprechen zu erfinden. |
| `/objections` | Sammle plausible Einwände einer Zielgruppe und beantworte sie sachlich; keine künstlichen Probleme oder falschen Garantien erzeugen. |
| `/contentplan` | Baue einen Editorialplan aus Ziel, Audience, Themenclustern, Formaten und Frequenz; nicht bloß 30 austauschbare Posts erzeugen. |
| `/scamper` | Nutze SCAMPER als Kreativheuristik für Ersetzen, Kombinieren, Anpassen, Modifizieren, Umnutzen, Entfernen und Umkehren. |
| `/niche` | Schneide ein breites Thema in spezifischere Zielgruppen-/Problemfelder und nenne Nutzen sowie Grenzen der jeweiligen Zuspitzung. |

## Analysieren und Entscheiden

| Shortcut | KI-Regeln-Lesart |
|---|---|
| `/swot` | Strukturiere interne Stärken/Schwächen und externe Chancen/Risiken; Beobachtung und Annahme auseinanderhalten. |
| `/riskmap` | Ordne Risiken nach Eintrittswahrscheinlichkeit und Auswirkung; Unsicherheit und fehlende Daten explizit lassen. |
| `/compare` | Vergleiche Optionen nach vorab benannten Kriterien auf gleicher Datenbasis. |
| `/tradeoffs` | Zeige pro Option, was gewonnen, aufgegeben oder riskanter wird, statt eine scheinbar kostenlose beste Lösung zu behaupten. |
| `/regret` | Nutze Regret-Minimization als zusätzliche Entscheidungslinse, nicht als alleinige Entscheidungsregel. |
| `/counter` | Formuliere das stärkste vernünftige Gegenargument zur Ausgangsthese; funktional nahe an `/steelman`. |
| `/blindspots` | Suche übersehene Annahmen, Stakeholder, Abhängigkeiten, Nebenwirkungen und Informationslücken. |
| `/numbers` | Rechne eine Entscheidung mit expliziten Zahlen, Annahmen und Sensitivitäten durch; fehlende Werte nicht durch Scheingenauigkeit ersetzen. |
| `/ooda` | Strukturiere eine dynamische Lage in Beobachten, Einordnen, Entscheiden und Handeln; nach neuem Feedback erneut iterieren. |
| `/criteria` | Definiere Kriterien und Gewichtung vor der Bewertung, damit das Ergebnis nicht nachträglich an die Lieblingsoption angepasst wird. |

## Denksysteme und Problemlösung

| Shortcut | KI-Regeln-Lesart |
|---|---|
| `/lenses` | Betrachte ein Problem durch mehrere relevante Perspektiven, etwa Geld, Menschen, Zeit, Technik oder Risiko; Linsen an die Aufgabe anpassen. |
| `/blackswan` | Suche nach übersehenen Tail-Risks und fragilen Annahmen mit hoher Auswirkung; echte Black Swans lassen sich per Definition nicht vollständig vorhersagen. |
| `/systemmap` | Mappe Akteure, Ressourcen, Kräfte, Rückkopplungen und Abhängigkeiten eines Systems. |
| `/meta` | Prüfe vor der Lösung, ob Frage, Ziel, Messgröße oder Problemrahmen überhaupt passend gewählt sind. |
| `/reverseengineer` | Arbeite von beobachtetem Ergebnis rückwärts zu wahrscheinlichen Bestandteilen und Entscheidungen; bei fremden Systemen Rechte/Autorisierung beachten. |
| `/hypotheses` | Formuliere mehrere konkurrierende Erklärungen und jeweils eine Beobachtung oder einen Test, der zwischen ihnen unterscheiden kann. |
| `/paradox` | Suche echte Spannungen oder widersprüchliche Annahmen und erkläre, ob sie auflösbar, kontextabhängig oder fundamental sind. |
| `/fractal` | Betrachte dasselbe Problem auf mehreren Ebenen vom Gesamtsystem bis zum konkreten Detail und prüfe, ob Aussagen skalenabhängig sind. |
| `/bottleneck` | Identifiziere den aktuell begrenzenden Engpass anhand von Evidence und prüfe, ob seine Entlastung tatsächlich den Gesamtdurchsatz erhöht. |
| `/leverage` | Suche nach dem Hebel mit hohem erwarteten Nutzen pro zusätzlicher Ressource; Nebenwirkungen und Abhängigkeiten mitbewerten. |

## Kreativ und Zukunft

| Shortcut | KI-Regeln-Lesart |
|---|---|
| `/predict` | Skizziere plausible Entwicklungen aus aktuellem Wissen mit Annahmen, Szenarien und Unsicherheit statt eine sichere Zukunft vorherzusagen. |
| `/futurehistory` | Schreibe ein ausdrücklich spekulatives Zukunftsszenario rückblickend als Geschichte, ohne Fiktion als Prognose auszugeben. |
| `/roleplay` | Simuliere ein Gespräch oder Gegenüber zum Üben; bei realen Personen keine private Kenntnis oder tatsächliche Haltung vortäuschen. |
| `/whatif` | Ändere gezielt eine Annahme und verfolge die plausiblen Folgen, inklusive Zweit- und Drittrundeneffekten. |
| `/storyboard` | Plane Szenen, Bildinhalt, Text/Voice und grobes Timing. Für echte Medienproduktion anschließend geeignete Bild-/Video-Workflows verwenden. |
| `/worldbuild` | Entwickle Weltregeln, Orte, Fraktionen und Figuren mit interner Konsistenz und klaren Grenzen. |
| `/villain` | Erzähle eine vorhandene Geschichte aus Sicht einer Gegenfigur, ohne automatisch ihre moralische Bewertung zu übernehmen. |
| `/twist` | Erzeuge mehrere Wendungsoptionen, die aus vorhandenen Motiven vorbereitet werden können statt nur zufällig zu überraschen. |
| `/dialog` | Schreibe ein Gespräch zwischen Rollen/Figuren mit unterscheidbaren Zielen und Stimmen; reale Personen nicht als Quelle privater Aussagen behandeln. |
| `/namegen` | Erzeuge mehrere Namensrichtungen mit kurzer Begründung und prüfe auf offensichtliche Verwechslungs-/Markenrisiken nur, wenn entsprechende Recherche vorliegt. |

## Coding und Technik

| Shortcut | KI-Regeln-Lesart |
|---|---|
| `/debug` | Analysiere Fehlerbild, reproduzierbare Ursache und kleinsten sinnvollen Fix; nicht nur die Fehlermeldung paraphrasieren. |
| `/explaincode` | Erkläre Code nach Struktur, Datenfluss und kritischen Stellen; Zeile-für-Zeile nur, wenn das wirklich hilft. |
| `/refactor` | Verbessere Struktur oder Lesbarkeit bei beabsichtigt unverändertem Verhalten und sichere relevante Regressionen durch Tests. |
| `/regex` | Erzeuge einen regulären Ausdruck mit Annahmen, Beispielen, Grenzen und gegebenenfalls engine-spezifischen Besonderheiten. |
| `/excel` | Formuliere passende Excel-/Spreadsheet-Formel anhand der tatsächlichen Tabellenstruktur und Locale-Konventionen. |
| `/tests` | Entwirf Tests für relevantes Verhalten, Grenzfälle und Regressionen; Testcode beweist noch keinen ausgeführten Pass. |
| `/sql` | Übersetze eine fachliche Datenfrage in SQL nur gegen bekanntes Schema/Dialekt oder markiere notwendige Annahmen. |
| `/comment` | Ergänze Kommentare dort, wo Intent, Randbedingung oder nicht offensichtliche Entscheidung erklärt werden muss; offensichtlichen Code nicht nacherzählen. |
| `/security` | Führe einen begrenzten Security-Review des vorliegenden Codes durch und benenne Scope, Evidence und offene Prüfungen; kein Anspruch auf vollständige Schwachstellenfreiheit. |
| `/shortcut` | Plane einen iPhone-/Mac-Kurzbefehl beziehungsweise Automationsablauf schrittweise; konkrete Aktionen und UI können versionsabhängig sein. |

## Alltag und Planung

| Shortcut | KI-Regeln-Lesart |
|---|---|
| `/convert` | Wandle Einheiten, Mengen oder Formate mit nachvollziehbarer Rechnung um; bei aktuellen Währungen echte FX-Daten verwenden. |
| `/budget` | Erstelle aus angegebenen Einnahmen, Fixkosten, variablen Kosten und Zielwerten einen transparenten Haushaltsplan mit Annahmen. |
| `/mealplan` | Plane Mahlzeiten anhand genannter Präferenzen, Zeit und Budget; medizinische Diätanforderungen nicht ungeprüft ableiten. |
| `/negotiate` | Entwirf eine Verhandlungsstrategie mit Ziel, Interessen, Argumenten, Alternativen und Rückzugspunkt. |
| `/complaint` | Formuliere eine sachliche Beschwerde mit überprüfbaren Fakten, gewünschter Lösung und nur tatsächlich begründeten Fristen. |
| `/travel` | Entwirf einen Reiseplan aus Interessen, Zeit und Budget; aktuelle Öffnungszeiten, Preise, Verbindungen und lokale Fakten bei Bedarf live prüfen. |
| `/workout` | Entwirf ein Trainingsgerüst aus Ziel, Zeit, Material und Erfahrung; medizinische Einschränkungen nicht diagnostizieren oder übergehen. |
| `/habit` | Zerlege eine Gewohnheit in kleine, beobachtbare Schritte, Trigger und einfache Rückkehrstrategie nach Aussetzern. |
| `/inbox` | Sortiere eine To-do-Liste nach Dringlichkeit, Wichtigkeit, Abhängigkeiten und nächstem konkreten Schritt. |
| `/godmode` | Erzeuge einen umfassenden ersten Entwurf mit sinnvollen Annahmen statt unnötiger Rückfragen; fehlende Pflichtinformationen, Rechte- oder Sicherheitsgates dürfen dadurch nicht übersprungen werden. |

## Routing zu KI-Regeln

Die Shortcuts sind Bedienkürzel. Bei anspruchsvolleren Aufgaben übernehmen die zuständigen Disziplinen:

```text
/polish /voice /active /dejargon /rhythm
→ Schreiben-Skills

/gaps /roadmap /teachback /cheatsheet
→ Lern-/Recherchekontext

/swot /riskmap /compare /criteria /numbers
→ Analyse-/Entscheidungsworkflow

/storyboard /carousel /repurpose
→ Social-Media-/Content- bzw. Medienworkflow

/debug /refactor /tests /security /sql
→ Coding-, Testing-, Security- oder Datenbank-Skills

/travel /budget /workout /mealplan
→ domänenspezifische Regeln + aktuelle/geeignete Datenquellen
```

## Leitgedanke

> Ein gutes Kürzel spart Wörter. Gute Arbeit braucht trotzdem Kontext, Evidence und die richtige Fachdisziplin.
