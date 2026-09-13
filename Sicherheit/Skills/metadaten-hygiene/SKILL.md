---
name: metadaten-hygiene
description: Eigene oder ausdrücklich autorisiert bearbeitete Dateien kontrolliert auf unnötige, sensible oder unbeabsichtigte Metadaten bereinigen, ohne erforderliche Provenienz-, Disclosure-, Rechte- oder Fachinformationen blind zu entfernen. Verwenden bei Privacy- und Datei-Hygiene vor Weitergabe; nicht für Detector-Evasion, sichtbare Fremd-Watermarks oder die Verschleierung erforderlicher Herkunftsangaben.
---

# Metadaten-Hygiene

Nutze die Regeln aus `../../Inhaltsprovenienz-und-Metadatenhygiene.md`.

## Verantwortung

Dieser Skill beantwortet:

> Welche Metadaten dürfen und sollen aus einem autorisierten Artefakt für den konkreten Zweck entfernt, reduziert oder erhalten werden, und wie wird die Änderung verifiziert?

Typische legitime Ziele:

- GPS-, Geräte- oder Bearbeitungsmetadaten aus eigenen Dateien vor Veröffentlichung reduzieren;
- unnötige Dokumenteigenschaften wie Autor-/Softwarefelder aus einer freigegebenen Kopie entfernen;
- unbeabsichtigte technische Metadaten minimieren;
- ungewöhnliche Unicode-Artefakte in autorisiertem Text gezielt bereinigen, sofern ihre Funktion verstanden ist;
- eine saubere Sharing-Kopie erzeugen und danach erneut prüfen.

## Autorisierung und Scope

Vor jeder Änderung klären:

1. Ist der Inhalt Eigentum des Nutzers oder ausdrücklich zur Bearbeitung autorisiert?
2. Was ist das konkrete Hygiene-/Privacy-Ziel?
3. Welche Metadaten müssen erhalten bleiben?
4. Welche Datei oder Kopie darf verändert werden?
5. Ist die gewünschte Änderung reversibel oder existiert ein Original?

Ein allgemeiner Review-Auftrag autorisiert keine Bereinigung. Eine explizite Bitte wie „entferne die GPS-Metadaten aus meiner Datei“ autorisiert genau diesen begrenzten Scope.

## Erhaltspflichten

Nicht blind entfernen:

- gesetzlich, vertraglich, akademisch oder plattformseitig erforderliche Disclosure-/Provenienzangaben;
- Rechte-, Lizenz-, Copyright- oder Attribution-Hinweise, wenn ihre Entfernung Rechte oder Pflichten verschleiern würde;
- fachlich relevante Dokumenteigenschaften, die für Nachvollziehbarkeit, Audit, Archivierung oder Workflow benötigt werden;
- Signatur-/Integritätsinformationen, deren Entfernung den Nutzer über die Wirkung täuschen würde;
- legitime Unicode-/Bidi-/Whitespace-Zeichen mit semantischer oder typografischer Funktion.

Wenn die Erhaltungspflicht unklar ist, die Unsicherheit sichtbar machen und keine irreversible Bereinigung als sicher darstellen.

## Nicht verantwortlich für

- sichtbare Fremd-Watermarks oder Logos aus Bildern entfernen;
- statistische Text-Watermarks durch detector-getriebene Paraphrase schwächen;
- AI-Detector-Scores optimieren oder „human-written“ vortäuschen;
- Watermark-Stealing, Secret-Key-Rekonstruktion oder Verifikationsumgehung;
- verpflichtende Provenienz absichtlich zur Täuschung entfernen;
- eine Datei allein aufgrund vermuteter KI-Herkunft zu reinigen.

Für natürliche Textüberarbeitung ist `natuerliches-schreiben` zuständig. Für reine Bestandsaufnahme ist zuerst `inhaltsprovenienz-review` zuständig.

## Arbeitsweise

### 1. Inspect first

Vor dem Clean den Ist-Zustand erfassen:

- konkrete Metadatenfelder / Provenienzsignale;
- Format und Toolfähigkeiten;
- gewünschte Entfernung versus Erhaltung;
- potenzielle Nebenwirkungen.

### 2. Change Set formulieren

Vor der Änderung explizit trennen:

- **remove** – konkret autorisierte Felder/Artefakte;
- **keep** – bewusst zu erhaltende Felder;
- **unknown** – unklare oder nicht interpretierbare Informationen;
- **unsupported** – mit den vorhandenen Tools nicht sicher bearbeitbar.

`strip all metadata` ist kein Universaldefault.

### 3. Sicher ausführen

Wenn möglich:

- neue bereinigte Kopie statt Original überschreiben;
- kleinsten ausreichenden Eingriff verwenden;
- Format und Nutzdaten erhalten;
- keine unnötige Re-Encoding-/Qualitätsverschlechterung erzeugen;
- Toolbericht und tatsächliches Ergebnis nicht verwechseln.

### 4. Re-Inspection

Nach der Änderung erneut prüfen:

- wurden nur die freigegebenen Metadaten entfernt?
- blieben die Keep-Felder erhalten?
- ist die Datei weiterhin lesbar/nutzbar?
- sind nicht prüfbare Residual-Risiken sichtbar?

Ein erfolgreiches Strippen von EXIF/XMP/C2PA-Containerdaten beweist nicht, dass keine andere Provenienz- oder Watermark-Klasse mehr existiert.

## Status

Geeignete Abschlusszustände:

- `CLEANED_AS_REQUESTED` – autorisierte Änderung verifiziert;
- `CLEANED_WITH_RESIDUAL_RISK` – Änderung erfolgreich, weitere Klassen nicht verifizierbar;
- `BLOCKED_BY_REQUIRED_METADATA` – gewünschte Entfernung kollidiert mit bestätigter Erhaltungspflicht;
- `UNVERIFIED` – Tool-/Formatgrenze verhindert belastbare Aussage;
- `NO_CHANGE_NEEDED` – kein autorisierter Hygiene-Bedarf gefunden.

## Abschluss

Vor Abschluss prüfen:

1. War die Änderung ausdrücklich autorisiert?
2. Wurden erforderliche Angaben erhalten?
3. Wurde nur der minimale freigegebene Scope verändert?
4. Existiert nach Möglichkeit ein unverändertes Original?
5. Wurde der Endzustand erneut inspiziert?
6. Wurde keine Detector-Evasion oder menschliche Urheberschaft behauptet?
