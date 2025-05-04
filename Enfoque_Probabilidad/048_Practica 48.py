# Tema: Percepción - Texturas y Sombras
# Simula la detección de textura midiendo la cantidad de cambios de intensidad

# Imagen simulada con regiones lisas y texturizadas
imagen = [
    [50, 50, 50, 200, 50],
    [50, 50, 50, 200, 50],
    [50, 50, 50, 200, 50],
    [50, 50, 50, 200, 50],
    [50, 50, 50, 200, 50]
]

# Contador de cambios bruscos (indicador de textura)
cambios = 0

# Comparamos cada píxel con su vecino derecho
for fila in imagen:
    for i in range(len(fila) - 1):
        if abs(fila[i] - fila[i+1]) > 100:
            cambios += 1

print("Cantidad de cambios de intensidad (textura):", cambios)
