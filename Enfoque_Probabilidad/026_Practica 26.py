# TEMA: Modelos Ocultos de Markov (HMM)
# OBJETIVO: Calcular probabilidad de una secuencia de observaciones

# Estados ocultos
estados = ["S", "R"]  # Soleado, Lluvioso

# Matriz de transición
trans = {
    "S": {"S": 0.8, "R": 0.2},
    "R": {"S": 0.4, "R": 0.6}
}

# Matriz de observación
obs = {
    "S": {"paseo": 0.9, "ver_tv": 0.1},
    "R": {"paseo": 0.2, "ver_tv": 0.8}
}

# Secuencia observada
observaciones = ["paseo", "ver_tv", "paseo"]

# Suposición: comenzamos en "S"
prob = 1.0
estado_actual = "S"

for o in observaciones:
    prob *= obs[estado_actual][o]  # Prob. observación
    estado_actual = max(trans[estado_actual], key=trans[estado_actual].get)  # Transición más probable

print(f"Probabilidad aproximada de la secuencia: {prob:.4f}")
