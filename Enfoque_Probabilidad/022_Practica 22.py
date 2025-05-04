# Tema: Aprendizaje Probabilístico - Algoritmo EM (Expectation-Maximization)
# Objetivo: Agrupar datos en dos distribuciones gaussianas (simplificado, sin librerías externas)

import random  # Usamos random para simular datos

# Generamos una muestra de datos combinando dos distribuciones distintas
datos = [random.gauss(5, 1) for _ in range(10)] + [random.gauss(15, 1) for _ in range(10)]

# Inicializamos los parámetros: medias arbitrarias
mu1, mu2 = 4.0, 16.0

# Número de iteraciones del algoritmo
iteraciones = 10

# Pequeño valor para evitar división por cero
epsilon = 1e-6

# EM: Expectation-Maximization
for _ in range(iteraciones):
    # Paso E: calculamos las responsabilidades (qué tan probable es que un dato pertenezca a cada grupo)
    responsabilidades = []
    for d in datos:
        # Evitamos división por cero sumando epsilon al denominador si es necesario
        r1 = 1 / (abs(d - mu1) + epsilon)
        r2 = 1 / (abs(d - mu2) + epsilon)
        total = r1 + r2
        responsabilidades.append((r1 / total, r2 / total))

    # Paso M: actualizamos las medias usando las responsabilidades calculadas
    suma1, suma2 = 0, 0
    total_r1, total_r2 = 0, 0
    for i, d in enumerate(datos):
        r1, r2 = responsabilidades[i]
        suma1 += r1 * d
        suma2 += r2 * d
        total_r1 += r1
        total_r2 += r2
    mu1 = suma1 / total_r1
    mu2 = suma2 / total_r2

# Mostramos las medias finales
print("Media estimada para grupo 1:", round(mu1, 2))
print("Media estimada para grupo 2:", round(mu2, 2))
