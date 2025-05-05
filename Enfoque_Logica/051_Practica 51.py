# Implementación simple de un árbol de decisión usando el algoritmo ID3

import math

# Función para calcular la entropía
def calcular_entropia(dataset):
    """Calcula la entropía de un conjunto de datos."""
    total = len(dataset)
    frec = {}
    
    for item in dataset:
        if item not in frec:
            frec[item] = 1
        else:
            frec[item] += 1
    
    entropia = 0
    for key in frec:
        probabilidad = frec[key] / total
        entropia -= probabilidad * math.log2(probabilidad)
    
    return entropia

# Función de ID3
def id3(dataset, atributos):
    """Genera un árbol de decisión utilizando el algoritmo ID3."""
    if len(set([item[-1] for item in dataset])) == 1:
        return dataset[0][-1]  # Clase final si todos los ejemplos tienen la misma clase
    
    if len(atributos) == 0:
        return max(set([item[-1] for item in dataset]), key = [item[-1] for item in dataset].count)
    
    # Calculando la mejor división (atributo con la mayor ganancia de información)
    entropia_total = calcular_entropia([item[-1] for item in dataset])
    mejor_atributo = None
    mejor_ganancia = 0
    mejor_division = None
    
    for atributo in atributos:
        valores = set([item[atributo] for item in dataset])
        division = {}
        
        for valor in valores:
            division[valor] = [item for item in dataset if item[atributo] == valor]
        
        ganancia = entropia_total
        for subgrupo in division.values():
            ganancia -= (len(subgrupo) / len(dataset)) * calcular_entropia([item[-1] for item in subgrupo])
        
        if ganancia > mejor_ganancia:
            mejor_ganancia = ganancia
            mejor_atributo = atributo
            mejor_division = division
    
    # Construir árbol recursivamente
    sub_arboles = {}
    for valor, subgrupo in mejor_division.items():
        sub_arboles[valor] = id3(subgrupo, [atributo for atributo in atributos if atributo != mejor_atributo])
    
    return {mejor_atributo: sub_arboles}

# Ejemplo de uso
dataset = [["rojo", "manzana", "comestible"], ["verde", "pera", "comestible"], ["amarillo", "banana", "comestible"], ["marrón", "tierra", "no comestible"]]
atributos = [0, 1]  # índice de atributos: color, forma
arbol = id3(dataset, atributos)
print("Árbol de decisión:", arbol)
