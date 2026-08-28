# Workflow – Review-Revise Loop

## Ziel

Ein vorhandenes Ergebnis iterativ gegen Auftrag, lokale Projektwahrheit und passende Qualitätskriterien prüfen, daraus den kleinsten sinnvollen nächsten Eingriff ableiten und gezielt überarbeiten, bis ein akzeptierter Zustand, ein Strategiewechsel oder ein Stop erreicht ist.

Der Workflow ist fachübergreifend. Das eigentliche Qualitätsurteil bleibt beim jeweils passenden Fachreview.

## Grundmuster

```text
Auftrag / Zielzustand
→ Erzeugen oder Umsetzen
→ kritischer Review
→ Urteil und Findings
→ Änderungsstrategie
→ Human Gate, falls erforderlich
→ gezielte Revision
→ erneuter Review
↺
→ FINAL / STOP / Strategiewechsel
```

## Wann verwenden

Geeignet, wenn ein bereits erzeugtes Ergebnis schrittweise verbessert werden soll, zum Beispiel bei:

- Bildern und Bildserien;
- Texten und Dokumentation;
- Code und technischen Änderungen;
- Webseiten und UI;
- Konzepten, Plänen oder Spezifikationen;
- delegierter Arbeit zwischen Planer, Worker und Reviewer.

Typische natürliche Trigger für den Review-Schritt sind etwa:

- „Dein Urteil?“
- „Deine Meinung dazu?“
- „Was würdest du noch ändern?“
- „Prüf das Ergebnis nochmal kritisch.“
- „Ist das so final oder braucht es noch eine Runde?“

Ein bloßer Review-Auftrag autorisiert noch keine Änderung.

## Rollen

Die Rollen sind logisch getrennt, müssen aber nicht zwingend von verschiedenen Modellen oder Chats ausgeführt werden.

### Auftraggeber / Mensch

- setzt Ziel, Scope und lokale Wahrheit;
- entscheidet an erforderlichen Human Gates;
- kann Findings akzeptieren, verwerfen oder neu priorisieren;
- bestimmt, wann ein ausreichend gutes Ergebnis freigegeben wird.

### Erzeuger / Worker

- erstellt oder verändert das Ergebnis innerhalb des freigegebenen Scopes;
- übernimmt keine neue Projektentscheidung nur aufgrund eines Review-Findings.

### Reviewer

- prüft das konkrete Ergebnis gegen Auftrag und relevante Quellen;
- benennt Stärken und relevante Abweichungen;
- priorisiert Findings;
- empfiehlt einen nächsten Status beziehungsweise Eingriff;
- verteidigt die vorherige eigene Arbeit nicht reflexhaft.

Wenn Erzeuger und Reviewer dasselbe Modell oder derselbe Chat sind, ist das ein **kritischer Same-Model-Review**, kein unabhängiger Review. Unabhängigkeit nur behaupten, wenn die lokale Prüfanordnung sie tatsächlich herstellt.

## Ablauf

### 1. Review-Basis bestimmen

Vor dem Urteil klären:

- Was war der konkrete Auftrag?
- Welche lokale Projektwahrheit oder Spezifikation gilt?
- Welcher Stand wird gerade geprüft?
- Welcher Fachreview passt zum Artefakt?
- Welche früheren Entscheidungen oder freigegebenen Eigenschaften sollen erhalten bleiben?

### 2. Ergebnis kritisch prüfen

Den passenden Fachskill oder die passende Fachregel verwenden, zum Beispiel:

- Bild → `bildreview`;
- Code → `code-review`;
- Webdesign → `web-design-review` und bei Bedarf `visual-verification`;
- Text → `stilreview` oder den passenden Dokumentations-/Schreibreview;
- Architektur / Requirements / Reliability / Data Engineering → jeweiliger Fachreview.

Nicht nur Fehler suchen. Auch ausdrücklich festhalten, was funktioniert und bei der nächsten Revision geschützt werden soll.

### 3. Urteil und Findings liefern

Ein brauchbares Review unterscheidet mindestens:

- **Stärken / Keeper:** Was soll erhalten bleiben?
- **Relevante Findings:** Was weicht vom Ziel ab?
- **Schwere und Lokalität:** lokal, mehrere begrenzte Punkte oder grundlegend?
- **Nächster Status:** final, gezielte Revision, größerer Neuansatz oder Stop?
- **Nächster Eingriff:** so eng wie sinnvoll.

Keine künstlichen Findings erzeugen, nur um eine weitere Runde zu rechtfertigen.

### 4. Änderungsstrategie wählen

Grundsatz:

> So wenig neu bauen wie möglich, so viel ändern wie nötig.

Daraus können je nach Domäne beispielsweise folgen:

