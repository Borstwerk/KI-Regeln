# Prompt Caching und stabile Kontexte

## Zweck

Manche Modell-/Agentenruntimes können wiederkehrende Eingabepräfixe zwischenspeichern. Gutes Context Engineering kann solche Mechanismen unterstützen, ohne fachliche Korrektheit an Cache-Optimierung zu opfern.

## Allgemeines Prinzip

Wenn die verwendete Runtime Präfix- oder Prompt-Caching unterstützt:

- stabile Instruktionen und Definitionen möglichst stabil halten;
- häufig wechselnde Daten eher nach stabilen Bestandteilen anordnen;
- unnötiges Umsortieren oder Umschreiben identischer Instruktionen vermeiden;
- providerseitige Cache-Signale beobachten, wenn verfügbar.

## Append-only als mögliches Muster

Einige Runtimes profitieren davon, bestehende modell-sichtbare Historie nicht rückwirkend zu verändern, sondern neue Informationen anzuhängen.

Das ist ein runtimeabhängiges Optimierungsmuster, keine universelle Protokollregel.

## Providerlokal bleiben

Nicht zentral festschreiben:

- Cache-Mindestlänge;
- Cache-Lebensdauer;
- konkrete Rabatte oder Preise;
- Cache-Key-Syntax;
- providerbezogene Breakpoint- oder Retention-Mechanismen.

Diese Angaben müssen gegen die tatsächlich verwendete Modell-/API-Version geprüft werden.

## Korrektheit vor Hit Rate

Nicht:

- veraltete Instruktionen behalten, nur damit ein Präfix gleich bleibt;
- sensible Daten unnötig wiederverwenden;
- benötigte aktuelle Projektinformation aus Cache-Gründen verzögern;
- semantisch falsche Reihenfolgen erzeugen, nur um eine höhere Hit Rate zu erreichen.

Eine höhere Cache-Quote ist nur dann ein Gewinn, wenn Verhalten und Aktualität korrekt bleiben.

## Messung

Wenn verfügbar, gemeinsam betrachten:

```text
Input-Tokens
+ Cache-Read/-Write-Signale
+ Latenz
+ Outcome
```

Nicht nur die Cache-Hit-Rate optimieren.

## Leitgedanke

> Stabilisiere wiederverwendbaren Kontext dort, wo es fachlich natürlich ist – nicht dort, wo Caching die Wahrheit verbiegen würde.