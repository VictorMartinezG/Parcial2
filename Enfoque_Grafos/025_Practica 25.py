# TEMA: Red Bayesiana Dinámica — Modela evolución de variables en el tiempo

# Probabilidad de que esté lloviendo mañana depende del clima hoy
P_lluvia = {
    'hoy_lluvia': 0.8,
    'hoy_no_lluvia': 0.2
}

# Estado inicial
estado_hoy = 'hoy_lluvia'

# Simulamos probabilidad para el siguiente día
prob_lluvia_mañana = P_lluvia[estado_hoy]
print(f"Probabilidad de lluvia mañana: {prob_lluvia_mañana}")
