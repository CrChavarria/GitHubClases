from FuncionesCalculadora import *
#forma IZI
resultado1 = sumar(5,10)
resultado2 = sumar(90,5)
resultado = resultado1 - resultado2
print(resultado)

#forma senior
print(f"El resultado de {sumar(5,10)} - {sumar(90,5)} = {resta(sumar(5,10), sumar(90,5))}")

