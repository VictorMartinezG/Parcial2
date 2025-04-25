# Práctica 7: Búsqueda en Grafos con conjunto de visitados
from collections import deque
def bfs_en_grafo(grafo, inicio, objetivo):
    visitados = set()  # Nodos visitados para evitar ciclos
    cola = deque([[inicio]])  # Cola de caminos a explorar

    while cola:
        camino = cola.popleft()
        nodo = camino[-1]

        if nodo == objetivo:
            return camino  # Retornamos el camino si llegamos al objetivo

        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo.get(nodo, []):  # Vecinos del nodo actual
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)  # Agregamos nuevo camino a la cola
                

    return None  # Si no se encuentra camino

grafo_simple = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


print("\nBúsqueda en Grafos - Camino:", bfs_en_grafo(grafo_simple, 'A', 'F'))