# TEMA: Procesos Estacionarios
# OBJETIVO: Simular un proceso estacionario donde la media y varianza son constantes en el tiempo
# No usa bibliotecas externas, solo impresión de resumen estadístico

import random
import statistics  # Para calcular media y desviación estándar

# Genera una serie de valores aleatorios con media y desviación constantes
def generar_proceso_estacionario(n=100):
    media = 0
    desviacion = 1
    return [random.gauss(media, desviacion) for _ in range(n)]

# Generar el proceso
proceso = generar_proceso_estacionario(100)

# Mostrar un resumen en consola
print("Primeros 10 valores del proceso estacionario:")
print(proceso[:10])  # Mostrar solo los primeros valores

# Calcular media y desviación estándar de la serie completa
media_observada = statistics.mean(proceso)
desviacion_observada = statistics.stdev(proceso)

print("\nMedia observada:", round(media_observada, 4))
print("Desviación estándar observada:", round(desviacion_observada, 4))

# Mostrar si cumple con ser aproximadamente estacionario
if abs(media_observada) < 0.5 and abs(desviacion_observada - 1) < 0.5:
    print("\nComportamiento estacionario aproximado verificado.")
else:
    print("\nAdvertencia: posibles desviaciones del comportamiento estacionario.")

