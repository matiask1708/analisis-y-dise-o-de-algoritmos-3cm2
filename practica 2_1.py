#Este programa se encarga de generar un codigo para resolver el punto 2,5 de la practica 2 de Analisis y diseño de algoritmos 

import random
import numpy as np
import matplotlib.pyplot as plt
import timeit


def generar_arreglo_aleatorio(tamano):
    return [random.randint(1, 1000) for _ in range(tamano)]       


def quicksort(arr):
    #CASO BASE 
    if len(arr)<=1:
        return arr
    #CASO GENERAL
    pivote = arr[0]
    menores = []
    mayores = []
    for i in range(1, len(arr)):
        if arr[i]<pivote:
            menores.append(arr[i])
        else:
            mayores.append(arr[i])
    return menores + [pivote] + mayores




n = 100
longitud_Arreglos = [random.randint(1,n ) for i in range(100)]
x_valores = []
y_valores = []


for i, tamano in enumerate(longitud_Arreglos,1):
    arr=generar_arreglo_aleatorio(tamano)
    print(f"Arreglo {i} original de tamaño {tamano}: {np.array(arr)}")
    time= timeit.timeit(lambda:quicksort(arr),number=1000)
    x_valores.append(tamano)
    y_valores.append(time)
    print(f"Arreglo{i}ordenado de tamaño{tamano}:{np.array(quicksort(arr))}")
    print(f"Tardó {time} segundos en ordenarse.")


plt.plot(x_valores)
plt.xlabel('Longitud del arreglo')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Rendimiento de Quicksort con pivote en la posicion 0 para los arreglos')
plt.show()