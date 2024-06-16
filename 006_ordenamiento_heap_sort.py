# -*- coding: utf-8 -*-
# Autor: arroy

def ordenar_monticulo(arreglo, n, i):
    # Inicializar el mayor como raíz
    mayor = i
    # izquierda = 2 * i + 1
    izquierda = 2 * i + 1
    # derecha = 2 * i + 2
    derecha = 2 * i + 2

    # Ver si el hijo izquierdo de la raíz existe y es mayor que la raíz
    if izquierda < n and arreglo[i] < arreglo[izquierda]:
        mayor = izquierda

    # Ver si el hijo derecho de la raíz existe y es mayor que la raíz
    if derecha < n and arreglo[mayor] < arreglo[derecha]:
        mayor = derecha

    # Cambiar la raíz si es necesario
    if mayor != i:
        arreglo[i], arreglo[mayor] = arreglo[mayor], arreglo[i]  # intercambio

        # Aplicar ordenar_monticulo al subárbol afectado
        ordenar_monticulo(arreglo, n, mayor)

def heap_sort(arreglo):
    n = len(arreglo)

    # Construir un maxheap.
    for i in range(n // 2 - 1, -1, -1):
        ordenar_monticulo(arreglo, n, i)

    # Extraer elementos uno por uno
    for i in range(n-1, 0, -1):
        # Mover la raíz actual al final
        arreglo[i], arreglo[0] = arreglo[0], arreglo[i]
        # llamar a ordenar_monticulo en el montículo reducido
        ordenar_monticulo(arreglo, i, 0)

# Código para probar la función
arreglo_prueba = [12, 11, 13, 5, 6, 7]
heap_sort(arreglo_prueba)
n = len(arreglo_prueba)
print("El arreglo ordenado es:")
for i in range(n):
    print("%d" % arreglo_prueba[i])
