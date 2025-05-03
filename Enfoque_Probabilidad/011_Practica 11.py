# TEMA: Inferencia por Enumeración
# OBJETIVO: Calcular P(Lluvia | Césped mojado) usando enumeración

# Definimos las probabilidades como antes
P_lluvia = 0.2
P_sprinkler_given_lluvia = {True: 0.01, False: 0.4}
P_cesped_given_lluvia_sprinkler = {
    (True, True): 0.99,
    (True, False): 0.8,
    (False, True): 0.9,
    (False, False): 0.0
}

# Enumeración para obtener P(Lluvia | Césped mojado)
def enumerar_lluvia_dado_cesped():
    numerador = 0.0
    denominador = 0.0
    for lluvia in [True, False]:
        p_lluvia = P_lluvia if lluvia else 1 - P_lluvia
        for sprinkler in [True, False]:
            p_sprinkler = P_sprinkler_given_lluvia[lluvia] if sprinkler else 1 - P_sprinkler_given_lluvia[lluvia]
            p_cesped = P_cesped_given_lluvia_sprinkler[(lluvia, sprinkler)]
            prob = p_lluvia * p_sprinkler * p_cesped
            if lluvia:
                numerador += prob
            denominador += prob
    return numerador / denominador

# Ejecutar
print("P(Lluvia | Césped mojado):", enumerar_lluvia_dado_cesped())
