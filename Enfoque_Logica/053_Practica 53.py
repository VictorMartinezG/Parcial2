# Implementar Boosting básico (AdaBoost)
import numpy as np

# Función para aplicar el clasificador débil (un clasificador simple como un perceptrón)
def weak_classifier(X, weights):
    # Realizamos una predicción simple
    return np.sign(np.dot(X, np.ones(X.shape[1])))  # Supone que todas las características son positivas

# Datos de ejemplo (2 características, 5 muestras)
X_train = np.array([[0, 1], [1, 0], [1, 1], [0, 0], [1, 1]])
y_train = np.array([1, -1, 1, -1, 1])  # Etiquetas de clase

# Ponderaciones iniciales (uniformemente distribuidas)
weights = np.ones(len(X_train)) / len(X_train)

# Boosting básico
for i in range(5):  # Número de iteraciones
    predictions = weak_classifier(X_train, weights)
    error = np.sum(weights * (predictions != y_train)) / np.sum(weights)  # Error ponderado
    
    # Actualización de los pesos
    alpha = 0.5 * np.log((1 - error) / error)
    weights *= np.exp(-alpha * y_train * predictions)

    print(f"Iteración {i + 1}: Error = {error:.2f}")

