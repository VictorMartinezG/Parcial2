# Planificación Lógica Proposicional: SATPLAN

# SATPLAN es un enfoque que utiliza la lógica proposicional y técnicas de
# satisfacibilidad booleana (SAT) para resolver problemas de planificación.

# Representación del problema
estado_inicial = {'A': False, 'B': False}
estado_objetivo = {'A': True}
acciones = [('A', ['B']), ('B', [])]

# Implementación de SATPLAN
def satplan(acciones, estado_inicial, estado_objetivo):
    """Usa SATPLAN para resolver el problema de planificación."""
    plan = []
    estado = estado_inicial.copy()
    for accion, precondiciones in acciones:
        if all(estado[pre] == True for pre in precondiciones):
            plan.append(accion)
            estado[accion] = True
    return plan if all(estado[clave] == estado_objetivo[clave] for clave in estado_objetivo) else None

print("Plan de SATPLAN:", satplan(acciones, estado_inicial, estado_objetivo))
