# Tema: Gramáticas Probabilísticas Independientes del Contexto
# Este código genera frases simples con reglas con probabilidades

import random

# Reglas con probabilidades
reglas = {
    "S": [("NP VP", 1.0)],
    "NP": [("el gato", 0.5), ("el perro", 0.5)],
    "VP": [("duerme", 0.5), ("ladra", 0.5)]
}

# Función recursiva para expandir símbolos
def expandir(simbolo):
    if simbolo not in reglas:
        return simbolo  # Terminal
    elecciones = reglas[simbolo]
    r = random.random()
    acumulado = 0
    for produccion, prob in elecciones:
        acumulado += prob
        if r < acumulado:
            return ' '.join([expandir(s) for s in produccion.split()])
    return ""  # Fallback

# Generar frase
print("Frase generada:", expandir("S")) 
