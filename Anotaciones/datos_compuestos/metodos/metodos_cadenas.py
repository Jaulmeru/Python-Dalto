string_1 = "Hola Python"
string_2 = "Metodos de cadenas"
string_num = "0123456789"

# dir() Recibe un objeto y devuelve una lista con sus metodos 
#print(dir(string_2))

#Sintaxis de metodos objeto.metodo(parametro)

# .upper() devuelve la cadena en mayusculas
mayusc = string_1.upper() 

# .lower() devuelve la cadena en minusculas
minusc = string_1.lower()

# .capitalize() devuelve la cadena con solo la primera letra en mayuscula
capital = string_1.capitalize()


# .find() Busca una cadena dentro de otra cadena
# si la encuentra retorna su posicion
# si NO la encuentra retorna -1
buscar_find = string_1.find("i")

# .index() Busca una cadena dentro de otra cadena
# si la encuentra retorna su posicion
# si NO la encuentra devuelve una excepcion
buscar_index = string_1.index("l")


# .isnumeric() Devuelve True si la cadena solamente contiene numeros 0 al 1, caso contrario False
numerico = string_num.isnumeric()

# .isalpha() Devuelve True si la cadena solamente contiene letras A a la Z, caso contrario False
alpha = string_1.isalpha()

# .isalnum() Devuelve True si la cadena solamente contiene letras A a la Z o numeros, caso contrario False
alphanum = string_1.isalnum()


# .count() devuelve el numero de veces que una cadena se encuentra dentro de otra cadena
contar_coincidencias = string_1.count("Py")

# len() cuenta cuantos caracteres tiene la cadena
contar_caracteres = len(string_1)


# .startswith() Valida si la cadena comienza con otra cadena. Devuelve Booleano
comienza = string_1.startswith("Hola")

# .endswith() Valida si la cadena comienza con otra cadena. Devuelve Booleano
termina = string_1.endswith("Hola")


# .replace() Reemplaza una parte de la cadena con otra cadena diferente si es que encuentra coincidencia
cadena_reemplazada = string_1.replace("Python", string_2)

# .split() separa una cadena en una lista de cadenas a partir de otra cadena dada
cadena_separada = string_2.split(" ")

print(cadena_separada)