# Tema: Lógica difusa - en lugar de verdadero/falso, usamos grados de verdad [0,1]

# Definimos una función de pertenencia difusa para "temperatura alta"
def temperatura_alta(temp):
    if temp <= 20:
        return 0.0
    elif temp >= 30:
        return 1.0
    else:
        return (temp - 20) / 10

# Temperaturas de prueba
temps = [18, 22, 25, 30, 35]

# Evaluamos el grado de verdad
grados = [temperatura_alta(t) for t in temps]

# Mostramos resultados
print("Grados de temperatura alta (lógica difusa):")
for t, g in zip(temps, grados):
    print(f"Temp: {t}°C → Grado: {g:.2f}")
