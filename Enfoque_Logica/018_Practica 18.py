# Tema: Reglas de diagnóstico y causales
# Ejemplo: si Fiebre(x) ∧ Tos(x) → Gripe(x)

# Base de hechos
fiebre = ["Juan", "Ana"]
tos = ["Juan"]

# Aplicamos regla de diagnóstico: si tiene fiebre y tos, entonces gripe
def diagnostico():
    pacientes = []
    for x in fiebre:
        if x in tos:
            pacientes.append(x)
    return pacientes

# Mostramos los pacientes diagnosticados con gripe
print("Diagnóstico de gripe:", diagnostico())
