# Definiendo la clase (plantilla)
class Perro:
    # Método Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def ladrar(self):
        return "Guau"