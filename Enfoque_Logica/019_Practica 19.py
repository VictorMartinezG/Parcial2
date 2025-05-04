# Tema: Ingeniería del conocimiento
# Simulamos una base de conocimientos con predicados y hechos

# Conocimiento estructurado en reglas
conocimiento = {
    "mamífero": lambda x: x in ["perro", "gato"],
    "vuela": lambda x: x == "pájaro"
}

# Consultamos el conocimiento
def consultar(predicado, sujeto):
    if predicado in conocimiento:
        return conocimiento[predicado](sujeto)
    return False

# Ejemplos de consultas
print("¿Es perro un mamífero?", consultar("mamífero", "perro"))
print("¿Vuela el gato?", consultar("vuela", "gato"))
