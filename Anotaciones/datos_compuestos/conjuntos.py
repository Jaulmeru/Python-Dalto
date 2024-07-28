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