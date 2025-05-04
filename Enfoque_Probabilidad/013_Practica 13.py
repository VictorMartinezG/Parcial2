# TEMA: Muestreo Directo
# OBJETIVO: Estimar P(Lluvia | Césped mojado) usando muestreo directo

import random

# Definimos las probabilidades necesarias
P_lluvia = 0.2  # Probabilidad de que llueva

# P(Sprinkler | Lluvia)
P_sprinkler_given_lluvia = {
    True: 0.01,
    False: 0.4
}

# P(Césped mojado | Lluvia, Sprinkler)
P_cesped_given_lluvia_sprinkler = {
    (True, True): 0.99,
    (True, False): 0.8,
    (False, True): 0.9,
    (False, False): 0.0
}

# Función de muestreo directo
def muestreo_directo(n=10000):
    cuenta_lluvia_y_cesped = 0  # Contador de muestras donde hay lluvia y césped mojado
    cuenta_cesped = 0           # Contador de todas las veces que hay césped mojado

    for _ in range(n):
        # Generamos si llueve o no
        lluvia = random.random() < P_lluvia

        # Generamos si el aspersor se activa o no
        sprinkler = random.random() < P_sprinkler_given_lluvia[lluvia]

        # Obtenemos probabilidad de césped mojado dado lluvia y aspersor
        p_cesped = P_cesped_given_lluvia_sprinkler[(lluvia, sprinkler)]

        # Determinamos si el césped está mojado o no
        cesped = random.random() < p_cesped

        # Si el césped está mojado, actualizamos contadores
        if cesped:
            cuenta_cesped += 1
            if lluvia:
                cuenta_lluvia_y_cesped += 1

    # Estimamos P(Lluvia | Césped mojado) como la fracción de veces que hubo lluvia dado que el césped está mojado
    if cuenta_cesped == 0:
        return 0  # Evita división por cero
    return cuenta_lluvia_y_cesped / cuenta_cesped

# Ejecutamos el muestreo y mostramos el resultado
print("P(Lluvia | Césped mojado) por muestreo:", muestreo_directo())
