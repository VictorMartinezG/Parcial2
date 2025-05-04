# Tema: Representación del Conocimiento
# Se simula una base de conocimiento simple con hechos y reglas

# Base de hechos representada como diccionario
hechos = {
    "gato_tiene_bigotes": True,
    "gato_es_mamifero": True,
    "gato_tiene_alas": False
}

# Regla: Si un animal tiene bigotes y es mamífero, entonces es un gato
def es_gato():
    return hechos["gato_tiene_bigotes"] and hechos["gato_es_mamifero"]

# Evaluación de la regla
print("¿Es un gato según los hechos?:", es_gato())

