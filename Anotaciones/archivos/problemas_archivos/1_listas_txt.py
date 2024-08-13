# De una lista con nombres y una con apellidos, escribir los datos en un txt
nombres,apellidos = ["Vanessa","Ernesto","Carlos"],["Diaz","Rodriguez","Gutierrez"]

with open("Anotaciones\\archivos\\problemas_archivos\\txt\\1.txt","w",encoding="UTF-8") as txt:
    # Mi forma
    #for nombre,apellido in zip(nombres,apellidos):
    #    txt.writelines([nombre," ",apellido,"\n"])

    #En una sola linea
    [txt.writelines(["- ",nombre," ",apellido,"\n"]) for nombre,apellido in zip(nombres,apellidos)]