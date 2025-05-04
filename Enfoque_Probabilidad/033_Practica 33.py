# Tema: ADALINE (neurona adaptativa lineal)
# Objetivo: Entrenar un modelo ADALINE simple para compuerta lógica AND

# Datos de entrenamiento
datos = [([0, 0], 0),
         ([0, 1], 0),
         ([1, 0], 0),
         ([1, 1], 1)]

# Pesos iniciales
pesos = [0.0, 0.0]
bias = 0.0
tasa_aprendizaje = 0.1

# Entrenamiento por 15 épocas
for epoca in range(15):
    for entrada, salida_deseada in datos:
        # Salida lineal sin función de activación
        salida = sum(x * w for x, w in zip(entrada, pesos)) + bias
        # Error entre salida esperada y obtenida
        error = salida_deseada - salida
        # Ajustamos pesos y bias con la regla delta
        pesos = [w + tasa_aprendizaje * error * x for w, x in zip(pesos, entrada)]
        bias += tasa_aprendizaje * error

# Mostramos pesos y bias finales
print("Pesos finales:", pesos)
print("Bias final:", bias)
