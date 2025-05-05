# Algoritmos de Planificación: STRIPS y ADL

# El modelo STRIPS y ADL son representaciones para la planificación automática
# de acciones en inteligencia artificial, donde STRIPS define la forma básica
# de representar los estados y acciones, y ADL agrega mayor expresividad.

# Representación de un estado
estado_inicial = {'A': False, 'B': False, 'C': False}
estado_objetivo = {'A': True, 'C': True}

# Acción en STRIPS
def accion(strips_action, estado):
    """Simula la acción dentro del modelo STRIPS, cambiando el estado."""
    precondiciones, efectos = strips_action
    if all(estado[pre] == True for pre in precondiciones):
        for efecto in efectos:
            estado[efecto] = True
    return estado

# Acción ejemplo: 'A' se hace verdadera si 'B' es verdadera
strips_action = (['B'], ['A'])

# Aplicar acción
estado_actual = estado_inicial.copy()
estado_actual = accion(strips_action, estado_actual)
print(f"Estado después de aplicar la acción: {estado_actual}")

# Verificar si el estado cumple con el objetivo
def verifica_objetivo(estado, objetivo):
    """Verifica si el estado alcanzado cumple con el objetivo."""
    return all(estado[clave] == objetivo[clave] for clave in objetivo)

print("¿Estado objetivo alcanzado?", verifica_objetivo(estado_actual, estado_objetivo))
