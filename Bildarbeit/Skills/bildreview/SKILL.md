---
name: bildreview
description: Prüft eine einzelne Bildgenerierung auf Aufgabe, Identität, Kontinuität, Anatomie, Physik, Stil und entscheidet zwischen Keeper, Feinschliff oder Neubau. Verwenden nach einer Bildgenerierung, wenn Produktionsauftrag und Ergebnis kritisch geprüft und ein enger nächster Status gewählt werden sollen.
---

# Bildreview

Dieser Skill nutzt `../../Bildpruefung-und-Freigabe.md` sowie bei Serien zusätzlich `../../Kontinuitaet-und-Zustandsmatrix.md`.

## Ziel

Nicht nur bewerten, ob ein Bild attraktiv ist, sondern ob es die konkrete Produktionsaufgabe korrekt erfüllt.

Ein Review durch dasselbe Modell oder denselben Chat kann kritisch und nützlich sein, ist aber nicht allein dadurch unabhängig. Unabhängigkeit nur behaupten, wenn die konkrete Prüfanordnung sie tatsächlich herstellt.

## Ablauf

1. Pre-Brief und relevante Projektquellen lesen.
2. Geplanten Moment gegen tatsächliches Bild prüfen.
3. Identität und aktuelle Zustände prüfen.
4. Anatomie, Geometrie, Kontakt und physische Plausibilität prüfen.
5. Stil, Licht, Lesbarkeit und ungewollten Text prüfen.
6. Bildwirkung und Komposition bewerten.
7. Fehler nach Schwere und Lokalität einordnen.
8. genau einen nächsten Status empfehlen.

## Mögliche Status

- **Behalten / final**
- **enger lokaler Feinschliff**
- **kontrollierter Feinschliff**
- **kontrollierter kompositorischer Neubau**
- **kompletter Neubau**

## Entscheidungsregeln

Ein lokaler Fehler rechtfertigt keinen vollständigen Neubau, wenn Komposition und Wirkung stark sind.

Ein spektakuläres Bild rechtfertigt keinen Keeper, wenn Moment, Identität oder Kontinuität falsch sind.

Wenn mehrere Reparaturversuche denselben Fehler wiederholen:

- Fehlerursache analysieren;
- Pose, Perspektive oder Komplexität verändern;
- Referenzen und Ausschlüsse prüfen;
- nicht denselben Versuch endlos wiederholen.

Eine ältere Fassung darf gewinnen, wenn sie insgesamt stärker und richtiger ist.

## Ausgabeformat

```markdown
## Urteil
<kurze Gesamtbewertung>

## Stärken
- ...

## Relevante Fehler
- ...

## Kontinuität / Identität
- ...

## Empfohlener Status
<genau einer der fünf Status>

## Nächster Eingriff
<so eng wie sinnvoll beschreiben>
```

## Leitfrage

> Sieht das Bild stark aus **und** erfüllt es exakt seine Aufgabe?