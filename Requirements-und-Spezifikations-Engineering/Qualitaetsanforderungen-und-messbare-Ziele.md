# Qualitätsanforderungen und messbare Ziele

## Zweck

Qualitätsanforderungen beschreiben relevante Eigenschaften des Systems oder seiner Nutzung unter konkreten Bedingungen. Schlagwörter wie `schnell`, `hochverfügbar` oder `sicher` reichen dafür nicht.

## Von Eigenschaft zu Szenario

Hilfreiches Format:

```text
Stimulus / relevante Bedingung
→ betroffener Flow / Systemteil
→ erwartete Reaktion
→ messbares oder beobachtbares Ergebnis
→ Mess-/Bewertungsbedingungen
```

Beispiele für Qualitätsfelder können Performance, Availability, Reliability, Accessibility, Usability, Security, Privacy, Compatibility, Maintainability oder Portability sein. Keine Taxonomie ist eine Pflicht-Checkliste.

## Zielwerte

Ein Zielwert braucht Herkunft und Scope. Prüfen:

- Quelle beziehungsweise Entscheidung;
- betroffener Flow/Population;
- Betriebszustand oder Environment;
- Messmethode soweit für Interpretation nötig;
- Zeitraum/Fenster, falls relevant;
- Toleranz oder Ausnahmebedingungen.

Fehlt ein entscheidungsrelevanter Wert, bleibt er offen. Requirements Engineering darf keinen Branchenwert als Stakeholderziel erfinden.

## Baseline vs. Target

```text
Ist-Messung / Baseline
≠
verbindliches Ziel
```

Eine heutige Performance kann als Evidence dienen, wird aber erst durch bestätigte Entscheidung zum Sollwert.

## Reliability-Ziele

Geschäftlich beziehungsweise produktseitig bestätigte Availability-, Recovery- oder Datenverlustziele können hier entstehen. `Reliability-und-System-Observability/` operationalisiert sie anschließend in geeignete Mess- und Betriebsmodelle.

Requirements darf daher beispielsweise ein bestätigtes RTO/RPO oder Nutzerziel dokumentieren, aber nicht eigenmächtig SLI-Implementierung, Alert-Threshold oder Architekturpattern festlegen.

## Security-/Compliance-Ziele

Security- oder Compliance-Bedarf muss auf reale Policy, Threat, Regulation oder Stakeholderentscheidung zurückgeführt werden. Die konkrete Control-Auswahl und fachliche Security-Analyse gehören zur Sicherheitsdomäne.

## Trade-offs

Qualitätsziele können konkurrieren. Requirements Engineering macht Konflikte sichtbar; Architecture bewertet später, welche Struktur die bestätigten Ziele mit welchen Trade-offs erfüllen kann.

## Leitgedanke

> Ein Qualitätswort wird erst durch Kontext, Ziel und Bewertungskriterium zu einer belastbaren Anforderung.