# Tema: Aprendizaje Basado en el Conocimiento
# Se infiere una regla a partir de ejemplos positivos

# Ejemplos positivos de frutas rojas
ejemplos = ["manzana", "cereza", "fresa"]

# Supongamos que queremos aprender una regla general
def es_fruta_roja(fruta):
    return fruta in ejemplos

# Se prueba con un nuevo ejemplo
print("¿La manzana es fruta roja?:", es_fruta_roja("manzana"))
print("¿La pera es fruta roja?:", es_fruta_roja("pera"))
