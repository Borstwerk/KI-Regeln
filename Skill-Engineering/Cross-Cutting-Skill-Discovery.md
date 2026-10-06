# Cross-Cutting Skill Discovery und Routing Overlays

## Problem

Problem-first Routing löst die erste Frage gut:

> Welcher fachliche Skill bearbeitet den eigentlichen Auftrag?

Bei einem größeren Skillbestand entsteht aber eine zweite Frage:

> Gibt es einen domänenübergreifenden Skill, den der Nutzer nicht kennen muss, der das Ergebnis trotzdem materiell verbessert oder absichert?

Beispiel:

~~~text
"Vergleiche drei Architekturvarianten
und gib mir eine Empfehlung."
~~~

Primärer fachlicher Skill:

~~~text
architecture-tradeoff-analysis
~~~

Die Aufgabenform kann zusätzlich `visual-answer` rechtfertigen, obwohl der Nutzer den Skill nicht kennt, ihn nicht nennt und nicht einmal wissen muss, dass eine visuelle Antwort möglich ist.

Diese zweite Entdeckung ist Aufgabe des Routers.

## Grundprinzip

> Skill Discovery ist Systemarbeit, nicht Nutzerarbeit.

Der Nutzer darf Skillnamen verwenden. Er muss sie aber nicht kennen.

Ein frischer Agent soll deshalb nicht nur nach fachlicher Domäne routen, sondern nach dem Primärrouting einen kleinen globalen Overlay-Pass ausführen.

## Mehrstufiges Routing

~~~text
Nutzerauftrag
      ↓
1. PRIMARY
   Was ist der eigentliche fachliche Job?
      ↓
2. WORKFLOW
   Ist ein vorhandener mehrphasiger Workflow nötig?
      ↓
3. OVERLAY PASS
   Gibt es domänenübergreifende Skills,
   deren eigene Triggerbeschreibung jetzt passt?
      ↓
4. ASSURANCE / GATES
   Welche Evidence, Reviews oder Freigaben
   sind für den Completion Claim nötig?
      ↓
5. RUNTIME
   Welche native Capability, Plugin/App oder
   welcher Fallback führt den Job aus?
~~~

Der Overlay-Pass ersetzt weder primäres Routing noch fachliche Skills.

## routing-overlays.yml

Die Datei `../routing-overlays.yml` ist absichtlich klein.

Sie ist keine zweite Skill-Datenbank und enthält keine Triggertexte.

Beispielstruktur:

~~~yaml
- skill: visual-answer
  phase: presentation
~~~

Das bedeutet nur:

> Nach dem fachlichen Routing soll der Router die Description von `visual-answer` kurz gegen die konkrete Aufgabe prüfen.

Es bedeutet **nicht**:

- Skill automatisch laden;
- Skill immer aktivieren;
- Trigger aus dem Overlay ableiten;
- einen Skill allein wegen seiner Phase verwenden.

Die Trigger-Wahrheit bleibt in der jeweiligen `SKILL.md`.

## Overlay-Phasen

### presentation

Prüft, ob Form und Darstellung die Nutzbarkeit materiell verbessern.

Beispiel: `visual-answer`.

### communication

Prüft, ob Empfänger, Beziehung, gewünschte Reaktion oder Kommunikationslage die Formulierung materiell bestimmen.

Beispiel: `adressatengerechte-kommunikation`.

### assurance

Prüft, ob ein Ergebnis vor Abschluss zusätzliche Evidence-/Review-Disziplin benötigt.

Beispiele: `citation-audit`, `verification-loop`.

### security

Prüft Cross-Cutting-Risiken, wenn externe Skills, neue Tools oder mächtige Rechte in den Auftrag geraten.

Beispiele: `skill-security-review`, `tool-permission-review`.

Die Phasen sind Routinghilfen, keine Autorisierungs- oder Maturityklassen.

## Algorithmus für einen frischen Agenten

### Schritt 1 – Primären Job finden

