# Inhaltsprovenienz und Metadatenhygiene

## Zweck

Diese Fachgrundlage trennt zwei Jobs, die technisch eng verwandt, aber in Wirkung und Autorisierung verschieden sind:

- **Inhaltsprovenienz-Review** – vorhandene Provenienz- und Metadatensignale read-only untersuchen;
- **Metadaten-Hygiene** – eigene oder ausdrücklich autorisierte Artefakte gezielt bereinigen.

Die Trennung verhindert, dass aus einem Analysefund automatisch ein Entfernungsauftrag wird.

## Kernmodell

```text
Artefakt
→ unterstützte Prüfklassen bestimmen
→ inspect
→ Evidence klassifizieren
→ Zweck / Autorisierung / Erhaltungspflichten
→ optional begrenztes Change Set
→ Human Gate soweit erforderlich
→ bereinigen
→ re-inspect
→ Residual Risk
```

## Provenienzklassen

Je nach Format und verfügbarer Tooling-Evidence können relevant sein:

- C2PA / Content Credentials und andere strukturierte Provenienzcontainer;
- EXIF, XMP und andere Bild-/Medienmetadaten;
- Dokumenteigenschaften in Office-, PDF-, EPUB- oder vergleichbaren Containern;
- Autor-, Software-, Geräte-, Generator- und Bearbeitungsfelder;
- sichtbare Herkunftshinweise;
- ungewöhnliche Unicode-, Tag-, Bidi-, Whitespace- oder Homoglyph-Artefakte in Text;
- weitere eingebettete Signale, sofern ein konkretes Tool sie tatsächlich verifizieren kann.

Nicht jede Klasse ist in jedem Format vorhanden oder mit jedem Tool prüfbar.

## Evidence statt Herkunftsmythos

Provenienz ist kein binärer AI-/Human-Schalter.

Es gilt:

> Ein gefundener Marker beweist nur das, was dieser Marker und sein Trust-Kontext tatsächlich aussagen.

> Kein gefundener Marker beweist nicht, dass ein Inhalt ohne KI, ohne Bearbeitung oder ohne bestimmte Software entstanden ist.

> Entfernte Metadaten beweisen nicht, dass keine anderen Provenienzsignale mehr vorhanden sind.

Toolausgaben, Herstellerfelder oder Dateinamen dürfen nicht zu größeren Authorship-Claims aufgeblasen werden.

## Inspect-first

Vor einer Bereinigung immer zuerst den Ist-Zustand bestimmen, sofern das Artefakt und die Tools dies zulassen.

Die Inspektion soll mindestens unterscheiden:

- tatsächlich beobachtete Felder oder Strukturen;
- interpretierte Bedeutung;
- Confidence;
- nicht unterstützte Prüfklassen;
- mögliche False Positives oder legitime Erklärungen.

Ein Tool, das C2PA lesen kann, kann damit nicht automatisch statistische Text- oder Pixel-Watermarks beurteilen. Capability Detection gehört zur Evidence.

## Unicode-Hygiene

Unsichtbare oder ungewöhnliche Unicode-Zeichen können technische Artefakte, beabsichtigte Typografie oder notwendige Sprach-/Layoutinformation sein.

Besonders vorsichtig behandeln:

- NBSP und Narrow NBSP;
- Bidi-Steuerzeichen;
- CJK-Spaces;
- Zero-width-Zeichen;
- Variation Selectors und Emoji-Verbindungen;
- Homoglyphen;
- Unicode-Normalisierung.

Die Regel lautet:

> auffällig ≠ schädlich

> ungewöhnlich ≠ Watermark

> normalisierbar ≠ sollte normalisiert werden

Aggressive Normalisierung nur nach konkretem Zweck und mit Prüfung möglicher semantischer, sprachlicher oder typografischer Nebenwirkungen.

## Privacy-Hygiene

Legitime Hygieneziele können sein:

- GPS- oder Geräteinformationen vor externer Weitergabe minimieren;
- unbeabsichtigte Autor-/Softwarefelder entfernen;
- unnötige technische Metadaten reduzieren;
- eine separate Sharing-Kopie erzeugen;
- technische Textartefakte entfernen, die Suche, Diff oder Copy/Paste stören.

