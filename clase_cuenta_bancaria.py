#Erick Ronaldo Mendez Alvarado - 20212021200

class CuentaBancaria:

#Saldo inicializado en cero.
    def __init__(self, titular:str, saldo: float = 0.00):
        self.titular = titular
        self.saldo = saldo
        


    def depositar(self,cantidad):
        self.saldo = self.saldo + cantidad
        print(f"Deposito de L.{cantidad} exitoso")
        

    def retirar(self,cantidad):
        if cantidad>self.saldo:
            print("Transaccion invalida, fondos insuficiente") 
        else:
            self.saldo = self.saldo - cantidad
            print(f"Retiro de L.{cantidad} exitoso")

    def mostrar_saldo(self):
        print(f"Saldo actual: L.{self.saldo}\n")


    
cuenta1 = CuentaBancaria("Erick Ronaldo Mendez Alvarado")
print(f"Titular de la cuenta: {cuenta1.titular}")

cuenta1.depositar(1000)
cuenta1.mostrar_saldo()

cuenta1.depositar(500.50)
cuenta1.mostrar_saldo()

cuenta1.retirar(500.50)
cuenta1.mostrar_saldo()

cuenta1.retirar(2000) 
cuenta1.mostrar_saldo()      