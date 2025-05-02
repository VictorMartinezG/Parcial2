# TEMA: Búsqueda de la Política — Ajusta directamente la política para maximizar recompensa

import random

# Estados y acciones
estados = ['A', 'B', 'C']
acciones = {'A': ['B'], 'B': ['C'], 'C': ['C']}
recompensas = {'A': 0, 'B': 0, 'C': 10}

# Política inicial aleatoria
politica = {s: random.choice(acciones[s]) for s in estados}

# Función de evaluación de política
def evaluar(politica):
    estado = 'A'
    total = 0
    factor = 1
    while estado != 'C':
        accion = politica[estado]
        total += factor * recompensas[accion]
        estado = accion
        factor *= 0.9
    return total

# Búsqueda simple por mejora aleatoria
for _ in range(10):
    nueva_politica = {s: random.choice(acciones[s]) for s in estados}
    if evaluar(nueva_politica) > evaluar(politica):
        politica = nueva_politica  # Se acepta si mejora

print("Política encontrada por búsqueda:", politica)
