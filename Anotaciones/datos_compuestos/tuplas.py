# Las tuplas son un tipo de dato compuesto por uno o mas datos indexados 
# estas son inmutables, por lo que una vez creadas no se pueden cambiar ni los valores internos ni la cantidad de ellos

#    Formas de crear tuplas
# Definicion simple
tupla = ("dato_0","dato_1","dato_2")
print(f"Definicion simple crea {type(tupla)}")
# Definicion sin parentesis
tupla = "dato_0",
print(f"Definicion sin parentesis crea {type(tupla)}")
# Funcion tuple(<lista>) 
tupla = tuple(["dato_0","dato_1","dato_2"])
print(f"Funcion tuple(<lista>) crea {type(tupla)}")

