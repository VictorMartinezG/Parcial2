# Redes Jerárquicas de Tareas

# Este enfoque permite organizar las tareas de planificación en una jerarquía,
# donde las tareas más generales se desglosan en tareas más específicas.

# Representación de tareas jerárquicas
tareas = [
    ('Tarea General', ['Subtarea 1', 'Subtarea 2']),
    ('Subtarea 1', []),
    ('Subtarea 2', [])
]

# Planificación jerárquica
def planificacion_jerarquica(tareas):
    """Genera un plan jerárquico desde una estructura de tareas."""
    plan = []
    for tarea, subtareas in tareas:
        plan.append(tarea)
        for subtarea in subtareas:
            plan.append(subtarea)
    return plan

print("Plan jerárquico:", planificacion_jerarquica(tareas))
