# Batch, Streaming und Zeitsemantik

## Zweck

Batch und Streaming sind Verarbeitungsmodelle mit unterschiedlichen Betriebs- und Zeitsemantiken. Die Wahl soll aus fachlichem Bedarf, Datencharakter und Kosten entstehen – nicht aus Reife- oder Modernitätsdogmen.

## Bounded vs. unbounded

Wichtiger als Produktnamen ist zunächst:

- Ist der Input endlich/bounded oder fortlaufend/unbounded?
- Wann gilt ein Ergebnis als ausreichend vollständig?
- Welche Latenz benötigt der Consumer wirklich?
- Welche Korrekturen oder verspäteten Daten sind zu erwarten?

## Zeitbegriffe

Mindestens unterscheiden:

- **Event Time:** Zeitpunkt, zu dem das fachliche Ereignis stattfand;
- **Source/Update Time:** Zeitpunkt einer Änderung in der Quelle;
- **Ingestion Time:** Zeitpunkt der Aufnahme in die Pipeline;
- **Processing Time:** Zeitpunkt der Verarbeitung;
- **Publish/Availability Time:** Zeitpunkt, zu dem Consumer das Ergebnis sehen können.

Diese Zeitachsen können erheblich auseinanderliegen.

## Windows und Late Data

Bei zeitbasierten Aggregationen klären:

- Window-Typ und fachliche Bedeutung;
- Event-Time-Zuordnung;
- wann ein Fenster als ausreichend vollständig gilt;
- wie Late Data behandelt wird;
- ob Ergebnisse aktualisiert/retracted/versioniert werden;
- wie lange State vorgehalten werden muss.

Watermarks sind Schätzungen beziehungsweise Fortschrittssignale, keine Garantie, dass nie wieder ältere Daten eintreffen.

## Streaming ≠ Exactly Once

Streaming sagt nichts automatisch über Delivery oder Processing Guarantees aus.

Ende-zu-Ende-Korrektheit hängt von Source, State, Processing und Sink ab.

## Batch ≠ veraltet

Batch ist oft angemessen, wenn:

- fachliche Latenz großzügig ist;
- Quellen natürlich periodisch vorliegen;
- einfachere Reconciliation wichtiger ist;
- Kosten oder Betriebsaufwand für kontinuierliche Verarbeitung keinen Nutzen liefern.

## Lambda/Kappa/andere Patterns

Architekturbezeichnungen sind keine zentralen Vorgaben. Entscheidend ist, ob die lokale Lösung die benötigte Semantik mit vertretbarer Komplexität liefert.

## Nicht tun

- Streaming als automatische Zielarchitektur setzen;
- Processing Time als Event Time ausgeben;
- Watermark mit garantierter Vollständigkeit gleichsetzen;
- Late Data ungefragt verwerfen;
- Window-/Lateness-Werte ohne fachliche Grundlage erfinden;
- Batch und Streaming künstlich doppelt implementieren, nur weil ein Pattern es nahelegt.