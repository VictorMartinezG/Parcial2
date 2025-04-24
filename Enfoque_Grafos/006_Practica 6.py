# Práctica 6: Búsqueda Bidireccional
from collections import deque
def bidireccional(grafo, inicio, objetivo):
    if inicio == objetivo:
        return [inicio]  # Caso trivial: inicio y objetivo iguales

    frente_inicio = deque([[inicio]])  # Caminos desde el inicio
    frente_objetivo = deque([[objetivo]])  # Caminos desde el objetivo
    visitados_inicio = {inicio}  # Nodos visitados desde el inicio
    visitados_objetivo = {objetivo}  # Nodos visitados desde el objetivo

    while frente_inicio and frente_objetivo:
        # Expansión desde el inicio
        camino_inicio = frente_inicio.popleft()
        nodo_inicio = camino_inicio[-1]

        for vecino in grafo.get(nodo_inicio, []):
            if vecino in visitados_objetivo:
                for camino_obj in frente_objetivo:
                    if camino_obj[-1] == vecino:
                        return camino_inicio + camino_obj[::-1][1:]  # Unimos caminos
            if vecino not in visitados_inicio:
                visitados_inicio.add(vecino)
                frente_inicio.append(camino_inicio + [vecino])

        # Expansión desde el objetivo
        camino_objetivo = frente_objetivo.popleft()
        nodo_objetivo = camino_objetivo[-1]

        for vecino in grafo.get(nodo_objetivo, []):
            if vecino in visitados_inicio:
                for camino_ini in frente_inicio:
                    if camino_ini[-1] == vecino:
                        return camino_ini + camino_objetivo[::-1][1:]  # Unimos caminos
            if vecino not in visitados_objetivo:
                visitados_objetivo.add(vecino)
                frente_objetivo.append(camino_objetivo + [vecino])

    return None  # Si no hay conexión entre ambas búsquedas

grafo_simple = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("\nBidireccional - Camino:", bidireccional(grafo_simple, 'A', 'F'))