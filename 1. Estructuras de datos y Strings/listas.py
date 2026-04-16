# Listas ( Colección de elementos mutables y ordenados)

#   Indices
#Nombre      0(-7)    1(-6)    2(-5)   3(-4)       4(-3)        5(-2)     6(-1)
lista = ["Manzana", "Banana", "Pera", "Banana", "Mandarina", "Frutilla", "Ananá"]
print(lista)
print(lista[1]) # Devuelve "Banana" ( Segun el indice entre corchetes)
print(lista[2:5]) # Devuelve "['Pera', 'Banana', 'Mandarina']" (Segun el rango entre corchetes, el segundo indice no lo toma)
print(lista[-3:-1]) # Lo mismo de arriba pero al reves

# se puede cambiar un elemento de la lista igualando su indice con el nuevo valor, como cuando definimos una variable
lista[3] = "Palta"
print(lista)

# o incertar nuevos elementos con .insert() o append()
lista.insert(4,"Uvas")
lista.append("Rabano")

# Se pueden unir 2 listas
lista_2 = ["Cebolla", "Tomate", "Papa", "Lechuga"]
lista.extend(lista_2) # como argumento se pueden usar otras listas o tplas, pero no se puede hacer al revez en el caso de las tuplas.
print(lista)

lista_aux = lista.copy() # Copia el contenido de una lista en la nueva que estamos definiendo.

# Se pueden borrar elementos de las listas.
lista.remove("Pera") # Esto elimina el primer elemento que coincide con el argumento.
lista.pop() # Borra el ultimo elemento o si le ponemos un indice como argumento, borra el elemento con ese indice.
print(lista)
lista.clear() # Elimina todos los elementos de la lista, y la deja bacia
print(lista)

lista.extend(lista_aux)
del lista_aux
print(lista)

# Bucles:
#   bucle for
for fruta in lista:
    print(fruta)

#   bucle for con indice disponible
for i in range(len(lista)):     # len() nos devuelve el largo de la lista en cantidad de elementos, así que hay estamos sacando el rango de ese largo, que seria toda la lista.
    print(lista[i])
    print(i)

#   bucle while
i=0
while i < len(lista):
    print(lista[i])
    i += 1

#   Shorthand (Avreviación)
#       bucle for
[print(fruta) for fruta in lista] # Esto hace lo mismo que el bucle for que vimos antes, pero en una sola linea.
lista_con_e = [fruta for fruta in lista if "e" in fruta] # Un for con un if
print(lista_con_e)

# Ordenamiento de listas
#   .sort() y .reverse()
fruta.sort() # Lo ordena alfabeticamete de manera ascendente.
fruta.sort(reverse = True) # Ordena de manera descendente
fruta.sort(key = str.capitalize) # .sort() es ke sensitive, si unas empiezan por mayusculas y otras por minusculas, se rompe el ordenamiento
fruta.reverse() # daa vuelta el orden actual de los elementos.

