# TEMA: Aprendizaje Profundo
# OBJETIVO: Simulación de una neurona con activación

# Entrada
x = 1.0

# Peso y sesgo (bias)
w = 0.5
b = 0.1

# Activación lineal + función de activación sigmoide
z = w * x + b
y = 1 / (1 + 2.71828**(-z))  # Sigmoid

print(f"Salida de la neurona: {y:.2f}")
