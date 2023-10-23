
#creado por Fernando Ruiz Correa
n=int(input('ingresa el numero para sacar el factorial: '))
def fact_recursivo(n):
    if n==1:
     return 1
    else:
       return n*fact_recursivo(n-1)

  
resultado = fact_recursivo(n)
print(resultado)
