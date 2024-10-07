
#Erick Ronaldo Mendez Alvarado - 20212021200
class Rectangulo:

    #Base y altura inicializadas en cero.
    def __init__(self, base: float = 0.00 , altura: float = 0.00):
        self.base = base
        self.altura = altura

    def area(self):
        print(f'El área del rectángulo es {self.base * self.altura} unidades cuadradas')
    
    def perimetro(self):
        print(f'El perímetro del rectángulo es {2 * (self.base + self.altura)} unidades')


rectangulo1 = Rectangulo(5.00, 3.00)
rectangulo1.area()
rectangulo1.perimetro()

