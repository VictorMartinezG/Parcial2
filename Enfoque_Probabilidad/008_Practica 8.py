# TEMA: Red Bayesiana
# OBJETIVO: Representar una red bayesiana simple con probabilidades condicionales

# Definimos las probabilidades
P_lluvia = 0.2                    # Probabilidad de que llueva
P_sprinkler_given_lluvia = {     # Probabilidad de que el aspersor se active dado si llueve
    True: 0.01,
    False: 0.4
}
P_cesped_given_lluvia_sprinkler = {  # Probabilidad de que el césped esté mojado dado lluvia y aspersor
    (True, True): 0.99,
    (True, False): 0.8,
    (False, True): 0.9,
    (False, False): 0.0
}

# Calculamos la probabilidad total de que el césped esté mojado (por enumeración de todos los casos)
def prob_cesped_mojado():
    total = 0.0
    for lluvia in [True, False]:
        p_lluvia = P_lluvia if lluvia else 1 - P_lluvia
        for sprinkler in [True, False]:
            p_sprinkler = P_sprinkler_given_lluvia[lluvia] if sprinkler else 1 - P_sprinkler_given_lluvia[lluvia]
            p_cesped = P_cesped_given_lluvia_sprinkler[(lluvia, sprinkler)]
            total += p_lluvia * p_sprinkler * p_cesped
    return total

# Ejecutar
print("P(Césped mojado):", prob_cesped_mojado())
