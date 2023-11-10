import random
import numpy as np
import matplotlib.pyplot as plt
import timeit

def mochila_fraccionaria(capacidad, objetos):
 #Ordenar por valor peso
 objetos.sort(key = lambda x: x[0]/x[1],reverse = True)
 total_objetos = 0.0
 mochila = []
 for valor, peso in objetos:
  #Si el objeto se puede guardar completo
    if capacidad >= peso:
        mochila.append((valor, peso))
        total_objetos = total_objetos+valor
        capacidad -=peso
   #El objeto pesa mas 
    else:
         fracc = capacidad/ peso
         mochila.append((valor*fracc, peso*fracc))
         total_objetos += valor*fracc
         break
 return total_objetos, mochila


def valores_prueba(n_items):
   obj = [(random.randint(1, 50), random.randint(1, 100)) for _ in range(n_items)]
   capacity= random.randint(1,1000 )
   return obj, capacity

def medir_tiempo_ejecucion(func, capacidad, objetos):
    tiempo_inicio = timeit.default_timer()
    func(capacidad, objetos)
    tiempo_fin = timeit.default_timer()
    return tiempo_fin - tiempo_inicio

def graficar_tiempos(n_items_range):
    tiempos = []

    for n_items in n_items_range:
        objetos, capacidad = valores_prueba(n_items)
        tiempo = medir_tiempo_ejecucion(mochila_fraccionaria, capacidad, objetos)
        tiempos.append(tiempo)

    # Graficar los resultados
    plt.plot(n_items_range, tiempos, marker='o')
    plt.title('Tiempo de ejecución vs Número de objetos')
    plt.xlabel('Número de objetos')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.show()

if __name__ == "__main__":
    n_items = random.randint(1,1000)
    objetos, capacidad= valores_prueba(n_items)
    total_objetos, mochila=mochila_fraccionaria(capacidad, objetos)
    print(f"La capacidad es {capacidad} y los objetos son: {objetos} ")
    print(f"El total de objetos es {total_objetos} y la mochila es{mochila}")
    
    n_items_range = range(1, 1001, 50)  # Puedes ajustar el rango según tus necesidades
    graficar_tiempos(n_items_range)
#if __name__ == "__main__":
    #n_items = random.randint(1,1000)
    #objetos, capacidad= valores_prueba(n_items)
    #total_objetos, mochila=mochila_fraccionaria(capacidad, objetos)
    #print(f"La capacidad es {capacidad} y los objetos son: {objetos} ")
    #print(f"El total de objetos es {total_objetos} y la mochila es{mochila}")
    

   #objetos = [(5,10),(1,15),(1,8),(3,15)]
   #capacidad = 35

   #total_objetos, mochila = mochila_fraccionaria(capacidad, objetos)
   #print(f"El total de objetos es {total_objetos} y la mochila{mochila}")
  
   

