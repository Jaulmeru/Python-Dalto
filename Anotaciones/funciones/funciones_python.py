numeros = (46,65,24,33,9)

# max(<iterable>)
print("")
print(f"Numero maximo: {max(numeros)}")
print(f"Numero minimo: {min(numeros)}")

print("")
print("---------------------------")
print("")

# bool(<dato>) 
    # False -- 0, vacio, False, None
    # True -- numero distinti de 0, true, string
print(f"Funcion bool:   {bool(-1)}")

# all(<iterable>) Evalua cada uno de los elementos, devuelve True solo si todos los elementos son True
print(f"Funcion all:   {all([154,0,True])}")

print("")
print("---------------------------")
print("")

# sum(<iterable>) Suma todos los elementos de un iterable
print(f"Suma con sum():   {sum(numeros)}")