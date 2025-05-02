# TEMA: Búsqueda de Vuelta Atrás — Resolución por retroceso en CSP
# OBJETIVO: Asignar colores a regiones sin que dos regiones vecinas tengan el mismo color

# Lista de variables: regiones del mapa
variables = ['A', 'B', 'C', 'D']

# Dominios: colores posibles para cada región
dominios = {
    'A': ['rojo', 'verde'],
    'B': ['rojo', 'verde'],
    'C': ['rojo', 'verde'],
    'D': ['rojo', 'verde']
}

# Restricciones: regiones adyacentes no pueden tener el mismo color
adyacencias = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Función para verificar si una asignación es válida
def es_valida(variable, valor, asignacion):
    for vecino in adyacencias[variable]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False  # Hay un conflicto con un vecino
    return True  # La asignación es válida

# Función principal de búsqueda de vuelta atrás (backtracking)
def backtrack(asignacion):
    # Si todas las variables están asignadas, retornamos la solución
    if len(asignacion) == len(variables):
        return asignacion
    
    # Elegimos la siguiente variable no asignada
    var = next(v for v in variables if v not in asignacion)
    
    # Probamos cada valor posible del dominio de la variable
    for valor in dominios[var]:
        if es_valida(var, valor, asignacion):
            asignacion[var] = valor  # Asignamos el valor
            resultado = backtrack(asignacion)  # Llamada recursiva
            if resultado:
                return resultado  # Si se encuentra solución, se retorna
            del asignacion[var]  # Retroceso (deshacer asignación)
    
    return None  # No se encontró solución válida para esta rama

# Ejecutamos la búsqueda desde una asignación vacía
print("Solución por vuelta atrás:", backtrack({}))
