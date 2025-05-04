# Tema: Lógica modal - operadores como "posible" (◇) y "necesario" (□)
# Usamos valores booleanos para representar mundos posibles

# Base de conocimiento en mundos posibles
mundos = {
    "mundo1": {"llueve": True},
    "mundo2": {"llueve": False}
}

# □p (necesariamente llueve) = llueve en todos los mundos
necesario = all(m["llueve"] for m in mundos.values())

# ◇p (posiblemente llueve) = llueve en al menos un mundo
posible = any(m["llueve"] for m in mundos.values())

print("¿□ llueve?", necesario)
print("¿◇ llueve?", posible)
