from collections import deque
from Input import edges, SOURCE, SINK


def build_residual_graph(edge_list):
    """Builds the residual graph from the list of directed edges."""
    residual = {}

    for u, v, cap in edge_list:
        if u not in residual:
            residual[u] = {}
        if v not in residual:
            residual[v] = {}

        # Add forward capacity
        residual[u][v] = residual[u].get(v, 0) + cap

        # Ensure backward edge exists with initial capacity of 0
        if u not in residual[v]:
            residual[v][u] = 0

    return residual


def bfs_levels(residual_graph, source, sink):
    """BFS from the source that assigns a level (distance in edges) to every
    vertex reachable through edges with residual capacity > 0.
    Returns the level dictionary, or None if the sink is unreachable."""
    level = {source: 0}
    queue = deque([source])

    while queue:
        u = queue.popleft()

        for v, cap in residual_graph[u].items():
            # Not yet leveled and there is available residual capacity
            if v not in level and cap > 0:
                level[v] = level[u] + 1
                queue.append(v)

    return level if sink in level else None


def dfs_push(residual_graph, u, sink, pushed, level, neighbors, pointer, path):
    """DFS restricted to the level graph (edges going from level k to level k+1).
    Pushes flow along ONE path from u to the sink and returns the amount pushed
    (0 if no path exists). 'pointer' remembers, for each vertex, the next edge to
    try, so an edge that led to a dead end is never explored twice in a phase."""
    if u == sink:
        path.append(u)
        return pushed

    while pointer[u] < len(neighbors[u]):
        v = neighbors[u][pointer[u]]
        cap = residual_graph[u][v]

        # Only follow edges that go exactly one level deeper and still have capacity
        if cap > 0 and level.get(v, -1) == level[u] + 1:
            flow = dfs_push(residual_graph, v, sink, min(pushed, cap),
                            level, neighbors, pointer, path)
            if flow > 0:
                # Update residual capacities of the edge and its reverse edge
                residual_graph[u][v] -= flow
                residual_graph[v][u] += flow
                path.append(u)
                return flow

        # Dead end (or saturated edge): never try this edge again in this phase
        pointer[u] += 1

    return 0


def dinic(edge_list, source, sink):
    """Executes Dinic's algorithm to find the maximum flow."""
    residual_graph = build_residual_graph(edge_list)

    if source not in residual_graph or sink not in residual_graph:
        raise ValueError("SOURCE and SINK must both appear in the edges list.")
    if source == sink:
        raise ValueError("SOURCE and SINK must be different vertices.")

    max_flow = 0
    phase = 1

    print(f"--- Dinic Execution ({source} -> {sink}) ---\n")

    # Each loop turn is one phase: BFS levels, then a blocking flow with DFS
    while True:
        level = bfs_levels(residual_graph, source, sink)
        if level is None:
            break  # the sink can no longer be reached: the flow is maximum

        levels_text = ", ".join(f"{v}={l}" for v, l in sorted(level.items(), key=lambda x: x[1]))
        print(f"Phase {phase}: levels = {levels_text}")

        neighbors = {u: list(residual_graph[u]) for u in residual_graph}
        pointer = {u: 0 for u in residual_graph}
        phase_flow = 0

        # Blocking flow: keep pushing paths until none is left in the level graph
        while True:
            path = []
            pushed = dfs_push(residual_graph, source, sink, float("inf"),
                              level, neighbors, pointer, path)
            if pushed == 0:
                break

            path.reverse()
            print(f"  {' -> '.join(path)} | Flow added = {pushed}")
            phase_flow += pushed

        print(f"  Blocking flow of phase {phase} = {phase_flow}\n")
        max_flow += phase_flow
        phase += 1

    print(f"--- Final Result ---")
    print(f"Maximum flow from {source} to {sink} = {max_flow}")
    return max_flow


if __name__ == "__main__":
    dinic(edges, SOURCE, SINK)
