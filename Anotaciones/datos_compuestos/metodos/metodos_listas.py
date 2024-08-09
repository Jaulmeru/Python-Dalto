# Creacion de lista con list()   <-- Poco usual
lista = list(["Hola","aprendiendo",260602,False])

# len() Cuenta cuantos elementos deiferentes contiene la lista
len(lista)
print(f"Numero de elementos iniciales: {len(lista)}")

# .append() Agrega un elemento al final de la lista
lista.append("Hola")
print("----------------------------")
print("")
print(f".appen()  -  {len(lista)} elementos")
print(lista)
print("")

# .insert() Agrega un elemento a la lista en el indice indicado
lista.insert(2,"insert()")
print("----------------------------")
print("")
print(f".insert()  -  {len(lista)} elementos")
print(lista)
print("")

# .extend() Agrega varios elementos de otra lista al final de la lista actual
lista.extend([4010471,2024,"Ulises"])
print("----------------------------")
print("")
print(f".extend()  -  {len(lista)} elementos")
print(lista)
print("")

# .pop() Elimina un elemento de la lista en el indice indicado
# Uliliza numeros negativos para eliminas elementos empezando por el ultimo
lista.pop(-1)
print("----------------------------")
print("")
print(f".pop()  -  {len(lista)} elementos")
print(lista)
print("")

# .remove() Elimina un elemento buscandolo por su valor
# Si no lo encuentra, arroja excepcion. Si hay mas de uno, elimina el primero solamente
lista.remove("Hola")
print("----------------------------")
print("")
print(f".remove()  -  {len(lista)} elementos")
print(lista)
print("")

### Pequeña practica eliminando todos los elementos que no son numeros
eliminar = []
for i in range(len(lista)):
    if type(lista[i]) == str :
        eliminar.insert(0,i)
for i in range(len(eliminar)):
    lista.pop(eliminar[i])
eliminar.clear()

print("----------------------------")
print("")
print(f"Strings eliminadas  -  {len(lista)} elementos")
print(lista)
print("")

# .reverse() Voltea los index de los elementos de la lista 
lista.reverse()
print("----------------------------")
print("")
print(f".reverse()  -  {len(lista)} elementos")
print(lista)
print("")

# .sort() Ordena los elementos (Solo numericos) del menor al mayor
# Con el parametro reverse=True se ordenan de mayor a menor
lista.sort()
print("----------------------------")
print("")
print(f".sort()  -  {len(lista)} elementos")
print(lista)
print("")

# .clear() Elimina todos los elementos de una lista, la deja vacia
lista.clear()
print("----------------------------")
print("")
print(f".clear()  -  {len(lista)} elementos")
print(lista)
print("")

