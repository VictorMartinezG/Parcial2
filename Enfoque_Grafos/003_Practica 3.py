# Práctica 3: Búsqueda en Profundidad (DFS)
def dfs(grafo, inicio, objetivo, visitados=None):
    if visitados is None:
        visitados = set()  # Inicializamos el conjunto de nodos visitados

    visitados.add(inicio)  # Marcamos el nodo actual como visitado

    if inicio == objetivo:
        return [inicio]  # Si encontramos el objetivo, devolvemos el camino

    for vecino in grafo.get(inicio, []):  # Exploramos vecinos no visitados
        if vecino not in visitados:
            camino = dfs(grafo, vecino, objetivo, visitados)
            if camino:
                return [inicio] + camino  # Si encontramos el camino, lo construimos

    return None  # Si no se encuentra el objetivo

# Grafo simple para DFS
grafo_simple = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("\nDFS - Camino encontrado:", dfs(grafo_simple, 'A', 'F'))