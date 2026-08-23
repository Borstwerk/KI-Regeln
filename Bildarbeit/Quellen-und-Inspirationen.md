# Quellen und Inspirationen zur Bildarbeit

Dieser Bereich fasst allgemeine Arbeitsprinzipien für konsistente Bildserien zusammen. Die folgenden Quellen dienten als Inspiration und technische Einordnung. Sie sind keine verbindliche Projektspezifikation.

Letzte inhaltliche Prüfung dieser Quellenbasis: **2026-08-23**.

Lebende Produktdokumentationen werden zusätzlich über `../Dokumentation/upstream-sources.yml` semantisch beobachtet.

## Adobe Firefly – Style Reference

Adobe beschreibt Style References als Mittel, um Stil, Farben, künstlerische Methode und Stimmung über mehrere Generierungen hinweg zu steuern. Die Referenzstärke kann separat geregelt werden.

Quelle:

https://developer.adobe.com/firefly-services/docs/firefly-api/guides/concepts/style-image-reference/

## Adobe Firefly – Structure Reference

Adobe trennt Style Reference ausdrücklich von Structure Reference. Structure Reference steuert strukturelle Eigenschaften wie Umriss, Bildaufbau und Tiefenwirkung und besitzt ebenfalls eine einstellbare Stärke.

Quelle:

https://developer.adobe.com/firefly-services/docs/firefly-api/guides/concepts/structure-image-reference/

## Midjourney – Character Reference / Omni Reference

Midjourney dokumentiert Character Reference beziehungsweise Omni Reference für die Wiederverwendung wiederkehrender Figuren, Objekte, Fahrzeuge oder nichtmenschlicher Kreaturen über mehrere Szenen hinweg.

Quellen:

https://docs.midjourney.com/hc/en-us/articles/32162917505293-Character-Reference

https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference

Stand der Prüfung 2026-08-23:

- die Character-Reference-Dokumentation weist für V7 auf Omni Reference als Nachfolger hin;
- Omni Reference ist deshalb der aktuellere Produktmechanismus für V7;
- die zentrale Regel dieses Repositories bleibt bewusst toolneutral und spricht allgemein von Identitätsreferenzen.

## Midjourney – Style Reference

Midjourney bietet mit Style References und Style Creator wiederverwendbare Stilanker für Serienproduktionen.

Quellen:

https://updates.midjourney.com/style-references-for-v7/

https://docs.midjourney.com/hc/en-us/articles/41308374558221-Style-Creator

Die laufend gepflegte Style-Creator-Dokumentation wird aktiv beobachtet. Der V7-Updateartikel bleibt als zeitbezogene Referenz dokumentiert, wird aber nicht als mutable Dependency behandelt.

## Allgemeine Einordnung

Die konkrete Funktion und Bezeichnung von Referenzmechanismen hängt vom Bildsystem ab. Für dieses Repository werden daraus nur die übertragbaren Prinzipien übernommen:

- Identitätsreferenz, Stilreferenz und Strukturreferenz getrennt betrachten;
- Referenzstärke bewusst nach Zweck wählen;
- wiederkehrende Entitäten mit freigegebenen Produktionsreferenzen stabilisieren;
- Referenzbilder nicht als automatische Wahrheit für alle sichtbaren Details behandeln;
- eine Bildserie als kontrollierten Produktionsprozess und nicht als Folge unabhängiger Zufallsgenerierungen behandeln.

## Herkunft der Produktionslogik

Die Regeln zu Quellenpriorität, Szenen-Zustandsmatrix, Pre-Brief, Review-Stufen, Schutz vor Endlosschleifen und Abschlussaudit wurden aus einem erprobten Serienillustrations-Workflow abstrahiert und von konkreten Figuren-, Welt- und Projektdetails getrennt.

## Leitgedanke

> Technische Referenzfunktionen helfen bei Konsistenz. Die eigentliche visuelle Wahrheit bleibt trotzdem im Projekt definiert.