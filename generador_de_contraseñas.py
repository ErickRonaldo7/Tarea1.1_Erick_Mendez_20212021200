#Erick Ronaldo Mendez Alvarado - 20212021200
import random 
import string



def generador_contrasena(a: int):

    generador = True #mantener el while.
    contador = 0   #contador de caracteres.
    contrasena = '' #para que entre vacia al ciclo.
    while generador:
         
        numero = random.choice(string.digits) #escoge un digito.
        letra = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')#escoge cualquier letra de la cadena.
        signo = random.choice(string.punctuation)#escoge cualquier signo de puntuacion.
     

        caracter_seleccionado = random.choice([numero,letra,signo]) 
        #de los tres anteriores escoge uno, ya sea numero, letra o signo al azar.

        contrasena += caracter_seleccionado
        #anade caracreres a la contrasena.
        contador = contador + 1

        if contador == a:
          print(f'la contraseña generada es: {contrasena}')
          generador = False



longitud = int(input("Ingrese la longitud de contraseña deseada: "))
if longitud < 8:
        print("Longitud minima para contraseña segura es de 8,elija un nuevo tamaño: ")
else:
    generador_contrasena(longitud)
