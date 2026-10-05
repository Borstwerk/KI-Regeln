# Toolanforderungen und Fallbacks

## Inhalt

- Grundprinzip
- Typische Capabilities
- Capability Detection
- Plugin-/App-Routing
- Gute Fallbacks
- Kein Capability-Theater
- Rechte und Least Privilege
- Script Dependency Contract
- Portabilität
- Leitgedanke

## Grundprinzip

Ein Skill darf Fähigkeiten der Laufzeit nicht stillschweigend voraussetzen.

Vor der Ausführung unterscheiden:

- **requires** – ohne diese Fähigkeit ist der Skill nicht sinnvoll ausführbar;
- **optional** – verbessert den Workflow;
- **forbidden unless approved** – riskante Fähigkeit, die nicht automatisch genutzt werden darf.

## Typische Capabilities

Beispiele:

- Dateien lesen;
- Dateien schreiben;
- Webzugriff;
- Browser-/Renderzugriff;
- Shell / Codeausführung;
- GitHub lesen oder schreiben;
- Subagents / Parallelisierung;
- Screenshots;
- Netzwerkzugriff;
- externe Aktionen.

## Capability Detection

```text
bevorzugter Weg
→ Capability vorhanden?
   ├─ ja → verwenden
   └─ nein
        ↓
      definierter Fallback vorhanden?
        ├─ ja → transparent degradieren
        └─ nein → blocked / unverified melden
```

## Plugin-/App-Routing

Eine benötigte Capability kann aus unterschiedlichen Runtime-Quellen kommen:

- nativ aus dem Host;
- aus einem bereits installierten/verbundenen Plugin oder einer App;
- aus einer erst noch zu verbindenden externen Integration;
- aus einem manuellen Fallback.

Bevor ein Nutzer zu Copy-Paste, CSV-Export, Screenshots oder einem manuellen Wechsel in ein Fremdsystem geschickt wird, prüfen:

~~~text
Capability benötigt
→ nativ vorhanden?
   ├─ ja → nutzen
   └─ nein
        ↓
      passende verbundene Integration vorhanden?
        ├─ ja → Scope + Rechte prüfen → nutzen
        └─ nein
             ↓
           Plugin/App verfügbar und materiell hilfreich?
             ├─ ja → Verbindung/Installation anbieten
             └─ nein → Fallback
~~~

Dabei gilt:

~~~text
verfügbar ≠ verbunden
verbunden ≠ autorisiert
lesen ≠ schreiben ≠ externe Aktion
~~~

Für die lokale Risikoabschätzung können externe Integrationen grob als `READ`, `WRITE` oder `ACTION` betrachtet werden. Das ist eine Governancehilfe, keine universelle technische Plugin-Klassifikation.

Konkrete Appnamen gehören normalerweise in Runtime-/Adapterlogik, nicht in den portablen fachlichen Skill-Kern.

Details: `Plugin-App-und-Capability-Routing.md`.

## Gute Fallbacks

Fallbacks erhalten möglichst die fachliche Disziplin.

Beispiele:

- keine Subagents → Research-Threads sequenziell statt parallel bearbeiten;
- kein Browser → visuelle Verifikation ausdrücklich als nicht durchgeführt markieren;
- kein ausführbarer Test → keine bestandene Verifikation behaupten;
- kein GitHub-Schreibzugriff → Patch/Änderungsvorschlag liefern statt Commit behaupten.

## Kein Capability-Theater

Nicht behaupten:

- einen Browser geprüft zu haben, wenn nur Code gelesen wurde;
- parallel delegiert zu haben, wenn keine Delegation verfügbar war;
- Tests ausgeführt zu haben, wenn nur Testcode betrachtet wurde;
- eine Quelle geöffnet zu haben, wenn nur ein Suchsnippet vorlag.

## Rechte und Least Privilege

Ein Skill soll nur die Rechte verlangen, die sein Auftrag wirklich benötigt.

Lesen und Bewerten benötigt nicht automatisch Schreib-, Netzwerk- oder Ausführungsrechte.

Riskante, irreversible oder extern sichtbare Aktionen bleiben an vorhandene Freigaberegeln gebunden.

## Script Dependency Contract

Ein Skill, der Scripts oder andere ausführbare Hilfen nutzt, soll deren Laufzeitvoraussetzungen explizit machen.

Mindestens prüfen beziehungsweise dokumentieren:

- benötigte Runtime oder Interpreter;
- benötigte Packages, Libraries oder externe Tools;
- Versionsgrenzen nur dort, wo sie fachlich oder technisch relevant sind;
- ob Package-Manager, Netzwerk oder weitere Installationsrechte benötigt würden;
- wie die Verfügbarkeit vor Ausführung geprüft wird;
- welcher Fallback oder `blocked`-/`unverified`-Status gilt, wenn eine Abhängigkeit fehlt.

Eine fehlende Dependency ist **keine automatische Installationsautorisierung**.

```text
Dependency feststellen
→ bereits vorhanden?
   ├─ ja → verwenden
   └─ nein
        ↓
      Installation in dieser Runtime möglich und autorisiert?
        ├─ ja → kontrolliert installieren / bereitstellen
        └─ nein → Fallback oder blocked
```

Ein `pip install`, `npm install`, System-Package-Install oder vergleichbarer Write/Network-Schritt darf nicht allein deshalb ausgeführt werden, weil ein Script ihn benötigt. Runtime-Adapter oder vorbereitete Umgebungen dürfen Dependencies bereitstellen, ohne den portablen Skill-Kern mit host-spezifischen Installationsbefehlen zu füllen.

## Portabilität

Toolnamen oder Clientmechanik nicht unnötig mit der fachlichen Logik vermischen.

Bevorzugt:

```text
Capability: Webzugriff
```

statt:

```text
muss Tool X mit Parameter Y verwenden
```

sofern die konkrete Plattform nicht selbst Gegenstand des Skills ist.

### Portabler Kern und Runtime-Adapter

Modellwahl, konkrete Toolnamen, Turn-Limits, Isolationseinstellungen oder client-spezifische Subagent-/Hook-Konfiguration gehören nicht automatisch in den fachlichen Skill-Kern.

Bevorzugtes Modell:

```text
Skill-Kern
→ fachliche Disziplin + Capability-Vertrag

Runtime-Adapter
→ konkrete Tools + Modell + Limits + Hostmechanik
```

Ein beobachteter Modellfehler soll nicht reflexartig als allgemeine Skillregel konserviert werden. Zuerst prüfen, ob eine fachliche Invariante fehlt oder lediglich ein host-/modellspezifischer Workaround nötig ist.

Adapter dürfen Sicherheits-, Scope- oder Human-Gates des Kerns nicht abschwächen.

Details: `Portabler-Skill-Kern-und-Runtime-Adapter.md`.

## Leitgedanke

> Ein portabler Skill beschreibt benötigte Fähigkeiten und ehrliche Fallbacks – nicht eine erfundene Idealumgebung.
