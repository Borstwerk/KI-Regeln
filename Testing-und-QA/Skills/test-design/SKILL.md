---
name: test-design
description: Entwirft konkrete Testfälle aus Anforderungen, Invarianten, Zuständen, Grenzwerten und Failure Modes. Verwenden, wenn konkrete Testfälle oder eine systematische Testfallmenge benötigt werden. Nicht als allgemeine Teststrategie oder E2E-Ausführung verwenden.
---

# Test Design

## Ziel

Konkrete, aussagekräftige Tests mit belastbarem Oracle entwerfen.

## Arbeitsweise

1. Testbasis und zugesichertes Verhalten identifizieren.
2. Relevante Eingabedimensionen, Zustände und Grenzen bestimmen.
3. Passende Techniken auswählen, zum Beispiel:
   - Äquivalenzklassen;
   - Grenzwerte;
   - Entscheidungstabellen;
   - Zustandsübergänge;
   - Pairwise / Kombinationen;
   - Property-based Testing.
4. Happy Path und relevante Negativ-/Fehlerfälle entwerfen.
5. Erwartungswert unabhängig von der Produktionsimplementierung ableiten.
6. Vorbedingungen und benötigte Testdaten benennen.
7. Prüfen, ob der Test Verhalten statt unnötige Implementierungsdetails schützt.
8. Bei kritischen Regeln Brechprobe/Mutation als mögliche Wirksamkeitsprüfung benennen.

## Ausgabe je Testfall

```text
Ziel / Risiko
Vorbedingungen
Eingaben / Zustand
Aktion
Erwartetes Ergebnis
Testebene
Daten / Dependency-Bedarf
```

## Stoppen / markieren

- erwartetes Verhalten ist nicht spezifiziert;
- fachlicher Oracle fehlt;
- Engine-/Framework-Verhalten müsste erfunden werden;
- Testfall würde eine neue Produktentscheidung vorwegnehmen.

## Regeln

- Produktionslogik nicht einfach im Test duplizieren;
- keine sinnlosen Varianten nur für höhere Fallzahl;
- Grenz- und Fehlerfälle am realen Risiko ausrichten;
- Properties als Invarianten formulieren, nicht als zufällige Inputgenerator-Spielerei.