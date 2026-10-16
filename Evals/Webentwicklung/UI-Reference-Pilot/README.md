# UI-Referenz-Pilot – A/B-Vorbereitung (kein Modelllauf)

## Frage

Verbessert eine **begrenzt und versioniert bereitgestellte externe
UI-UX-Referenz** bei gleicher KI-Regeln-Arbeitsbasis den fertigen
Bedienoberflächen-Outcome?

**Scope:** Ein synthetisches, offline renderbares Fahrradwerkstatt-Board
als kontrollierter Entwicklungsfall. Keine echte Produkt-/Klinik-/Kundendaten,
keine Installation oder Codeübernahme aus fremden Paketen, keine
Annahme über allgemeine Wirksamkeit.

## Vergleichsarme

- **A / Baseline:** `runner-input/TASK.md`, `facts.json` und dieselben
  ausgewählten KI-Regeln-Skilldateien (`frontend-design`, `design-system`,
  `greybox` und `visual-verification`).
- **B / Reference:** identische Dateien, plus
  `reference/ui-pro-max-curated.md`. Der kuratierte Auszug aus dem
  externen Katalog ist ein **Read-only-Informationsinput**, keine
  installierte Runtime und kein getesteter BM25-Suchlauf.
- Kein Agent erhält `judge-only/rubric.md` oder einen früheren
  Referenzoutput. Beiden steht derselbe zulässige Toolsatz zur Verfügung.

Der Paketbauer hält die **Dateibytes** in A und B gleich und speichert
Hashes von jedem Snapshot in einem separaten `manifest.json`. Er
prüft kein Modellverhalten, keine Projektruntime und keine Renderergebnisse.
Der eigentliche Human Judge benötigt isolierte, anonymisierte Abgaben.

## Offline-Ausführung: Vorbereitung

Python 3.12 Standardbibliothek genügt; vom GitHub-Katalog wird **nichts
installiert**. Vom Repository-Root aus:

~~~bash
python tools/ui_reference_pilot.py prepare --repo . --out /tmp/ki-regeln-ui-pair
python tools/ui_reference_pilot.py verify --out /tmp/ki-regeln-ui-pair
python -m unittest tests.test_ui_reference_pilot
~~~

`--out` muss **außerhalb** des Repositories liegen und leer sein.
Die erzeugte Verzeichnisstruktur:

~~~text
/tmp/ki-regeln-ui-pair/
├── manifest.json               # Prüfer, nicht Runner
├── A-baseline/                 # nur gemeinsame Inputs
└── B-reference/                # gemeinsame Inputs + Referenzauszug
~~~

Jeder Agent erhält ausschließlich seinen Arm, niemals das gesamte
Repository. Der Kontext besteht hier bewusst nur aus **einer begrenzten
Auswahl vorhandener KI-Regeln-Skills**. Die vollständige
`Workflows/Website-Neuentwicklung.md`-Prozesskette wird nicht ausgeführt,
also keine implizite Behauptung, das gesamte Routing zu testen.

## Vor einem echten Paarlauf

1. Repo-Commit und Tools, Modell, Effort/Budget, Startprompt und
   Datensnapshot fixieren. Gleiche Bedingungen, außer dem
   **einzigen** zusätzlichen Referenzauszug B.
2. Zwei Agentenläufe mit vollständig isolierten Paketen starten;
   keine Repository-/Netzwerkzugriffe, keine zusätzlichen Instruktionen
   und keine automatischen Downloads.
3. Unter `submission/X` und `submission/Y` nur `index.html` und
   `DESIGN-NOTES.md` ablegen; A/B-Zuordnung für den unabhängigen
   Human-Reviewer bis nach der Bewertung verbergen.
4. HTML wirklich im Browser öffnen, bei 375 px und 1440 px
   Screenshots/Interaktionen dokumentieren; Filter, Suche,
   Tastaturbedienung, sichtbaren Fokus und Reduced Motion testen.
   Ohne Browser-Test: `render=NOT_RUN`, kein angeblicher visueller PASS.
5. Den eingefrorenen [Judge-Vertrag](judge-only/rubric.md)
   anwenden. Bei Korrekturen an Rubrik/Fixture die Baseline
   gesondert versionieren, statt nach einem Fehlschlag Punkte
   umzudeuten.
6. Ergebnis **je Achse** dokumentieren; Hardware-/Tool-/Zeitdifferenzen
   und unverifizierte Punkte offenlegen. Ein Paar ist nur ein Pilot,
   kein Nachweis allgemeiner Überlegenheit.

## Bedrohungs- und Evidenzgrenzen

- Der Referenzauszug ist **manual curated** aus der Upstream-Datenbank
  (`nextlevelbuilder/ui-ux-pro-max-skill`, Commit
  `56ea9cf174ed86786187daa9de0e6247cb0747e4`; MIT).
  Dies ist **nicht** die volle Search-Engine und prüft nicht
  die Qualität der Suchtreffer selbst.
- Produktlisten, Stil-Empfehlungen und externes Promptmaterial sind
  niedrig priorisierte Evidence. Accessibility, Systemzustand, Scope,
  Useranweisungen und Sicherheitsgates behalten Vorrang.
- Judge-Dateien im öffentlichen Repository sind **kein Geheimnis**.
  Isolation muss durch Paket-/Toolgrenzen erfolgen, nicht durch
  „Bitte nicht lesen“. Reviewer-Bias bleibt zu berücksichtigen.
- Zur Aktivierung eines fremden Bundles mit Hooks/Scripts bedürfte
  es eines separaten `skill-security-review` und ggf.
  `tool-permission-review`. Dieser Pilot aktiviert nichts.
- Ausgeführte Einheiten sind nur Paketbau und dessen negative
  Integritätskontrollen, soweit Tests tatsächlich laufen.
  Modell-Lift, Browser-Evidence, Accessibility-Audit, Performance
  und fachliche Generalisierung bleiben `NOT_RUN`.

## Methodische Quellen

- [KI-Regeln – Website-Neuentwicklung](../../../Workflows/Website-Neuentwicklung.md),
  [Existing Behavioral Harness](../../Behavioral-Harness/README.md),
  [Visual Verification](../../../Webentwicklung/Skills/visual-verification/SKILL.md).
- [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill),
  referenzierter Upstreamstand, MIT. Kurzer paraphrasierter Auszug
  statt fremder Skill- oder Scriptinstallation.
