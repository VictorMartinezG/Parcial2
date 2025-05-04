# Tema: Percepción - Movimiento
# Detecta movimiento entre dos imágenes comparando diferencias

# Imagen en t = 0
imagen_1 = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

# Imagen en t = 1 (el objeto se movió a la derecha)
imagen_2 = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 0, 0]
]

# Contamos los píxeles que cambiaron
cambios = 0
for i in range(3):
    for j in range(3):
        if imagen_1[i][j] != imagen_2[i][j]:
            cambios += 1

print("Cantidad de píxeles que cambiaron (movimiento):", cambios)
