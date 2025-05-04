# Tema: Inferencia Lógica Proposicional
# Usamos Modus Ponens: Si A ⇒ B y A es verdadero, entonces B también

# Asumimos que 'A implica B' y que 'A' es verdadero
A = True
B = None  # Aún no sabemos si B es verdadero

# Aplicamos inferencia usando Modus Ponens
if A:
    B = True

# Mostramos el resultado de la inferencia
print("Si A es verdadero y A implica B, entonces B es:", B)
