# Tema: Tratamiento Lógico del Lenguaje
# Se interpreta una oración como lógica proposicional

# Diccionario de proposiciones asociadas a oraciones
oraciones = {
    "Juan come": True,
    "Pedro duerme": False
}

# Función que traduce y evalúa la oración
def interpretar(oracion):
    return oraciones.get(oracion, "Oración desconocida")

# Se evalúa una oración
print("¿'Juan come' es verdadera?:", interpretar("Juan come"))
print("¿'Pedro duerme' es verdadera?:", interpretar("Pedro duerme"))
