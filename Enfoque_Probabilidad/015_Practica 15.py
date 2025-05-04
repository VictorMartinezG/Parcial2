# TEMA: Monte Carlo para Cadenas de Markov
# OBJETIVO: Estimar la distribución estacionaria de una cadena de Markov usando simulación

import random

# Definimos los estados posibles de la cadena
estados = ["Soleado", "Nublado", "Lluvioso"]

# Definimos la matriz de transición de estado
# Cada estado tiene una distribución de probabilidad condicional hacia los siguientes estados
transiciones = {
    "Soleado": {"Soleado": 0.6, "Nublado": 0.3, "Lluvioso": 0.1},
    "Nublado": {"Soleado": 0.2, "Nublado": 0.4, "Lluvioso": 0.4},
    "Lluvioso": {"Soleado": 0.1, "Nublado": 0.3, "Lluvioso": 0.6}
}

# Número de simulaciones para la técnica Monte Carlo
num_simulaciones = 10000

# Estado inicial (puede ser cualquiera, pero elegimos Soleado)
estado_actual = "Soleado"

# Diccionario para contar cuántas veces se visita cada estado
conteo_estados = {estado: 0 for estado in estados}

# Función para elegir el siguiente estado basado en la distribución de probabilidad
def elegir_estado(distribucion):
    r = random.random()
    acumulado = 0
    for estado, prob in distribucion.items():
        acumulado += prob
        if r <= acumulado:
            return estado
    return estado  # en caso de error de redondeo

# Simulación de la cadena de Markov usando Monte Carlo
for _ in range(num_simulaciones):
    # Elegimos el siguiente estado según las probabilidades de transición
    estado_actual = elegir_estado(transiciones[estado_actual])
    # Contamos la visita al estado
    conteo_estados[estado_actual] += 1

# Calculamos la distribución estimada dividiendo por el total de simulaciones
distribucion_estimada = {estado: conteo / num_simulaciones for estado, conteo in conteo_estados.items()}

# Mostramos el resultado
print("Distribución estacionaria estimada (Monte Carlo):")
for estado, prob in distribucion_estimada.items():
    print(f"{estado}: {prob:.4f}")
