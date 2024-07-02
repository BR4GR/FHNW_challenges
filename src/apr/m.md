## Lernpfad Asymptotische Komplexität

- Die Grundidee, wieviel mal länger braucht ein Algorithmus bei wachsendem Input? 
- Die Komplexität ist die Funktion die die Wachstumsrate der Laufzeit wachsendem Input beschreibt.
- T(n)
- Algorithmen werden in Komplexitätsklassen eingeteilt, um ihre Effizienz zu vergleichen. Diese Klassen geben an, wie schnell die Laufzeit oder der Ressourcenverbrauch wächst.
- in aufsteigender Komplexität:
	-  **O(1)**: Konstant
	- **O(log n)**: Logarithmisch
	- O(n**1/2)
	- **O(n)**: Linear
	- **O(n log n)**: Linear-logarithmisch
	- **O(n^2)**: Quadratisch
	- **O(n^3)**: Kubisch
	- **O(n^x)**: x  bis unendlich
	- **O(2^n)**: Exponentiell
	- **O(x^n)**: Exponentiell x  bis unendlich
	- **O(n!)**: Fakultät
- Die O-Notation (Big-O-Notation) wird verwendet, um eine obere Schranke für die Laufzeitfunktion eines Algorithmus zu definieren. Sie beschreibt das schlimmste Wachstumsszenario der Laufzeit, indem sie irrelevante konstante Faktoren und niedrigere Ordnungsfaktoren ignoriert.
- Die asymptotische Komplexität ist besonders nützlich, um das Verhalten von Algorithmen für sehr große Eingabegrößen zu verstehen und zu vergleichen, da konstante Faktoren und kleinere Eingaben oft weniger relevant sind.
- Rechenregeln für die O-Notation
	- ![[asymptotische_kompexität_rechnungen.png]]
- Die asymptotische Komplexität hilft Entscheidungen darüber zu treffen, welche Algorithmen für bestimmte Anwendungen geeignet sind, insbesondere wenn mit großen Datenmengen gearbeitet wird.
- Sie bietet ein Werkzeug, um die langfristige Skalierbarkeit und Effizienz von Algorithmen zu beurteilen und zu optimieren.
- Achtung! Komplexität kann nicht immer nur durch das zählen von schleifen bestimmt werden.
- 

#### Beispiel 1:
```python
count = 0
for i in range(n):
    for j in range(4):
        for k in range(j):
            count += 1
```
- **Äußere Schleife**: Läuft \( n \) Mal.
- **Mittlere Schleife**: Läuft 4 Mal (konstant).
- **Innere Schleife**: Läuft j Mal, wobei j von 0 bis 3 variiert.
- Komplexität: Die innere Schleife läuft im Durchschnitt 2 Mal pro Iteration der mittleren Schleife, also insgesamt \( 4 \times 2 = 8 \). Daher beträgt die Gesamtkomplexität \( O(n) \).

#### Beispiel 2:
```python
count = 0
i = 1
while i < n:
    count += 1
    i *= 2
```
- Die Schleife verdoppelt \( i \) bei jeder Iteration.
- Komplexität: \( O(\log n) \).

#### Beispiel 3:
```python
count = 0
for i in range(n):
    for j in range(2 ** i):
        count += 1
```
- **Äußere Schleife**: Läuft \( n \) Mal.
- **Innere Schleife**: Läuft \( 2^i \) Mal.
- Komplexität: \( O(2^0 + 2^1 + 2^2 + ... + 2^{n-1}) \) = \( O(2^n) \).

#### Beispiel 4:
```python
count = 0
for i in range(2 ** n):
    for j in range(i):
        count += 1
```
- **Äußere Schleife**: Läuft \( 2^n \) Mal.
- **Innere Schleife**: Läuft im Durchschnitt \( 2^{n-1} \) Mal.
- Komplexität: \( O(2^n \times 2^{n-1}) = O(2^{2n-1}) = O(2^{2n}) \).


## Datenablage in Arrays

### Python Listen

- Eine Python-Liste ist im Grunde nur ein Array mit einem Zähler. Sobald das Array voll ist, wird alles in ein größeres Array kopiert:
     ```python
     lst = [[0] * 10, 0]  # Array-basierte Liste mit Länge 10
     # [das Array, der Zähler]
     ```

