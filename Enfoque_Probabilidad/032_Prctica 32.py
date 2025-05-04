# Tema: Redes Neuronales - Perceptrón
# Objetivo: Entrenar un perceptrón para aprender la compuerta lógica AND

# Datos de entrada (x1, x2) y salida deseada
datos = [([0, 0], 0),
         ([0, 1], 0),
         ([1, 0], 0),
         ([1, 1], 1)]

pesos = [0.0, 0.0]  # Pesos iniciales
bias = 0.0  # Sesgo
tasa_aprendizaje = 0.1  # Paso de actualización

# Entrenamos por varias épocas
for epoca in range(10):
    for entrada, salida_esperada in datos:
        # Cálculo de la salida actual
        suma = sum(x * w for x, w in zip(entrada, pesos)) + bias
        salida = 1 if suma > 0 else 0

        # Calculamos el error
        error = salida_esperada - salida

        # Actualizamos los pesos y el sesgo
        pesos = [w + tasa_aprendizaje * error * x for w, x in zip(pesos, entrada)]
        bias += tasa_aprendizaje * error

# Mostramos los pesos entrenados
print("Pesos finales:", pesos)
print("Bias final:", bias)
