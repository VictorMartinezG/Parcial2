# Tema: Lógica no monotónica - el conocimiento puede cambiar
# Lo que antes era cierto puede dejar de serlo al añadir nuevos hechos

# Base inicial
hechos = {"pájaro": "vuela"}

# Nueva información contradice el conocimiento anterior
excepciones = {"pájaro": "no vuela"}  # como un pingüino

def razonar(hechos, excepciones):
    if "pájaro" in excepciones:
        return excepciones["pájaro"]
    return hechos.get("pájaro", "desconocido")

# Resultado antes y después de excepciones
print("Conclusión lógica no monotónica:", razonar(hechos, excepciones))
