#Sin argumento y sin retorno
def nombre():
    print("Mi nombre es Cristopher")
#Si no se coloca el nombre() nunca aparecerá el print, es como para llamar al print
nombre()

#Sin Argumentos y con retorno
def sumar():
    num1 = 9
    num2 = 10
    return(num1 + num2)

print("la suma es: ", sumar()+ 1)


#Con Argumentos y sin retorno
def sumar2(a, b):
    suma = a+b
    print(f"la suma de los argumentos es: {suma}")

num3 = int(input("ingrese un numero: "))
num4 = int(input("ingrese un segundo numero: "))
sumar2(num3, num4)

#Con Argumentos y con retorno
def sumar3 (a, b):
    suma = a+b
    return(suma)

num5 = int(input("ingrese el primer numero: "))
num6 = int(input("ingrese un segundo numero: "))
print(f"el resultado de la suma es: ", sumar3(num5, num6))


#OTRAS FUNCIONES

def varios_valores(*args):
    for arg in args:
        print(arg)
varios_valores(4.5,"Buenos dias", [1,2,3,4,5])

#OTRAS FUNCIONES

def mostrar_valores():
    return("Buenos dias", 15, [10, 20, 30])
mostrar_valores()