# TEMA: Reconocimiento del Habla
# OBJETIVO: Simular el reconocimiento de palabras basadas en fonemas observados

# Frases posibles
frases = {
    "hola": ["h", "o", "l", "a"],
    "ola": ["o", "l", "a"],
    "halo": ["h", "a", "l", "o"]
}

# Fonemas observados (ruidosos)
observados = ["h", "o", "l", "a"]

# Función de coincidencia: cuenta fonemas coincidentes
def coincidencia(palabra, observados):
    esperados = frases[palabra]
    puntos = sum(1 for e, o in zip(esperados, observados) if e == o)
    return puntos / len(esperados)

# Evaluamos cada palabra
mejor = None
puntaje_max = -1
for palabra in frases:
    score = coincidencia(palabra, observados)
    print(f"{palabra}: {score:.2f}")
    if score > puntaje_max:
        puntaje_max = score
        mejor = palabra

# Resultado final
print(f"\nPalabra reconocida: {mejor}")
