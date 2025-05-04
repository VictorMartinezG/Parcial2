# Tema: Sintaxis y Semántica - Tablas de Verdad
# Este código genera la tabla de verdad para una proposición lógica: (A ∧ B) → C

# Importamos itertools para generar combinaciones de valores booleanos
import itertools

# Definimos la función para imprimir la tabla de verdad
def tabla_verdad():
    # Definimos los valores posibles para A, B y C
    valores = [True, False]

    # Encabezado de la tabla
    print("A\tB\tC\t(A ∧ B) → C")

    # Iteramos por todas las combinaciones posibles de A, B y C
    for A, B, C in itertools.product(valores, repeat=3):
        # Evaluamos la proposición (A ∧ B) → C
        resultado = (not (A and B)) or C
        # Imprimimos la fila correspondiente
        print(f"{A}\t{B}\t{C}\t{resultado}")

# Ejecutamos la función
tabla_verdad()
