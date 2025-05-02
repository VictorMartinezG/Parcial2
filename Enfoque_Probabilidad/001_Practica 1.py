# TEMA: Incertidumbre y Probabilidad — Cálculo simple de probabilidades condicionadas

# Definimos probabilidades básicas
P_lluvia = 0.3              # Probabilidad de que llueva
P_sin_paraguas_dado_lluvia = 0.1  # Probabilidad de no llevar paraguas si llueve

# Usamos regla de la probabilidad conjunta
P_lluvia_y_sin_paraguas = P_lluvia * P_sin_paraguas_dado_lluvia

print("Probabilidad de que llueva y no lleves paraguas:", P_lluvia_y_sin_paraguas)
