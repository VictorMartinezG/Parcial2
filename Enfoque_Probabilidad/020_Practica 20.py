# TEMA: Aprendizaje Bayesiano
# OBJETIVO: Clasificar si una fruta es "manzana" o "naranja" basada en su color

# Probabilidades previas
P_manzana = 0.5
P_naranja = 0.5

# Probabilidades condicionales del color
P_rojo_dado_manzana = 0.8
P_rojo_dado_naranja = 0.2

# Observación: la fruta es roja
# Aplicamos Teorema de Bayes para cada clase

# Probabilidad de ser manzana dado que es roja
P_manzana_dado_rojo = (P_rojo_dado_manzana * P_manzana) / (
    P_rojo_dado_manzana * P_manzana + P_rojo_dado_naranja * P_naranja
)

# Resultado
print(f"Probabilidad de ser manzana si es roja: {P_manzana_dado_rojo:.2f}")
