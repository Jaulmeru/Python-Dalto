# Una forma mas optima para leer es con la estructura with
# Ejecuta un bloque de codigo si se consigue abrir un archivo y al terminar el bloque, se cierra automaticamente
def leer_mi_txt():
    with open("Anotaciones\\archivos\\TXT\\texto.txt",encoding="UTF-8") as archivo:
        texto = archivo.read()
        print(texto)