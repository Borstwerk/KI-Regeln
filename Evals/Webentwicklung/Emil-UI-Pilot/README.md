# EK-01 – Design Engineering: überprüfbarer Vergleich mit KI-Regeln

**Stand:** 27.10.2026 · **Status:** `PLANNED / MODEL NOT RUN / BUNDLE NOT ADMITTED`

- [Quellen-/Kandidatenkarte](../../../Dokumentation/Emil-Kowalski-UI-Skills-Optionen.md)
- [Synthetische Entwicklungsfälle](cases.json) – Vorschläge, **nicht**
  ausgeführte oder vorab validierte Benchmarks.
- Originalquelle:
  [emilkowalski/skills](https://github.com/emilkowalski/skills)
  (`main@2d228630ba1446365f614a108cb8252f1feda202`).

## Kernentscheidung

Können *gezielte* Methoden aus den 15 externen UI-Skills
bestehende KI-Regeln-Skills in einem der fünf Bereiche verbessern,
ohne unnötige neue Pflichtskills, unzulässige Seiteneffekte
oder unbelegte UI-/Performance-Claims zu erzeugen?

### Vergleichsarme pro Fall

| Arm | Input / Rechte | Aussage |
| --- | --- | --- |
| **A – Baseline** | Bestehende relevante KI-Regeln-Skills, normaler Workflow/Bootstrap, korrekte QA und Browser-/Quellzugänge | Heutiger Outcome, **keine künstlich geschwächte Baseline** |
| **B – interne Methodenprobe** | Identischer Auftrag; zusätzlich nur die aus EK-01 unabhängig formulierte, kurze Spezialmethode | Lässt sich der Mehrwert ohne externen Skill erreichen? |
| **C – externer Originalskill** | Exakt gewählter, gepinnter `SKILL.md`-Text plus zwingend benötigte gepinnte Referenzen, **nach Security-/Source-Admission** | Ob das vollständige Methodenmaterial gegenüber B mehr bringt |

**Arm C ist BLOCKED**, bis der konkrete Skill inkl. referenzierter
Dateien/Installationsanweisungen durch `skill-security-review` geprüft
und als **Testinput** zugelassen wurde. Keine globale
`npx skills ...`-Installation, keine automatische
Source-Promotion, kein Plugin-/MCP-Zugriff. Fremdanweisungen
bleiben referenzierte Inhalte statt neue Autorität.

### Fünf Pilotspuren

| Spur | Neue Hypothese | Bestehende Owner | Harte Outcomes |
| --- | --- | --- | --- |
| **EK-01A – break-ui** | Plausible Grenzdaten + dev-only Toggle findet **mehr echte** Darstellungs-/Interaktionsfehler | `test-design`, `visual-verification`, `accessibility-review` | Reproduzierbare Datenrandfehler, False Positives, keine Produktions-Toggle-Artefakte |
| **EK-01B – prototype** | 3 sichtbar **verschiedene** Varianten statt 3 Farbtöne verbessern begründete UI-Entscheidung | `frontend-design`, `greybox`, `design-system`, `visual-verification` | Isolation, Bedienbarkeit, kein Product-Write vor Auswahl, realer Unterschied |
| **EK-01C – mobile-native** | Mobile-Web-/PWA-Gerätekanten werden erkannt, die reine Viewportprüfung übersieht | `visual-verification`, `accessibility-review`, `frontend-performance` | Touch-/Keyboard-/Safe-Area-/Viewport-Evidence auf tatsächlichem Gerät |
| **EK-01D – improve-animations** | Read-only Audit liefert **kleine, tatsächlich ausführbare** Handoff-Pläne | `motion-review`, `delegation-contract`, `motion-implementation` | Richtige Prioritäten, vollständiger Code-/Test-/Scope-Contract, kein Auto-Fix |
| **EK-01E – Apple fluid interactions** | Gesten- und Velocity-Handoff-Prüfung findet reale „fühlt sich falsch an“-Defekte | `motion-design`, `motion-review`, `accessibility-review` | Kein Sprung bei Unterbrechung, direkter Kontakt, Reduced Motion, Fokus-/Touchparität |

**Apple-Details:** `apple-design` ist ein *von Emil
Kowalski verfasster*, Apple-inspirierter Web-Skill, **kein**
offizieller Apple-Skill. `animate-expo` und `write-swift`
sind separate, **optionale F-Spuren** nur bei vorhandenem
React-Native/Expo- oder Swift-/SwiftUI-Projekt mit passenden
Versionen. Kein neues Expo-/Swift-Projekt zur Rechtfertigung
eines Skills anlegen.

## Entwicklungsfälle und Negative Controls

Die [`cases.json`](cases.json) enthält jeweils zwei
**synthetische** Fälle pro Spur, darunter bewusste
Near-Misses: völlig passende UI ohne neues Motion-Bedürfnis,
fehlende Browser-/Gerätecapability, nicht zu kopierende
Apple-Stilvorgaben, einmalige UI-Tweaks ohne Prototyp-Bedarf,
Schema-/Datenstress unter echten Inputgrenzen.
Die Fallbeispiele sind *Task-Ideen*, keine angeblich
vorliegenden Repositories oder Browser-Ergebnisse.

### A – realistische UI-Randdaten

1. Unterschied zwischen (a) Demo- und (b) geprüften
   Worst-Case-Daten **am selben API-/Prop-Boundary**.
   Long-name, Unicode/RTL, extreme Beträge, null/one/list,
   Fehlzustände, Statuslängen, 1000-Zeilen-Liste nur
   falls API das tatsächlich zulässt.
2. Kein `<script>` aus Inhaltsfeldern ausführen; keine
   realen Adressen/Tokens in Fixtures.
3. Nur `PASS`, wenn reale Render-/Interaktions-
   Evidence die Wirkung zeigt. Ein Toggle,
   der CSS selbst manipuliert, ist kein gültiger Test.
4. Bei leerem/fehlendem Datenschema explizite
   Unsicherheit und zulässige Testwerte, keine
   erfundene „Produktionsgrenze“.

### B – divergente lokale Prototypen

1. Drei **begründet unterschiedliche** Layout-,
   Interaktions- oder Dichtekonzepte; gemeinsame
   bestehenden Projekt-Tokens respektieren.
2. Isolierter Prototyp, kein produktiver Import
   oder Merge vor Nutzerwahl.
3. Wenn kein Runtime-Server erwünscht ist:
   eine lokal öffnende, selbstständige HTML-Datei,
   nur Standard-Webtechnologien; Umschalten,
   Tastatursteuerung, Fokus und Demo-Interaktionen
   müssen funktionieren, nicht nur Screenshots.
4. Die Original-Picker-Spezifikation aus dem
   Fremdrepo **nicht** kopieren; für Arm B
   unabhängig formulierten Picker nutzen.

### C – mobile-native

1. CSS `@media (hover: hover) and (pointer: fine)`,
   `dvh`, sichere Insets, Touch-/Scroll-/Keyboard-
   Verhalten jeweils auf **tatsächlich** benötigten
   Browsern/Geräten prüfen; keine globale
   UA-/Gerätebreiten-Heuristik.
2. iPad mit Maus/Trackpad und Touch ist
   expliziter Edge Case, wenn relevant.
3. Desktop-Simulation beweist keine realen
   Touch-/Hardware-Eigenheiten.
4. Ohne Gerät `NOT RUN` statt „mobile PASS“.

### D – Motion-Plan-Handoff

1. Unabhängiger read-only Audit mit
   Quellzeilen, Echtheitsprüfung, Priorität,
   klaren Stop-/Scope-Gates.
2. Jeder ausgewählte Fix kann an einen
   anderen Agenten übergeben werden:
   Zielverhalten, konkrete Dateien,
   keine neue Dependency ohne Grund,
   Mess-/Playback-/Reduced-Motion-Gates.
3. Keine unbelegten pauschalen „alles
   über 300ms ist kaputt“-Fehlalarme.
4. `motion-review`-Evidence bleibt maßgeblich;
   ohne Wiedergabe keine gefühlte Motion
   als verifiziert ausgeben.

### E – Apple-inspirierte direkte Manipulation

1. Kontext: Swipe/Sheet, interaktiver
   Drag oder unterbrechbare Navigation;
   kein generelles iOS-/Glass-Redesign.
2. Test **während** der Bewegung:
   Finger folgt Komponente, Input lässt sich
   unterbrechen/umkehren, Release-Velocity
   geht ohne sichtbaren Sprung über,
   Bounds und Cancel funktionieren.
3. Reduced Motion und Tastatur-/Fokus-
   Alternative; Screenreader- und
   Touchziele nicht für reine Physik opfern.
4. Alle konkreten Zeit-, Spring- und
   Gesture-APIs an aktuelle Plattform-/
   Librarydokumentation und realen
   Browser-/Geräte-Support binden.

## Bewertungsvertrag

- **Nicht kompensierbar:** Safety/Accessibility/
  Gate-Verstöße, unautorisierte Produktivänderung,
  eingebautes Test-Backdoor, falsche PASS-Aussage
  oder kopierte unlizenzierte Source.
- **Fachlich:** echte Defekte gefunden,
  falsche Defekte vermieden, Handlungsfähigkeit
  des zweiten Agents, Endnutzer-Outcome,
  richtige Priorisierung und Regressionsquote.
- **Technisch:** Render-/Interaktionsbelege,
  Fokus, Keyboard, ARIA, Touch, Gerätedaten,
  echte Browser- und Performance-Messwerte.
- **Effizienz:** realer Agenten-Input/Output,
  Docs-/Skill-Reads, Wiederholungen,
  Latenz und Gesamtkosten – nur soweit
  wirklich gemessen; sonst `NOT MEASURED`.
- **Getrennte Evidenz:** Markdown-Eval,
  statischer Source-Review, lokales HTML,
  Browser-Snapshot und echter Touch-Test
  sind **verschiedene Nachweisklassen**.

### Sichere Ausführungsreihenfolge

1. Daten-/Taskpakete und unabhängige
   Judge-Kriterien in isolierter Sandbox
   **vor** Agentenläufen einfrieren.
2. Erst **EK-01A** und **EK-01B** als kleine
   A/B-Vergleiche (ein Fall pro Spur,
   gleiche Tools/Version/Effort/Limit).
3. **EK-01C** nur mit real verfügbarem
   Smartphone/Tablet, sonst separat markieren.
4. **EK-01D/E** nur mit tatsächlicher
   laufender UI und gesicherten Browser-/
   Playback-/Gestendaten; keine künstlichen
   PASS-Nachweise aus Quelltext.
5. **C-Arm** erst nach separatem
   Bundle-Admission-Review; danach
   höchstens bedarfsweise statt alle 15
   Skills im Kontext zu laden.
6. Am Schluss: vorhandenen Owner ergänzen,
   **nur** einen eindeutig neuen Spezialskill
   bauen, optionalen Originalskill zulassen,
   oder `KEEP BASELINE`.

Keine direkten Modell-APIs, kein zusätzlicher
geplanter GitHub-Action-Agentenlauf,
keine lokalen Softwarepflichtinstallationen.

## Status

| Nachweis | Stand |
| --- | --- |
| 15 Upstream-Skills und KI-Regeln-Katalog statisch gelesen | `OBSERVED` |
| Bestehenden überwachten Motion-Upstream und Versionsdrift erkannt | `OBSERVED / DIFF UNREVIEWED` |
| EK-01 A–E + vorbereitete Dev-Fälle | `PLANNED` |
| Tatsächliche Testfälle durch Agenten/Browser/Touch ausgeführt | `NOT RUN` |
| Qualität/Tokenersparnis oder neuer Skill gerechtfertigt | `UNVERIFIED` |
