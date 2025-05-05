# Implementación simplificada de un árbol de regresión (M5) para ilustración

import numpy as np

# Función para calcular el error cuadrático medio (MSE)
def calcular_mse(dataset):
    """Calcula el error cuadrático medio de un conjunto de datos."""
    valores = [item[-1] for item in dataset]
    media = np.mean(valores)
    mse = np.mean((valores - media) ** 2)
    return mse

# Función de árbol de regresión (M5)
def m5_regression(dataset, atributos):
    """Construcción de un árbol de regresión M5 (simplificado)."""
    if len(set([item[-1] for item in dataset])) == 1:
        return np.mean([item[-1] for item in dataset])  # Media si todos los valores son iguales
    
    if len(atributos) == 0:
        return np.mean([item[-1] for item in dataset])
    
    mejor_atributo = None
    mejor_mse = float("inf")
    mejor_division = None
    
    for atributo in atributos:
        valores = set([item[atributo] for item in dataset])
        division = {}
        
        for valor in valores:
            division[valor] = [item for item in dataset if item[atributo] == valor]
        
        mse = 0
        for subgrupo in division.values():
            mse += len(subgrupo) * calcular_mse(subgrupo)
        
        mse /= len(dataset)
        
        if mse < mejor_mse:
            mejor_mse = mse
            mejor_atributo = atributo
            mejor_division = division
    
    sub_arboles = {}
    for valor, subgrupo in mejor_division.items():
        sub_arboles[valor] = m5_regression(subgrupo, [atributo for atributo in atributos if atributo != mejor_atributo])
    
    return {mejor_atributo: sub_arboles}

# Ejemplo de uso
dataset = [[1, 2, 3], [2, 3, 5], [3, 4, 6], [4, 5, 8]]
atributos = [0, 1]  # atributos: las primeras dos columnas
arbol = m5_regression(dataset, atributos)
print("Árbol de regresión:", arbol)
