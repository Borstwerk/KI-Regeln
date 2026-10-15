# Öffentliche Einstiege und Sprachpflege

## Ziel

KI-Regeln trennt öffentliche Orientierung für Menschen von verbindlichen Agentenregeln. Die Dokumentation soll für Außenstehende rasch erfassbar und für Agenten mit **wenigen kanonischen Quellen** pflegbar bleiben. Dieses Dokument ist die Pflegeanleitung, **keine neue Routing-Wahrheit**.

## Dokumentverantwortung

| Datei | Publikum / Rolle | Kanonisch für |
| --- | --- | --- |
| [README.md](../README.md) | internationale GitHub-Besucher | kurze englische Positionierung, sichtbare Einstiege und Lizenzhinweise |
| [START-HIER.md](../START-HIER.md) | Menschen, Deutsch | nutzbarer deutscher Schnellstart |
| [START-HERE.md](../START-HERE.md) | Menschen, Englisch | nutzbarer englischer Schnellstart |
| [AGENTS.md](../AGENTS.md) | KI-Agenten, technisch | **einziger verbindlicher Bootstrap und die Agenten-Discovery-Gates** |
| [Skill-Handbuch.md](Skill-Handbuch.md) + [skill-catalog.yml](../skill-catalog.yml) | Agenten / Fachnutzer | konkrete Skill-Auswahl, Reife, Capabilities und Routing |
| [workflow-index.yml](../workflow-index.yml) + [routing-overlays.yml](../routing-overlays.yml) | Agenten | Workflow-Inventar bzw. Cross-Cutting-Discovery |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | Maintainer | Beitrags- und Reviewprozesse |
| [ASSET-LICENSES.md](../ASSET-LICENSES.md) + [open-source-readiness.yml](open-source-readiness.yml) | Wiederverwendung / Release | Ausnahmen, Assets und Release-Gates |

Eine menschliche Übersetzung darf **niemals** als Ersatz für `AGENTS.md`, Katalog, Workflow-Index oder projektspezifische Quellen ausgegeben werden. Deutsch ist derzeit die technische Dokumentationssprache. Nicht alle Fachdateien sind übersetzt; englische Einstiege verlinken deswegen ausdrücklich auf deutsche Detaildokumente.

## Pflege bei Änderungen – für Menschen und Agenten

1. **Änderungsgegenstand prüfen:** Geht es um Projektpositionierung, Einstieg, technischen Ablauf, Skill-Routing oder externe Lizenzen? Zuständige kanonische Datei zuerst lesen.
2. **Nur die betroffenen Einstiege aktualisieren:** Neue Skills und normale Codeänderungen müssen nicht automatisch in beiden Schnellstarts erwähnt werden. Keine automatisch generierten vollständigen Übersetzungen des Repositories.
3. **Wenn Quickstart-Inhalte betroffen sind:** `START-HIER.md` und `START-HERE.md` **inhaltlich** vergleichen. Fachliche Aussage, Voraussetzungen, Rechte, Begrenzungen und Links gleichwertig halten. Natürliche Sprache bevorzugen, nicht wortgetreu duplizieren.
4. **Wenn die öffentliche Positionierung betroffen ist:** `README.md` knapp halten und die beiden Sprachpfade erhalten; Details in vorhandene Handbücher verlinken. Keine falschen Aussagen über Echtzeit-Ausführung, unabhängige Evaluation oder öffentliche Freigabe.
5. **Bei Lizenz-/Reuse-Aussagen:** `LICENSE`, `ASSET-LICENSES.md`, `REUSE.toml`, `THIRD-PARTY-NOTICES.md` und `open-source-readiness.yml` gegenprüfen. Eine öffentliche englische Paraphrase verändert niemals die Lizenz.
6. **Tests und Review:** `python -m unittest tests.test_public_entrypoints` und `python tools/check_public_entrypoints.py` oder den vorhandenen Repo-Validierungslauf ausführen. Fachliche Übersetzungsqualität, Lesbarkeit und Lizenzformulierungen zusätzlich **menschlich oder durch getrenntes semantisches Review** kontrollieren.

## Was automatisch geprüft wird

- Dateien vorhanden, H1 vorhanden, gegenseitige DE/EN-Links und zentrale Zielgruppen-/Reuse-Links vorhanden.
- Lokale Markdown-Datei-/Verzeichnisziele auf Existenz geprüft (keine Netzwerkanfrage, kein Browser). Relative Links dürfen das Repository nicht verlassen.
- `README.md` bleibt bewusst kompakt (maximal 8.500 Bytes).

**Nicht automatisch geprüft:** Sprachqualität, semantische Äquivalenz, inhaltliche Aktualität externer Webseiten, Markdown-Fragment-Anker, echte Agentenausführung, Browserdarstellung, Security oder Releasefreigabe. Diese Grenzen in PR-Berichten offenlassen.

## Wartungssignale statt blindem Auto-Sync

| Änderung | Zu prüfen |
| --- | --- |
| Öffentliche Projektpositionierung / neue Zielgruppe | README; ob beide Quickstarts angepasst werden müssen |
| Anwendung oder Erstzugang verändert | beide Quickstarts; Zugangs- und Capability-Grenzen |
| Agenten-Routing oder Agentengates verändert | ausschließlich kanonische Agentendateien + Tests; gegebenenfalls menschliche Verweise, **keine** Übersetzung der Gates |
| Lizenz, Provenance, Media-Reuse verändert | maßgebliche Lizenz-/Readiness-Dateien; öffentliche Kurzbeschreibung |
| Neuer Skill, Eval oder Workflow | kanonische Registry / betroffene Fachreferenz; Quickstarts nur bei tatsächlich verändertem Nutzerweg |

## Kaltlese-Regressionsprüfung

Bei wesentlichen Änderungen am öffentlichen Einstieg den begrenzten [Onboarding-Kaltlesetest](../Evals/Onboarding/README.md) als Review-Protokoll verwenden. Automatische Link- und Strukturtests sind wichtig, ersetzen aber weder einen unvoreingenommenen Menschen noch einen tatsächlich isolierten frischen Modelllauf. Statische Dokumentenprüfung und Live-Erprobung müssen separat ausgewiesen werden.

## Pflegeprinzip

> **Eine technische Wahrheit; zwei menschliche Sprachen; möglichst wenig doppelt gepflegter Text.**
