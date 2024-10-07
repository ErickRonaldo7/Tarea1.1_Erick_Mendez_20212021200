#Erick Ronaldo Mendez Alvarado - 20212021200


def es_primo(a: int):
    if (a <2):
        print(f"{a} no es un número primo\n")

       
    for i in range(2, a):
        if a % i == 0:
            print(f"El numero {a} no es un número primo\n")
            return  #sale si se encuentra un divisor.
    print(f"El nuemro {a} es un número primo\n")  # Si no se encontraron divisores.


print("Ingrese 's' para salir\n ") #opcion para que el usuario pueda salir del programa.

programa = True
while (programa):

    a = (input("Ingrese un numero: "))
    
    if (a.lower() == 's'):
        programa= False #cuando el usuario ingresa 's' se cierra el programa.
        print("Saliendo...")
    
    elif (a.isdigit()): #se ocupa de los nuemeros menores a cero y determinar si una letra es diferente a 's'.
        es_primo(int(a)) #funcion que determina si es primo.
    else: 
        print("Ingrese un numero valido\n ") 

    



        

