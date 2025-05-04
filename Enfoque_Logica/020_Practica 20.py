# Tema: Unificación
# Comparamos términos y buscamos una sustitución que los haga iguales

# Unificamos padre(X, juan) con padre(pedro, Y)

def unificar(t1, t2):
    if t1[0] != t2[0] or len(t1[1]) != len(t2[1]):
        return None
    sustituciones = {}
    for a, b in zip(t1[1], t2[1]):
        if a != b:
            if a.islower():  # es variable
                sustituciones[a] = b
            elif b.islower():
                sustituciones[b] = a
            else:
                return None
    return sustituciones

# Estructura (función, [argumentos])
t1 = ("padre", ["X", "juan"])
t2 = ("padre", ["pedro", "Y"])

print("Unificación:", unificar(t1, t2))
