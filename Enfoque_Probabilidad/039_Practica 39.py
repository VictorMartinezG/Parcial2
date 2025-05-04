# Tema: Modelo Probabilístico del Lenguaje
# Este código construye un modelo unigram y calcula la probabilidad de una oración

# Texto base (corpus)
corpus = "el gato duerme el perro ladra el gato maulla el perro duerme"

# Separar en palabras
palabras = corpus.split()

# Contar ocurrencias
frecuencias = {}
total = 0
for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    total += 1  # Contar total de palabras

# Función para calcular la probabilidad de una oración
def probabilidad_oracion(oracion):
    oracion_palabras = oracion.split()
    prob = 1.0
    for p in oracion_palabras:
        prob *= frecuencias.get(p, 0) / total if p in frecuencias else 0
    return prob

# Ejemplo
oracion = "el gato duerme"
print("Probabilidad de la oración:", probabilidad_oracion(oracion))
