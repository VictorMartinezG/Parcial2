# Tema: Percepción - Reconocimiento de Objetos
# Detecta un patrón de objeto cuadrado en una imagen simulada

# Imagen 5x5 con un cuadrado en el centro
imagen = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Revisamos si hay un patrón de 3x3 lleno de 1s en el centro
objeto_detectado = True
for i in range(1, 4):
    for j in range(1, 4):
        if imagen[i][j] != 1:
            objeto_detectado = False

print("¿Objeto cuadrado detectado?:", objeto_detectado)
