# Validation, Verifikation und Readiness

## Zweck

Requirements werden geprüft, bevor ihre Fehler teuer in Design, Code, Daten oder Betrieb eingebaut werden. Dabei müssen mehrere Begriffe sauber getrennt bleiben.

## Requirements Validation

Requirements Validation fragt sinngemäß:

> Beschreiben diese Requirements tatsächlich den relevanten Bedarf und sind sie geeignet, das richtige Produkt beziehungsweise die richtige Änderung zu bauen?

Prüfachsen:

- Stakeholder-/Ziel-Fit;
- Scope und Vollständigkeit für die anstehende Entscheidung;
- Klarheit und Eindeutigkeit;
- Konsistenz und Konfliktfreiheit;
- Notwendigkeit / Herkunft;
- Feasibility-Risiken oder offene Annahmen;
- Verifizierbarkeit;
- Traceability;
- relevante nominale und off-nominale Szenarien.

## Requirements Verification

Je nach Terminologie wird damit die Prüfung bezeichnet, ob Requirements selbst definierte Qualitäts-/Formregeln erfüllen. Im Repo verwenden wir möglichst konkret `Requirement Quality Check` beziehungsweise `Requirements Validation`, um Verwechslungen mit Product Verification zu vermeiden.

## Product Verification

```text
Requirement
→ Umsetzung
→ Test / Analyse / Inspektion / Demonstration
→ Evidence, dass die implementierte Lösung das Requirement erfüllt
```

Die konkrete Product Verification gehört zu `Testing-und-QA/` und anderen zuständigen Fachprozessen.

## Product Validation

Product Validation fragt, ob das resultierende Produkt im beabsichtigten Nutzungskontext tatsächlich den Stakeholderbedarf erfüllt. Sie ist breiter als Requirements Validation und kann Nutzer-/Betriebsevidence benötigen.

## Readiness

Ein Requirements-Paket ist nicht deshalb `ready`, weil alle Felder eines Templates gefüllt sind.

Für einen Downstream-Handoff prüfen:

- relevante Sources und Stakeholder ausreichend abgedeckt;
- kritische Konflikte entschieden oder explizit blockierend;
- Scope/Non-Goals klar;
- entscheidungsrelevante Annahmen sichtbar;
- funktionale und qualitative Anforderungen ausreichend konkret;
- Acceptance-/Verification-Intent für kritische Requirements vorhanden;
- Traceability/Provenance für relevante Aussagen vorhanden;
- offene Punkte nach Wirkung priorisiert;
- Downstream-Consumer kennt verbleibende Unsicherheit.

Mögliche Verdicts:

- `READY_FOR_LOCAL_GATE`
- `READY_WITH_GAPS`
- `BLOCKED`
- `UNVERIFIED`

Das Verdict autorisiert keine Architektur-, Implementierungs-, Merge-, Deployment- oder Releaseaktion.

## Leitgedanke

> Requirements Readiness bedeutet ausreichend belastbare Grundlage für die nächste Entscheidung – nicht perfekte Dokumentfülle.