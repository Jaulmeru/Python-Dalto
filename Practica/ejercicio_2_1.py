# Ingresar una lista de alumnos con edades y ordenar por edades
# El mayor sera el profesor y el menor el asistente

alumnos = [["Luis",26],["Isaac",27],["Josue",20]]

print("Ingresa cuantos alumnos quieras con el siguiente formato:")
print("nombre edad")
print("Escribe 'Fin' cuando hayas acabado de ingresar")

flag = True
while flag:
    user_input = input("- ")
    if user_input.count(" ")>1:
        print("Utiliza un formato valido")
    elif user_input.count(" ") == 1:
        alumno = user_input.split(" ")
        alumno[1] = int(alumno[1]) # type: ignore
        alumnos.insert(0,alumno)
    else:
        user_input = user_input.lower()
        if user_input != "fin":
            print("Para terminar escribe 'Fin'")
        else:
            print("Registro terminado")
            flag = False
print("")
print("---------------------------")
print("")

# Ordena por edad 
alumnos.sort(key= lambda alumno: alumno[1])

print("Lista de alumnos")
for alumno in alumnos:
    nombre, edad = alumno
    print(f"Edad: {edad}  Nombre: {nombre}")

print("")
print("---------------------------")
print("")

profesor = max(alumnos,key=lambda alumno: alumno[1])
asistente = min(alumnos,key=lambda alumno: alumno[1])

print(f"El profesor sera {profesor[0]}")
print(f"El asistente sera {asistente[0]}")