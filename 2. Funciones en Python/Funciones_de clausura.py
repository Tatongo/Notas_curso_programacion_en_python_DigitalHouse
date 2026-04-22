def exterior ( x ):
    def interior ( y ):
        return x + y
    return interior

# Creamos una clausura llamando a la función EXTERIOR

clausura = exterior(10) 
# En esta variable se puede pensar que se guardo la función interior con el argumento x,
# y cada vez que llamemos a la variable se va a ejecutar con el nuevo argumento que le pasemos.


# Ahora cuando llamemos a la funciòn clausura va a Recordar el calor que le dimos las veces que queramos.

resultado = clausura(5)

print (resultado, clausura(20))