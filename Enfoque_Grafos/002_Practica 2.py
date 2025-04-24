# Práctica 2: Búsqueda de Costo Uniforme (Uniform Cost Search)
import heapq  # Usamos heapq para crear una cola de prioridad (min-heap)

def costo_uniforme(grafo, inicio, objetivo):
    cola = [(0, [inicio])]  # Cola de prioridad que guarda tuplas de (costo acumulado, camino)
    visitados = set()  # Conjunto para guardar nodos visitados y evitar ciclos

    while cola:
        costo, camino = heapq.heappop(cola)  # Extraemos el camino con menor costo total
        nodo = camino[-1]  # El último nodo del camino actual

        if nodo in visitados:
            continue  # Si ya fue visitado, se ignora

        if nodo == objetivo:
            return camino, costo  # Si es el objetivo, devolvemos el camino y el costo

        visitados.add(nodo)  # Marcamos el nodo como visitado

        for vecino, costo_extra in grafo.get(nodo, []):  # Iteramos sobre vecinos y su costo
            nuevo_camino = list(camino)  # Copiamos el camino actual
            nuevo_camino.append(vecino)  # Añadimos el vecino al nuevo camino
            heapq.heappush(cola, (costo + costo_extra, nuevo_camino))  # Insertamos con el nuevo costo

    return None, float('inf')  # Si no se encuentra camino, devolvemos infinito

# Grafo con costos (ponderado)
grafo_ponderado = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 7), ('E', 1)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Ejecutamos la búsqueda desde A hasta F
camino, costo = costo_uniforme(grafo_ponderado, 'A', 'F')
print("Camino encontrado:", camino)
print("Costo total:", costo)