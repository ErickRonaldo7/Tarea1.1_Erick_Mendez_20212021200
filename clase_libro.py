#Erick Ronaldo Mendez Alvarado - 20212021200

class Libro:
    def __init__(self, titulo:str, autor:str, anio_publicacion:int,numero_paginas:int):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.numero_paginas = numero_paginas   
        
    def mostrar_informacion(self):
        print(f'Titulo: {self.titulo} \nAutor: {self.autor} \nAño de publicación: {self.anio_publicacion} \nNúmero de páginas: {self.numero_paginas}')
        

libro1 = Libro("Los amantes bajo el Danubio","Federico Andahazi",2015,336)
libro1.mostrar_informacion()