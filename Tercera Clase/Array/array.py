#1D: 1 dimencion (4,)
#2D: 2 dimenciones (2,3)
#3D: 3 diemnciones (4,3,2)

#a traves de una lista
import numpy
#lista = [1,2,3,4,5]
#type (lista)
#print(lista)


#con datos directamente
#para crear un arreglo o un vector en python usamos la funcion array() de la bibliioteca Numpy. tenemos dos formas de utilizarla
import numpy
#arreglo = numpy.array([1,2,3,4,5])
#print(arreglo)

import numpy as np
#arreglo = np.array([1,2,3,4,5])
#print(arreglo)


#lista = [0,1,2,3,4,5,6,7,8,9,10]
#a=np.array(lista)
#dimension del arreglo "ndim"
#print(a.ndim)
#largo del arreglo
#print(len(a))
#mostrar intervalo
#print(a[1:7])
#print(a[::2])


#lista = [i for i in range (0,101)]
#print(c[0::10])

#a = np.array(lista)
#suma= 1
#for i in range(len(a)):
#    suma = suma + a[i]
#   suma=suma + (a[i]*a[i])
#   print(a[i])
#    print(suma)

#import numpy as np
#numeros = np.arange (0, 1001, 50)
#print(numeros)

#arreglo1 = np.array([1,2,3])
#arreglo2 = arreglo1[:]
#print(arreglo2)
#arreglo2[0] = 100
#print(arreglo2)
#print(arreglo)

#arreglo1 = np.array([1,2,3])
#arreglo2 = arreglo1[:].copy()
#print(arreglo2)
#arreglo2[0] = 100
#print(arreglo2)
#print(arreglo1)

import numpy as np
arreglo = np.array([1,2,3,4,5])
arreglo + 1
print(arreglo)

arreglo = np.ones(10)
arreglo = arreglo + 4999
print(arreglo)