# TEMA: Comprobación Hacia Delante (Forward Checking) — Asignación sin conflictos
# OBJETIVO: Asignar colores a regiones usando CSP y reducir ramas inválidas al anticipar conflictos

import copy  # Necesario para copiar estructuras de dominio sin modificarlas directamente

# Lista de variables: regiones del mapa
variables = ['A', 'B', 'C', 'D']

# Dominios: colores disponibles para cada variable
dominios = {
    'A': ['rojo', 'verde'],
    'B': ['rojo', 'verde'],
    'C': ['rojo', 'verde'],
    'D': ['rojo', 'verde']
}

# Restricciones de adyacencia (vecinos no pueden tener el mismo color)
adyacencias = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Función que verifica si asignar un valor a una variable no entra en conflicto con sus vecinos
def es_valida(variable, valor, asignacion):
    for vecino in adyacencias[variable]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False  # Conflicto: el vecino ya tiene el mismo valor
    return True  # No hay conflicto, la asignación es válida

# Algoritmo principal de Comprobación Hacia Delante
def forward_checking(asignacion, dominios_actuales):
    # Si todas las variables están asignadas, se retorna la solución
    if len(asignacion) == len(variables):
        return asignacion
    
    # Elegir la siguiente variable no asignada
    var = next(v for v in variables if v not in asignacion)
    
    # Probar cada valor posible del dominio de la variable
    for valor in dominios_actuales[var]:
        if es_valida(var, valor, asignacion):
            asignacion[var] = valor  # Asignar valor a variable
            nuevos_dominios = copy.deepcopy(dominios_actuales)  # Clonar dominios actuales
            
            # Eliminar el valor de los dominios de los vecinos
            for vecino in adyacencias[var]:
                if vecino not in asignacion:
                    # Remueve valores que son iguales al actual (que causarían conflicto)
                    nuevos_dominios[vecino] = [
                        v for v in nuevos_dominios[vecino] if v != valor
                    ]
                    # Si algún dominio queda vacío, se cancela esta rama
                    if not nuevos_dominios[vecino]:
                        break
            else:
                # Si todo está bien, seguir de manera recursiva
                resultado = forward_checking(asignacion, nuevos_dominios)
                if resultado:
                    return resultado
            del asignacion[var]  # Si no funcionó, deshacemos la asignación
    
    return None  # No se encontró solución válida

# Ejecutar el algoritmo con una copia del dominio original
print("Solución con comprobación hacia delante:", forward_checking({}, copy.deepcopy(dominios)))
