# Tema: Regla de Hebb
# Objetivo: Aprendizaje simple con regla Hebbiana

# Entradas y salidas
entradas = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
salidas = [1, -1, -1, 1]

# Inicializamos pesos
pesos = [0, 0]

# Regla de Hebb: w_i = w_i + x_i * y
for x, y in zip(entradas, salidas):
    pesos = [w + xi * y for w, xi in zip(pesos, x)]

print("Pesos aprendidos con Hebb:", pesos)
