diccionario = {
    'nombre' : "Ulises",
    'apellido' : "Mendoza",
    'edad' : 23,
    'matrimonio' : False 
}

print("")
print("Diccionario")
print(diccionario)
print("")

# .keys() devuelve una clase dict_keys con las claves de todo el diccionario
claves = diccionario.keys()
print("----------------------------")
print("")
print(f".keys()")
print(claves)
print("")

# .get() Devuelve el valor asignado a la cable pasada
# Si no encuentra el valor devuelve none
get = diccionario.get("edad")
print("----------------------------")
print("")
print(f".get()")
print(get)
print("")

# .pop() Elimina un elemento del diccionario a travez de su key
diccionario.pop('matrimonio')
print("----------------------------")
print("")
print(f".pop()")
print(diccionario)
print("")

# .items() devuelve un elemento iterable
items = diccionario.items()
print("----------------------------")
print("")
print(f".items()")
print(items)
print("")


# .clear() Elimina todos los elementos del diccionario, lo deja vacio
diccionario.clear()
print("----------------------------")
print("")
print(f".clear()")
print(diccionario)
print("")