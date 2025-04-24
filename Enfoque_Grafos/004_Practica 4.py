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
                return resultado  # Retornamos si se encuentra una solución
        return None

    return dfs_limitado(inicio, objetivo, limite, [])  # Inicia el DFS con límite

print("\nDFS Limitado - Camino:", profundidad_limitada(grafo_simple, 'A', 'F', 3))
