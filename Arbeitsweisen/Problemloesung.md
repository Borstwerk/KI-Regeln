# Problemlösung mit KI

## Zweck

Diese Arbeitsweise eignet sich für technische, analytische und organisatorische Probleme, bei denen nicht nur eine Antwort, sondern ein nachvollziehbarer Lösungsweg benötigt wird.

## 1. Beobachtung vor Lösung

Nicht mit der ersten plausiblen Erklärung starten.

Zuerst festhalten:

- Was wurde tatsächlich beobachtet?
- Was ist erwartet worden?
- Was ist davon abweichend?
- Unter welchen Bedingungen tritt es auf?
- Welche Informationen fehlen noch?

Symptom und Ursache getrennt halten.

## 2. Problem möglichst klein machen

Ein großes Problem in den kleinsten noch relevanten Fall zerlegen.

Dazu können gehören:

- Eingaben reduzieren;
- Abhängigkeiten einzeln entfernen;
- einen einzelnen Prozessschritt isolieren;
- einen kleinen Testfall bauen;
- nur einen Parameter gleichzeitig verändern.

Ein kleiner reproduzierbarer Fehler ist wertvoller als eine große Menge unscharfer Beobachtungen.

## 3. Hypothesen statt Vermutungsmonopol

Bei unklarer Ursache mehrere falsifizierbare Hypothesen bilden.

Für jede Hypothese festhalten:

- warum sie plausibel ist;
- welche Beobachtung dafür sprechen würde;
- welche Beobachtung sie widerlegen würde;
- wie sie möglichst günstig geprüft werden kann.

Keine Hypothese wird zur Tatsache, nur weil sie gut klingt.

## 4. Gezielt messen

Messungen, Logs, Tests oder Vergleiche sollen konkrete Fragen beantworten.

Nicht wahllos Daten sammeln. Jede zusätzliche Beobachtung sollte helfen, mindestens zwei Hypothesen voneinander zu unterscheiden oder eine Entscheidung abzusichern.

## 5. Kleine überprüfbare Schritte

Nicht die komplette Lösung auf einmal bauen, wenn einzelne Entscheidungen nacheinander geprüft werden können.

Bevorzugter Zyklus:

```text
kleine Annahme
→ kleiner Versuch
→ Ergebnis prüfen
→ nächste Entscheidung
```

Das reduziert Fehlannahmen und macht Korrekturen billig.

## 6. Ursache vor Symptom

Ein Workaround kann sinnvoll sein, wenn er ausdrücklich als solcher behandelt wird. Er darf aber nicht als Root-Cause-Fix verkauft werden.

Vor einem dauerhaften Fix fragen:

- Welche Bedingung erzeugt den Fehler wirklich?
- Wird diese Bedingung durch den Fix beseitigt?
- Oder wird nur das sichtbare Symptom unterdrückt?

## 7. Bestehendes System respektieren

Eine lokale Lösung ist nicht automatisch Anlass für eine neue Architektur.

- keine unnötigen Abstraktionen;
- keine neuen Schichten ohne konkreten Nutzen;
- keinen funktionierenden Nachbarbereich vorsorglich umbauen;
- bestehende Begriffe und Strukturen wiederverwenden, wenn sie passen.

KISS hat Vorrang vor Architekturkosmetik.

## 8. Systeme statt wiederholter Einzelarbeit

Wenn dasselbe Problem regelmäßig wiederkehrt, prüfen, ob eine kleine wiederverwendbare Regel, Vorlage, Automatisierung oder ein Test sinnvoller ist als wiederholte Handarbeit.

Nicht jedes Einzelproblem rechtfertigt ein System. Wiederholung und tatsächlicher Wartungsnutzen sind die Kriterien.

## 9. Gegenprobe einbauen

Bei wichtigen Erkenntnissen prüfen, ob der Nachweis die behauptete Eigenschaft wirklich erkennen kann.

Beispiele:

- Test schlägt fehl, wenn die Schutzbedingung probeweise entfernt wird;
- Messung ändert sich, wenn die vermutete Ursache gezielt verändert wird;
- Review vergleicht tatsächlichen Diff statt nur Abschlussbericht.

Ein Nachweis, der auch bei gebrochenem Verhalten grün bleibt, ist kein belastbarer Nachweis.

## 10. Ergebnis sauber trennen

Am Ende unterscheiden:

- Beobachtung;
- bestätigte Ursache;
- verworfene wesentliche Hypothesen;
- umgesetzte oder empfohlene Maßnahme;
- Nachweis;
- verbleibende Unsicherheit.

So bleibt nachvollziehbar, was bekannt ist und was nur vermutet wird.