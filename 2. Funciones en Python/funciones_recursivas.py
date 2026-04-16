# Funciónes recursivas con su documentación

def suma_naturales(n):
    """
    Esta función suma todos los naturales desde 1 a n.

    Args:
        n (int): hasta que número sumamos los naturales.

    Returns:
        int: Un entero con el resultado de la suma.
    """
    if n == 1:
        return 1
    else:
        return n + suma_naturales(n-1)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n *factorial(n-1)

def contador(n):
    print (n)
    n += 1
    if n <= 10:
        contador(n)
    
print(suma_naturales(5))
print(factorial(5))
contador(0)