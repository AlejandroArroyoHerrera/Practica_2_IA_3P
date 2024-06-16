# -*- coding: utf-8 -*-
# Autor: arroy

def ordenamiento_por_seleccion(lista):
    # Longitud de la lista
    n = len(lista)
    
    # Recorrer todos los elementos de la lista
    for i in range(n):
        # Encontrar el mínimo elemento restante sin ordenar
        indice_minimo = i
        for j in range(i+1, n):
            if lista[indice_minimo] > lista[j]:
                indice_minimo = j
        
        # Intercambiar el elemento mínimo encontrado con el primer elemento
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

# Lista de números desordenados
lista_numeros = [64, 25, 12, 22, 11]

# Llamada a la función de ordenamiento por selección
lista_ordenada = ordenamiento_por_seleccion(lista_numeros)

# Imprimir la lista ordenada
print("Lista ordenada:", lista_ordenada)