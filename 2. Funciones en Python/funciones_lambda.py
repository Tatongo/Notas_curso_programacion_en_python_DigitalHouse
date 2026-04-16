# Funciones Lambda

def duplicar(num):
    return num*2

print(duplicar(5))

#duplicar_lambda = lambda num:  num * 2

#print(duplicar_lambda(5))

#------------------------------------------

def multiplicar(a,b):
    return a * b

print(multiplicar(5,4))

#multiplicar_lambda = lambda a,b: a*b

#print(multiplicar_lambda(5,4))

#------------------------------------------

def operaciones(operacion):
    if operacion == "suma":
        return lambda x, y: x + y
    elif operacion == "resta":
        return lambda x, y: x - y
    elif operacion == "multiplicación":
        return lambda x, y: x * y
    elif operacion == "divición":
        return lambda x, y: x / y
    else:
        return lambda x, y: "Error"

suma = operaciones("suma")
print(suma(5,7))

prueba = operaciones("pepito")
print(prueba(6,14))

#-----------------------------------------
# Funciones como argumentos

estudiantes = [
    {"nombre":"Juan","edad":20},
    {"nombre":"María","edad":25},
    {"nombre":"Pedro","edad":22}
]

estudiantes_ordenados = sorted(estudiantes, key= lambda x : x['edad'])

print(estudiantes_ordenados)

#----------------------------------------

def aplicar_funcion(func, valor):
    return func(valor)

def cuadrado(x):
    return x * x

def cubo(x):
    return x * x * x

print (aplicar_funcion(cuadrado, 3))
print (aplicar_funcion(cubo, 3))