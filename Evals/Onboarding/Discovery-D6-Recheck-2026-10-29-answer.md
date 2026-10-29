# Antwort der gezielten D6-Nachprüfung

Unveränderter Antworttext; ausschließlich temporäre absolute Snapshot-Linkziele
sind auf den geprüften Quellencommit mit gleicher Zeilenangabe gepinnt.

1. **Ein bestehender Skill scheitert wiederholt.**
   Einstieg ist [Workflows/Skill-Verbesserung-aus-Evals-und-Fehlern.md](https://github.com/Borstwerk/KI-Regeln/blob/f0f83181d6be368399774e117fc64ba5bdd5f8b7/Workflows/Skill-Verbesserung-aus-Evals-und-Fehlern.md#L7), Abschnitt „Einstieg“. Der Weg führt über Baseline und frühere Fälle, Ursachenprüfung, Änderungskandidat, getrennte Development-/Regression-/Held-out-Evidence sowie Review und Human Gate. Zuerst prüfen, ob tatsächlich der Skill verantwortlich ist: [Skill-Engineering/Evidence-getriebene-Skill-Verbesserung.md](https://github.com/Borstwerk/KI-Regeln/blob/f0f83181d6be368399774e117fc64ba5bdd5f8b7/Skill-Engineering/Evidence-getriebene-Skill-Verbesserung.md#L47), „Ursache klassifizieren“, nennt auch Runtime, Tooling, Harness, Daten und Spezifikation als mögliche Ursachen.

2. **Teststrategie oder konkrete Grenzwertfälle?**
   Für die Frage „Welche Risiken prüfen wir auf welchen Testebenen?“ passt [Testing-und-QA/Skills/test-strategy/SKILL.md](https://github.com/Borstwerk/KI-Regeln/blob/f0f83181d6be368399774e117fc64ba5bdd5f8b7/Testing-und-QA/Skills/test-strategy/SKILL.md#L3). Für konkrete Eingaben, Grenzwerte, Zustände und erwartete Ergebnisse passt [Testing-und-QA/Skills/test-design/SKILL.md](https://github.com/Borstwerk/KI-Regeln/blob/f0f83181d6be368399774e117fc64ba5bdd5f8b7/Testing-und-QA/Skills/test-design/SKILL.md#L12), „Arbeitsweise“. Werden beide Ergebnisse gebraucht, verbindet sie [Workflows/Teststrategie-und-QA.md](https://github.com/Borstwerk/KI-Regeln/blob/f0f83181d6be368399774e117fc64ba5bdd5f8b7/Workflows/Teststrategie-und-QA.md#L9). Für tatsächliche Grenzwertfälle fehlen hier konkrete Anforderungen und fachlich festgelegte Erwartungswerte.

3. **Einen Workflow ergänzen: Welche Datei ist maßgeblich?**
   Der **verbindliche Beitrags- und Reviewweg** steht in [CONTRIBUTING.md](https://github.com/Borstwerk/KI-Regeln/blob/f0f83181d6be368399774e117fc64ba5bdd5f8b7/CONTRIBUTING.md#L5). Die konkrete Anleitung liefert [Workflows/README.md](https://github.com/Borstwerk/KI-Regeln/blob/f0f83181d6be368399774e117fc64ba5bdd5f8b7/Workflows/README.md#L17), „Workflow beitragen“: vorhandene Abläufe prüfen, Ablauf als Markdown unter `Workflows/` beschreiben und in `workflow-index.yml` registrieren. Der Index ist das maßgebliche Workflow-Inventar; `CONTRIBUTING.md:42` schreibt die Registrierung ausdrücklich vor.

Die benötigten Orientierungsquellen sind vorhanden. Ausschließlich gelesen und gezielt gesucht; keine Änderungen, Installationen, Tests oder externen Aktionen ausgeführt.
