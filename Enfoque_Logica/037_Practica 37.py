# Tema: Razonamiento por Defecto y No Monotónico
# Este código simula razonamiento por defecto con excepciones

# Base de conocimiento con reglas por defecto
base = {
    "es_ave": ["pinguino", "loro"],
    "vuela_por_defecto": ["loro"],  # el pingüino no vuela
    "no_vuela": ["pinguino"]
}

# Función para determinar si vuela o no
def puede_volar(ave):
    if ave in base["no_vuela"]:
        return False
    elif ave in base["vuela_por_defecto"] or ave in base["es_ave"]:
        return True
    else:
        return False

# Ejemplos
print("¿Puede volar un pingüino?", puede_volar("pinguino"))  # False
print("¿Puede volar un loro?", puede_volar("loro"))          # True
