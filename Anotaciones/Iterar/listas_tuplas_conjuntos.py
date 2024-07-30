# Iterar es una forma de recorrer cada uno de los elementos de un iterable (tuplas, listas, conjuntos, rangos y mas)
# Los elementos iterables tienen definido el metodo __iter__


# El ejemplo usa la lista que devuelve los metodos y atributos de una tupla vacia
# Esto se puede usar para cualquier lista, tupla o conjunto
atributos_metodos = dir(())
for atributo_metodo in atributos_metodos:
    print(atributo_metodo)

print("")
print("---------------------------")
print("")

# Con zip(<iterable>,<iterable>) se pueden recorrer dos o mas elementos a la vez si estos tienen la misma cantidad de valores
conjunto = {"elemento_1","elemento_2","elemento_3","elemento_4"}
cadena = "hola"
for elemento,letra in zip(conjunto,cadena):
    print(f"{elemento} con letra {letra}")

print("")
print("---------------------------")
print("")

# range(a,b) genera un elemento rango que compone empezando de a hasta b-1
# si se usa solo range(a) genera un rango de 0 hasta a-1
# El rango es utilizado en un for para iterar sobre el pasando por cada numero
for num in range(1,11):
    print(num)

print("")
print("---------------------------")
print("")

# enumerate(<iterable>) generara una tupla de esta forma (index,valor) para cada elemento del iterable
for atributo_metodo_enum in enumerate(atributos_metodos):
    index,valor = atributo_metodo_enum
    print(f"{index} : {valor}")
# se puede utilizar el else en los bucles para que se ejecute algo siempre al terminar el bucle
else:
    print("Final del ultimo bucle")
