# Espacio de Estados

# Un espacio de estados es una representación de todos los estados posibles
# que se pueden alcanzar desde un estado inicial hasta un estado objetivo.

# Representación de estados simples
estado_inicial = (0, 0)  # coordenada en el plano XY
estado_objetivo = (2, 2)

# Función para generar sucesores
def sucesores(estado):
    """Genera los posibles sucesores de un estado dado."""
    x, y = estado
    return [(x+1, y), (x, y+1)]  # movimientos posibles en el eje X o Y

# Buscar camino en el espacio de estados
def busca_camino(estado_inicial, estado_objetivo):
    """Busca un camino en el espacio de estados usando búsqueda por amplitud."""
    frontera = [estado_inicial]
    visitados = set()
    while frontera:
        estado = frontera.pop(0)
        if estado == estado_objetivo:
            return True  # Se alcanzó el objetivo
        for sucesor in sucesores(estado):
            if sucesor not in visitados:
                frontera.append(sucesor)
                visitados.add(sucesor)
    return False

print("¿Camino encontrado?", busca_camino(estado_inicial, estado_objetivo))
