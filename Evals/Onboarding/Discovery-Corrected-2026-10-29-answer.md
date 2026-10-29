**1. Einen neuen Skill beitragen**

Beginne bei [CONTRIBUTING.md, „Skills, Workflows und Evals“, Z. 30](https://github.com/Borstwerk/KI-Regeln/blob/211048868a4fc713710450c3c4d3ff17a0923698/CONTRIBUTING.md#L30) und [Skill-Engineering/README.md, „Einstieg nach Arbeitsfrage“, Z. 5](https://github.com/Borstwerk/KI-Regeln/blob/211048868a4fc713710450c3c4d3ff17a0923698/Skill-Engineering/README.md#L5). Kläre zuerst den wiederverwendbaren Bedarf und ob ein vorhandener Skill bereits genügt.

Zur Prüfung gehören:

- klare Verantwortung, Description, positive Trigger und Near-Misses;
- Inputs, Outputs, Evidence, Stop-Regeln, minimale Rechte und Fallbacks;
- unabhängiger fachlicher Review sowie Trigger-, Behavior-, Outcome- und Regression-Evals; bei Sicherheitswirkung zusätzlich Security-Review;
- konsistenter Katalog-/Evalstand, belegte Maturity und bei Fremdmaterial geklärte Provenance und Lizenz.

Fundstellen: [skill-authoring/SKILL.md, Ablauf ab Z. 12](https://github.com/Borstwerk/KI-Regeln/blob/211048868a4fc713710450c3c4d3ff17a0923698/Skill-Engineering/Skills/skill-authoring/SKILL.md#L12), [Skill-Review-und-Evals.md, Review-Achsen und Eval-Klassen ab Z. 22](https://github.com/Borstwerk/KI-Regeln/blob/211048868a4fc713710450c3c4d3ff17a0923698/Skill-Engineering/Skill-Review-und-Evals.md#L22). Neue Skills starten standardmäßig `experimental`. Der Beitragsweg führt über einen engen Branch, passende lokale Validierung und einen PR nach `main`; siehe [CONTRIBUTING.md, Z. 5](https://github.com/Borstwerk/KI-Regeln/blob/211048868a4fc713710450c3c4d3ff17a0923698/CONTRIBUTING.md#L5). Das Validation Harness führt **keine Behavioral Evals** aus: [Local-Validation-Harness.md, Z. 27](https://github.com/Borstwerk/KI-Regeln/blob/211048868a4fc713710450c3c4d3ff17a0923698/Dokumentation/Local-Validation-Harness.md#L27).

**2. Externen MCP-Server mit zusätzlichen Rechten verwenden**

**Ja, mitgelieferte Skills ändern den Prüfweg.**

- **Ohne Skills:** Die Baseline aus [Sicherheit/MCP-und-externe-Tools.md, „Ownership nach Objekttyp“, Z. 7](https://github.com/Borstwerk/KI-Regeln/blob/211048868a4fc713710450c3c4d3ff17a0923698/Sicherheit/MCP-und-externe-Tools.md#L7) gilt; `tool-permission-review` prüft die zusätzlichen Rechte. Dazu gehören Zweck, minimale Rechte, Datenfluss, Außenwirkung, Fallbacks und Gates. Deklarierte Rechte, technische Durchsetzung und konkrete Autorisierung sind getrennt zu bewerten: [tool-permission-review/SKILL.md, Z. 42](https://github.com/Borstwerk/KI-Regeln/blob/211048868a4fc713710450c3c4d3ff17a0923698/Sicherheit/Skills/tool-permission-review/SKILL.md#L42).
- **Mit mindestens einer `SKILL.md`:** Das gesamte Paket gilt als Skill-Bundle. `skill-security-review` übernimmt die Admission einschließlich MCP-, Hook- und Script-Dateien sowie Berechtigungsrisiken. Ein zusätzlicher Permission-Review ist nur für einen eigenständigen Prüfauftrag zum Berechtigungsdesign nötig: [AGENTS.md, Routing-Schritt 10, Z. 84](https://github.com/Borstwerk/KI-Regeln/blob/211048868a4fc713710450c3c4d3ff17a0923698/AGENTS.md#L84).

`prompt-injection-review` kommt bei einer tatsächlich vorhandenen verdächtigen beziehungsweise instruktionshaltigen Quelle als eigenständigem Prüfjob hinzu. Toolverfügbarkeit oder bestehende Verbindung autorisieren keine Außenaktion.

**3. Nicht gelaufenen Test als geprüft melden**

**Nein, soweit der Abschlussclaim diesen Test voraussetzt.** Melde `NOT RUN` mit Grund, bei fehlenden Voraussetzungen gegebenenfalls `BLOCKED`; nicht belastbare Ergebnisse bleiben `UNVERIFIED`. Tatsächlich bestandene Teilprüfungen darfst du einzeln nennen, aber nicht zur Gesamtfreigabe hochrechnen.

Belege: [AGENTS.md, „Harte Grenzen“, Z. 134](https://github.com/Borstwerk/KI-Regeln/blob/211048868a4fc713710450c3c4d3ff17a0923698/AGENTS.md#L134) verlangt frische Evidence für genau den behaupteten Zustand; [Umgebungsabhaengige-Verifikation-und-Reports.md, Statussemantik ab Z. 30](https://github.com/Borstwerk/KI-Regeln/blob/211048868a4fc713710450c3c4d3ff17a0923698/Testing-und-QA/Umgebungsabhaengige-Verifikation-und-Reports.md#L30) untersagt die Hochrechnung fehlender Pflichtchecks. Passende Formulierung: „Bearbeitung abgeschlossen; Test X: NOT RUN wegen Y; die betroffene Eigenschaft bleibt unverifiziert.“

Die benötigten Regelquellen waren vorhanden. Für diese Orientierung wurden ausschließlich Dateien gelesen und gezielt durchsucht.