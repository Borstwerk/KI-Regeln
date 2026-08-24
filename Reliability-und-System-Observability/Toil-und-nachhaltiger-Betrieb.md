# Toil und nachhaltiger Betrieb

## Zweck

Toil macht sichtbar, wo Betrieb dauerhaft durch wiederkehrende, manuelle oder schlecht skalierende Arbeit belastet wird.

Toil ist kein moralisches Urteil über operative Arbeit. Manche manuelle Arbeit ist bewusst, selten oder risikogerecht.

## Typische Toil-Merkmale

Eine Tätigkeit ist ein starker Toil-Kandidat, wenn mehrere Punkte zutreffen:

- manuell;
- wiederkehrend;
- weitgehend deterministisch;
- grundsätzlich automatisierbar;
- reaktiv/taktisch statt dauerhaft wertschaffend;
- wächst mit System-, Nutzer- oder Incidentvolumen;
- erzeugt wenig neues Wissen;
- muss regelmäßig erneut erledigt werden.

Beispiele können sein:

- repetitive manuelle Deploy-/Recovery-Schritte;
- wiederkehrendes Alert-Acknowledge ohne Entscheidung;
- immer gleiche Incidenttriage;
- manuelle Capacity-/Quota-Anpassungen;
- wiederkehrende Daten-/Job-Reparaturen;
- Copy/Paste zwischen Betriebssystemen;
- Routinechecks, die maschinell zuverlässig prüfbar wären.

## Nicht alles Manuelle ist Toil

Nicht automatisch als Toil einstufen:

- seltene hochriskante Freigabe;
- bewusster Human Gate;
- komplexe Diagnose mit neuem Erkenntnisgewinn;
- Review/Entscheidung, die echte Abwägung benötigt;
- einmalige Migration;
- Incidentarbeit mit ungewöhnlichem Failure Mode.

## Warum Toil Reliability betrifft

Hoher Toil kann:

- Responsezeit verlängern;
- Fehlerwahrscheinlichkeit erhöhen;
- On-Call-Belastung steigern;
- Capacity von Operators begrenzen;
- wichtige Reliability-Arbeit verdrängen;
- verdeckte Abhängigkeit von Einzelpersonen erzeugen;
- bei Wachstum nicht linear mitwachsen können.

## Toil sichtbar machen

Mögliche Evidence:

- Häufigkeit;
- Zeitaufwand;
- Anzahl manueller Schritte;
- Anzahl betroffener Personen/Teams;
- Fehler-/Reworkrate;
- Incident-/Ticketvolumen;
- Wachstum mit Systemlast;
- Warte-/Handoffzeiten.

Keine universelle Zielquote für „maximal X % Toil“ zentral festlegen.

## Priorisierung

Automatisierung nicht nur nach Häufigkeit priorisieren.

Berücksichtigen:

- Risiko der manuellen Arbeit;
- Kosten der Automatisierung;
- Blast Radius einer falschen Automatisierung;
- Reversibilität;
- benötigte Human Gates;
- Änderungsrate des zugrunde liegenden Prozesses;
- erwartete Lebensdauer;
- ob bessere Architektur den Prozess ganz eliminieren könnte.

## Automatisierung mit Guardrails

```text
manueller wiederkehrender Ablauf
→ stabilen Prozess verstehen
→ Preconditions / Invarianten
→ Automatisierung entwerfen
→ Preview / Dry Run, wenn möglich
→ Gate bei Außenwirkung
→ Fresh Verification
→ Betrieb beobachten
```

Ein schlechter manueller Prozess wird durch Automatisierung nur schneller und reichweitenstärker schlecht.

## Toil und Postmortems

Wiederkehrende manuelle Mitigation oder Triage ist ein sinnvoller Postmortem-/Reliability-Follow-up-Kandidat.

Nicht jedes Toil-Finding braucht einen neuen Skill. Meist führt es zu:

- Infra-/DevOps-Automation;
- besserem Alerting;
- Runbookverbesserung;
- Architecture Change;
- Capacity-/Scaling-Verbesserung;
- besserer Observability;
- Test-/Recovery-Automation.

## Leitgedanke

> Nachhaltiger Betrieb reduziert wiederkehrende Arbeit dort, wo Automatisierung oder Systemdesign Risiko und Aufwand tatsächlich senken – nicht dort, wo ein Human Gate bewusst Schutz bietet.