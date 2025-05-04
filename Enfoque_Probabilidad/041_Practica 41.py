# Tema: Gramáticas Probabilísticas Lexicalizadas
# Se incluyen palabras específicas con su categoría y probabilidades

import random

# Gramática con palabras específicas (lexicalizadas)
reglas = {
    "S": [("NP VP", 1.0)],
    "NP": [("Det N", 1.0)],
    "Det": [("el", 0.5), ("un", 0.5)],
    "N": [("gato", 0.5), ("perro", 0.5)],
    "VP": [("V", 0.5), ("V NP", 0.5)],
    "V": [("duerme", 0.5), ("ve", 0.5)]
}

# Función para generar una oración
def expandir(simbolo):
    if simbolo not in reglas:
        return simbolo
    elecciones = reglas[simbolo]
    r = random.random()
    acumulado = 0
    for produccion, prob in elecciones:
        acumulado += prob
        if r < acumulado:
            return ' '.join([expandir(s) for s in produccion.split()])
    return ""

# Resultado
print("Frase lexicalizada:", expandir("S"))
