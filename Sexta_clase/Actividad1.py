#Ejercicio 1
def resta(a,b):
    return a-b
resta(30, 10)
print(resta(30, 10))

#Ejercicio 2
def resta2(a,b):
    return a-b
resta2(b=30, a=10)
print(resta2(a =10, b = 30))

#Ejercicio 3
def funcion():
    return "bienvenidos a python"
frase = funcion()
print(frase)

#Ejercicio 4
def resta3(a=None, b=None):
    if a== None or b ==None:
        print("error, faltan parametros a la funcion")
        return
    return a-b
resta3()

#Ejercicio 5
def calculo(precio, descuento):
    return precio -(precio * descuento /100)

datos = [10000, 10]
print("el monto final a pagar es: ", calculo(*datos))

#Ejercicio 6

def saludo(nombre, mensaje = 'Python'):
    print(mensaje, nombre)
saludo(mensaje="buen dia", nombre ="Pedro")