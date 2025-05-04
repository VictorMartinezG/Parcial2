# Tema: Mapas Autoorganizados de Kohonen
# Objetivo: Simulación simplificada con 1D de dos neuronas

# Datos simples de entrada
datos = [[0.2], [0.8], [0.4], [0.9]]

# Pesos de dos neuronas
pesos = [0.3, 0.7]
tasa_aprendizaje = 0.1

# Entrenamiento simple
for epoca in range(5):
    for entrada in datos:
        # Calculamos distancia de cada neurona
        distancias = [abs(p - entrada[0]) for p in pesos]
        ganadora = distancias.index(min(distancias))  # neurona ganadora

        # Ajustamos solo la neurona ganadora
        pesos[ganadora] += tasa_aprendizaje * (entrada[0] - pesos[ganadora])

print("Pesos entrenados de neuronas Kohonen:", pesos)
