#importar funciones desde otra carpeta
from FuncionesCalculadora import *

menu_activo = True
opcion_seleccionada = 0
numero_1 = 0
numero_2= 0
resultado = 0


while menu_activo:
    print("1.- Sumar 2 numeros")
    print("2.- Restar 2 numeros")
    print("3.- Dividir 2 numeros")
    print("4.- Multiplicar 2 numeros")
    print("5.- Numero exponencial de un numero")
    print("6.- salir")
    

    opcion_seleccionada=int(input("Seleccione una opcion "))
    if opcion_seleccionada == 1:
        numero_1 = int(input("ingrese un primer numero "))
        numero_2 = int(input("Ingrese un segundo numero "))
        resultado = sumar(numero_1, numero_2)
        print("El resultado de la suma es ", resultado)

    if opcion_seleccionada == 2:
        numero_1 = int(input("ingrese un primer numero "))
        numero_2 = int(input("Ingrese un segundo numero "))
        resultado = resta(numero_1, numero_2)
        print("El resultado de la resta es ", resultado)

    if opcion_seleccionada == 3:
        numero_1 = int(input("ingrese un primer numero "))
        numero_2 = int(input("Ingrese un segundo numero "))
        resultado = divicion(numero_1, numero_2)
        print("El resultado de la divicion es ", resultado)
    
    if opcion_seleccionada == 4:
        numero_1 = int(input("ingrese un primer numero "))
        numero_2 = int(input("Ingrese un segundo numero "))
        resultado = multiplicacion(numero_1, numero_2)
        print("El resultado de la multiplicacion es ", resultado)
    
    if opcion_seleccionada == 5:
        numero_1 = int(input("ingrese un primer numero "))
        numero_2 = int(input("Ingrese un segundo numero "))
        resultado = exponencial(numero_1, numero_2)
        print("El resultado de la exponencial es ", resultado)

    if opcion_seleccionada == 6:
        menu_activo = False