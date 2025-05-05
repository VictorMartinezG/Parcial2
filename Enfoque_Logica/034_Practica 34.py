# Tema: Acciones, Situaciones y Eventos - Marcos
# Este código representa marcos (frames) para estructurar conocimiento sobre eventos

# Definimos un marco para un evento: ir al cine
marco_ir_al_cine = {
    "actor": "persona",
    "acción": "ver película",
    "lugar": "cine",
    "objetivo": "entretenimiento"
}

# Función que describe la acción basada en el marco
def describir_evento(marco):
    # Formatea una frase a partir del marco
    return f"{marco['actor']} va al {marco['lugar']} para {marco['acción']} por {marco['objetivo']}."

# Ejemplo de uso
print(describir_evento(marco_ir_al_cine))
