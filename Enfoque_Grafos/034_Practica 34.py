# TEMA: Propagación de Restricciones (AC-3)
# OBJETIVO: Hacer que todos los dominios de variables sean consistentes respecto a sus restricciones

from collections import deque  # Usamos deque para implementar la cola de arcos

# Variables y dominios iniciales
variables = ['A', 'B', 'C']
dominios = {
    'A': [1, 2, 3],
    'B': [1, 2],
    'C': [2, 3]
}

# Restricciones binarias (vecinos no pueden tener el mismo valor)
adyacencias = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}

# Función que revisa si hay valores válidos en el dominio de xi dados los de xj
def revisar(xi, xj):
    eliminado = False
    for x in dominios[xi][:]:
        # Si no hay ningún valor en xj que cumpla la restricción, eliminamos x
        if not any(x != y for y in dominios[xj]):
            dominios[xi].remove(x)
            eliminado = True
    return eliminado

# Algoritmo AC-3
def ac3():
    # Creamos una cola de arcos (pares de variables)
    cola = deque([(xi, xj) for xi in variables for xj in adyacencias[xi]])
    
    while cola:
        xi, xj = cola.popleft()  # Sacamos el primer arco
        if revisar(xi, xj):
            # Si eliminamos algún valor, debemos volver a revisar con los vecinos de xi (menos xj)
            for xk in adyacencias[xi]:
                if xk != xj:
                    cola.append((xk, xi))
    return dominios

# Ejecutar el algoritmo
resultado = ac3()
print("Dominios tras propagación de restricciones (AC-3):", resultado)
