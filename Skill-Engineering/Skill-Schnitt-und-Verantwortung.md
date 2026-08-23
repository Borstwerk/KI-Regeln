# Skill-Schnitt und Verantwortung

## Zweck

Nicht jede Regel, jeder Prompt oder jede wiederkehrende Formulierung braucht einen eigenen Skill.

Ein eigener Skill ist sinnvoll, wenn eine **wiederkehrende Arbeitsdisziplin** mit eigener Aktivierungslogik, eigenem Ergebnis und klaren Grenzen existiert.

## Gute Skill-Grenzen

Ein Skill sollte möglichst eine zusammenhängende Verantwortung besitzen:

```text
Trigger
→ begrenzte Arbeitsdisziplin
→ überprüfbares Ergebnis
```

Beispiele:

- `code-review` prüft einen tatsächlichen Diff;
- `citation-audit` prüft Claim-Zitat-Zuordnung;
- `greybox` klärt Seitenstruktur vor visueller Politur.

## Wann kein neuer Skill nötig ist

Keinen eigenen Skill erzeugen, wenn:

- nur eine einzelne allgemeine Regel ergänzt wird;
- die Aufgabe vollständig Teil eines bestehenden Skills ist;
- der Unterschied nur aus Toolnamen oder Plattformnamen besteht;
- der Skill keinen eigenständigen Trigger hätte;
- er nur einen anderen Skill umbenennt;
- er projektlokale Wahrheit enthält.

## Split- und Merge-Signale

### Skill aufteilen

Aufteilen, wenn:

- völlig unterschiedliche Trigger entstehen;
- unterschiedliche Sources of Truth gelten;
- Teile unabhängig eingesetzt oder reviewed werden müssen;
- ein Teil andere Toolrechte oder Sicherheitsgrenzen benötigt;
- der Skill so groß wird, dass fast immer nur ein kleiner Teil relevant ist.

### Skills zusammenführen

Zusammenführen, wenn:

- sie fast immer gemeinsam triggern;
- Inputs, Output und Reviewkriterien identisch sind;
- ihre Trennung nur Dateiorganisation statt Arbeitslogik ausdrückt.

## Kein versteckter Orchestrator

Ein Fachskill soll nicht stillschweigend immer weitere Skills auslösen und dadurch Scope vergrößern.

Wenn mehrere Skills regelmäßig in einer festen Reihenfolge gebraucht werden, gehört diese Reihenfolge eher in einen **Workflow / ein Recipe** als in einen immer größer werdenden Skill.

## Projektwahrheit bleibt lokal

Ein Skill beschreibt **wie** gearbeitet wird.

Er darf keine konkrete:

- Produktanforderung;
- Architekturentscheidung;
- Marke;
- Serienfigur;
- interne Datenquelle;
- reale Freigabe

als allgemeine Regel festschreiben.

## Leitfrage

> Kann dieser Skill für eine völlig fremde Person oder ein anderes Projekt dieselbe Arbeitsdisziplin sinnvoll beschreiben?

Wenn nein, gehört der Inhalt eher in lokale Projektregeln.
