Die lokalen Lesebefehle wurden durch die Laufzeitrichtlinie blockiert. Deshalb kann ich nur den von dir eingeblendeten Inhalt von `AGENTS.md` belegen. Die übrigen Quellen sind **nicht gelesen**; ob sie fehlen, konnte ich nicht feststellen.

1. **Neuen Skill beitragen**

   Beginne mit `Dokumentation/Skill-Handbuch.md`, prüfe `skill-catalog.yml` und `routing-overlays.yml`; bei einem plausiblen mehrphasigen Ablauf zusätzlich `workflow-index.yml` und den passenden Workflow. Danach sind die benötigten `SKILL.md`-Dateien auszuwählen.

   Zur Prüfung gehören laut Bootstrap mindestens Scope und Zuständigkeit, `maturity`, `eval_coverage`, `capabilities`, `related` sowie Skill-Frontmatter. Für externe Skills kommen Provenance und Lizenzlage hinzu. Maturity darf nicht aus Plausibilität oder wenigen Beispielen hochgestuft werden. Repository-Änderungen sollen später mit dem lokalen Validation Harness geprüft werden.

   **Fundstellen:** bereitgestellte `AGENTS.md`, „Routing“, Schritte 3–8; „Repository-Validierung“; „Harte Grenzen“. Einen konkreten Beitragsleitfaden oder dessen vollständige Prüfliste konnte ich mangels Dateizugriff **nicht verifizieren**.

2. **Externen MCP-Server mit zusätzlichen Rechten verwenden**

   **Ja, mitgelieferte Skills ändern den Prüfweg.** Für einen eigenständigen MCP-Server gilt die Baseline aus `Sicherheit/MCP-und-externe-Tools.md`: `tool-permission-review` prüft Capability- und Rechteumfang. `prompt-injection-review` kommt bei tatsächlich instruktionshaltigem oder verdächtigem untrusted Input hinzu.

   Liefert das Paket Skills mit, wird es insgesamt als **Skill-Bundle** behandelt: `skill-security-review` übernimmt die Admission einschließlich Berechtigungsrisiken. `tool-permission-review` ist zusätzlich nötig, wenn das Berechtigungsdesign einen eigenständigen Prüfauftrag bildet. Toolverfügbarkeit oder eine bestehende Verbindung erteilen keine Autorisierung für Außenaktionen.

   **Fundstellen:** bereitgestellte `AGENTS.md`, „Routing“, Schritte 8–10; „Harte Grenzen“. Die MCP-Baseline und die genannten Skill-Dateien konnte ich nicht öffnen; konkrete zusätzliche Anforderungen bleiben daher ungeprüft.

3. **Nicht gelaufenen Test als geprüft melden**

   **Nein, nicht hinsichtlich dieses Tests.** Kennzeichne ihn als `NOT RUN`; bleibt dadurch eine relevante Aussage unbelegt, als `UNVERIFIED` beziehungsweise bei tatsächlicher Blockade `BLOCKED`. Bereits ausgeführte Prüfungen dürfen mit ihrem konkreten Umfang genannt werden. Ein pauschales PASS oder „vollständig geprüft“ wäre ohne passende frische Evidence unzulässig.

   Beispiel: „Bearbeitung abgeschlossen; Test X: NOT RUN wegen …; die davon abhängige Eigenschaft bleibt UNVERIFIED.“

   **Fundstellen:** bereitgestellte `AGENTS.md`, „Repository-Validierung“ und „Harte Grenzen“, insbesondere „Keine Evals als bestanden darstellen, die nicht ausgeführt wurden“ und die Beschränkung von Erfolgsclaims auf frische Evidence.