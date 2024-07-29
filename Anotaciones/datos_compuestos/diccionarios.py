# Un diccionario es un tipo de dato que reune varios valores que en lugar de indexarse, se referencian desde otro valor (key)
# Las keys deben ser hasheables por lo que incluso se pueden utilizar tuplas o conjuntos congelados

#    Formas de crear diccionarios
# Definicion simple
diccionario = {
    'nombre' : "Javier",
    'apellido' : "Mendoza",
    'edad' : "23"
}
print(f"Definicion simple crea {type(diccionario)}")
# Funcion dict(key = valor) Permite crear diccionarios vacios
diccionario = dict(nombre="Javier", apellido="Mendoza", edad=23)
print(f"Funcion dict(key = valor) crea {type(diccionario)}")
print("")
print(diccionario)
print("--------------------")


# .fromkeys(<iterable>,<valor>) Crea un diccionario en base a un objeto que se puede recorrer, strings, listas etc como key
# agrega a todas las keys el valor del segundo parametro, por defecto none
diccionario = dict.fromkeys(["nombre","apellido","edad"],"vacio")
print(diccionario)
print(diccionario["nombre"])