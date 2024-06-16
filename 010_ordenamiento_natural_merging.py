# -*- coding: utf-8 -*-
# Autor: arroy

# Función para realizar la fusión natural de dos sublistas
def fusionar(sublista1, sublista2):
    i, j = 0, 0
    resultado = []
    
    # Fusionar las dos sublistas mientras haya elementos en ambas
    while i < len(sublista1) and j < len(sublista2):
        if sublista1[i] <= sublista2[j]:
            resultado.append(sublista1[i])
            i += 1
        else:
            resultado.append(sublista2[j])
            j += 1
    
    # Agregar los elementos restantes de sublista1, si los hay
    while i < len(sublista1):
        resultado.append(sublista1[i])
        i += 1
    
    # Agregar los elementos restantes de sublista2, si los hay
    while j < len(sublista2):
        resultado.append(sublista2[j])
        j += 1
    
    return resultado

# Función principal para el ordenamiento natural merging
def ordenamiento_natural(lista):
    # Lista para almacenar las sublistas naturales
    sublistas = []
    sublista_actual = [lista[0]]

    # Dividir la lista en sublistas naturales
    for i in range(1, len(lista)):
        if lista[i] >= lista[i - 1]:
            sublista_actual.append(lista[i])
        else:
            sublistas.append(sublista_actual)
            sublista_actual = [lista[i]]
    sublistas.append(sublista_actual)

    # Fusionar sublistas hasta que quede una sola lista ordenada
    while len(sublistas) > 1:
        nuevas_sublistas = []
        for i in range(0, len(sublistas) - 1, 2):
            nueva_sublista = fusionar(sublistas[i], sublistas[i + 1])
            nuevas_sublistas.append(nueva_sublista)
        if len(sublistas) % 2 == 1:
            nuevas_sublistas.append(sublistas[-1])
        sublistas = nuevas_sublistas

    return sublistas[0]

# Ejemplo de uso
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
lista_ordenada = ordenamiento_natural(lista)
print("Lista ordenada:", lista_ordenada)