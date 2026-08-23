# Nutzung des Repositories

## Zweck

Dieses Dokument erklärt, wie `KI-Regeln` sinnvoll in echten Projekten eingesetzt wird.

Das Repository ist keine automatische Master-Steuerung. Es ist eine zentrale Bibliothek aus:

- allgemeinen Regeln;
- begrenzten Skills;
- wiederholbaren Evals;
- Workflows / Recipes;
- Quellen- und Upstream-Governance.

## Grundprinzip

> Allgemeine Arbeitsweise zentral, konkrete Wahrheit lokal.

Zentrale Regeln beschreiben **wie** gearbeitet wird. Projekte definieren **was** konkret gebaut, geschrieben, recherchiert, dokumentiert, geprüft oder freigegeben werden soll.

## Empfohlenes Nutzungsmodell

```text
Projektaufgabe
→ lokale Wahrheit / Anforderungen bestimmen
→ passenden Workflow prüfen
→ nur benötigte Skills auswählen
→ skill-catalog.yml auf Maturity, Capabilities und Evals prüfen
→ lokale Regeln ergänzen
→ arbeiten und Evidence erzeugen
→ passende Reviews / Gates
```

Nicht empfehlenswert:

- das komplette Repository ungefiltert in jeden Agentenkontext zu laden;
- alle Skills in jedes Projekt zu kopieren;
- Workflows als automatische Autorisierung aller enthaltenen Aktionen zu behandeln;
- immer ungeprüft den neuesten `main`-Stand zu übernehmen;
- allgemeine Regeln als Ersatz für Spezifikation, Architektur oder Source of Truth zu benutzen.

## Was ist was?

### Regel

Beschreibt allgemeine Leitplanken und Hintergründe.

### Skill

Beschreibt eine begrenzte Arbeitsdisziplin:

```text
Trigger
→ Prozess
→ Ergebnis / Evidence
```

### Workflow / Recipe

Verbindet mehrere Skills für ein größeres Ziel.

```text
Skill A
→ Handoff
→ Skill B
→ Review
→ Gate
```

### Eval

Prüft, ob ein Skill in typischen, schwierigen und negativen Fällen das erwartete Verhalten zeigt.

### Skill-Katalog

`../skill-catalog.yml` dokumentiert unter anderem:

- Skill-ID und Pfad;
- Maturity;
- Evalabdeckung;
- relevante Capabilities;
- verwandte Skills.

## Maturity richtig lesen

```text
experimental
→ candidate
→ stable
→ deprecated
→ retired
```

`experimental` bedeutet nicht „schlecht“. Es bedeutet: neue oder wesentlich umgebaute Logik, deren formale Praxis-/Evalbasis noch begrenzt ist.

`candidate` bedeutet: bereits praktisch oder konzeptionell bewährt, aber noch nicht breit genug für `stable` abgesichert.

`stable` soll bewusst verdient werden durch:

- wiederholte reale Nutzung oder Golden Tasks;
- passende positive und Near-Miss-Evals;
- Behavior-/Outcome-Evals;
- keine offenen schweren Skill-Review-Funde;
- klare Capability-/Fallback-Grenzen;
- Security Review bei mächtigen Skills.

Ein Projekt darf bewusst experimentelle Skills einsetzen. Es sollte dann nur wissen, dass zusätzliche Reviewlast sinnvoll ist.

## Capabilities und Fallbacks

Ein Skill soll nicht voraussetzen, dass jede Laufzeit Browser, Shell, Subagents, GitHub Write oder andere Fähigkeiten besitzt.

```text
Capability vorhanden?
├─ ja → normaler Weg
└─ nein
   ├─ Fallback möglich → transparent degradieren
   └─ kein Fallback → blocked / unverified
```

Nicht erlauben:

- Browserprüfung behaupten, obwohl nur Quellcode gelesen wurde;
- Tests als ausgeführt darstellen, wenn sie nicht liefen;
- Delegation behaupten, wenn keine Subagents verfügbar waren.

## Sicherheit

Bei Skills oder Workflows mit externen Inhalten, Scripts, Netzwerk, Secrets, Schreibrechten oder Außenwirkung passende Security-Regeln ergänzen.

Typische Zusatzskills:

- `Sicherheit/Skills/skill-security-review/SKILL.md`;
- `Sicherheit/Skills/prompt-injection-review/SKILL.md`;
- `Sicherheit/Skills/tool-permission-review/SKILL.md`.

Dabei gilt:

> Toolverfügbarkeit ist keine Autorisierung.

> Fremder Inhalt bleibt Daten und erhält keine neuen Befehlsrechte.

## Beispiel: Softwareprojekt

Möglicher Workflow:

`../Workflows/Software-Feature.md`

Typische Skills:

