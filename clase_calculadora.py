#Erick Ronaldo Mendez Alvarado - 20212021200


class Calculadora:
    def __init__(self,a: float , b:float):
        self.a = a
        self.b = b


    #metodos, acciones de la calculadora
    def suma(self):
        print(f'{self.a} + {self.b} = {self.a+self.b}')
    
    def resta(self):
        print(f'{self.a} - {self.b} = {self.a - self.b}')

    def multiplicacion(self):
        print(f'{self.a} * {self.b} = {self.a * self.b}')

    def division(self):
        if self.b == 0:
            print("Operacion invalida, no se puede dividir entre cero.")
        else:
            print(f'{self.a} / {self.b} = {self.a / self.b}')


#eleccion de operacion
print('1. Suma\n 2. Resta\n 3. Multiplicacion\n 4. Division\n 5.Salir')
menu = True
while (menu):

    opcion = float(input("Elija la operacion a realizar:"))

    match opcion:
        case 1:
            print("Ingrese los valores:\n")
            a = float(input("a: "))
            b = float(input("b: "))
            calduladora1 = Calculadora(a,b)
            calduladora1.suma()
            print()
            

        case 2:
            print("Ingrese los valores:\n")
            a = float(input("a: "))
            b = float(input("b: "))
            calduladora1 = Calculadora(a,b)
            calduladora1.resta()
            print()#salto de linea.

        case 3:
            print("Ingrese los valores:\n")
            a = float(input("a: "))
            b = float(input("b: "))
            calduladora1 = Calculadora(a,b)
            calduladora1.multiplicacion()
            print()#salto de linea.

        case 4:
            print("Ingrese los valores:\n")
            a = float(input("a: "))
            b = float(input("b: "))
            calduladora1 = Calculadora(a,b)
            calduladora1.division()
            print()#salto de linea.
    
        case 5:
            #opcion para salir de la calculadora.
            if (opcion ==5):
                menu = False
            print("Saliendo...")
          








