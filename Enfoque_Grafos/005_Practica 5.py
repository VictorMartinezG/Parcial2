
# Práctica 4: Búsqueda en Profundidad Limitada
def profundidad_limitada(grafo, inicio, objetivo, limite):
    def dfs_limitado(nodo, objetivo, limite, camino):
        if limite < 0:
            return None  # Si se supera el límite, se detiene
        camino.append(nodo)  # Agregamos el nodo actual al camino
        if nodo == objetivo:
            return camino  # Si llegamos al objetivo, devolvemos el camino
        for vecino in grafo.get(nodo, []):
            resultado = dfs_limitado(vecino, objetivo, limite - 1, list(camino))
            if resultado:
                return resultado
        return None

    return dfs_limitado(inicio, objetivo, limite, [])

# Práctica 5: Búsqueda en Profundidad Iterativa
def profundidad_iterativa(grafo, inicio, objetivo, limite_max):
    for limite in range(limite_max + 1):  # Se aumenta el límite progresivamente
        resultado = profundidad_limitada(grafo, inicio, objetivo, limite)
        if resultado:
            return resultado  # Se devuelve el primer camino encontrado
    return None  # Si no se encuentra camino


grafo_simple = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("\nDFS Iterativo - Camino:", profundidad_iterativa(grafo_simple, 'A', 'F', 5))