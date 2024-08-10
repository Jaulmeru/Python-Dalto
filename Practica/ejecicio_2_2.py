# Crear una funcion que segun un numero dado devuelva una lista con los numeros primos anteriores a este


def encontrar_primos (num):
    primos = []
    for numero in range(3,num+1,2):
        for primo in primos:
            if numero % primo == 0:
                break
        else:
            primos.append(numero)
    primos.insert(0,2)
    primos.insert(0,1)
    return primos



print(encontrar_primos(int(input("Ingresa un numero: "))))
