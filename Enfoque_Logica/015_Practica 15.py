# Tema: Backtracking
# Buscamos una asignación válida para variables lógicas con restricciones

# Variables A y B deben cumplir A ≠ B
def backtrack():
    for A in [True, False]:
        for B in [True, False]:
            if A != B:
                return A, B

# Ejecutamos y mostramos la solución
asignacion = backtrack()
print("Asignación válida (A, B):", asignacion)
