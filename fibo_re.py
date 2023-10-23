#creado por Fernando Ruiz Correa 

n=int(input('ingrese el numero de terminos en la serie fibonacci: '))
def fibonacci_recursivo(n):
    if n==0:
     return 0
    elif n==1:
        return 1
    else:
       return fibonacci_recursivo(n-2)+fibonacci_recursivo(n-1)
        
        


resultado = fibonacci_recursivo(n)
print("La serie fibonacci para los primeros ",n,"terminos es:")

for i in range(n):
        print(fibonacci_recursivo(i))