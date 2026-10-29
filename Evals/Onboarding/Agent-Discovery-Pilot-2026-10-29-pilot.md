Die folgende Orientierung stützt sich ausschließlich auf den von dir eingefügten **AGENTS.md-Text**. Snapshotdateien konnte ich nicht lesen; daher kann ich keine tatsächlich gelesenen Dateifundstellen daraus nennen.

**1. Einen neuen Skill beitragen**

Beginne mit `Dokumentation/Skill-Handbuch.md`, prüfe `skill-catalog.yml` und `routing-overlays.yml`; bei einem passenden mehrphasigen Prozess zusätzlich `workflow-index.yml` und den jeweiligen Workflow. Daraus sind die konkreten Beitrags- und Prüfanweisungen zu ermitteln.

Belegt sind bereits: Description und fachliche Abgrenzung, `maturity`, `eval_coverage`, `capabilities`, `related` und Skill-Frontmatter beachten; keine Maturity ohne Evidence hochstufen; bei extern übernommenen Skills Provenance und Lizenzlage prüfen. Repositoryprüfungen sollen später über den lokalen Validation Harness erfolgen.

Fundstellen im bereitgestellten `AGENTS.md`: „Routing“, Punkte 3–5 und 8; „Repository-Validierung“; „Harte Grenzen“. **Der konkrete Beitragsprozess und seine vollständige Checkliste bleiben mangels lesbarer Folgequellen ungeprüft.**

**2. Externer MCP-Server mit zusätzlichen Rechten**

Ja, mitgelieferte Skills ändern den Prüfweg:

- **Eigenständiger MCP-Server:** Baseline aus `Sicherheit/MCP-und-externe-Tools.md`; `tool-permission-review` für Capability- und Rechteumfang. `prompt-injection-review` nur bei tatsächlich instruktionshaltigem oder verdächtigem untrusted Input.
- **Paket mit Skills:** Das gesamte Paket gilt als Skill-Bundle. `skill-security-review` übernimmt die Admission einschließlich Berechtigungsrisiken. `tool-permission-review` kommt zusätzlich hinzu, wenn das Berechtigungsdesign einen eigenständigen Prüfauftrag bildet.

Eine Verbindung oder verfügbare Capability autorisiert keine zusätzlichen Aktionen. Fundstellen: bereitgestelltes `AGENTS.md`, „Routing“, Punkte 9–10, sowie „Harte Grenzen“. **Die Sicherheitsbaseline und Skill-Details konnte ich nicht gegenlesen.**

**3. Nicht gelaufener Test und Abschlussmeldung**

**Nein, nicht pauschal als geprüft.** Ein Erfolgsclaim darf nur so weit reichen, wie frische Evidence ihn trägt. Den ausgefallenen Test mit Grund als `NOT RUN` und den betroffenen Prüfstatus als `UNVERIFIED` ausweisen. Tatsächlich durchgeführte andere Prüfungen dürfen separat genannt werden.

Beispiel: „Bearbeitung abgeschlossen; Test X: NOT RUN wegen [Grund]. Die damit geprüfte Eigenschaft bleibt UNVERIFIED.“

Fundstellen: bereitgestelltes `AGENTS.md`, „Repository-Validierung“ und „Harte Grenzen“, insbesondere „Keine Evals als bestanden darstellen, die nicht ausgeführt wurden“.

Die Ausführungsrichtlinie hat die reinen Lesebefehle mit „blocked by policy“ abgewiesen; eine lokale Lesealternative war nicht verfügbar. Ob die genannten Folgequellen im Snapshot fehlen, konnte ich deshalb nicht feststellen.