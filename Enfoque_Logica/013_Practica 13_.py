# Tema: Resolución y Forma Normal Conjuntiva (FNC)
# Convertimos proposiciones a FNC y aplicamos resolución básica

# Proposiciones en FNC: (A ∨ B) ∧ (¬B ∨ C)
clausulas = [["A", "B"], ["¬B", "C"]]

# Simulamos resolución entre (A ∨ B) y (¬B ∨ C) eliminando B
resolvente = []

for literal in clausulas[0]:
    if "¬" + literal in clausulas[1] or (literal[1:] if literal.startswith("¬") else "¬" + literal) in clausulas[1]:
        # Agregamos los otros literales que no son complemento
        for l in clausulas[0] + clausulas[1]:
            if l != literal and l != ("¬" + literal if not literal.startswith("¬") else literal[1:]):
                if l not in resolvente:
                    resolvente.append(l)

# Mostramos el resultado
print("Resolvente:", resolvente)
