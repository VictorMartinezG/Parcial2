# Tema: Lógica Difusa
# Se aplica lógica difusa para determinar el nivel de temperatura (bajo, medio, alto)

# Función de pertenencia difusa para temperatura "alta"
def pertenencia_alta(temp):
    if temp <= 25:
        return 0
    elif temp >= 35:
        return 1
    else:
        return (temp - 25) / 10

# Prueba con un valor de temperatura
temperatura = 30
nivel = pertenencia_alta(temperatura)

# Se muestra el grado de pertenencia al conjunto "Alta"
print("Grado de pertenencia a 'Alta' para", temperatura, "°C:", nivel)
