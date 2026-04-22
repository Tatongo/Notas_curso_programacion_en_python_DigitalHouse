# Funciones de orden Superior
# Son aquellas que reciben o devuelven una función como argumento
# Map - Toma una funciòn y un iterable como argumento y aplica la función a cada elemento del iterable.
from functools import reduce


def cuadrado(x):
    return x*x

numeros =[1,2,3,4,5]

cuadrados = list(map(cuadrado, numeros))
cuadrados_lambda = list(map(lambda x : x * x, numeros))

print(cuadrados, " = ", cuadrados_lambda)

# Filter - Toma una funciòn que devuelve true or false y devuelve los elementos que reaccionen a ese true.

def es_par(x):
    return x%2 == 0

pares = list(filter(es_par, numeros))
pares_lambda = list(filter(lambda x : x % 2 == 0, numeros))

print (pares, " = ", pares_lambda)
# reduce - Toma una funciòn de 2 argumentos y un iterable y aplica la funciòn de forma acumulativa a los elementos del iterable

def suma (x,y):
    return x + y

sumatoria = reduce(suma, numeros)

print (sumatoria)