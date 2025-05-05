# Tema: Incertidumbre y Factores de Certeza
# Este código simula decisiones basadas en grados de certeza

# Base con factores de certeza (0 a 1)
certezas = {
    "llueve": 0.9,
    "trafico": 0.7
}

# Función para tomar decisiones si el riesgo es alto
def riesgo_total(certezas):
    # Calculamos riesgo como producto de los factores
    riesgo = certezas["llueve"] * certezas["trafico"]
    return riesgo

# Evaluar
riesgo = riesgo_total(certezas)
print(f"Nivel de riesgo total: {riesgo:.2f}")
print("¿Salir o no?", "Mejor espero." if riesgo > 0.5 else "Puedo salir.")
