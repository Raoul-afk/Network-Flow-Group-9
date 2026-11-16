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

def bfs(residual_graph, source, sink, parent):
    """Breadth-First Search to find an augmenting path in the residual graph."""
    visited = {source}
    queue = [source]
    
    while queue:
        u = queue.pop(0)
        
        for v, cap in residual_graph[u].items():
            # If not visited and there is available residual capacity
            if v not in visited and cap > 0:
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
                queue.append(v)
                
    return False

def edmonds_karp(edge_list, source, sink):
    """Executes the Edmonds-Karp algorithm to find the maximum flow."""
    residual_graph = build_residual_graph(edge_list)
    parent = {}
    max_flow = 0
    iteration = 1

    print(f"--- Edmonds-Karp Execution ({source} -> {sink}) ---\n")

    # While there is an augmenting path from source to sink
    while bfs(residual_graph, source, sink, parent):
        # Find the bottleneck capacity along the path found
        path_flow = float("inf")
        curr = sink
        path = []
        
        while curr != source:
            path.append(curr)
            prev = parent[curr]
            path_flow = min(path_flow, residual_graph[prev][curr])
            curr = prev
        path.append(source)
        path.reverse()
        
        print(f"Iteration {iteration}: {' -> '.join(path)} | Flow added = {path_flow}")

        # Update residual capacities of the edges and reverse edges
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = u

        max_flow += path_flow
        iteration += 1
        parent = {}

    print(f"\n--- Final Result ---")
    print(f"Maximum flow from {source} to {sink} = {max_flow}")
    return max_flow

if __name__ == "__main__":
    edmonds_karp(edges, SOURCE, SINK)
