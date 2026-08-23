# Externe Aktionen und Bestätigung

## Grundsatz

Aktionen mit realer Außenwirkung sind von Analyse und Entwurf zu unterscheiden.

Beispiele:

- Nachricht senden;
- Issue oder PR veröffentlichen;
- Datei öffentlich bereitstellen;
- Deployment starten;
- Produktion ändern;
- Einladung versenden;
- Daten löschen;
- kostenpflichtige Aktion auslösen.

## Analyse ≠ Aktion

```text
"Formuliere eine Mail"
≠
"Sende die Mail"
```

```text
"Plane den Deploy"
≠
"Deploye"
```

Der Agent darf nicht aus der Möglichkeit einer Aktion auf deren Autorisierung schließen.

## Gates

Vor riskanten oder extern sichtbaren Aktionen prüfen:

- ist die Aktion ausdrücklich beauftragt oder im freigegebenen Workflow enthalten?
- sind Ziel, Empfänger und Scope eindeutig?
- sind irreversible Folgen verständlich?
- wurde die aktuelle Version des Artefakts geprüft?
- existiert ein projektspezifisches Human Gate?

## Vorschau und Ausführung

Wo sinnvoll trennen:

```text
Entwurf / Preview
→ Review
→ explizite Freigabe
→ Ausführung
→ Evidence / Ergebnis
```

Nicht jede kleine Aktion benötigt denselben Prozess. Risiko und Reversibilität bestimmen die Strenge.

## Keine implizite Kettenautorisierung

Die Freigabe eines Schrittes erlaubt nicht automatisch spätere Schritte.

Beispiel:

```text
Commit freigegeben
≠ Push freigegeben
≠ Merge freigegeben
≠ Deploy freigegeben
```

sofern der Projektprozess diese Gates getrennt definiert.

## Fehlgeschlagene Aktion

Bei Fehler nicht automatisch mit stärkerer Berechtigung, anderem Ziel oder destruktiverem Fallback fortfahren.

Fehler analysieren, Scope erhalten und nötigenfalls eskalieren.

## Leitgedanke

> Vorbereiten darf autonomer sein als Veröffentlichen. Außenwirkung braucht passende Autorisierung.
