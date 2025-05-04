# Tema: Aprendizaje Probabilístico - Algoritmo EM
# Objetivo: Usar EM para encontrar dos medias (mu1, mu2) en una mezcla de dos distribuciones normales

import random  # Importamos la librería random para generar datos simulados

# Generamos datos con dos distribuciones gaussianas simuladas (una alrededor de 5 y otra de 15)
datos = [random.gauss(5, 1) for _ in range(10)] + [random.gauss(15, 1) for _ in range(10)]

# Inicializamos las medias arbitrariamente
mu1, mu2 = 4.0, 16.0

# Número de iteraciones para ajustar los parámetros
iteraciones = 10

# Definimos un pequeño valor para evitar divisiones por cero
epsilon = 1e-6

# Bucle principal del algoritmo EM
for _ in range(iteraciones):
    responsabilidades = []  # Lista para almacenar qué tan probable es que cada dato pertenezca a cada grupo

    # Paso E: Calcular las responsabilidades
    for d in datos:
        # Calculamos la "responsabilidad" (inversa de la distancia + epsilon para evitar división por cero)
        r1 = 1 / (abs(d - mu1) + epsilon)
        r2 = 1 / (abs(d - mu2) + epsilon)
        total = r1 + r2
        responsabilidades.append((r1 / total, r2 / total))  # Normalizamos para que sumen 1

    # Paso M: Actualizamos las medias según las responsabilidades
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

# Imprimimos los resultados finales de las medias estimadas
print("Media estimada para grupo 1:", round(mu1, 2))
print("Media estimada para grupo 2:", round(mu2, 2))
