# Tema: Cuantificadores ∀ (para todo) y ∃ (existe)
# Evaluamos una fórmula ∀x (P(x)) y ∃x (Q(x)) para un dominio

# Dominio de elementos
dominio = [1, 2, 3, 4, 5]

# Predicados
def P(x):
    return x > 0

def Q(x):
    return x == 3

# Verificamos ∀x P(x)
todos_cumplen = all(P(x) for x in dominio)
print("¿∀x P(x)?", todos_cumplen)

# Verificamos ∃x Q(x)
existe_algun = any(Q(x) for x in dominio)
print("¿∃x Q(x)?", existe_algun)
