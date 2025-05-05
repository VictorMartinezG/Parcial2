# Planificación Condicional

# La planificación condicional permite que las acciones se ejecuten bajo ciertas condiciones
# que se verifican antes de que se ejecute la acción.

# Ejemplo de planificación condicional
def planificacion_condicional(acciones, estado_inicial):
    """Simula la planificación condicional con acciones basadas en condiciones."""
    plan = []
    estado = estado_inicial.copy()
    for accion, precondiciones, condicion in acciones:
        if all(estado[pre] == True for pre in precondiciones):
            if condicion(estado):
                plan.append(accion)
                estado[accion] = True
    return plan

# Acción con condición
acciones_condicionales = [
    ('Acción A', ['B'], lambda estado: estado['B'] == True)
]

estado_inicial = {'A': False, 'B': True}
print("Plan condicional:", planificacion_condicional(acciones_condicionales, estado_inicial))
