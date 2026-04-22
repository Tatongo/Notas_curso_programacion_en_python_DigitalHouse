def division ( dividendo, divisor):
    try:
        resultado = dividendo / divisor
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
        resultado = None
    return resultado

def obtener_entero(texto):
    try:
        entero = int(texto)
    except ValueError:
        print ("No se pudo convertir a entero lo ingresado.")
        entero = None
    return entero

print(division(5,0))
print ("Esto se imprimiría igual si intentamos dividir por 0")

print(obtener_entero("abc"))
print(obtener_entero("123"))