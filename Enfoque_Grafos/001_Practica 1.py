# Práctica 1: Busqueda de anchura
from collections import deque  # Importamos deque para usar una cola eficiente (FIFO)

def bfs(grafo, inicio, objetivo):
    visitados = set()  # Conjunto para registrar los nodos que ya fueron visitados
    cola = deque([[inicio]])  # Cola de caminos posibles, comenzando con el nodo inicial

    while cola:  # Mientras haya caminos por explorar
        camino = cola.popleft()  # Sacamos el primer camino de la cola
        nodo = camino[-1]  # Obtenemos el último nodo del camino actual

        if nodo in visitados:  # Si ya fue visitado, lo ignoramos
            continue

        if nodo == objetivo:  # Si encontramos el objetivo, retornamos el camino
            return camino

        visitados.add(nodo)  # Marcamos el nodo como visitado

        for vecino in grafo.get(nodo, []):  # Iteramos sobre los vecinos del nodo actual
            nuevo_camino = list(camino)  # Copiamos el camino actual
            nuevo_camino.append(vecino)  # Añadimos el vecino al nuevo camino
            cola.append(nuevo_camino)  # Agregamos el nuevo camino a la cola

    return None  # Si no se encuentra el objetivo, se retorna None

# Definimos un grafo como un diccionario
# Las claves son los nodos y los valores son listas de nodos vecinos

# Ejemplo de grafo simple
# A está conectado con B y C, B con D y E, C con F, etc.
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Ejecutamos la búsqueda desde A hasta F
print("Camino encontrado:", bfs(grafo, 'A', 'F'))
