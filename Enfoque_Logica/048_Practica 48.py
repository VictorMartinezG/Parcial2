# Vigilancia de Ejecución y Replanificación

# Este enfoque se utiliza para monitorear la ejecución del plan y replanificar
# si se detectan cambios en el entorno que puedan afectar el éxito del plan.

# Simulación de monitoreo y replanificación
def vigilancia_replanificacion(estado_inicial, estado_objetivo, plan):
    """Monitorea la ejecución del plan y realiza replanificación si es necesario."""
    estado = estado_inicial.copy()  # Hacer una copia para no modificar el original
    for accion in plan:
        if estado != estado_objetivo:
            # Replanificación si el estado no es el objetivo
            print("Replanificando...")
            return False
        estado[accion] = True
    return True

# Definir estado_inicial y estado_objetivo
estado_inicial = {'A': False, 'B': False}
estado_objetivo = {'A': True, 'B': True}  # Ajuste aquí según lo que necesites

# Ejecutar el código
print("Plan ejecutado exitosamente:", vigilancia_replanificacion(estado_inicial, estado_objetivo, ["A"]))
