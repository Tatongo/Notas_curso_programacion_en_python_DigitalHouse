# Conjuntos (Colección de elementos mutables y no ordenados)

#   No tienen Indices
conjunto = {"Manzana", "Banana", "Pera", "Banana", "Mandarina", "Frutilla", "Ananá"}

print(conjunto) # Como vemos no acepta duplicados, y se ordena automaicamente por tipo de dato y por tamaño, y elimina directamente esos duplicados.

# True y false (Booleanos) los toma como iguales a los int 1 y 0, asi que esos datos en particular no pueden coexistir en un mismo set.

# Podemos usar el metodo len para saber su longitud.
longitud = len(conjunto)
print(longitud)
# podemos usa el metodo .add() para agregar elementos y .update() `para extender el set con otro set o otra estuctura o eleento como argumento
# tambien se puede utilizar .pop() para eliminar uno aliatoriamente.
# .union(), .update() y |
# .intersection() y & .intersection_update() .diference_update()

for fruta in conjunto:
    print(fruta)

# No se puede recorrer con while, por que no hay indices. Ese for es la unica manera.
#.copy funciona, sin mantener el orden.