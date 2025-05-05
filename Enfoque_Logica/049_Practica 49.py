# Planificación Continua y Multiagente

# En este tipo de planificación, múltiples agentes trabajan de manera
# conjunta para lograr un objetivo común.

# Simulación de planificación multiagente
def planificacion_multiagente(agentes, tareas):
    """Simula la planificación continua en un entorno multiagente."""
    planes = {}
    for agente in agentes:
        planes[agente] = [tarea for tarea in tareas if tarea not in planes.values()]
    return planes

agentes = ['Agente 1', 'Agente 2']
tareas = ['Tarea A', 'Tarea B', 'Tarea C']
print("Planes de agentes:", planificacion_multiagente(agentes, tareas))
