# TEMA: k-NN y k-Medias
# OBJETIVO: Clasificar con k-NN y agrupar con k-medias

# Datos con clases
datos = [(1.0, 'A'), (1.2, 'A'), (3.0, 'B'), (3.2, 'B')]
nuevo = 1.1

# k-NN con k=1
distancias = [(abs(d[0] - nuevo), d[1]) for d in datos]
distancias.sort()
print(f"k-NN clasifica como: {distancias[0][1]}")

# k-medias con 2 centroides
grupo1, grupo2 = [], []
c1, c2 = 1.0, 3.0

for d, _ in datos:
    if abs(d - c1) < abs(d - c2):
        grupo1.append(d)
    else:
        grupo2.append(d)

print(f"k-Medias grupos: {grupo1} y {grupo2}")
