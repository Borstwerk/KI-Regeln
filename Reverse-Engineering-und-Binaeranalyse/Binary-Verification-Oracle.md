# Binary Verification Oracle – Vergleich gegen ein Referenzartefakt

## Zweck

Eine rekonstruierte Funktion, Bibliothek oder Anwendung ist nicht deshalb äquivalent, weil dekompilierter Pseudocode plausibel aussieht oder der neue Code kompiliert.

Ein **Verification Oracle** ist ein reproduzierbarer und vom Worker unabhängiger Prüfpfad, der eine vorher definierte Eigenschaft gegen ein zulässiges Referenzartefakt prüft. Es ergänzt den Skill `binary-analysis` und ist **kein neuer Skill oder universelles Tool**.

## Prüfstufen und präzise Claims

| Stufe | Beobachtbarer Check | Erlaubte Aussage |
|---|---|---|
| L0 | Pseudocode / Funktionsstruktur visuell plausibel | Hypothese, kein Verifikations-PASS |
| L1 | Rekonstruktion baut mit dokumentierten Toolchain-Daten | Build ist reproduzierbar; Semantik noch offen |
| L2 | definierte Referenzfälle, Invarianten und Negativtests bestehen | verifiziert für getestete Fälle |
| L3 | differentialer Vergleich gegen Original-Ausgaben / Seiteneffekte in kontrollierter Sandbox | Äquivalenz innerhalb gemessener Inputs und beobachteter Effekte |
| L4 | relocation-/symbolbewusster Byte- und Datenvergleich unter **kontrollierter identischer Toolchain** | starke byte-/strukturbezogene Äquivalenz für genau geprüfte Einheiten |

**L4 ≠ allgemeiner Beweis semantischer Gleichwertigkeit.** Byteidentität unter sauber kontrolliertem Build ist starkes Indiz für eine exakt reproduzierte Einheit. Verschiedene, aber semantisch äquivalente Builds können andere Bytes besitzen.

## Oracle-Contract

Der Prüfpfad soll vor der Worker-Änderung festgelegt und versioniert sein:

- `reference_hash`, `candidate_hash`, untersuchte Funktion/Version;
- Toolchain, Compilerflags, ABI, Symbol-/Debug-Infos, Architektur;
- Normalisierungsregeln wie Relocation-Masken und Symbolzuordnungen;
- erlaubte Abweichungen, Abbruchkriterien und Unsicherheiten;
- Testfälle oder Vergleichsinputs samt Provenienz;
- Ergebnis mit `PASS / FAIL / INCONCLUSIVE / NOT RUN`, Prüfartefakt und Hash;
- unabhängiger Owner der Akzeptanzkriterien.

Relocations nicht einfach ignorieren: referenzierte **Symbole und Offsets** separat prüfen. Sonst kann ein Bytevergleich falsche Übereinstimmung signalisieren.

## Verifikationsschutz

**Worker darf das eigene Oracle nicht unkontrolliert ändern.**

- Oracle-Scripts, Baseline, Thresholds, Normalisierungsregeln und Referenzhashes zunächst read-only bereitstellen.
- Worker darf Testausführung anstoßen und Resultate lesen; kein Recht auf verdeckte Änderungen, Abschalten oder Ersatz-Oracle.
- Sachlich berechtigte Oracle-Korrektur als **separate, begründete Änderung** mit unabhängiger Freigabe und erneuter Baseline-Evidence.
- Soll-/Ist-Output des Oracles nicht vom Worker als unverifizierte Selbstauskunft akzeptieren.
- Wenn ein alternativer Prüfweg nötig ist, dessen Unabhängigkeit und Zulässigkeit explizit dokumentieren.

Der Originalcode/das Binary kann proprietär sein: Autorisierung, Export-/Lizenzgrenzen, isolierte Ausführung, Providerdatenübertragung und Schutz von Secrets bleiben vorrangig.

## Bei fehlender Evidenz

- Original fehlt: L3/L4 `NOT RUN`, kein behaupteter Äquivalenz-PASS.
- Nur Pseudocode: L0, Hypothese bleibt unbestätigt.
- Verschiedene Toolchains: L4 nicht als unabhängiger Korrektheitsbeweis behaupten.
- Output passt, aber Seiteneffekte wurden nicht geprüft: Scope von L3 begrenzen.
- Oracle meldet `FAIL`: keine stillen Test-/Threshold-Abschwächungen; Ursache untersuchen.

## Übertragbares Muster

[500+ Billion Tokens Later – Letting AI Agents Decompile A First-Person Shooter](https://momo5502.com/posts/2026-10-09-game-decompilation/) dokumentiert, wie ein relocation-/symbolbewusster Bytevergleich als mechanischer Prüfpfad eingesetzt wurde. Das ist eine **Methodenquelle**, keine implizite Bestätigung, dass eine beliebige Binärrekonstruktion dasselbe Ergebnis erreichen kann.

## Leitgedanke

> Eine unabhängige, vorab definierte Gegenprobe ist stärkere Evidence als die überzeugendste Erklärung des Workers.
