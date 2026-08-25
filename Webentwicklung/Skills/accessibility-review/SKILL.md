---
name: accessibility-review
description: Prüft Weboberflächen auf relevante Accessibility-Anforderungen in Semantik, Tastaturbedienung, Fokus, Kontrast, Formularen und dynamischen Zuständen. Verwenden vor Freigaben neuer oder geänderter Oberflächen sowie bei interaktiven Komponenten und Accessibility-Regressionsrisiken.
---

# Skill: Accessibility Review

## Zweck

Prüfe eine Weboberfläche auf grundlegende und relevante Accessibility-Anforderungen in Semantik, Tastaturbedienung, Fokus, Kontrast, Formularen und dynamischen Zuständen.

## Verwenden wenn

- eine neue oder geänderte Weboberfläche vor Freigabe geprüft wird;
- Formulare, Dialoge, Navigation oder interaktive Komponenten betroffen sind;
- Accessibility-Regressionsrisiken bestehen.

## Eingaben

- gerenderte Oberfläche;
- relevanter Quellcode, sofern verfügbar;
- lokale Browser-/Accessibility-Anforderungen;
- vorhandene automatisierte Checks.

## Arbeitsweise

1. Prüfe native Semantik vor ARIA.
2. Bediene den Kernflow per Tastatur.
3. Prüfe sichtbare und logische Fokusführung.
4. Prüfe Labels, Fehlermeldungen und Formularzusammenhänge.
5. Prüfe Kontrast und Statuskommunikation.
6. Prüfe Bilder/Medien auf angemessene Alternativen.
7. Prüfe Motion-Präferenzen und vermeidbare Bewegung.
8. Prüfe Zoom/Reflow und kleine Viewports.
9. Nutze automatisierte Accessibility-Checks, falls vorhanden.
10. Unterscheide automatisch gefundene Hinweise von manuell bestätigten Problemen.

## Ausgabe

```text
Geprüfte Flows/Zustände
Automatisierte Checks
Manuelle Tastatur-/Fokusprüfung
Blocker
Hohe/Mittlere/Kleine Funde
Nicht geprüfte Bereiche
Offene Risiken
```

## Regeln

- Placeholder ersetzt kein Label.
- Farbe ist nie das einzige Statussignal.
- Ein `div` mit Click-Handler ist nicht automatisch ein guter Button.
- Automatisierte Checks beweisen nicht vollständige Accessibility.
- Ungeprüft bedeutet nicht bestanden.

## Stop-Regeln

Stoppe oder eskaliere, wenn:

- eine lokale Compliance-Anforderung unklar ist;
- ein Fix breite Architektur-/Designänderungen benötigt;
- relevante assistive Technik nicht verfügbar ist und dadurch keine belastbare Aussage möglich ist.

## Leitgedanke

> Accessibility wird geprüft wie Funktionalität: mit echter Bedienung, nicht nur mit gut gemeintem Markup.