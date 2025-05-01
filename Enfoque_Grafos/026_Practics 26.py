# TEMA: Teoría de Juegos — Modelo de decisiones entre jugadores; buscamos equilibrio de Nash

# Matriz de pagos simplificada: (Jugador1, Jugador2)
# Acciones: Cooperar (C) o Traicionar (T)
matriz_pagos = {
    ('C', 'C'): (3, 3),
    ('C', 'T'): (0, 5),
    ('T', 'C'): (5, 0),
    ('T', 'T'): (1, 1)
}

# Evaluamos todas las combinaciones
acciones = ['C', 'T']
for a1 in acciones:
    for a2 in acciones:
        pago = matriz_pagos[(a1, a2)]
        print(f"Jugador1: {a1}, Jugador2: {a2} → Pagos: {pago}")
