# Grafos de Planificación: GRAPHPLAN

# GRAPHPLAN es un algoritmo que utiliza un grafo de planificación para representar
# las acciones y sus dependencias, ayudando a determinar una secuencia de acciones
# que llevará a un estado objetivo.

# Función para crear un grafo de planificación simple
def graphplan(acciones, estado_inicial, estado_objetivo):
    """Genera un plan utilizando GRAPHPLAN con búsqueda en grafos."""
    grafo = {'acciones': [], 'precondiciones': {}, 'efectos': {}}
    
    # Preparar el grafo con acciones
    for accion, precondiciones in acciones:
        grafo['acciones'].append(accion)
        grafo['precondiciones'][accion] = precondiciones
        grafo['efectos'][accion] = [accion]  # Por simplicidad, los efectos son la acción misma
    
    # Simula la ejecución de las acciones
    plan = []
    estado = estado_inicial.copy()
    for accion in grafo['acciones']:
        if all(estado[pre] == True for pre in grafo['precondiciones'][accion]):
            plan.append(accion)
            estado[accion] = True  # Ejecuta la acción
            if all(estado[clave] == estado_objetivo[clave] for clave in estado_objetivo):
                break
    return plan

estado_inicial = {'A': False, 'B': False, 'C': False}
estado_objetivo = {'A': True, 'C': True}
acciones = [('A', ['B']), ('B', [])]
print("Plan de GRAPHPLAN:", graphplan(acciones, estado_inicial, estado_objetivo))
