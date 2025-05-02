# TEMA: Problemas de Satisfacción de Restricciones — Coloreo de mapa

# Variables: regiones del mapa
variables = ['A', 'B', 'C', 'D']

# Dominios: colores disponibles
dominios = {
    'A': ['rojo', 'verde'],
    'B': ['rojo', 'verde'],
    'C': ['rojo', 'verde'],
    'D': ['rojo', 'verde']
}

# Restricciones: adyacencia (no pueden tener el mismo color)
adyacencias = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Verifica si una asignación es válida
def es_valida(variable, valor, asignacion):
    for vecino in adyacencias[variable]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False  # Conflicto: mismo color con vecino
    return True
