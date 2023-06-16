def grabar (lista_producto):
    #momentaneo
    print("Funcion grabar.........")

def buscar (numero_parte):
    #Momentaneo
    print("buscar numero de parte.........")

def imprimir (reporte):
    #momentaneo
    print("imprimendo........")

def validar_informacion (numero_producto, nombre_producto, precio):
    precio_valido = False
    nombre_valido = False
    numero_valido = False
    if numero_producto.index("-") == 6 and numero_producto.index(" ") == 10:
        numero_valido = True
    else:
        print("numero producto invalido")
    if len(nombre_producto) >=6:
        nombre_valido = True
    else:
        print("nombre invalido")
    if precio > 0:
        precio_valido = True
    else:
        print("precio invalido")

    if precio_valido == True and numero_valido == True and nombre_valido == True:
        return True
    else:
        return False