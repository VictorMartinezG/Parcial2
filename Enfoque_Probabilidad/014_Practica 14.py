# TEMA: Ponderación de Verosimilitud (Likelihood Weighting)
# OBJETIVO: Estimar P(Lluvia | Césped mojado = True) ponderando las muestras

import random

# Definimos las probabilidades base
P_lluvia = 0.2  # Probabilidad de lluvia

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

# Función para hacer ponderación de verosimilitud
def ponderacion_verosimilitud(n=10000):
    peso_lluvia_true = 0  # Suma de pesos cuando hay lluvia
    peso_lluvia_false = 0  # Suma de pesos cuando no hay lluvia

    for _ in range(n):
        # Muestra de lluvia
        lluvia = random.random() < P_lluvia

        # Muestra de sprinkler condicional a lluvia
        sprinkler = random.random() < P_sprinkler_given_lluvia[lluvia]

        # Observamos que césped mojado = True, así que tomamos el peso
        peso = P_cesped_given_lluvia_sprinkler[(lluvia, sprinkler)]

        # Acumulamos el peso según si hay lluvia o no
        if lluvia:
            peso_lluvia_true += peso
        else:
            peso_lluvia_false += peso

    # Normalizamos para obtener P(Lluvia | Césped mojado = True)
    total_peso = peso_lluvia_true + peso_lluvia_false
    if total_peso == 0:
        return 0  # Evitar división por cero
    return peso_lluvia_true / total_peso

# Ejecutamos la estimación
print("P(Lluvia | Césped mojado = True) por ponderación:", ponderacion_verosimilitud())
