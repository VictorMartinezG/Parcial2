import heapq  # Importamos la librería heapq para manejar colas de prioridad (min-heaps)

# Definimos el grafo como un diccionario donde cada nodo tiene una lista de vecinos
grafo = {
    'A': ['B', 'C'],  # A se conecta con B y C
    'B': ['D', 'E'],  # B se conecta con D y E
    'C': ['F'],       # C se conecta con F
    'D': [],          # D no tiene vecinos
    'E': ['G'],       # E se conecta con G
    'F': [],          # F no tiene vecinos
    'G': []           # G no tiene vecinos
}

# Diccionario de heurísticas (valor estimado desde cada nodo al objetivo)
heuristica = {
    'A': 7,  # Heurística del nodo A
    'B': 6,  # Heurística del nodo B
    'C': 2,  # Heurística del nodo C
    'D': 1,  # Heurística del nodo D
    'E': 1,  # Heurística del nodo E
    'F': 0,  # Heurística del nodo F
    'G': 0   # Heurística del nodo G
}

# Función que implementa la búsqueda voraz primero el mejor
def busqueda_voraz(grafo, inicio, objetivo):
    visitados = set()  # Creamos un conjunto para almacenar nodos ya visitados
    cola_prioridad = []  # Inicializamos una cola de prioridad (heap)

    # Insertamos el nodo inicial junto con su heurística
    heapq.heappush(cola_prioridad, (heuristica[inicio], inicio))

    # Mientras haya nodos en la cola de prioridad
    while cola_prioridad:
        _, nodo_actual = heapq.heappop(cola_prioridad)  # Sacamos el nodo con menor heurística

        print(f"Visitando: {nodo_actual}")  # Mostramos el nodo actual que estamos visitando

        if nodo_actual == objetivo:  # Si llegamos al objetivo
            print("Objetivo alcanzado.")  # Imprimimos mensaje de éxito
            return True  # Terminamos la búsqueda con éxito

        if nodo_actual not in visitados:  # Si el nodo no ha sido visitado antes
            visitados.add(nodo_actual)  # Lo agregamos a la lista de visitados

            # Recorremos cada vecino del nodo actual
            for vecino in grafo[nodo_actual]:
                if vecino not in visitados:  # Si el vecino no ha sido visitado
                    # Insertamos el vecino en la cola con su heurística
                    heapq.heappush(cola_prioridad, (heuristica[vecino], vecino))

    # Si salimos del bucle sin encontrar el objetivo
    print("Objetivo no encontrado.")  # Imprimimos mensaje de fallo
    return False  # Indicamos que no se encontró el objetivo

# Llamamos a la función para iniciar la búsqueda desde 'A' hasta 'G'
busqueda_voraz(grafo, 'A', 'G')
