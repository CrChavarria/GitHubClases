#Un arreglo es una estructura de datos, para almacenar datos
#Tiene una diferencia con las listas: Los arreglos solo pueden contener un solo tipo de datos
import numpy as np




#arreglos 1dimension
    #arreglo = np.array([i*3 for i in range(51,102,10)])
    #arreglo = arreglo *3
    #print(arreglo)


#arreglos en 2 dimensiones
#caso tradicional
import numpy as np
matriz = np.array([[0,1,2],[3,4,5]])
for f in range (2):
    for c in range (3):
        print(matriz[f][c])
print("")
print(matriz[1,1])


matriz = np.array([[0,1,2],[3,4,5]])
print(matriz)


#matriz con ceros
import numpy as np
matriz = np.zeros ((3,3))
print(matriz)

#matriz con unos
import numpy as np
matriz = np.ones ((3,3))

#matriz con diagonal principal de 1
import numpy as np
matriz = np.diag ([1,1,1])
print(matriz)





#sumar elementos por fila
import numpy as np
lista = [[1,2,3],[4,5,6]]
matriz = np.array(lista)
print("suma elementos de fila 0: ", matriz[0,:].sum())
print("suma elementos de fila 0: ", matriz[1,:].sum())

#sumar todos los elementos
import numpy as np
lista = [[1,2,3],[4,5,6]]
matriz = np.array(lista)
print(matriz.sum())

#arreglos en dos dimensiones

import numpy as np
matriz = np.array([[0,1,2],[3,4,5]])
matriz.ndim
#esto es igual a 2

import numpy as np
matriz = np.array([[0,1,2],[3,4,5]])
matriz.shape
#esto es igual a 2,3

import numpy as np
matriz = np.array([[0,1,2],[3,4,5]])
matriz.size



#concadenar dos matrizes
import numpy as np
m1 = np.array([[1,2,3],[4,5,6]])
m2 = np.array([[10, 20, 30], [40 ,50, 60]])
print(np.concatenate((m1, m2), axis= 0))
print("")
print("ejercicio 1")
import numpy as np
arreglo = np.random.randint(0, 101, size= (3,3))
matriz = np.array(arreglo)
print(matriz)

print("ejercicio 2")


print("suma ", matriz.sum())
print("minimo ", matriz.min())
print("maximo ", matriz.max())
print("promedio ", matriz.sum()/matriz.size  )