- enger lokaler Fix;
- kontrollierter Feinschliff;
- begrenztes Refactoring;
- gezielte strukturelle Überarbeitung;
- kontrollierter Teil- oder Neuaufbau;
- Rückkehr zu einer älteren stärkeren Fassung;
- keine Änderung / final.

Eine neue Version ist kein Qualitätsbeweis.

### 5. Human Gate beachten

Wenn der Nutzer nur nach Urteil, Meinung oder Feedback gefragt hat:

> Review liefern → auf Freigabe warten.

Erst Formulierungen wie „machen wir so“, „setz das um“ oder eine bereits vorhandene explizite Revisionsautorisierung erlauben die Änderung innerhalb des vereinbarten Scopes.

Ein Review-Finding erweitert weder Toolrechte noch Produktions-, Publishing-, Deployment- oder andere externe Autorisierung.

### 6. Gezielt revidieren

Bei der Revision:

- bestätigte Stärken schützen;
- nur die freigegebenen Findings adressieren;
- lokale Wahrheit nicht durch plausiblere Eigenideen ersetzen;
- unnötige Nebeneffekte vermeiden;
- bei produktiven oder externen Aktionen zusätzliche lokale Gates beachten.

### 7. Erneut prüfen

Nach der Revision denselben relevanten Zielzustand erneut prüfen.

Wo objektive Evidence verfügbar ist, den passenden `verification-loop` beziehungsweise Fachvalidator zusätzlich verwenden. Review und Verifikation dürfen sich ergänzen, sind aber nicht dasselbe.

## Verhältnis zum Verification Loop

```text
verification-loop
= Arbeiten → nachweisbar prüfen → diagnostizieren → korrigieren

review-revise-loop
= Ergebnis fachlich beurteilen → Änderungsstrategie wählen
  → erforderliches Human Gate → revidieren → erneut beurteilen
```

Der `verification-loop` ist besonders stark, wenn reproduzierbare Tests, Messungen oder Validatoren existieren. Der Review-Revise Loop deckt zusätzlich qualitative Urteile, menschliche Auswahl und iteratives Refinement ab.

Beide können innerhalb derselben Arbeit kombiniert werden.

## Planer–Worker–Reviewer-Muster

Bei delegierter Arbeit kann der Workflow so aussehen:

```text
Planer
→ definiert Auftrag, Scope und Akzeptanz

Worker
→ liefert Ergebnis und Evidence

Reviewer / Planer
→ prüft gegen Auftrag
→ APPROVE oder Findings + begrenzten Anpassungsauftrag

Mensch / zuständiges Gate
→ bestätigt erforderliche Richtungsänderung

Worker
→ setzt nächste Iteration um
```

Ein Worker-Erfolg ist kein automatischer Review-Erfolg. Ein Review-Erfolg ist keine automatische externe Freigabe.

## Schutz vor Endlosschleifen

Nicht denselben Reparaturversuch unbegrenzt wiederholen.

Strategie neu bewerten, wenn:

- dasselbe relevante Finding nach mehreren gezielten Versuchen wiederkehrt;
- jede Korrektur neue gleich schwere Fehler erzeugt;
- die Ursache in Auftrag, Architektur, Komposition oder fehlender Projektwahrheit liegt;
- eine ältere Fassung insgesamt besser ist;
- weiteres Optimieren einen bereits starken Keeper wahrscheinlich verschlechtert.

Dann je nach Fall:

- Ursache neu diagnostizieren;
- Scope oder Ansatz vereinfachen;
- frühere Version wiederherstellen;
- kontrollierten Neuansatz wählen;
- zusätzliche Evidence oder Fachreview einholen;
- stoppen und eine neue menschliche Entscheidung anfordern.

## Stop- und Abschlusszustände

Der Loop endet mit einem klaren Zustand:

- **FINAL / APPROVE** – Ergebnis erfüllt den aktuellen Auftrag ausreichend;
- **REVISE** – konkrete, freigegebene Findings bleiben offen;
- **REPLAN** – der bisherige Ansatz ist nicht mehr der sinnvollste;
- **BLOCKED** – notwendiger Kontext, Evidence oder eine Entscheidung fehlt;
- **STOP** – weitere Iteration ist nicht sinnvoll oder nicht autorisiert.

„Final“ bedeutet nur final für den aktuell geprüften Scope. Es ersetzt keine separat erforderliche Release-, Publishing-, Deployment- oder sonstige Außenfreigabe.

## Leitgedanken

> Review ist kein Reflex zur Verteidigung der eigenen vorherigen Arbeit.

> Ein lokales Problem braucht nicht automatisch einen globalen Neubau.

> Same-Model-Review kann nützlich sein, ist aber kein unabhängiger Review.

> Iteration endet nicht bei theoretischer Perfektion, sondern bei einem ausreichend guten, nachvollziehbar akzeptierten Zustand.
