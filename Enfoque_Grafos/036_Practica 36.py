# TEMA: Búsqueda Local — Mínimos Conflictos
# OBJETIVO: Resolver CSP grandes usando heurística que minimiza conflictos

import random

# Variables: 4 reinas (problema de 4-reinas)
variables = [0, 1, 2, 3]  # Columnas
n = len(variables)

# Función para contar conflictos en la posición actual
def contar_conflictos(asignacion, fila, col):
    conflictos = 0
    for c in range(n):
        if c != col:
            f = asignacion[c]
            if f == fila or abs(f - fila) == abs(c - col):  # Misma fila o diagonal
                conflictos += 1
    return conflictos

# Algoritmo de mínimos conflictos
def min_conflicts(max_intentos=1000):
    asignacion = [random.randint(0, n - 1) for _ in variables]  # Inicializar aleatorio
    
    for _ in range(max_intentos):
        # Verificar si es solución (sin conflictos)
        conflictos_totales = sum(contar_conflictos(asignacion, asignacion[col], col) for col in variables)
        if conflictos_totales == 0:
            return asignacion
        
        # Escoger una reina con conflicto
        col_conflicto = random.choice([col for col in variables if contar_conflictos(asignacion, asignacion[col], col) > 0])
        
        # Moverla a la fila que cause menos conflictos
        min_conf = float('inf')
        mejor_fila = 0
        for fila in range(n):
            conf = contar_conflictos(asignacion, fila, col_conflicto)
            if conf < min_conf:
                min_conf = conf
                mejor_fila = fila
        asignacion[col_conflicto] = mejor_fila
    return None  # No se encontró solución

# Ejecutar
print("Solución con mínimos conflictos (4 reinas):", min_conflicts())
