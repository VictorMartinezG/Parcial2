# Grafo AO*: cada nodo se conecta mediante relaciones OR o AND
grafo = {
    'A': [('B', 'OR'), ('C', 'AND')],  # A tiene dos opciones: B (OR), o C con hijos AND
    'B': [],                           # B es un nodo hoja
    'C': ['D', 'E'],                   # C se conecta a D y E (AND implícito)
    'D': [],                           # D es hoja
    'E': []                            # E es hoja
}

# Heurísticas del grafo
heuristica = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0,
    'E': 0
}

# Función recursiva para AO* (simplificada)
def ao_star(nodo):
    print(f"Procesando nodo: {nodo}")  # Mostramos el nodo actual
    if not grafo[nodo]:  # Si es hoja
        print(f"Es hoja: {nodo}")  # Lo indicamos
        return True  # Terminamos

    for hijo in grafo[nodo]:  # Iteramos por los hijos
        if isinstance(hijo, tuple):  # Si es una relación OR
            if ao_star(hijo[0]):  # Si uno cumple
                return True  # Es válido
        else:  # Si son hijos AND (implícito)
            if all(ao_star(h) for h in grafo[nodo]):  # Todos deben cumplirse
                return True  # Retornamos éxito

    return False  # Si no se cumple ninguna condición

ao_star('A')  # Iniciamos la búsqueda
