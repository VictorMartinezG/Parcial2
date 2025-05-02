# TEMA: Q-Learning — Aprende valores Q sin conocer el modelo del entorno

import random

# Estados y acciones posibles
estados = ['A', 'B', 'C']
acciones = {'A': ['B'], 'B': ['C'], 'C': ['C']}

# Recompensas por acción
recompensas = {'A': 0, 'B': 0, 'C': 10}

# Inicializamos Q-valores
Q = {(s, a): 0 for s in estados for a in acciones[s]}

alpha = 0.5       # Tasa de aprendizaje
gamma = 0.9       # Factor de descuento

# Simulación de episodios
for episodio in range(20):
    estado = 'A'
    while estado != 'C':
        accion = random.choice(acciones[estado])  # Política exploratoria aleatoria
        siguiente = accion
        recompensa = recompensas[siguiente]
        max_q = max([Q[siguiente, a2] for a2 in acciones[siguiente]])
        Q[estado, accion] += alpha * (recompensa + gamma * max_q - Q[estado, accion])
        estado = siguiente

# Se elige la mejor acción para cada estado
politica = {s: max(acciones[s], key=lambda a: Q[s, a]) for s in estados}
print("Política óptima aprendida:", politica)
