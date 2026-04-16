texto = "hoLa muNdo"
texto_espacios = "      Hola Mundo          "
texto_separado = "Python, JavaScripts,Django,React"
lista_a_texto =["Hola"," Mundo"]
numeros = "123456"
letras = "abc"
espacio = " "
repeticion = "Manzana, Naranja, Manzana, Limón"

print("capitalize: ", texto.capitalize()) # Convierte la primera letra en mayúscula (el resto en minúscula)
print("Upper: ", texto.upper()) # Convierte el texto entero en mayúsculas
print("Lower: ", texto.lower()) # Convierte el texto entero en minúsculas
print("Strip: ", texto_espacios.strip()) # Elimina los espacios al comienzo y al final
print("replace: ", texto_espacios.replace("Mundo","Tatos")) # Reemplaza una palabra por otra
print("split: ", texto_separado.split(",")) # Separar texto en ítems de una lista
print("find: ",texto.find("muNdo")) # Junta los ítems de una lista en un string
print("rfind:", repeticion.rfind("Manzana")) # Muestra la última posición donde arranca el texto ingresado
print("index:", texto.index("muNdo")) # Muestra la posición donde arranca el texto ingresado
print("startswith:", texto.startswith("hoLa")) # Indica si comienza o no con la palabra ingresada
print("endswith:", texto.endswith("muNdo")) # Indica si finaliza o no con la palabra ingresada
print("isdigit:", numeros.isdigit()) # Indica si todos los caracteres son números o no (espacios no son números)
print("isalpha:", texto.isalpha()) # Indica si todos los caracteres son letras o no (espacios no son letras)
print("isalnum:", letras.isalnum()) # Indica si todos los caracteres son alfanuméricos o no (espacio no son letras ni números)
print("isspace:", espacio.isspace()) # Indica si el string sólo está hecho de espacios
print("count:", repeticion.count("Manzana")) # Indica cuantas veces se repite la palabra ingresada