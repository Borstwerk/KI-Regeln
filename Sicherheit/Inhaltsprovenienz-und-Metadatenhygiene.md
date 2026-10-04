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

## Textsignale getrennt behandeln

Bei Text mindestens drei technisch verschiedene Klassen auseinanderhalten:

### 1. Deterministische Artefakte

Beispiele können sein:

- unerwartete Zero-Width-/Tag-Zeichen;
- bestimmte Bidi-/Default-Ignorable-Steuerzeichen;
- ungewöhnliche Private-Use- oder Noncharacter-Zeichen;
- unbeabsichtigte Homoglyphen oder technisch schädliche Whitespace-Artefakte.

Wenn Position und Funktion konkret geprüft werden können, ist ein gezielter Before/After-Check möglich.

Aber auch hier gilt: Das Zeichen selbst beweist **keinen** bestimmten Generator. Derselbe Codepoint kann legitime Sprach-, Emoji-, Layout- oder Typografiefunktion besitzen.

### 2. Statistische / tokenbasierte Signale

Ein statistisches Text-Watermark oder ein Detektorsignal lebt nicht als einzelnes unsichtbares Zeichen in der Datei.

Daraus folgt:

- Unicode-/Metadaten-Cleaning beweist keine Entfernung statistischer Signale;
- ein Rewrite kann Tokenmuster verändern, ist aber ohne passenden Detector/Key kein verifizierter „Watermark-Remove“;
- fehlende lokale Detection ist kein Herkunftsbeweis;
- ein Stylometry-/Burstiness-/Phrase-Score ist höchstens Diagnose-Evidence für genau seine gemessenen Merkmale.

### 3. Sprachqualität / Voice

Generische, gleichförmige oder künstlich klingende Prosa ist ein Schreibqualitätsproblem und gehört primär zu `natuerliches-schreiben`, `stilreview` oder `korrekturlektorat`.

Bei Rewrite müssen insbesondere geschützt bleiben:

- Claims und Fakten;
- Zahlen, Namen und Zitate;
- Unsicherheit und Einschränkungen;
- Fachbegriffe, Code, Pfade, URLs und Identifikatoren;
- erforderliche Disclosure-/Attributionsangaben;
- beobachtbare Eigenheiten einer tatsächlichen Autorstimme, solange sie kein klares Verständlichkeitsproblem erzeugen.

Nicht jeden ungewöhnlichen Rhythmus oder jede Wiederholung „wegpolieren“, nur weil sie von einem Heuristik-Score als auffällig bewertet wird.

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

Methodische Referenz ist `guillaumemeyer/watermarks-remover`, geprüft am Repository-Commit `1181fd4e8cc581931a5ee672697a646721e92c78` (MIT).

Besonders relevant sind inzwischen sowohl `remove-ai-marks` als auch der getrennte `clean-user-facing-text`-Skill.

Übernommen werden Konzepte wie:

- Inspect-first;
- Trennung verschiedener Provenienz-/Markerklassen;
- deterministische Unicode-Hygiene getrennt von statistischer Rewrite-Evidence;
- Schutz nicht-prosaischer und inhaltlich stabiler Bereiche;
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
