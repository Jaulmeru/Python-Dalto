# Para leer un txt como lectura se deben realizar los pasos abrir - leer - cerrar

#funcion para abrir el archivo
def abrir():
    # open abre la ruta especificada y se agrega el atributo encoding="UTF-8" para utilizar todos los caracteres
    return open("Anotaciones\\archivos\\TXT\\texto.txt",encoding="UTF-8")

print("--------------------------------")

archivo = abrir()
# Informacion de el archivo abierto
print(archivo)
print("--------------------------------")

#Lee todo el archivo
texto = archivo.read()
print(texto)
print("--------------------------------")

# Hay que cerrar el archivo para poder leer de nuevo
archivo.close()
archivo = abrir()

# Lee solamente la primera linea
texto = archivo.readline()
print(texto)

print("--------------------------------")

# Hay que cerrar el archivo para poder leer de nuevo
archivo.close()
archivo = abrir()

# Lee todas las lineas y las devuelve como una lista
texto = archivo.readlines()
print(texto)

# Es necesario siempre dejar cerrado el archivo
archivo.close()