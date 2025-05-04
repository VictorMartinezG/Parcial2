# TEMA: Filtrado, Predicción, Suavizado y Explicación
# OBJETIVO: Simular el proceso básico en un modelo oculto con evidencia parcial

# Estados ocultos y observaciones
estados = ["Sano", "Enfermo"]
observaciones = ["Normal", "Fiebre"]

# Probabilidad de transición entre estados ocultos
P_trans = {
    "Sano": {"Sano": 0.7, "Enfermo": 0.3},
    "Enfermo": {"Sano": 0.4, "Enfermo": 0.6}
}

# Probabilidad de observaciones dadas los estados
P_obs = {
    "Sano": {"Normal": 0.9, "Fiebre": 0.1},
    "Enfermo": {"Normal": 0.3, "Fiebre": 0.7}
}

# Evidencia observada
evidencia = ["Normal", "Fiebre", "Fiebre"]

# Inicialización de creencias (uniforme)
belief = {"Sano": 0.5, "Enfermo": 0.5}

# Función para filtrar (actualizar creencias)
def filtrado(evidencia):
    global belief
    for obs in evidencia:
        nueva = {}
        for estado in estados:
            # Predicción a partir del estado anterior
            pred = sum(belief[prev] * P_trans[prev][estado] for prev in estados)
            # Actualización con observación
            nueva[estado] = pred * P_obs[estado][obs]
        # Normalizar
        total = sum(nueva.values())
        belief = {k: v / total for k, v in nueva.items()}
    return belief

# Aplicamos el filtrado con la evidencia
resultado = filtrado(evidencia)

print("Probabilidades filtradas (último estado dado la evidencia):")
print(resultado)
