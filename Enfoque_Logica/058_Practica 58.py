# Implementación simple para FOIL
import numpy as np

# Datos de ejemplo (2 características, 4 muestras)
X_train = np.array([[0, 1], [1, 0], [1, 1], [0, 0]])
y_train = np.array([1, -1, 1, -1])  # Etiquetas de clase

# Implementar una regla FOIL básica (si X[0] == 1, entonces predice 1)
def foil_rule(X):
    if X[0] == 1:
        return 1
    else:
        return -1

# Clasificar las muestras usando FOIL
predictions = [foil_rule(x) for x in X_train]

# Mostrar predicciones y precisión
print("Predicciones FOIL:", predictions)
print("Valores reales:", y_train)

# Calcular la precisión
accuracy = np.mean(np.array(predictions) == y_train)
print(f"Precisión FOIL: {accuracy:.2f}")
