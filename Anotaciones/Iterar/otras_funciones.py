#       continue
# dentro del bucle si se llega a la declaracion continue, inmediatamente termina la iteracion actual y salta a la siguiente

# Ejemplo. Termina el ciclo antes de imprimir si el numero no es multiplo de 3
for num in range(1,20):
    if num%3 != 0: 
        continue
    print(num)
else:
    print("Termina el ejemplo de continue")
    print("")



#       break
# Si se llega a la declaracion break termina el bucle inmediatamente 
# no continua con las siguientes iteraciones ni ejecuta el else

# Ejemplo. El bucle se termina cuando va en el 11 aunque el rango sea hasta 100
for num in range(100):
    print(num)
    if num == 11:
        break
else:
    print("Termina el ejemplo de break")
    print("")


print("")
print("---------------------------")
print("")

# Para operaciones sensillas se puede hacer un for en una sola linea sacando los valores como lista

# Ejemplo. Sacar los cuadrados de un rango de numeros
cuadrados = [x**2 for x in range(10)]
print(cuadrados)