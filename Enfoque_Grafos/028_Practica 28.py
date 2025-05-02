# TEMA: Aprendizaje por Refuerzo Activo — El agente explora y mejora su política con experiencia

import random

# Definimos estados y acciones posibles
estados = ['A', 'B', 'C']
acciones = {'A': ['B'], 'B': ['C'], 'C': ['C']}

# Recompensas directas
recompensas = {'A': 0, 'B': 0, 'C': 10}
descuento = 0.9

# Inicializamos valores y política
V = {s: 0 for s in estados}
politica = {s: random.choice(acciones[s]) for s in estados}

# Iteramos para aprender y mejorar política
for _ in range(10):
    for s in estados:
        mejores_valores = []
        for a in acciones[s]:
            valor = recompensas[a] + descuento * V[a]
            mejores_valores.append((valor, a))
        mejor_valor, mejor_accion = max(mejores_valores)
        V[s] = mejor_valor
        politica[s] = mejor_accion  # Se mejora la política

print("Política aprendida:", politica)
