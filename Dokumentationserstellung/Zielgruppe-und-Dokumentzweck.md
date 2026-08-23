# Zielgruppe und Dokumentzweck

## Zweck

Gute Dokumentation beginnt damit, **wer** sie in **welcher Situation** verwendet und **welches Ergebnis** danach möglich sein soll.

## Vor dem Schreiben klären

Mindestens:

- primäre Zielgruppe;
- Vorwissen;
- konkrete Aufgabe oder Informationsbedarf;
- Nutzungssituation;
- erwartetes Ergebnis;
- relevante Version oder Systemgrenze;
- notwendige Sources of Truth.

## Leserzustand statt abstrakter Persona

Nützlicher als eine dekorative Persona ist meist die konkrete Situation:

```text
Person kennt Produkt kaum
+ möchte erstes Ergebnis
→ Quickstart / Tutorial

Person kennt Produkt
+ muss Aufgabe X lösen
→ How-to

Person arbeitet bereits
+ braucht Parameter Y
→ Reference

Person kennt Verhalten
+ möchte Designentscheidung verstehen
→ Explanation / ADR
```

## Vorwissen explizit machen

Dokumentation soll weder unnötig alles erklären noch stillschweigend Kenntnisse voraussetzen.

Vorbedingungen können betreffen:

- technische Kenntnisse;
- installierte Software;
- Berechtigungen;
- vorhandene Konfiguration;
- fachliche Begriffe;
- vorherige Dokumente oder Schritte.

## Erfolgskriterium definieren

Vor dem Schreiben möglichst festlegen, woran gute Dokumentation erkennbar ist.

Beispiele:

- ein neuer Nutzer erreicht ein erstes funktionierendes Ergebnis;
- ein erfahrener Nutzer kann Aufgabe X ohne Rückfrage erledigen;
- ein Parameter ist in kurzer Zeit auffindbar;
- eine Architekturentscheidung ist später nachvollziehbar;
- ein On-Call-Ingenieur kann einen bekannten Fehler sicher diagnostizieren und mitigieren.

## Nicht für alle gleichzeitig schreiben

Ein Dokument, das gleichzeitig Anfänger, Experten, Betrieb, Management und API-Integratoren vollständig bedienen will, wird oft für niemanden besonders gut.

Besser:

- primäre Zielgruppe festlegen;
- notwendige Nebenbedürfnisse verlinken;
- unterschiedliche Dokumenttypen trennen.

## Sprache an Nutzungssituation anpassen

Unter Stress oder während einer konkreten Aufgabe:

- kurze eindeutige Schritte;
- Bedingungen vor Aktionen;
- erwartete Ergebnisse direkt nennen;
- keine langen konzeptuellen Abschweifungen.

Beim Lernen oder Verstehen:

- Zusammenhänge und Begründungen zulassen;
- Alternativen und Trade-offs erklären;
- Beispiele als Denkstütze verwenden.

## Leitgedanke

> Dokumentation wird nicht für ein Thema geschrieben, sondern für einen Leser in einer konkreten Situation.
