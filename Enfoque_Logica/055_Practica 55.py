# Seleccionar la mejor hipótesis basada en la precisión
import numpy as np

# Datos de ejemplo (5 muestras, 2 características)
X_train = np.array([[0, 1], [1, 0], [1, 1], [0, 0], [1, 1]])
y_train = np.array([1, -1, 1, -1, 1])  # Etiquetas de clase

# Definimos dos modelos (funciones sencillas)
def model1(X):
    return np.sign(np.sum(X))

def model2(X):
    return np.sign(np.prod(X))

# Función para calcular precisión
def accuracy(predictions, y):
    return np.mean(predictions == y)

# Evaluar los modelos
acc1 = accuracy([model1(x) for x in X_train], y_train)
acc2 = accuracy([model2(x) for x in X_train], y_train)

# Seleccionar el modelo con mejor precisión
if acc1 > acc2:
    print(f"Mejor modelo: Modelo 1 con precisión {acc1:.2f}")
else:
    print(f"Mejor modelo: Modelo 2 con precisión {acc2:.2f}")
