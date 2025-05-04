# Tema: Extracción de Información
# Extrae nombres de animales y acciones en frases

# Frases base
frases = [
    "el gato duerme",
    "el perro ladra",
    "la gata maulla"
]

# Reglas simples para extraer [sujeto, verbo]
def extraer(frase):
    palabras = frase.split()
    if len(palabras) == 3:
        sujeto = palabras[1]
        verbo = palabras[2]
        return (sujeto, verbo)
    return None

# Mostrar información extraída
for frase in frases:
    print("Extracción:", extraer(frase))
