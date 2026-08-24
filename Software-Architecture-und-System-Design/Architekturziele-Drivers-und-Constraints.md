# Architekturziele, Drivers und Constraints

## Zweck

Architekturentscheidungen beginnen mit den Kräften, die eine Struktur tatsächlich formen. Patternnamen, Frameworkpräferenzen und Diagrammkonventionen sind keine Architecture Drivers.

## Typische Drivers

- funktionale Fähigkeiten und kritische End-to-End-Flows;
- fachliche Invarianten und Sources of Truth;
- messbare Qualitätsanforderungen wie Latenz, Verfügbarkeit, Änderbarkeit oder Recovery;
- Lastform, Datenvolumen, Burst, Fan-out, Skew oder Hotspots;
- Sicherheits-, Datenschutz- oder regulatorische Anforderungen;
- Team-, Ownership-, Betriebs- und Kostenconstraints;
- Integrationen, bestehende Plattformen und irreversible Legacygrenzen;
- Migrationsfenster, Compatibility und zulässige Zwischenzustände.

## Driver ≠ Wunschliste

Aussagen wie `skalierbar`, `modern`, `cloud-native`, `wartbar` oder `enterprise-ready` sind ohne Szenario nicht entscheidungsfähig.

Stattdessen konkretisieren:

```text
Stimulus
→ betroffener Systemteil
→ erwartete Reaktion
→ messbares oder beobachtbares Ergebnis
→ relevante Grenze / Constraint
```

Beispiel:

```text
Ein externer Provider antwortet 30 Sekunden nicht
→ Checkout bleibt erreichbar
→ keine Doppelbuchung
→ Request endet innerhalb lokaler Deadline
→ Retry-Verantwortung ist eindeutig
```

## Annahmen und Evidence

Jeder wesentliche Driver erhält einen Status:

- `CONFIRMED` – durch verbindliche Anforderung oder belastbare Evidence gestützt;
- `ASSUMED` – für den Entwurf angenommene, noch nicht bestätigte Grundlage;
- `UNVERIFIED` – relevante Aussage ohne ausreichende Evidence;
- `CONFLICTING` – Quellen oder Ist-Zustand widersprechen sich.

Keine erfundenen QPS-, SLO-, RTO-/RPO-, Kosten- oder Teamwerte einsetzen, nur damit ein Design vollständig aussieht.

## Requirement-Grenze

Architecture darf Anforderungen operationalisieren und auf Entscheidungsrelevanz prüfen. Sie darf fehlende Produkt- oder Qualitätsziele nicht selbst verbindlich festlegen.

Wenn ein fehlender Wert die Strukturentscheidung verändert:

1. Unsicherheit markieren;
2. Sensitivität der Entscheidung zeigen;
3. an Requirements beziehungsweise lokale Stakeholderentscheidung übergeben.

## Leitgedanke

> Eine Architektur ist nur so begründet wie die Drivers, die ihre Struktur tatsächlich erzwingen.