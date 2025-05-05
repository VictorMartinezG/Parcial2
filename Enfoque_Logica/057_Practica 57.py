# Implementación simple para mostrar la importancia de características
import numpy as np

# Datos de ejemplo (2 características, 4 muestras)
X_train = np.array([[0, 1], [1, 0], [1, 1], [0, 0]])
y_train = np.array([1, -1, 1, -1])  # Etiquetas de clase

# Modelo simple: sumar las características
def simple_model(X):
    return np.sum(X)

# Clasificar las muestras
predictions = [simple_model(x) for x in X_train]

# Mostrar las predicciones y las diferencias
print("Predicciones:", predictions)
print("Valores reales:", y_train)

# Calcular la "importancia" (en este caso, la diferencia en las predicciones)
importances = np.abs(np.array(predictions) - y_train)
print("Importancia de características (diferencia):", importances)
