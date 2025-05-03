# TEMA: Regla de la Cadena
# OBJETIVO: Descomponer una probabilidad conjunta en factores condicionales

# Variables: A → B → C (una cadena causal)
P_A = 0.3  # Probabilidad de A
P_B_given_A = {True: 0.8, False: 0.1}  # P(B|A)
P_C_given_B = {True: 0.7, False: 0.2}  # P(C|B)

# Calculamos P(A, B, C) usando la regla de la cadena
def probabilidad_total():
    total = 0
    for A in [True, False]:
        pA = P_A if A else 1 - P_A
        for B in [True, False]:
            pB = P_B_given_A[A] if B else 1 - P_B_given_A[A]
            for C in [True, False]:
                pC = P_C_given_B[B] if C else 1 - P_C_given_B[B]
                total += pA * pB * pC  # P(A) * P(B|A) * P(C|B)
    return total

# Ejecutar
print("Probabilidad total conjunta P(A,B,C):", probabilidad_total())
