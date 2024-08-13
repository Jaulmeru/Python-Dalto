import pandas as pd
df = pd.read_csv("Anotaciones\\archivos\\problemas_archivos\\csv\\archivo.csv")

# Originalmente contiene int
print(type(df["Edad"][0]))
print(df["Edad"][0])
print("")

#Se cambia el tipo de dato
df["Edad"] = df["Edad"].astype(str)

#Ahora contiene str
print(type(df["Edad"][0]))
print(df["Edad"][0])

print("--------------------")
print("Sin cambios")
print(df)
print("--------------------")

# Remplazar datos por otro valor
df["Apellido"].replace("Mendoza","MENDOZA",inplace=True)
print("--------------------")
print("Remplazo")
print(df)
print("--------------------")

# Eliminar filas donde haya valores vacios
df = df.dropna()
print("--------------------")
print("Eliminadas filas con vacios")
print(df)
print("--------------------")

# Eliminiar filas duplicadas
df = df.drop_duplicates()
print("--------------------")
print("Eliminadas filas duplicadas")
print(df)
print("--------------------")

# Guardar los datos en un nuevo csv
df.to_csv("Anotaciones\\archivos\\problemas_archivos\\csv\\archivo_limpio.csv")