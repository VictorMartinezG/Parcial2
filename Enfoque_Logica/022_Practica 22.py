# Tema: Simulación simple de Prolog
# Base de datos y consultas como en Prolog

# Hechos
padres = [("juan", "maria"), ("pedro", "juan")]

# Regla: abuelo(X,Z) :- padre(X,Y), padre(Y,Z)
def es_abuelo(X, Z):
    for (a, b) in padres:
        if a == X:
            for (c, d) in padres:
                if c == b and d == Z:
                    return True
    return False

# Consulta simulada
print("¿Es juan abuelo de maria?", es_abuelo("juan", "maria"))
print("¿Es pedro abuelo de maria?", es_abuelo("pedro", "maria"))
