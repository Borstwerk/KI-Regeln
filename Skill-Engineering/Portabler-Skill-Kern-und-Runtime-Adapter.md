# Portabler Skill-Kern und Runtime-Adapter

## Inhalt

- Zweck
- Zwei Ebenen
- Source of Truth
- Modell-spezifische Workarounds
- Capability statt Toolname
- Modell-/Runtime-Evidence
- Reviewfragen
- Ausnahmen
- Leitgedanke

## Zweck

Wiederverwendbare Skills sollen ihre **fachliche Arbeitsdisziplin** von agenten-, modell- oder runtime-spezifischer Ausführungskonfiguration trennen.

> Der Skill-Kern beschreibt, was zuverlässig passieren soll. Der Runtime-Adapter beschreibt, wie eine konkrete Laufzeit diese Disziplin ausführt.

## Zwei Ebenen

### 1. Portabler Skill-Kern

In den gemeinsamen Kern gehören insbesondere:

- Verantwortung und Scope;
- Trigger und Near-Misses;
- fachlicher Prozess;
- Inputs, Outputs und Evidence;
- benötigte Capabilities;
- Fallbacks;
- Stop-/Eskalationsbedingungen;
- Sicherheits- und Freigaberegeln.

Der Kern soll keine konkrete Runtime voraussetzen, wenn die Plattform nicht selbst Gegenstand des Skills ist.

### 2. Runtime-/Client-Adapter

In einen Adapter oder klar gekapselte Runtime-Metadaten gehören beispielsweise:

- konkrete Modellwahl;
- Toolnamen und Tool-Allow-/Deny-Listen;
- Turn-Limits;
- Context-/Isolation-Modi;
- client-spezifische Subagent-Konfiguration;
- host-spezifische Hooks oder Command Wrapper;
- temporäre Workarounds für konkrete Runtime-Bugs.

Ein Adapter darf die fachlichen Gates des Skill-Kerns nicht stillschweigend abschwächen.

## Source of Truth

Bei mehreren Clients gilt:

```text
fachlicher Skill-Kern
        ↓
Runtime-Anforderungen / Capabilities
        ↓
client-spezifischer Adapter
```

Nicht mehrere fast gleiche `SKILL.md`-Kopien von Hand auseinanderentwickeln, wenn dieselbe fachliche Disziplin gemeint ist.

Wo Adapter mechanisch generiert werden können, sollte eine gemeinsame deklarative Source of Truth bevorzugt werden.

## Modell-spezifische Workarounds

Ein beobachteter Fehler eines bestimmten Modells ist zunächst **Runtime-Evidence**, keine allgemeine Skillregel.

Vor einer Kernänderung prüfen:

1. tritt das Verhalten über Modelle/Hosts hinweg auf?
2. beschreibt die Änderung eine fachliche Invariante oder nur einen Workaround?
3. lässt sich der Workaround im Adapter kapseln?
4. braucht die Kernregel wirklich zusätzliche Komplexität?

Beispiel:

```text
schlecht:
"Wenn Modell X den zweiten Schritt oft vergisst, wiederhole ihn dreimal."

besser:
Kern: "Vor Abschluss müssen die definierten Pflichtprüfungen nachweisbar ausgeführt sein."
Adapter: host-/modellspezifische Unterstützung nur dort, wo sie tatsächlich nötig ist.
```

## Capability statt Toolname

Der Skill-Kern soll möglichst Fähigkeiten benennen:

```text
repository-read
browser-preferred
code-execution-required
external-actions-gated
```

statt konkrete Toolnamen als allgemeine Wahrheit einzubauen.

Konkrete Toolzuordnung ist Aufgabe des Adapters oder der aktuellen Laufzeit.

## Modell-/Runtime-Evidence

Die Frage **welches konkrete Modell mit welcher Runtime einen Skill erfolgreich ausgeführt hat** gehört primär in Eval-/Run-Evidence oder Runtime-Konfiguration – nicht als allgemeine fachliche Wahrheit in den portablen Skill-Kern.

Für Skills, die auf mehreren Modell-/Runtime-Zielen verwendet werden sollen:

- die tatsächlich vorgesehenen Ziele benennen;
- dieselben relevanten Evalfälle auf diesen Zielen ausführen, soweit praktisch möglich;
- konkrete Provider-/Modellkennung, Runtime-/Adapterstand und Ergebnis im Run dokumentieren, wenn bekannt;
- nicht ausgeführte Kombinationen als `NOT RUN` oder `UNVERIFIED` behandeln;
- Claims auf die tatsächlich gemessenen Umgebungen begrenzen.

Eine herstellerspezifische Modellreihe ist ein Beispiel für eine Testmatrix, **keine universelle Pflichtliste** für alle KI-Regeln-Skills. Ebenso wird kein generisches `model:`-Feld in die gemeinsame `SKILL.md`-Frontmatter eingeführt, nur um eine konkrete Testumgebung festzuschreiben.

Wenn unterschiedliche Modelle unterschiedliche Unterstützung benötigen, zuerst prüfen, ob eine fachliche Invariante im Kern fehlt, der Skill unnötig übererklärt oder unterbestimmt ist, ein deterministischer Schritt besser als Script abgebildet wird oder der Unterschied in einen Runtime-Adapter gehört.

## Reviewfragen

- Ist die fachliche Logik ohne einen bestimmten Client verständlich?
- stehen Modell-, Tool-, Turn- oder Isolationseinstellungen im Kern, obwohl sie runtime-spezifisch sind?
- ist ein Workaround fälschlich zur allgemeinen Prozessregel geworden?
- kann derselbe Kern in einem zweiten kompatiblen Host genutzt werden?
- bleiben Sicherheits- und Human-Gates beim Adapter erhalten?
- ist klar, welche Teile portable Regeln und welche Runtime-Konfiguration sind?
- sind Modell-/Runtime-Claims an tatsächlich ausgeführte Evidence gebunden statt aus Kompatibilität vermutet?

## Ausnahmen

Plattformspezifische Details dürfen im Kern stehen, wenn genau diese Plattform Gegenstand des Skills ist.

Beispiele:

- Review einer konkreten GitHub-Actions-Konfiguration;
- Nutzung einer bestimmten proprietären API;
- Migration zwischen zwei benannten Agentenclients.

Dann ist die Plattform Teil des fachlichen Scopes und keine versehentliche Kopplung.

## Leitgedanke

> Portable Skills kodieren die Disziplin. Adapter kodieren die Umgebung.
