#Escribe un programa en python que resuelva el ordenamiento burbuja de manera iterativa, recursiva, en la forma recursiva se deben definir los caso base y general
#Creado por Fernando Ruiz Correa

vector = [3,7,1,9,0,3,4]
def Ordenamiento_burbuja(vector):
    n=len(vector)

    for i in range(1,n):

        for j in range(0,n-1):

            if vector[j]>vector[j+1]:
                aux=vector[j]
                vector[j]=vector[j+1]
                vector[j+1]=aux
    return vector

def burubja_recursiva(vector,n):
    if n == 1:
    #Caso base Cuando el tamño del arreglo es igual a 2
        return
    
    for i in range(n - 1):
       
        if vector[i] > vector[i + 1]:
            vector[i], vector[i + 1] = vector[i + 1], vector[i]

    
    burubja_recursiva(vector, n - 1)

def mostrar_menu():
    print("Menú:")
    print("1. Iterativo ")
    print("2. Recursivo ")
    print("3. Salir ")


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1/2/3): ")

    if opcion == "1":
        print(f"El arreglo sun ordenar es:{vector}")
        arreglo_ordenado = Ordenamiento_burbuja(vector)
        print(f"El arreglo ordenado es: {arreglo_ordenado}")

    elif opcion == "2":
        print(f"El arreglo sun ordenar es:{vector}")
        arreglo_ordenado_recursivo=burubja_recursiva(vector,len(vector))
        print(f"El arreglo ordenado es: {arreglo_ordenado}")

    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3).")
       




