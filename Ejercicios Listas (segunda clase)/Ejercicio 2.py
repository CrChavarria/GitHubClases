Flag = True
numero= 0
lista_numeros=[]
while Flag:
    numero= int(input("ingrese un numero, si ingresa 0 se detiene "))
    if numero == 0:
        Flag = False
    else:
        lista_numeros.append(numero);
lista_numeros.sort();
print(lista_numeros)
print("la lista tiene un largo de: ", len(lista_numeros))
print("la suma de la lista es de: ", sum(lista_numeros))

resultado = sum(lista_numeros)/len(lista_numeros)
print(resultado)