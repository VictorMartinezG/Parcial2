# TEMA: Salto Atrás Dirigido por Conflictos
# OBJETIVO: Evitar explorar ramas que sabemos que fallarán, saltando al responsable del conflicto

# Variables y dominios
variables = ['X', 'Y', 'Z']
dominios = {
    'X': [1, 2],
    'Y': [1, 2],
    'Z': [1, 2]
}

# Restricciones binarias: X ≠ Y, Y ≠ Z
restricciones = {
    ('X', 'Y'): lambda x, y: x != y,
    ('Y', 'Z'): lambda y, z: y != z
}

# Función que verifica si una asignación satisface las restricciones
def cumple_restricciones(asignacion, nueva_var):
    for (xi, xj), restriccion in restricciones.items():
        if xi in asignacion and xj in asignacion:
            if not restriccion(asignacion[xi], asignacion[xj]):
                return False, xi  # Retorna la variable que causó el conflicto
    return True, None

# Función principal con backjumping
def backjump(asignacion, nivel):
    if len(asignacion) == len(variables):
        return asignacion
    
    var = variables[nivel]
    for valor in dominios[var]:
        asignacion[var] = valor
        valido, conflicto = cumple_restricciones(asignacion, var)
        if valido:
            resultado = backjump(asignacion, nivel + 1)
            if resultado:
                return resultado
        else:
            if conflicto and variables.index(conflicto) < nivel:
                return None  # Saltamos hacia atrás al responsable
        del asignacion[var]
    return None

# Ejecutar
print("Solución con salto atrás dirigido por conflictos:", backjump({}, 0))
