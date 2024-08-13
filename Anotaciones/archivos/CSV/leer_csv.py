# CSV es un archivo separado por comas que se utiliza como una tabla para almacenar datos
# Se puede utilizar el modulo csv aunque no es lo mas profesional
import csv

with open("Anotaciones\\archivos\\CSV\\archivo.csv",encoding="UTF-8")as archivo:
    datos = csv.reader(archivo)
    for fila in datos:
        print(fila)