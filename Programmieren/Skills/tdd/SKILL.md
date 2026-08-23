---
name: tdd
description: Testgetriebene Umsetzung für KI-gestützte Softwarearbeit. Verwenden, wenn ein freigegebener Feature- oder Bugfix-Scope in kleinen überprüfbaren Schnitten umgesetzt wird.
---

# Test-Driven Development

Dieser Skill unterstützt die Umsetzung. Er ersetzt weder Anforderung noch freigegebenen Plan.

## Vorbedingung

Bevor Code geändert wird:

1. Anforderung und freigegebenen Plan identifizieren.
2. Vereinbarte fachliche Testgrenzen beziehungsweise Seams übernehmen.
3. Wenn Planung fehlt, widersprüchlich ist oder eine notwendige Architekturentscheidung offenlässt: stoppen und den offenen Punkt melden statt implementieren.

## Arbeitsweise

Für jeden kleinen fachlichen Schnitt:

1. Einen Test schreiben, der das gewünschte Verhalten an einer belastbaren Grenze beschreibt.
2. Den engsten passenden Testlauf ausführen und bestätigen, dass der neue Test aus dem erwarteten Grund rot ist.
3. Nur die kleinste fachlich richtige Änderung implementieren, die diesen Schnitt erfüllt.
4. Den engen Testlauf erneut ausführen und grün bestätigen.
5. Erst danach den nächsten Schnitt beginnen.

Nicht erst alle Tests und anschließend die gesamte Implementierung schreiben. Der letzte Red/Green-Zyklus soll die nächste Entscheidung informieren.

## Gute Tests

Ein Test soll:

- Verhalten prüfen, nicht private Implementierungsdetails;
- einen unabhängigen erwarteten Wert besitzen und nicht einfach Produktionslogik nachbauen;
- bei Refactoring grün bleiben, solange das zugesicherte Verhalten unverändert bleibt;
- bei Persistenzänderungen einen echten Roundtrip oder eine echte Migration prüfen;
- bei Snapshots oder Ableitungen relevante Zustandsübergänge prüfen, wenn der Slice diese Pfade berührt;
- UI oder Integration möglichst über belastbare Verhaltenseffekte prüfen, ohne interne Struktur unnötig festzufrieren.

Keine Tests lockern, löschen oder umformulieren, nur damit neue Implementierung grün wird.

Wenn eine alte Zusicherung fachlich nicht mehr gilt, muss das aus Anforderung oder freigegebenem Plan hervorgehen.

## Brechprobe

Wenn eine kritische Eigenschaft leicht versehentlich umgangen werden kann, nach dem grünen Testlauf eine gezielte Brechprobe durchführen:

- Schutzbedingung probeweise entfernen oder einen falschen Zustand einführen;
- bestätigen, dass mindestens der dafür gedachte Test rot wird;
- Probe vollständig zurückbauen;
- Endstand erneut grün ausführen.

Brechproben sind besonders wertvoll bei Migrationen, Deduplizierung, Rollback, Zustandskopplung, Sicherheitsregeln und Persistenzpfaden.

## Refactoring und Scope

Refactoring nur, wenn es für den freigegebenen Slice notwendig ist oder direkt aus dem letzten Zyklus als lokale Vereinfachung folgt.

Kein Architekturputz nebenbei. Keine neue Abhängigkeit ohne begründeten Plan.

## Abschluss

Vor Abschluss mindestens:

- relevante enge Tests grün;
- vollständige passende Testsuite grün;
- Format-, Lint- und Build-Prüfungen des Repositories grün;
- Diff-Prüfung ohne offensichtliche Format- oder Whitespacefehler;
- Diff gegen die freigegebene Scope-Grenze geprüft;
- relevante Brechproben dokumentiert;
- verbleibende manuelle Prüfungen benannt.

Grün bedeutet: Die Umsetzung ist technisch belegt. Freigabe erfolgt nach dem gültigen Review- und Freigabeprozess.