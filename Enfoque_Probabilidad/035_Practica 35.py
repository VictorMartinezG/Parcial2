# Tema: Red Multicapa
# Objetivo: Resolver XOR con una red de 2 capas

import math

# Función sigmoide
def sigmoide(x):
    return 1 / (1 + math.exp(-x))

# Derivada de sigmoide
def derivada_sigmoide(x):
    return x * (1 - x)

# Datos de entrada y salida deseada
datos = [([0, 0], 0),
         ([0, 1], 1),
         ([1, 0], 1),
         ([1, 1], 0)]

# Pesos y bias iniciales (hardcodeados para 2 entradas, 2 ocultas y 1 salida)
w_ih = [[0.5, -0.6], [0.4, 0.3]]  # pesos entrada a oculta
b_h = [0.0, 0.0]
w_ho = [0.7, -0.5]  # pesos oculta a salida
b_o = 0.0
lr = 0.5  # tasa de aprendizaje

for epoca in range(10000):
    for entrada, salida_deseada in datos:
        # Capa oculta
        h_in = [sum(i * w for i, w in zip(entrada, col)) + b for col, b in zip(zip(*w_ih), b_h)]
        h_out = [sigmoide(x) for x in h_in]

        # Capa de salida
        salida_in = sum(h * w for h, w in zip(h_out, w_ho)) + b_o
        salida = sigmoide(salida_in)

        # Error de salida
        error = salida_deseada - salida
        d_salida = error * derivada_sigmoide(salida)

        # Retropropagación a capa oculta
        d_h = [d_salida * w * derivada_sigmoide(h) for w, h in zip(w_ho, h_out)]

        # Actualizar pesos salida
        w_ho = [w + lr * d_salida * h for w, h in zip(w_ho, h_out)]
        b_o += lr * d_salida

        # Actualizar pesos entrada a oculta
        for i in range(len(w_ih)):
            for j in range(len(w_ih[0])):
                w_ih[i][j] += lr * d_h[j] * entrada[i]
        b_h = [b + lr * d for b, d in zip(b_h, d_h)]

# Probamos la red
print("Red entrenada para XOR:")
for entrada, _ in datos:
    h_in = [sum(i * w for i, w in zip(entrada, col)) + b for col, b in zip(zip(*w_ih), b_h)]
    h_out = [sigmoide(x) for x in h_in]
    salida_in = sum(h * w for h, w in zip(h_out, w_ho)) + b_o
    salida = sigmoide(salida_in)
    print(f"{entrada} => {round(salida)}")
