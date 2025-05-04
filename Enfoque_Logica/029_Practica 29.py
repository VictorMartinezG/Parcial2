# Tema: Lógica por defecto - asumir lo normal hasta que se diga lo contrario

# Base de reglas por defecto
def por_defecto(animal):
    if animal == "pájaro":
        return "vuela por defecto"
    else:
        return "no se sabe"

# Agregamos conocimiento específico
conocimiento = {"pingüino": "no vuela"}

def razonamiento(animal):
    if animal in conocimiento:
        return conocimiento[animal]
    return por_defecto(animal)

print("Pingüino:", razonamiento("pingüino"))
print("Canario:", razonamiento("pájaro"))
