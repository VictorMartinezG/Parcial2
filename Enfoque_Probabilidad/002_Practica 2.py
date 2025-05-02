# TEMA: Red Bayesiana — Nodo A influye en B, usamos probabilidad condicional

# P(A): Probabilidad de que haya incendio
P_A = 0.01

# P(B|A): Sonó alarma si hay incendio
P_B_dado_A = 0.9

# P(B|¬A): Sonó alarma sin incendio
P_B_dado_noA = 0.1

# P(B): Teorema de la probabilidad total
P_B = P_A * P_B_dado_A + (1 - P_A) * P_B_dado_noA

# P(A|B): Teorema de Bayes
P_A_dado_B = (P_A * P_B_dado_A) / P_B

print("Probabilidad de incendio dado que sonó la alarma:", P_A_dado_B)
