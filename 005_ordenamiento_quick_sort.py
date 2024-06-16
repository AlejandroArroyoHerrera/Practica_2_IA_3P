# -*- coding: utf-8 -*-
# Autor: arroy

def ordenamiento_rapido(lista):
    # Función auxiliar para realizar el ordenamiento
    def quicksort(array, inicio, fin):
        if inicio < fin:
            # Posición del pivote
            pivote = particion(array, inicio, fin)
            # Ordenar la lista antes y después del pivote
            quicksort(array, inicio, pivote-1)
            quicksort(array, pivote+1, fin)

    # Función para dividir el array y hacer los intercambios
    def particion(array, inicio, fin):
        # Seleccionar el último elemento como pivote
        pivote = array[fin]
        i = inicio - 1
        for j in range(inicio, fin):
            # Si el elemento actual es menor o igual al pivote
            if array[j] <= pivote:
                # Incrementar el índice del menor elemento
                i += 1
                array[i], array[j] = array[j], array[i]
        # Intercambiar el pivote con el elemento en la posición i+1
        array[i+1], array[fin] = array[fin], array[i+1]
        return i + 1

    # Llamada inicial a la función quicksort
    quicksort(lista, 0, len(lista)-1)
    return lista

# Lista de números desordenados
lista_numeros = [10, 7, 8, 9, 1, 5]

# Llamada a la función de ordenamiento rápido
lista_ordenada = ordenamiento_rapido(lista_numeros)

# Imprimir la lista ordenada
print("Lista ordenada:", lista_ordenada)
