# Para acceder a un modulo desde algun otro hay que enrutar correctamete
print("--------------------------------")
# Aqui se importa un modulo build-in. No es necesario hacer un enrutamiento por que el path donde se encuentra ya esta guardado
import sys
# para ver todas las rutas guardadas
def mostrar_paths():
    paths = sys.path
    for elem in paths:
        print(elem)

mostrar_paths()
# Al ejecutarse esto se observan varias rutas propias de python donde se ubican los modulos build-in
print("--------------------------------")
# Tambien aparece la ruta ruta donde se encuentra este modulo
# Por eso podemos importar de forma directa si se encuentran en la misma carpeta
import modulo_importado
print("--------------------------------")
# Igualmente si queremos importar de una subcarpeta de nuestro directorio actual se puede hacer 
import subcarpeta.modulo_en_subcarpeta
# Para usar un elemento del modulo hay que poner el nombre completo si no se renombra con as
subcarpeta.modulo_en_subcarpeta.hola()
print("--------------------------------")

# Para usar modulos que no esten en la carpeta actual hay que agregar un directorio al path donde se pueda encontrar
sys.path.append("C:\\Users\\admin\\Desktop\\Cursos\\Python Dalto\\modulos_propios")
mostrar_paths()
print("--------------------------------")
# Ahora se puede importar de la misma forma que antes
from calculadora import calcular_linea as calc
calc()