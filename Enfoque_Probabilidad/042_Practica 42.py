# Tema: Recuperación de Información (IR)
# Indexa oraciones y permite buscar palabras claves

# Documentos base
documentos = [
    "el gato duerme en el sofá",
    "el perro juega en el patio",
    "la gata maulla fuerte"
]

# Indexar palabras por documento
indice = {}
for i, doc in enumerate(documentos):
    for palabra in doc.split():
        if palabra not in indice:
            indice[palabra] = []
        if i not in indice[palabra]:
            indice[palabra].append(i)

# Buscar documentos por palabra clave
def buscar(palabra):
    return [documentos[i] for i in indice.get(palabra, [])]

# Ejemplo de búsqueda
print("Documentos con 'gato':", buscar("gato"))
