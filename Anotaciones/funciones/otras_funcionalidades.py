# Keyword arguments 
# Puedes ingresarlos en el orden que sea especificando a que argumento se quiere definir valor

def keyword (arg1,arg2,arg3):
    print(f"{arg1} - {arg2} - {arg3}")

keyword(arg2 = 9, arg3 = "hola", arg1 = True)

# Argumentos opcionales

def opcionales(num1,num2,mult = 1):
    return (num1 + num2) * mult

print(f"Sin el ultimo argumento: {opcionales(3,4)}") # Por defecto multiplica por 1
print(f"Con el ultimo argumento: {opcionales(3,4,2)}") # Ahora se multiplica por 2
