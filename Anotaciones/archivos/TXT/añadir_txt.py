from abrir_txt_with import leer_mi_txt as leer

# Para hacer una sobrescritura de un archivo hay que abrirlo con el parametro "w"
with open("Anotaciones\\archivos\\TXT\\texto.txt","a",encoding="UTF-8") as archivo:
    # Escribe en el archivo y borra lo demas que habia
    archivo.write("Esto se va a escribir pero no va a borrar lo demas\n")

    # Recibe un iterable y escribe cada elemento en el archivo, para hacer salto de linea se utiliza \n
    archivo.writelines(["Primera linea de writelines añadida","\n","Segunda linea de writelines añadida","\n"])
leer()