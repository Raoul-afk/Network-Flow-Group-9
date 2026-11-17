# Informatics ITS Graph Theory class Group 9

## 1. Identity
* **Course:** Informatics ITS Graph Theory class Group 9
* **Group Members:**
  * Calixte BERTHIER - 5999261123
  * Emmanuel SANTINI - 5999261124
  * Rida BINDECH - 5999261011

---

## 2. Short explanation about algorithms

### 1. Edmonds-Karp Algorithm (Network Flow)
We implemented the **Edmonds-Karp algorithm** to solve the maximum flow problem in a directed network. 
Unlike the standard Ford-Fulkerson method which can use arbitrary augmenting paths (potentially leading to poor performance or infinite loops with real numbers), Edmonds-Karp strictly uses a **Breadth-First Search (BFS)** to find the shortest augmenting path (in terms of number of edges) at each iteration:
1. **Residual Graph:** The algorithm builds a residual graph containing both forward capacities and backward edges (initialized to 0) to allow flow cancellation.
2. **Shortest Augmenting Path (BFS):** A BFS traverses the residual graph from the source to the sink to find the path with the fewest edges having available capacity.
3. **Bottleneck & Update:** The minimum capacity (bottleneck) along this path is computed and added to the total maximum flow. Residual capacities are then updated across direct and reverse edges.
4. **Termination:** The process repeats until no more augmenting paths can reach the sink.

### 2. Dinic's Algorithm (Network Flow)
We implemented **Dinic's algorithm**, which also finds the maximum flow but works in **phases** instead of one path at a time. Each phase has two steps:
1. **Level graph (BFS):** A BFS from the source over the residual graph gives every vertex a *level* (its distance in edges from the source), using only edges with residual capacity > 0. If the sink is not reached, the algorithm stops: the current flow is maximum.
2. **Blocking flow (DFS):** A DFS then pushes flow from the source to the sink **only along edges going from level *k* to level *k+1***. Many augmenting paths are pushed in the same phase, until every path of the level graph contains a saturated edge (this is called a *blocking flow*). A pointer per vertex remembers the next edge to try, so an edge that led to a dead end is never explored twice in a phase.
3. **Residual update:** As in Edmonds-Karp, each push decreases the forward residual capacity and increases the backward one, which allows flow cancellation.
4. **Termination:** After each phase the distance from the source to the sink strictly increases (it can be at most $V-1$), so there are at most $V$ phases.

**Difference with Edmonds-Karp:** Edmonds-Karp runs one BFS for every single augmenting path, whereas Dinic runs one BFS per phase and then finds all the shortest paths of that phase with the DFS.

---

## 3. Project File Structure

```text
├── main.py     # Point d'entrée principal (runs both algorithms and compares them)
├── Edmonds_karp.py  # Implémentation de l'algorithme d'Edmonds-Karp
├── Dinic.py       # Implémentation de l'algorithme de Dinic
├── Input.py      # Définition du graphe (SOURCE, SINK, edges)
└── README.md

```

---

## 4. Prerequisite to run the code
* **Python 3.8+** (standard library only, no external package)

---

## 5. Instructions to run the code

*Note for macOS / Linux users: Use `python3` (on Windows, `python` or `py`).*

Make sure your `Input.py` file is configured with your desired network, then run from your terminal:

```bash
python main.py    # runs Edmonds-Karp and Dinic, then compares the results
python main.py edmonds  # runs Edmonds-Karp only
python main.py dinic  # runs Dinic only
```

Each algorithm can also be run on its own: `python Edmonds_karp.py` or `python Dinic.py`.

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

--- Dinic Execution (S -> T) ---

Phase 1: levels = S=0, A=1, B=1, C=2, D=2, T=3
  S -> A -> C -> T | Flow added = 7
  S -> B -> C -> T | Flow added = 2
  S -> B -> D -> T | Flow added = 6
  Blocking flow of phase 1 = 15

Phase 2: levels = S=0, A=1, B=2, C=3, D=4, T=5
  S -> A -> B -> C -> D -> T | Flow added = 1
  Blocking flow of phase 2 = 1

--- Final Result ---
Maximum flow from S to T = 16

=== Comparison ===
Edmonds-Karp: 16
Dinic: 16
Both algorithms agree.
```

**How to read the Dinic output:** in phase 1 the shortest paths have 3 edges (T is at level 3), and three of them are pushed after a single BFS (total 15). In phase 2 the distance to T has increased to 5 and the remaining capacity is used by the last path (+1). In phase 3 (not printed) the BFS cannot reach T anymore, so the algorithm stops. The maximum flow, **16**, equals the capacity of the minimum cut {S, A, B} → {C, D, T}: 7 + 3 + 6 = 16.

---

## 8. AI tools usage disclosure

AI tools were used to help structure the README, reformat algorithm explanations for clarity.
