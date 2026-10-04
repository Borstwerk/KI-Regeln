# Responsive Design und Interaktion

## Inhalt

- Zweck
- Grundregel
- 1. Mobile nicht erst am Ende prüfen
- 2. Inhalt priorisieren statt nur umbrechen
- 3. Breakpoints aus Layoutbedarf ableiten
- 4. Touch und Pointer unterscheiden
- 5. Interaktion braucht sichtbare Zustände
- 6. Motion unterstützt Orientierung
- 7. Motion begrenzen
- 8. Progressive Experience Enhancement
- 9. Formulare als Interaktionssystem
- 10. Navigation muss erreichbar bleiben
- 11. Dichte bewusst steuern
- Qualitätscheck
- Leitgedanke

## Zweck

Dieses Dokument beschreibt responsive Gestaltung und Interaktion als Teil des Designs – nicht als nachträgliche technische Reparatur.

## Grundregel

> Responsive bedeutet nicht, Desktop schmaler zu machen. Es bedeutet, Priorität und Bedienung an den verfügbaren Raum anzupassen.

## 1. Mobile nicht erst am Ende prüfen

Bereits während Design und Greyboxing berücksichtigen:

- Reihenfolge der Inhalte;
- Navigation;
- Hauptaktionen;
- Tabellen und Datenansichten;
- komplexe Formulare;
- Medienverhältnisse;
- Touch-Ziele;
- Sticky-Elemente.

## 2. Inhalt priorisieren statt nur umbrechen

Auf kleinen Screens kann es sinnvoll sein:

- Sekundärinformationen später zu zeigen;
- komplexe Vergleiche anders darzustellen;
- Navigation zu verdichten;
- Nebenaktionen in Menüs zu verschieben;
- große Visualisierungen auf mehrere Zustände aufzuteilen.

Wichtig ist, dass die Kernaufgabe erhalten bleibt.

## 3. Breakpoints aus Layoutbedarf ableiten

Nicht automatisch nur bekannte Gerätebreiten verwenden.

Ein Breakpoint ist sinnvoll, wenn das bestehende Layout nicht mehr lesbar oder bedienbar bleibt.

## 4. Touch und Pointer unterscheiden

Prüfen:

- ausreichend große Touch-Ziele;
- Hover ist nie die einzige Informationsquelle;
- Drag-and-Drop besitzt gegebenenfalls Alternativen;
- Kontextmenüs sind nicht der einzige Zugangsweg;
- Tooltips enthalten keine unverzichtbaren Informationen.

## 5. Interaktion braucht sichtbare Zustände

Mindestens relevante Zustände gestalten:

- default;
- hover, sofern sinnvoll;
- focus;
- active/pressed;
- disabled;
- loading;
- success;
- error;
- empty.

Nicht nur den idealen Screenshot-Zustand bauen.

## 6. Motion unterstützt Orientierung

Animation kann helfen bei:

- räumlicher Kontinuität;
- Statuswechseln;
- Fokusführung;
- Bestätigung einer Aktion;
- verständlichem Ein-/Ausblenden.

Nicht jede Section braucht Scroll-Reveal.

## 7. Motion begrenzen

Vermeiden:

- unnötige Daueranimationen;
- große Parallaxeffekte ohne Zweck;
- Interaktionen, die Inhalt verzögern;
- Animationen, die Fokus oder Lesbarkeit verschlechtern;
- stark unterschiedliche Easing- und Dauerwerte ohne System.

`prefers-reduced-motion` und vergleichbare Nutzerpräferenzen berücksichtigen.

## 8. Progressive Experience Enhancement

Aufwendige 3D-, WebGL-, Canvas-, Parallax-, Scrolltelling- oder andere Experience-Layer dürfen die Kernaufgabe einer Website nicht versehentlich an eine einzige technische Fähigkeit binden.

Für relevante Signature Experiences einen lokalen **Fallback Contract** definieren:

```text
Core Experience
- Welche Information / Aufgabe muss erhalten bleiben?

Enhanced Experience
- Was fügt 3D / Motion / Scroll / Canvas tatsächlich hinzu?

Mobile / Touch
- Wie funktioniert die Aufgabe ohne Hover oder große Pointerfläche?

Reduced Motion
- Welche Information bleibt erhalten, wenn Bewegung reduziert/ersetzt wird?

Capability / Failure
- Was passiert, wenn Spezialruntime, Asset, WebGL/Canvas oder Enhancement nicht verfügbar ist?
```

Für Marketing-, Editorial- und Informationsseiten soll Kerninhalt beziehungsweise Haupt-CTA nicht ausschließlich hinter einem Spezialeffekt liegen.

Bei Produkten, deren eigentliche Funktion technisch an 3D/WebGL gebunden ist, muss der Fallback nicht dieselbe Funktion vollständig replizieren. Er soll aber den Zustand ehrlich erklären und, soweit möglich, Orientierung oder einen alternativen Pfad anbieten.

Progressive Enhancement bedeutet nicht zwingend „alles muss ohne JavaScript identisch funktionieren“. Es bedeutet, dass zusätzliche technische Fähigkeiten **bewusst** auf einen tragfähigen Kern aufgesetzt werden und ihr Ausfall nicht zufällig über Produktbedeutung oder Navigation entscheidet.

## 9. Formulare als Interaktionssystem

Prüfen:

- klare Labels;
- sinnvolle Gruppierung;
- verständliche Pflichtfelder;
- Inline-Hinweise dort, wo sie helfen;
- Fehlermeldungen nah am Problem;
- Datenverlust bei Fehlern vermeiden;
- korrekte Tastaturbedienung.

## 10. Navigation muss erreichbar bleiben

Responsive Navigation darf nicht nur kompakter, sondern muss weiterhin verständlich sein.

Prüfen:

- Menüöffnung und -schließung;
- Fokusführung;
- Escape-Verhalten;
- aktuelle Seite;
- Unterebenen;
- Scrollposition;
- Touchbedienung.

## 11. Dichte bewusst steuern

Desktop darf mehr Parallelität zeigen, Mobile braucht häufiger Sequenz.

Das bedeutet nicht automatisch große Abstände auf kleinen Screens. Entscheidend ist lesbare und bedienbare Informationsdichte.

## Qualitätscheck

1. Wurde Mobile bereits vor der Implementierungsphase berücksichtigt?
2. Bleibt die Hauptaufgabe auf kleinen Screens klar?
3. Sind Breakpoints inhaltlich begründet?
4. Funktioniert die Oberfläche ohne Hover?
5. Sind Focus-, Loading-, Error- und Empty-States vorhanden?
6. Dient Motion der Orientierung?
7. Werden Nutzerpräferenzen berücksichtigt?
8. Besitzen aufwendige Signature Experiences einen expliziten Core-/Enhanced-/Fallback-Vertrag?
9. Sind Formulare und Navigation auch per Tastatur und Touch bedienbar?

## Leitgedanke

> Responsive Qualität zeigt sich nicht daran, dass nichts überläuft, sondern daran, dass die Aufgabe auf jedem relevanten Gerät verständlich und bedienbar bleibt.