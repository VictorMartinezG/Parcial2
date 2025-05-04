# TEMA: Procesos de Markov (Hipótesis de Markov)
# OBJETIVO: Simular un proceso de Markov simple donde el siguiente estado depende solo del actual

import random

# Estados posibles
estados = ["A", "B", "C"]

# Matriz de transición que depende solo del estado actual (hipótesis de Markov)
transiciones = {
    "A": {"A": 0.2, "B": 0.6, "C": 0.2},
    "B": {"A": 0.1, "B": 0.4, "C": 0.5},
    "C": {"A": 0.7, "B": 0.2, "C": 0.1}
}

# Elegir un nuevo estado dado el actual
def siguiente_estado(estado_actual):
    r = random.random()
    acumulado = 0
    for estado, prob in transiciones[estado_actual].items():
        acumulado += prob
        if r <= acumulado:
            return estado
    return estado_actual  # fallback

# Ejecutar el proceso de Markov
estado = "A"
trayectoria = [estado]

for _ in range(20):
    estado = siguiente_estado(estado)
    trayectoria.append(estado)

print("Trayectoria de estados (Proceso de Markov):")
print(trayectoria)
