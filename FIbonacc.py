fib=[]
n=int(input('ingresa la posicion a buscar: '))
def fibonacci(n):
  # Definir los primeros dos números de la serie
  
  # Crear una lista para almacenar los números de la serie
  fib.insert(0,1)
  fib.insert(1,1)
  # Generar los números restantes y almacenar en la lista
  for i in range(2, n):
    next=fib[i-2]+fib[i-1]
    fib.append(next)

  # Devolver la lista de números de la serie
# Ejemplo de uso
fibonacci(100)
print(fib[n])