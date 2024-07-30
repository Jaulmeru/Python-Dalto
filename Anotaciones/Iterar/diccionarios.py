# Iterar diccionarios es de una forma un poco distinta
diccionario = dict(A="arbol",B="blanco",C="cagrejo")

#Iterar de forma sencilla y nos regresa solamente las key
for elemento in diccionario:
    print(elemento)

print("")
print("---------------------------")
print("")

# .items() es la forma para iterar es la siguiente que devuelve una tupla (key,value) 
for tupla in diccionario.items():
    key,value = tupla
    print(f"{key} - {value}")