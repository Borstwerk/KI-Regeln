# Context Engineering für KI-Agenten

## Zweck

Context Engineering beschreibt, welche Informationen ein Agent für die aktuelle Aufgabe benötigt und wie dieser Kontext über längere Arbeitsläufe sauber gehalten wird.

Das Ziel ist nicht maximal viel Kontext, sondern **minimal ausreichender, aktueller und signalstarker Kontext**.

## Grundprinzip

> Relevanz vor Vollständigkeit.

Ein zu kleiner Kontext führt zu falschen Annahmen. Ein zu großer Kontext kann Rauschen, Widersprüche, Staleness, unnötigen Tokenverbrauch und schlechtere Nutzung relevanter Informationen erzeugen.

Kontextfenstergröße ist deshalb eine technische Kapazität, kein Qualitätsziel.

## Kontextquellen priorisieren

Wenn möglich, Informationen in dieser Reihenfolge beziehen:

1. konkreter Auftrag;
2. verbindliche Spezifikation oder Anforderung;
3. aktuelle Projektentscheidungen und Architektur;
4. relevante Implementierung;
5. relevante Tests und Nachweise;
6. zusätzliche historische oder erläuternde Informationen nur bei Bedarf.

Eine ältere Zusammenfassung darf eine aktuellere Quelle der Wahrheit nicht überschreiben.

## Kontext gezielt laden

Vor einer Aufgabe klären:

- Welche Entscheidung soll der Agent treffen oder welche Änderung soll er durchführen?
- Welche Dateien, Dokumente oder Schnittstellen beeinflussen diese Entscheidung tatsächlich?
- Welche Regeln gelten für diesen Arbeitsschritt?
- Welche Informationen sind nur Hintergrund und können zunächst weggelassen werden?
- Welche Informationen können just-in-time geladen werden?

Nicht vorsorglich das gesamte Repository, die komplette Historie, alle Skills oder alle verfügbaren Tools in den aktiven Kontext laden, wenn gezielte Quellen genügen.

## Quellen referenzieren statt duplizieren

Wenn ein kanonisches Dokument existiert, möglichst darauf verweisen statt seinen Inhalt in neue Agentendokumente zu kopieren.

Duplikate erzeugen schnell eine zweite Wahrheit.

Beispiele:

- Architekturentscheidung in einer kanonischen Entscheidungsdatei belassen;
- Requirement nicht zusätzlich als neue Wahrheitsschicht in einen Handoff kopieren;
- Tests nicht als Prosa neu beschreiben, wenn der konkrete Test als Nachweis referenziert werden kann;
- große Artefakte über stabile Referenz plus relevante Kurzbeschreibung weitergeben.

## Active Context, Working State und Persistent Knowledge

Drei Ebenen unterscheiden:

```text
Active Context
→ aktuell modell-sichtbare Informationen

Working State
→ task-/threadbezogener Zustand über mehrere Schritte oder Sessions

Persistent Knowledge
→ dauerhaft gepflegtes Wissen über einzelne Tasks hinaus
```

Details stehen in `Working-Memory-und-Persistenzgrenzen.md`.

Dauerhaftes Wissensmanagement ist kein Unterfall des aktiven Kontextfensters.

## Kontext über längere Loops pflegen

Längere Agentenläufe erzeugen neue Informationen. Dabei unterscheiden:

- **stabile Ergebnisse** – Entscheidungen, geprüfte Fakten, akzeptierte Artefakte;
- **temporäre Arbeitshypothesen** – noch nicht bestätigte Vermutungen;
- **veraltete Zwischenstände** – durch spätere Ergebnisse widerlegt oder ersetzt.

Nur benötigte stabile Ergebnisse und aktuell relevante offene Punkte sollen in folgende aktive Kontexte übernommen werden.

Taskbezogener Zustand kann außerhalb des Kontextfensters als Working State persistiert werden.

## Context Budget und Token-Effizienz

