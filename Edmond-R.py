from input import edges, SOURCE, SINK

def build_residual_graph(edge_list):
    """
    Construit le graphe résiduel à partir de la liste d'arcs orientés.
    """
    residual = {}
    
    for u, v, cap in edge_list:
        if u not in residual:
            residual[u] = {}
        if v not in residual:
            residual[v] = {}
            
        residual[u][v] = residual[u].get(v, 0) + cap
        
        if u not in residual[v]:
            residual[v][u] = 0
            
    return residual

def bfs(residual_graph, source, sink, parent):
    """
    Parcours en largeur (BFS) utilisant une liste classique au lieu de deque.
    """
    visited = {source}
    queue = [source]  # Utilisation d'une liste standard
    
    while queue:
        # .pop(0) retire le premier élément (comportement FIFO),
        # mais décale tous les éléments restants (moins performant sur de très grands graphes).
        u = queue.pop(0)
        
        for v, cap in residual_graph[u].items():
            if v not in visited and cap > 0:
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
                queue.append(v)
                
    return False

def edmonds_karp(edge_list, source, sink):
    """
    Exécute l'algorithme d'Edmonds-Karp sans dépendance externe.
    """
    residual_graph = build_residual_graph(edge_list)
    parent = {}
    max_flow = 0
    iteration = 1

    print(f"--- Exécution d'Edmonds-Karp ({source} -> {sink}) --- (Sans deque)\n")

    while bfs(residual_graph, source, sink, parent):
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
        
        print(f"Itération {iteration} : {' -> '.join(path)} | Flot ajouté = {path_flow}")

        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = u

        max_flow += path_flow
        iteration += 1
        parent = {}

    print(f"\n--- Résultat final ---")
    print(f"Valeur du flot maximal de {source} à {sink} = {max_flow}")
    return max_flow

if __name__ == "__main__":
    edmonds_karp(edges, SOURCE, SINK)