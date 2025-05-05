# Tipos de razonamiento y aprendizaje
# Razonamiento Deductivo: A partir de premisas generales se deducen conclusiones.
# Razonamiento Inductivo: A partir de observaciones particulares se generalizan conclusiones.
# Razonamiento Abductivo: Se infiere la causa más probable para una observación.

# Ejemplo de aprendizaje inductivo: Dado un conjunto de ejemplos, aprender un modelo.
# Este ejemplo es simple para ilustrar el proceso.

def razonamiento_inductivo(observaciones):
    """Realiza razonamiento inductivo a partir de las observaciones."""
    # Supongamos que aprendemos una relación en el conjunto de datos
    modelo_aprendido = set(observaciones)
    return modelo_aprendido

# Ejemplo de observaciones
observaciones = [("rojo", "manzana"), ("verde", "pera"), ("amarillo", "banana")]
modelo = razonamiento_inductivo(observaciones)
print("Modelo aprendido:", modelo)