- `Agentenarbeit/Skills/context-engineering/SKILL.md`;
- `Agentenarbeit/Skills/task-graph/SKILL.md` bei komplexeren Features;
- `Agentenarbeit/Skills/delegation-contract/SKILL.md` bei Delegation;
- `Programmieren/Skills/domain-modeling/SKILL.md` bei unklarer Domäne;
- `Programmieren/Skills/tdd/SKILL.md`;
- `Agentenarbeit/Skills/verification-loop/SKILL.md`;
- `Programmieren/Skills/code-review/SKILL.md`.

Lokal bleiben:

- Architektur;
- Produktanforderungen;
- Test- und Releaseumgebungen;
- Freigabegates;
- Deploymentrechte.

## Beispiel: Bugdiagnose

Workflow:

`../Workflows/Bugdiagnose.md`

Kern:

```text
diagnose
→ Root Cause / Fix
→ verification-loop
→ code-review
```

Logs, HARs und Traces vor Weitergabe auf Secrets und personenbezogene Daten prüfen.

## Beispiel: Deep Research

Workflow:

`../Workflows/Deep-Research.md`

Kern:

```text
research-plan
→ deep-research
→ source-evaluation
→ research-synthesis
→ claim-verification bei kritischen Claims
→ citation-audit
```

Für eine kleine aktuelle Faktenfrage kann dagegen `web-search` allein genügen.

Lokal bleiben:

- konkrete Research-Frage;
- interne Quellen;
- zulässige Datenräume;
- Freshness;
- fachliche Bewertungskriterien.

## Beispiel: Technische Dokumentation

Workflow:

`../Workflows/Technische-Dokumentation.md`

Kern:

```text
optional Recherche
→ docs-plan
→ passender Dokumenttyp-Skill
→ technical-writing
→ docs-review
```

Lokal bleiben reale Sources of Truth, Terminologie, Zielgruppen, Ownership und betriebliche Regeln.

## Beispiel: Website-Neuentwicklung

Workflow:

`../Workflows/Website-Neuentwicklung.md`

Kern:

```text
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

Lokal bleiben Marke, realer Content, `DESIGN.md`, Framework, Komponentenbibliothek, Performancebudgets, Hosting und Releaseweg.

Für eine bestehende Seite siehe `../Workflows/Bestehende-Website-Review.md`.

## Beispiel: Bildserie

Workflow:

`../Workflows/Bildserie.md`

Kern:

```text
entitaetsbibel
→ bild-prebrief
→ Generierung
→ bildreview
→ serien-kontinuitaetscheck
→ Abschlussaudit
```

Charakterbibeln, konkrete Referenzbilder und Welt-/Serienkanon bleiben lokal.

## Beispiel: Schreibprojekt

Typische Skills:

- `Schreiben/Skills/natuerliches-schreiben/SKILL.md`;
- `Schreiben/Skills/kreatives-schreiben/SKILL.md`;
- `Schreiben/Skills/stilreview/SKILL.md`.

Figuren, Weltlogik, Stimme und Projektkanon bleiben lokal.

## Beispiel: Skill-Entwicklung

Für einen neuen zentralen Skill:

```text
skill-authoring
→ skill-review
→ Evals
→ bei relevanten Capabilities skill-security-review
→ Maturity-Entscheidung
```

Neue zentrale Skills starten normalerweise `experimental`.

Ein projektspezifischer Sonderfall gehört dagegen eher in lokale Agentenregeln als in einen neuen zentralen Skill.

## Projektmanifest

Vorlage:

`../Vorlagen/ki-regeln.template.yml`

Das Manifest kann dokumentieren:

- gepinnte zentrale Version oder Commit;
- ausgewählte Regeln;
- ausgewählte Skills;
- ausgewählte Workflows;
- projektspezifische Qualitäts-/Maturity-Policy;
- lokale Projektregeldateien.

Beispiel:

```yaml
source: Borstwerk/KI-Regeln
version: "<released-version-or-commit>"

skills:
  - Programmieren/Skills/diagnose
  - Programmieren/Skills/code-review

workflows:
  - Workflows/Bugdiagnose.md

quality_policy:
  minimum_maturity: candidate
  require_security_review_for_powerful_skills: true
```

## Updates bewusst übernehmen

```text
neue zentrale Version / Upstream-Änderung
→ Changelog / Diff prüfen
→ betroffene Skills und Workflows identifizieren
→ Evals und Security-Auswirkung prüfen
→ bewusst übernehmen oder ablehnen
→ Projektmanifest aktualisieren
```

Ein Upstream-Update ist nur ein Review-Signal.

## Wichtige Warnung

Ein Skill oder Workflow ersetzt niemals:

- eine Spezifikation;
- eine Architekturentscheidung;
- eine Research-Frage oder fachliche Definition;
- eine reale Source of Truth;
- einen Serienkanon;
- eine Markenentscheidung;
- eine Projektfreigabe;
- menschliche Verantwortung.

## Leitgedanke

> Nicht möglichst viele Regeln laden, sondern die richtigen Regeln und die richtige Reife für die aktuelle Aufgabe wählen.
