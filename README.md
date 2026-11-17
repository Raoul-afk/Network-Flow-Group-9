# Informatics ITS Graph Theory class Group 9

## 1. Identity
* **Course:** Informatics ITS Graph Theory class Group 9
* **Group Members:**
  * Calixte BERTHIER - 5999261123
  * Emmanuel SANTINI - 5999261124
  * 

---

## 2. Short explanation about algorithms

### 1. Edmonds-Karp Algorithm (Network Flow)
We implemented the **Edmonds-Karp algorithm** to solve the maximum flow problem in a directed network. 
Unlike the standard Ford-Fulkerson method which can use arbitrary augmenting paths (potentially leading to poor performance or infinite loops with real numbers), Edmonds-Karp strictly uses a **Breadth-First Search (BFS)** to find the shortest augmenting path (in terms of number of edges) at each iteration:
1. **Residual Graph:** The algorithm builds a residual graph containing both forward capacities and backward edges (initialized to 0) to allow flow cancellation.
2. **Shortest Augmenting Path (BFS):** A BFS traverses the residual graph from the source to the sink to find the path with the fewest edges having available capacity.
3. **Bottleneck & Update:** The minimum capacity (bottleneck) along this path is computed and added to the total maximum flow. Residual capacities are then updated across direct and reverse edges.
4. **Termination:** The process repeats until no more augmenting paths can reach the sink. The time complexity is guaranteed to be $O(V \cdot E^2)$.

### 2. [Second Algorithm ]


---

## 3. Project File Structure

```text
├── main.py          # Point d'entrée principal
├── Edmonds_karp.py  # Implémentation de l'algorithme
├── Input.py         # Définition du graphe (SOURCE, SINK, edges)
└── README.md

```

---

## 4. Prerequisite to run the code
* **Python 3.8+**

---

## 5. Instructions to run the code

*Note for macOS / Linux users: Use `python3` (on Windows, `python` or `py` usually works).*

Make sure your `input.py` file is configured with your desired network, then execute the Edmonds-Karp script directly from your terminal:

```bash
python main.py
```

---

## 6. Input file format (`Input.py`)
The network is defined via a modular Python input structure:
* `SOURCE`: The starting node identifier (e.g., `"S"`).
* `SINK`: The destination node identifier (e.g., `"T"`).
* `edges`: A list of directed tuples formatted as `(u, v, capacity)`.

Example (`Input.py`):
```python
SOURCE = "S"
SINK = "T"

edges = [
    ("S", "A", 10),
    ("S", "B", 8),
    ("A", "B", 4),
    ("A", "C", 7),
    ("B", "C", 3),
    ("B", "D", 6),
    ("C", "D", 2),
    ("C", "T", 9),
    ("D", "T", 8),
]
```

---

## 7. Result of sample run

```text
=== Algorithm Execution ===
--- Edmonds-Karp Execution (S -> T) ---

Iteration 1: S -> A -> C -> T | Flow added = 7
Iteration 2: S -> B -> C -> T | Flow added = 2
Iteration 3: S -> B -> D -> T | Flow added = 6
Iteration 4: S -> A -> B -> C -> D -> T | Flow added = 1

--- Final Result ---
Maximum flow from S to T = 16
```


---

## 8. AI tools usage disclosure

AI tools were used to help structure the README, reformat algorithm explanations for clarity, and assist in Python code modularization. All core logic, graph structures, and validation checks were carried out by the team.
