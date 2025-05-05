# Tema: Taxonomías - Categorías y Objetos
# Este código representa una taxonomía de categorías y objetos en un árbol jerárquico

# Taxonomía en forma de árbol: cada nodo tiene hijos
taxonomia = {
    "vehículo": ["terrestre", "acuático"],
    "terrestre": ["auto", "moto"],
    "acuático": ["lancha", "submarino"]
}

# Función para imprimir la jerarquía de la taxonomía
def imprimir_taxonomia(categoria, nivel=0):
    # Imprime la categoría con sangría según su nivel
    print("  " * nivel + "- " + categoria)
    # Si tiene subcategorías, se imprimen recursivamente
    for sub in taxonomia.get(categoria, []):
        imprimir_taxonomia(sub, nivel + 1)

# Mostrar toda la taxonomía
imprimir_taxonomia("vehículo")
