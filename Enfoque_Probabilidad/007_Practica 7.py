# TEMA: Percepción — Sensor que detecta si hay pared con error

import random

# Estado real (hay pared o no)
estado_real = "pared"

# Sensor con error del 20%
def sensor():
    if estado_real == "pared":
        return "pared" if random.random() < 0.8 else "no pared"
    else:
        return "no pared" if random.random() < 0.8 else "pared"

# Simulamos varias lecturas del sensor
lecturas = [sensor() for _ in range(10)]
print("Lecturas del sensor:", lecturas)

# Contamos frecuencia
from collections import Counter
conteo = Counter(lecturas)
prob_pared = conteo["pared"] / len(lecturas)

print("Probabilidad estimada de que haya pared:", prob_pared)
