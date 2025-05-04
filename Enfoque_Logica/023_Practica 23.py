# Tema: Skolemización (eliminación de cuantificadores existenciales)
# Ejemplo: ∀x ∃y P(x, y) → P(x, f(x))

# Representamos la fórmula skolemizada
def P(x, y):
    return f"P({x}, {y})"

# Skolemización: ∃y se reemplaza por función f(x)
def skolemizar():
    for x in ["a", "b", "c"]:
        y = f"f({x})"
        print(P(x, y))

# Ejecutamos
skolemizar()
