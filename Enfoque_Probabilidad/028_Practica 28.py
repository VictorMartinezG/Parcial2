# TEMA: SVM (Núcleo lineal simplificado)
# OBJETIVO: Clasificar con una frontera lineal entre dos clases

# Datos (x, clase)
datos = [(-1, -1), (-2, -1), (1, 1), (2, 1)]

# Clasificación de un nuevo punto
nuevo = 0.5

# Frontera lineal: x = 0 separa ambas clases
if nuevo >= 0:
    print("Clase: +1")
else:
    print("Clase: -1")
