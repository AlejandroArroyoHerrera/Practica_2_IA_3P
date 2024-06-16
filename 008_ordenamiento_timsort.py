# -*- coding: utf-8 -*-
# Autor: arroy

# Definición del tamaño mínimo para ejecutar la inserción directa
TAMANO_MINIMO = 32

def insercion_directa(array, left, right):
    """Función que realiza la ordenación por inserción directa"""
    for i in range(left + 1, right + 1):
        elemento_clave = array[i]
        j = i - 1
        while j >= left and array[j] > elemento_clave:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = elemento_clave

def fusionar(array, l, m, r):
    """Función que fusiona dos subarrays ordenados"""
    len1, len2 = m - l + 1, r - m
    izquierda = array[l:m + 1]
    derecha = array[m + 1:r + 1]

    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if izquierda[i] <= derecha[j]:
            array[k] = izquierda[i]
            i += 1
        else:
            array[k] = derecha[j]
            j += 1
        k += 1

    while i < len1:
        array[k] = izquierda[i]
        k += 1
        i += 1

    while j < len2:
        array[k] = derecha[j]
        k += 1
        j += 1

def timsort(array):
    """Función principal que ejecuta el algoritmo Timsort"""
    n = len(array)
    for i in range(0, n, TAMANO_MINIMO):
        insercion_directa(array, i, min(i + TAMANO_MINIMO - 1, n - 1))

    tamano = TAMANO_MINIMO
    while tamano < n:
        for izquierda in range(0, n, 2 * tamano):
            medio = min(n - 1, izquierda + tamano - 1)
            derecha = min((izquierda + 2 * tamano - 1), (n - 1))
            if medio < derecha:
                fusionar(array, izquierda, medio, derecha)
        tamano = 2 * tamano

# Ejemplo de uso del algoritmo Timsort
array = [34, 7, 23, 32, 5, 62, 32, 7, 31, 5]
print("Lista desordenada:", array)
timsort(array)
print("Lista ordenada:", array)