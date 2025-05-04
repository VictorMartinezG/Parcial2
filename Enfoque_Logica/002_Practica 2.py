# Tema: Lógica de Primer Orden
# Este código representa relaciones con predicados simples como "esAmigo(juan, maria)"

# Definimos un conjunto de relaciones como una lista de tuplas
amigos = [("juan", "maria"), ("maria", "pedro"), ("pedro", "ana")]

# Función que verifica si dos personas son amigas directamente
def es_amigo(x, y):
    return (x, y) in amigos

# Verificamos relaciones
print("¿Juan es amigo de Maria?:", es_amigo("juan", "maria"))
print("¿Pedro es amigo de Juan?:", es_amigo("pedro", "juan"))
