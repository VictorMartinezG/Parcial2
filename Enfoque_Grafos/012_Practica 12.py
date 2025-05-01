# Grafo con ciclos
grafo = {
    'A': ['B', 'C'],  # A se conecta a B y C
    'B': ['A', 'D'],  # B se conecta a A y D
    'C': ['A', 'E'],  # C se conecta a A y E
    'D': ['B'],       # D se conecta a B
    'E': ['C']        # E se conecta a C
}

# Heurísticas
heuristica = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 1,
    'E': 2
}

# Función de búsqueda tabú
def tabu_search(grafo, inicio, max_iter=5):
    actual = inicio  # Empezamos en el nodo inicial
    mejor = actual  # Guardamos el mejor nodo encontrado
    lista_tabu = set()  # Lista tabú (nodos que no queremos repetir)

    for _ in range(max_iter):  # Número máximo de iteraciones
        vecinos = [n for n in grafo[actual] if n not in lista_tabu]  # Vecinos no tabú
        if not vecinos:  # Si no hay vecinos válidos, detenemos
            break

        siguiente = min(vecinos, key=lambda x: heuristica[x])  # Escogemos el mejor vecino
        lista_tabu.add(actual)  # Marcamos actual como tabú
        actual = siguiente  # Avanzamos

        print(f"Actual: {actual}")  # Mostramos progreso

        if heuristica[actual] < heuristica[mejor]:  # Si es mejor que el mejor actual
            mejor = actual  # Lo actualizamos

    print(f"Mejor solución encontrada: {mejor}")  # Mostramos resultado

tabu_search(grafo, 'A')  # Ejecutamos
