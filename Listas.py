"""Lista = [1, "hola", 3.67, [1,2,3]]
print(Lista[2])

lIsta = [1,2,3,4]
print(lIsta[2])

a = [12, "python", 3.1416]
print(a[0])
print(a[1])
print(a[2])"""

a = [12, "python", 3.1416]
#agrega mas elementos a la lista
a_b = [100, 200]
a.extend(a_b)
#agrega un elemento entremedio de la lista
a.insert(4, 150)
#elimina un elemento en especifico
a.remove("python")
#elimina el ultimo elemento
a.pop()
#da vuelta la lista
a.reverse()
#ordena los elementos de menor a myor
a.sort()
#los ordena de manera inversa
a.sort(reverse=True)
print(a)