Datensparsamkeit ist ein legitimes Ziel. Sie ist aber kein Freibrief, notwendige Herkunfts-, Rechte-, Audit- oder Disclosure-Information zu entfernen.

## Erhaltungspflichten

Vor einem Change Set prüfen, ob Metadaten oder Provenienzsignale für den konkreten Kontext erhalten bleiben müssen, etwa wegen:

- gesetzlicher oder regulatorischer Vorgaben;
- akademischer oder institutioneller Disclosure-Regeln;
- Plattformbedingungen;
- Lizenz, Copyright oder Attribution;
- Signatur, Integrität oder Auditierbarkeit;
- lokaler Workflow-, Archiv- oder Compliance-Anforderungen.

Wenn die Rechts- oder Policy-Lage nicht belegt ist, keine pauschale Zulässigkeitsbehauptung erfinden.

## Detector-Evasion ist kein lokales Produktziel

Nicht aus diesem Bereich ableiten:

- Optimierung auf GPTZero-, Pangram-, Originality-, Turnitin- oder andere Detector-Scores;
- statistische Text-Watermark-Reduktion als Selbstzweck;
- „humanization“ zur Täuschung über Urheberschaft;
- Watermark-Stealing oder Secret-Key-Rekonstruktion;
- gezielte Zerstörung von Verifikationssignalen, um verpflichtende Transparenz zu umgehen.

Bei einem vorhandenen Text bleibt Qualität bei `natuerliches-schreiben`, `stilreview`, `korrekturlektorat` oder `deutsche-typografie`. Ein Detector-Hinweis kann Anlass für echten Textreview sein, aber kein eigenes Akzeptanzziel.

## Sichtbare Watermarks

Ein sichtbares Logo, Stock-Watermark oder eingebrannter Schriftzug ist kein Metadatenproblem.

Daher:

- nicht über `metadaten-hygiene` routen;
- Eigentum, Lizenz und Bearbeitungsrecht separat klären;
- Bild-/Medienbearbeitung nur im tatsächlich autorisierten Scope durchführen.

## Minimaler Eingriff

Bei einer autorisierten Bereinigung:

1. Original oder belastbare Rückfallebene erhalten, soweit praktisch;
2. konkretes Remove-/Keep-Set definieren;
3. kleinsten ausreichenden Eingriff wählen;
4. unnötiges Re-Encoding oder Inhaltsänderung vermeiden;
5. Ergebnis erneut inspizieren;
6. Residual Risk sichtbar lassen.

`strip all metadata` ist kein Default.

## Upstream-Einordnung

Methodische Referenz ist `guillaumemeyer/watermarks-remover`, geprüft am Repository-Commit `d9e9590d94e19b39eb2794266292324bfec8249a` (MIT).

Übernommen werden Konzepte wie:

- Inspect-first;
- Trennung verschiedener Provenienz-/Markerklassen;
- Capability Detection;
- Before/After-Evidence;
- False-Positive- und Residual-Risk-Denken;
- die Trennung verifizierbarer Entfernung von best-effort Aussagen.

Bewusst **nicht** übernommen werden:

- Detector-Evasion als Produktziel;
- statistische Rewrite-Rezepte zur Watermark-Reduktion;
- Watermark-Stealing;
- destructive Pixel-/Audio-/Video-Purification als zentrale Standardfähigkeit;
- vendor- oder toolgebundene Service-, Plugin-, Docker-, HTTP- oder Modellarchitektur;
- pauschales Entfernen von Provenienzsignalen ohne Rechte-/Disclosure-Prüfung.

Das Upstream-Repository ist Methodenreferenz, keine Runtime- oder Sync-Abhängigkeit.

## Leitgedanken

> Erst feststellen, was tatsächlich vorhanden ist. Dann entscheiden, was wirklich weg darf.

> Privacy-Hygiene darf Provenienz nicht in Täuschung verwandeln.

> Keine Markierung gefunden ist kein Herkunftsbeweis.
