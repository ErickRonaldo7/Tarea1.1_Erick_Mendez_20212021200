import random #para poder usar random.

numeros_random = random.Random() 
numero_adivinar = numeros_random.randint(1, 100) #genera un numero random entre 1-100
intentos = 0

print("¡Adivina el número entre 1 y 100!")

vida_juego = True
while (vida_juego):
    
    numero_usuario = int(input("Ingresa un numero: "))
    intentos = intentos + 1

    #Verifica si el numero_usuario es menor o mayor al random.
    if numero_usuario<numero_adivinar :
        print("El numero a adivinar es mayor.\n")
    elif numero_usuario > numero_adivinar:
        print("El numero a adivinar es menor.\n")
    else:
        print(f"¡Felicitaciones! Has adivinado el número en {intentos} intentos.")
        vida_juego = False  #sale al adivinar