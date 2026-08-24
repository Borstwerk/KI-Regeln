# Evolution, Migration und Zwischenzustände

## Zweck

Bestehende Architektur wird selten atomar ersetzt. Eine belastbare Architekturänderung muss deshalb nicht nur Zielzustand, sondern auch Übergang, Compatibility, Recovery und Zwischenzustände erklären.

## Evolution statt Big Rewrite

Bevor ein Rewrite vorgeschlagen wird, prüfen:

- welches konkrete Problem nicht lokal lösbar ist;
- welche Teile tatsächlich geändert werden müssen;
- welche bestehende Funktion oder Schnittstelle erhalten bleiben muss;
- ob ein vertikaler Slice den neuen Ansatz zuerst beweisen kann;
- wie der alte Pfad kontrolliert ausläuft.

## Migrationsmodell

```text
Architecture 0 / Ist-Zustand
→ begrenzter Change Slice
→ koexistierender Zwischenzustand
→ Fresh Verification
→ weiterer Slice
→ Cutover / Retirement
```

Für jeden Schritt:

- Scope und Owner;
- Contract-/Schema-/Datenkompatibilität;
- Read-/Write-Pfad;
- Observability und Erfolgssignal;
- Rollback-/Abort-Möglichkeit;
- irreversible Nebenwirkungen;
- Cleanup-/Retirement-Kriterium.

## Patterns

Strangler, Branch by Abstraction, Parallel Run, Shadow Traffic, Dual Read/Write oder Adapter können helfen, sind aber keine universellen Defaults.

Insbesondere Dual Write erzeugt eigene Konsistenz- und Recoveryprobleme und darf nicht als triviale Migrationshilfe behandelt werden.

## Architecture Debt

Nicht jede Abweichung vom Zielbild ist sofort zu entfernen. Architektur-Schulden werden nach realer Wirkung priorisiert:

- verletzt eine Invariante;
- erhöht Change- oder Failure-Risiko;
- blockiert relevantes Ziel;
- erzeugt doppelte Wahrheit oder gefährliche Kopplung;
- kann bewusst als begrenzter Legacyzustand akzeptiert werden.

## Execution-Grenze

`architecture-evolution` plant und bewertet. Codeänderungen, Datenmigrationen, Deployments, Traffic Switches oder produktive Cutovers bleiben in den jeweiligen Fachprozessen und lokalen Gates.

## Leitgedanke

> Eine gute Zielarchitektur ist wertlos, wenn der Weg dorthin nur als Sprung über eine Schlucht beschrieben ist.