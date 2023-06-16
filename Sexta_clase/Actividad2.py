menú = True
opcion_seleccionada = 0
total_objeto = 0
Total_iva = 0
total_compra = 0

def Calcular_IVA(valor_pagar):
    Total_iva = 0.19 * valor_pagar
    return Total_iva

def calcular_imc(peso, altura):
    estado="no calculado"
    IMC = peso/altura**2
    if IMC < 18.5:
        estado = "Bajo peso"
    elif IMC >= 18.5 and IMC <24.9:
        estado = "Adecuado"
    elif IMC >= 25 and IMC <=29.9:
        estado = "Sobrepeso"
    elif IMC >=30 and IMC <=34.9:
        estado = "Obecidad Grado I"
    elif IMC >=35 and IMC <=39.9:
        estado = "Obecidad Grado II"
    elif IMC >40:
        estado = "Obecidad Grado III"
    return estado + "IMC = " + str (IMC)




print("Tienda imaginaria")
print("1.- Calcular IVA")
print("2.- Descuento")
print("3.- Calcular Imc")
print("4.- Salir")


opcion_seleccionada = int(input("Ingres lo que desea colocar "))
if opcion_seleccionada == 1:
    valor_pagar = int(input("Ingrese una cantidad: "))
    print("el iva de su compra es ", Calcular_IVA(valor_pagar))


if opcion_seleccionada == 3:
    peso= float(input("Ingrese su peso"))
    altura = float(input("Ingrese su altura"))
    calcular_imc(peso, altura)

if opcion_seleccionada == 4:
    menú = False