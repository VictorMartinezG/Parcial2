# TEMA: Agrupamiento No Supervisado
# OBJETIVO: Agrupar datos similares sin saber clases

datos = [1.0, 1.2, 0.8, 3.0, 3.2, 2.9]

# Inicialización de centroides
c1, c2 = 1.0, 3.0

# Asignar cada dato al centroide más cercano
grupo1 = []
grupo2 = []

for d in datos:
    if abs(d - c1) < abs(d - c2):
        grupo1.append(d)
    else:
        grupo2.append(d)

print(f"Grupo 1: {grupo1}")
print(f"Grupo 2: {grupo2}")
