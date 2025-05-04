# TEMA: Aprendizaje por Refuerzo Pasivo — El agente observa y evalúa una política fija

# Estados y política fija (decisión en cada estado)
estados = ['A', 'B', 'C']
politica = {'A': 'B', 'B': 'C', 'C': 'C'}

# Recompensas por estado
recompensas = {'A': 0, 'B': 0, 'C': 10}
descuento = 0.9

# Inicializamos valores
V = {s: 0 for s in estados}

# Iteramos para evaluar política
for _ in range(10):
    for s in estados:
        a = politica[s]        # Acción definida por la política
        V[s] = recompensas[a] + descuento * V[a]  # Fórmula de Bellman con política fija

print("Valor de estados según política:", V)
