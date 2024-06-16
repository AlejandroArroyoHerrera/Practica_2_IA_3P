# -*- coding: utf-8 -*-
# Autor: arroy

# Función para dividir los datos en series iniciales para el ordenamiento polifásico
def dividir_series(datos, num_series):
    # Crear listas vacías para las series
    series = [[] for _ in range(num_series)]
    # Distribuir los elementos en las series
    for i, elemento in enumerate(datos):
        # Asignar elemento a la serie correspondiente
        series[i % num_series].append(elemento)
    return series

# Función para combinar dos series ordenadas
def combinar_series(serie1, serie2):
    # Lista para mantener la serie combinada
    serie_combinada = []
    # Índices para las series
    i, j = 0, 0
    # Combinar las dos series hasta que una se agote
    while i < len(serie1) and j < len(serie2):
        if serie1[i] < serie2[j]:
            serie_combinada.append(serie1[i])
            i += 1
        else:
            serie_combinada.append(serie2[j])
            j += 1
    # Agregar los elementos restantes de la serie que no se ha agotado
    serie_combinada.extend(serie1[i:])
    serie_combinada.extend(serie2[j:])
    return serie_combinada

# Función principal del ordenamiento polifásico
def ordenamiento_polifasico(datos):
    # Número de series iniciales (puede ser ajustado)
    num_series = 3
    # Dividir los datos en series iniciales
    series = dividir_series(datos, num_series)
    
    # Ordenar cada serie individualmente (aquí se puede usar cualquier algoritmo de ordenamiento interno)
    for i in range(num_series):
        series[i].sort()
    
    # Combinar las series ordenadas hasta obtener una sola serie ordenada
    while len(series) > 1:
        nueva_serie = combinar_series(series.pop(0), series.pop(0))
        series.append(nueva_serie)
    
    # Retornar la serie combinada y ordenada finalmente
    return series[0]

# Ejemplo de uso del algoritmo de ordenamiento polifásico
datos = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
datos_ordenados = ordenamiento_polifasico(datos)
print("Datos ordenados:", datos_ordenados)
