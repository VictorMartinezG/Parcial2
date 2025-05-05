# Tema: Modelo Probabilista Racional
# El agente toma la acción con mayor utilidad esperada

# Acciones posibles con sus probabilidades y utilidades
acciones = {
    "salir_con_paraguas": {"p": 0.9, "utilidad": 7},
    "salir_sin_paraguas": {"p": 0.1, "utilidad": 2},
    "no_salir": {"p": 1.0, "utilidad": 5}
}

# Elegir acción con mayor utilidad esperada
def mejor_decision(acciones):
    mejor = None
    mejor_valor = -float("inf")
    for accion, datos in acciones.items():
        utilidad_esperada = datos["p"] * datos["utilidad"]
        if utilidad_esperada > mejor_valor:
            mejor_valor = utilidad_esperada
            mejor = accion
    return mejor, mejor_valor

# Evaluar
accion, valor = mejor_decision(acciones)
print("Mejor acción:", accion)
print("Utilidad esperada:", valor)
