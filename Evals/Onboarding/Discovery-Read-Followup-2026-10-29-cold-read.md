1. **Neuen Skill beitragen**

Beginne bei [CONTRIBUTING.md, Z. 16–40](https://github.com/Borstwerk/KI-Regeln/blob/87320bb92b7ce2ed02ff8bd5a433d263ad5a4d6f/CONTRIBUTING.md#L16) und [Skill-Engineering/README.md, Z. 5–12](https://github.com/Borstwerk/KI-Regeln/blob/87320bb92b7ce2ed02ff8bd5a433d263ad5a4d6f/Skill-Engineering/README.md#L5). Zuerst einen wiederverwendbaren Bedarf und die Lücke gegenüber vorhandenen Skills belegen. Für den Entwurf ist `skill-authoring`, für den unabhängigen Qualitätsreview `skill-review` vorgesehen.

Zur Prüfung gehören Verantwortung und Abgrenzung, Trigger und Near-Misses, Inputs/Outputs samt Evidence, minimale Rechte und Fallbacks, Portabilität, Abhängigkeiten und Stop-Gates. Evals sollen positive und paraphrasierte Trigger, Near-Misses, fehlende Capabilities beziehungsweise Pflichtinformationen sowie schwierige Fälle abdecken. Fundstelle: [skill-review/SKILL.md, Z. 12–105](https://github.com/Borstwerk/KI-Regeln/blob/87320bb92b7ce2ed02ff8bd5a433d263ad5a4d6f/Skill-Engineering/Skills/skill-review/SKILL.md#L12).

Katalog und Evals konsistent pflegen; fehlende Coverage ausdrücklich begründen. Neue Skills starten standardmäßig `experimental`; relevante Sicherheitsfähigkeiten benötigen zusätzlich Sicherheitsreview. Später gehören passende Harness-Prüfungen, dokumentierte Ergebnisse und ein fachlich geprüfter PR dazu: [skill-authoring/SKILL.md, Z. 67–76](https://github.com/Borstwerk/KI-Regeln/blob/87320bb92b7ce2ed02ff8bd5a433d263ad5a4d6f/Skill-Engineering/Skills/skill-authoring/SKILL.md#L67), [CONTRIBUTING.md, Z. 5–12 und 44–52](https://github.com/Borstwerk/KI-Regeln/blob/87320bb92b7ce2ed02ff8bd5a433d263ad5a4d6f/CONTRIBUTING.md#L5). Bei fremden Bestandteilen Herkunft und Lizenz am verwendeten Stand klären.

2. **Externen MCP-Server mit zusätzlichen Rechten verwenden**

Ja, mitgelieferte Skills ändern den Prüfweg:

- **Ohne Skills:** Die MCP-Baseline gilt; `tool-permission-review` prüft die zusätzlichen Rechte nach Zweck, Least Privilege, Datenzugriff, Außenwirkung, Fallback und Gate.
- **Mit mindestens einer `SKILL.md`:** Das Gesamtpaket gilt als Skill-Bundle. `skill-security-review` übernimmt die Zulassungsprüfung einschließlich enthaltener MCP-, Hook- und Script-Dateien. Ein zusätzlicher `tool-permission-review` ist nur nötig, wenn das Berechtigungsdesign einen eigenständigen Prüfauftrag bildet.

Belege: [Sicherheit/MCP-und-externe-Tools.md, Z. 7–29](https://github.com/Borstwerk/KI-Regeln/blob/87320bb92b7ce2ed02ff8bd5a433d263ad5a4d6f/Sicherheit/MCP-und-externe-Tools.md#L7) und [Dokumentation/Skill-Handbuch.md, Z. 96](https://github.com/Borstwerk/KI-Regeln/blob/87320bb92b7ce2ed02ff8bd5a433d263ad5a4d6f/Dokumentation/Skill-Handbuch.md#L96).

Zu prüfen sind insbesondere Herkunft, Version/Pinning, Updates, tatsächliche Komponenten, Datenflüsse und Rechte. `prompt-injection-review` kommt bei einem eigenen Prüfjob zu verdächtigen oder instruktionshaltigen externen Inhalten hinzu. Toolverfügbarkeit erteilt keine Aktionsfreigabe; Rechteänderungen erfordern eine neue Zulassungsentscheidung.

3. **Nicht gelaufenen Test als geprüft melden**

**Nein, keinen uneingeschränkten Prüf- oder PASS-Claim.** Den Test als `NOT RUN`, den betroffenen Ergebnisstand als `UNVERIFIED` beziehungsweise bei einem blockierenden Gate als `BLOCKED` ausweisen. Grund und verbleibende Prüflücke nennen. Tatsächlich bestandene andere Checks dürfen separat und mit ihrem genauen Umfang gemeldet werden.

Das steht ausdrücklich in [AGENTS.md, Z. 128–134](https://github.com/Borstwerk/KI-Regeln/blob/87320bb92b7ce2ed02ff8bd5a433d263ad5a4d6f/AGENTS.md#L128). Auch ein struktureller Harness-PASS ersetzt keine Verhaltensprüfung: [Local-Validation-Harness.md, Z. 212–218](https://github.com/Borstwerk/KI-Regeln/blob/87320bb92b7ce2ed02ff8bd5a433d263ad5a4d6f/Dokumentation/Local-Validation-Harness.md#L212). Für diese ehrliche Statusmeldung ist ohne iterative Umsetzung kein `verification-loop` erforderlich.

Quellenlücke im Snapshot: Die registrierten Dateien `Recherche/Skills/citation-audit/SKILL.md` und `Schreiben/Skills/adressatengerechte-kommunikation/SKILL.md` fehlen auch nach gezielter Suche. Ihre kanonischen Descriptions konnten daher nicht geprüft werden; die obigen Aussagen sind durch die jeweils genannten vorhandenen Quellen belegt.