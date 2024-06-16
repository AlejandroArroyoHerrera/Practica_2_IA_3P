# -*- coding: utf-8 -*-
# Autor: arroy

import heapq

def balancear_mezcla_multiway(arrays):

    # Crear una lista de min-heaps
    heap = []
    
    # Insertar el primer elemento de cada lista en el heap
    for i in range(len(arrays)):
        if arrays[i]:
            # Agregar una tupla que contiene el elemento, el índice de la lista y el índice del elemento en la lista
            heapq.heappush(heap, (arrays[i][0], i, 0))

    resultado = []

    # Mientras el heap no esté vacío
    while heap:
        # Obtener el elemento más pequeño del heap
        valor, lista_idx, elemento_idx = heapq.heappop(heap)
        resultado.append(valor)

        # Si la lista de la que proviene el elemento tiene más elementos, agregar el siguiente al heap
        if elemento_idx + 1 < len(arrays[lista_idx]):
            siguiente_elemento = arrays[lista_idx][elemento_idx + 1]
            heapq.heappush(heap, (siguiente_elemento, lista_idx, elemento_idx + 1))

    return resultado

# Ejemplo de uso
listas_para_ordenar = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

# Llamada a la función para ordenar las listas
resultado_ordenado = balancear_mezcla_multiway(listas_para_ordenar)
print(resultado_ordenado)