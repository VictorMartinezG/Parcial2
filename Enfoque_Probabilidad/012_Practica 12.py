# TEMA: Eliminación de Variables
# OBJETIVO: Eliminar la variable "sprinkler" para calcular P(Césped | Lluvia)

# Definimos las probabilidades necesarias
P_sprinkler_given_lluvia = {     # P(Sprinkler | Lluvia)
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

# Vamos a eliminar la variable "sprinkler"
# Calculamos P(Césped mojado | Lluvia) sumando sobre sprinkler
P_cesped_dado_lluvia = {}  # Diccionario para guardar los resultados

# Iteramos sobre los posibles valores de lluvia
for lluvia in [True, False]:
    total = 0
    # Sumamos sobre sprinkler (eliminamos esa variable)
    for sprinkler in [True, False]:
        # P(Sprinkler | Lluvia)
        p_sprinkler = P_sprinkler_given_lluvia[lluvia] if sprinkler else 1 - P_sprinkler_given_lluvia[lluvia]
        # P(Césped mojado | Lluvia, Sprinkler)
        p_cesped = P_cesped_given_lluvia_sprinkler[(lluvia, sprinkler)]
        # Multiplicamos y sumamos
        total += p_sprinkler * p_cesped
    # Guardamos el resultado
    P_cesped_dado_lluvia[lluvia] = total

# Mostrar los resultados
print("P(Césped mojado | Lluvia):", P_cesped_dado_lluvia)
