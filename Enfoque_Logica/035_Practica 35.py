# Tema: Eventos y Objetos Mentales - Creencias
# Este código simula creencias simples que un agente puede tener

# Diccionario de creencias del agente
creencias = {
    "llueve": True,
    "tengo_paraguas": False,
    "debo_salir": True
}

# Función para decidir si salir o no
def decision_salir(creencias):
    if creencias["llueve"] and not creencias["tengo_paraguas"]:
        return "No debo salir, me voy a mojar."
    elif creencias["debo_salir"]:
        return "Salgo preparado."
    else:
        return "Me quedo en casa."

# Evaluación
print("Decisión del agente:", decision_salir(creencias))
