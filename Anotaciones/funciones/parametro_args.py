# Crear funcion con una cantidad de parametros indefinidos
# Colocar un parametro con * hace que puedas recibir cualquier cantidad de parametros 
# estos se empaquetaran dentro de la funcion como una unica lista
# Solo se puede usar hasta el final por que tomara todos los parametros ingresados siguientes

def sumar(nombre,*numeros):
    suma = sum(numeros)
    print(f"Hola {nombre} la suma es {suma}")

sumar("Javi",6,8,2,4)