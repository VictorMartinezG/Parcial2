# Tema: Percepción - Detección de Aristas y Segmentación
# Detecta aristas en una matriz de imagen usando diferencias de intensidad

# Imagen simulada 5x5 con bordes en el centro
imagen = [
    [10, 10, 10, 10, 10],
    [10, 255, 255, 255, 10],
    [10, 255, 10, 255, 10],
    [10, 255, 255, 255, 10],
    [10, 10, 10, 10, 10]
]

# Matriz de salida para los bordes
bordes = [[0 for _ in range(5)] for _ in range(5)]

# Recorremos los píxeles del centro
for i in range(1, 4):
    for j in range(1, 4):
        centro = imagen[i][j]
        vecinos = imagen[i-1][j] + imagen[i+1][j] + imagen[i][j-1] + imagen[i][j+1]
        promedio_vecinos = vecinos / 4
        # Si la diferencia es alta, hay borde
        bordes[i][j] = 255 if abs(centro - promedio_vecinos) > 100 else 0

# Mostramos el resultado
print("Resultado de detección de aristas:")
for fila in bordes:
    print(fila)
