# TEMA: Reconocimiento del Habla — Usamos un modelo oculto de Markov (HMM)

import random

# Estados ocultos (letras o fonemas)
estados = ['S', 'E']

# Observaciones posibles
observaciones = ['sss', 'ee']

# Probabilidades de transición entre estados
transicion = {
    'S': {'S': 0.7, 'E': 0.3},
    'E': {'S': 0.4, 'E': 0.6}
}

# Probabilidades de emisión (sonido que se oye desde cada estado)
emision = {
    'S': {'sss': 0.8, 'ee': 0.2},
    'E': {'sss': 0.1, 'ee': 0.9}
}

# Secuencia observada
secuencia = ['sss', 'ee', 'sss']

# Algoritmo de Viterbi (versión simplificada para ejemplo)
probabilidad = {'S': 1.0, 'E': 0.0}
for obs in secuencia:
    nueva = {}
    for estado in estados:
        max_prob = max(probabilidad[ant] * transicion[ant][estado] * emision[estado][obs] for ant in estados)
        nueva[estado] = max_prob
    probabilidad = nueva

print("Probabilidad de secuencia observada:", max(probabilidad.values()))
