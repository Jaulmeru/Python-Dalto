# Las funciones lambda son una forma de crear una sola expresion sin necesidad de crear un bloque de funcion completo

# Ejemplo funcion que devuelve el cuadrado de un numero
cuadrado = lambda x: x**2
numero = 3
print(f"El cuadrado de {numero} es {cuadrado(numero)}")

print("")
print("---------------------------")
print("")

# Ejemplo con filter() 
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
pares = filter(lambda num: num % 2 == 0,numeros)
print(list(pares))
