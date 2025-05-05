# Tema: Ingeniería del Conocimiento - Ontologías
# Este código simula una ontología simple usando diccionarios y relaciones jerárquicas

# Definimos una estructura de ontología como un diccionario con relaciones
ontologia = {
    "animal": [],
    "mamifero": ["animal"],  # mamífero es un tipo de animal
    "perro": ["mamifero"],   # perro es un tipo de mamífero
    "gato": ["mamifero"],
    "ave": ["animal"]
}

# Función recursiva para verificar si una clase pertenece a otra
def es_subclase(de, a):
    # Si ambas clases son iguales, es subclase
    if de == a:
        return True
    # Si la clase no tiene padres, termina
    if de not in ontologia:
        return False
    # Busca recursivamente en los padres
    for padre in ontologia[de]:
        if es_subclase(padre, a):
            return True
    return False

# Ejemplo de uso
print("¿Perro es un animal?", es_subclase("perro", "animal"))  # True
print("¿Ave es un mamífero?", es_subclase("ave", "mamifero"))  # False
