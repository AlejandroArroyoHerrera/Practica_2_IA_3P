# -*- coding: utf-8 -*-
# Autor: arroy

def shell_sort(arreglo):
    # Iniciar con un intervalo grande, luego reducir el intervalo
    n = len(arreglo)
    intervalo = n // 2

    # Realizar un ordenamiento por inserción "gapped" para este intervalo
    while intervalo > 0:
        for i in range(intervalo, n):
            # Guardar el elemento arreglo[i] y su posición
            temp = arreglo[i]
            j = i
            # Desplazar elementos anteriores al intervalo hasta encontrar la ubicación correcta para arreglo[i]
            while j >= intervalo and arreglo[j - intervalo] > temp:
                arreglo[j] = arreglo[j - intervalo]
                j -= intervalo

            # Colocar temp (el valor original de arreglo[i]) en su posición correcta
            arreglo[j] = temp
        # Reducir el intervalo para la siguiente ronda de "gapped" ordenamiento por inserción
        intervalo //= 2

# Código para probar la función
arreglo_prueba = [12, 34, 54, 2, 3]
shell_sort(arreglo_prueba)
print("El arreglo ordenado es:")
for i in range(len(arreglo_prueba)):
    print("%d" % arreglo_prueba[i])


