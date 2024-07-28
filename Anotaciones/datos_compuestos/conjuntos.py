# Un conjunto es un tipo de variable compuesta por diferentes elementos NO indexados y que NO se pueden repetir entre ellos
# los elementos dentro de este no pueden ser editados individualmente ya que son inmutables
# No es inmutable, por lo que se le pueden agregar valores o eliminarle

#    Formas de crear conjuntos
# Definicion simple
conjunto = {"dato_0","dato_1","dato_2"}
print(f"Definicion simple crea {type(conjunto)}")
# Funcion set(<lista>) 
conjunto = set(["dato_0","dato_1","dato_2"])
print(f"Funcion set(<lista>) crea {type(conjunto)}")

# Un conjunto no puede ser agregado dentro de otro conjunto directamente y a que los valores de un conjunto DEBEN ser inmutables
# Para hacer esto se debe crear un conjunto congelado
subconjunto = frozenset(["dato_sub_0","dato_sub_1"]) 
conjunto = {"dato_0",subconjunto,"dato_1"}
print(conjunto)
print("-------------------------------")

# Teoria de conjuntos 
conjunto_a = {1,2,3,7,11,13} 
conjunto_b = {2,11,13}

# Verificar si b es subconjunto de a
resultado = conjunto_b.issubset(conjunto_a)
resultado = conjunto_b <= conjunto_a
print(f"b es un subconjunto de a?: {resultado}")

# Verificar si b es superconjunto de a
resultado = conjunto_b.issuperset(conjunto_a)
resultado = conjunto_b > conjunto_a
print(f"b es un superconjunto de a?: {resultado}")

# Verificar si no tienen ningun valor en comun
resultado = conjunto_b.isdisjoint(conjunto_a)
print(f"a y b NO comparten ningun valor?: {resultado}")