# Tema: Planificación
# Planeamos llegar de A a C usando acciones disponibles

# Estados y acciones representadas como diccionario
acciones = {
    "A": ["B"],
    "B": ["C"],
    "C": []
}

# Función de planificación simple tipo DFS (Depth-First Search)
def planificar(inicio, meta, camino=[]):
    camino = camino + [inicio]
    if inicio == meta:
        return camino
    for siguiente in acciones[inicio]:
        if siguiente not in camino:
            nuevo_camino = planificar(siguiente, meta, camino)
            if nuevo_camino:
                return nuevo_camino
    return None

# Se planifica de A a C
print("Plan de A a C:", planificar("A", "C"))
