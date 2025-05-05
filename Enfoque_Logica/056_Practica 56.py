# Generar reglas simples y mostrar la precisión
import numpy as np

# Datos de ejemplo (2 características, 4 muestras)
X_train = np.array([[0, 1], [1, 0], [1, 1], [0, 0]])
y_train = np.array([1, -1, 1, -1])  # Etiquetas de clase

# Regla 1: Si la primera característica es 1, predice 1
# Regla 2: Si la segunda característica es 1, predice -1
def rule1(X):
    return 1 if X[0] == 1 else -1

def rule2(X):
    return -1 if X[1] == 1 else 1

# Evaluar reglas
pred1 = [rule1(x) for x in X_train]
pred2 = [rule2(x) for x in X_train]

# Calcular precisión de las reglas
def accuracy(predictions, y):
    return np.mean(predictions == y)

acc1 = accuracy(pred1, y_train)
acc2 = accuracy(pred2, y_train)

print(f"Precisión de Regla 1: {acc1:.2f}")
print(f"Precisión de Regla 2: {acc2:.2f}")
