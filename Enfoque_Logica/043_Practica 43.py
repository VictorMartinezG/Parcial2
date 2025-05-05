# Planificación de Orden Parcial

# La planificación de orden parcial permite que las acciones puedan ocurrir
# en cualquier orden siempre que sus precondiciones estén satisfechas.

# Representación de acciones
acciones = [
    ('A', ['B']),  # Acción A requiere B
    ('B', []),     # Acción B no tiene precondiciones
]

# Planificación de acciones en orden parcial
def planificacion_parcial(acciones, estado_inicial):
    """Genera un plan parcial basado en las precondiciones."""
    plan = []
    estado = estado_inicial.copy()
    while acciones:
        for accion, precondiciones in acciones:
            if all(estado[pre] == True for pre in precondiciones):
                plan.append(accion)
                estado[accion] = True  # Ejecuta la acción
                acciones = [a for a in acciones if a[0] != accion]  # Elimina acción ya ejecutada
                break
    return plan

estado_inicial = {'A': False, 'B': False}
print(f"Plan de acciones: {planificacion_parcial(acciones, estado_inicial)}")
