# Tema: Redes Neuronales - Funciones de Activación
# Objetivo: Comparar salidas usando distintas funciones de activación

import math  # Usamos funciones matemáticas estándar

x = 1.0  # Entrada de ejemplo

# Función sigmoide
sigmoide = 1 / (1 + math.exp(-x))

# Función tangente hiperbólica
tanh = math.tanh(x)

# Función ReLU (Rectified Linear Unit)
relu = max(0, x)

# Imprimimos cada salida
print("Sigmoide:", round(sigmoide, 4))
print("Tanh:", round(tanh, 4))
print("ReLU:", relu)
