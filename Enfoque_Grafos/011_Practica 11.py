# Definimos un grafo simple
grafo = {
    'A': ['B', 'C'],  # A se conecta a B y C
    'B': ['D'],       # B se conecta a D
    'C': ['E'],       # C se conecta a E
    'D': [],          # D es hoja
    'E': []           # E es hoja
}

# Heurísticas de cada nodo
heuristica = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 1,
    'E': 2
}

# Función que implementa Hill Climbing
def hill_climbing(grafo, inicio):
    actual = inicio  # Iniciamos desde el nodo inicial

    while True:
        vecinos = grafo[actual]  # Obtenemos vecinos del nodo actual
        if not vecinos:  # Si no hay vecinos, terminamos
            break

        mejor = min(vecinos, key=lambda x: heuristica[x])  # Elegimos vecino con mejor heurística

        if heuristica[mejor] >= heuristica[actual]:  # Si no mejora, nos detenemos
            break

        actual = mejor  # Avanzamos al mejor vecino
        print(f"Moviéndome a: {actual}")  # Mostramos el movimiento

    print(f"Resultado final: {actual}")  # Resultado del algoritmo

hill_climbing(grafo, 'A')  # Llamamos a la función
