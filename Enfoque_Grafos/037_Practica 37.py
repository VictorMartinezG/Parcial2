# TEMA: Acondicionamiento del Corte (Cutset Conditioning)
# OBJETIVO: Romper ciclos en un CSP convirtiéndolo en un árbol al fijar algunas variables

# Variables y dominios
variables = ['A', 'B', 'C']
dominios = {
    'A': [1, 2],
    'B': [1, 2],
    'C': [1, 2]
}

# Restricciones: todas diferentes
def consistente(asignacion):
    return len(set(asignacion.values())) == len(asignacion)

# Asignación forzada (cutset): fijamos una variable
def cutset_conditioning():
    soluciones = []
    for valor_cut in dominios['A']:
        asignacion = {'A': valor_cut}
        
        # Resolver el resto como árbol (B y C)
        for b in dominios['B']:
            for c in dominios['C']:
                asignacion_temp = asignacion.copy()
                asignacion_temp['B'] = b
                asignacion_temp['C'] = c
                if consistente(asignacion_temp):
                    soluciones.append(asignacion_temp)
    return soluciones

# Ejecutar
print("Soluciones por acondicionamiento del corte:", cutset_conditioning())
