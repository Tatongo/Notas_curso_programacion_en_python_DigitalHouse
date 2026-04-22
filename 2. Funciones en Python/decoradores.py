# Decorador y wrapper

def decorador(function):
    def envoltorio():
        print("Esta funcionalidad se dispararìa antes de la función que nos pasan por arguemento")
        function()
        print("...")

def saludar():
    print("Hola, estoy saludando")

saludo_decorado = decorador(saludar)

saludo_decorado()