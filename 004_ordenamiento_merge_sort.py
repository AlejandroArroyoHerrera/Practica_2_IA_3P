# -*- coding: utf-8 -*-
# Autor: arroy

def ordenamiento_por_mezcla(lista):
    # Si la lista es mayor que 1, se divide y se ordena
    if len(lista) > 1:
        # Dividir la lista en dos mitades
        mitad = len(lista) // 2
        sublista_izquierda = lista[:mitad]
        sublista_derecha = lista[mitad:]

        # Ordenamiento recursivo de las sublistas
        ordenamiento_por_mezcla(sublista_izquierda)
        ordenamiento_por_mezcla(sublista_derecha)

        # Indices para recorrer las sublistas
        i = j = k = 0

        # Copiar datos a las sublistas temporales
        while i < len(sublista_izquierda) and j < len(sublista_derecha):
            if sublista_izquierda[i] < sublista_derecha[j]:
                lista[k] = sublista_izquierda[i]
                i += 1
            else:
                lista[k] = sublista_derecha[j]
                j += 1
            k += 1

        # Comprobar si quedan elementos en la sublista izquierda
        while i < len(sublista_izquierda):
            lista[k] = sublista_izquierda[i]
            i += 1
            k += 1

        # Comprobar si quedan elementos en la sublista derecha
        while j < len(sublista_derecha):
            lista[k] = sublista_derecha[j]
            j += 1
            k += 1

    return lista

# Lista de números desordenados
lista_numeros = [38, 27, 43, 3, 9, 82, 10]

# Llamada a la función de ordenamiento por mezcla
lista_ordenada = ordenamiento_por_mezcla(lista_numeros)

# Imprimir la lista ordenada
print("Lista ordenada:", lista_ordenada)

