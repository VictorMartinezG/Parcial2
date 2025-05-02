# TEMA: Redes Neuronales — Perceptrón simple

# Entradas y salidas para AND
entradas = [[0,0], [0,1], [1,0], [1,1]]
salidas = [0, 0, 0, 1]

# Pesos y sesgo iniciales
pesos = [0, 0]
sesgo = 0
tasa = 0.1

# Entrenamiento del perceptrón
for _ in range(10):
    for i, x in enumerate(entradas):
        suma = x[0]*pesos[0] + x[1]*pesos[1] + sesgo
        salida = 1 if suma > 0 else 0
        error = salidas[i] - salida
        pesos[0] += tasa * error * x[0]
        pesos[1] += tasa * error * x[1]
        sesgo += tasa * error

print("Pesos finales:", pesos, "Sesgo:", sesgo)
