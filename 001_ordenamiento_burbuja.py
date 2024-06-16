# -*- coding: utf-8 -*-
# Autor: arroy


def ordenamiento_burbuja(lista):
    # Longitud de la lista
    n = len(lista)
    
    # Recorrer todos los elementos de la lista
    for i in range(n):
        # Los últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Recorrer la lista desde 0 hasta n-i-1
            # Intercambiar si el elemento encontrado es mayor que el siguiente
            if lista[j] > lista[j+1]:
                # Intercambio de elementos
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Lista de números desordenados
lista_numeros = [64, 34, 25, 12, 22, 11, 90]

# Llamada a la función de ordenamiento burbuja
lista_ordenada = ordenamiento_burbuja(lista_numeros)

# Imprimir la lista ordenada
print("Lista ordenada:", lista_ordenada)