Tokenverbrauch wird nicht isoliert optimiert.

Beobachte, wenn verfügbar:

- Input-/Output-Tokens;
- Cache-Signale;
- Tooloutput-Größe;
- Anzahl von Modell-/Toolaufrufen;
- Latenz;
- Task Outcome.

Siehe `Context-Budget-und-Token-Effizienz.md`.

## Context Rot und Signalqualität

Großer Kontext kann nutzlos oder schädlich werden, obwohl die benötigte Information formal enthalten ist.

Typische Risiken:

- Duplikate;
- Altstände;
- widersprüchliche Zusammenfassungen;
- große irrelevante Tooloutputs;
- zu viele gleichzeitig sichtbare Skills oder Tools;
- vermischte Fakten und Hypothesen.

Siehe `Context-Rot-und-Signalqualitaet.md`.

## Context Compaction

Wenn ein Arbeitslauf zu lang wird oder eine Phase abgeschlossen ist, Kontext bewusst verdichten.

Dabei besonders erhalten:

- aktuelles Ziel und Scope;
- harte Constraints;
- Sources of Truth;
- bestätigte Entscheidungen;
- aktueller Artefaktzustand;
- offene Risiken und Fehler;
- Evidence und Gate-Status;
- relevante Sackgassen;
- nächsten prüfbaren Schritt.

Compaction soll nach Möglichkeit über Fortsetzungsfähigkeit evaluiert werden, nicht nur über Kürze.

Siehe `Context-Compaction.md`.

## Long-Horizon Handoffs

Wenn eine neue Session oder ein anderer Agent übernimmt, ein eigenständig nutzbares Handoff erzeugen.

Ein Handoff ist nicht bloß Compaction: Es besitzt einen Übergabevertrag für eine neue Arbeitsinstanz.

Siehe `Long-Horizon-Handoffs.md`.

## Tool Outputs und Offloading

Deterministische Filterung, Aggregation und Vorverarbeitung möglichst außerhalb des Modellkontexts durchführen, wenn dadurch keine relevante Evidence verloren geht.

Große Rohoutputs nicht automatisch vollständig in den Kontext zurückführen.

Siehe `Tool-Outputs-und-Context-Offloading.md`.

## Prompt Caching

Wenn eine Runtime Prompt-/Präfix-Caching unterstützt, stabile Kontextbestandteile möglichst stabil strukturieren. Providerdetails wie Cache-Lebensdauer, Mindestgrößen oder Preise bleiben lokal und versionsabhängig.

Siehe `Prompt-Caching-und-stabile-Kontexte.md`.

## Sicherheitsregel

Persönliche, geheime oder fachlich irrelevante Daten nicht allein deshalb in den Kontext aufnehmen, weil sie verfügbar sind.

Ausgelagerter Working State, Handoffs und Rohartefakte unterliegen denselben Datenschutz-, Berechtigungs- und Sicherheitsregeln wie aktive Inhalte.

## Qualitätscheck

Vor oder während eines Agentenlaufs prüfen:

1. Ist der Auftrag eindeutig?
2. Sind die relevanten Sources of Truth vorhanden?
3. Gibt es widersprüchliche oder veraltete Informationen?
4. Enthält der Kontext unnötige Daten oder große Rohoutputs?
5. Fehlt eine Information, ohne die der Agent nur raten könnte?
6. Kann ein großes Dokument durch Referenz, Ausschnitt oder Just-in-time-Retrieval ersetzt werden?
7. Wird taskbezogener Zustand sinnvoll außerhalb des aktiven Fensters gehalten?
8. Ist Compaction oder ein Handoff nötig?
9. Wurde eine Context-Optimierung gegen die Ergebnisqualität geprüft?

## Leitgedanke

> Kontext ist Arbeitsmaterial, kein Archivdump. Halte das relevante Signal aktiv und den restlichen Zustand zuverlässig adressierbar.