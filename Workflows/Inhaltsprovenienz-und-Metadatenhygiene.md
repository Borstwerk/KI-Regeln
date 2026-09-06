# Workflow – Inhaltsprovenienz und Metadatenhygiene

## Ziel

Vorhandene Dateien oder Inhalte zuerst auf belegbare Provenienz- und Metadatensignale prüfen und nur bei einem ausdrücklich autorisierten Hygiene-/Privacy-Ziel ein begrenztes, verifizierbares Change Set anwenden.

Der Workflow verbindet read-only Review und optionale Bereinigung, ohne aus einem Fund automatisch eine Entfernung abzuleiten.

## Ablauf

```text
Artefakt + Nutzerziel
→ inhaltsprovenienz-review
→ Befunde / Confidence / Unsupported Classes
→ Bereinigung überhaupt gewünscht und autorisiert?
   ├─ nein → Review-Ergebnis
   └─ ja
      → Erhaltungspflichten / Rechte / Disclosure
      → Remove / Keep / Unknown / Unsupported
      → Human Gate soweit erforderlich
      → metadaten-hygiene
      → Re-Inspection
      → Residual Risk / Abschlussstatus
```

## 1. Auftrag und Artefakt bestimmen

Klären:

- welche konkrete Datei oder Fassung geprüft wird;
- ob nur Analyse oder auch Änderung gewünscht ist;
- ob der Inhalt dem Nutzer gehört oder zur Bearbeitung autorisiert ist;
- welcher Weitergabe-, Privacy-, Hygiene- oder Audit-Zweck vorliegt;
- welche Tools und Formate tatsächlich unterstützt werden.

Keine Eigentums- oder Rechteannahme erfinden, wenn sie für eine Änderung materiell ist.

## 2. Read-only Provenienz-Review

Mit `inhaltsprovenienz-review`:

- vorhandene Metadaten- und Provenienzklassen prüfen;
- beobachtete Evidence von Interpretation trennen;
- Confidence und False-Positive-Grenzen nennen;
- nicht unterstützte Klassen als `UNVERIFIED` markieren;
- keine menschliche oder KI-Urheberschaft aus bloßer Marker-Abwesenheit ableiten.

Wenn der Nutzer nur wissen wollte, was in der Datei steckt, endet der Workflow hier.

## 3. Bereinigungsziel und Erhaltungspflichten

Nur weitergehen, wenn eine Änderung gewünscht und autorisiert ist.

Vor dem Change Set prüfen:

- Privacy-Ziel;
- Lizenz-/Attribution-Pflichten;
- gesetzliche, akademische, regulatorische oder Plattform-Disclosure;
- Signatur-/Integritätswirkung;
- Audit-/Archivierungsbedarf;
- semantische oder typografische Funktion ungewöhnlicher Unicode-Zeichen.

Unklare Rechts- oder Policy-Fragen nicht mit plausiblen Defaults beantworten.

## 4. Change Set

Explizit festhalten:

- `remove` – konkret autorisierte Metadaten;
- `keep` – bewusst zu erhaltende Metadaten;
- `unknown` – unklare Felder;
- `unsupported` – mit vorhandenen Fähigkeiten nicht sicher bearbeitbar.

Beispiele:

```text
remove: GPS, Kamera-Seriennummer
keep: Copyright/Attribution, Aufnahmezeit
unknown: proprietäres MakerNote
unsupported: Pixel-Watermark-Prüfung
```

`strip all metadata` nur dann, wenn dies ausdrücklich gewünscht, zulässig und mit den Erhaltungspflichten vereinbar ist.

## 5. Human Gate

Ein neuer Human Gate ist erforderlich, wenn während der Analyse ein zusätzlicher, zuvor nicht autorisierter Eingriff vorgeschlagen wird oder eine relevante Erhaltungspflicht/Integritätswirkung eine neue Entscheidung verlangt.

Ein bereits ausdrücklicher Auftrag wie „erstelle aus meinem Foto eine Kopie ohne GPS“ autorisiert diesen begrenzten Change Scope; er autorisiert nicht automatisch weitere Entfernung.

## 6. Bereinigung

Mit `metadaten-hygiene`:

- wenn möglich eine neue Sharing-/Clean-Kopie erzeugen;
- minimalen Eingriff verwenden;
- Nutzdaten und Format erhalten;
- unnötiges Re-Encoding vermeiden;
- keine statistische Detector-Evasion oder sichtbare Watermark-Bearbeitung hineinziehen.

## 7. Re-Inspection

Nach der Änderung erneut mit passenden Inspektionsfähigkeiten prüfen:

- Remove-Set tatsächlich entfernt?
- Keep-Set erhalten?
- Datei weiterhin intakt und nutzbar?
- neue oder verbliebene relevante Metadaten?
- nicht unterstützte Provenienzklassen weiterhin `UNVERIFIED`?

## 8. Abschluss

Abschlussbericht trennt:

- **verifiziert entfernt**;
- **bewusst erhalten**;
- **nicht verändert / außerhalb Scope**;
- **nicht prüfbar**;
- **Residual Risk**.

Geeignete Zustände:

- `REVIEWED`
- `CLEANED_AS_REQUESTED`
- `CLEANED_WITH_RESIDUAL_RISK`
- `BLOCKED_BY_REQUIRED_METADATA`
- `UNVERIFIED`
- `NO_CHANGE_NEEDED`

## Harte Grenzen

Nicht Bestandteil dieses Workflows:

- Detector-Score-Optimierung;
- statistische Text-Watermark-Zerstörung durch wiederholte Paraphrase;
- Watermark-Stealing;
- Secret-Key-Rekonstruktion;
- Entfernen sichtbarer Fremd-Watermarks;
- Verschleiern verpflichtender Disclosure-/Attribution-Angaben;
- Behauptung „keine Metadaten = menschlich erstellt“.

## Leitgedanken

> Review ≠ Removal Authorization.

> Entfernt ≠ nie vorhanden.

> Nicht gefunden ≠ nicht vorhanden.

> Metadaten-Hygiene dient Privacy und kontrollierter Weitergabe, nicht Herkunftstäuschung.
