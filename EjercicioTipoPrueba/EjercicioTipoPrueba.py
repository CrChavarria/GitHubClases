from FuncionesTipoPrueba import *
import numpy as np
menú_ejercicio = True
opcion_seleccionada = 0
precio = 0
numero_producto = 0
nombre_producto = ""
todos_los_productos=[]

while menú_ejercicio:
    print("1.- Grabar ")
    print("2.- Buscar ")
    print("3.- Imprimir ")
    print("4.- Salir ")

    opcion_seleccionada = int(input("Seleccione una opcion: "))
    if opcion_seleccionada == 1:   
        print("Usted seleccionó la opcion 1")
        for n in range (3):
            numero_producto=str(input("inrgese el numero del producto: "))
            nombre_producto=str(input("ingrese el nombre del producto: "))
            precio=int(input("Ingrese Precio del producto: "))
            reultado_validacion = validar_informacion(numero_producto, nombre_producto, precio)
            if reultado_validacion == True:
                un_producto=[numero_producto, nombre_producto, precio]
                todos_los_productos.append(un_producto)
        print(todos_los_productos)

    if opcion_seleccionada == 2:
        print("Usted seleccionó Buscar")


    if opcion_seleccionada == 3:
        print("Usted seleccionó Imprimir")


    if opcion_seleccionada == 4:
        menú_ejercicio = False