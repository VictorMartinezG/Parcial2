# Tema: Percepción - Etiquetado de Líneas
# Etiqueta regiones conectadas de 1s en una matriz binaria

# Imagen con dos regiones de 1s separadas
imagen = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 0]
]

# Etiquetado simple con número de regiones
etiquetas = [[0 for _ in fila] for fila in imagen]
etiqueta_actual = 1

# Función recursiva para etiquetar
def etiquetar(i, j, valor):
    if 0 <= i < len(imagen) and 0 <= j < len(imagen[0]):
        if imagen[i][j] == 1 and etiquetas[i][j] == 0:
            etiquetas[i][j] = valor
            etiquetar(i+1, j, valor)
            etiquetar(i-1, j, valor)
            etiquetar(i, j+1, valor)
            etiquetar(i, j-1, valor)

# Etiquetamos todas las regiones
for i in range(len(imagen)):
    for j in range(len(imagen[0])):
        if imagen[i][j] == 1 and etiquetas[i][j] == 0:
            etiquetar(i, j, etiqueta_actual)
            etiqueta_actual += 1

# Mostramos el resultado
print("Etiquetas asignadas:")
for fila in etiquetas:
    print(fila)
