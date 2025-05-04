# Tema: Agentes lógicos
# Simulamos un agente que razona con reglas y hechos

# Base de hechos
hechos = {"llueve", "nublado"}

# Base de reglas: si llueve ∧ nublado → mojarse
def agente():
    if "llueve" in hechos and "nublado" in hechos:
        return "me mojo"
    return "no me mojo"

# Ejecutamos la acción del agente
print("Resultado del agente lógico:", agente())
