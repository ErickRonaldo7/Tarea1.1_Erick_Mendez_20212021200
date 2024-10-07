#Erick Ronaldo Mendez Alvarado - 20212021200


def fibonacci(n: int):
    a = 0 
    b = 1

    for i in range(n):
        c = a + b
        a = b
        b = c

    return b 
    
numero = int(input("Ingrese un numero limite para secuencia de fibonacci: "))

for i in range (numero):
    print(fibonacci(i))
