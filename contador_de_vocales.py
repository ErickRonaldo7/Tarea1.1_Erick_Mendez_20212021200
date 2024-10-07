#Erick Ronaldo Mendez Alvarado - 2012021200

def contar_vovales(palabra: str = ''):
    palabra = input("Ingrese una frase: ")
    palabra = palabra.lower()
    cantidad = 0
    for i in range (len(palabra)):
        if palabra[i] in 'aeiou':
            cantidad = cantidad + 1
    print(f"La frase {palabra} tiene: {cantidad} vocales")

contar_vovales()

