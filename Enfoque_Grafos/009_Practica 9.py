import heapq  # Importamos heapq para manejar una cola de prioridad

# Grafo representado con vecinos y el costo de ir a ellos
grafo = {
    'A': [('B', 1), ('C', 4)],  # A se conecta a B (costo 1) y a C (costo 4)
    'B': [('D', 5), ('E', 2)],  # B se conecta a D y E
    'C': [('F', 3)],            # C se conecta a F
    'D': [],                    # D no tiene vecinos
    'E': [('G', 1)],            # E se conecta a G
    'F': [],                    # F no tiene vecinos
    'G': []                     # G no tiene vecinos
}

# Heurística estimada desde cada nodo al objetivo
heuristica = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 1,
    'F': 0,
    'G': 0
}

# Implementación de A*
def busqueda_a_estrella(grafo, inicio, objetivo):
    cola = []  # Inicializamos la cola de prioridad
    heapq.heappush(cola, (heuristica[inicio], 0, inicio))  # Insertamos el nodo inicial (f(n), g(n), nodo)
    visitados = set()  # Para evitar ciclos

    while cola:  # Mientras haya elementos por explorar
        fn, costo, actual = heapq.heappop(cola)  # Sacamos el nodo con menor f(n)
        print(f"Visitando: {actual} con costo acumulado: {costo}")  # Mostramos nodo actual

        if actual == objetivo:  # Si llegamos al objetivo
            print("Objetivo alcanzado.")  # Lo indicamos
            return True  # Éxito

        if actual not in visitados:  # Si no ha sido visitado
            visitados.add(actual)  # Lo marcamos como visitado

            for vecino, costo_arista in grafo.get(actual, []):  # Recorremos sus vecinos
                if vecino not in visitados:  # Si no ha sido visitado
                    nuevo_costo = costo + costo_arista  # Calculamos nuevo g(n)
                    fn = nuevo_costo + heuristica[vecino]  # Calculamos f(n)
                    heapq.heappush(cola, (fn, nuevo_costo, vecino))  # Lo agregamos a la cola

    print("Objetivo no encontrado.")  # Si salimos del bucle sin encontrarlo
    return False  # Fallo

busqueda_a_estrella(grafo, 'A', 'G')  # Llamamos a la función
