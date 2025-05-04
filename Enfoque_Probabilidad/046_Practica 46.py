# Tema: Percepción - Preprocesado: Filtros
# Aplica un filtro de suavizado simple sobre una matriz (imagen)

# Imagen simulada 3x3 con ruido
imagen = [
    [100, 180, 90],
    [200, 255, 100],
    [90,  160, 80]
]

# Filtro promedio simple (sin usar bordes para simplificar)
promedio = (
    imagen[0][0] + imagen[0][1] + imagen[0][2] +
    imagen[1][0] + imagen[1][1] + imagen[1][2] +
    imagen[2][0] + imagen[2][1] + imagen[2][2]
) // 9  # Promedio de los 9 píxeles

# Mostramos imagen original y resultado
print("Imagen original:")
for fila in imagen:
    print(fila)

print("Resultado del filtro promedio aplicado al centro:", promedio)
