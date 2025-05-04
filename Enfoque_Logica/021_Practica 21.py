# Tema: Encadenamiento hacia adelante y atrás en lógica de primer orden

# Base de reglas: si humano(x) → mortal(x)
humanos = ["Sócrates"]

# Hacia adelante: si x es humano, entonces x es mortal
mortales = []
for x in humanos:
    mortales.append(x)

print("Hacia adelante - mortales:", mortales)

# Hacia atrás: queremos probar mortal(Sócrates), preguntamos si es humano
consulta = "Sócrates"
if consulta in humanos:
    print("Hacia atrás - Sí, es mortal porque es humano.")
else:
    print("Hacia atrás - No se puede probar.")
