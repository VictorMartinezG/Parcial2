# TEMA: Tratamiento Probabilístico del Lenguaje — Modelo n-grama (bigrama)

from collections import defaultdict

# Corpus de texto
texto = "el gato duerme el gato come el perro ladra"

# Tokenizamos y contamos bigramas
palabras = texto.split()
bigrama = defaultdict(int)
unigrama = defaultdict(int)

for i in range(len(palabras) - 1):
    unigrama[palabras[i]] += 1
    bigrama[(palabras[i], palabras[i+1])] += 1

# Probabilidad condicional P(p2|p1) = conteo(p1,p2) / conteo(p1)
def prob(p1, p2):
    return bigrama[(p1, p2)] / unigrama[p1]

print("P(duerme | gato):", prob("gato", "duerme"))
print("P(come | gato):", prob("gato", "come"))
