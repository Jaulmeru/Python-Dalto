# Los modulos son los diferentes archivos .py con codigo python que se pueden llamar desde otros para organizar mejor el codigo
#   Existen a grandes rasgos 3 tipos 
#   build-in: Ya incorporados en python y no es necesario mas que importar https://docs.python.org/3/library/
#   De terceros: Creados por alguien mas, los descargamos y usamos
#   Propios: Hechos por uno mismo



# Importando todo el modulo math que permite hacer operaciones matematicas y trigonometricas
import math

# Utilizando el metodo .sqrt para obtener la raiz cuadrada de un numero
print(math.sqrt(64))


# Importando un modulo propio con un sobrenombre
import modulo_importado as modulito
# Utilizando el metodo definido por mi en otro modulo
modulito.saludo_1("Javi")

# Importando varias funciones especificas de un modulo para usarlas directamente y colocandoles un sobrenombre
from modulo_importado import saludo_2 as cordial, saludo_3 as grosero

# Utilizando las funciones importadas con su sobrenombre
cordial("Luis")
grosero("Joel")