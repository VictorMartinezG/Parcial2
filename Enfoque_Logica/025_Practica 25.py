# Tema: Lógica de orden superior
# Permite usar funciones como argumentos de otras funciones (funciones de funciones)

# Definimos funciones predicado
def es_par(x):
    return x % 2 == 0

def aplicar_a_lista(f, lista):
    # Aplica una función predicado a una lista
    return [f(x) for x in lista]

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Aplicamos el predicado es_par
resultado = aplicar_a_lista(es_par, numeros)

print("Resultado de lógica de orden superior:", resultado)