**Komplexität der wichtigsten Funktionen**:
- O(n)
	- `index(lst, value, start, stop)`
	- `count(lst, value)` Vorkommen eines Wertes zählen
	- `insert(lst, index, element)` wegen des Verschiebens
	- `remove(lst, value)` wegen des Verschiebens
- O(1)
	- `append(lst, element)`


### **Programmieraufgaben: Heuristik über Zufallsgenerator-Verteilung**

Aufgabe: Dokumentation der Häufigkeitsverteilung von Zufallszahlen durch Datenstrukturen, die Paare aus Zufallswerten und deren Häufigkeit speichern.

**Vier verschiedene Implementierungen**:
- a **Liste von Paaren (Tupeln)**
- b **Geordnete Liste mit binärer Suche**
- c **Liste mit Zufallszahlen als Indizes**
- d Dictionary

Dieses Thema haben wir ausführlich besprochen glaube ich.
die Rangliste ist:
- c Direkter Zugriff auf die liste via index
- d Dictionary ist ein bisschen langsamer wegen hashing hat aber auch zugriff O(1)
- b muss das element suchen aber braucht dafür nur log(n) zusätzliche Zeit
- a am langsamsten wegen extra loop zum suchen


### Binäre Suche Wichtige Konzepte:

- **3-Wege-Suche**:
	- Verwendet drei Fälle (< x, x, > x) und beendet die Suche, wenn x gefunden wird oder die Bereiche aneinanderstoßen.
- **2-Wege-Suche**:
	- Verwendet zwei Fälle (links, rechts) und ist kürzer und effizienter als die 3-Wege-Suche.
    - Sucht Grenzen zwischen zwei Bereichen, z.B. alle Werte kleiner als x und alle Werte größer oder gleich x.
- **Anwendung auf kontinuierliche Funktionen**:
    - Die Monotonie einer Funktion ermöglicht die Anwendung der binären Suche auf kontinuierlich verteilte Werte.
    - Abbruchkriterium bei einer vorgegebenen Genauigkeit oder wenn keine weiteren darstellbaren Werte zwischen den Intervallgrenzen vorhanden sind.

### Hash Tables

- Hash Tables (dictionary in python) bieten schnelle Zugriffszeiten , idealerweise in O(1).

- **Die Funktion `hash()`**:
    - Hash-Funktion erzeugt einen Hash-Wert für ein Element, der zur Berechnung eines Indexes in der Hash Table verwendet wird.
    - Beispiel: `hash(e) % n` berechnet den Index, an dem das Element e gespeichert wird, wobei n die Größe der Tabelle ist.
    - Ziel der Hash-Funktion: gleichmäßige und reproduzierbare Verteilung der Hash-Werte.
    - die Länge des tables sollte eine Primzahl sein andernfalls könnte es sein das nur wenige indexes des Tables genutzt werden, dass liegt daran das die länge des Tables und die hashes zu grosse gemeinsame Teiler haben.
- 
- **Kollisionsbehandlung**:
    - **Separate Chaining**:
        - Bei Kollisionen werden Elemente in einer Liste am berechneten Index gespeichert.
        - Einfach zu implementieren, aber zusätzlicher Speicheraufwand für Listen.
    - **Open Addressing**:
        - Elemente werden direkt in der Hash Table gespeichert, und bei Kollisionen wird ein alternativer Platz gesucht.
        - **Linear Probing**: Suche nach dem nächsten freien Platz in linearer Reihenfolge.
        - **Double Hashing**: Verwendung einer zweiten Hash-Funktion zur Berechnung eines neuen Schritts bei Kollisionen, um Clustering zu vermeiden.

- **Load Factor (λ)**:
    - Verhältnis von Anzahl der Elemente zur Tabellengröße.
    - Empfehlungen für Effizienz:
        - Separate Chaining: λ < 1.
        - Linear Probing: λ < 0.75.
        - Double Hashing: λ < 0.9.
    - Rehashing: Erzeugung einer größeren Tabelle und Neuberechnung der Positionen, wenn der Load Factor eine Grenze überschreitet.

```

```