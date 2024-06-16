# -*- coding: utf-8 -*-
# Autor: arroy

def mezcla_directa(lista):
    # Si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista

    # Encontrar el punto medio de la lista
    mitad = len(lista) // 2

    # Dividir la lista en dos mitades
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    # Llamada recursiva para ordenar cada mitad
    izquierda = mezcla_directa(izquierda)
    derecha = mezcla_directa(derecha)

    # Mezclar las dos mitades ordenadas
    return mezclar(izquierda, derecha)

def mezclar(izquierda, derecha):
    resultado = []  # Lista para almacenar el resultado de la mezcla
    i = 0  # Índice para recorrer la lista izquierda
    j = 0  # Índice para recorrer la lista derecha

    # Mientras ambos índices estén dentro de los límites de sus respectivas listas
    while i < len(izquierda) and j < len(derecha):
        # Comparar y agregar el menor de los elementos al resultado
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar los elementos restantes de la lista izquierda, si los hay
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1

    # Agregar los elementos restantes de la lista derecha, si los hay
    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    return resultado

# Ejemplo de uso
lista = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", lista)
lista_ordenada = mezcla_directa(lista)
print("Lista ordenada:", lista_ordenada)

