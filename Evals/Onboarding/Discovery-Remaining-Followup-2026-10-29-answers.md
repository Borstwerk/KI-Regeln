# Antworten des separaten Discovery-Folgelaufs

Unveränderter Antworttext; ausschließlich temporäre absolute Snapshot-Links
sind auf denselben Quellenstand cc8f8b6 mit derselben Zeilenangabe gepinnt.

## D2 / D4 / D6

1. **Wiederholt scheiternder Skill:** Einstieg ist [Workflows/Skill-Verbesserung-aus-Evals-und-Fehlern.md](https://github.com/Borstwerk/KI-Regeln/blob/cc8f8b6b945bc1cd0d5078433d67c03fb97e97d9/Workflows/Skill-Verbesserung-aus-Evals-und-Fehlern.md#L7), Abschnitt „Einstieg“. Der Weg: Baseline und frühere Fälle prüfen → Ursache eingrenzen → Änderungskandidat → getrennte Entwicklungs-, Regressions- und unabhängige Evidence → Review → menschliche Freigabe. Die methodische Grundlage steht in [Skill-Engineering/Evidence-getriebene-Skill-Verbesserung.md](https://github.com/Borstwerk/KI-Regeln/blob/cc8f8b6b945bc1cd0d5078433d67c03fb97e97d9/Skill-Engineering/Evidence-getriebene-Skill-Verbesserung.md#L47), „Ursache klassifizieren“: Wiederholung allein beweist keinen Skillfehler; auch Runtime, Tooling, Harness oder Spezifikation können ursächlich sein.

2. **Teststrategie oder konkrete Grenzwertfälle:** Für „Welche Risiken prüfen wir auf welchen Testebenen?“ passt [Testing-und-QA/Skills/test-strategy/SKILL.md](https://github.com/Borstwerk/KI-Regeln/blob/cc8f8b6b945bc1cd0d5078433d67c03fb97e97d9/Testing-und-QA/Skills/test-strategy/SKILL.md#L3). Für konkrete Eingaben, Grenzen und erwartete Ergebnisse passt [Testing-und-QA/Skills/test-design/SKILL.md](https://github.com/Borstwerk/KI-Regeln/blob/cc8f8b6b945bc1cd0d5078433d67c03fb97e97d9/Testing-und-QA/Skills/test-design/SKILL.md#L12), „Arbeitsweise“: ausdrücklich Grenzwerte, Äquivalenzklassen und Zustandsübergänge. Wenn beides nötig ist, verbindet [Workflows/Teststrategie-und-QA.md](https://github.com/Borstwerk/KI-Regeln/blob/cc8f8b6b945bc1cd0d5078433d67c03fb97e97d9/Workflows/Teststrategie-und-QA.md#L9) Strategie und anschließenden Fallentwurf. Ohne konkrete Fachanforderungen lassen sich noch keine belastbaren Grenzwerte festlegen.

3. **Workflow ergänzen:** Für die Registrierung ist [workflow-index.yml](https://github.com/Borstwerk/KI-Regeln/blob/cc8f8b6b945bc1cd0d5078433d67c03fb97e97d9/workflow-index.yml#L2) maßgeblich. [CONTRIBUTING.md](https://github.com/Borstwerk/KI-Regeln/blob/cc8f8b6b945bc1cd0d5078433d67c03fb97e97d9/CONTRIBUTING.md#L30) verlangt, zuerst vorhandene Lösungen zu prüfen, und schreibt in Zeile 42 ausdrücklich die Aufnahme neuer Workflows in diesen Index vor. Der Ablauf selbst gehört in eine Datei unter `Workflows/`; die Gestaltungsregeln stehen in [Workflows/README.md](https://github.com/Borstwerk/KI-Regeln/blob/cc8f8b6b945bc1cd0d5078433d67c03fb97e97d9/Workflows/README.md#L17), „Grundregeln“: klare Handoffs, Evidence und unveränderte menschliche Freigabegrenzen.

Die nötigen Orientierungsquellen sind vorhanden. Nur gelesen und gezielt gesucht; keine Änderungen, Installationen, Tests, weiteren Agenten oder externen Aktionen.

## D7

Wenn du **Tool- und Berechtigungsrechte eines Agenten oder einer Integration** meinst, passt `tool-permission-review`. Der Skill prüft minimale Rechte, Datenzugriffe und nötige Freigaben.

Meinst du solche Toolrechte, **Benutzer-/Rollenberechtigungen** oder **Zugriffsprotokolle**? Davon hängt die genaue Auswahl ab.

## D8

eins, zwei
