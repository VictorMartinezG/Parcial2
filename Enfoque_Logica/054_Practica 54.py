# Implementar un árbol de decisión simple
import numpy as np

# Datos de ejemplo (2 características, 4 muestras)
X_train = np.array([[0, 1], [1, 0], [1, 1], [0, 0]])
y_train = np.array([1, -1, 1, -1])  # Etiquetas de clase

# Árbol de decisión simple
def decision_tree(X):
    if X[0] == 0:
        return -1
    else:
        return 1

# Clasificar los datos de prueba
for x in X_train:
    print(f"Entrada: {x}, Predicción: {decision_tree(x)}")
