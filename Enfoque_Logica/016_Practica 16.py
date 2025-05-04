# Tema: Búsqueda Local en lógica
# Búsqueda local para encontrar una asignación que cumpla una fórmula

# Fórmula: A ∧ ¬B
def evaluar(asignacion):
    A, B = asignacion["A"], asignacion["B"]
    return A and not B

# Inicializamos con una asignación aleatoria
asignacion = {"A": False, "B": True}

# Realizamos una búsqueda local sencilla
for _ in range(10):
    if evaluar(asignacion):
        break
    # Alternamos los valores de A y B
    asignacion["A"] = not asignacion["A"]
    asignacion["B"] = not asignacion["B"]

print("Asignación encontrada:", asignacion)
