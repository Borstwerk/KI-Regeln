---
name: inhaltsprovenienz-review
description: Vorhandene Dateien oder Inhalte read-only auf sichtbare und maschinenlesbare Provenienzsignale, Metadaten, Content Credentials, ungewöhnliche Unicode-Artefakte und dokumentierte Herkunftshinweise prüfen. Verwenden wenn der Nutzer wissen will, welche Provenienz-, Generator-, Geräte- oder Bearbeitungshinweise in einer Datei stecken, ohne diese bereits zu entfernen oder zu verändern.
---

# Inhaltsprovenienz-Review

Nutze die Regeln aus `../../Inhaltsprovenienz-und-Metadatenhygiene.md`.

## Verantwortung

Dieser Skill beantwortet read-only:

> Welche belegbaren Provenienz- und Metadatensignale sind in diesem Inhalt vorhanden, wie belastbar sind sie und was lässt sich daraus nicht ableiten?

Typische Prüfobjekte:

- Bild-, Audio-, Video- und Dokumentmetadaten;
- C2PA / Content Credentials oder vergleichbare dokumentierte Provenienzcontainer;
- EXIF, XMP und Dokumenteigenschaften;
- Generator-, Software-, Geräte-, Autor- oder Bearbeitungshinweise;
- ungewöhnliche Unicode-, Bidi-, Tag- oder Whitespace-Artefakte in Textdateien;
- sichtbare Hinweise, sofern sie im vorliegenden Artefakt tatsächlich erkennbar sind.

## Nicht verantwortlich für

- Entfernen oder Umschreiben von Provenienz- oder Metadaten;
- Detector-Evasion oder Optimierung eines „human score“;
- statistische Watermark-Zerstörung durch Paraphrase;
- Watermark-Stealing, Secret-Key-Rekonstruktion oder Umgehung von Verifikationssystemen;
- die Behauptung, ein Inhalt sei menschlich erstellt, nur weil keine lokale Markierung gefunden wurde;
- Urheberrechts-, Compliance- oder Rechtsberatung.

Für eine ausdrücklich autorisierte Metadatenbereinigung ist `metadaten-hygiene` zuständig. Für Textqualität oder natürliche Formulierungen bleibt `natuerliches-schreiben` zuständig.

## Inspect-first

Nicht aus Dateityp, Herkunft oder Modellgedächtnis auf vorhandene Marker schließen.

Zuerst die tatsächlich verfügbare Evidence bestimmen:

1. konkretes Artefakt und Dateiversion;
2. unterstützte Inspektionsfähigkeiten des vorhandenen Tools;
3. sichtbare und maschinenlesbare Befunde getrennt erfassen;
4. Befundklasse und Confidence dokumentieren;
5. Grenzen der Inspektion nennen.

Wenn ein Tool ein Format oder eine Provenienzklasse nicht prüfen kann, lautet der Status `UNVERIFIED`, nicht „nicht vorhanden“.

## Befundklassen

Befunde mindestens trennen in:

- **confirmed** – direkt im Artefakt nachweisbare strukturierte Evidence;
- **probable** – mehrere passende Indizien, aber kein eindeutiger Nachweis;
- **informational** – Metadatum oder Merkmal ohne belastbaren Provenienzschluss;
- **likely_false_positive** – technisch auffälliges Signal mit plausibler legitimer Erklärung;
- **unverified** – relevante Prüfklasse konnte mit den vorhandenen Fähigkeiten nicht verifiziert werden.

Ein ungewöhnliches Unicode-Zeichen ist nicht automatisch ein Watermark. Ein Softwarefeld beweist nicht, welches Modell einen Inhalt erzeugt hat. Fehlende C2PA-Daten beweisen nicht, dass keine KI beteiligt war.

## Unicode-Grenze

Bei Text insbesondere unterscheiden zwischen:

- unerwarteten unsichtbaren Steuer-/Tag-Zeichen;
- legitimen NBSP-, Narrow-NBSP-, CJK-, Bidi- oder typografischen Zeichen;
- Homoglyphen oder Normalisierungsfragen;
- tatsächlicher Funktion im konkreten Kontext.

Keine aggressive Normalisierung allein aufgrund einer Auffälligkeit empfehlen.

## Provenienz ≠ Authentizität

Es gilt:

> Provenienzsignal = Evidence über einen Bearbeitungs- oder Herkunftskanal.
>
> Provenienzsignal ≠ vollständige Entstehungsgeschichte.
>
> Kein lokales Provenienzsignal ≠ menschliche Urheberschaft bewiesen.

Auch ein erfolgreich verifiziertes Provenienzmanifest kann nur das belegen, was sein konkreter Signatur- und Trust-Kontext tatsächlich aussagt.

## Ausgabe

Ein Review enthält knapp:

1. Prüfobjekt und Scope;
2. verifizierte Befunde mit Klasse;
3. relevante Metadaten oder Provenienzsignale;
4. mögliche legitime Erklärungen / False-Positive-Grenzen;
5. nicht prüfbare Klassen und Residual Risk;
6. falls gewünscht: nächster Schritt `metadaten-hygiene`, jedoch ohne implizite Änderungsautorisierung.

## Abschluss

Vor dem Abschluss prüfen:

- Wurde nur tatsächlich beobachtete Evidence berichtet?
- Wurde „nicht gefunden“ sauber von „nicht vorhanden“ getrennt?
- Wurde kein AI-/Human-Authorship-Verdict aus Metadaten konstruiert?
- Wurden legitime Unicode-/Metadatenfälle nicht pauschal als verdächtig markiert?
- Wurde keine Entfernung oder Detector-Evasion ungefragt gestartet?
