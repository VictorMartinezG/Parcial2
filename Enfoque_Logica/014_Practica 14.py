# Tema: Encadenamiento hacia delante y atrás
# Encadenamiento hacia adelante para deducir hechos

# Base de reglas: si A y B entonces C
reglas = [{"si": ["A", "B"], "entonces": "C"}]
hechos = ["A", "B"]  # Hechos conocidos

# Aplicamos encadenamiento hacia adelante
nuevos_hechos = hechos[:]

for regla in reglas:
    if all(premisa in hechos for premisa in regla["si"]):
        nuevos_hechos.append(regla["entonces"])

print("Hechos deducidos:", nuevos_hechos)
