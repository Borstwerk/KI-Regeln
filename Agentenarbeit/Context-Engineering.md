# Context Engineering für KI-Agenten

## Zweck

Context Engineering beschreibt, welche Informationen ein Agent für die aktuelle Aufgabe benötigt und wie dieser Kontext über längere Arbeitsläufe sauber gehalten wird.

Das Ziel ist nicht maximal viel Kontext, sondern **minimal ausreichender Kontext**.

## Grundprinzip

> Relevanz vor Vollständigkeit.

Ein zu kleiner Kontext führt zu falschen Annahmen. Ein zu großer Kontext erhöht Rauschen, Widersprüche und die Gefahr, dass veraltete oder irrelevante Informationen Entscheidungen beeinflussen.

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

Nicht vorsorglich das gesamte Repository oder eine komplette Historie laden, wenn wenige gezielte Quellen genügen.

## Quellen referenzieren statt duplizieren

Wenn ein kanonisches Dokument existiert, möglichst darauf verweisen statt seinen Inhalt in neue Agentendokumente zu kopieren.

Duplikate erzeugen schnell eine zweite Wahrheit.

Beispiele:

- Architekturentscheidung in `DECISIONS.md` belassen;
- Requirement nicht zusätzlich in einen Handoff kopieren;
- Tests nicht als Prosa neu beschreiben, wenn der konkrete Test als Nachweis referenziert werden kann.

## Kontext über längere Loops pflegen

Längere Agentenläufe erzeugen neue Informationen. Dabei unterscheiden:

- **stabile Ergebnisse** – Entscheidungen, geprüfte Fakten, akzeptierte Artefakte;
- **temporäre Arbeitshypothesen** – noch nicht bestätigte Vermutungen;
- **veraltete Zwischenstände** – durch spätere Ergebnisse widerlegt oder ersetzt.

Nur stabile Ergebnisse sollen dauerhaft in den folgenden Kontext eingehen.

## Kontextkompression

Wenn ein Arbeitslauf zu lang wird, nicht blind den gesamten Verlauf weiterreichen.

Stattdessen verdichten:

- aktuelles Ziel;
- bestätigte Entscheidungen;
- relevante geänderte Dateien oder Artefakte;
- offene Risiken;
- fehlgeschlagene Ansätze nur, wenn sie eine Wiederholung verhindern;
- nächsten prüfbaren Arbeitsschritt.

## Sicherheitsregel

Persönliche, geheime oder fachlich irrelevante Daten nicht allein deshalb in den Kontext aufnehmen, weil sie verfügbar sind.

Der Agent soll nur Informationen erhalten, die für die Aufgabe erforderlich oder ausdrücklich gewünscht sind.

## Qualitätscheck

Vor einem Agentenlauf prüfen:

1. Ist der Auftrag eindeutig?
2. Sind die relevanten Quellen der Wahrheit vorhanden?
3. Gibt es widersprüchliche oder veraltete Informationen im Kontext?
4. Enthält der Kontext unnötige Daten?
5. Fehlt eine Information, ohne die der Agent nur raten könnte?
6. Kann ein großes Dokument durch einen gezielten Verweis oder Ausschnitt ersetzt werden?

## Leitgedanke

> Kontext ist Arbeitsmaterial, kein Archivdump.