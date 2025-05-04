# Tema: Lógica temporal
# Usamos una secuencia de estados a lo largo del tiempo

# Estado del sistema a lo largo del tiempo
tiempo = [
    {"motor_encendido": False},
    {"motor_encendido": True},
    {"motor_encendido": True},
    {"motor_encendido": False}
]

# ◻p (siempre p): motor está siempre encendido
siempre_encendido = all(e["motor_encendido"] for e in tiempo)

# ◇p (alguna vez p): motor está encendido en algún momento
alguna_vez_encendido = any(e["motor_encendido"] for e in tiempo)

print("¿Siempre encendido?", siempre_encendido)
print("¿Alguna vez encendido?", alguna_vez_encendido)
