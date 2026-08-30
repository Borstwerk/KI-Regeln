# KI-Regeln – Start hier

## Du bringst die Aufgabe. KI-Regeln hilft bei der passenden Arbeitsweise.

KI-Regeln richtet sich an Menschen, die generative KI für reale Aufgaben einsetzen möchten, ohne sich zuerst tief in Prompt Engineering, Agentensysteme oder einzelne KI-Werkzeuge einarbeiten zu müssen.

Der Einstieg ist deshalb **nicht**: „Welchen Skill soll ich verwenden?“

Der Einstieg ist:

> **Was möchtest du erreichen?**

Beschreibe deine Aufgabe in normaler Sprache, nenne die Informationen oder Dateien, die dafür relevant sind, und lass die KI im Repository nach den passenden Regeln, Skills und Workflows suchen.

## So benutzt du KI-Regeln

```text
konkretes Problem oder Ziel beschreiben
→ vorhandene Informationen / Dateien / Projektregeln bereitstellen
→ KI ordnet die Aufgabe ein
→ KI wählt den kleinsten ausreichenden Skill-/Workflow-Satz
→ fehlende, wirklich notwendige Informationen klären
→ Aufgabe bearbeiten
→ Ergebnis gegen Quellen, Regeln und Auftrag prüfen
→ Human Gate, wenn eine reale Entscheidung oder Außenwirkung es erfordert
```

Du musst dafür weder die Namen der Skills kennen noch den kompletten Werkzeugkasten verstehen.

## Beispiel für einen Startauftrag

Du kannst einer KI zum Beispiel schreiben:

> Ich möchte folgende Aufgabe lösen: **[Aufgabe beschreiben]**. Prüfe in diesem Repository, welche Regeln, Skills oder Workflows dafür tatsächlich passen. Wähle den kleinsten ausreichenden Satz, erkläre die Auswahl kurz und arbeite dann damit. Nutze meine Projektinformationen und vorhandenen Quellen als konkrete Wahrheit. Frage nur nach Informationen, die für die Aufgabe wirklich fehlen. Erfinde fehlende Fakten nicht und mache notwendige menschliche Freigaben sichtbar.

Das ist nur ein Einstiegsmuster, kein Pflichtprompt.

## Typische Aufgaben

| Wenn du zum Beispiel … | Dann kann KI-Regeln typischerweise in diesen Bereichen routen |
|---|---|
| etwas recherchieren oder eine Behauptung prüfen möchtest | Recherche |
| einen Text schreiben, überarbeiten oder adressatengerecht formulieren möchtest | Schreiben |
| eine Geschichte, Figuren, Welt oder einen längeren Erzählbogen entwickeln möchtest | Storyentwicklung und Fiktion |
| deine finanzielle Ausgangslage, Rücklagen, Schulden oder Anlagen analysieren möchtest | Finanzen |
| Bilder oder eine konsistente Bildserie entwickeln möchtest | Bildarbeit |
| eine Website bauen oder prüfen möchtest | Webentwicklung |
| Code entwickeln oder einen Fehler diagnostizieren möchtest | Programmieren |
| eine Datenbank dokumentieren, analysieren oder ändern möchtest | Datenbanken / Dokumentationserstellung |
| Anforderungen klären oder spezifizieren möchtest | Requirements und Spezifikations-Engineering |
| technische Dokumentation erstellen möchtest | Dokumentationserstellung |
| Wissen über längere Zeit strukturiert pflegen möchtest | Wissensmanagement |
| Infrastruktur, Deployments oder Betriebsprobleme bearbeiten möchtest | Infrastruktur / Reliability |

Diese Tabelle ist **nur Orientierung**. Ein reales Problem kann mehrere Bereiche berühren, und oft genügt ein einzelner Skill. Die KI soll nicht möglichst viele Skills laden, sondern nur die tatsächlich notwendigen.

## Was du nicht lernen musst

Für die normale Nutzung musst du nicht zuerst verstehen:

- wie `skill-catalog.yml` aufgebaut ist;
- welche Maturity-Stufen existieren;
- wie Evalpacks intern funktionieren;
- wie Agenten- oder Tool-Routing technisch umgesetzt wird;
- wie viele Skills das Repository enthält;
- welche Prompt-Formulierung angeblich „perfekt“ ist.

Diese Mechanismen existieren, damit der Werkzeugkasten kontrollierbarer und nachvollziehbarer wird. Sie sind nicht die Eintrittskarte für seine Nutzung.

## Was trotzdem bei dir beziehungsweise im Projekt bleibt

KI-Regeln liefert allgemeine Arbeitsweisen. Es kennt nicht automatisch deine konkrete Projektwahrheit.

Dazu gehören je nach Aufgabe zum Beispiel:

- reale Anforderungen und Ziele;
- vorhandene Dateien, Daten und Quellen;
- gültige Projektentscheidungen;
- fachliche oder visuelle Vorgaben;
- tatsächliche System-, Datenbank- oder Toolzustände;
- persönliche Präferenzen, soweit sie für die Aufgabe relevant sind;
- Freigaben für Veröffentlichungen, Käufe, Deployments oder andere Außenaktionen.

Grundregel:

> **Allgemeine Arbeitsweise zentral, konkrete Wahrheit lokal.**

## Warum gibt es KI-Regeln?

KI-Regeln entstand aus einer einfachen Beobachtung: Viele Menschen können ihre Arbeit und private Projekte mit generativer KI verbessern, möchten aber nicht zuerst selbst zu KI-Spezialisten werden.

Der Werkzeugkasten soll diese Lücke schließen. Er sammelt wiederverwendbare Arbeitsweisen so, dass eine KI von einem **konkreten Problem** zu den passenden Methoden routen kann, während Quellen, Unsicherheit, Prüfungen und menschliche Entscheidungen sichtbar bleiben.

Das Ziel ist deshalb nicht, für jede denkbare Aufgabe einen fertigen Prompt anzubieten. Das Ziel ist ein belastbares Arbeitsmodell:

```text
Problem
→ passende Werkzeuge
→ kontrollierte Bearbeitung
→ überprüfbares Ergebnis
```

## Wenn du mehr wissen möchtest

- Reale Beispiele: [`PRAXISBEISPIELE.md`](PRAXISBEISPIELE.md)
- Ausführlichere Nutzung: [`Dokumentation/Nutzung-des-Repositories.md`](Dokumentation/Nutzung-des-Repositories.md)
- Wie die Skill-Auswahl funktioniert: [`Dokumentation/Skill-Handbuch.md`](Dokumentation/Skill-Handbuch.md)
- Reife und Evalabdeckung: [`Dokumentation/Skill-Katalog.md`](Dokumentation/Skill-Katalog.md)
- Technischer Einstieg für Agenten: [`AGENTS.md`](AGENTS.md)

> **Der Skill-Katalog ist der Werkzeugschrank. Dein Problem ist der Startpunkt.**
