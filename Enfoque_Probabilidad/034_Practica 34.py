# Tema: Separabilidad Lineal
# Objetivo: Probar si los datos de XOR son linealmente separables (no lo son)

# Datos XOR: no linealmente separables
datos = [([0, 0], 0),
         ([0, 1], 1),
         ([1, 0], 1),
         ([1, 1], 0)]

# Intento de entrenamiento con perceptrón
pesos = [0.0, 0.0]
bias = 0.0
tasa_aprendizaje = 0.1

for epoca in range(20):
    error_total = 0
    for entrada, salida_esperada in datos:
        suma = sum(x * w for x, w in zip(entrada, pesos)) + bias
        salida = 1 if suma > 0 else 0
        error = salida_esperada - salida
        error_total += abs(error)
        pesos = [w + tasa_aprendizaje * error * x for w, x in zip(pesos, entrada)]
        bias += tasa_aprendizaje * error
    if error_total == 0:
        break

# Resultado esperado: no aprenderá correctamente
print("Pesos:", pesos)
print("Bias:", bias)
print("Error total:", error_total)
