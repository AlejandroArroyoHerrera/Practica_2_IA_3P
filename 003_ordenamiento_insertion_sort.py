# -*- coding: utf-8 -*-
# Autor: arroy

def ordenamiento_por_insercion(lista):
    # Longitud de la lista
    n = len(lista)
    
    # Recorrer de 1 a n en la lista
    for i in range(1, n):
        # Elemento actual a ser comparado
        clave = lista[i]
        
        # Mover los elementos de lista[0..i-1], que son mayores que la clave,
        # a una posición adelante de su posición actual
        j = i-1
        while j >=0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

# Lista de números desordenados
lista_numeros = [12, 11, 13, 5, 6]

# Llamada a la función de ordenamiento por inserción
lista_ordenada = ordenamiento_por_insercion(lista_numeros)

# Imprimir la lista ordenada
print("Lista ordenada:", lista_ordenada)

