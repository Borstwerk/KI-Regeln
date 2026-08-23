# Beispiele, Code und Verifikation

## Zweck

Beispiele sind nicht nur Illustration. In technischer Dokumentation werden sie häufig direkt kopiert und ausgeführt.

## Grundsatz

> Ein Beispiel ist erst dann belastbar, wenn geprüft wurde, dass es zum beschriebenen System passt.

## Ausführbare Beispiele bevorzugen

Wenn ein Beispiel ausführbar sein soll:

- vollständige notwendige Imports oder Voraussetzungen nennen;
- echte Parameter- und Funktionsnamen verwenden;
- keine erfundenen APIs;
- erwartetes Ergebnis zeigen;
- unnötigen Beispielballast vermeiden.

## Beispiele testen

Wo praktisch möglich:

- Befehle ausführen;
- Codebeispiele kompilieren oder testen;
- API-Beispiele gegen Schema oder Testumgebung prüfen;
- Konfigurationsbeispiele gegen Parser oder Schema validieren;
- Beispielausgaben mit dem tatsächlichen Verhalten vergleichen.

Nicht ausgeführte Beispiele nicht als „getestet“ darstellen.

## Links prüfen

Vor Freigabe wichtiger Dokumentation:

- interne Links;
- externe Links;
- Anker;
- Versionslinks;
- Download- oder Installationspfade

prüfen oder ausdrücklich als ungeprüft kennzeichnen.

## Parameter gegen Source of Truth prüfen

Besonders bei Reference und API-Dokumentation:

- Name;
- Typ;
- Default;
- Pflicht/optional;
- Wertebereich;
- Version;
- Fehlermeldungen

gegen das kanonische Schema oder die tatsächliche Implementierung prüfen.

## Realistische Beispiele

Verwende kleine realistische Beispiele statt künstlicher Komplexität.

Platzhalter müssen als Platzhalter erkennbar sein.

Keine scheinbar realen:

- Tokens;
- Kundendaten;
- Zugangsdaten;
- Hostnamen;
- produktiven IP-Adressen;
- Kennzahlen

erfinden.

## Sicherheitskritische Befehle

Bei destruktiven oder riskanten Befehlen:

- Wirkung klar benennen;
- Voraussetzungen nennen;
- Scope sichtbar machen;
- wenn möglich sicheren Prüf- oder Dry-Run-Schritt voranstellen;
- Rollback oder Recovery nennen, sofern vorhanden.

## Screenshots

Screenshots eignen sich für Orientierung, können aber schnell veralten.

Vor Nutzung prüfen:

- ist die UI-Version aktuell?
- zeigt der Screenshot nur notwendige Informationen?
- enthält er sensible Daten?
- gibt es textliche Alternativen?
- muss er bei UI-Änderungen gezielt mitgepflegt werden?

## Verifikationsstatus sichtbar halten

Für umfangreiche oder betriebsrelevante Dokumentation kann ein kleiner Status sinnvoll sein:

```text
Beispiele: geprüft
Links: geprüft
Version: 4.2
Letzte fachliche Prüfung: 2026-08-23
```

Das ersetzt keine echte Wartung, macht Veraltung aber leichter erkennbar.

## Leitgedanke

> Dokumentation wird nicht dadurch korrekt, dass ihr Codeblock plausibel aussieht.
