# KI-Regeln – Start hier

**Sprache:** Deutsch · [English](START-HERE.md) · [Projektübersicht](README.md)

> **Du bringst die Aufgabe. Die KI hilft dir, die passende Arbeitsweise zu finden.**

KI-Regeln ist für Menschen gedacht, die mit generativer KI **etwas Konkretes erledigen** möchten, ohne vorher Skill-Namen oder Agentenarchitektur lernen zu müssen. Starte mit deinem Ziel, nicht mit dem Werkzeugkasten.

## 1. Beschreibe dein Ziel

Zum Beispiel: „Ich möchte ein PowerShell-Skript sicher erweitern“, „Prüfe diese Behauptung anhand guter Quellen“ oder „Hilf mir, eine Geschichte konsistent zu überarbeiten“.

Für einen ersten Auftrag genügt beispielsweise:

> Ich möchte **[Aufgabe]** lösen. Du darfst dafür die Dateien des KI-Regeln-Repositories lesen. Prüfe, welche Regeln, Skills oder Workflows sinnvoll sind, wähle nur die tatsächlich benötigten und erkläre kurz deine Auswahl. Nutze meine Projektinformationen als konkrete Wahrheit und sage ehrlich, was du nicht prüfen konntest. Frage nach einer Freigabe, bevor du riskante oder externe Aktionen ausführst.

Das ist **ein Beispiel, kein Pflichtprompt**.

## 2. Gib der KI Zugang zu den relevanten Informationen

- Stelle deiner KI das Repository, die benötigten Dateien oder einen verfügbaren Repository-Zugriff bereit. **Ein bloßer Link garantiert nicht**, dass das Modell die Dateien tatsächlich gelesen hat.
- Teile die Aufgabenstellung, vorhandene Projektregeln und passende Quellen. Private Daten und Zugangsdaten nur über dafür geeignete, autorisierte Wege verwenden.
- KI-Regeln ist **keine automatisch installierte ChatGPT- oder Codex-Funktion**. Ob ein Skill gelesen, ein Tool verwendet oder ein Test ausgeführt werden kann, hängt vom konkreten Zugriff und der Laufzeit ab.

## 3. Was die KI mit KI-Regeln machen soll

```text
Deine Aufgabe und die vorhandenen Projektinformationen
→ lokale Wahrheit und Anforderungen verstehen
→ passende Skills / Workflows gezielt entdecken
→ mit geeigneten Werkzeugen arbeiten
→ tatsächliche Ergebnisse und Prüfgrenzen offenlegen
→ erforderliche Freigaben einholen
```

Sie soll nicht den kompletten Katalog laden oder dich zuerst nach Skill-Namen fragen. Manchmal ist **kein** besonderer Skill nötig. Wenn du neue Möglichkeiten kennenlernen möchtest, frage: *„Welche zusätzlichen Fähigkeiten könnten für diese Aufgabe wirklich hilfreich sein?“*

## 4. Was bleibt beim Menschen beziehungsweise Projekt?

KI-Regeln liefert allgemeine Methoden, aber **keine automatische Kenntnis deiner Projektwahrheit**. Anforderungen, Dateien, Systeme, aktuelle Fakten, Testdaten, persönliche Vorgaben und Berechtigungen kommen weiterhin aus deinem konkreten Kontext.

Ein definierter Test ist kein ausgeführter Test; eine grüne Strukturprüfung ist kein unabhängiger Qualitätsnachweis. Reale Freigaben für Veröffentlichungen, Änderungen an produktiven Daten oder Deployments bleiben menschliche beziehungsweise projektspezifische Entscheidungen.

## 5. Und wenn du tiefer einsteigen willst?

- [Praxisbeispiele](PRAXISBEISPIELE.md) – echte Arbeitsabläufe einschließlich Grenzen und Korrekturen.
- [Ausführliche Nutzung](Dokumentation/Nutzung-des-Repositories.md) – Projektintegration und Arbeitsmodell.
- [Skill-Handbuch](Dokumentation/Skill-Handbuch.md) – wie die Werkzeugauswahl funktioniert.
- [Skill-Katalog und Reife](Dokumentation/Skill-Katalog.md) – Skills, Maturity und Evalabdeckung.
- [AGENTS.md](AGENTS.md) – verbindlicher technischer Einstieg für KI-Agenten (nicht der menschliche Schnellstart).
- [CONTRIBUTING.md](CONTRIBUTING.md) – mithelfen und Änderungen einbringen.

**Grundprinzip:** Allgemeine Arbeitsweise zentral, konkrete Wahrheit lokal.
