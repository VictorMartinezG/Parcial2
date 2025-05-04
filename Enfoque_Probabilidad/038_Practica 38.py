# Tema: Red de Hopfield
# Objetivo: Recuperar un patrón almacenado

# Patrón binario original
patron = [1, -1, 1, -1]

# Matriz de pesos simétrica sin autoconexiones
pesos = [[0 for _ in patron] for _ in patron]
for i in range(len(patron)):
    for j in range(len(patron)):
        if i != j:
            pesos[i][j] = patron[i] * patron[j]

# Patrón ruidoso
entrada = [1, 1, 1, -1]

# Actualización asincrónica
for _ in range(5):
    for i in range(len(entrada)):
        suma = sum(pesos[i][j] * entrada[j] for j in range(len(entrada)))
        entrada[i] = 1 if suma >= 0 else -1

print("Patrón recuperado:", entrada)
