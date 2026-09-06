# Workflow: Persönliche Finanzplanung

## Zweck

Ein wiederholbarer Ablauf für persönliche Finanzplanung von der Ausgangslage bis zu Szenarien und optionaler Anlageanalyse, ohne aus Analyse automatisch Finanzaktionen abzuleiten.

## Wann verwenden

- Gesamtüberblick über persönliche Finanzen;
- Spar-/Rücklagen-/Schuldenprioritäten;
- langfristige Vermögensentwicklung;
- bestehendes Portfolio als Teil des Gesamtplans;
- Rebalancing eines Portfolios gegen eine bestätigte Zielallokation;
- Vergleich neuer Anlageoptionen innerhalb bestätigter Ziele.

Für eine einzelne eng begrenzte Frage nur den passenden Skill verwenden.

## Ablauf

### 1. Ziel und Scope

Klären:

- Was soll finanziell erreicht oder entschieden werden?
- Welcher Zeithorizont ist relevant?
- Welche Daten dürfen verwendet/persistiert werden?
- Welche Jurisdiktion ist für Steuer-/Rechtsfragen relevant?

### 2. Finanzbaseline

`finanzstatus-und-cashflow`

Ergebnis:

- Vermögen/Verbindlichkeiten;
- Cashflow;
- Liquidität;
- Verpflichtungen;
- Missing Evidence.

Ohne tragfähige Baseline keine scheinpräzise Optimierung.

### 3. Liquiditätsreserve

Optional `ruecklagenplanung`.

Konkrete Risiken und Einkommensstabilität vor universellen Faustregeln.

### 4. Schulden

Optional `schuldenstrategie`.

Kosten, Liquidität, Risiko und Vertragsbedingungen gemeinsam betrachten.

### 5. Vermögensentwicklung

`vermoegensprojektion`

Mehrere Szenarien mit expliziten Rendite-, Inflations-, Kosten- und gegebenenfalls Steuerannahmen. Projektion nicht als Prognose darstellen. Materielle Risiken können über gezielte Stress-/What-if-Szenarien geprüft werden, ohne ihnen erfundene Eintrittswahrscheinlichkeiten zu geben.

### 6. Vorhandenes Portfolio

Optional `portfolioanalyse`.

Read-only Struktur-, Konzentrations-, Kosten-, Liquiditäts- und Risikoprüfung. Exakte aktuelle Aussagen brauchen aktuelle Produkt-/Marktdaten.

### 7. Portfolio-Rebalancing

Optional `portfolio-rebalancing`, aber nur bei explizitem Änderungsauftrag und bestätigter Zielallokation beziehungsweise autorisierten Zielbändern.

Abweichungen, neue Cashflows, Kosten, Liquidität und belegte Steuerfolgen gemeinsam betrachten. Keine Zielallokation oder universelle Rebalancing-Bandbreite erfinden. Der Rebalancing-Plan bleibt vor realen Orders read-only.

### 8. Neue Anlageoptionen

Optional `anlagevergleich`.

Nur Optionen vergleichen, die zum bestätigten Ziel/Zeithorizont passen. Aktuelle Gebühren, Steuerregeln und Produkteigenschaften mit aktueller Evidence.

Für eine tiefergehende Unternehmens- oder Bewertungsfrage kann der separate Workflow `Unternehmens-und-Investmentanalyse.md` verwendet werden.

### 9. Synthese

Ergebnis als priorisierte Entscheidungspunkte:

```text
jetzt stabilisieren
→ nächste sinnvolle Finanzentscheidung
→ langfristige Szenarien
→ optionale Portfolio-/Rebalancingfragen
→ optionale Anlagefragen
```

Dabei Annahmen, Unsicherheiten und Zielkonflikte sichtbar lassen.

### 10. Human Gate

Plan, Analyse, Rebalancing-Vorschlag oder Vergleich autorisiert keine:

- Überweisung;
- Kontoeröffnung/-schließung;
- Kreditaufnahme/-änderung;
- Vertragsänderung;
- Kauf-/Verkaufsorder;
- sonstige externe Finanzaktion.

Vor realer Ausführung ist eine separate lokale Freigabe erforderlich.

### 11. Review und Pflege

Plan bei materiellen Änderungen aktualisieren, zum Beispiel geänderte Ziele, Einkommen, Schulden, größere Ausgaben oder Portfolio-/Produktänderungen.

Bei qualitativer Revision kann `Review-Revise-Loop` verwendet werden.

## Completion

Abgeschlossen ist der Workflow, wenn:

- Ausgangsdaten und Datenstand sichtbar sind;
- Ziele und Zeithorizont feststehen oder als offen markiert sind;
- relevante Risiken, Kosten und Liquidität berücksichtigt wurden;
- Projektionen als Annahmenszenarien erkennbar sind;
- Rebalancing nur gegen bestätigte Ziele erfolgt;
- aktuelle/jurisdiktionsabhängige Fakten belegt oder als Missing Evidence markiert sind;
- reale Finanzaktionen separat gegatet bleiben.

## Leitgedanke

> Ein guter Finanzplan macht Entscheidungen belastbarer. Er macht die Zukunft nicht sicher.