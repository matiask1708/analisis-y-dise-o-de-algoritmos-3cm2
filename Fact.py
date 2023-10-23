def factorial(numero):
    r=1
    for i in range(1,numero):
        r*=i
    return r
print("Escoja un numero")
n = int(input())
print("El factorial de",n,"es",factorial(n+1))
