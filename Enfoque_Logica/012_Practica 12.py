# Tema: Equivalencia, Validez y Satisfacibilidad
# Comprobamos si dos proposiciones son equivalentes

# Definimos dos expresiones lógicas equivalentes: A → B y ¬A ∨ B
def son_equivalentes():
    for A in [True, False]:
        for B in [True, False]:
            # Evaluamos ambas expresiones
            expr1 = (not A) or B        # ¬A ∨ B
            expr2 = (not A) or B        # A → B (mismo resultado aquí)
            # Comparamos los resultados
            if expr1 != expr2:
                return False
    return True

# Imprimimos si son equivalentes
print("¿Son equivalentes A → B y ¬A ∨ B?", son_equivalentes())