Nutze `AGENTS.md`, `Dokumentation/Skill-Handbuch.md`, `skill-catalog.yml` und bei Bedarf `workflow-index.yml`.

Ziel: kleinsten fachlich ausreichenden Skill-/Workflow-Satz bestimmen.

### Schritt 2 – Overlay-Liste lesen

Nur die wenigen IDs aus `routing-overlays.yml` berücksichtigen. Nicht alle zentralen Skills erneut durchsuchen.

### Schritt 3 – Triggerbeschreibung prüfen

Für jeden Overlay-Kandidaten:

1. Catalog-Eintrag prüfen;
2. Description der `SKILL.md` lesen;
3. positive Trigger und Near-Miss-Grenzen gegen den realen Auftrag prüfen;
4. nur bei materiellem Zusatznutzen auswählen.

`related` bleibt ein Hinweis und erzeugt keine automatische Aktivierung.

### Schritt 4 – klein halten

Der Overlay-Pass soll den Skill-Satz nicht aufblasen.

Typischer Auftrag:

~~~text
1 Primary Skill
+ 0–1 Presentation/Communication Overlay
+ nur notwendige Assurance-/Security-Skills
~~~

Mehrere Overlays sind möglich, müssen aber jeweils einen eigenen notwendigen Job besitzen.

## Beispiele

### Architekturvergleich

~~~text
Auftrag:
"Drei Varianten vergleichen und Empfehlung geben."

PRIMARY
→ architecture-tradeoff-analysis

OVERLAY PASS
→ visual-answer: ja,
   weil mehrere Optionen × Kriterien × Empfehlung

ERGEBNIS
→ fachlich belastbarer Vergleich
+ scanbare Entscheidung
~~~

### Kurzer Faktenlookup

~~~text
Auftrag:
"Was bedeutet HTTP 404?"

PRIMARY
→ direkte Antwort / ggf. kein Skill

OVERLAY PASS
→ visual-answer: nein
→ communication: nein
→ assurance: nein

ERGEBNIS
→ kurze Antwort
~~~

### Belegte Research-Synthese vor Veröffentlichung

~~~text
PRIMARY
→ research-synthesis

OVERLAY / ASSURANCE
→ citation-audit,
   wenn der Text weitgehend fertig ist und
   wichtige Claims gegen konkrete Evidence
   geprüft werden sollen
~~~

### Neue externe Agent-Fähigkeit

~~~text
PRIMARY
→ eigentlicher Fachjob

SECURITY OVERLAY
→ skill-security-review,
   wenn ein externer/mächtiger Skill aktiviert werden soll

→ tool-permission-review,
   wenn neue Netzwerk-, Schreib-, Execute-
   oder Produktionsrechte verlangt werden
~~~

## Menschlicher Einstieg

Ein neuer Nutzer soll nicht zuerst den Skill-Katalog lesen.

Ausreichend ist:

> Beschreibe die Aufgabe in normaler Sprache. KI-Regeln soll selbst passende fachliche Skills, mögliche Cross-Cutting-Overlays und notwendige Reviews auswählen.

Optional kann der Nutzer fragen:

> Welche zusätzlichen Fähigkeiten könnten bei dieser Aufgabe helfen, die ich wahrscheinlich nicht kenne?

Die Antwort soll konkrete relevante Möglichkeiten nennen, nicht den gesamten Katalog auskippen.

## Anti-Patterns

Nicht:

~~~text
alle Skills
→ alle Trigger im Kontext prüfen
~~~

Nicht:

~~~text
routing-overlays.yml
→ alle Overlays automatisch aktivieren
~~~

Nicht:

~~~text
Trigger in SKILL.md
+ zweite Triggerkopie im Overlay
→ Drift
~~~

Sondern:

~~~text
Primärraum klein halten
→ kleine Overlay-Liste
→ kanonische Skill-Description prüfen
→ nur materiell passende Skills laden
~~~

## Leitgedanke

> Der Werkzeugschrank darf groß sein. Der aktive Werkzeuggürtel soll klein bleiben.
