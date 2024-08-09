# Estructura para crear funciones con parametro, y retorno de varios valores como tupla o lista
def nombre_funcion(parametro):
    mas_uno = parametro + 1
    menos_uno = parametro - 1
    return [mas_uno,parametro,menos_uno]

n1,n2,n3 = nombre_funcion(6)
print(f"{n1} - {n2} - {n3}")

print(type(nombre_funcion)) # Sin ejecutarse type devuelve funcion
print(type(nombre_funcion(6))) # Al ejecutar es manejado como su valor de retorno

