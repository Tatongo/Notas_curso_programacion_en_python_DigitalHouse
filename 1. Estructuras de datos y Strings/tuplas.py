# Tuplas (Colección de elementos inmutables y ordenados)

#   Indices
#Nombre      0(-7)    1(-6)    2(-5)   3(-4)       4(-3)        5(-2)     6(-1)
tupla = ("Manzana", "Banana", "Pera", "Banana", "Mandarina", "Frutilla", "Ananá") # Acepta duplicados

print(tupla[1]) # Devuelve "Banana"
print(tupla[1:4]) # Devuelve ("Banana", "Pera", "Banana")
print(tupla[-5:-2]) # Devuelve ("Pera", "Banana", "Mandarina")

if "Mandarina" in tupla:        # Se puede usar in para comprobar sus elementos.
    print("Si hay Mandarina")

# No se puede hacer una asignacion de un valor en una tupla como normalmente
#   tupla[1] = "Naranja" (no funcionaría)
#
# Se podria copiar la tupla en una lista auxiliar, cambiar lo que necesitamos y volverlo a convertir a tupla con el constructor de la clase list() y tuple()

print(tupla)
lista = list(tupla)
lista[1] = "Naranja"
tupla = tuple(lista)
print(tupla)

# Lo mismo deberiamos hacer si queremos eliminar un elemento o agregarlo en un lugar especifico, aunque si podemos sumar 2 tuplas para tener algo como
# el metodo .extend(), aunque no es exactamente igual.

# Si se puede usar del para eliminar una tupla de la existencia, así como lo hacemos con la lista.
del lista # Cambiariamos lista por tupla

# Las tuplas se pueden desempaquetar igualando la cantidad de variables que tiene una tupla a la tupla en cuestion
(a,b,c,d,e,f,g) = tupla # Se que mi tupla tiene 7 elementos, asi que creo 7 variables y las igualo a la tupla, de esta forma, se le asignara a cada elemento esa variable.

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

(a,b,c,*resto) = tupla  # Con el asterisco separo solo los elementos que necesito de la tupla, y el resto los dejo en una nueva tupla
print(resto)

del a,b,c,d,e,f,g,resto

# Los Bucles funcioan iguales que en las listas
# Bucles:
#   bucle for
for fruta in tupla:
    print(fruta)

#   bucle for con indice disponible
for i in range(len(tupla)):     # len() nos devuelve el largo de la lista en cantidad de elementos, así que hay estamos sacando el rango de ese largo, que seria toda la lista.
    print(tupla[i])
    print(i)

#   bucle while
i=0
while i < len(tupla):
    print(tupla[i])
    i += 1

