# Tema: Percepción - Gráficos por Computador
# Este código simula una imagen en escala de grises como matriz de píxeles

# Creamos una imagen de 8x8 píxeles con un patrón de cuadrado en el centro
imagen = []

# Recorremos las filas
for i in range(8):
    fila = []
    for j in range(8):
        # Si estamos dentro del área del cuadrado central, ponemos blanco (255)
        if 2 <= i <= 5 and 2 <= j <= 5:
            fila.append(255)
        else:
            # Si no, gris oscuro
            fila.append(50)
    imagen.append(fila)

# Mostramos la "imagen"
print("Imagen simulada en escala de grises:")
for fila in imagen:
    print(fila)
