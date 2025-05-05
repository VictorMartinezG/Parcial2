# Tema: Reglas, Redes Semánticas y Lógica Descriptiva
# Simulación de reglas y red semántica básica

# Base de hechos
hechos = {
    "es_humano": ["socrates"],
    "es_mortal": []
}

# Reglas simples
def aplicar_reglas(hechos):
    for individuo in hechos["es_humano"]:
        if individuo not in hechos["es_mortal"]:
            hechos["es_mortal"].append(individuo)

# Aplicamos reglas
aplicar_reglas(hechos)

# Mostrar resultados
print("Hechos actualizados:", hechos)
