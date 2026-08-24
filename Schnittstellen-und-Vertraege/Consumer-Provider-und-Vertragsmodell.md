# Consumer, Provider und Vertragsmodell

## Kern

Eine Schnittstelle entsteht erst durch eine Erwartungsbeziehung.

- **Provider** stellt Verhalten, Daten oder Ereignisse bereit.
- **Consumer** baut beobachtbare Erwartungen darauf auf.
- **Contract** beschreibt die zugesicherte Bedeutung zwischen beiden.

## Vor dem Design klären

- welche Capability über die Grenze benötigt wird;
- wer Provider und Owner ist;
- welche Consumer existieren oder erwartet werden;
- ob Consumer gemeinsam oder unabhängig deployt werden;
- welche Stabilitäts- und Supporterwartung gilt;
- welche Daten- und Berechtigungsgrenzen betroffen sind;
- welche Failure-, Retry- und Zeitsemantik relevant ist.

## Architekturgrenze

Der Bereich entscheidet nicht eigenmächtig, welche Services oder Module existieren sollen.

```text
Software Architecture
→ Wo und warum verläuft die Grenze?

Schnittstellen und Verträge
→ Was bedeutet die Kommunikation über diese Grenze?
```

`interface-design` darf die Eignung einer vorgegebenen Grenze oder eines Interaktionsstils hinterfragen, aber keine große Systemzerlegung stillschweigend als Nebenprodukt durchführen.

## Öffentlicher Contract ≠ internes Modell

Interne Klassen, Datenbanktabellen oder Frameworkobjekte sind nicht automatisch geeignete öffentliche Repräsentationen.

Eine stabile Schnittstelle soll interne Refactorings erlauben, solange die zugesicherte Consumer-Sicht erhalten bleibt.

## Observable Behavior

Nicht nur dokumentierte Felder können faktisch zu Consumerannahmen werden. Auch beobachtbares Verhalten wie Defaults, Reihenfolge, Fehlertypen, Null-/Absent-Verhalten oder Retry-Eigenschaften kann Abhängigkeiten erzeugen.

Deshalb bei Brownfield-Arbeit reale Nutzung und vorhandene Consumer prüfen statt nur die Spezifikation zu lesen.

## Leitgedanke

> Ein Contract wird vom Consumer erlebt, nicht vom Provider behauptet.