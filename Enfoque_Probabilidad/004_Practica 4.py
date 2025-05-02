# TEMA: Deep Learning — Red neuronal simple para clasificación con probabilidad

import numpy as np

# Datos de entrada (XOR)
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])  # Etiquetas

# Inicializamos pesos aleatorios
W1 = np.random.randn(2, 2)
b1 = np.zeros((1, 2))
W2 = np.random.randn(2, 1)
b2 = np.zeros((1, 1))

# Funciones de activación
def sigmoid(x): return 1 / (1 + np.exp(-x))
def sigmoid_deriv(x): return x * (1 - x)

# Entrenamiento con retropropagación
for _ in range(1000):
    z1 = X.dot(W1) + b1
    a1 = sigmoid(z1)
    z2 = a1.dot(W2) + b2
    a2 = sigmoid(z2)

    error = y - a2
    d2 = error * sigmoid_deriv(a2)
    d1 = d2.dot(W2.T) * sigmoid_deriv(a1)

    W2 += a1.T.dot(d2)
    b2 += np.sum(d2, axis=0, keepdims=True)
    W1 += X.T.dot(d1)
    b1 += np.sum(d1, axis=0)

print("Predicción final:", a2.round())
