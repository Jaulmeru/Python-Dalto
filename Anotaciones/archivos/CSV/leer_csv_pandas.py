# Pandas es una biblioteca de terceros muy popular para analisis de datos
# para instalarla hay que tener pip instalado e insatalar pandas con el comando en cmd "py -m pip install pandas"

# Ahora si lo podemos importar
import pandas as pd # pd es un nombre comunmente usado para pandas

# Se usa la funcion .read_csv para acceder al archivo y guardar en un dataframe
dataframe = pd.read_csv("Anotaciones\\archivos\\CSV\\archivo.csv")
dataframe2 = pd.read_csv("Anotaciones\\archivos\\CSV\\archivo2.csv")
# Muestra todo el contenido
print("DataFrame completo")
print(dataframe)
print("--------------------------------")

# muestra solo los datos de una columna
print("Una Sola columna")
print(dataframe["Nombre"])
print("--------------------------------")

# Ordenar los datos por una columna de forma ascendente
print("Ordenados por nombre")
print(dataframe.sort_values("Nombre"))
print("--------------------------------")

# .sort_values() Ordenar los datos por una columna de forma desendente
print("Ordenados por nombre")
print(dataframe.sort_values("Nombre",ascending=False))
print("--------------------------------")

# pd.concat(<list>) Concatena una lista de data frames en uno solo. Si alguna columna no coincide, se agrega NaN en los valores vacios
print("Concat")
print(pd.concat([dataframe,dataframe2]))
print("--------------------------------")

# .head(<int>) Devuelve un df con la cantidad de filas indicadas de otro df comenzando de arriba
print("Head")
print(dataframe.head(2))
print("--------------------------------")

# .tail(<int>) Devuelve un df con la cantidad de filas indicadas de otro df comenzando de abaji
print("Tail")
print(dataframe.tail(2))
print("--------------------------------")

# .shape Accede a una tupla con el numero de filas y columnas
print("Filas y columnas")
print(dataframe.shape)
print("--------------------------------")

# .describe() Devuelve informacion estadistica sobre el df
print("Informacion estadistica")
print(dataframe.describe())
print("--------------------------------")

# .loc[<filas>,<nombre_columna>] es una propiedad con la que podemos acceder a valores especificos llamando a la columna por nombre
print("Fila 3 Apellido")
print(dataframe.loc[3,"Apellido"])
print("--------------------------------")

# .iloc[<filas>,<columnas>] es una propiedad con la que podemos acceder a valores especificos llamando a la columna por index
print("Fila 3 Apellido")
print(dataframe.iloc[3,1])
print("--------------------------------")

# En ambas se puede usar slicing para obtener varios datos especificos
print("Filas 1 y 2  Nombre y edad")
print(dataframe.iloc[1:3,::2])
print("--------------------------------")

# Se pueden utilizar tambien condicionales para tomar solo ciertos datos
print("Nombre de los mayores de 23 años")
print(dataframe.loc[dataframe["Edad"]>=23,"Nombre"])
print("--------------------------------")
