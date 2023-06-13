menú = True
opcion_seleccionada = 0
total_objeto = 0
Total_iva = 0
total_compra = 0
print("Tienda imaginaria")
print("1.- Calcular IVA")
print("2.- Descuento")
print("3.- Calcular Imc")
print("4.- Salir")
def Calcular_IVA(valor_pagar):
    Total_iva = 0.19 * valor_pagar
    return Total_iva

opcion_seleccionada = int(input("Ingres lo que desea colocar "))
if opcion_seleccionada == 1:
    valor_pagar = int(input("Ingrese una cantidad: "))
    print("el iva de su compra es ", Calcular_IVA(valor_pagar))

if opcion_seleccionada == 2:
    total_sin_descuento = int(input("Ingrese una cantidad a la que agregar un descuento "))
    porcentaje_descuento = int(input("Ingrese descuento "))
    valor_descuento = porcentaje_descuento * 0.01
    total_descontar = total_sin_descuento * valor_descuento
    print(total_descontar)
    print("valor descuento", valor_descuento)

if opcion_seleccionada == 4:
    menú = False