# Tema: Redes Neuronales - Computación Neuronal
# Objetivo: Simular una neurona artificial con suma ponderada y activación binaria

# Entradas simuladas a una neurona
entradas = [1, 0, 1]  # Valores de entrada binarios
pesos = [0.5, -0.6, 0.3]  # Pesos asignados a cada entrada
umbral = 0.0  # Umbral de activación

# Calculamos la suma ponderada (producto punto)
suma_ponderada = sum(x * w for x, w in zip(entradas, pesos))

# Aplicamos función de activación binaria (step)
salida = 1 if suma_ponderada > umbral else 0

# Mostramos el resultado de la neurona
print("Salida de la neurona:", salida)
