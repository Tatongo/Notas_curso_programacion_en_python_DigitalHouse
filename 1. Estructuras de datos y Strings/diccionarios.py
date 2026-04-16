# Diccionarios ( Colecciòn no ordenada de pares "Clave:valor")

diccionario = {
    "nombre":"Luis",
    "edad":25,
    "ciudad":"Santa fe",
    "Profesión":"Consultor IT",
    "Tecnologías": ["Python", "Flutter", "Angular", "PHP", "SQL", "Kotlin"]
}

print(diccionario)
print(diccionario["nombre"])

usuario = diccionario.get("nombre")

claves = diccionario.keys()
print (claves)
print(type(claves))

valores = diccionario.values()
print(valores)
print(type(valores))

diccionario["edad"] = 26
diccionario["estado civil"] = "soltero"

#.pop(clave) elimina el par y .popitem() elimina el ultima par de datos
copia_diccionario = dict(diccionario)

for key in diccionario:
    print(diccionario[key])

# Los diccionarios se pueden anidar. Se recorren con un doble for.